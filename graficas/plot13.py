import sys, statistics as st, openpyxl
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
f15 = sys.argv[1]; out = sys.argv[2]
ws = openpyxl.load_workbook(f15, data_only=True)["Hoja2"]
rows = [(r[0].strip(), r[2]) for r in ws.iter_rows(values_only=True) if r[0] and r[2]]
# 'WT2 #6 13 1' es la réplica 1 de WT2 #13 5 nM (así la agrupa la propia hoja)
rows = [("WT2 #13 5 1" if n == "WT2 #6 13 1" else n, v) for n, v in rows]
def bio(name):  # media de los pocillos técnicos de una réplica biológica
    return st.mean(v for n, v in rows if n == name)
rep = {}  # (genotipo, conc) -> lista de (exp, ratio)
for g in ("WT2", "MUT1"):
    for c in ("5", "10"):
        ctrl = st.mean(v for n, v in rows if n.startswith(f"{g} C- {c} "))
        rep[(g, c)] = [("15-sep", bio(f"{g} #13 {c} {b}") / ctrl) for b in (1, 2)]
# 0,5 y 1 nM: ratios por réplica corregidos por RNA (ddpcr_resultados.xlsx)
rep[("WT2", "0,5")] = [("01-oct", 1.222), ("01-oct", 1.081)]
rep[("WT2", "1")]   = [("01-oct", 1.044), ("01-oct", 0.906)]
rep[("MUT1", "0,5")] = [("01-oct", 0.747), ("01-oct", 0.424), ("08-oct", 0.787), ("08-oct", 0.658)]
rep[("MUT1", "1")]   = [("01-oct", 0.523), ("08-oct", 0.407), ("08-oct", 0.685)]  # sin A06
concs = ["0,5", "1", "5", "10"]
col = {"WT2": "#2a78d6", "MUT1": "#eb6834"}
mk = {"01-oct": "o", "08-oct": "s", "15-sep": "D"}
fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=200)
w = 0.36
print("Genotipo\tConc\tn\t% KRT10 vs c-\tSD\t% silenciamiento")
for i, g in enumerate(("WT2", "MUT1")):
    for j, c in enumerate(concs):
        vals = [r * 100 for _, r in rep[(g, c)]]
        m = st.mean(vals); sd = st.stdev(vals)
        x = j + (i - 0.5) * w
        ax.bar(x, m, w - 0.04, color=col[g], alpha=0.85, label=g if j == 0 else None, zorder=2)
        ax.errorbar(x, m, sd, color="#333", capsize=3, lw=1, zorder=3)
        for k, (e, r) in enumerate(rep[(g, c)]):
            ax.scatter(x + (k - (len(vals)-1)/2) * 0.05, r * 100, marker=mk[e], s=22,
                       facecolor="white", edgecolor="#222", lw=0.9, zorder=4)
        ax.text(x, m + sd + 3, f"{m:.0f}%", ha="center", fontsize=8, color="#333")
        print(f"{g}\t{c} nM\t{len(vals)}\t{m:.1f}\t{sd:.1f}\t{100-m:.0f}%")
ax.axhline(100, color="#888", ls="--", lw=1, zorder=1)
ax.set_xticks(range(4), [f"{c} nM" for c in concs])
ax.set_ylabel("ARNm KRT10 (% vs control negativo)")
ax.set_title("Silenciamiento con siRNA #13 (ddPCR, corregido por RNA)", fontsize=11)
ax.set_ylim(0, 140)
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.grid(axis="y", color="#e5e5e5", zorder=0)
h1, l1 = ax.get_legend_handles_labels()
from matplotlib.lines import Line2D
h2 = [Line2D([], [], marker=mk[e], ls="", mfc="white", mec="#222", label=f"réplica {e}") for e in mk]
ax.legend(h1 + h2, l1 + [h.get_label() for h in h2], fontsize=8, frameon=False, ncol=2, loc="upper right")
fig.text(0.01, 0.01, "Barras: media ± SD de réplicas biológicas. 1 nM MUT1 sin A06 (atípico). 0,5–1 nM y 5–10 nM son experimentos distintos.",
         fontsize=6.5, color="#555")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(out)
