#!/usr/bin/env python3
"""Verifica una pareja de cebadores de clonaje In-Fusion contra los ficheros reales.

No diseña nada: coge los oligos que ya tienes escritos y comprueba, uno por uno,
que hacen lo que crees que hacen. Todo lo que imprime sale del fichero de
secuencia y del MCS que le pases; nada de memoria.

Uso típico (la pareja ClonK10MC del constructo 1):

    python3 verifica_oligos.py \\
        --donante ../secuencias/pCMV6-KRT10.dna \\
        --mcs tctagagctagcgaattcgaatttaaatcggatccgcggccgcgtcga \\
        --enzima BamHI-HF \\
        --f TTCGAATTTAAATCGGCCATGTCTGTTCGATACAGCTCAAGC \\
        --r ACGCGGCCGCGGATCTTATCAGTATCTTGGTCCCTTAGATGAAGACTCGCC

Con `--aceptor` (el GenBank del vector parental) comprueba además que la enzima
corta una sola vez en todo el plásmido, que es lo único que el MCS suelto no
puede decirte.

    python3 verifica_oligos.py --autotest
"""
from __future__ import annotations

import argparse
import sys

from enzimas import POR_NOMBRE
from formatos import lee
from seqlib import busca, busca_ambas, gc, limpia, rc, tm_nn, traduce

TM_MINIMA = 58.0          # Takara: la zona de apareo de un cebador In-Fusion
BRAZO = 15                # In-Fusion clásico: 15 nt de homología con el vector


class Informe:
    """Acumula comprobaciones para poder salir con código != 0 si algo falla."""

    def __init__(self) -> None:
        self.fallos = 0
        self.avisos = 0

    def ok(self, texto: str) -> None:
        print(f"  [ OK ]   {texto}")

    def fallo(self, texto: str) -> None:
        self.fallos += 1
        print(f"  [FALLO]  {texto}")

    def aviso(self, texto: str) -> None:
        self.avisos += 1
        print(f"  [AVISO]  {texto}")

    def comprueba(self, cond: bool, bien: str, mal: str) -> bool:
        (self.ok if cond else self.fallo)(bien if cond else mal)
        return cond


def titulo(t: str) -> None:
    print(f"\n{t}\n{'-' * len(t)}")


def descompon(primer: str, molde: str, hebra: int) -> tuple[str, str, list[int]]:
    """Parte el cebador en (cola 5' no apareante, zona de apareo, posiciones).

    Busca el sufijo 3' más largo que exista en la hebra indicada del molde.
    """
    diana = molde if hebra > 0 else rc(molde)
    for largo in range(len(primer), 9, -1):
        pos = busca(diana, primer[-largo:])
        if pos:
            return primer[:len(primer) - largo], primer[-largo:], pos
    return primer, "", []


def coords(pos0: int, largo: int, molde: str, hebra: int) -> tuple[int, int]:
    """Pasa una posición 0-based (en la hebra usada) a 1-based sobre la hebra +."""
    if hebra > 0:
        return pos0 + 1, pos0 + largo
    return len(molde) - (pos0 + largo) + 1, len(molde) - pos0


def analiza_cebador(inf: Informe, nombre: str, primer: str, molde: str, hebra: int,
                    brazo_esperado: str) -> dict:
    titulo(f"{nombre} — {len(primer)} nt")
    cola, apareo, pos = descompon(primer, molde, hebra)
    if not apareo:
        inf.fallo("no aparea en ningún sitio del molde")
        return {}
    ini, fin = coords(pos[0], len(apareo), molde, hebra)
    tm = tm_nn(apareo)

    print(f"  cola 5'  : {cola or '(ninguna)'}  ({len(cola)} nt)")
    print(f"  apareo   : {apareo}  ({len(apareo)} nt, GC {gc(apareo):.1f} %, Tm {tm:.1f} C)")
    print(f"  posición : {ini}..{fin} de la hebra {'+' if hebra > 0 else '-'}")
    print(f"  cebador entero: GC {gc(primer):.1f} %, Tm {tm_nn(primer):.1f} C")

    inf.comprueba(len(pos) == 1,
                  "la zona de apareo es única en el molde",
                  f"la zona de apareo sale {len(pos)} veces en el molde: mal cebado garantizado")
    inf.comprueba(tm >= TM_MINIMA,
                  f"Tm de apareo {tm:.1f} C >= {TM_MINIMA:.0f} C (mínimo de Takara)",
                  f"Tm de apareo {tm:.1f} C < {TM_MINIMA:.0f} C: alarga la zona de apareo")
    inf.comprueba(cola[:BRAZO] == brazo_esperado,
                  f"el brazo In-Fusion es exactamente {brazo_esperado}",
                  f"brazo {cola[:BRAZO]!r}, el vector cortado pide {brazo_esperado!r}")
    if primer[-1] in "GC":
        inf.ok("acaba en G/C (pinza 3')")
    else:
        inf.aviso("no acaba en G/C; no es grave pero la pinza 3' ayuda")
    return {"cola": cola, "apareo": apareo, "ini": ini, "fin": fin, "tm": tm}


