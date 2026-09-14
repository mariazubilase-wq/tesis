"""Lectura de FASTA y GenBank sin dependencias externas."""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from seqlib import limpia


@dataclass
class Rasgo:
    clave: str
    inicio: int          # 0-based, inclusivo
    fin: int             # 0-based, exclusivo
    hebra: int           # +1 / -1
    etiqueta: str = ""
    cualificadores: dict = field(default_factory=dict)
    compuesto: bool = False

    def __len__(self) -> int:
        return self.fin - self.inicio


@dataclass
class Registro:
    nombre: str
    seq: str
    circular: bool = True
    rasgos: list = field(default_factory=list)
    procedencia: str = ""

    def __len__(self) -> int:
        return len(self.seq)

    def rasgos_como(self, *palabras: str) -> list:
        """Rasgos cuya etiqueta/clave contiene alguna de las palabras (sin distinguir mayúsculas)."""
        pal = [p.lower() for p in palabras]
        fuera = []
        for r in self.rasgos:
            texto = " ".join([r.clave, r.etiqueta,
                              " ".join(str(v) for v in r.cualificadores.values())]).lower()
            if any(p in texto for p in pal):
                fuera.append(r)
        return fuera


_LOC_SIMPLE = re.compile(r"(\d+)\s*\.\.\s*(\d+)")


def _parsea_localizacion(loc: str):
    """Devuelve (inicio0, fin, hebra, compuesto). Soporta a..b, complement(), join()."""
    compuesto = "join" in loc or "order" in loc
    hebra = -1 if "complement" in loc else 1
    nums = _LOC_SIMPLE.findall(loc)
    if not nums:
        solo = re.findall(r"\d+", loc)
        if not solo:
            return None
        p = int(solo[0])
        return p - 1, p, hebra, compuesto
    inicios = [int(a) for a, _ in nums]
    fines = [int(b) for _, b in nums]
    return min(inicios) - 1, max(fines), hebra, compuesto


def lee_genbank(texto: str, procedencia: str = "") -> Registro:
    lineas = texto.splitlines()
    nombre, circular = "", False
    seq_partes: list[str] = []
    rasgos: list[Rasgo] = []

    modo = None
    rasgo_actual = None
    cual_clave = None
    cual_val: list[str] = []

    def cierra_cualificador():
        nonlocal cual_clave, cual_val
        if rasgo_actual is not None and cual_clave:
            v = " ".join(cual_val).strip().strip('"')
            rasgo_actual.cualificadores[cual_clave] = v
            if cual_clave in ("label", "gene", "product", "note", "standard_name") \
                    and not rasgo_actual.etiqueta:
                rasgo_actual.etiqueta = v
        cual_clave, cual_val = None, []

    for ln in lineas:
        if ln.startswith("LOCUS"):
            campos = ln.split()
            if len(campos) > 1:
                nombre = campos[1]
            circular = "circular" in ln.lower()
            continue
        if ln.startswith("FEATURES"):
            modo = "rasgos"
            continue
        if ln.startswith("ORIGIN"):
            cierra_cualificador()
            modo = "seq"
            continue
        if ln.startswith("//"):
            modo = None
            continue

        if modo == "rasgos":
            if len(ln) > 5 and ln[5] != " " and not ln.startswith("     "):
                continue
            cuerpo = ln[5:] if len(ln) > 5 else ""
            if ln[:21].strip() and not cuerpo.lstrip().startswith("/"):
                # Línea de cabecera de rasgo: clave + localización
                cierra_cualificador()
                clave = ln[5:21].strip()
                loc = ln[21:].strip()
                p = _parsea_localizacion(loc)
                if p:
                    rasgo_actual = Rasgo(clave, p[0], p[1], p[2], compuesto=p[3])
                    rasgos.append(rasgo_actual)
                else:
                    rasgo_actual = None
            elif cuerpo.lstrip().startswith("/"):
                cierra_cualificador()
                trozo = cuerpo.lstrip()[1:]
                if "=" in trozo:
                    cual_clave, v = trozo.split("=", 1)
                    cual_val = [v]
                else:
                    cual_clave, cual_val = trozo, [""]
            elif cual_clave is not None:
                cual_val.append(cuerpo.strip())
        elif modo == "seq":
            seq_partes.append(limpia(ln))

    cierra_cualificador()
    return Registro(nombre or "sin_nombre", "".join(seq_partes), circular, rasgos, procedencia)


def lee_fasta(texto: str, procedencia: str = "") -> Registro:
    nombre, partes = "sin_nombre", []
    for ln in texto.splitlines():
        if ln.startswith(">"):
            if partes:
                break
            nombre = ln[1:].strip().split()[0] if ln[1:].strip() else "sin_nombre"
        else:
            partes.append(limpia(ln))
    return Registro(nombre, "".join(partes), True, [], procedencia)


def lee(ruta: str) -> Registro:
    with open(ruta, "r", encoding="utf-8", errors="replace") as fh:
        texto = fh.read()
    if re.search(r"^LOCUS", texto, re.M):
        r = lee_genbank(texto, ruta)
    elif texto.lstrip().startswith(">"):
        r = lee_fasta(texto, ruta)
    else:
        # Texto plano: sólo secuencia.
        r = Registro("sin_nombre", limpia(texto), True, [], ruta)
    if not r.seq:
        raise ValueError(f"No se ha podido extraer secuencia de {ruta}")
    bases = set(r.seq) - set("ACGTN")
    if bases:
        raise ValueError(f"{ruta}: bases no reconocidas {sorted(bases)[:8]}")
    return r
