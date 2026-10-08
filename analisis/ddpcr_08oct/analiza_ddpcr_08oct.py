#!/usr/bin/env python3
"""Análisis ddPCR 08-oct (MUT1: c-, #13 0,5 y #13 1) — ver ANALISIS.md.

Diseño: nombre = condición + nº de réplica BIOLÓGICA (1 o 2). Pocillos con el mismo nombre = réplicas TÉCNICAS.
 1. Por pocillo se conserva el target con más copias/µL.
 2. Técnicas -> media por réplica biológica. Biológicas -> media ± SD por condición (n = 2).
 3. Normalización contra la media del c- (de las 2 réplicas biológicas).
 4. Además se corrige por el RNA de cada réplica biológica (ng/µL, libreta).
"""
import glob, os, re
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AQUI = os.path.dirname(os.path.abspath(__file__))
XLSX = glob.glob(os.path.join(AQUI, "datos", "*.xlsx"))[0]
CONC = "Conc(copies/µL)"
# RNA de la libreta (ng/µL, ya multiplicado x2 según la libreta). Clave = (condición, nº réplica biológica)
RNA = {("c-", 1): 0.70, ("c-", 2): 0.62, ("#13 1NM", 1): 0.52, ("#13 1NM", 2): 0.80,
       ("#13 0,5NM", 1): 0.52, ("#13 0,5NM", 2): 0.79}
ORD = ["c-", "#13 0,5NM", "#13 1NM"]
COL = {"c-": "#9a9a9a", "#13 0,5NM": "#e08a97", "#13 1NM": "#d1495b"}
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})

raw = pd.read_excel(XLSX).rename(columns={"Sample description 1": "Muestra"})
raw["Muestra"] = raw["Muestra"].fillna("").astype(str).str.strip()

# --- 1. pocillos usados / excluidos ----------------------------------------
def parsea(s):
    m = re.fullmatch(r"mut1 c- (\d)", s, re.I)
    if m: return "c-", int(m[1])
    m = re.fullmatch(r"#13 (1|0,5) (\d)", s)
    if m: return f"#13 {m[1]}NM", int(m[2])
    return None
ok = raw[raw.Muestra.map(lambda s: parsea(s) is not None)].copy()
exc = raw[~raw.index.isin(ok.index)]
excl = exc.pivot(index="Well", columns="Target", values=CONC)
excl.columns = ["Copias/µL T1 (FAM)", "Copias/µL T2 (VIC)"]
excl["Muestra"] = exc.drop_duplicates("Well").set_index("Well").Muestra.replace("", "(sin nombre)")
excl["Gotas"] = exc.drop_duplicates("Well").set_index("Well")["Accepted Droplets"]
excl["Motivo"] = ["Sin nombre, ~0 copias: pocillo vacío/NTC" if m == "(sin nombre)" else
                  "No es MUT1; T2 saturado (todas las gotas positivas)" for m in excl.Muestra]
excl.reset_index().to_csv(f"{AQUI}/resultados/0_pocillos_excluidos.csv", index=False, float_format="%.4f")

idx = ok.groupby("Well")[CONC].idxmax()
dom = ok.loc[idx].copy()
otro = ok.drop(idx).set_index("Well")[CONC]
dom["Conc_otro_target"] = dom.Well.map(otro)
dom["Pct_otro"] = 100 * dom.Conc_otro_target / dom[CONC]
dom[["Condicion", "Rep_bio"]] = dom.Muestra.apply(lambda s: pd.Series(parsea(s)))
dom = dom.rename(columns={CONC: "Copias_uL", "Target": "Target_dominante", "DyeName(s)": "Dye"})
dom["RNA_ngul"] = [RNA[(c, r)] for c, r in zip(dom.Condicion, dom.Rep_bio)]
dom["Copias_por_ng_RNA"] = dom.Copias_uL / dom.RNA_ngul
dom = dom[["Well", "Muestra", "Condicion", "Rep_bio", "Target_dominante", "Dye", "Copias_uL", "Conc_otro_target",
           "Pct_otro", "Accepted Droplets", "Positives", "RNA_ngul", "Copias_por_ng_RNA"]].reset_index(drop=True)
dom.to_csv(f"{AQUI}/resultados/1_target_dominante_por_pocillo.csv", index=False, float_format="%.4f")

METRICAS = [("Copias_uL", "", "copias/µL de reacción", "sin corregir por RNA"),
            ("Copias_por_ng_RNA", "_porRNA", "copias/µL ÷ ng/µL de RNA", "corregido por RNA")]

def bio(d, m):   # técnicas -> réplica biológica
    g = d.groupby(["Condicion", "Rep_bio"], sort=False)[m]
    return g.agg(n_tecnicas="count", media="mean", sd_tecnica=lambda x: x.std(ddof=1) if len(x) > 1 else np.nan
                 ).reset_index().assign(pocillos=g.apply(lambda x: ",".join(d.loc[x.index, "Well"])).values)