def verifica(donante, mcs: str, enzima_nombre: str, f: str, r: str, aceptor=None) -> int:
    inf = Informe()
    seq = donante.seq
    enz = POR_NOMBRE.get(enzima_nombre)
    if enz is None:
        print(f"Enzima desconocida: {enzima_nombre}. Conocidas: {', '.join(sorted(POR_NOMBRE))}")
        return 2

    # ---------------------------------------------------------------- vector
    titulo(f"1. El vector abierto con {enz.nombre} ({enz.diana})")
    cortes = busca(mcs, enz.diana)
    print(f"  MCS aportado: {len(mcs)} nt")
    if not inf.comprueba(len(cortes) == 1,
                         f"{enz.diana} aparece una sola vez en el MCS (posición {cortes[0] + 1 if cortes else '-'})",
                         f"{enz.diana} aparece {len(cortes)} veces en el MCS"):
        return 1
    punto = cortes[0] + enz.corte
    izq, der = mcs[:punto], mcs[punto:]
    brazo5, brazo3 = izq[-BRAZO:], der[:BRAZO]
    print(f"  corte {enz.diana[:enz.corte]}^{enz.diana[enz.corte:]} entre {punto} y {punto + 1}")
    print(f"  extremo izquierdo ...{izq[-24:]}")
    print(f"  extremo derecho      {der[:24]}...")
    print(f"  brazo 5' que hace falta en F: {brazo5}")
    print(f"  brazo 3' que hace falta en R: {rc(brazo3)}   (sentido: {brazo3})")
    if aceptor is not None:
        n = len(busca(aceptor.seq, enz.diana, circular=aceptor.circular))
        inf.comprueba(n == 1,
                      f"{enz.nombre} corta una sola vez en el vector completo",
                      f"{enz.nombre} corta {n} veces en el vector completo: no sirve para linearizar")
    else:
        inf.aviso(f"sin --aceptor no se puede comprobar que {enz.nombre} corte UNA sola vez "
                  "en todo el vector; el MCS suelto no lo dice")

    # -------------------------------------------------------------- cebadores
    dF = analiza_cebador(inf, "Cebador directo (F)", f, seq, +1, brazo5)
    dR = analiza_cebador(inf, "Cebador reverso (R)", r, seq, -1, rc(brazo3))
    if not dF or not dR:
        return 1

    titulo("2. Orientación y amplicón")
    if not inf.comprueba(dF["ini"] < dR["fin"],
                         f"F ({dF['ini']}) queda aguas arriba de R ({dR['fin']}): la PCR produce algo",
                         "los cebadores apuntan hacia fuera: no hay amplicón"):
        return 1
    amp = dF["cola"] + seq[dF["ini"] - 1:dR["fin"]] + rc(dR["cola"])
    print(f"  amplicón: {len(amp)} pb   GC {gc(amp):.1f} %")
    print(f"  molde amplificado: {dF['ini']}..{dR['fin']} ({dR['fin'] - dF['ini'] + 1} nt)")
    inf.comprueba(amp[:BRAZO] == brazo5 and amp[-BRAZO:] == brazo3,
                  "los dos extremos del amplicón son homólogos al vector cortado",
                  "los extremos del amplicón no casan con el vector")
    dtm = abs(dF["tm"] - dR["tm"])
    (inf.ok if dtm <= 5 else inf.aviso)(f"diferencia de Tm entre F y R: {dtm:.1f} C")

    # ------------------------------------------------------------- constructo
    titulo("3. El constructo tras la In-Fusion")
    final = izq + amp[BRAZO:-BRAZO] + der
    print(f"  ventana reconstruida: {len(final)} nt "
          f"(MCS de {len(mcs)} + {len(final) - len(mcs)} pb de inserto neto)")
    print(f"  unión 5': ...{izq[-12:]} | {amp[BRAZO:BRAZO + 12]}...")
    print(f"  unión 3': ...{amp[-BRAZO - 12:-BRAZO]} | {der[:12]}...")
    quedan = busca_ambas(final, enz.diana)
    inf.comprueba(not quedan,
                  f"la diana {enz.nombre} queda destruida: digestión diagnóstica gratis "
                  "(el clon bueno no corta, el vector religado sí)",
                  f"la diana {enz.nombre} sobrevive en el constructo ({len(quedan)} copias)")

    titulo("4. Pauta de lectura")
    i_atg = final.find("ATG")
    utr = final[:i_atg]
    print(f"  5'UTR visible (dentro del MCS): {utr}")
    inf.comprueba("ATG" not in utr,
                  "ningún ATG por delante del iniciador dentro del MCS conocido",
                  "hay un ATG aguas arriba dentro del MCS: posible uORF")
    menos3, mas4 = final[i_atg - 3], final[i_atg + 3]
    print(f"  Kozak: {final[i_atg - 6:i_atg]}|{final[i_atg:i_atg + 4]}   -3 = {menos3}   +4 = {mas4}")
    inf.comprueba(menos3 in "AG",
                  f"-3 = {menos3}, purina: Kozak funcional",
                  f"-3 = {menos3}, pirimidina: Kozak débil, mete GCCACC o GCC delante del ATG")
    if mas4 != "G":
        inf.aviso(f"+4 = {mas4} (no G). Suele ser inevitable: es la 1a base del 2o codón")

    prot = traduce(final[i_atg:])
    stop = prot.find("*")
    inf.comprueba(stop > 0, f"ORF de {stop} aa hasta el primer stop",
                  "no hay codón de parada en pauta: el ribosoma se sale del inserto")
    if stop > 0:
        cierre = final[i_atg + stop * 3:i_atg + stop * 3 + 6]
        print(f"  proteína: {prot[:10]}... {prot[max(0, stop - 8):stop]}   cierre: {cierre}")
        (inf.ok if traduce(cierre) == "**" else inf.aviso)(
            f"codones de parada al final: {cierre} ({'doble' if traduce(cierre) == '**' else 'sencillo'})")
        inf.comprueba("*" not in prot[:stop],
                      "ningún stop interno", "hay un stop prematuro dentro de la ORF")

    # Comparación con la ORF anotada del donante, si la hay.
    for ra in donante.rasgos:
        et = (ra.etiqueta or "").lower()
        if "atg" in et or "inici" in et:
            nativa = traduce(seq[ra.inicio:])
            s2 = nativa.find("*")
            corte_nat = nativa[:s2 if s2 > 0 else None]
            if len(corte_nat) >= stop:
                igual = corte_nat[:stop] == prot[:stop]
                inf.comprueba(igual,
                              f"la proteína coincide con la del donante desde su ATG anotado ({stop} aa)",
                              "la proteína NO coincide con la traducción del donante")
            break

    titulo("5. Riesgo de PCR sobre el molde")
    peor = ("", 0.0, 0)
    paso = 150
    for i in range(0, max(1, len(amp) - paso), paso):
        tr = amp[i:i + paso * 2]
        vent = [tr[j:j + 20] for j in range(len(tr) - 19)]
        rep = len(vent) - len(set(vent))
        if gc(tr) > peor[1]:
            peor = (f"{i + 1}..{i + len(tr)}", gc(tr), rep)
    vent = [amp[j:j + 20] for j in range(len(amp) - 19)]
    print(f"  GC global {gc(amp):.1f} %   tramo más GC: {peor[0]} con {peor[1]:.1f} %")
    print(f"  ventanas de 20 nt repetidas en todo el amplicón: {len(vent) - len(set(vent))}")
    if peor[1] > 65:
        inf.aviso(f"hay un tramo al {peor[1]:.1f} % de GC: polimerasa de molde difícil "
                  "(PrimeSTAR GXL / Q5 con GC enhancer) y secuenciación completa de los clones")

    titulo("6. Resumen")
    print(f"  fallos: {inf.fallos}   avisos: {inf.avisos}")
    if inf.fallos == 0:
        print("  La pareja es correcta para lo que dice hacer.")
    return 1 if inf.fallos else 0


