#!/usr/bin/env python3
"""
Análisis termodinámico de los oligos del proyecto.

Tm por vecino más próximo (SantaLucia 1998, tabla unificada), corrección salina
monovalente, equivalencia de Mg2+ de Owczarzy. Detecta dímeros y horquillas
calculando la ΔG37 real de cada apareamiento posible, no contando bases.

    python3 herramientas/analiza_oligos.py
"""
import re, os, math, itertools

AQUI = os.path.dirname(os.path.abspath(__file__))
GB   = os.path.join(AQUI, "..", "secuencias", "pCMV6-KRT10.gb")
COMP = str.maketrans("ACGT", "TGCA")
rc   = lambda s: s.translate(COMP)[::-1]
R    = 1.98720425864083          # cal/(mol·K)

# ---- SantaLucia 1998, tabla unificada: (dH kcal/mol, dS cal/mol/K, dG37 kcal/mol)
NN = {
 "AA": (-7.9, -22.2, -1.00), "TT": (-7.9, -22.2, -1.00),
 "AT": (-7.2, -20.4, -0.88), "TA": (-7.2, -21.3, -0.58),
 "CA": (-8.5, -22.7, -1.45), "TG": (-8.5, -22.7, -1.45),
 "GT": (-8.4, -22.4, -1.44), "AC": (-8.4, -22.4, -1.44),
 "CT": (-7.8, -21.0, -1.28), "AG": (-7.8, -21.0, -1.28),
 "GA": (-8.2, -22.2, -1.30), "TC": (-8.2, -22.2, -1.30),
 "CG": (-10.6, -27.2, -2.17),
 "GC": (-9.8, -24.4, -2.24),
 "GG": (-8.0, -19.9, -1.84), "CC": (-8.0, -19.9, -1.84),
}
INI = {"G": (0.1, -2.8), "C": (0.1, -2.8), "A": (2.3, 4.1), "T": (2.3, 4.1)}

def na_equivalente(na_mM=50.0, mg_mM=2.0, dntp_mM=0.2):
    """Owczarzy 2008: convierte Mg2+ libre en Na+ equivalente."""
    libre = max(mg_mM - dntp_mM, 0.0)
    return na_mM + 120.0 * math.sqrt(libre)

def tm(seq, conc_nM=500.0, na_mM=50.0, mg_mM=2.0, dntp_mM=0.2):
    """Tm de vecino más próximo, en °C. conc = concentración del oligo."""
    s = seq.upper()
    if len(s) < 2: return float("nan")
    dH = dS = 0.0
    for i in range(len(s) - 1):
        h, sdelta, _ = NN[s[i:i+2]]
        dH += h; dS += sdelta
    for extremo in (s[0], s[-1]):
        h, sdelta = INI[extremo]
        dH += h; dS += sdelta
    na = na_equivalente(na_mM, mg_mM, dntp_mM) / 1000.0        # M
    dS += 0.368 * (len(s) - 1) * math.log(na)
    ct = conc_nM * 1e-9
    auto = (s == rc(s))
    denom = dS + R * math.log(ct if auto else ct / 4.0)
    return (dH * 1000.0) / denom - 273.15

def gc(s):
    return 100.0 * sum(s.count(b) for b in "GC") / len(s)

def dg_duplex(a, b):
    """ΔG37 de aparear a (5'->3') contra b (3'->5'), ambos del mismo largo.
    Sólo suma tramos contiguos apareados; los desapareamientos rompen el tramo."""
    par = [a[i] == COMP_CHAR[b[i]] for i in range(len(a))]
    total, i = 0.0, 0
    while i < len(par):
        if not par[i]: i += 1; continue
        j = i
        while j + 1 < len(par) and par[j+1]: j += 1
        tramo = a[i:j+1]
        if len(tramo) >= 2:
            g = sum(NN[tramo[k:k+2]][2] for k in range(len(tramo)-1))
            g += 0.98 if tramo[0] in "GC" else 1.03
            g += 0.98 if tramo[-1] in "GC" else 1.03
            total += min(g, 0.0)
        i = j + 1
    return total
COMP_CHAR = {"A":"T","T":"A","G":"C","C":"G"}

def peor_dimero(a, b):
    """Desliza b invertido contra a y devuelve (ΔG más negativa, offset, esquema)."""
    br = b[::-1]                       # b escrito 3'->5' bajo a
    mejor = (0.0, None, None)
    for off in range(-(len(br) - 1), len(a)):
        ai, bi, sa, sb = max(0, off), max(0, -off), [], []
        n = min(len(a) - ai, len(br) - bi)
        if n < 3: continue
        sa, sb = a[ai:ai+n], br[bi:bi+n]
        g = dg_duplex(sa, sb)
        if g < mejor[0]:
            pares = "".join("|" if sa[i] == COMP_CHAR[sb[i]] else " " for i in range(n))
            esquema = (f"        5'-{' '*ai}{sa}-3'\n"
                       f"           {' '*ai}{pares}\n"
                       f"        3'-{' '*ai}{sb}-5'")
            mejor = (g, off, esquema)
    return mejor

def dimero_3p(a, b, n=5):
    """¿Los n últimos nt del extremo 3' de a aparean en algún sitio de b?
    Es el dímero que de verdad se extiende y arruina la PCR."""
    cola = a[-n:]
    diana = rc(cola)
    pos = b.find(diana)
    return (pos >= 0, cola, pos)

def horquilla(s, lazo_min=3):
    """Peor horquilla intramolecular: tallo contiguo más estable."""
    mejor = (0.0, None)
    for i in range(len(s)):
        for j in range(i + lazo_min + 2, len(s) + 1):
            for L in range(3, (j - i - lazo_min)//2 + 1):
                izq, der = s[i:i+L], s[j-L:j]
                if izq == rc(der):
                    g = sum(NN[izq[k:k+2]][2] for k in range(L-1))
                    g += (0.98 if izq[0] in "GC" else 1.03)
                    g += (0.98 if izq[-1] in "GC" else 1.03)
                    if g < mejor[0]: mejor = (g, (i, j, L, j-L-(i+L)))
    return mejor

def leer_gb(ruta):
    t = open(ruta).read().split("ORIGIN")[1]
    return re.sub(r"\s", "", "".join(
        re.findall(r"^\s*\d+\s+([acgtnACGTN\s]+)$", t, re.M))).upper()
