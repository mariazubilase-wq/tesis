#!/usr/bin/env python3
"""Construye y valida las parejas de oligos de shRNA para el minicírculo con GFP.

Vector: pMC.CMV-GFP-H1-MCS (System Biosciences), promotor H1 (Pol III).
MCS conocido: GGATCC TCT GAATTC  ->  BamHI y EcoRI separados por 3 nt.

Plantilla del fabricante (de su figura):

  5'-GATCC [sentido N21] CTTCCTGTCAGA [antisentido N21] TTTTTG   -3'
  3'-    G [           ] GAAGGACAGTCT [                ] AAAAACTTAA-5'
      ^^^^                                                       ^^^^
      saliente BamHI + C de relleno            terminador Pol III + G de EcoRI

La C tras GATC NO es parte de la diana: completa el GGATCC al ligar, porque
el vector sólo aporta la primera G del sitio.

Uso:
  python3 disena_shrna.py --salida ../secuencias/pedido_oligos_shrna.txt
  python3 disena_shrna.py --autotest
"""
from __future__ import annotations

import argparse
import re
import sys

MCS = "GGATCCTCTGAATTC"        # tal como lo da SBI
LAZO_SBI = "CTTCCTGTCAGA"      # lazo del fabricante, 12 nt
RELLENO_BAM = "C"              # completa GGATCC en la unión
TERMINADOR = "TTTTTG"          # 5 T (Pol III) + G que completa GAATTC
SALIENTE_BAM = "GATC"
SALIENTE_ECO = "AATT"

# Dianas de 21 nt. El scramble es la secuencia clásica del pLKO.1-scramble
# (Addgene 1864); sh13 es la horquilla del proyecto.
DIANAS = {
    "sh13":   ("AATGACTGCCTGGCTTCCTTT", "horquilla 13 del proyecto"),
    "shSCR":  ("CCTAAGGTTAAGTCGCCCTCG", "control no diana (scramble, Addgene 1864)"),
}


def revcomp(s: str) -> str:
    return s.translate(str.maketrans("ACGT", "TGCA"))[::-1]


def construye(diana: str, lazo: str = LAZO_SBI) -> tuple[str, str]:
    """Devuelve (TOP, BOT), ambos 5'->3', listos para pedir."""
    top = SALIENTE_BAM + RELLENO_BAM + diana + lazo + revcomp(diana) + TERMINADOR
    bot = SALIENTE_ECO + revcomp(top[len(SALIENTE_BAM):])
    return top, bot


def mcs_reconstruido(top: str) -> str:
    """MCS tras la ligación: la G del vector + inserto + AATTC del vector."""
    return MCS[:1] + top + "AATTC"


def valida(nombre: str, diana: str, top: str, bot: str) -> list[tuple[bool, str]]:
    """Cada comprobación como (pasa, descripción). Ninguna debe fallar."""
    nucleo = top[len(SALIENTE_BAM):]          # lo que queda apareado
    union = mcs_reconstruido(top)
    transcrito = nucleo                        # lo que lee H1, sin líder del vector
    antisentido = revcomp(diana)
    # región que se transcribe antes del terminador: relleno + tallo + lazo
    previo = nucleo[:-len(TERMINADOR)]

    c = []
    c.append((len(diana) == 21, f"diana de 21 nt (son {len(diana)})"))
    c.append((set(diana) <= set("ACGT"), "diana sin bases ambiguas"))
    c.append((bot == SALIENTE_ECO + revcomp(nucleo),
              "BOT es el complementario inverso exacto del TOP"))
    c.append((len(top) == len(bot), f"TOP y BOT igual longitud ({len(top)} nt)"))
    c.append((top.startswith(SALIENTE_BAM), "saliente BamHI GATC en el TOP"))
    c.append((bot.startswith(SALIENTE_ECO), "saliente EcoRI AATT en el BOT"))
    c.append(("GGATCC" in union, "BamHI se regenera al ligar"))
    c.append((union.count("GAATTC") == 1, "EcoRI se regenera al ligar (1 copia)"))
    c.append((nucleo.count("GGATCC") == 0 and revcomp(nucleo).count("GGATCC") == 0,
              "sin BamHI interno"))
    c.append((nucleo.count("GAATTC") == 0 and revcomp(nucleo).count("GAATTC") == 0,
              "sin EcoRI interno"))
    c.append((not re.search(r"T{4,}", previo),
              "sin tiradas de >=4 T antes del terminador (no termina antes de tiempo)"))
    c.append((TERMINADOR.count("T") == 5, "terminador Pol III de 5 T"))
    c.append((revcomp(diana) == antisentido, "antisentido = complementario inverso"))
    c.append((LAZO_SBI in top, "lazo del fabricante presente"))
    c.append((diana not in LAZO_SBI and lazo_libre(diana), "lazo no solapa con la diana"))
    gc = 100 * (diana.count("G") + diana.count("C")) / len(diana)
    c.append((30 <= gc <= 65, f"GC de la diana en rango 30-65 % (es {gc:.0f} %)"))
    c.append((len(transcrito) == 1 + 21 + len(LAZO_SBI) + 21 + len(TERMINADOR),
              "longitud del transcrito coherente"))
    return c


