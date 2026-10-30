#!/usr/bin/env python3
"""Simula una PCR y el clonaje del amplicón en un plásmido, y escribe el `.dna`.

Complementa a `disena_clonaje.py`: aquélla **diseña** (elige la pareja de enzimas
y calcula los cebadores); ésta **ejecuta el experimento en el ordenador** con los
cebadores ya decididos y devuelve el plásmido resultante como `.dna` de SnapGene
(lo abre el Viewer gratuito) y como GenBank.

Lo que hace, en orden:

1. **PCR.** Localiza la zona de apareamiento de cada cebador en el molde —la cola
   5' no aparea— y construye el amplicón: cola directa + región amplificada +
   complementario inverso de la cola reversa. Avisa si algún cebador tiene más de
   un sitio de apareamiento plausible.
2. **Digestión.** Corta amplicón y vector con la pareja de enzimas y **exige que
   cada diana sea única en los dos**. Si no lo es, se para: eso es un clonaje que
   no sale.
3. **Ligación direccional.** Une los extremos cohesivos homólogos y cierra el
   círculo. Comprueba que las dos dianas se regeneran en las uniones.
4. **Anotación.** Arrastra los rasgos del vector y del inserto a las coordenadas
   nuevas, anota las uniones, los cebadores retenidos, el Kozak y el ORF.
5. **Salida.** `.dna`, `.gb` y un informe en Markdown con las uniones, la
   traducción de los extremos del ORF y las digestiones diagnósticas.

Uso típico (cebadores ya diseñados):

    python3 simula_clonaje.py \\
        --aceptor  ../secuencias/pMC.EF1a-MCS-SV40polyA.gb \\
        --donante  ../secuencias/pCMV6-KRT10.gb \\
        --directo  CACCACGCTAGCGCCACCATGTCTGTTCGATACAGCTCA \\
        --reverso  CACCACGGATCCTCATTAGTTCTGGATTGACTCCTCCAG \\
        --enzimas  NheI-HF,BamHI-HF \\
        --nombre   pMC.EF1a-KRT10-SV40polyA \\
        --salida   ../resultados

Sin ficheros a mano:

    python3 simula_clonaje.py --demo       # ejemplo completo en ../resultados
    python3 simula_clonaje.py --autotest   # comprobaciones internas

Python >= 3.9. Sin dependencias externas. No accede a internet.
"""
from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass, field

from enzimas import POR_NOMBRE, PANEL_NEVERA, TODAS
from formatos import Rasgo, Registro, escribe_genbank, lee
from seqlib import busca, busca_ambas, gc, limpia, rc, tm_nn, traduce
from snapgene import escribe_dna

MIN_APAREAMIENTO = 12
# Por debajo de esto un "solape" es coincidencia, no un brazo de homología:
# ningún método de ensamblado por homología funciona con tan poco.
SUELO_SOLAPE = 8


class ErrorClonaje(Exception):
    """Algo que haría fracasar el clonaje de verdad, no sólo el programa."""


# ---------------------------------------------------------------------------
# Utilidades de rasgos
# ---------------------------------------------------------------------------

def _desplaza(r: Rasgo, d: int, etiqueta_extra: str = "") -> Rasgo:
    cual = dict(r.cualificadores)
    if etiqueta_extra:
        cual["note"] = (cual.get("note", "") + " " + etiqueta_extra).strip()
    return Rasgo(r.clave, r.inicio + d, r.fin + d, r.hebra, r.etiqueta, cual, r.compuesto)


def rota(registro: Registro, n: int) -> tuple[Registro, list[str]]:
    """Renumera un plásmido circular para que la base `n` (0-based) sea la 1."""
    if not registro.circular:
        raise ErrorClonaje("no se puede renumerar una molécula lineal")
    L = len(registro.seq)
    n %= L
    if n == 0:
        return registro, []
    seq = registro.seq[n:] + registro.seq[:n]
    nuevos, avisos = [], []
    for r in registro.rasgos:
        i, f = r.inicio - n, r.fin - n
        if i < 0 and f > 0:
            avisos.append(f"rasgo «{r.etiqueta or r.clave}» descartado: cruza el nuevo origen")
            continue
        if i < 0:
            i, f = i + L, f + L
        nuevos.append(Rasgo(r.clave, i, f, r.hebra, r.etiqueta,
                            dict(r.cualificadores), r.compuesto))
    return Registro(registro.nombre, seq, True, nuevos, registro.procedencia), avisos


# ---------------------------------------------------------------------------
# PCR
# ---------------------------------------------------------------------------

@dataclass
class Apareamiento:
    inicio: int          # 0-based en la hebra superior del molde
    largo: int
    cola: str            # porción 5' que no aparea
    hebra: int


def apareamiento(molde: Registro, cebador: str, hebra: int) -> Apareamiento:
    """Zona de apareamiento más larga e inequívoca del extremo 3' del cebador."""
    p = limpia(cebador)
    if len(p) < MIN_APAREAMIENTO:
        raise ErrorClonaje(f"cebador demasiado corto: {p}")
    for L in range(len(p), MIN_APAREAMIENTO - 1, -1):
        diana = p[-L:] if hebra == 1 else rc(p[-L:])
        pos = busca(molde.seq, diana, molde.circular)
        if len(pos) == 1:
            return Apareamiento(pos[0], L, p[:len(p) - L], hebra)
        if len(pos) > 1:
            raise ErrorClonaje(
                f"el cebador {'directo' if hebra == 1 else 'reverso'} aparea en "
                f"{len(pos)} sitios con sus últimos {L} nt (posiciones {pos[:5]}). "
                "Hay que rediseñarlo.")
    raise ErrorClonaje(
        f"el cebador {'directo' if hebra == 1 else 'reverso'} no aparea en el molde "
        f"(se han probado colas de hasta {MIN_APAREAMIENTO} nt). "
        "¿Es el molde correcto? ¿Está el cebador en la orientación correcta?")


def avisos_inespecificidad(molde: Registro, cebador: str) -> list[str]:
    """Sitios adicionales donde los últimos 15 nt podrían anclar."""
    cola3 = limpia(cebador)[-15:]
    n = len(busca_ambas(molde.seq, cola3, molde.circular))
    if n > 1:
        return [f"los últimos 15 nt de un cebador aparecen {n} veces en el molde "
                "(contando las dos hebras): posible producto secundario"]
    return []


@dataclass
class ResultadoPCR:
    amplicon: Registro
    directo: str
    reverso: str
    ap_directo: Apareamiento
    ap_reverso: Apareamiento
    avisos: list[str] = field(default_factory=list)


def pcr(molde: Registro, directo: str, reverso: str) -> ResultadoPCR:
    directo, reverso = limpia(directo), limpia(reverso)
    af = apareamiento(molde, directo, 1)
    ar = apareamiento(molde, reverso, -1)

    ini = af.inicio
    fin = ar.inicio + ar.largo          # exclusivo, hebra superior
    envuelve = False
    if fin <= ini:
        if not molde.circular:
            raise ErrorClonaje(
                "los cebadores apuntan hacia fuera: en un molde lineal no amplifican. "
                f"(directo en {ini + 1}, reverso acaba en {fin})")
        region = molde.seq[ini:] + molde.seq[:fin]
        envuelve = True
    else:
        region = molde.seq[ini:fin]

    if len(region) < af.largo + ar.largo:
        raise ErrorClonaje("los cebadores se solapan: no hay producto")

    seq = af.cola + region + rc(ar.cola)
    d = len(af.cola) - ini

    avisos: list[str] = []
    avisos += avisos_inespecificidad(molde, directo)
    avisos += avisos_inespecificidad(molde, reverso)

    rasgos = []
    for r in molde.rasgos:
        if envuelve:
            continue
        if r.inicio >= ini and r.fin <= fin:
            rasgos.append(_desplaza(r, d))
        elif r.fin > ini and r.inicio < fin:
            avisos.append(f"rasgo «{r.etiqueta or r.clave}» del molde queda cortado "
                          "por la PCR: no se arrastra al amplicón")
    if envuelve:
        avisos.append("el amplicón cruza el origen numérico del molde: "
                      "los rasgos del molde no se arrastran")

    rasgos.append(Rasgo("primer_bind", 0, len(directo), 1, "cebador directo",
                        {"note": f"cola 5' de {len(af.cola)} nt + "
                                 f"{af.largo} nt de apareamiento"}))
    rasgos.append(Rasgo("primer_bind", len(seq) - len(reverso), len(seq), -1,
                        "cebador reverso",
                        {"note": f"cola 5' de {len(ar.cola)} nt + "
                                 f"{ar.largo} nt de apareamiento"}))

    amp = Registro(f"amplicon_{molde.nombre}", seq, False, rasgos,
                   f"PCR sobre {molde.procedencia or molde.nombre}")
    return ResultadoPCR(amp, directo, reverso, af, ar, avisos)


