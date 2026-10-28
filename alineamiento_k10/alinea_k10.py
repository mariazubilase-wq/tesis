#!/usr/bin/env python3
"""Alinea K10 humana vs murina y localiza el residuo equivalente a una posicion dada.

Uso:
    python3 -I alinea_k10.py humana.fasta murina.fasta [POS_HUMANA]

POS_HUMANA por defecto 156 (hotspot R156 de KRT10 humana).

Metodo doble, para poder contrastar:
  (A) Ventana de contexto: coge N residuos alrededor de la posicion humana y busca
      en la secuencia murina la ventana con mas identidad. Robusto y facil de verificar
      a ojo. Es el resultado principal.
  (B) Alineamiento global Needleman-Wunsch completo. Sirve de control independiente:
      si A y B coinciden, el numero es fiable.
"""
import sys


def read_fasta(path):
    """Devuelve (cabecera, secuencia) del primer registro. Tolera texto pegado sin cabecera."""
    header, parts = "", []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if parts:          # ya habia una secuencia: paramos en el 2o registro
                    break
                header = line[1:]
                continue
            parts.append("".join(c for c in line if c.isalpha()))
    return header, "".join(parts).upper()


def context_scan(human, mouse, pos, flank=12):
    """(A) Busca la ventana murina mas parecida a la ventana humana centrada en pos (1-based)."""
    i = pos - 1
    lo, hi = max(0, i - flank), min(len(human), i + flank + 1)
    win = human[lo:hi]
    offset_in_win = i - lo                      # donde cae el residuo diana dentro de la ventana
    best = (-1, None)
    for j in range(len(mouse) - len(win) + 1):
        score = sum(1 for a, b in zip(win, mouse[j:j + len(win)]) if a == b)
        if score > best[0]:
            best = (score, j)
    score, j = best
    mouse_idx = j + offset_in_win               # 0-based en la murina
    return {
        "human_window": win,
        "mouse_window": mouse[j:j + len(win)],
        "identities": score,
        "window_len": len(win),
        "mouse_pos": mouse_idx + 1,             # 1-based
        "mouse_res": mouse[mouse_idx],
    }


def needleman_wunsch(a, b, match=2, mismatch=-1, gap=-5):
    """(B) Alineamiento global clasico con hueco lineal. Devuelve las dos cadenas alineadas."""
    n, m = len(a), len(b)
    # matriz de puntuaciones por filas (lista de listas de ints)
    prev = [gap * j for j in range(m + 1)]
    ptr = [[0] * (m + 1) for _ in range(n + 1)]   # 0=diag 1=arriba(gap en b) 2=izq(gap en a)
    for j in range(1, m + 1):
        ptr[0][j] = 2
    for i in range(1, n + 1):
        cur = [gap * i] + [0] * m
        ptr[i][0] = 1
        for j in range(1, m + 1):
            d = prev[j - 1] + (match if a[i - 1] == b[j - 1] else mismatch)
            u = prev[j] + gap
            l = cur[j - 1] + gap
            bestv = d
            bestp = 0
            if u > bestv:
                bestv, bestp = u, 1
            if l > bestv:
                bestv, bestp = l, 2
            cur[j] = bestv
            ptr[i][j] = bestp
        prev = cur
    # traceback
    i, j = n, m
    ra, rb = [], []
    while i > 0 or j > 0:
        p = ptr[i][j]
        if i > 0 and j > 0 and p == 0:
            ra.append(a[i - 1]); rb.append(b[j - 1]); i -= 1; j -= 1
        elif i > 0 and (p == 1 or j == 0):
            ra.append(a[i - 1]); rb.append("-"); i -= 1
        else:
            ra.append("-"); rb.append(b[j - 1]); j -= 1
    return "".join(reversed(ra)), "".join(reversed(rb))


def map_via_alignment(aa, ab, pos):
    """Dada la posicion 1-based en la secuencia A, devuelve (pos_en_B, residuo_en_B, col)."""
    ca = cb = 0
    for col, (x, y) in enumerate(zip(aa, ab)):
        if x != "-":
            ca += 1
        if y != "-":
            cb += 1
        if ca == pos and x != "-":
            return (cb if y != "-" else None), y, col
    return None, None, None


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    hp, mp = sys.argv[1], sys.argv[2]
    pos = int(sys.argv[3]) if len(sys.argv) > 3 else 156

    hh, hs = read_fasta(hp)
    mh, ms = read_fasta(mp)

    print("=" * 72)
    print("SECUENCIAS")
    print(f"  humana : {hh[:70] or '(sin cabecera)'}")
    print(f"           longitud = {len(hs)} aa")
    print(f"  murina : {mh[:70] or '(sin cabecera)'}")
    print(f"           longitud = {len(ms)} aa")
    print(f"  diferencia de longitud = {len(hs) - len(ms):+d} aa")

    if pos > len(hs):
        print(f"\n!! La posicion {pos} excede la longitud de la secuencia humana.")
        sys.exit(2)

    print("\n" + "=" * 72)
    print(f"RESIDUO HUMANO EN LA POSICION {pos}: {hs[pos-1]}")
    if hs[pos - 1] != "R":
        print("  !! AVISO: no es una arginina. Revisa la numeracion o el isoforma usado.")

    print("\n" + "=" * 72)
    print("(A) VENTANA DE CONTEXTO")
    r = context_scan(hs, ms, pos)
    print(f"  ventana humana : {r['human_window']}")
    print(f"  ventana murina : {r['mouse_window']}")
    print(f"  identidad en la ventana: {r['identities']}/{r['window_len']}")
    print(f"  --> posicion murina equivalente: {r['mouse_pos']}  (residuo {r['mouse_res']})")
    print(f"  --> desplazamiento humano->raton: {r['mouse_pos'] - pos:+d}")

    print("\n" + "=" * 72)
    print("(B) ALINEAMIENTO GLOBAL (control independiente)")
    aa, ab = needleman_wunsch(hs, ms)
    ident = sum(1 for x, y in zip(aa, ab) if x == y and x != "-")
    print(f"  longitud del alineamiento: {len(aa)}")
    print(f"  identidad global: {ident}/{min(len(hs), len(ms))} = {100.0*ident/min(len(hs), len(ms)):.1f}%")
    bpos, bres, col = map_via_alignment(aa, ab, pos)
    print(f"  --> posicion murina equivalente: {bpos}  (residuo {bres})")
    if col is not None:
        s, e = max(0, col - 25), min(len(aa), col + 26)
        marker = "".join("^" if k == col else " " for k in range(s, e))
        print("\n  bloque alineado alrededor del residuo diana:")
        print(f"    humana : {aa[s:e]}")
        print(f"    murina : {ab[s:e]}")
        print(f"             {marker}")

    print("\n" + "=" * 72)
    print("VEREDICTO")
    if bpos is not None and bpos == r["mouse_pos"]:
        print(f"  Los dos metodos COINCIDEN: humana {pos}{hs[pos-1]}  ==  murina {bpos}{bres}")
        print(f"  Numeracion fiable. Desplazamiento {bpos - pos:+d} aa.")
    else:
        print(f"  !! Los metodos DISCREPAN (A={r['mouse_pos']}, B={bpos}).")
        print("  Revisar a mano el bloque alineado antes de usar el numero.")
    print("=" * 72)


if __name__ == "__main__":
    main()
