#!/usr/bin/env python3
"""Genera la figura de la nanopartícula lipídica (LNP) en SVG.

Uso:  python3 herramientas/figura_lnp.py diseno/figura_nanoparticula_lipidica.svg

La figura es un corte de una LNP: monocapa externa de lípidos, PEG en la
superficie, colesterol intercalado y, dentro, micelas invertidas que envuelven
el ácido nucleico. Todo se dibuja por cálculo para que las colas y las cabezas
queden bien orientadas; si quieres retocar el resultado, edita el SVG de salida.
"""

import math
import sys

W, H = 960, 540
CX, CY, R = 262, 300, 144          # centro y radio de la partícula

ION_H, ION_T = "#2f6f7e", "#79aeb8"   # lípido ionizable
PHO_H, PHO_T = "#3f74ad", "#9bbede"   # fosfolípido
CHOL = "#d9a441"                      # colesterol
PEG_H, PEG_C = "#7d5fa6", "#a98fcb"   # lípido-PEG
NA = "#8f2436"                        # ácido nucleico
INK, GREY = "#39414f", "#6b7280"

out = []
add = out.append


def lipido(x, y, ang, head, tail, hr=5.2, largo=24, sep=2.4):
    """Un lípido con la cabeza en (x, y) y las colas hacia el ángulo `ang`."""
    dx, dy = math.cos(ang), math.sin(ang)
    px, py = -dy, dx
    for s in (-1, 1):
        x0, y0 = x + dx * 3 + px * sep * s, y + dy * 3 + py * sep * s
        x1, y1 = x + dx * largo + px * sep * 2.1 * s, y + dy * largo + py * sep * 2.1 * s
        xm, ym = (x0 + x1) / 2 + px * 2.6 * s, (y0 + y1) / 2 + py * 2.6 * s
        add(f'<path d="M{x0:.1f},{y0:.1f} Q{xm:.1f},{ym:.1f} {x1:.1f},{y1:.1f}" '
            f'fill="none" stroke="{tail}" stroke-width="2" stroke-linecap="round"/>')
    add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{hr}" fill="{head}"/>')


def colesterol(x, y, ang, escala=1.0):
    g = math.degrees(ang)
    add(f'<g transform="translate({x:.1f},{y:.1f}) rotate({g:.1f}) scale({escala})">'
        f'<rect x="-3" y="-8" width="6" height="16" rx="3" fill="{CHOL}"/>'
        f'<circle cx="0" cy="-8" r="3.1" fill="{CHOL}"/></g>')


def peg(x, y, ang, largo=26):
    """Cadena de PEG saliendo hacia fuera desde (x, y)."""
    dx, dy = math.cos(ang), math.sin(ang)
    px, py = -dy, dx
    pts = []
    for i in range(5):
        t = largo * i / 4
        lat = 5.0 * math.sin(i * 1.9)
        pts.append((x + dx * t + px * lat, y + dy * t + py * lat))
    d = f'M{pts[0][0]:.1f},{pts[0][1]:.1f}'
    for i in range(1, len(pts)):
        xa, ya = pts[i - 1]
        xb, yb = pts[i]
        d += f' Q{(xa + xb) / 2 + px * 4:.1f},{(ya + yb) / 2 + py * 4:.1f} {xb:.1f},{yb:.1f}'
    add(f'<path d="{d}" fill="none" stroke="{PEG_C}" stroke-width="2.2" stroke-linecap="round"/>')
    add(f'<circle cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="3.2" fill="{PEG_C}"/>')


def ovillo(mx, my, ra, fase=0.0, vueltas=2.1, grosor=2.6):
    """Un ovillo suave de ácido nucleico: espiral dibujada con curvas."""
    pts = []
    n = 34
    for i in range(n + 1):
        t = i / n
        a = fase + 2 * math.pi * vueltas * t
        rr = ra * (0.22 + 0.78 * t)
        pts.append((mx + rr * math.cos(a), my + rr * math.sin(a)))
    d = f'M{pts[0][0]:.1f},{pts[0][1]:.1f}'
    for i in range(1, len(pts) - 1):
        xa, ya = pts[i]
        xb, yb = (pts[i][0] + pts[i + 1][0]) / 2, (pts[i][1] + pts[i + 1][1]) / 2
        d += f' Q{xa:.1f},{ya:.1f} {xb:.1f},{yb:.1f}'
    return (f'<path d="{d}" fill="none" stroke="{NA}" stroke-width="{grosor}" '
            f'stroke-linecap="round"/>')