def cond(b):     # biológicas -> condición
    g = b.groupby("Condicion", sort=False).media
    r = g.agg(n="count", media="mean", sd="std", minimo="min", maximo="max").reset_index()
    r["Condicion"] = pd.Categorical(r.Condicion, ORD, ordered=True)
    return r.sort_values("Condicion").assign(Condicion=lambda x: x.Condicion.astype(str)).reset_index(drop=True)

def normaliza(c, b):
    ctrl = c[c.Condicion == "c-"].iloc[0]; out = []
    for _, r in c[c.Condicion != "c-"].iterrows():
        fold = r.media / ctrl.media
        rel = np.sqrt((r.sd / r.media) ** 2 + (ctrl.sd / ctrl.media) ** 2)
        ind = b[b.Condicion == r.Condicion].media / ctrl.media
        out.append(dict(Condicion=r.Condicion, media_muestra=r.media, media_control=ctrl.media, n_bio=r.n,
                        fold_vs_control=fold, SD_propagada=fold * rel, SD_propia=r.sd / ctrl.media,
                        SD_control_propia=ctrl.sd / ctrl.media, ratios_replicas_bio=";".join(f"{x:.3f}" for x in ind)))
    return pd.DataFrame(out)

# --- figuras ----------------------------------------------------------------
wells = list(dom.Well)
fig, axs = plt.subplots(1, 1, figsize=(10, 4.5))
pw = ok.pivot(index="Well", columns="Target", values=CONC); nom = ok.drop_duplicates("Well").set_index("Well").Muestra
x = np.arange(len(pw)); w = .4
axs.bar(x - w/2, pw[1], w, label="Target 1 (FAM)", color="#e0a030"); axs.bar(x + w/2, pw[2], w, label="Target 2 (VIC)", color="#4a9b6e")
axs.set_xticks(x); axs.set_xticklabels([f"{i}\n{nom[i]}" for i in pw.index], rotation=60, ha="right", fontsize=7)
axs.set_yscale("log"); axs.set_ylabel("copias/µL"); axs.legend(frameon=False)
axs.set_title("Fig. 1 · Los dos targets en cada pocillo MUT1 (crudo; target 1 domina siempre)")
fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/fig1_targets_por_pocillo.png", dpi=200); plt.close(fig)

fig, axs = plt.subplots(1, 2, figsize=(11, 4.2))
for ax, (m, suf, ylab, tit) in zip(axs, METRICAS):
    ax.bar(range(len(dom)), dom[m], color=[COL[c] for c in dom.Condicion], edgecolor=["k" if r == 2 else "none" for r in dom.Rep_bio])
    ax.set_xticks(range(len(dom))); ax.set_xticklabels([f"{r.Well}\n{r.Condicion} · bio{r.Rep_bio}" for _, r in dom.iterrows()], rotation=70, ha="right", fontsize=6.5)
    ax.set_ylabel(ylab); ax.set_title(tit)
fig.suptitle("Fig. 2 · Target 1 (FAM) por pocillo (borde negro = réplica biológica 2)"); fig.tight_layout()
fig.savefig(f"{AQUI}/figuras/fig2_target_dominante.png", dpi=200); plt.close(fig)

fig, ax = plt.subplots(figsize=(7.5, 3.8))
ax.bar(range(len(dom)), dom["Accepted Droplets"], color=[COL[c] for c in dom.Condicion])
ax.axhline(10000, color="k", ls="--", lw=.8); ax.text(len(dom) - .5, 10300, "10 000", ha="right", fontsize=7)
ax.set_xticks(range(len(dom))); ax.set_xticklabels(dom.Well, rotation=60, fontsize=8)
ax.set_ylabel("gotas aceptadas"); ax.set_title("Fig. 5 · Control de calidad: gotas por pocillo (A09–A12 < 10 000)")
fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/fig5_gotas.png", dpi=200); plt.close(fig)

fig, ax = plt.subplots(figsize=(7.5, 3.8))
r_ = dom.drop_duplicates(["Condicion", "Rep_bio"]); 
ax.bar(range(len(r_)), r_.RNA_ngul, color=[COL[c] for c in r_.Condicion])
ax.set_xticks(range(len(r_))); ax.set_xticklabels([f"{r.Condicion}\nbio{r.Rep_bio}" for _, r in r_.iterrows()], fontsize=8)
ax.set_ylabel("RNA (ng/µL, libreta)"); ax.set_title("Fig. 6 · RNA por réplica biológica")
fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/fig6_RNA_por_replica.png", dpi=200); plt.close(fig)

