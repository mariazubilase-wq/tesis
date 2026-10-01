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
# RNA anotado a mano (libreta), en orden de pocillo; el valor real en pocillo es la MITAD (dilución posterior)
RNA_LIBRETA = {"A01": 3, "A02": 2.6, "A03": 2.92, "A04": 3.36, "A05": 2.42, "A06": 2.1,
               "A07": 2.8, "A08": 3.06, "A09": 2.97, "A10": 3.28, "A11": 2.94, "A12": 2.35}
dom["RNA_uL"] = dom.Well.map(RNA_LIBRETA) / 2
dom["Copias_por_uL_RNA"] = dom.Copias_uL / dom.RNA_uL
dom.to_csv(f"{AQUI}/resultados/1_target_dominante_por_pocillo.csv", index=False, float_format="%.4f")

dom["Excluido_sensib"] = dom.Well == "A06"   # A06 = valor atípico (ver ANALISIS.md)

def resumen(d, m):
    g = d.groupby(["Genotipo", "Condicion"], sort=False)[m]
    r = g.agg(n="count", media="mean", sd=lambda x: x.std(ddof=1) if len(x) > 1 else np.nan,
              minimo="min", maximo="max").reset_index()
    r["pocillos"] = g.apply(lambda x: ",".join(d.loc[x.index, "Well"])).values
    return r

def normaliza(res, d, m):
    out = []
    for gen in ["WT2", "MUT1"]:
        c = res[(res.Genotipo == gen) & (res.Condicion == "c-")].iloc[0]
        for _, r in res[(res.Genotipo == gen) & (res.Condicion != "c-")].iterrows():
            fold = r.media / c.media
            # con n<2 en muestra o control no hay SD válida: no se propaga nada (NaN), no se usa solo la del otro
            rel = np.sqrt((r.sd / r.media) ** 2 + (c.sd / c.media) ** 2) if min(r.n, c.n) > 1 else np.nan
            ind = d[(d.Genotipo == gen) & (d.Condicion == r.Condicion)][m] / c.media
            out.append(dict(Genotipo=gen, Condicion=r.Condicion, media_muestra=r.media,
                            media_control=c.media, n_muestra=r.n, n_control=c.n,
                            fold_vs_control=fold, SD_propagada=fold * rel,
                            SD_propia=r.sd / c.media, SD_control_propia=c.sd / c.media,
                            ratios_replicas=";".join(f"{x:.3f}" for x in ind)))
    return pd.DataFrame(out)

COL = {"WT2": "#1b6ca8", "MUT1": "#d1495b"}
ORD = ["c-", "#13 0,5NM", "#13 1NM"]
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})

def fig_medias(d, m, ylab, titulo, fn):
    fig, axs = plt.subplots(1, 2, figsize=(9, 4.2))
    for ax, gen in zip(axs, ["WT2", "MUT1"]):
        for i, c in enumerate(ORD):
            sub = d[(d.Genotipo == gen) & (d.Condicion == c)]
            s_ = sub[m]
            if s_.empty: continue
            ax.bar(i, s_.mean(), color=COL[gen], alpha=.55, yerr=s_.std(ddof=1) if len(s_) > 1 else None, capsize=4)
            xs = i + np.linspace(-.08, .08, len(s_))
            ax.scatter(xs, s_, color="k", s=18, zorder=3)
            for (_, r), xx in zip(sub.iterrows(), xs):
                ax.annotate(r.Well, (xx, r[m]), fontsize=6, xytext=(3, 3), textcoords="offset points")
        ax.set_xticks(range(3)); ax.set_xticklabels(ORD)
        ax.set_title(f"{gen}  (target {'T2/VIC' if gen=='WT2' else 'T1/FAM'})"); ax.set_ylabel(ylab)
    fig.suptitle(titulo); fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/{fn}", dpi=200); plt.close(fig)