def micela_invertida(mx, my, rm, nl=11, semilla=0.0):
    """Micela invertida: cabezas hacia dentro, colas hacia fuera, ácido nucleico dentro."""
    add(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="{rm - 2:.1f}" fill="#f7eef0"/>')
    for i in range(nl):
        a = 2 * math.pi * i / nl + semilla
        hx, hy = mx + rm * math.cos(a), my + rm * math.sin(a)
        lipido(hx, hy, a, ION_H, ION_T, hr=4.4, largo=16, sep=2.0)
    add(ovillo(mx, my, rm * 0.62, semilla, grosor=2.6))


# ----------------------------------------------------------------- lienzo
add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
    f'viewBox="0 0 {W} {H}" font-family="Verdana, DejaVu Sans, sans-serif">')
add('<defs>'
    '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
    'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6b7280"/></marker>'
    '<marker id="ar2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
    'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#39414f"/></marker>'
    '<radialGradient id="nucleo" cx="50%" cy="48%" r="58%">'
    '<stop offset="0%" stop-color="#fdf7f3"/><stop offset="100%" stop-color="#f3e6de"/>'
    '</radialGradient></defs>')
add(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')

add(f'<text x="40" y="46" font-size="24" font-weight="bold" fill="#1f2937">'
    f'Nanopartículas lipídicas</text>')
add('<rect x="40" y="58" width="520" height="3.5" fill="#8f2436"/>')
add(f'<text x="40" y="80" font-size="11.5" fill="{GREY}">corte por la mitad de una partícula</text>')

# ------------------------------------------------------- cuerpo de la LNP
add(f'<circle cx="{CX}" cy="{CY}" r="{R - 16}" fill="url(#nucleo)"/>')

# micelas invertidas con la carga
for mx, my, rm, s in [(CX - 4, CY + 6, 34, 0.3),
                      (CX + 62, CY - 58, 27, 1.1),
                      (CX - 66, CY - 54, 25, 2.0),
                      (CX - 62, CY + 68, 26, 0.7),
                      (CX + 66, CY + 62, 25, 1.6)]:
    micela_invertida(mx, my, rm, semilla=s)

# colesterol suelto entre las micelas
for ax, rr in [(0.35, 104), (1.25, 100), (2.1, 98), (3.0, 104), (3.9, 100),
               (4.7, 96), (5.5, 102), (0.85, 62), (2.6, 66), (4.3, 64)]:
    colesterol(CX + rr * math.cos(ax), CY + rr * math.sin(ax), ax + math.pi / 2, 0.9)

# monocapa externa
patron = ['ION', 'ION', 'PHO', 'ION', 'CHOL', 'ION', 'PHO', 'ION', 'PEG', 'ION', 'ION', 'PHO']
N = 48
for i in range(N):
    a = 2 * math.pi * i / N - math.pi / 2
    tipo = patron[i % len(patron)]
    hx, hy = CX + R * math.cos(a), CY + R * math.sin(a)
    if tipo == 'CHOL':
        colesterol(CX + (R - 13) * math.cos(a), CY + (R - 13) * math.sin(a), a + math.pi / 2, 1.0)
    elif tipo == 'PEG':
        lipido(hx, hy, a + math.pi, PEG_H, PEG_C)
        peg(hx + 4 * math.cos(a), hy + 4 * math.sin(a), a)
    elif tipo == 'PHO':
        lipido(hx, hy, a + math.pi, PHO_H, PHO_T)
    else:
        lipido(hx, hy, a + math.pi, ION_H, ION_T)

# diámetro
y_d = CY + R + 36
add(f'<line x1="{CX - R}" y1="{y_d}" x2="{CX + R}" y2="{y_d}" stroke="{GREY}" '
    f'stroke-width="1.6" marker-start="url(#ar)" marker-end="url(#ar)"/>')
add(f'<text x="{CX}" y="{y_d + 18}" text-anchor="middle" font-size="11" fill="{GREY}">'
    f'≈ 80–100 nm (unas mil veces más fina que un pelo)</text>')

# --------------------------------------------------------------- leyenda
LX = 468
add(f'<text x="{LX}" y="108" font-size="13.5" font-weight="bold" fill="{INK}">De qué está hecha</text>')

filas = [
    (136, 'ION', 'Lípido ionizable', 'atrapa el DNA o el RNA y, ya dentro,', 'rompe el endosoma para soltarlo'),
    (196, 'PHO', 'Fosfolípido', 'forma la pared de la partícula,', 'como la membrana de una célula'),
    (256, 'CHOL', 'Colesterol', 'se mete entre los lípidos y da', 'rigidez: la partícula no se deshace'),
    (316, 'PEG', 'Lípido-PEG', 'la capa resbaladiza de fuera: evita', 'que se peguen entre sí y la protege'),
]
for y, tipo, titulo, l1, l2 in filas:
    ix, iy = LX + 16, y + 2
    if tipo == 'CHOL':
        colesterol(ix, iy, 0, 1.15)
    elif tipo == 'PEG':
        lipido(ix, iy - 4, math.pi / 2, PEG_H, PEG_C, hr=5.4, largo=18)
        peg(ix, iy - 9, -math.pi / 2, 16)
    else:
        h, t = (ION_H, ION_T) if tipo == 'ION' else (PHO_H, PHO_T)
        lipido(ix, iy - 10, math.pi / 2, h, t, hr=5.4, largo=20)
    add(f'<text x="{LX + 50}" y="{y - 4}" font-size="12.5" font-weight="bold" fill="{INK}">{titulo}</text>')
    add(f'<text x="{LX + 50}" y="{y + 12}" font-size="10.5" fill="{GREY}">{l1}</text>')
    add(f'<text x="{LX + 50}" y="{y + 26}" font-size="10.5" fill="{GREY}">{l2}</text>')

# la carga
add(f'<rect x="{LX}" y="356" width="452" height="56" rx="8" fill="#fbf1f2"/>')
add(ovillo(LX + 28, 384, 11, 0.4, grosor=2.4))
add(f'<text x="{LX + 58}" y="380" font-size="12.5" font-weight="bold" fill="#8f2436">La carga: el ácido nucleico</text>')
add(f'<text x="{LX + 58}" y="396" font-size="10.5" fill="{GREY}">el minicírculo con KRT10, o el siRNA, van ovillados dentro</text>')

# cómo entrega la carga
add(f'<text x="{LX}" y="444" font-size="13.5" font-weight="bold" fill="{INK}">Cómo entrega la carga</text>')
pasos = [('1', 'la célula la traga', '(endocitosis)'),
         ('2', 'rompe el endosoma', 'el lípido se carga +'),
         ('3', 'el gen queda libre', 'dentro de la célula')]
for i, (n, l1, l2) in enumerate(pasos):
    x = LX + i * 152
    add(f'<circle cx="{x + 10}" cy="{468}" r="10" fill="{ION_H}"/>')
    add(f'<text x="{x + 10}" y="{472}" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">{n}</text>')
    add(f'<text x="{x + 26}" y="{466}" font-size="10" fill="{INK}">{l1}</text>')
    add(f'<text x="{x + 26}" y="{480}" font-size="10" fill="{GREY}">{l2}</text>')
    if i < 2:
        add(f'<line x1="{x + 130}" y1="468" x2="{x + 146}" y2="468" stroke="{INK}" '
            f'stroke-width="1.8" marker-end="url(#ar2)"/>')

add(f'<text x="40" y="524" font-size="9.5" fill="#9aa1a9">'
    f'Terapia génica en ictiosis epidermolítica · KRT10</text>')
add('</svg>')

destino = sys.argv[1] if len(sys.argv) > 1 else 'figura_nanoparticula_lipidica.svg'
with open(destino, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out) + '\n')
print(f'escrito: {destino}')
