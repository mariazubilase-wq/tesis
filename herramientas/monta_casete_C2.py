#!/usr/bin/env python3
"""
Monta el fragmento sintético del constructo 2: promotor H1 + horquilla + terminador,
con los brazos de In-Fusion puestos, listo para pegarlo en el pedido.

Uso:
    python3 monta_casete_C2.py --promotor H1.txt --horquilla sh466-A
    python3 monta_casete_C2.py --promotor H1.txt --horquilla sh466-A \
        --brazo5 NNNNNNNNNNNNNNN --brazo3 NNNNNNNNNNNNNNN

El promotor NO viene incluido a propósito: hay que sacarlo de una fuente real
(GenBank de pSUPER para H1, de pLKO.1 para U6, o la biblioteca del proveedor).
Escribir 230 pb de promotor de memoria es tirar el pedido.
"""
import argparse, os, re, sys, textwrap

AQUI = os.path.dirname(os.path.abspath(__file__))
HORQ = os.path.join(AQUI, "..", "secuencias", "constructos", "horquillas.fa")
COMP = str.maketrans("ACGTacgt", "TGCAtgca")
rc = lambda s: s.translate(COMP)[::-1]

def lee_fasta(ruta):
    d, k = {}, None
    for l in open(ruta):
        l = l.strip()
        if l.startswith(">"): k = l[1:].split()[0]; d[k] = ""
        elif k: d[k] += re.sub(r"[^ACGTacgt]", "", l)
    return d

def limpia(s):
    return re.sub(r"[^ACGT]", "", s.upper())

ap = argparse.ArgumentParser()
ap.add_argument("--promotor", required=True,
                help="fichero (texto o FASTA) con la secuencia del promotor Pol III, "
                     "terminando EXACTAMENTE en el +1 de transcripción")
ap.add_argument("--horquilla", default="sh466-A",
                help="sh466-A (defecto), shSCR, sh466-B, sh466-P10")
ap.add_argument("--brazo5", default="N"*15, help="15 nt del extremo del vector, aguas arriba")
ap.add_argument("--brazo3", default="N"*15, help="15 nt del extremo del vector, aguas abajo")
ap.add_argument("--salida", default=None)
a = ap.parse_args()

prom = limpia(open(a.promotor).read())
horquillas = lee_fasta(HORQ)
clave = a.horquilla + "_horquilla"
if clave not in horquillas:
    sys.exit(f"Horquilla desconocida. Disponibles: "
             f"{[k[:-10] for k in horquillas if k.endswith('_horquilla')]}")
h = horquillas[clave]

if len(a.brazo5) != 15 or len(a.brazo3) != 15:
    sys.exit("Los brazos de In-Fusion son de 15 nt EXACTOS.")

frag = a.brazo5 + prom + h + a.brazo3

print("=" * 74)
print(f"CASETE C2 — {a.horquilla}")
print("=" * 74)
tallo, lazo = h[:21], h[21:27]
print(f"  brazo 5' In-Fusion : {a.brazo5:>15s}   {'PENDIENTE del GenBank' if 'N' in a.brazo5 else 'ok'}")
print(f"  promotor Pol III   : {len(prom):>5d} pb   …{prom[-30:]}")
print(f"  horquilla          : {len(h):>5d} nt")
print(f"     tallo sentido   : {tallo}")
print(f"     lazo            : {lazo}")
print(f"     tallo antisent. : {h[27:48]}   (complemento inverso: {rc(tallo) == h[27:48]})")
print(f"     terminador      : {h[48:]}")
print(f"  brazo 3' In-Fusion : {a.brazo3:>15s}   {'PENDIENTE del GenBank' if 'N' in a.brazo3 else 'ok'}")
print(f"  TOTAL              : {len(frag)} pb")
print()

# avisos que importan al encargarlo
print("COMPROBACIONES:")
tt = [m.start() for m in re.finditer("TTTT", prom + h[:48])]
print(f"  corridas de 4+ T antes del terminador : "
      f"{'ninguna ✔' if not tt else f'{len(tt)} en {tt} — Pol III terminaría antes ✗'}")
print(f"  el promotor acaba justo antes del tallo: "
      f"comprueba a mano que {prom[-6:]} es el +1")
gc = 100 * sum(frag.count(b) for b in "GC") / len(frag)
print(f"  GC del fragmento                      : {gc:.1f}%")
print(f"  horquilla de 21 pb                    : la marcará el proveedor como "
      f"'secuencia compleja'. Es normal; pídelo igual.")

if a.salida:
    with open(a.salida, "w") as fh:
        fh.write(f">casete_C2_{a.horquilla}_{len(frag)}pb\n")
        fh.write("\n".join(textwrap.wrap(frag, 60)) + "\n")
    print(f"\nEscrito en {a.salida}")
else:
    print("\nFRAGMENTO COMPLETO:")
    print("\n".join(textwrap.wrap(frag, 60)))
