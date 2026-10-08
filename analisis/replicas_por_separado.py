#!/usr/bin/env python3
"""Cada réplica biológica por separado (E1 = 01-oct, E2 = 08-oct), normalizada de dos formas:
  · vs MEDIA del c-            (referencia común a las dos réplicas)
  · vs c- de LA MISMA réplica  (pareado: réplica 1 con c- 1, réplica 2 con c- 2)
Y 'veces menos' = 1 / (veces vs c-). Salida: replicas_por_separado/*.csv y figuras."""
import os, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
AQUI = os.path.dirname(os.path.abspath(__file__)); OUT = f"{AQUI}/replicas_por_separado"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})

# --- E1: cada pocillo = una réplica biológica; nº de réplica = orden del pocillo dentro de la condición (libreta: «1 1», «1 2») ---
e1 = pd.read_csv(f"{AQUI}/ddpcr_13/resultados/1_target_dominante_por_pocillo.csv")
e1["Rep"] = e1.groupby(["Genotipo", "Condicion"]).Well.rank().astype(int)
e1 = e1.assign(Exp="E1 (01-oct)", Pocillos=e1.Well, RNA=e1.RNA_uL, RNA_u="µL", Cop=e1.Copias_uL, CopRNA=e1.Copias_por_uL_RNA,
               Nota=np.where(e1.Well == "A06", "atípico (¿fallo técnico?)", ""))[
    ["Exp", "Genotipo", "Condicion", "Rep", "Pocillos", "Cop", "RNA", "RNA_u", "CopRNA", "Nota"]]
# --- E2: media de los 2 pocillos técnicos de cada réplica biológica ---
w2 = pd.read_csv(f"{AQUI}/ddpcr_08oct/resultados/1_target_dominante_por_pocillo.csv")
g = w2.groupby(["Condicion", "Rep_bio"], sort=False)
e2 = g.agg(Pocillos=("Well", ",".join), Cop=("Copias_uL", "mean"), RNA=("RNA_ngul", "first"), CopRNA=("Copias_por_ng_RNA", "mean")).reset_index()
e2 = e2.rename(columns={"Rep_bio": "Rep"}).assign(Exp="E2 (08-oct)", Genotipo="MUT1", RNA_u="ng/µL", Nota="")[e1.columns]
d = pd.concat([e1, e2], ignore_index=True)

filas = []
for (exp, gen), s in d.groupby(["Exp", "Genotipo"], sort=False):
    ctrl = s[s.Condicion == "c-"].set_index("Rep")
    for _, r in s.iterrows():
        o = r.to_dict()
        for k, col in (("sin", "Cop"), ("RNA", "CopRNA")):
            o[f"{k}_vs_media"] = r[col] / ctrl[col].mean()
            o[f"{k}_vs_par"] = r[col] / ctrl.loc[r.Rep, col]
            o[f"{k}_menos_media"] = 1 / o[f"{k}_vs_media"]; o[f"{k}_menos_par"] = 1 / o[f"{k}_vs_par"]
        filas.append(o)
T = pd.DataFrame(filas)
T["_o"] = T.Condicion.map({"c-": 0, "#13 0,5NM": 1, "#13 1NM": 2}); T = T.sort_values(["Exp", "Genotipo", "_o", "Rep"]).drop(columns="_o")
T.to_csv(f"{OUT}/replicas_por_separado.csv", index=False, float_format="%.4f")

# --- figuras: 2x2 (filas: sin corregir / por RNA; columnas: vs media c- / vs c- misma réplica) ---
CC = {"bio1": "#4c78a8", "bio2": "#f58518"}
def fig(exp, gen, fn):
    s = T[(T.Exp == exp) & (T.Genotipo == gen)]; conds = ["c-", "#13 0,5NM", "#13 1NM"]
    f, axs = plt.subplots(2, 2, figsize=(9.5, 7), sharey="row")
    for i, (k, nk) in enumerate((("sin", "sin corregir por RNA"), ("RNA", "corregido por RNA"))):
        for j, (m, nm) in enumerate((("media", "vs MEDIA del c-"), ("par", "vs c- de la MISMA réplica"))):
            ax = axs[i, j]; col = f"{k}_vs_{m}"
            for x, c in enumerate(conds):
                v = s[s.Condicion == c].sort_values("Rep")
                for b, (_, r) in enumerate(v.iterrows()):
                    xx = x + (b - .5) * .36
                    ax.bar(xx, r[col], .34, color=CC[f"bio{int(r.Rep)}"], label=f"réplica biológica {int(r.Rep)}" if x == 0 else None)
                    ax.text(xx, r[col], f"{r[col]:.2f}\n(÷{1 / r[col]:.1f})" if c != "c-" or m == "media" else f"{r[col]:.2f}", ha="center", va="bottom", fontsize=7)
                    if r.Nota: ax.text(xx, 0.02, "A06", ha="center", fontsize=7, color="w")
            ax.axhline(1, color="grey", ls="--", lw=.8)
            ax.set_xticks(range(3)); ax.set_xticklabels(conds); ax.set_title(f"{nk} · {nm}", fontsize=9)
            if j == 0: ax.set_ylabel("veces vs c-   (÷ = veces menos)")
    axs[0, 0].legend(frameon=False, fontsize=8)
    f.suptitle(f"{exp} · {gen}: cada réplica biológica por separado"); f.tight_layout(); f.savefig(f"{OUT}/figuras/{fn}", dpi=190); plt.close(f)
fig("E1 (01-oct)", "MUT1", "E1_MUT1.png"); fig("E1 (01-oct)", "WT2", "E1_WT2.png"); fig("E2 (08-oct)", "MUT1", "E2_MUT1.png")
pd.set_option("display.width", 250)
print(T[T.Condicion != "c-"][["Exp", "Genotipo", "Condicion", "Rep", "Pocillos", "sin_vs_media", "sin_vs_par", "RNA_vs_media", "RNA_vs_par", "RNA_menos_par"]].to_string(float_format=lambda v: f"{v:.2f}"))