# ---------------------------------------------------------------------------
# Digestión
# ---------------------------------------------------------------------------

@dataclass
class Corte:
    diana: int        # 0-based, inicio de la diana
    arriba: int       # corte en la hebra superior (coordenada entre bases)
    abajo: int        # corte en la hebra inferior, en coordenadas de la superior


def cortes(registro: Registro, enz) -> list[Corte]:
    if enz.diana != rc(enz.diana):
        raise NotImplementedError(
            f"{enz.nombre} tiene diana no palindrómica: no está contemplado")
    fuera = []
    for p in busca_ambas(registro.seq, enz.diana, registro.circular):
        fuera.append(Corte(p, p + enz.corte, p + len(enz.diana) - enz.corte))
    return fuera


def corte_unico(registro: Registro, enz, que_es: str) -> Corte:
    cs = cortes(registro, enz)
    if not cs:
        raise ErrorClonaje(f"{enz.nombre} no corta en {que_es} ({registro.nombre})")
    if len(cs) > 1:
        posiciones = ", ".join(str(c.diana + 1) for c in cs[:8])
        raise ErrorClonaje(
            f"{enz.nombre} corta {len(cs)} veces en {que_es} ({registro.nombre}): "
            f"posiciones {posiciones}. Con esta pareja el clonaje direccional no "
            "funciona; hay que cambiar de enzima.")
    return cs[0]


def pareja_que_flanquea(producto: Registro, ins_ini: int, ins_fin: int):
    """Pareja de enzimas únicas que flanquea el inserto, la más ajustada posible.

    Devuelve (arriba, abajo, en_nevera) o None. Prioriza el panel del congelador:
    una pareja que haya que comprar sirve de poco esta semana.
    """
    def busca_en(panel):
        arriba, abajo = [], []
        for e in panel:
            try:
                cs = cortes(producto, e)
            except NotImplementedError:
                continue
            if len(cs) != 1:
                continue
            c = cs[0].arriba
            if c <= ins_ini:
                arriba.append((ins_ini - c, e))
            elif c >= ins_fin:
                abajo.append((c - ins_fin, e))
        if arriba and abajo:
            return min(arriba)[1], min(abajo)[1]
        return None

    p = busca_en(PANEL_NEVERA)
    if p:
        return p[0], p[1], True
    p = busca_en(TODAS)
    if p:
        return p[0], p[1], False
    return None


def fragmentos_multiple(registro: Registro, enzimas) -> list[int]:
    """Tamaños de fragmento de una digestión con varias enzimas a la vez."""
    puntos = sorted({c.arriba % len(registro.seq)
                     for e in enzimas for c in cortes(registro, e)})
    if not puntos:
        return [len(registro.seq)]
    if registro.circular:
        if len(puntos) == 1:
            return [len(registro.seq)]
        return sorted((puntos[(i + 1) % len(puntos)] - p) % len(registro.seq)
                      for i, p in enumerate(puntos))
    bordes = [0] + puntos + [len(registro.seq)]
    return sorted(b - a for a, b in zip(bordes, bordes[1:]) if b > a)


def fragmentos(registro: Registro, enz) -> list[int]:
    """Tamaños de fragmento de una digestión completa (para el gel diagnóstico)."""
    puntos = sorted(c.arriba % len(registro.seq) for c in cortes(registro, enz))
    if not puntos:
        return [len(registro.seq)]
    if registro.circular:
        return sorted((puntos[(i + 1) % len(puntos)] - p) % len(registro.seq) or
                      len(registro.seq)
                      for i, p in enumerate(puntos))
    bordes = [0] + puntos + [len(registro.seq)]
    return sorted(b - a for a, b in zip(bordes, bordes[1:]) if b > a)


# ---------------------------------------------------------------------------
# Ligación
# ---------------------------------------------------------------------------

@dataclass
class ResultadoClonaje:
    producto: Registro
    amplicon: Registro
    aceptor: Registro
    inserto: str
    enz5: object
    enz3: object
    union5: int           # coordenada 0-based del inicio de la unión 5'
    union3: int
    avisos: list[str] = field(default_factory=list)
    pcr: ResultadoPCR | None = None
    mecanismo: str = "restriccion"      # "restriccion" | "solapes"
    etiqueta5: str = ""
    etiqueta3: str = ""


def liga(aceptor: Registro, res_pcr: ResultadoPCR, enz5, enz3,
         nombre: str = "") -> ResultadoClonaje:
    """Clonaje direccional: corta los dos, mete el inserto, cierra el círculo."""
    if not aceptor.circular:
        raise ErrorClonaje("el aceptor tiene que ser circular")
    if enz5.saliente_seq() == enz3.saliente_seq():
        cual = enz5.saliente_seq() or "extremos romos"
        raise ErrorClonaje(
            f"{enz5.nombre} y {enz3.nombre} dejan el mismo extremo ({cual}): el "
            "inserto entraría en las dos orientaciones y el vector se cerraría "
            "solo. El clonaje no es direccional; cambia la pareja.")

    avisos: list[str] = []
    amp = res_pcr.amplicon

    # --- Cortes, exigiendo unicidad en los dos ---
    c5v = corte_unico(aceptor, enz5, "el vector")
    c3v = corte_unico(aceptor, enz3, "el vector")
    corte_unico(amp, enz5, "el amplicón")
    corte_unico(amp, enz3, "el amplicón")

    # Dos cosas obligan a renumerar el vector antes de cortar:
    #   a) que una diana quede partida por el origen numérico del fichero;
    #   b) que la diana 3' preceda a la 5', con lo que el fragmento «de en medio»
    #      sería casi todo el plásmido en vez del MCS.
    # Se renumera poniendo la base 1 en el inicio de la diana 5'.
    parte_origen = any(c.diana + len(e.diana) > len(aceptor.seq)
                       for c, e in ((c5v, enz5), (c3v, enz3)))
    if parte_origen or c5v.arriba > c3v.arriba:
        motivo = ("una diana queda partida por el origen numérico del fichero"
                  if parte_origen else
                  f"la diana de {enz5.nombre} va después de la de {enz3.nombre}")
        antigua = c5v.diana
        aceptor, av = rota(aceptor, antigua)
        avisos.append(f"vector renumerado ({motivo}): la base 1 pasa a ser la "
                      f"antigua {antigua + 1}")
        avisos += av
        c5v = corte_unico(aceptor, enz5, "el vector")
        c3v = corte_unico(aceptor, enz3, "el vector")
        if c5v.arriba > c3v.arriba:
            raise ErrorClonaje(
                f"en el vector la diana de {enz3.nombre} está delante de la de "
                f"{enz5.nombre}: con esta pareja el inserto entraría al revés "
                "respecto al promotor. Intercambia las dos enzimas (y los "
                "cebadores) o cambia de pareja.")

    c5i = corte_unico(amp, enz5, "el amplicón")
    c3i = corte_unico(amp, enz3, "el amplicón")
    if c5i.arriba > c3i.arriba:
        raise ErrorClonaje(
            f"en el amplicón la diana de {enz5.nombre} va después de la de "
            f"{enz3.nombre}: los cebadores están intercambiados.")

    inserto = amp.seq[c5i.arriba:c3i.arriba]
    perdido_vector = c3v.arriba - c5v.arriba
    if perdido_vector > 200:
        avisos.append(f"la digestión del vector elimina {perdido_vector} pb entre "
                      "las dos dianas: comprueba que sólo sea el MCS")

    seq = aceptor.seq[:c5v.arriba] + inserto + aceptor.seq[c3v.arriba:]
    d_cola = c5v.arriba + len(inserto) - c3v.arriba     # para los rasgos de cola

    # --- Comprobación: las dos dianas se regeneran ---
    u5 = c5v.arriba - enz5.corte
    u3 = c5v.arriba + len(inserto) - enz3.corte
    if seq[u5:u5 + len(enz5.diana)] != enz5.diana:
        raise ErrorClonaje(f"la unión 5' no regenera la diana de {enz5.nombre}: "
                           f"{seq[u5:u5 + len(enz5.diana)]}")
    if seq[u3:u3 + len(enz3.diana)] != enz3.diana:
        raise ErrorClonaje(f"la unión 3' no regenera la diana de {enz3.nombre}: "
                           f"{seq[u3:u3 + len(enz3.diana)]}")

    # --- Rasgos ---
    rasgos: list[Rasgo] = []
    for r in aceptor.rasgos:
        if r.fin <= c5v.arriba:
            rasgos.append(_desplaza(r, 0))
        elif r.inicio >= c3v.arriba:
            rasgos.append(_desplaza(r, d_cola))
        else:
            avisos.append(f"rasgo «{r.etiqueta or r.clave}» del vector descartado: "
                          "cae en el fragmento que se sustituye")

    d_ins = c5v.arriba - c5i.arriba
    for r in amp.rasgos:
        if r.clave == "primer_bind":
            continue
        if r.inicio >= c5i.arriba and r.fin <= c3i.arriba:
            rasgos.append(_desplaza(r, d_ins))
        elif r.fin > c5i.arriba and r.inicio < c3i.arriba:
            avisos.append(f"rasgo «{r.etiqueta or r.clave}» del inserto queda "
                          "cortado por la digestión")

    rasgos.append(Rasgo("misc_feature", u5, u5 + len(enz5.diana), 1,
                        f"unión 5' ({enz5.nombre})",
                        {"note": "diana regenerada en la ligación"}))
    rasgos.append(Rasgo("misc_feature", u3, u3 + len(enz3.diana), 1,
                        f"unión 3' ({enz3.nombre})",
                        {"note": "diana regenerada en la ligación"}))
    rasgos.append(Rasgo("misc_feature", c5v.arriba, c5v.arriba + len(inserto), 1,
                        "inserto", {"note": f"amplicón digerido, {len(inserto)} pb"}))

    # Cebadores: sólo la parte que sobrevive a la digestión.
    cebadores_producto = []
    resto_f = len(res_pcr.directo) - c5i.arriba
    if resto_f > 0:
        ini = c5v.arriba
        rasgos.append(Rasgo("primer_bind", ini, ini + resto_f, 1, "cebador directo",
                            {"note": "porción retenida tras la digestión"}))
        cebadores_producto.append(("cebador directo", res_pcr.directo,
                                   ini, ini + resto_f, 1))
    resto_r = c3i.arriba - (len(amp.seq) - len(res_pcr.reverso))
    if resto_r > 0:
        fin = c5v.arriba + len(inserto)
        rasgos.append(Rasgo("primer_bind", fin - resto_r, fin, -1, "cebador reverso",
                            {"note": "porción retenida tras la digestión"}))
        cebadores_producto.append(("cebador reverso", res_pcr.reverso,
                                   fin - resto_r, fin, -1))

    # Kozak y ORF del inserto.
    rasgos += _anota_orf(seq, c5v.arriba, c5v.arriba + len(inserto), avisos)

    producto = Registro(nombre or f"{aceptor.nombre}_con_inserto", seq, True,
                        sorted(rasgos, key=lambda r: (r.inicio, -len(r))),
                        "ligación in silico")
    producto.cebadores_snapgene = cebadores_producto      # type: ignore[attr-defined]

    return ResultadoClonaje(producto, amp, aceptor, inserto, enz5, enz3,
                            u5, u3, avisos, res_pcr, "restriccion",
                            f"diana de {enz5.nombre} regenerada",
                            f"diana de {enz3.nombre} regenerada")


