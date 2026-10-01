#!/usr/bin/env python3
"""Análisis ddPCR #13 (WT2 / MUT1, 1NM y 0,5NM) — ver ANALISIS.md.

Pasos:
 1. Por pocillo se conserva el target con más copias/µL (el otro es señal cruzada/ruido).
 2. Se promedian las réplicas biológicas (pocillos) de cada muestra.
 3. Cada muestra se normaliza contra el control negativo de su genotipo (wt2 c- / mut1 c-).
"""
import glob, os
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AQUI = os.path.dirname(os.path.abspath(__file__))
XLSX = glob.glob(os.path.join(AQUI, "datos", "*.xlsx"))[0]
CONC = "Conc(copies/µL)"

df = pd.read_excel(XLSX)
df = df.rename(columns={"Sample description 1": "Muestra"})
df["Muestra"] = df["Muestra"].fillna("").astype(str).str.strip()

# --- 1. target dominante por pocillo -------------------------------------
sin_nombre = df[df.Muestra == ""]["Well"].unique().tolist()
df = df[df.Muestra != ""]                      # B01: sin nombre -> fuera
idx = df.groupby("Well")[CONC].idxmax()
dom = df.loc[idx].copy()
dom["Dye"] = dom["DyeName(s)"]
otro = df.drop(idx).set_index("Well")[CONC]
dom["Conc_otro_target"] = dom["Well"].map(otro)
dom["Pct_otro"] = 100 * dom["Conc_otro_target"] / dom[CONC]

def norm_nombre(s):
    s = s.upper().replace(",", ".")
    if "WT2" in s: g = "WT2"
    elif "MUT1" in s: g = "MUT1"
    else: raise ValueError(s)
    if "C-" in s: c = "c-"
    elif "0.5" in s: c = "#13 0,5NM"
    else: c = "#13 1NM"
    return g, c
dom[["Genotipo", "Condicion"]] = dom.Muestra.apply(lambda s: pd.Series(norm_nombre(s)))
dom = dom.rename(columns={CONC: "Copias_uL", "Target": "Target_dominante"})
cols = ["Well", "Muestra", "Genotipo", "Condicion", "Target_dominante", "Dye",
        "Copias_uL", "Conc_otro_target", "Pct_otro", "Accepted Droplets", "Positives"]
dom = dom[cols].reset_index(drop=True)
dom.to_csv(f"{AQUI}/resultados/1_target_dominante_por_pocillo.csv", index=False, float_format="%.4f")

# --- 2. medias de réplicas ------------------------------------------------
def resumen(d):
    g = d.groupby(["Genotipo", "Condicion"], sort=False).Copias_uL
    r = g.agg(n="count", media="mean", sd=lambda x: x.std(ddof=1) if len(x) > 1 else np.nan,
              minimo="min", maximo="max").reset_index()
    r["pocillos"] = g.apply(lambda x: ",".join(d.loc[x.index, "Well"])).values
    return r
res_all = resumen(dom)

# A06 es un valor atípico claro (ver ANALISIS.md): se da el análisis con y sin él
dom["Excluido_sensib"] = dom.Well == "A06"
res_sin = resumen(dom[~dom.Excluido_sensib])
res_all.to_csv(f"{AQUI}/resultados/2_medias_replicas.csv", index=False, float_format="%.4f")
res_sin.to_csv(f"{AQUI}/resultados/2b_medias_replicas_sin_A06.csv", index=False, float_format="%.4f")