def fig_norm(nor, titulo, fn):
    fig, axs = plt.subplots(1, 2, figsize=(8, 4.2))
    for ax, gen in zip(axs, ["WT2", "MUT1"]):
        ax.bar(0, 1, color="grey", alpha=.6); ax.axhline(1, color="grey", ls="--", lw=.8)
        sub = nor[nor.Genotipo == gen]
        for j, (_, r) in enumerate(sub.iterrows(), 1):
            ax.bar(j, r.fold_vs_control, color=COL[gen], alpha=.7, yerr=r.SD_propagada, capsize=4)
            ratios = [float(v) for v in r.ratios_replicas.split(";")]
            ax.scatter(j + np.linspace(-.08, .08, len(ratios)), ratios, color="k", s=18, zorder=3)
            top = r.fold_vs_control + (0 if np.isnan(r.SD_propagada) else r.SD_propagada)
            et = f"{r.fold_vs_control:.2f}" + ("\n(n=1, sin SD)" if r.n_muestra < 2 else "")
            ax.text(j, top, et, ha="center", va="bottom", fontsize=8)
        ax.set_xticks(range(len(sub) + 1)); ax.set_xticklabels(["c- (=1)"] + list(sub.Condicion))
        ax.set_ylabel("veces vs c-"); ax.set_title(gen)
    fig.suptitle(titulo); fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/{fn}", dpi=200); plt.close(fig)

def fig_norm_propia(nor, titulo, fn):
    """Cada barra con SUS réplicas: valor / media del c- (referencia fija). El c- lleva su propia SD."""
    fig, axs = plt.subplots(1, 2, figsize=(8, 4.2))
    for ax, gen in zip(axs, ["WT2", "MUT1"]):
        sub = nor[nor.Genotipo == gen]
        sdc = sub.SD_control_propia.iloc[0]
        ax.bar(0, 1, color="grey", alpha=.6, yerr=None if np.isnan(sdc) else sdc, capsize=4)
        ax.axhline(1, color="grey", ls="--", lw=.8)
        for j, (_, r) in enumerate(sub.iterrows(), 1):
            sd = r.SD_propia
            ax.bar(j, r.fold_vs_control, color=COL[gen], alpha=.7, yerr=None if np.isnan(sd) else sd, capsize=4)
            ratios = [float(v) for v in r.ratios_replicas.split(";")]
            ax.scatter(j + np.linspace(-.08, .08, len(ratios)), ratios, color="k", s=18, zorder=3)
            top = r.fold_vs_control + (0 if np.isnan(sd) else sd)
            ax.text(j, top, f"{r.fold_vs_control:.2f}" + ("\n(n=1, sin SD)" if r.n_muestra < 2 else ""), ha="center", va="bottom", fontsize=8)
        ctrl = d_ctrl[gen]
        ax.scatter(np.linspace(-.08, .08, len(ctrl)), ctrl, color="k", s=18, zorder=3)
        ax.set_xticks(range(len(sub) + 1)); ax.set_xticklabels(["c- (=1)"] + list(sub.Condicion))
        ax.set_ylabel("veces vs media del c-"); ax.set_title(gen)
    fig.suptitle(titulo); fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/{fn}", dpi=200); plt.close(fig)

# (metrica, sufijo ficheros, etiqueta eje, nombre en título)
METRICAS = [("Copias_uL", "", "copias/µL de reacción", "sin corregir por RNA"),
            ("Copias_por_uL_RNA", "_porRNA", "copias/µL ÷ µL de RNA", "corregido por RNA")]