def _solape(a: str, b: str, maximo: int = 80) -> int:
    """Longitud del solape exacto entre el final de `a` y el principio de `b`."""
    for n in range(min(maximo, len(a), len(b)), 0, -1):
        if a[-n:] == b[:n]:
            return n
    return 0


def ensambla_solapes(aceptor: Registro, res_pcr: ResultadoPCR, enz,
                     nombre: str = "", min_solape: int = 15,
                     etiqueta_orf: str = "ORF del inserto") -> ResultadoClonaje:
    """Ensamblado por homología (In-Fusion de Takara, Gibson, HiFi…).

    El vector se linealiza con **una** enzima y el inserto entra por los brazos de
    homología que llevan las colas 5' de los cebadores. No se digiere el inserto y
    la unión no deja cicatriz: el producto es vector + inserto exactamente, con el
    solape contado una sola vez. La diana de linealización suele quedar destruida,
    y eso es justo el cribado.
    """
    if not aceptor.circular:
        raise ErrorClonaje("el aceptor tiene que ser circular")

    avisos: list[str] = []
    amp = res_pcr.amplicon
    c = corte_unico(aceptor, enz, "el vector").arriba      # corte en hebra superior

    izq, der = aceptor.seq[:c], aceptor.seq[c:]
    ov5 = _solape(izq, amp.seq)
    ov3 = _solape(amp.seq, der)

    for lado, cual, ov in (("5'", "directo", ov5), ("3'", "reverso", ov3)):
        if ov < SUELO_SOLAPE:
            raise ErrorClonaje(
                f"la cola del cebador {cual} no solapa con el extremo {lado} del "
                f"vector linealizado con {enz.nombre} "
                f"(solape de sólo {ov} nt, por debajo del suelo de {SUELO_SOLAPE}). "
                "Sin brazo de homología no hay ensamblado: comprueba "
                "que la enzima de linealización es la correcta y que la cola está "
                "escrita en la orientación debida.")
        if ov < min_solape:
            avisos.append(
                f"el brazo de homología {lado} mide {ov} nt, menos de los "
                f"{min_solape} nt que pide el protocolo: la eficiencia cae")

    medio = amp.seq[ov5:len(amp.seq) - ov3]
    if len(medio) <= 0:
        raise ErrorClonaje("los dos brazos de homología se solapan entre sí: "
                           "no queda inserto en medio")

    # Un brazo que aparezca más de una vez en el vector puede ensamblar en el
    # sitio equivocado.
    for lado, brazo in (("5'", izq[-ov5:]), ("3'", der[:ov3])):
        n = len(busca(aceptor.seq, brazo, True))
        if n > 1:
            avisos.append(f"el brazo de homología {lado} ({brazo}) aparece {n} veces "
                          "en el vector: el ensamblado podría ir al sitio equivocado")

    # Si los dos extremos del amplicón se solapan entre sí, el inserto se
    # circulariza solo y compite con el ensamblado.
    auto = _solape(amp.seq, amp.seq[:len(amp.seq) // 2] or amp.seq)
    if auto >= min_solape:
        avisos.append(f"los dos extremos del amplicón comparten {auto} nt: el "
                      "inserto puede circularizarse solo")

    seq = izq + medio + der
    d = len(medio)

    # --- Rasgos: el vector conserva su numeración hasta el corte ---
    rasgos: list[Rasgo] = []
    for r in aceptor.rasgos:
        if r.fin <= c:
            rasgos.append(_desplaza(r, 0))
        elif r.inicio >= c:
            rasgos.append(_desplaza(r, d))
        else:
            # Rasgo partido por el punto de inserción: se parte en dos trozos, que
            # es más informativo que descartarlo (le pasa al MCS, por ejemplo).
            etq = r.etiqueta or r.clave
            rasgos.append(Rasgo(r.clave, r.inicio, c, r.hebra, f"{etq} (5')",
                                {**r.cualificadores,
                                 "note": "partido por el punto de inserción"}))
            rasgos.append(Rasgo(r.clave, c + d, r.fin + d, r.hebra, f"{etq} (3')",
                                {**r.cualificadores,
                                 "note": "partido por el punto de inserción"}))
            avisos.append(f"rasgo «{etq}» partido por el punto de inserción: "
                          "se anota en dos trozos")

    for r in amp.rasgos:
        if r.clave == "primer_bind":
            continue
        i, f = r.inicio - ov5 + c, r.fin - ov5 + c
        if r.inicio >= ov5 and r.fin <= len(amp.seq) - ov3:
            rasgos.append(Rasgo(r.clave, i, f, r.hebra, r.etiqueta,
                                dict(r.cualificadores), r.compuesto))

    rasgos.append(Rasgo("misc_feature", c - ov5, c, 1, f"brazo de homología 5' ({ov5} nt)",
                        {"note": "secuencia del vector aportada por la cola del "
                                 "cebador directo; la unión no deja cicatriz"}))
    rasgos.append(Rasgo("misc_feature", c + d, c + d + ov3, 1,
                        f"brazo de homología 3' ({ov3} nt)",
                        {"note": "secuencia del vector aportada por la cola del "
                                 "cebador reverso; la unión no deja cicatriz"}))
    rasgos.append(Rasgo("misc_feature", c, c + d, 1, "inserto",
                        {"note": f"{d} pb nuevos respecto al vector"}))

    # Los cebadores se conservan enteros: no hay digestión del inserto.
    cebadores_producto = [
        ("cebador directo", res_pcr.directo, c - ov5, c - ov5 + len(res_pcr.directo), 1),
        ("cebador reverso", res_pcr.reverso,
         c + d + ov3 - len(res_pcr.reverso), c + d + ov3, -1),
    ]
    for nom, seq_ceb, i, f, hebra in cebadores_producto:
        rasgos.append(Rasgo("primer_bind", i, f, hebra, nom,
                            {"note": "se conserva entero (no se digiere el inserto)"}))

    rasgos += _anota_orf(seq, c - ov5, c + d + ov3, avisos, etiqueta_orf)

    # --- Comprobaciones duras ---
    if seq[c - ov5:c] != izq[-ov5:] or seq[c + d:c + d + ov3] != der[:ov3]:
        raise ErrorClonaje("las uniones no reconstruyen la secuencia del vector")
    if seq[:c] != izq or seq[c + d:] != der:
        raise ErrorClonaje("el producto no conserva el vector fuera del punto "
                           "de inserción")
    sitios = busca_ambas(seq, enz.diana, True)
    if sitios:
        avisos.append(f"{enz.nombre} sigue cortando el producto en "
                      f"{[p + 1 for p in sitios]}: el cribado por pérdida del sitio "
                      "no sirve en este clon")

    producto = Registro(nombre or f"{aceptor.nombre}_con_inserto", seq, True,
                        sorted(rasgos, key=lambda r: (r.inicio, -len(r))),
                        "ensamblado por solapes in silico")
    producto.cebadores_snapgene = cebadores_producto      # type: ignore[attr-defined]

    return ResultadoClonaje(producto, amp, aceptor, medio, enz, enz,
                            c - ov5, c + d, avisos, res_pcr, "solapes",
                            f"brazo de homología 5' ({ov5} nt)",
                            f"brazo de homología 3' ({ov3} nt)")


def _anota_orf(seq: str, ini: int, fin: int, avisos: list[str],
               etiqueta: str = "ORF del inserto") -> list[Rasgo]:
    """Anota el primer ORF completo del inserto, y el Kozak si está."""
    rasgos: list[Rasgo] = []
    region = seq[ini:fin]
    p = region.find("ATG")
    if p < 0:
        avisos.append("no hay ATG en el inserto: no se anota ORF")
        return rasgos
    inicio_orf = ini + p
    prot = traduce(seq[inicio_orf:fin])
    stop = prot.find("*")
    if stop < 0:
        avisos.append("el ORF del inserto no acaba en codón stop dentro del inserto: "
                      "comprueba el cebador reverso")
        fin_orf = inicio_orf + 3 * len(prot)
    else:
        fin_orf = inicio_orf + 3 * (stop + 1)
    rasgos.append(Rasgo("CDS", inicio_orf, fin_orf, 1, etiqueta,
                        {"note": f"{(fin_orf - inicio_orf) // 3 - 1} aminoácidos + stop",
                         "translation": prot[:stop] if stop >= 0 else prot}))
    if stop >= 0:
        n_stops = 0
        while prot[stop + n_stops:stop + n_stops + 1] == "*":
            n_stops += 1
        rasgos.append(Rasgo("misc_feature", fin_orf - 3, fin_orf + 3 * (n_stops - 1), 1,
                            "stop", {"note": f"{n_stops} codón(es) de parada"}))

    # Contexto Kozak: lo que manda es la purina en -3 y la G en +4.
    ctx = seq[max(0, inicio_orf - 6):inicio_orf]
    m3 = seq[inicio_orf - 3] if inicio_orf >= 3 else "?"
    p4 = seq[inicio_orf + 3] if inicio_orf + 3 < len(seq) else "?"
    calidad = ("óptimo" if m3 in "AG" and p4 == "G" else
               "aceptable (purina en -3, +4 no es G)" if m3 in "AG" else
               "DÉBIL: no hay purina en -3")
    rasgos.append(Rasgo("regulatory", max(0, inicio_orf - 6), inicio_orf, 1,
                        "contexto Kozak",
                        {"note": f"{ctx}ATG{p4} · -3={m3} +4={p4} · {calidad}"}))
    if m3 not in "AG":
        avisos.append(f"contexto Kozak débil: en -3 hay {m3}, no una purina")
    return rasgos


# ---------------------------------------------------------------------------
# Cebadores automáticos (caso genérico)
# ---------------------------------------------------------------------------

def localiza_cds(registro: Registro) -> tuple[int, int]:
    """CDS anotado si lo hay; si no, el ORF más largo. Devuelve (inicio0, fin)."""
    cds = [r for r in registro.rasgos if r.clave.upper() == "CDS" and not r.compuesto]
    if cds:
        mejor = max(cds, key=len)
        return mejor.inicio, mejor.fin
    mejor = (0, 0)
    for marco in range(3):
        i = marco
        while i < len(registro.seq) - 2:
            if registro.seq[i:i + 3] == "ATG":
                j = i
                while j < len(registro.seq) - 2:
                    if registro.seq[j:j + 3] in ("TAA", "TAG", "TGA"):
                        if j + 3 - i > mejor[1] - mejor[0]:
                            mejor = (i, j + 3)
                        break
                    j += 3
                i = j + 3
            else:
                i += 3
    if mejor[1] == 0:
        raise ErrorClonaje("no se ha encontrado ningún ORF en el donante")
    return mejor


def cebadores_automaticos(donante: Registro, enz5, enz3, proteccion: str = "CACCAC",
                          kozak: str = "GCCACC", stops: str = "TAATGA",
                          tm_objetivo: float = 62.0,
                          inicio_cds: int | None = None,
                          fin_cds: int | None = None) -> tuple[str, str, int, int]:
    """Construye los dos cebadores con la misma arquitectura que el diseño.

    directo: protección + diana5 + Kozak + ATG + apareamiento
    reverso: protección + diana3 + rc(stops) + rc(final del CDS sin su stop)
    """
    i, f = localiza_cds(donante)
    if inicio_cds is not None:
        i = inicio_cds
    if fin_cds is not None:
        f = fin_cds
    cds = donante.seq[i:f]
    if not cds.startswith("ATG"):
        raise ErrorClonaje(f"el CDS no empieza por ATG ({cds[:3]})")
    if cds[-3:] in ("TAA", "TAG", "TGA"):
        cds_sin_stop = cds[:-3]
    else:
        cds_sin_stop = cds

    def ajusta(trozo_fn) -> str:
        mejor, mejor_dist = None, 1e9
        for L in range(18, 31):
            s = trozo_fn(L)
            t = tm_nn(s)
            pinza = s[-1] in "GC"
            dist = abs(t - tm_objetivo) + (0 if pinza else 1.5)
            if dist < mejor_dist:
                mejor, mejor_dist = s, dist
        return mejor or trozo_fn(20)

    ap_f = ajusta(lambda L: cds_sin_stop[3:3 + L])
    ap_r = ajusta(lambda L: rc(cds_sin_stop[-L:]))

    directo = proteccion + enz5.diana + kozak + "ATG" + ap_f
    reverso = proteccion + enz3.diana + rc(stops) + ap_r
    return directo, reverso, i, f


# ---------------------------------------------------------------------------
# Informe
# ---------------------------------------------------------------------------

def _ventana(seq: str, centro: int, n: int = 24) -> str:
    L = len(seq)
    return "".join(seq[(centro + k) % L] for k in range(-n, n))


def informe(res: ResultadoClonaje) -> str:
    p = res.producto
    rp = res.pcr
    lin: list[str] = []
    a = lin.append

    a(f"# Clonaje in silico — {p.nombre}")
    a("")
    a("Generado por `herramientas/simula_clonaje.py`. **No sustituye a la "
      "secuenciación del clon**: lo que predice es lo que *debería* salir.")
    a("")
    a("## 1. Piezas")
    a("")
    a("| Pieza | Tamaño | Procedencia |")
    a("|---|---:|---|")
    a(f"| Molde de la PCR | {len(rp.amplicon.seq) if rp else 0} pb (amplicón) | "
      f"{rp.amplicon.procedencia if rp else '—'} |")
    a(f"| Vector aceptor | {len(res.aceptor.seq)} pb | {res.aceptor.procedencia} |")
    etq_ins = ("Inserto digerido" if res.mecanismo == "restriccion"
               else "Inserto neto (sin los brazos)")
    origen_ins = ("amplicón cortado" if res.mecanismo == "restriccion"
                  else "amplicón menos los dos solapes")
    a(f"| {etq_ins} | {len(res.inserto)} pb | {origen_ins} |")
    a(f"| **Producto** | **{len(p.seq)} pb** | circular |")
    a("")

    if rp:
        a("## 2. PCR")
        a("")
        a("| | Directo | Reverso |")
        a("|---|---|---|")
        a(f"| Secuencia 5'→3' | `{rp.directo}` | `{rp.reverso}` |")
        a(f"| Longitud | {len(rp.directo)} nt | {len(rp.reverso)} nt |")
        a(f"| Cola 5' (no aparea) | {len(rp.ap_directo.cola)} nt | "
          f"{len(rp.ap_reverso.cola)} nt |")
        a(f"| Apareamiento | {rp.ap_directo.largo} nt | {rp.ap_reverso.largo} nt |")
        a(f"| Tm apareamiento | {tm_nn(rp.directo[-rp.ap_directo.largo:]):.1f} °C | "
          f"{tm_nn(rp.reverso[-rp.ap_reverso.largo:]):.1f} °C |")
        a(f"| Tm cebador completo | {tm_nn(rp.directo):.1f} °C | "
          f"{tm_nn(rp.reverso):.1f} °C |")
        a(f"| GC | {gc(rp.directo):.0f} % | {gc(rp.reverso):.0f} % |")
        a("")
        if res.mecanismo == "restriccion":
            a(f"Amplicón: **{len(rp.amplicon.seq)} pb**, GC {gc(rp.amplicon.seq):.0f} %. "
              f"Tras digerir: **{len(res.inserto)} pb**.")
        else:
            a(f"Amplicón: **{len(rp.amplicon.seq)} pb**, GC {gc(rp.amplicon.seq):.0f} %. "
              f"Se usa entero; aporta **{len(res.inserto)} pb** nuevos al plásmido "
              "(el resto son los dos brazos, que ya están en el vector).")
        a("")

    a("## 3. Uniones del clon final")
    a("")
    a("Esto es lo que tiene que aparecer al secuenciar (24 nt a cada lado):")
    a("")
    pref = "unión 5'  …"
    sangria = " " * (len(pref) + 24)
    a("```")
    a(f"{pref}{_ventana(p.seq, res.union5)}…")
    a(f"{sangria}^ {res.etiqueta5 or res.enz5.nombre}")
    a(f"unión 3'  …{_ventana(p.seq, res.union3)}…")
    a(f"{sangria}^ {res.etiqueta3 or res.enz3.nombre}")
    a("```")
    if res.mecanismo == "solapes":
        a("")
        a("El ensamblado por homología **no deja cicatriz**: en las dos uniones la "
          "secuencia del vector continúa exactamente como en el parental, y el "
          "solape se cuenta una sola vez.")
    a("")

    orf = [r for r in p.rasgos if r.clave == "CDS"
           and "translation" in r.cualificadores]
    if orf:
        r = orf[0]
        prot = r.cualificadores.get("translation", "")
        a("## 4. El ORF que queda clonado")
        a("")
        a(f"- Posición en el plásmido: {r.inicio + 1}–{r.fin}")
        a(f"- Longitud: {(r.fin - r.inicio)} pb = {len(prot)} aminoácidos + stop")
        a(f"- Primeros 12 aa: `{prot[:12]}`")
        a(f"- Últimos 12 aa: `{prot[-12:]}`")
        a("")
        a("**Míralos.** Es la comprobación de 10 segundos que evita clonar algo que "
          "no es lo que crees.")
        a("")
        if "*" in prot:
            a("> ⚠️ Hay un codón stop interno en el ORF. Algo va mal.")
            a("")

    a("## 5. Digestiones diagnósticas del producto")
    a("")
    a("| Enzima | Cortes | Fragmentos (pb) |")
    a("|---|---:|---|")
    for e in PANEL_NEVERA:
        try:
            cs = cortes(p, e)
        except NotImplementedError:
            continue
        if not cs:
            continue
        fr = ", ".join(str(x) for x in reversed(fragmentos(p, e)))
        a(f"| {e.nombre} | {len(cs)} | {fr} |")
    if res.mecanismo == "restriccion":
        dob = fragmentos_multiple(p, [res.enz5, res.enz3])
        a(f"| **{res.enz5.nombre} + {res.enz3.nombre}** | 2 | "
          f"{', '.join(str(x) for x in reversed(dob))} |")
        a("")
        a(f"La doble digestión libera el inserto ({len(res.inserto)} pb) del "
          "esqueleto: es el cribado más directo, y en el vector vacío da una sola "
          f"banda del tamaño del plásmido ({len(res.aceptor.seq)} pb).")
    else:
        n = len(cortes(p, res.enz5))
        a("")
        if n == 0:
            a(f"**{res.enz5.nombre} ya no corta el producto** (0 sitios), mientras "
              f"que el vector vacío recircularizado se linealiza a "
              f"{len(res.aceptor.seq)} pb. Ése es el cribado directo: el clon "
              "correcto no corta.")
        else:
            a(f"⚠️ {res.enz5.nombre} todavía corta el producto {n} vez/veces, así "
              "que el cribado por pérdida del sitio **no vale** en este clon: usa "
              "otra pareja de la tabla.")
        ins = [x for x in p.rasgos if x.etiqueta == "inserto"]
        if ins:
            arriba, abajo = [], []
            for e in TODAS:
                try:
                    cs = cortes(p, e)
                except NotImplementedError:
                    continue
                if len(cs) != 1:
                    continue
                c = cs[0].arriba
                if c <= ins[0].inicio:
                    arriba.append((ins[0].inicio - c, e.nombre, e, c))
                elif c >= ins[0].fin:
                    abajo.append((c - ins[0].fin, e.nombre, e, c))
            if arriba and abajo:
                a("")
                a("Enzimas de corte único que flanquean el inserto (las más cercanas "
                  "primero; ✦ = en el congelador):")
                a("")
                a("| Lado | Enzima | Corta en | Distancia al inserto |")
                a("|---|---|---:|---:|")
                for lado, lista in (("5'", sorted(arriba)[:5]),
                                    ("3'", sorted(abajo)[:5])):
                    for dist, _, e, c in lista:
                        marca = " ✦" if e.nevera else ""
                        a(f"| {lado} | {e.nombre}{marca} | {c} | {dist} pb |")
        par = pareja_que_flanquea(p, ins[0].inicio, ins[0].fin) if ins else None
        if par:
            e1, e2, nevera = par
            fr = fragmentos_multiple(p, [e1, e2])
            liberado = min(fr)
            a("")
            a(f"Para confirmar el tamaño del inserto, la pareja única más ajustada "
              f"que lo flanquea es **{e1.nombre} + {e2.nombre}**: "
              f"{', '.join(str(x) for x in reversed(fr))} pb, o sea el inserto más "
              f"{liberado - len(res.inserto)} pb de vector."
              + ("" if nevera else " Ojo: alguna de las dos no está en el panel del "
                 "congelador."))
    a("")

    if res.pcr:
        ceb_vector = [x for x in p.rasgos if x.clave == "primer_bind"
                      and x.hebra == 1 and not x.etiqueta.startswith("cebador ")]
        rev = [x for x in p.rasgos if x.clave == "primer_bind" and x.hebra == -1]
        if ceb_vector and rev:
            a("## 5b. PCR de colonia")
            a("")
            a("Con un cebador directo que ya está anotado en el vector y el reverso "
              "del clonaje, el tamaño esperado en el clon correcto es:")
            a("")
            a("| Directo (del vector) | Posición | Con el reverso del clonaje |")
            a("|---|---:|---:|")
            for c in ceb_vector:
                tam = rev[0].fin - c.inicio
                a(f"| {c.etiqueta} | {c.inicio + 1} | **{tam} pb** |")
            a("")
            a("En el vector vacío ese producto no sale (el cebador reverso no tiene "
              "dónde aparear), así que la ausencia de banda es informativa.")
            a("")

    a("## 6. Rasgos del producto")
    a("")
    a("| Inicio | Fin | Hebra | Tipo | Etiqueta |")
    a("|---:|---:|:---:|---|---|")
    for r in p.rasgos:
        a(f"| {r.inicio + 1} | {r.fin} | {'+' if r.hebra >= 0 else '−'} | "
          f"{r.clave} | {r.etiqueta} |")
    a("")

    avisos = (rp.avisos if rp else []) + res.avisos
    a("## 7. Avisos")
    a("")
    if avisos:
        for x in avisos:
            a(f"- {x}")
    else:
        a("Ninguno.")
    a("")
    return "\n".join(lin)


# ---------------------------------------------------------------------------
# Demo: vector y donante sintéticos
# ---------------------------------------------------------------------------

MCS_DEMO = "TCTAGAGCTAGCGAATTCGAATTTAAATCGGATCCGCGGCCGCGTCGA"


def _relleno(n: int, semilla: int = 7) -> str:
    """Relleno reproducible sin dianas de las enzimas del panel."""
    import random
    r = random.Random(semilla)
    malas = [e.diana for e in PANEL_NEVERA]
    s = ""
    while len(s) < n:
        s += r.choice("ACGT")
        if any(d in s[-10:] for d in malas):
            s = s[:-1]
    return s


def vector_demo() -> Registro:
    attb = "GTGCCAGGGCGTGCCCTTGGGCTCCCCGGGCGCG"
    attp = "GTAGTGCCCCAACTGGGGTAACCTTTGAGTTCTCTCAGTTGGGGG"
    ef1a = "GGGCAGGGGCGGGGTTCGGCTTCTGGCGTGTGACCGGCGG" + _relleno(180, 1)
    polya = "AACTTGTTTATTGCAGCTTATAATGGTTACAAATAAAGCAATAGCATCACAAATTTCACAAATAAAGCA"
    ori = _relleno(600, 2)
    kanr = _relleno(800, 3)

    partes = [("attB", attb), ("relleno1", _relleno(40, 4)),
              ("promoter_EF1a", ef1a), ("MCS", MCS_DEMO),
              ("polyA_SV40", polya), ("relleno2", _relleno(60, 5)),
              ("attP", attp), ("rep_origin", ori), ("KanR", kanr)]

    seq, rasgos, pos = "", [], 0
    claves = {"attB": "misc_recomb", "attP": "misc_recomb",
              "promoter_EF1a": "promoter", "MCS": "misc_feature",
              "polyA_SV40": "polyA_signal", "rep_origin": "rep_origin",
              "KanR": "CDS"}
    for nombre, s in partes:
        seq += s
        if nombre in claves:
            rasgos.append(Rasgo(claves[nombre], pos, pos + len(s), 1, nombre))
        pos += len(s)
    return Registro("pMC.EF1a-MCS-SV40polyA_DEMO", seq, True, rasgos,
                    "vector sintético de demostración (NO es el vector real)")


def donante_demo() -> Registro:
    cds = "ATG" + _relleno(297, 11) + "TAA"
    # Nos aseguramos de que no haya stops en fase antes del final.
    bases = list(cds)
    for k in range(3, len(cds) - 3, 3):
        if "".join(bases[k:k + 3]) in ("TAA", "TAG", "TGA"):
            bases[k + 2] = "C"
    cds = "".join(bases)
    seq = _relleno(120, 12) + cds + _relleno(150, 13)
    rasgos = [Rasgo("CDS", 120, 120 + len(cds), 1, "GEN_DEMO")]
    return Registro("pDonante-GEN_DEMO_DEMO", seq, True, rasgos,
                    "donante sintético de demostración")


# ---------------------------------------------------------------------------
# Autotest
# ---------------------------------------------------------------------------

def autotest() -> int:
    fallos: list[str] = []
    hechas = 0

    def ok(cond, msg):
        nonlocal hechas
        hechas += 1
        if not cond:
            fallos.append(msg)

    # --- PCR ---
    molde = Registro("m", "AAAA" + _relleno(80, 21) + "TTTT", False, [], "test")
    d = "CACCACGCTAGC" + molde.seq[4:24]
    r = "CACCACGGATCC" + rc(molde.seq[60:80])
    res = pcr(molde, d, r)
    ok(res.amplicon.seq == "CACCACGCTAGC" + molde.seq[4:80] + rc("CACCACGGATCC"),
       "amplicón mal construido")
    ok(res.ap_directo.cola == "CACCACGCTAGC", "cola directa mal")
    ok(res.ap_reverso.largo == 20, "apareamiento reverso mal")

    # Cebadores invertidos -> error
    try:
        pcr(molde, r, d)
        ok(False, "no detecta cebadores intercambiados en molde lineal")
    except ErrorClonaje:
        pass

    # Molde circular: amplicón que cruza el origen.
    circ = Registro("c", "ATGCGTACGTTAGCGGATCAAGGCTTACGATCGCTTAAGGCTAA", True, [], "t")
    res2 = pcr(circ, circ.seq[30:44], rc(circ.seq[5:19]))
    ok(len(res2.amplicon.seq) == (19 - 30) % len(circ.seq), "amplicón circular mal")

    # --- Cortes ---
    bam = POR_NOMBRE["BamHI-HF"]
    c = cortes(Registro("x", "AAAGGATCCAAA", False, [], ""), bam)
    ok(len(c) == 1 and c[0].diana == 3 and c[0].arriba == 4 and c[0].abajo == 8,
       "coordenadas de corte de BamHI mal")
    kpn = POR_NOMBRE["KpnI"]
    ck = cortes(Registro("x", "AAAGGTACCAAA", False, [], ""), kpn)
    ok(ck[0].arriba == 8 and ck[0].abajo == 4, "saliente 3' de KpnI mal")
    pme = POR_NOMBRE["PmeI"]
    cp = cortes(Registro("x", "AAGTTTAAACAA", False, [], ""), pme)
    ok(cp[0].arriba == cp[0].abajo == 6, "corte romo de PmeI mal")
    for e in PANEL_NEVERA:
        if e.diana == rc(e.diana):
            cc = cortes(Registro("x", "AA" + e.diana + "AA", False, [], ""), e)
            ok(cc and cc[0].abajo - cc[0].arriba == e.saliente,
               f"saliente de {e.nombre} incoherente con la tabla")

    # Diana duplicada -> error
    try:
        corte_unico(Registro("x", "GGATCCAAAGGATCC", True, [], ""), bam, "prueba")
        ok(False, "no detecta diana duplicada")
    except ErrorClonaje:
        pass

    # --- Clonaje completo sobre la demo ---
    vec, don = vector_demo(), donante_demo()
    nhe, bam = POR_NOMBRE["NheI-HF"], POR_NOMBRE["BamHI-HF"]
    cd, cr, i0, f0 = cebadores_automaticos(don, nhe, bam)
    ok(cd.startswith("CACCACGCTAGCGCCACCATG"), "cebador directo automático mal")
    ok(cr.startswith("CACCACGGATCCTCATTA"), "cebador reverso automático mal")
    ok(localiza_cds(don) == (i0, f0), "localiza_cds incoherente")

    rpcr = pcr(don, cd, cr)
    cl = liga(vec, rpcr, nhe, bam, "demo")
    p = cl.producto

    ok(p.circular, "el producto no es circular")
    # Tamaño: vector - MCS entre dianas + inserto
    c5v, c3v = corte_unico(vec, nhe, "v"), corte_unico(vec, bam, "v")
    ok(len(p.seq) == len(vec.seq) - (c3v.arriba - c5v.arriba) + len(cl.inserto),
       "tamaño del producto incoherente")
    ok(len(cortes(p, nhe)) == 1, "NheI deja de ser única en el producto")
    ok(len(cortes(p, bam)) == 1, "BamHI deja de ser única en el producto")
    ok(p.seq[cl.union5:cl.union5 + 6] == "GCTAGC", "unión 5' sin diana NheI")
    ok(p.seq[cl.union3:cl.union3 + 6] == "GGATCC", "unión 3' sin diana BamHI")
    ok("TCTAGAGCTAGCGCCACCATG" in p.seq, "la unión 5' no es la del diseño")
    ok("TAATGAGGATCCGCGGCCGCGTCGA" in p.seq, "la unión 3' no es la del diseño")

    orf = [x for x in p.rasgos if x.clave == "CDS" and x.etiqueta == "ORF del inserto"]
    ok(len(orf) == 1, "no se ha anotado el ORF del inserto")
    if orf:
        prot = orf[0].cualificadores["translation"]
        ok("*" not in prot, "hay un stop interno en el ORF clonado")
        ok(traduce(p.seq[orf[0].inicio:orf[0].fin])[-1] == "*",
           "el ORF no acaba en stop")
        # El ORF clonado tiene que ser el del donante sin su stop nativo.
        esperado = traduce(don.seq[i0:f0 - 3])
        ok(prot == esperado, "el ORF clonado no coincide con el CDS del donante")
    koz = [x for x in p.rasgos if x.etiqueta == "contexto Kozak"]
    ok(len(koz) == 1, "contexto Kozak no anotado")
    ok(koz and "GCCACCATGT" in koz[0].cualificadores["note"],
       "el contexto Kozak anotado no es el que se construyó")
    ok(any(x.etiqueta == "stop" for x in p.rasgos), "codones de parada no anotados")

    # Rasgos del vector conservados y bien colocados
    for nombre in ("attB", "attP", "promoter_EF1a", "polyA_SV40"):
        r2 = [x for x in p.rasgos if x.etiqueta == nombre]
        ok(len(r2) == 1, f"rasgo {nombre} perdido en el producto")
        if r2:
            r1 = [x for x in vec.rasgos if x.etiqueta == nombre][0]
            ok(p.seq[r2[0].inicio:r2[0].fin] == vec.seq[r1.inicio:r1.fin],
               f"rasgo {nombre} desplazado a coordenadas equivocadas")
    ok(not any(x.etiqueta == "MCS" for x in p.rasgos),
       "el MCS sustituido sigue anotado")

    # El casete tiene que caer entre attB y attP (restricción del minicírculo)
    attb = [x for x in p.rasgos if x.etiqueta == "attB"][0]
    attp = [x for x in p.rasgos if x.etiqueta == "attP"][0]
    ins = [x for x in p.rasgos if x.etiqueta == "inserto"][0]
    ok(attb.fin <= ins.inicio and ins.fin <= attp.inicio,
       "el inserto no cae entre attB y attP")

    # --- Vector cuyo MCS cruza el origen numérico (dianas en orden inverso) ---
    c5 = corte_unico(vec, nhe, "v")
    vec_rot, _ = rota(vec, (c5.arriba + 10) % len(vec.seq))
    ok(corte_unico(vec_rot, bam, "v").arriba < corte_unico(vec_rot, nhe, "v").arriba,
       "el vector de prueba no tiene las dianas en orden inverso")
    cl_rot = liga(vec_rot, pcr(don, cd, cr), nhe, bam, "demo_rotado")
    ok(len(cl_rot.producto.seq) == len(p.seq),
       "el producto cambia de tamaño si el MCS cruza el origen")
    # Tras renumerar, la unión puede caer a caballo del origen: hay que buscar
    # en el círculo, no en la cadena lineal.
    circular_rot = cl_rot.producto.seq * 2
    ok("TCTAGAGCTAGCGCCACCATG" in circular_rot,
       "unión 5' mal con el MCS cruzando el origen")
    ok("TAATGAGGATCCGCGGCCGCGTCGA" in circular_rot,
       "unión 3' mal con el MCS cruzando el origen")
    ok(len(busca_ambas(cl_rot.producto.seq, nhe.diana, True)) == 1,
       "NheI no es única tras renumerar")
    ok(any("renumerado" in x for x in cl_rot.avisos), "no avisa de la renumeración")

    # Misma enzima en los dos extremos -> no direccional
    try:
        liga(vec, pcr(don, "CACCACGCTAGCGCCACCATG" + don.seq[i0 + 3:i0 + 23],
                      "CACCACGCTAGCTCATTA" + rc(don.seq[f0 - 23:f0 - 3])),
             nhe, nhe, "x")
        ok(False, "no detecta que la misma enzima a los dos lados no es direccional")
    except ErrorClonaje:
        pass

    # --- Ensamblado por solapes (In-Fusion / Gibson) ---
    cbam = corte_unico(vec, bam, "v")          # G^GATCC en el MCS de la demo
    brazo5 = vec.seq[cbam.arriba - 16:cbam.arriba]
    brazo3 = vec.seq[cbam.arriba:cbam.arriba + 15]
    cds_i, cds_f = localiza_cds(don)
    ap_f = don.seq[cds_i:cds_i + 25]
    ap_r = rc(don.seq[cds_f - 25:cds_f])
    F = brazo5 + ap_f
    R = rc(brazo3) + ap_r
    rs = pcr(don, F, R)
    es = ensambla_solapes(vec, rs, bam, "demo_infusion", 15, "GEN_DEMO")
    q = es.producto

    ok(es.mecanismo == "solapes", "mecanismo mal etiquetado")
    neto = len(rs.amplicon.seq) - 16 - 15
    ok(len(q.seq) == len(vec.seq) + neto,
       "tamaño del producto de ensamblado incoherente")
    ok(len(es.inserto) == neto, "inserto neto mal calculado")
    # Sin cicatriz: el vector se conserva entero y contiguo a los dos lados.
    ok(q.seq[:cbam.arriba] == vec.seq[:cbam.arriba],
       "el ensamblado altera el vector antes del punto de inserción")
    ok(q.seq[cbam.arriba + neto:] == vec.seq[cbam.arriba:],
       "el ensamblado altera el vector después del punto de inserción")
    ok(q.seq[cbam.arriba - 16:cbam.arriba] == brazo5, "brazo 5' mal reconstruido")
    ok(q.seq[cbam.arriba + neto:cbam.arriba + neto + 15] == brazo3,
       "brazo 3' mal reconstruido")
    # BamHI queda destruido: es el cribado del protocolo.
    ok(len(busca_ambas(q.seq, bam.diana, True)) == 0,
       "la diana de linealización no queda destruida")
    ok(len(busca_ambas(vec.seq, bam.diana, True)) == 1,
       "el vector de prueba no tenía BamHI única")
    # El inserto se anota con el nombre que se le pasa.
    ok(any(x.clave == "CDS" and x.etiqueta == "GEN_DEMO" for x in q.rasgos),
       "el ORF no se anota con la etiqueta pedida")
    # El MCS, partido por la inserción, se anota en dos trozos.
    ok(len([x for x in q.rasgos if x.etiqueta.startswith("MCS (")]) == 2,
       "el rasgo partido no se anota en dos trozos")
    # Rasgos del vector anteriores al corte conservan su numeración original.
    for nom in ("attB", "promoter_EF1a"):
        r1 = [x for x in vec.rasgos if x.etiqueta == nom][0]
        r2 = [x for x in q.rasgos if x.etiqueta == nom][0]
        ok((r1.inicio, r1.fin) == (r2.inicio, r2.fin),
           f"el ensamblado renumera «{nom}», que está antes del punto de inserción")
    # Los cebadores se conservan enteros.
    cf = [x for x in q.rasgos if x.etiqueta == "cebador directo"][0]
    ok(q.seq[cf.inicio:cf.fin] == F, "el cebador directo no se conserva entero")
    cr2 = [x for x in q.rasgos if x.etiqueta == "cebador reverso"][0]
    ok(rc(q.seq[cr2.inicio:cr2.fin]) == R, "el cebador reverso no se conserva entero")

    # Sin brazos de homología no hay ensamblado: tiene que fallar explícitamente.
    try:
        ensambla_solapes(vec, pcr(don, "GGGGGG" + ap_f, "CCCCCC" + ap_r), bam, "x")
        ok(False, "no detecta que faltan los brazos de homología")
    except ErrorClonaje:
        pass

    # Brazo corto: avisa pero ensambla.
    corto = ensambla_solapes(vec, pcr(don, vec.seq[cbam.arriba - 8:cbam.arriba] + ap_f,
                                     rc(brazo3) + ap_r), bam, "x", 15)
    ok(any("8 nt" in x for x in corto.avisos), "no avisa de un brazo demasiado corto")

    # Pareja diagnóstica: tiene que flanquear el inserto de verdad.
    ins = [x for x in q.rasgos if x.etiqueta == "inserto"][0]
    par = pareja_que_flanquea(q, ins.inicio, ins.fin)
    ok(par is not None, "no encuentra pareja diagnóstica")
    if par:
        e1, e2, _ = par
        ok(cortes(q, e1)[0].arriba <= ins.inicio and
           cortes(q, e2)[0].arriba >= ins.fin,
           "la pareja diagnóstica no flanquea el inserto")

    # --- Ida y vuelta por .dna y por GenBank ---
    import tempfile
    from snapgene import lee_dna
    with tempfile.TemporaryDirectory() as tmp:
        ruta = escribe_dna(p, os.path.join(tmp, "p.dna"), "demo",
                           getattr(p, "cebadores_snapgene", ()))
        q = lee_dna(ruta)
        ok(q.seq == p.seq, ".dna: la secuencia no sobrevive la ida y vuelta")
        ok(q.circular, ".dna: se pierde la topología circular")
        # Los cebadores viajan en su propio paquete; al releer vuelven como
        # rasgos primer_bind, una sola vez cada uno.
        esperados = [x for x in p.rasgos if x.clave != "primer_bind"]
        cebs_leidos = [x for x in q.rasgos if x.clave == "primer_bind"]
        ok(len(q.rasgos) - len(cebs_leidos) == len(esperados),
           ".dna: se pierden rasgos")
        ok(len(cebs_leidos) == 2, ".dna: los cebadores no vuelven (o se duplican)")
        for c in cebs_leidos:
            trozo = p.seq[c.inicio:c.fin]
            cebador = cd if c.hebra == 1 else cr
            if c.hebra == -1:
                trozo = rc(trozo)
            ok(len(trozo) > 0 and cebador.endswith(trozo),
               f".dna: el sitio de «{c.etiqueta}» no cae donde está el cebador")
        for r1, r2 in zip(esperados, [x for x in q.rasgos
                                      if x.clave != "primer_bind"]):
            ok(r1.inicio == r2.inicio and r1.fin == r2.fin,
               f".dna: coordenadas de «{r1.etiqueta}» cambian al releer")
            ok(r1.hebra == r2.hebra, f".dna: hebra de «{r1.etiqueta}» cambia")
        with open(ruta, "rb") as fh:
            ok(fh.read(1) == b"\x09", ".dna: el primer paquete no es la cabecera")

        gb = escribe_genbank(p, os.path.join(tmp, "p.gb"), "demo")
        g = lee(gb)
        ok(g.seq == p.seq, "GenBank: la secuencia no sobrevive la ida y vuelta")
        ok(g.circular, "GenBank: se pierde el circular")
        ok(len(g.rasgos) == len(p.rasgos), "GenBank: se pierden rasgos")
        for r1, r2 in zip(p.rasgos, g.rasgos):
            ok((r1.inicio, r1.fin, r1.hebra) == (r2.inicio, r2.fin, r2.hebra),
               f"GenBank: coordenadas de «{r1.etiqueta}» cambian al releer")

    # --- rota() ---
    rr, _ = rota(vec, 100)
    ok(rr.seq == vec.seq[100:] + vec.seq[:100], "rota() mal")
    ok(len(rr.seq) == len(vec.seq), "rota() cambia la longitud")

    # --- Informe ---
    txt = informe(cl)
    ok("Clonaje in silico" in txt and "unión 5'" in txt, "informe incompleto")
    txt2 = informe(es)
    ok("no deja cicatriz" in txt2, "el informe no explica el ensamblado sin cicatriz")
    ok("ya no corta el producto" in txt2, "el informe no da el cribado por BamHI")
    # El vector de demostración no trae cebadores anotados, así que la sección de
    # PCR de colonia no debe aparecer (sólo sale si el vector los lleva).
    ok("PCR de colonia" not in txt2,
       "inventa una PCR de colonia sin cebadores anotados en el vector")
    ok("flanquean el inserto" in txt2, "el informe no lista las enzimas que flanquean")

    print(f"autotest: {hechas} comprobaciones, "
          f"{'todas OK' if not fallos else f'{len(fallos)} FALLOS'}")
    for f in fallos:
        print(f"  - {f}")
    return 0 if not fallos else 1


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Simula PCR + clonaje y escribe el .dna del plásmido resultante",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--aceptor", help="plásmido donde se inserta (.gb/.dna/.fa)")
    ap.add_argument("--donante", help="molde de la PCR (.gb/.dna/.fa)")
    ap.add_argument("--directo", help="cebador directo 5'->3'")
    ap.add_argument("--reverso", help="cebador reverso 5'->3'")
    ap.add_argument("--enzimas", default="NheI-HF,BamHI-HF",
                    help="clonaje por restricción: pareja 5',3' "
                         "(por defecto: NheI-HF,BamHI-HF)")
    ap.add_argument("--infusion", metavar="ENZIMA",
                    help="ensamblado por homología (In-Fusion, Gibson, HiFi): "
                         "nombre de la enzima que linealiza el vector, p. ej. BamHI-HF. "
                         "Los brazos los aportan las colas 5' de los cebadores")
    ap.add_argument("--min-solape", type=int, default=15,
                    help="longitud mínima aceptable del brazo de homología (15)")
    ap.add_argument("--auto", action="store_true",
                    help="calcular los cebadores a partir del CDS del donante")
    ap.add_argument("--inicio-cds", type=int, help="forzar el ATG (posición 1-based)")
    ap.add_argument("--fin-cds", type=int, help="forzar el final del CDS (1-based)")
    ap.add_argument("--proteccion", default="CACCAC")
    ap.add_argument("--kozak", default="GCCACC")
    ap.add_argument("--nombre", default="", help="nombre del plásmido resultante")
    ap.add_argument("--nombre-orf", default="ORF del inserto",
                    help="etiqueta del ORF en el mapa, p. ej. KRT10")
    ap.add_argument("--salida", default="../resultados", help="carpeta de salida")
    ap.add_argument("--demo", action="store_true",
                    help="ejecutar con un vector y un donante sintéticos")
    ap.add_argument("--autotest", action="store_true")
    args = ap.parse_args(argv)

    if args.autotest:
        return autotest()

    if args.infusion:
        nombres = [args.infusion.strip()]
    else:
        nombres = [x.strip() for x in args.enzimas.split(",")]
        if len(nombres) != 2:
            print("--enzimas espera dos nombres separados por coma", file=sys.stderr)
            return 2
    for n in nombres:
        if n not in POR_NOMBRE:
            print(f"enzima desconocida: {n}\nDisponibles: "
                  f"{', '.join(sorted(POR_NOMBRE))}", file=sys.stderr)
            return 2
    enz5 = POR_NOMBRE[nombres[0]]
    enz3 = POR_NOMBRE[nombres[-1]]

    if args.demo:
        aceptor, donante = vector_demo(), donante_demo()
        nombre = args.nombre or "pMC.EF1a-GEN_DEMO-SV40polyA"
    else:
        if not args.aceptor or not args.donante:
            print("hacen falta --aceptor y --donante (o --demo). "
                  "Ver secuencias/LEEME.md", file=sys.stderr)
            return 2
        aceptor, donante = lee(args.aceptor), lee(args.donante)
        nombre = args.nombre or f"{aceptor.nombre}-inserto"

    try:
        if args.directo and args.reverso:
            directo, reverso = args.directo, args.reverso
        elif args.infusion:
            print("el ensamblado por homología necesita --directo y --reverso: los "
                  "brazos de homología los llevan las colas 5' y no se pueden "
                  "inventar", file=sys.stderr)
            return 2
        else:
            directo, reverso, i0, f0 = cebadores_automaticos(
                donante, enz5, enz3, args.proteccion, args.kozak,
                inicio_cds=(args.inicio_cds - 1) if args.inicio_cds else None,
                fin_cds=args.fin_cds)
            print(f"cebadores calculados a partir del CDS {i0 + 1}..{f0} del donante")

        res_pcr = pcr(donante, directo, reverso)
        if args.infusion:
            res = ensambla_solapes(aceptor, res_pcr, enz5, nombre, args.min_solape,
                                   args.nombre_orf)
        else:
            res = liga(aceptor, res_pcr, enz5, enz3, nombre)
    except ErrorClonaje as e:
        print(f"\nEl clonaje no sale: {e}\n", file=sys.stderr)
        return 1

    os.makedirs(args.salida, exist_ok=True)
    base = os.path.join(args.salida, nombre.replace("/", "_"))
    como = (f"ensamblado por homología sobre {enz5.nombre}"
            if args.infusion else f"con {enz5.nombre} + {enz3.nombre}")
    desc = (f"{nombre}: amplicón de {donante.nombre} clonado en {aceptor.nombre} "
            f"{como}. Simulado, sin verificar por secuenciación.")
    f_dna = escribe_dna(res.producto, base + ".dna", desc,
                        getattr(res.producto, "cebadores_snapgene", ()))
    f_gb = escribe_genbank(res.producto, base + ".gb", desc)
    f_amp = escribe_genbank(res.amplicon, base + "_amplicon.gb",
                            "amplicón de PCR antes de digerir")
    f_md = base + "_informe.md"
    with open(f_md, "w", encoding="utf-8") as fh:
        fh.write(informe(res))

    print(f"\nProducto: {nombre} — {len(res.producto.seq)} pb circular")
    print(f"  inserto {len(res.inserto)} pb, amplicón {len(res.amplicon.seq)} pb")
    print(f"  cebador directo: {res_pcr.directo}")
    print(f"  cebador reverso: {res_pcr.reverso}")
    for x in res_pcr.avisos + res.avisos:
        print(f"  aviso: {x}")
    print("\nFicheros:")
    for f in (f_dna, f_gb, f_amp, f_md):
        print(f"  {os.path.abspath(f)}")
    print("\nAbre el .dna con SnapGene Viewer (gratis). El .gb es el plan B.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