def lazo_libre(diana: str) -> bool:
    """El lazo no debe aparearse con los brazos mejor que en 6 pb."""
    comp = revcomp(LAZO_SBI)
    for k in range(7, len(comp) + 1):
        for i in range(len(comp) - k + 1):
            if comp[i:i + k] in diana or comp[i:i + k] in revcomp(diana):
                return False
    return True


def informe(nombre: str, diana: str, nota: str, lazo: str = LAZO_SBI) -> tuple[str, bool]:
    top, bot = construye(diana, lazo)
    pruebas = valida(nombre, diana, top, bot)
    ok = all(p for p, _ in pruebas)
    antis = revcomp(diana)

    L = []
    L.append(f"{nombre}  —  {nota}")
    L.append("-" * 72)
    L.append(f"  {nombre}_TOP   5'-{top}-3'   ({len(top)} nt)")
    L.append(f"  {nombre}_BOT   5'-{bot}-3'   ({len(bot)} nt)")
    L.append("")
    L.append("  desglose del TOP:")
    L.append(f"    GATC              saliente BamHI")
    L.append(f"    C                 relleno, completa GGATCC al ligar")
    L.append(f"    {diana}   hebra sentido (21 nt)")
    L.append(f"    {lazo}      lazo del fabricante")
    L.append(f"    {antis}   hebra antisentido (21 nt)")
    L.append(f"    TTTTT + G         terminador Pol III + G que completa GAATTC")
    L.append("")
    L.append(f"  MCS tras la ligación:  {mcs_reconstruido(top)}")
    L.append(f"  inserción neta:        +{len(mcs_reconstruido(top)) - len(MCS)} pb")
    L.append("")
    L.append("  comprobaciones:")
    for pasa, texto in pruebas:
        L.append(f"    [{'ok' if pasa else 'FALLA'}] {texto}")
    return "\n".join(L), ok


CABECERA = """\
PEDIDO DE OLIGOS — shRNA en pMC.CMV-GFP-H1-MCS
===============================================

Vector    : pMC.CMV-GFP-H1-MCS Parental Minicircle shRNA Cloning Vector (SBI)
Promotor  : H1 (RNA Pol III)
MCS       : GGATCC TCT GAATTC   (BamHI y EcoRI separados por 3 nt)
Plantilla : la del fabricante — GATCC [sentido] CTTCCTGTCAGA [antisentido] TTTTTG

Pedir los 4 oligos con PURIFICACIÓN PAGE (son 65-meros; el desalado estándar
arrastra truncados n-1 que meten deleciones de un nucleótido en la horquilla).
Escala 25 nmol sobra.
"""

PIE = """\
PROTOCOLO (resumido)
--------------------
1. Anillar cada pareja: 10 uM de cada oligo en tampón de anillado, 95 C 5 min,
   enfriar hasta 25 C a ~1 C/min.
2. Fosforilar con T4 PNK (los oligos sintéticos llegan con 5'-OH).
3. Vector: digerir PRIMERO con BamHI-HF, DESPUÉS añadir EcoRI-HF (ambas en
   rCutSmart). Ese orden deja 8 nt de flanco a la segunda enzima en vez de 4.
4. Desfosforilar el vector con rSAP — rSAP y no CIP, porque la rSAP se
   inactiva del todo a 65 C/5 min y la CIP residual comería los fosfatos
   del inserto.
5. Gel-purificar el vector lineal.
6. Ligar, SIEMPRE con un control de vector solo sin inserto.

Por qué los pasos 2+4: entre BamHI y EcoRI sólo hay 3 nt, así que el doble
digerido libera un relleno de 9 nt. Eso significa que en un gel NO puedes
distinguir vector cortado una vez de cortado dos veces, y el cortado una vez
religa. Con el vector desfosforilado no puede religar pase lo que pase; el
inserto aporta sus fosfatos y el círculo queda con dos mellas, que E. coli
repara sin problema. El control sin inserto te mide el fondo.

CRIBADO
-------
La inserción es de +56 pb sobre un plásmido de varias kb: NO se ve por tamaño
de miniprep. Usar:
  * PCR de colonia con un cebador en H1 y otro aguas abajo (vacío vs +56 pb,
    resoluble en agarosa al 2-3 % si el amplicón es corto), y
  * confirmación por Sanger desde H1 en los dos clones. Obligatoria.
El lazo del fabricante no aporta ninguna diana de restricción útil, así que
no hay atajo por digestión.

PENDIENTE — pedir a soporte técnico de SBI el GenBank completo del vector
-------------------------------------------------------------------------
Sin el mapa no se puede comprobar:
  1. cuántos nt hay entre el +1 de H1 y el BamHI (longitud del líder 5' que
     queda pegado a la horquilla),
  2. que BamHI y EcoRI sean de corte único en todo el plásmido,
  3. que el casete H1-shRNA caiga DENTRO de la región attB-attP — si queda
     fuera no acaba en el minicírculo y lo demás da igual.

Comprobar además en el manual si el fabricante especifica brazos de 19 o de
21 nt. Aquí se han usado 21, que es lo que se cuenta en su figura.
"""


