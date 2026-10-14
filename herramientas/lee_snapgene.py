#!/usr/bin/env python3
"""
Lector de ficheros SnapGene (.dna) — secuencia, rasgos y mapa de dianas.

SnapGene guarda el fichero como una serie de bloques:

    [1 byte: tipo][4 bytes: longitud, big-endian][carga util]

Sólo nos interesan dos tipos:

    tipo 0  → secuencia (el primer byte de la carga son banderas: topologia, etc.)
    tipo 10 → XML con los rasgos anotados (<Feature name=... range=...>)

No hay dependencias externas y no accede a internet.

Uso:

    python3 lee_snapgene.py fichero.dna                    # resumen + rasgos
    python3 lee_snapgene.py fichero.dna --fasta salida.fa  # exporta la secuencia
    python3 lee_snapgene.py fichero.dna --dianas           # dianas unicas
    python3 lee_snapgene.py fichero.dna --ventana 817 834  # dianas en un tramo
"""

import argparse
import re
import struct
import sys

COMPL = {"A": "T", "T": "A", "G": "C", "C": "G", "N": "N"}


def rc(s: str) -> str:
    """Hebra complementaria invertida."""
    return "".join(COMPL.get(c, "N") for c in s.upper()[::-1])


# Panel de enzimas de uso corriente. Sólo dianas sin degenerar: una diana con
# W/R/Y daria falsos negativos silenciosos, y en un diseno de clonaje eso es
# peor que no mirarla.
ENZIMAS = {
    "AatII": "GACGTC", "AflII": "CTTAAG", "AgeI": "ACCGGT", "ApaI": "GGGCCC",
    "AscI": "GGCGCGCC", "AsiSI": "GCGATCGC", "AvrII": "CCTAGG", "BamHI": "GGATCC",
    "BglII": "AGATCT", "BsiWI": "CGTACG", "BsrGI": "TGTACA", "BstBI": "TTCGAA",
    "BstZ17I": "GTATAC", "ClaI": "ATCGAT", "EcoRI": "GAATTC", "EcoRV": "GATATC",
    "FseI": "GGCCGGCC", "HindIII": "AAGCTT", "HpaI": "GTTAAC", "KpnI": "GGTACC",
    "MluI": "ACGCGT", "NcoI": "CCATGG", "NdeI": "CATATG", "NheI": "GCTAGC",
    "NotI": "GCGGCCGC", "NruI": "TCGCGA", "PacI": "TTAATTAA", "PmeI": "GTTTAAAC",
    "PmlI": "CACGTG", "PsiI": "TTATAA", "PstI": "CTGCAG", "PvuI": "CGATCG",
    "SacI": "GAGCTC", "SacII": "CCGCGG", "SalI": "GTCGAC", "SbfI": "CCTGCAGG",
    "SnaBI": "TACGTA", "SpeI": "ACTAGT", "SphI": "GCATGC", "StuI": "AGGCCT",
    "SwaI": "ATTTAAAT", "XbaI": "TCTAGA", "XhoI": "CTCGAG",
    "I-SceI": "TAGGGATAACAGGGTAAT",
}


def lee(path):
    """Devuelve (secuencia, [(nombre, inicio, fin)]) en coordenadas 1-based."""
    with open(path, "rb") as fh:
        data = fh.read()

    seq, rasgos = None, []
    i = 0
    while i < len(data) - 5:
        tipo = data[i]
        (longitud,) = struct.unpack(">I", data[i + 1:i + 5])
        if i + 5 + longitud > len(data):
            break
        carga = data[i + 5:i + 5 + longitud]

        if tipo == 0:
            seq = carga[1:].decode("ascii", "replace").upper()
        elif tipo == 10:
            xml = carga.decode("utf-8", "replace")
            for m in re.finditer(
                r'<Feature [^>]*name="([^"]*)"[^>]*>(.*?)</Feature>', xml, re.S
            ):
                tramos = re.findall(r'range="(\d+)-(\d+)"', m.group(2))
                if tramos:
                    rasgos.append(
                        (m.group(1), int(tramos[0][0]), int(tramos[-1][1]))
                    )
        i += 5 + longitud

    if seq is None:
        raise ValueError(f"{path}: no encontrado el bloque de secuencia (tipo 0)")
    return seq, rasgos


def dianas(seq, sitio):
    """Posiciones 1-based de un sitio en las dos hebras, sin duplicar."""
    pos = [m.start() + 1 for m in re.finditer("(?=" + sitio + ")", seq)]
    if rc(sitio) != sitio:
        pos += [m.start() + 1 for m in re.finditer("(?=" + rc(sitio) + ")", seq)]
    return sorted(set(pos))


def mapa(seq, ventana=None, solo_unicas=False):
    """[(enzima, diana, [posiciones], [posiciones dentro de la ventana])]"""
    salida = []
    for enz, sitio in sorted(ENZIMAS.items()):
        pos = dianas(seq, sitio)
        if not pos:
            continue
        if solo_unicas and len(pos) != 1:
            continue
        dentro = pos
        if ventana:
            a, b = ventana
            dentro = [p for p in pos if a <= p <= b]
            if not dentro:
                continue
        salida.append((enz, sitio, pos, dentro))
    return salida


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ficheros", nargs="+", help="uno o mas .dna")
    ap.add_argument("--fasta", metavar="SALIDA",
                    help="escribe la secuencia en FASTA (sólo con un fichero)")
    ap.add_argument("--dianas", action="store_true",
                    help="lista las enzimas de corte unico")
    ap.add_argument("--ventana", nargs=2, type=int, metavar=("INICIO", "FIN"),
                    help="lista las enzimas con diana en ese tramo")
    args = ap.parse_args()

    if args.fasta and len(args.ficheros) > 1:
        sys.exit("--fasta sólo admite un fichero de entrada")

    for path in args.ficheros:
        seq, rasgos = lee(path)
        nombre = path.split("/")[-1]
        print(f"\n## {nombre}  —  {len(seq)} pb")

        for n, a, b in sorted(rasgos, key=lambda r: r[1]):
            print(f"   {n:32s} {a:6d}..{b:<6d} ({b - a + 1:5d} pb)")

        if args.dianas:
            print("\n   Enzimas de corte unico:")
            for enz, sitio, pos, _ in mapa(seq, solo_unicas=True):
                print(f"     {enz:10s} {sitio:19s} {pos[0]}")

        if args.ventana:
            a, b = args.ventana
            print(f"\n   Dianas en {a}..{b}:")
            encontrado = False
            for enz, sitio, pos, dentro in mapa(seq, ventana=(a, b)):
                encontrado = True
                estado = "UNICA" if len(pos) == 1 else f"{len(pos)}x en {pos}"
                print(f"     {enz:10s} {sitio:19s} {dentro}   [{estado}]")
            if not encontrado:
                print("     (ninguna del panel)")

        if args.fasta:
            with open(args.fasta, "w") as fh:
                fh.write(f">{nombre}\n")
                for i in range(0, len(seq), 60):
                    fh.write(seq[i:i + 60] + "\n")
            print(f"\n   Secuencia escrita en {args.fasta}")


if __name__ == "__main__":
    main()
