#!/usr/bin/env python3
"""Genera dos figuras más de vehículos para el DNA, en SVG:

  * `liposoma`       — un liposoma cortado por la mitad, con el DNA en el
                       interior acuoso.
  * `microemulsion`  — gotas de aceite diminutas en agua, con el DNA pegado
                       a la superficie de la gota.

Uso:
    python3 herramientas/figura_vesiculas.py liposoma      diseno/figura_liposoma.svg
    python3 herramientas/figura_vesiculas.py microemulsion diseno/figura_microemulsion.svg

Como en `figura_lnp.py`, las cabezas y las colas van calculadas una a una para
que queden bien orientadas. Si quieres retocar algo, edita aquí y vuelve a
generar; el SVG de salida es desechable.
"""

import math
import sys

W, H = 960, 540

FOS_H, FOS_T = "#3f74ad", "#9bbede"   # fosfolípido
CAT_H, CAT_T = "#2f6f7e", "#79aeb8"   # tensioactivo catiónico
COT_H, COT_T = "#7d5fa6", "#a98fcb"   # cotensioactivo
CHOL = "#d9a441"                      # colesterol
ACEITE = "#f7e2b4"                    # aceite
AGUA = "#e8f1f6"                      # agua
NA = "#8f2436"                        # DNA
INK, GREY = "#39414f", "#6b7280"


# --------------------------------------------------------------- primitivas
def lipido(x, y, ang, head, tail, hr=5.2, largo=22, sep=2.4, colas=2):
    """Lípido con la cabeza en (x, y) y las colas apuntando hacia `ang`."""
    dx, dy = math.cos(ang), math.sin(ang)
    px, py = -dy, dx
    piezas = []
    desplazamientos = (-1, 1) if colas == 2 else (0,)
    for s in desplazamientos:
        x0, y0 = x + dx * 3 + px * sep * s, y + dy * 3 + py * sep * s
        x1, y1 = x + dx * largo + px * sep * 2.1 * s, y + dy * largo + py * sep * 2.1 * s
        xm = (x0 + x1) / 2 + px * (2.6 if s else 2.2)
        ym = (y0 + y1) / 2 + py * (2.6 if s else 2.2)
        piezas.append(f'<path d="M{x0:.1f},{y0:.1f} Q{xm:.1f},{ym:.1f} {x1:.1f},{y1:.1f}" '
                      f'fill="none" stroke="{tail}" stroke-width="2" stroke-linecap="round"/>')
    piezas.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{hr}" fill="{head}"/>')
    return ''.join(piezas)


def carga_mas(x, y, color="#ffffff", tam=7):
    return (f'<text x="{x:.1f}" y="{y + tam * 0.36:.1f}" text-anchor="middle" '
            f'font-size="{tam}" font-weight="bold" fill="{color}">+</text>')


def colesterol(x, y, ang, escala=1.0):
    g = math.degrees(ang)
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({g:.1f}) scale({escala})">'
            f'<rect x="-3" y="-8" width="6" height="16" rx="3" fill="{CHOL}"/>'
            f'<circle cx="0" cy="-8" r="3.1" fill="{CHOL}"/></g>')


def plasmido(cx, cy, r, lobulos=5, amp=2.6, fase=0.0, grosor=4.2, color=NA):
    """Un círculo de DNA ligeramente ondulado: se lee como plásmido o minicírculo."""
    pts = []
    n = 96
    for i in range(n + 1):
        t = 2 * math.pi * i / n
        rr = r + amp * math.sin(lobulos * t + fase)
        pts.append((cx + rr * math.cos(t), cy + rr * math.sin(t)))
    d = f'M{pts[0][0]:.1f},{pts[0][1]:.1f} ' + ' '.join(f'L{x:.1f},{y:.1f}' for x, y in pts[1:])
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}" '
            f'stroke-linejoin="round"/>')


