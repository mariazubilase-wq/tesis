"""Lectura y **escritura** de ficheros `.dna` de SnapGene, sin dependencias.

El formato `.dna` es una secuencia de paquetes:

    1 byte   tipo
    4 bytes  longitud (big-endian, sin signo)
    N bytes  datos

Tipos que se usan aquí:

| Tipo | Contenido |
|---|---|
| `0x09` | *cookie* de cabecera, **tiene que ser el primer paquete** |
| `0x00` | secuencia (1 byte de banderas + bases en ASCII) |
| `0x05` | cebadores (XML) |
| `0x06` | notas (XML) |
| `0x0A` | rasgos (XML) |

El byte de banderas de `0x00`: bit 0 = circular, bit 1 = doble hebra.

**Para qué sirve esto:** SnapGene Viewer (gratis) abre `.dna` y muestra el mapa,
los rasgos y los cebadores; lo que la licencia de pago aporta es *crear y editar*.
Generando el `.dna` aquí, el visor gratuito hace el resto.

Escrito sobre el formato tal y como lo documenta el lector de Biopython
(`Bio.SeqIO.SnapGeneIO`). Si una versión de SnapGene se queja de un fichero,
el GenBank que escribe `formatos.escribe_genbank` es el plan B.
"""
from __future__ import annotations

import datetime
import re
import struct
import xml.etree.ElementTree as ET
from html import escape

from formatos import Rasgo, Registro
from seqlib import limpia

COOKIE = b"SnapGene"

T_SEQ = 0x00
T_CEBADORES = 0x05
T_NOTAS = 0x06
T_COOKIE = 0x09
T_RASGOS = 0x0A

# Colores por tipo de rasgo, aproximando el criterio de SnapGene.
COLORES = {
    "CDS": "#ff7f50",
    "gene": "#ff7f50",
    "promoter": "#ffff80",
    "terminator": "#ff8080",
    "polyA_signal": "#ff8080",
    "rep_origin": "#ffac75",
    "primer_bind": "#a6acb3",
    "protein_bind": "#b1ff67",
    "misc_feature": "#99ccff",
    "misc_recomb": "#c6c9d1",
    "regulatory": "#b4abac",
    "5'UTR": "#c0c0c0",
    "3'UTR": "#c0c0c0",
}
COLOR_POR_DEFECTO = "#99ccff"


# ---------------------------------------------------------------------------
# Lectura
# ---------------------------------------------------------------------------

def _paquetes(datos: bytes):
    i = 0
    while i + 5 <= len(datos):
        tipo = datos[i]
        (n,) = struct.unpack(">I", datos[i + 1:i + 5])
        cuerpo = datos[i + 5:i + 5 + n]
        if len(cuerpo) != n:
            raise ValueError("fichero .dna truncado")
        yield tipo, cuerpo
        i += 5 + n


def lee_dna(ruta: str) -> Registro:
    """Lee un `.dna` y devuelve un `Registro` como los de `formatos`."""
    with open(ruta, "rb") as fh:
        datos = fh.read()
    if not datos[:1] or datos[0] != T_COOKIE:
        raise ValueError(f"{ruta}: no empieza por el paquete de cabecera de SnapGene")

    seq, circular, nombre = "", True, ""
    rasgos: list[Rasgo] = []

    for tipo, cuerpo in _paquetes(datos):
        if tipo == T_COOKIE:
            if cuerpo[:8] != COOKIE:
                raise ValueError(f"{ruta}: cabecera inesperada {cuerpo[:8]!r}")
        elif tipo == T_SEQ:
            circular = bool(cuerpo[0] & 0x01)
            seq = limpia(cuerpo[1:].decode("ascii", "replace"))
        elif tipo == T_RASGOS:
            rasgos.extend(_lee_rasgos(cuerpo))
        elif tipo == T_CEBADORES:
            rasgos.extend(_lee_cebadores(cuerpo))
        elif tipo == T_NOTAS:
            nombre = _lee_nombre(cuerpo) or nombre

    if not seq:
        raise ValueError(f"{ruta}: no contiene paquete de secuencia")

    base = re.sub(r"\.dna$", "", ruta.rsplit("/", 1)[-1], flags=re.I)
    return Registro(nombre or base or "sin_nombre", seq, circular, rasgos, ruta)


def _texto_xml(cuerpo: bytes) -> str:
    return cuerpo.decode("utf-8", "replace").lstrip("﻿")


def _lee_nombre(cuerpo: bytes) -> str:
    try:
        xml = ET.fromstring(_texto_xml(cuerpo))
    except ET.ParseError:
        return ""
    for et in ("CustomMapLabel", "Description"):
        n = xml.find(et)
        if n is not None and (n.text or "").strip():
            return n.text.strip()
    return ""


def _lee_rasgos(cuerpo: bytes) -> list[Rasgo]:
    try:
        xml = ET.fromstring(_texto_xml(cuerpo))
    except ET.ParseError:
        return []
    fuera: list[Rasgo] = []
    for f in xml.findall("Feature"):
        segmentos = f.findall("Segment")
        trozos = []
        for s in segmentos:
            rango = s.get("range", "")
            if "-" not in rango:
                continue
            a, b = rango.split("-", 1)
            try:
                trozos.append((int(a), int(b)))
            except ValueError:
                continue
        if not trozos:
            continue
        hebra = -1 if f.get("directionality") == "2" else 1
        etiqueta = f.get("name", "")
        cual = {}
        for q in f.findall("Q"):
            v = q.find("V")
            if v is not None:
                cual[q.get("name", "")] = v.get("text") or v.get("int") or ""
        fuera.append(Rasgo(
            clave=f.get("type", "misc_feature"),
            inicio=min(a for a, _ in trozos) - 1,   # SnapGene es 1-based inclusivo
            fin=max(b for _, b in trozos),
            hebra=hebra,
            etiqueta=etiqueta or cual.get("label", ""),
            cualificadores=cual,
            compuesto=len(trozos) > 1,
        ))
    return fuera