# ---------------------------------------------------------------------------
def autotest() -> int:
    """Comprobaciones internas, sin ficheros."""
    n = 0

    def chk(cond, que):
        nonlocal n
        n += 1
        if not cond:
            raise AssertionError(que)

    chk(rc("GATCCGCGGCCGCGT") == "ACGCGGCCGCGGATC", "rc del brazo 3'")
    mcs = limpia("tctagagctagcgaattcgaatttaaatcggatccgcggccgcgtcga")
    chk(len(mcs) == 48, "longitud del MCS de prueba")
    pos = busca(mcs, "GGATCC")
    chk(pos == [29], "BamHI en el MCS")
    punto = pos[0] + POR_NOMBRE["BamHI-HF"].corte
    chk(mcs[:punto][-15:] == "TTCGAATTTAAATCG", "brazo 5' derivado del corte")
    chk(mcs[punto:][:15] == "GATCCGCGGCCGCGT", "brazo 3' derivado del corte")

    izq_ap = "ATGTCTGTTCGATACAGCTCAAGC"                 # 24 nt
    der_ap = "GGCGAGTCTTCATCTAAGGGACCAAGATAC"           # 30 nt
    medio = "CATCACGATTGCAAGTCCATGGATCCTAGCAT"
    molde = "AAAATTA" + izq_ap + medio + der_ap + "TTTTGGG"
    cola, apareo, p = descompon("CCCCC" + izq_ap, molde, +1)
    chk(cola == "CCCCC" and apareo == izq_ap, "descomposición del directo")
    chk(coords(p[0], len(apareo), molde, +1) == (8, 31), "coordenadas 1-based del directo")
    colaR, apR, pR = descompon("GGGG" + rc(der_ap), molde, -1)
    chk(colaR == "GGGG" and apR == rc(der_ap), "descomposición del reverso")
    ini_r, fin_r = coords(pR[0], len(apR), molde, -1)
    chk((ini_r, fin_r) == (molde.find(der_ap) + 1, molde.find(der_ap) + len(der_ap)),
        "coordenadas del reverso sobre la hebra +")
    chk(ini_r > 31, "el reverso queda aguas abajo del directo")

    # Si la cola añadida coincide por casualidad con el molde, la zona de apareo
    # es más larga de lo que uno escribió. Es lo que pasa con el Kozak GCC de
    # ClonK10MC_F: el pCMV6 ya lleva GCC justo delante del ATG.
    cola2, ap2, _ = descompon("CCCCCTTA" + izq_ap, molde, +1)
    chk(cola2 == "CCCCC" and ap2 == "TTA" + izq_ap, "la cola que coincide cuenta como apareo")

    chk(traduce("TGATAA") == "**", "doble stop")
    chk(tm_nn("GCCATGTCTGTTCGATACAGCTCAAGC") > TM_MINIMA, "Tm de la zona de apareo de ejemplo")
    print(f"autotest: {n} comprobaciones OK")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--donante", help="fichero del plásmido molde (.dna, .gb o .fa)")
    p.add_argument("--aceptor", help="fichero del vector parental, para comprobar el corte único")
    p.add_argument("--mcs", help="secuencia del MCS del vector parental")
    p.add_argument("--enzima", default="BamHI-HF", help="enzima con la que se linealiza (por defecto BamHI-HF)")
    p.add_argument("--f", help="cebador directo")
    p.add_argument("--r", help="cebador reverso")
    p.add_argument("--autotest", action="store_true")
    a = p.parse_args()

    if a.autotest:
        return autotest()
    if not (a.donante and a.mcs and a.f and a.r):
        p.error("hacen falta --donante, --mcs, --f y --r (o --autotest)")

    donante = lee(a.donante)
    aceptor = lee(a.aceptor) if a.aceptor else None
    print(f"molde: {donante.nombre} — {len(donante.seq)} pb ({a.donante})")
    return verifica(donante, limpia(a.mcs), a.enzima, limpia(a.f), limpia(a.r), aceptor)


if __name__ == "__main__":
    sys.exit(main())