def hebra(x0, y0, x1, y1, amp=7, ondas=3, grosor=3.4, color=NA):
    """Una hebra de DNA suelta, ondulada, entre dos puntos."""
    dx, dy = x1 - x0, y1 - y0
    largo = math.hypot(dx, dy) or 1
    ux, uy = dx / largo, dy / largo
    px, py = -uy, ux
    pts = []
    n = 24
    for i in range(n + 1):
        t = i / n
        lat = amp * math.sin(2 * math.pi * ondas * t)
        pts.append((x0 + ux * largo * t + px * lat, y0 + uy * largo * t + py * lat))
    d = f'M{pts[0][0]:.1f},{pts[0][1]:.1f} ' + ' '.join(f'L{x:.1f},{y:.1f}' for x, y in pts[1:])
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def hebra_pegada(cx, cy, r, a0, a1, amp=4.0, ondas=5, grosor=3.2, color=NA):
    """Una hebra de DNA ondulada que abraza parte de una gota."""
    pts = []
    n = 72
    for i in range(n + 1):
        t = i / n
        a = a0 + (a1 - a0) * t
        rr = r + amp * math.sin(2 * math.pi * ondas * t)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d = f'M{pts[0][0]:.1f},{pts[0][1]:.1f} ' + ' '.join(f'L{x:.1f},{y:.1f}' for x, y in pts[1:])
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def cabecera(titulo, subtitulo=None):
    piezas = [f'<text x="40" y="46" font-size="24" font-weight="bold" fill="#1f2937">{titulo}</text>',
              '<rect x="40" y="58" width="520" height="3.5" fill="#8f2436"/>']
    if subtitulo:
        piezas.append(f'<text x="40" y="80" font-size="11.5" fill="{GREY}">{subtitulo}</text>')
    return piezas


DEFS = ('<defs>'
        '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6b7280"/></marker>'
        '<marker id="ar2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#39414f"/></marker>'
        '</defs>')


def pasos(out, x0, y, items, ancho=152, color=CAT_H):
    for i, (n, l1, l2) in enumerate(items):
        x = x0 + i * ancho
        out.append(f'<circle cx="{x + 10}" cy="{y}" r="10" fill="{color}"/>')
        out.append(f'<text x="{x + 10}" y="{y + 4}" text-anchor="middle" font-size="11" '
                   f'font-weight="bold" fill="#ffffff">{n}</text>')
        out.append(f'<text x="{x + 26}" y="{y - 2}" font-size="10" fill="{INK}">{l1}</text>')
        out.append(f'<text x="{x + 26}" y="{y + 12}" font-size="10" fill="{GREY}">{l2}</text>')
        if i < len(items) - 1:
            out.append(f'<line x1="{x + ancho - 22}" y1="{y}" x2="{x + ancho - 6}" y2="{y}" '
                       f'stroke="{INK}" stroke-width="1.8" marker-end="url(#ar2)"/>')


def leyenda(out, x, filas):
    """filas: (y, dibujo_svg, titulo, linea1, linea2)"""
    for y, icono, titulo, l1, l2 in filas:
        out.append(icono)
        out.append(f'<text x="{x + 50}" y="{y - 4}" font-size="12.5" font-weight="bold" fill="{INK}">{titulo}</text>')
        out.append(f'<text x="{x + 50}" y="{y + 12}" font-size="10.5" fill="{GREY}">{l1}</text>')
        if l2:
            out.append(f'<text x="{x + 50}" y="{y + 26}" font-size="10.5" fill="{GREY}">{l2}</text>')


def lienzo(titulo, subtitulo):
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           f'font-family="Verdana, DejaVu Sans, sans-serif">', DEFS,
           f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    out += cabecera(titulo, subtitulo)
    return out


def pie(out, texto='Terapia génica en ictiosis epidermolítica · KRT10'):
    out.append(f'<text x="40" y="524" font-size="9.5" fill="#9aa1a9">{texto}</text>')
    out.append('</svg>')


