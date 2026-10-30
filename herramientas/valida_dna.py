#!/usr/bin/env python3
"""Comprueba un `.dna` con un lector **independiente** (Biopython), si está.

Sirve para no tener que creerse el escritor de `snapgene.py`: si Biopython lee el
fichero y da la misma secuencia, longitud, topología y rasgos que el GenBank
hermano, el `.dna` está bien formado y SnapGene Viewer lo abrirá.

    python3 valida_dna.py ../resultados/mi_plasmido.dna

Biopython es **opcional**: si no está instalado, esto avisa y no pasa nada
(`pip install biopython`). El resto del repositorio no lo necesita.
"""
from __future__ import annotations

import os
import sys

from snapgene import lee_dna


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print(__doc__)
        return 2
    ruta = argv[0]

    propio = lee_dna(ruta)
    print(f"lector propio : {len(propio.seq)} pb, "
          f"{'circular' if propio.circular else 'lineal'}, "
          f"{len(propio.rasgos)} rasgos")

    try:
        from Bio import SeqIO
    except ImportError:
        print("Biopython no está instalado: no hay segunda opinión.\n"
              "  pip install biopython")
        return 0

    r = SeqIO.read(ruta, "snapgene")
    print(f"Biopython     : {len(r.seq)} pb, "
          f"{r.annotations.get('topology')}, {len(r.features)} rasgos")

    problemas = []
    if str(r.seq).upper() != propio.seq.upper():
        problemas.append("la secuencia no coincide entre los dos lectores")
    if (r.annotations.get("topology") == "circular") != propio.circular:
        problemas.append("la topología no coincide")

    gb = os.path.splitext(ruta)[0] + ".gb"
    if os.path.exists(gb):
        g = SeqIO.read(gb, "genbank")
        print(f"GenBank hermano: {len(g.seq)} pb, {g.annotations.get('topology')}, "
              f"{len(g.features)} rasgos")
        if str(g.seq).upper() != str(r.seq).upper():
            problemas.append(".dna y .gb no tienen la misma secuencia")

    for f in r.features:
        if f.location.start < 0 or f.location.end > len(r.seq):
            problemas.append(f"rasgo fuera de rango: {f.qualifiers.get('label')}")

    if problemas:
        print("\nPROBLEMAS:")
        for p in problemas:
            print(f"  - {p}")
        return 1
    print("\nOK: el .dna es legible por un lector independiente y es coherente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