# --- 3. normalización contra c- ------------------------------------------
def normaliza(res, d):
    out = []
    for gen in ["WT2", "MUT1"]:
        c = res[(res.Genotipo == gen) & (res.Condicion == "c-")].iloc[0]
        for _, r in res[(res.Genotipo == gen) & (res.Condicion != "c-")].iterrows():
            fold = r.media / c.media
            # error relativo propagado (SD/media de cada término, cociente de medias)
            rel = np.sqrt(np.nansum([(r.sd / r.media) ** 2, (c.sd / c.media) ** 2]))
            # ratio individual de cada réplica vs media del control
            ind = d[(d.Genotipo == gen) & (d.Condicion == r.Condicion)].Copias_uL / c.media
            out.append(dict(Genotipo=gen, Condicion=r.Condicion, media_muestra=r.media,
                            media_control=c.media, n_muestra=r.n, n_control=c.n,
                            fold_vs_control=fold, SD_propagada=fold * rel,
                            ratios_replicas=";".join(f"{x:.3f}" for x in ind)))
    return pd.DataFrame(out)
nor_all = normaliza(res_all, dom)
nor_sin = normaliza(res_sin, dom[~dom.Excluido_sensib])
nor_all.to_csv(f"{AQUI}/resultados/3_normalizado_vs_control.csv", index=False, float_format="%.4f")
nor_sin.to_csv(f"{AQUI}/resultados/3b_normalizado_vs_control_sin_A06.csv", index=False, float_format="%.4f")

# --- gráficas --------------------------------------------------------------
COL = {"WT2": "#1b6ca8", "MUT1": "#d1495b"}
ORD = ["c-", "#13 0,5NM", "#13 1NM"]
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})

# Fig 1: ambos targets por pocillo
raw = pd.read_excel(XLSX).rename(columns={"Sample description 1": "Muestra"})
raw = raw[raw.Muestra.notna() & (raw.Muestra.astype(str).str.strip() != "")]
pw = raw.pivot(index="Well", columns="Target", values=CONC)
nom = raw.drop_duplicates("Well").set_index("Well").Muestra
fig, ax = plt.subplots(figsize=(10, 4.5))
x = np.arange(len(pw)); w = .4
ax.bar(x - w/2, pw[1], w, label="Target 1 (FAM)", color="#e0a030")
ax.bar(x + w/2, pw[2], w, label="Target 2 (VIC)", color="#4a9b6e")
ax.set_xticks(x); ax.set_xticklabels([f"{i}\n{nom[i]}" for i in pw.index], rotation=60, ha="right", fontsize=7)
ax.set_ylabel("copias/µL"); ax.set_title("Fig. 1 · Los dos targets en cada pocillo (datos crudos)")
ax.set_yscale("log"); ax.legend(frameon=False)
fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/fig1_targets_por_pocillo.png", dpi=200); plt.close(fig)

# Fig 2: target dominante por pocillo
fig, ax = plt.subplots(figsize=(10, 4.5))
ax.bar(range(len(dom)), dom.Copias_uL, color=[COL[g] for g in dom.Genotipo])
for i, r in dom.iterrows():
    ax.text(i, r.Copias_uL, f"T{r.Target_dominante}", ha="center", va="bottom", fontsize=7)
ax.set_xticks(range(len(dom))); ax.set_xticklabels([f"{r.Well}\n{r.Muestra}" for _, r in dom.iterrows()], rotation=60, ha="right", fontsize=7)
ax.set_ylabel("copias/µL"); ax.set_title("Fig. 2 · Target con más copias por pocillo (WT2 → T2/VIC; MUT1 → T1/FAM)")
fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/fig2_target_dominante.png", dpi=200); plt.close(fig)

# Fig 3 y 4: medias con réplicas
def fig_medias(res, d, titulo, fn, norm=None):
    fig, axs = plt.subplots(1, 2, figsize=(9, 4.2))
    for ax, gen in zip(axs, ["WT2", "MUT1"]):
        for i, c in enumerate(ORD):
            s = d[(d.Genotipo == gen) & (d.Condicion == c)].Copias_uL
            if s.empty: continue
            ax.bar(i, s.mean(), color=COL[gen], alpha=.55, yerr=s.std(ddof=1) if len(s) > 1 else None, capsize=4)
            ax.scatter([i]*len(s) + np.linspace(-.08, .08, len(s)), s, color="k", s=18, zorder=3)
            for (_, r), xx in zip(d[(d.Genotipo == gen) & (d.Condicion == c)].iterrows(), [i - .08, i + .08]):
                ax.annotate(r.Well, (xx, r.Copias_uL), fontsize=6, xytext=(3, 3), textcoords="offset points")
        ax.set_xticks(range(3)); ax.set_xticklabels(ORD)
        ax.set_title(f"{gen}  (target {'T2/VIC' if gen=='WT2' else 'T1/FAM'})"); ax.set_ylabel("copias/µL")
    fig.suptitle(titulo); fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/{fn}", dpi=200); plt.close(fig)