def _lee_cebadores(cuerpo: bytes) -> list[Rasgo]:
    """Los cebadores se devuelven como rasgos `primer_bind`."""
    try:
        xml = ET.fromstring(_texto_xml(cuerpo))
    except ET.ParseError:
        return []
    fuera: list[Rasgo] = []
    for c in xml.findall("Primer"):
        for s in c.findall("BindingSite"):
            loc = s.get("location", "")
            if "-" not in loc:
                continue
            a, b = loc.split("-", 1)
            try:
                i, f = int(a), int(b)
            except ValueError:
                continue
            hebra = -1 if s.get("boundStrand") == "1" else 1
            fuera.append(Rasgo("primer_bind", i, f + 1, hebra,
                               c.get("name", "cebador"),
                               {"note": c.get("sequence", "")}))
    return fuera


# ---------------------------------------------------------------------------
# Escritura
# ---------------------------------------------------------------------------

def _paquete(tipo: int, cuerpo: bytes) -> bytes:
    return bytes([tipo]) + struct.pack(">I", len(cuerpo)) + cuerpo


def _xml_rasgos(registro: Registro) -> bytes:
    partes = [f'<Features nextValidID="{len(registro.rasgos)}">']
    for i, r in enumerate(registro.rasgos):
        inicio = max(1, r.inicio + 1)
        fin = min(len(registro.seq), r.fin)
        if fin < inicio:
            continue
        color = COLORES.get(r.clave, COLOR_POR_DEFECTO)
        direccion = "2" if r.hebra == -1 else "1"
        nombre = escape(r.etiqueta or r.clave, quote=True)
        partes.append(
            f'<Feature recentID="{i}" name="{nombre}" type="{escape(r.clave, quote=True)}"'
            f' directionality="{direccion}" allowSegmentOverlaps="0"'
            f' consecutiveTranslationNumbering="1">'
        )
        partes.append(
            f'<Segment range="{inicio}-{fin}" color="{color}" type="standard"'
            f' name="{nombre}"/>'
        )
        partes.append(f'<Q name="label"><V text="{nombre}"/></Q>')
        nota = r.cualificadores.get("note", "")
        if nota:
            partes.append(f'<Q name="note"><V text="{escape(str(nota), quote=True)}"/></Q>')
        partes.append("</Feature>")
    partes.append("</Features>")
    return "".join(partes).encode("utf-8")


def _xml_cebadores(cebadores) -> bytes:
    """`cebadores`: lista de (nombre, secuencia, inicio0, fin, hebra)."""
    partes = [f'<Primers nextValidID="{len(cebadores)}">']
    for i, (nombre, seq, inicio, fin, hebra) in enumerate(cebadores):
        hebra_unida = "1" if hebra == -1 else "0"
        partes.append(
            f'<Primer recentID="{i}" name="{escape(nombre, quote=True)}"'
            f' sequence="{escape(seq.upper(), quote=True)}">'
            f'<BindingSite location="{inicio}-{max(inicio, fin - 1)}"'
            f' boundStrand="{hebra_unida}" simplified="1"/>'
            f'</Primer>'
        )
    partes.append("</Primers>")
    return "".join(partes).encode("utf-8")


def _xml_notas(registro: Registro, descripcion: str) -> bytes:
    hoy = datetime.date.today().strftime("%Y.%m.%d")   # formato de SnapGene
    partes = [
        "<Notes>",
        f"<Created>{hoy}</Created>",
        f"<LastModified>{hoy}</LastModified>",
        "<Type>Synthetic</Type>",
        "<SequenceClass>UNA</SequenceClass>",
        "<ConfirmedExperimentally>0</ConfirmedExperimentally>",
        f"<CustomMapLabel>{escape(registro.nombre, quote=True)}</CustomMapLabel>",
        "<UseCustomMapLabel>1</UseCustomMapLabel>",
        f"<Description>{escape(descripcion, quote=True)}</Description>",
        "</Notes>",
    ]
    return "".join(partes).encode("utf-8")


def escribe_dna(registro: Registro, ruta: str, descripcion: str = "",
                cebadores=()) -> str:
    """Escribe el registro como `.dna`. Devuelve la ruta."""
    seq = limpia(registro.seq)
    if not seq:
        raise ValueError("secuencia vacía")

    banderas = 0x02                      # doble hebra
    if registro.circular:
        banderas |= 0x01

    # Si se pasan cebadores, van en su propio paquete: anotarlos *además* como
    # rasgos los duplicaría en el mapa.
    nombres_cebador = {c[0] for c in cebadores}
    visible = Registro(registro.nombre, seq, registro.circular,
                       [r for r in registro.rasgos
                        if not (r.clave == "primer_bind"
                                and r.etiqueta in nombres_cebador)],
                       registro.procedencia)

    bloques = [
        _paquete(T_COOKIE, COOKIE + struct.pack(">HHH", 1, 14, 14)),
        _paquete(T_SEQ, bytes([banderas]) + seq.lower().encode("ascii")),
        _paquete(T_RASGOS, _xml_rasgos(visible)),
        _paquete(T_NOTAS, _xml_notas(registro, descripcion)),
    ]
    if cebadores:
        bloques.insert(3, _paquete(T_CEBADORES, _xml_cebadores(cebadores)))

    with open(ruta, "wb") as fh:
        fh.write(b"".join(bloques))
    return ruta