def fig_tecnicas(d, b, m, ylab, titulo, fn):
    fig, ax = plt.subplots(figsize=(8, 4.2)); pos = 0; ticks = []; labs = []
    for c in ORD:
        for rb in (1, 2):
            s = d[(d.Condicion == c) & (d.Rep_bio == rb)][m]; bb = b[(b.Condicion == c) & (b.Rep_bio == rb)].iloc[0]
            ax.bar(pos, bb.media, color=COL[c], alpha=.7, yerr=bb.sd_tecnica, capsize=3)
            ax.scatter(pos + np.linspace(-.1, .1, len(s)), s, color="k", s=16, zorder=3)
            ticks.append(pos); labs.append(f"{c}\nbio{rb}"); pos += 1
        pos += .6
    ax.set_xticks(ticks); ax.set_xticklabels(labs, fontsize=8); ax.set_ylabel(ylab)
    ax.set_title(titulo); fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/{fn}", dpi=200); plt.close(fig)

def fig_medias(c, b, ylab, titulo, fn):
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    for i, r in c.iterrows():
        ax.bar(i, r.media, color=COL[r.Condicion], alpha=.75, yerr=r.sd, capsize=4)
        v = b[b.Condicion == r.Condicion].media
        ax.scatter(i + np.linspace(-.08, .08, len(v)), v, color="k", s=18, zorder=3)
    ax.set_xticks(range(len(c))); ax.set_xticklabels(c.Condicion); ax.set_ylabel(ylab)
    ax.set_title(titulo); fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/{fn}", dpi=200); plt.close(fig)

def fig_norm(nor, c_sd, titulo, fn, propia):
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    ax.bar(0, 1, color=COL["c-"], alpha=.75, yerr=nor.SD_control_propia.iloc[0] if propia else None, capsize=4)
    ax.axhline(1, color="grey", ls="--", lw=.8)
    for j, (_, r) in enumerate(nor.iterrows(), 1):
        sd = r.SD_propia if propia else r.SD_propagada
        ax.bar(j, r.fold_vs_control, color=COL[r.Condicion], alpha=.8, yerr=sd, capsize=4)
        rat = [float(v) for v in r.ratios_replicas_bio.split(";")]
        ax.scatter(j + np.linspace(-.08, .08, len(rat)), rat, color="k", s=18, zorder=3)
        ax.text(j, r.fold_vs_control + sd, f"{r.fold_vs_control:.2f}", ha="center", va="bottom", fontsize=8)
    if propia:
        ax.scatter(np.linspace(-.08, .08, len(c_sd)), c_sd, color="k", s=18, zorder=3)
    ax.set_xticks(range(len(nor) + 1)); ax.set_xticklabels(["c- (=1)"] + list(nor.Condicion))
    ax.set_ylabel("veces vs media del c-"); ax.set_title(titulo, fontsize=10)
    fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/{fn}", dpi=200); plt.close(fig)

for m, suf, ylab, tit in METRICAS:
    b = bio(dom, m); c = cond(b); nor = normaliza(c, b)
    b.to_csv(f"{AQUI}/resultados/2a_replicas_biologicas{suf}.csv", index=False, float_format="%.4f")
    c.to_csv(f"{AQUI}/resultados/2b_medias_condicion{suf}.csv", index=False, float_format="%.4f")
    nor.to_csv(f"{AQUI}/resultados/3_normalizado_vs_control{suf}.csv", index=False, float_format="%.4f")
    fig_tecnicas(dom, b, m, ylab, f"Fig. 3 · Técnicas (puntos) y media por réplica biológica, {tit}", f"fig3_tecnicas_y_biologicas{suf}.png")
    fig_medias(c, b, ylab, f"Fig. 4 · Media ± SD de las 2 réplicas biológicas, {tit}", f"fig4_medias_condicion{suf}.png")
    cm = b[b.Condicion == "c-"].media.values / c[c.Condicion == "c-"].media.iloc[0]
    fig_norm(nor, cm, f"Normalizado vs c-, SD propagada (incluye c-), {tit}", f"fig7_normalizado_SDpropagada{suf}.png", False)
    fig_norm(nor, cm, f"Normalizado vs c-, SD propia de cada grupo, {tit}", f"fig7_normalizado_SDpropia{suf}.png", True)
    print(f"\n== {m} ==\n", b.to_string(float_format=lambda v: f"{v:.2f}"), "\n", c.to_string(float_format=lambda v: f"{v:.2f}"), "\n",
          nor.drop(columns="ratios_replicas_bio").to_string(float_format=lambda v: f"{v:.3f}"))
print("\nExcluidos:\n", excl.to_string())
print(dom[["Well", "Condicion", "Rep_bio", "Copias_uL", "Pct_otro", "Accepted Droplets"]].to_string(float_format=lambda v: f"{v:.2f}"))