# ---------------------------------------------------------------- liposoma
def liposoma():
    CX, CY, R = 258, 296, 146
    GROSOR = 46                       # grosor de la bicapa
    RI = R - GROSOR                   # radio de la monocapa interna
    out = lienzo('Liposoma con DNA dentro', 'corte por la mitad de una vesícula')

    # interior acuoso
    out.append(f'<circle cx="{CX}" cy="{CY}" r="{RI - 4}" fill="{AGUA}"/>')
    # franja de la bicapa, para que se vea como una pared
    out.append(f'<circle cx="{CX}" cy="{CY}" r="{R - GROSOR / 2:.1f}" fill="none" '
               f'stroke="#f2f6fa" stroke-width="{GROSOR}"/>')

    # el DNA dentro: un minicírculo y una hebra suelta
    out.append(plasmido(CX - 24, CY + 4, 34, lobulos=5, amp=2.6, fase=0.4))
    out.append(plasmido(CX + 46, CY + 52, 19, lobulos=5, amp=2.2, fase=1.7, grosor=3.6))
    out.append(hebra(CX - 62, CY + 66, CX - 4, CY + 80, amp=5, ondas=2.5, grosor=3.2))
    etiqueta_dna = (CX + 158, CY + 124)

    # monocapa externa (cabezas fuera, colas hacia dentro)
    N = 54
    for i in range(N):
        a = 2 * math.pi * i / N - math.pi / 2
        x, y = CX + R * math.cos(a), CY + R * math.sin(a)
        if i % 9 == 4:
            out.append(colesterol(CX + (R - 22) * math.cos(a), CY + (R - 22) * math.sin(a),
                                  a + math.pi / 2, 1.0))
        else:
            out.append(lipido(x, y, a + math.pi, FOS_H, FOS_T, largo=20))

    # monocapa interna (cabezas dentro, colas hacia fuera)
    NI = 38
    for i in range(NI):
        a = 2 * math.pi * i / NI - math.pi / 2
        x, y = CX + RI * math.cos(a), CY + RI * math.sin(a)
        out.append(lipido(x, y, a, FOS_H, FOS_T, largo=20))

    # llamada al DNA
    out.append(f'<line x1="{CX + 10}" y1="{CY + 56}" x2="{etiqueta_dna[0] - 6}" '
               f'y2="{etiqueta_dna[1] - 4}" stroke="{GREY}" stroke-width="1.2"/>')
    out.append(f'<text x="{etiqueta_dna[0]}" y="{etiqueta_dna[1]}" font-size="11.5" '
               f'font-weight="bold" fill="{NA}">el DNA</text>')
    out.append(f'<text x="{etiqueta_dna[0]}" y="{etiqueta_dna[1] + 15}" font-size="10.5" '
               f'fill="{GREY}">flota en el agua</text>')

    # llamada a la bicapa
    out.append(f'<line x1="{CX + 118}" y1="{CY - 96}" x2="{CX + 150}" y2="{CY - 150}" '
               f'stroke="{GREY}" stroke-width="1.2"/>')
    out.append(f'<text x="{CX + 154}" y="{CY - 152}" font-size="11.5" font-weight="bold" fill="{INK}">bicapa</text>')
    out.append(f'<text x="{CX + 154}" y="{CY - 138}" font-size="10.5" fill="{GREY}">dos filas de lípidos,</text>')
    out.append(f'<text x="{CX + 154}" y="{CY - 125}" font-size="10.5" fill="{GREY}">igual que una membrana</text>')

    # diámetro
    y_d = CY + R + 34
    out.append(f'<line x1="{CX - R}" y1="{y_d}" x2="{CX + R}" y2="{y_d}" stroke="{GREY}" '
               f'stroke-width="1.6" marker-start="url(#ar)" marker-end="url(#ar)"/>')
    out.append(f'<text x="{CX}" y="{y_d + 18}" text-anchor="middle" font-size="11" fill="{GREY}">'
               f'≈ 100–200 nm</text>')

    # leyenda
    LX = 556
    out.append(f'<text x="{LX}" y="152" font-size="13.5" font-weight="bold" fill="{INK}">De qué está hecho</text>')
    leyenda(out, LX, [
        (180, lipido(LX + 16, 170, math.pi / 2, FOS_H, FOS_T, hr=5.4, largo=20),
         'Fosfolípidos', 'forman la bicapa: la parte que odia el agua', 'queda escondida en el medio'),
        (240, colesterol(LX + 16, 242, 0, 1.15),
         'Colesterol', 'intercalado en la pared, para que la', 'vesícula no se rompa antes de tiempo'),
        (300, plasmido(LX + 16, 300, 11, lobulos=5, amp=1.8, grosor=3),
         'El DNA va en el agua de dentro', 'el minicírculo con KRT10 flota en el interior,', 'protegido de las nucleasas'),
    ])

    # cómo entrega la carga
    out.append(f'<text x="{LX}" y="372" font-size="13.5" font-weight="bold" fill="{INK}">Cómo entrega la carga</text>')
    pasos(out, LX, 398, [('1', 'la célula lo capta', 'o se fusiona con ella'),
                         ('2', 'la vesícula se abre', 'dentro de la célula')], ancho=190, color=FOS_H)

    # diferencia con la LNP
    out.append(f'<rect x="{LX}" y="432" width="372" height="58" rx="8" fill="#f2f3f5"/>')
    out.append(f'<text x="{LX + 16}" y="454" font-size="11.5" font-weight="bold" fill="{INK}">'
               f'No es lo mismo que una nanopartícula lipídica</text>')
    out.append(f'<text x="{LX + 16}" y="472" font-size="10.5" fill="{GREY}">'
               f'el liposoma está hueco y lleva agua dentro;</text>')
    out.append(f'<text x="{LX + 16}" y="485" font-size="10.5" fill="{GREY}">'
               f'la LNP va rellena de lípido y DNA.</text>')

    pie(out)
    return out


