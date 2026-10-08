#!/usr/bin/env python3
"""WT2 #13 1NM (E1, 01-oct) y MUT1 #13 1NM (E2, 08-oct), corregido por RNA, veces vs media del c-,
barras = media de las réplicas biológicas ± SD propia; puntos = cada réplica."""
import os, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
AQUI = os.path.dirname(os.path.abspath(__file__))
t = pd.read_csv(f"{AQUI}/replicas_por_separado/replicas_por_separado.csv")
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
fig, axs = plt.subplots(1, 2, figsize=(8, 4.6), sharey=True)
for ax, (exp, gen, col, tit) in zip(axs, [("E1 (01-oct)", "WT2", "#1b6ca8", "WT2 · 01-oct"), ("E2 (08-oct)", "MUT1", "#d1495b", "MUT1 · 08-oct")]):
    s = t[(t.Exp == exp) & (t.Genotipo == gen)]
    for x, c in enumerate(["c-", "#13 1NM"]):
        v = s[s.Condicion == c].RNA_vs_media.values
        ax.bar(x, v.mean(), .6, color="#b0b0b0" if c == "c-" else col, alpha=.85, yerr=v.std(ddof=1), capsize=5)
        ax.scatter(x + np.array([-.1, .1]), v, color="k", s=24, zorder=3)
        ax.text(x, v.mean() + v.std(ddof=1) + .03, f"{v.mean():.2f}", ha="center", fontsize=10)
    ax.axhline(1, color="grey", ls="--", lw=.8)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["c-", "#13 1NM"]); ax.set_title(tit)
axs[0].set_ylabel("veces vs media del c-\n(corregido por RNA)")
fig.suptitle("#13 1NM: expresión relativa al control negativo", fontsize=11); fig.tight_layout()
fig.savefig(f"{AQUI}/grafica_WT2_01oct_MUT1_08oct_1NM.png", dpi=200)