def genera(lazo: str = LAZO_SBI) -> tuple[str, bool]:
    partes, todo_ok = [CABECERA], True
    for nombre, (diana, nota) in DIANAS.items():
        texto, ok = informe(nombre, diana, nota, lazo)
        partes.append(texto)
        todo_ok &= ok
    partes.append(PIE)
    return "\n\n".join(partes), todo_ok


def autotest() -> int:
    fallos = 0

    def check(cond, msg):
        nonlocal fallos
        if not cond:
            print(f"  FALLA: {msg}")
            fallos += 1

    # el ejemplo de la figura del fabricante, con N genéricas
    top, bot = construye("A" * 21)
    check(top.startswith("GATCC"), "el TOP empieza por GATCC (saliente + relleno)")
    check(top.endswith("TTTTTG"), "el TOP acaba en TTTTTG")
    check(bot.startswith("AATTC"), "el BOT empieza por AATTC")
    check(len(top) == 65 and len(bot) == 65, "65 nt por oligo con brazos de 21")

    # anillado: el núcleo debe ser doble cadena perfecta
    for nombre, (diana, _) in DIANAS.items():
        top, bot = construye(diana)
        nucleo = top[4:]
        check(bot[4:] == revcomp(nucleo), f"{nombre}: BOT complementa al TOP")
        check(len(nucleo) == 61, f"{nombre}: 61 pb apareadas")
        union = mcs_reconstruido(top)
        check("GGATCC" in union, f"{nombre}: BamHI regenerado")
        check(union.count("GAATTC") == 1, f"{nombre}: EcoRI regenerado")
        check(len(union) - len(MCS) == 56, f"{nombre}: inserción neta de +56 pb")
        check(not re.search(r"T{4,}", nucleo[:-6]),
              f"{nombre}: sin terminación prematura")
        for pasa, texto in valida(nombre, diana, top, bot):
            check(pasa, f"{nombre}: {texto}")

    # el relleno importa: sin él, una diana que empiece por A no regenera BamHI
    sin_relleno = "GATC" + "AATGACTGCCTGGCTTCCTTT"
    check("GGATCC" not in MCS[:1] + sin_relleno,
          "sin la C de relleno y diana que empieza por A, no hay BamHI (control negativo)")
    # ...pero una que empiece por C sí, por accidente
    con_c = "GATC" + "CCTAAGGTTAAGTCGCCCTCG"
    check("GGATCC" in MCS[:1] + con_c,
          "sin relleno pero con diana que empieza por C, el BamHI sale por accidente")

    # revcomp es involutivo
    check(revcomp(revcomp("ACGTACGT")) == "ACGTACGT", "revcomp involutivo")

    print(f"autotest: {'TODO OK' if not fallos else str(fallos) + ' fallo(s)'}")
    return 1 if fallos else 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--salida", help="fichero donde escribir el pedido")
    p.add_argument("--autotest", action="store_true", help="ejecuta las comprobaciones")
    a = p.parse_args()

    if a.autotest:
        return autotest()

    texto, ok = genera()
    if a.salida:
        with open(a.salida, "w", encoding="utf-8") as fh:
            fh.write(texto)
        print(f"escrito: {a.salida}")
    else:
        print(texto)
    if not ok:
        print("\nATENCIÓN: alguna comprobación ha fallado.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