# ----------------------------------------------------------- microemulsión
def gota(cx, cy, r, nl=None, cargas=True, detalle=False):
    """Una gota de aceite rodeada por una monocapa de tensioactivo."""
    piezas = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ACEITE}"/>']
    n = nl or max(8, int(r * 0.62))
    largo = max(8, r * 0.34)
    for i in range(n):
        a = 2 * math.pi * i / n - math.pi / 2
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        hr = max(3.2, r * 0.055)
        if detalle and i % 4 == 2:
            piezas.append(lipido(x, y, a + math.pi, COT_H, COT_T, hr=hr * 0.85,
                                 largo=largo * 0.6, colas=1))
        else:
            piezas.append(lipido(x, y, a + math.pi, CAT_H, CAT_T, hr=hr, largo=largo, colas=1))
            if cargas and r > 26 and i % 2 == 0:
                piezas.append(carga_mas(x, y, tam=hr * 1.5))
    return ''.join(piezas)


def microemulsion():
    out = lienzo('Microemulsión',
                 'gotas de aceite diminutas repartidas en agua, con el DNA pegado por fuera')

    # ---- panel del conjunto
    out.append(f'<rect x="40" y="104" width="248" height="330" rx="12" fill="{AGUA}" '
               f'stroke="#cfe0e9" stroke-width="1.5"/>')
    out.append(f'<text x="164" y="126" text-anchor="middle" font-size="11.5" font-weight="bold" '
               f'fill="{INK}">La mezcla, por fuera</text>')
    gotas = [(98, 178, 25), (182, 162, 17), (236, 212, 21), (112, 250, 19),
             (188, 246, 26), (250, 288, 14), (90, 320, 22), (164, 330, 16),
             (232, 362, 20), (122, 384, 15), (192, 396, 22)]
    for gx, gy, gr in gotas:
        out.append(gota(gx, gy, gr, cargas=False))
        a0 = (gx + gy) * 0.03
        out.append(hebra_pegada(gx, gy, gr + 7, a0, a0 + 3.9, amp=2.4, ondas=3.5, grosor=2.2))
    out.append(f'<text x="164" y="456" text-anchor="middle" font-size="10" fill="{GREY}">'
               f'transparente y estable: no hay que agitarla</text>')

    # ---- zoom de una gota
    out.append('<path d="M290,196 L372,150 M290,330 L372,420" stroke="#8a8f98" stroke-width="1.2" fill="none"/>')

    CX, CY, R = 494, 286, 104
    out.append(gota(CX, CY, R, nl=40, detalle=True))
    out.append(f'<text x="{CX}" y="{CY + 6}" text-anchor="middle" font-size="12.5" '
               f'font-weight="bold" fill="#b1832b">aceite</text>')
    out.append(f'<text x="{CX}" y="{CY + 22}" text-anchor="middle" font-size="10" fill="#b1832b">'
               f'el corazón de la gota</text>')

    # DNA pegado a la superficie
    out.append(hebra_pegada(CX, CY, R + 20, -2.7, 0.3, amp=5, ondas=4, grosor=4.0))
    out.append(hebra_pegada(CX, CY, R + 18, 1.5, 2.7, amp=4.5, ondas=2.5, grosor=4.0))
    out.append(hebra(CX - R - 14, CY + 62, CX - R - 58, CY + 96, amp=5, ondas=2, grosor=3.4))
    out.append(f'<text x="{CX}" y="{CY - R - 44}" text-anchor="middle" font-size="11.5" '
               f'font-weight="bold" fill="{NA}">el DNA se pega por fuera</text>')
    out.append(f'<text x="{CX}" y="{CY - R - 30}" text-anchor="middle" font-size="10" fill="{GREY}">'
               f'su carga − se une a la carga + de la gota</text>')
    out.append(f'<text x="{CX}" y="{CY + R + 48}" text-anchor="middle" font-size="11" fill="{GREY}">'
               f'≈ 10–100 nm</text>')

    # ---- leyenda
    LX = 638
    out.append(f'<text x="{LX}" y="128" font-size="13.5" font-weight="bold" fill="{INK}">De qué está hecha</text>')
    leyenda(out, LX, [
        (156, lipido(LX + 16, 146, math.pi / 2, CAT_H, CAT_T, hr=5.4, largo=20, colas=1)
         + carga_mas(LX + 16, 146, tam=8),
         'Tensioactivo catiónico', 'rodea la gota y le da carga +:', 'ahí es donde se engancha el DNA'),
        (216, lipido(LX + 16, 208, math.pi / 2, COT_H, COT_T, hr=4.8, largo=15, colas=1),
         'Cotensioactivo', 'una molécula pequeña que se cuela', 'entre las otras y lo hace estable'),
        (276, f'<circle cx="{LX + 16}" cy="272" r="11" fill="{ACEITE}" stroke="#d9bd80" stroke-width="1.5"/>',
         'Aceite', 'el interior de cada gota', ''),
        (322, f'<circle cx="{LX + 16}" cy="318" r="11" fill="{AGUA}" stroke="#bcd5e2" stroke-width="1.5"/>',
         'Agua', 'todo lo demás: es lo que se inyecta o', 'se aplica sobre la piel'),
    ])

    out.append(f'<rect x="{LX}" y="366" width="282" height="124" rx="8" fill="#f2f3f5"/>')
    out.append(f'<text x="{LX + 16}" y="390" font-size="12" font-weight="bold" fill="{INK}">'
               f'Por qué interesa</text>')
    for i, linea in enumerate(['se forma sola al mezclar: no hace falta',
                               'máquina ni energía',
                               'aguanta meses sin separarse',
                               'las gotas son tan pequeñas que la mezcla',
                               'se ve transparente']):
        out.append(f'<text x="{LX + 16}" y="{410 + i * 16}" font-size="10.5" fill="{GREY}">{linea}</text>')

    pie(out)
    return out


FIGURAS = {'liposoma': liposoma, 'microemulsion': microemulsion}

if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] not in FIGURAS:
        sys.exit(f'uso: {sys.argv[0]} [{" | ".join(FIGURAS)}] destino.svg')
    svg = '\n'.join(FIGURAS[sys.argv[1]]()) + '\n'
    with open(sys.argv[2], 'w', encoding='utf-8') as fh:
        fh.write(svg)
    print(f'escrito: {sys.argv[2]}')