RES = {}
for m, suf, ylab, tit in METRICAS:
    for sens, d in (("", dom), ("_sin_A06", dom[~dom.Excluido_sensib])):
        res = resumen(d, m); nor = normaliza(res, d, m)
        res.to_csv(f"{AQUI}/resultados/2_medias_replicas{suf}{sens}.csv", index=False, float_format="%.4f")
        nor.to_csv(f"{AQUI}/resultados/3_normalizado_vs_control{suf}{sens}.csv", index=False, float_format="%.4f")
        fig_medias(d, m, ylab, f"Media ± SD de réplicas, {tit}{' · sin A06' if sens else ''}", f"fig3_medias_replicas{suf}{sens}.png")
        fig_norm(nor, f"Normalizado vs c-, {tit}{' · sin A06' if sens else ''}", f"fig4_normalizado{suf}{sens}.png")
        d_ctrl = {g: (d[(d.Genotipo == g) & (d.Condicion == "c-")][m] / res[(res.Genotipo == g) & (res.Condicion == "c-")].media.iloc[0]).values for g in ["WT2", "MUT1"]}
        fig_norm_propia(nor, f"Normalizado vs c-, SD propia de cada grupo, {tit}{' · sin A06' if sens else ''}", f"fig4_normalizado_SDpropia{suf}{sens}.png")
        RES[(m, sens)] = (res, nor)

# Fig 7 y tabla: comparación con / sin A06 (normalizado vs c-, ambas métricas)
filas = []
for (m, sens), (res, nor) in RES.items():
    for _, r in nor.iterrows():
        filas.append(dict(Metrica="por RNA" if m == "Copias_por_uL_RNA" else "sin corregir",
                          A06="sin A06" if sens else "con A06", Genotipo=r.Genotipo,
                          Condicion=r.Condicion, fold=r.fold_vs_control, SD=r.SD_propagada, n=r.n_muestra))
comp = pd.DataFrame(filas)
comp.to_csv(f"{AQUI}/resultados/4_comparacion_con_sin_A06.csv", index=False, float_format="%.4f")
fig, axs = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
for ax, met in zip(axs, ["sin corregir", "por RNA"]):
    sub = comp[(comp.Metrica == met) & (comp.Genotipo == "MUT1")]
    for k, cond in enumerate(["#13 0,5NM", "#13 1NM"]):
        for j, (lab, col) in enumerate([("con A06", "#d1495b"), ("sin A06", "#888888")]):
            r = sub[(sub.Condicion == cond) & (sub.A06 == lab)].iloc[0]
            ax.bar(k + (j - .5) * .38, r.fold, .36, color=col, yerr=None if np.isnan(r.SD) else r.SD, capsize=3,
                   label=lab if k == 0 else None)
            ax.text(k + (j - .5) * .38, r.fold + (0 if np.isnan(r.SD) else r.SD), f"{r.fold:.2f}", ha="center", va="bottom", fontsize=8)
    ax.axhline(1, color="grey", ls="--", lw=.8)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["#13 0,5NM", "#13 1NM"]); ax.set_title(f"MUT1 · {met}")
axs[0].set_ylabel("veces vs mut1 c-"); axs[0].legend(frameon=False)
fig.suptitle("Fig. 7 · MUT1: efecto de incluir o quitar A06 (A06 solo afecta a 1NM)")
fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/fig7_comparacion_con_sin_A06.png", dpi=200); plt.close(fig)

# Fig 6: RNA por pocillo
fig, ax = plt.subplots(figsize=(8, 3.8))
ax.bar(range(len(dom)), dom.RNA_uL, color=[COL[g] for g in dom.Genotipo])
ax.set_xticks(range(len(dom))); ax.set_xticklabels(dom.Well, rotation=60, fontsize=8)
ax.set_ylabel("µL de RNA en pocillo (libreta ÷ 2)"); ax.set_title("Fig. 6 · RNA usado por pocillo")
fig.tight_layout(); fig.savefig(f"{AQUI}/figuras/fig6_RNA_por_pocillo.png", dpi=200); plt.close(fig)

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
for (m, sens), (res, nor) in RES.items():
    print(f"\n== {m} {sens or '(todos)'} =="); print(res.to_string(float_format=lambda v: f"{v:.2f}"))
    print(nor.drop(columns="ratios_replicas").to_string(float_format=lambda v: f"{v:.3f}"))
