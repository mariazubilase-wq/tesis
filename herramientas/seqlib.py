"""Utilidades mínimas de secuencia (sin dependencias externas).

Escrito para el diseño de clonaje de KRT10 en minicírculo. Python >= 3.9.
"""
from __future__ import annotations

import math
import re
from dataclasses import dataclass, field

COMPLEMENTO = str.maketrans("ACGTRYSWKMBDHVNacgtryswkmbdhvn",
                            "TGCAYRSWMKVHDBNtgcayrswmkvhdbn")

CODIGO = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L",
    "CTA": "L", "CTG": "L", "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V", "TCT": "S", "TCC": "S",
    "TCA": "S", "TCG": "S", "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T", "GCT": "A", "GCC": "A",
    "GCA": "A", "GCG": "A", "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "AAT": "N", "AAC": "N",
    "AAA": "K", "AAG": "K", "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W", "CGT": "R", "CGC": "R",
    "CGA": "R", "CGG": "R", "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

# Sinónimos por aminoácido (para los cambios wobble).
SINONIMOS: dict[str, list[str]] = {}
for _cod, _aa in CODIGO.items():
    SINONIMOS.setdefault(_aa, []).append(_cod)

IUPAC = {
    "A": "A", "C": "C", "G": "G", "T": "T",
    "R": "AG", "Y": "CT", "S": "CG", "W": "AT", "K": "GT", "M": "AC",
    "B": "CGT", "D": "AGT", "H": "ACT", "V": "ACG", "N": "ACGT",
}


def limpia(s: str) -> str:
    """Deja sólo letras de secuencia, en mayúsculas."""
    return re.sub(r"[^A-Za-z]", "", s).upper()


def rc(s: str) -> str:
    """Complementario inverso."""
    return s.translate(COMPLEMENTO)[::-1]


def gc(s: str) -> float:
    s = s.upper()
    if not s:
        return 0.0
    return 100.0 * (s.count("G") + s.count("C")) / len(s)


def traduce(s: str) -> str:
    s = s.upper()
    return "".join(CODIGO.get(s[i:i + 3], "X") for i in range(0, len(s) - 2, 3))


def a_regex(patron: str) -> re.Pattern:
    """Convierte un patrón IUPAC en expresión regular."""
    return re.compile("".join(
        f"[{IUPAC[b]}]" if len(IUPAC.get(b, b)) > 1 else b for b in patron.upper()))


def busca(seq: str, patron: str, circular: bool = False) -> list[int]:
    """Posiciones 0-based de todas las apariciones (solapantes) en la hebra dada.

    Si circular, busca también a caballo del origen numérico del fichero.
    """
    rx = a_regex(patron)
    diana = seq + (seq[:len(patron) - 1] if circular and len(seq) > len(patron) else "")
    vistos, fuera = set(), []
    for m in rx.finditer(diana):
        p = m.start() % len(seq)
        if p not in vistos:
            vistos.add(p)
            fuera.append(p)
    return sorted(fuera)


def busca_ambas(seq: str, patron: str, circular: bool = False) -> list[int]:
    """Posiciones en ambas hebras (para dianas no palindrómicas)."""
    pos = set(busca(seq, patron, circular))
    prc = rc(patron)
    if prc != patron.upper():
        for p in busca(seq, prc, circular):
            pos.add(p)
    return sorted(pos)


# ---------------------------------------------------------------------------
# Tm por vecino más próximo (SantaLucia 1998, parámetros unificados)
# ---------------------------------------------------------------------------
_NN_H = {"AA": -7.9, "TT": -7.9, "AT": -7.2, "TA": -7.2, "CA": -8.5, "TG": -8.5,
         "GT": -8.4, "AC": -8.4, "CT": -7.8, "AG": -7.8, "GA": -8.2, "TC": -8.2,
         "CG": -10.6, "GC": -9.8, "GG": -8.0, "CC": -8.0}
_NN_S = {"AA": -22.2, "TT": -22.2, "AT": -20.4, "TA": -21.3, "CA": -22.7,
         "TG": -22.7, "GT": -22.4, "AC": -22.4, "CT": -21.0, "AG": -21.0,
         "GA": -22.2, "TC": -22.2, "CG": -27.2, "GC": -24.4, "GG": -19.9,
         "CC": -19.9}


def tm_nn(seq: str, conc_primer_nM: float = 500.0, na_mM: float = 50.0) -> float:
    """Tm nearest-neighbour, corregida por sal (SantaLucia 1998).

    Valor orientativo: para Q5/Phusion hay que contrastarlo con la calculadora
    de NEB, que usa condiciones propias.
    """
    s = seq.upper()
    if len(s) < 2 or any(b not in "ACGT" for b in s):
        return float("nan")
    dh = 0.0
    ds = 0.0
    for i in range(len(s) - 1):
        par = s[i:i + 2]
        dh += _NN_H[par]
        ds += _NN_S[par]
    # Iniciación en cada extremo.
    for extremo in (s[0], s[-1]):
        if extremo in "GC":
            dh += 0.1
            ds += -2.8
        else:
            dh += 2.3
            ds += 4.1
    na = max(na_mM, 1e-6) / 1000.0
    ds += 0.368 * (len(s) - 1) * math.log(na)
    ct = conc_primer_nM * 1e-9
    r = 1.987
    return (dh * 1000.0) / (ds + r * math.log(ct / 4.0)) - 273.15


def peor_horquilla(seq: str, min_tallo: int = 5, min_bucle: int = 3) -> tuple[int, str]:
    """Tallo complementario más largo capaz de formar horquilla. Heurística."""
    s = seq.upper()
    mejor = (0, "")
    n = len(s)
    for i in range(n):
        for j in range(i + min_tallo + min_bucle, n + 1):
            for L in range(min_tallo, (j - i - min_bucle) // 2 + 1):
                a = s[i:i + L]
                b = s[j - L:j]
                if a == rc(b):
                    if L > mejor[0]:
                        mejor = (L, a)
    return mejor


def dimero_3p(a: str, b: str, min_solape: int = 4) -> tuple[int, str]:
    """Complementariedad del extremo 3' de a con cualquier parte de b."""
    a = a.upper()
    b = b.upper()
    mejor = (0, "")
    for L in range(min_solape, min(len(a), len(b)) + 1):
        cola = a[-L:]
        if rc(cola) in b:
            mejor = (L, cola)
    return mejor