fig_medias(res_all, dom, "Fig. 3 · Media ± SD de réplicas (puntos = pocillos), todos los datos", "fig3_medias_replicas.png")
fig_medias(res_sin, dom[~dom.Excluido_sensib], "Fig. 3b · Igual, sin A06 (atípico)", "fig3b_medias_replicas_sin_A06.png")

# Fig 4: normalizado
def fig_norm(nor, d, titulo, fn):
    fig, axs = plt.subplots(1, 2, figsize=(8, 4.2))
    for ax, gen in zip(axs, ["WT2", "MUT1"]):
        ax.bar(0, 1, color="grey", alpha=.6)
        ax.axhline(1, color="grey", ls="--", lw=.8)
        sub = nor[nor.Genotipo == gen]
        for j, (_, r) in enumerate(sub.iterrows(), 1):
            ax.bar(j, r.fold_vs_control, color=COL[gen], alpha=.7, yerr=r.SD_propagada, capsize=4)
            ratios = [float(v) for v in r.ratios_replicas.split(";")]
            ax.scatter(j + np.linspace(-.08, .08, len(ratios)), ratios, color="k", s=18, zorder=3)
            ax.text(j, r.fold_vs_control + (r.SD_propagada if not np.isnan(r.SD_propagada) else 0), f"{r.fold_vs_control:.2f}", ha="center", va="bottom", fontsize=8)
        ax.set_xticks(range(len(sub) + 1)); ax.set_xticklabels(["c- (=1)"] + list(sub.Condicion))
        ax.set_ylabel("veces vs c- (copias/µL)"); ax.set_title(gen)
    fig.suptitle(titulo); fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/{fn}", dpi=200); plt.close(fig)
fig_norm(nor_all, dom, "Fig. 4 · Normalizado contra el control negativo (todos los datos)", "fig4_normalizado.png")
fig_norm(nor_sin, dom[~dom.Excluido_sensib], "Fig. 4b · Normalizado contra c-, sin A06", "fig4b_normalizado_sin_A06.png")

# Fig 5: control de calidad (gotas)
fig, ax = plt.subplots(figsize=(8, 3.8))
ax.bar(range(len(dom)), dom["Accepted Droplets"], color=[COL[g] for g in dom.Genotipo])
ax.axhline(10000, color="k", ls="--", lw=.8); ax.text(len(dom) - .5, 10200, "10 000", ha="right", fontsize=7)
ax.set_xticks(range(len(dom))); ax.set_xticklabels(dom.Well, rotation=60, fontsize=8)
ax.set_ylabel("gotas aceptadas"); ax.set_title("Fig. 5 · Control de calidad: gotas por pocillo")
fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/fig5_gotas.png", dpi=200); plt.close(fig)

print("Pocillos sin nombre excluidos:", sin_nombre)
pd.set_option("display.width", 220)
print(dom.drop(columns="Excluido_sensib").to_string(float_format=lambda v: f"{v:.2f}"))
print(); print(res_all.to_string(float_format=lambda v: f"{v:.2f}"))
print(); print(nor_all.drop(columns="ratios_replicas").to_string(float_format=lambda v: f"{v:.3f}"))
print(); print(nor_sin.drop(columns="ratios_replicas").to_string(float_format=lambda v: f"{v:.3f}"))
