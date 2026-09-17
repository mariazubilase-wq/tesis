#!/usr/bin/env python3
"""Cierra el diseño de clonaje de un cDNA en un vector parental de minicírculo.

Lee el plásmido donante (p. ej. pCMV6-KRT10) y el vector aceptor
(pMC.EF1a-MCS-SV40polyA), y produce:

  * localización y validación del ORF en el donante (stop nativo, etiquetas)
  * mapa de la region attB-attP del aceptor y de la ventana de MCS utilizable
  * recuento de dianas en TODO el plásmido aceptor y en el inserto
  * parejas direccionales válidas, ordenadas
  * primers completos con bases de protección, Kozak y codones stop
  * tamaños esperados de PCR, construcción final, minicírculo y digestiones

No inventa secuencia: todo sale de los ficheros que se le pasan.

Uso:
  python3 disena_clonaje.py --donante pCMV6-KRT10.gb \
                            --aceptor pMC.EF1a-MCS-SV40polyA.gb \
                            --salida informe.md
  python3 disena_clonaje.py --autotest
"""
from __future__ import annotations

import argparse
import os
import sys
import textwrap

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import seqlib as S
from enzimas import (ETIQUETAS_PEPTIDO, MOTIVOS, PANEL_EXTRA, PANEL_NEVERA,
                     POR_NOMBRE, TODAS, Enzima)
from formatos import Rasgo, Registro, lee

KOZAK = "GCCACC"
STOPS_DOBLE = "TAATGA"      # dos codones stop en tándem
PROTECCION_DEF = "CACCAC"   # 6 bases de protección, GC equilibrado


# ===========================================================================
# Donante: encontrar el ORF
# ===========================================================================
def encuentra_orf(reg: Registro, min_aa: int = 200,
                  gen: str | None = None, fin_orf: int | None = None,
                  inicio_orf: int | None = None,
                  recortar: bool = True) -> dict:
    """Localiza el ORF de interés y, si viene fusionado a una etiqueta,
    lo recorta hasta el final nativo del gen.

    fin_orf: posición (1-based, sobre el donante) del último nt del ORF nativo,
             para forzar el recorte a mano.
    """
    candidatos = []

    for r in reg.rasgos:
        if r.clave.upper() != "CDS" or r.compuesto:
            continue
        etiqueta = (r.etiqueta or "").lower()
        if gen and gen.lower() not in etiqueta and gen.lower() not in \
                " ".join(str(v).lower() for v in r.cualificadores.values()):
            continue
        sub = reg.seq[r.inicio:r.fin]
        if r.hebra == -1:
            sub = S.rc(sub)
        candidatos.append(("anotacion CDS", r.inicio, r.fin, r.hebra, sub,
                           r.etiqueta))

    if not candidatos:
        for hebra, s in ((1, reg.seq), (-1, S.rc(reg.seq))):
            for pauta in range(3):
                i = pauta
                while i < len(s) - 2:
                    if s[i:i + 3] == "ATG":
                        j = i
                        while j < len(s) - 2:
                            if S.CODIGO.get(s[j:j + 3], "X") == "*":
                                break
                            j += 3
                        largo = j - i
                        if largo // 3 >= min_aa:
                            fin_inc_stop = min(j + 3, len(s))
                            sub = s[i:fin_inc_stop]
                            if hebra == 1:
                                ini0, fin0 = i, fin_inc_stop
                            else:
                                ini0 = len(s) - fin_inc_stop
                                fin0 = len(s) - i
                            candidatos.append(("ORF mas largo de las 6 pautas",
                                               ini0, fin0, hebra, sub, ""))
                            i = j + 3
                            continue
                    i += 3

    if not candidatos:
        raise SystemExit("No se ha encontrado ningún ORF de tamaño razonable "
                         "en el donante.")

    candidatos.sort(key=lambda c: len(c[4]), reverse=True)
    origen, ini, fin, hebra, sub, etiqueta_rasgo = candidatos[0]

    tiene_stop = S.CODIGO.get(sub[-3:], "X") == "*"
    orf_completo = sub[:-3] if tiene_stop else sub      # sin el stop

    # --- Recorte 5': un ATG en fase río arriba alarga el ORF artificialmente.
    # En un clon de lanzadera el ATG real va justo detrás del sitio de clonaje.
    recorte5 = {"aplicado": False, "motivo": "", "aa_eliminados": 0, "sitio": ""}
    desplaz5 = 0
    if inicio_orf is not None:
        nt = (inicio_orf - 1 - ini) if hebra == 1 else (fin - inicio_orf)
        if not (0 <= nt < len(orf_completo)) or nt % 3:
            raise SystemExit(f"--inicio-orf {inicio_orf} no cae en fase dentro "
                             f"del ORF localizado ({ini+1}-{fin}).")
        desplaz5 = nt
        recorte5.update(aplicado=True, motivo="posición indicada con --inicio-orf",
                        aa_eliminados=nt // 3)
    elif recortar:
        cabeza = orf_completo[:120]
        mejor = None
        for nombre in ("SgfI", "AsiSI", "NheI-HF", "NotI", "EcoRI", "HindIII",
                       "KpnI", "BamHI-HF", "XhoI", "SalI"):
            e = POR_NOMBRE.get(nombre)
            if not e:
                continue
            for rel in S.busca(cabeza, e.diana):
                fin_sitio = rel + len(e.diana)
                for k in range(fin_sitio, len(cabeza) - 2):
                    if k % 3 == 0 and orf_completo[k:k + 3] == "ATG":
                        if mejor is None or k > mejor[0]:
                            mejor = (k, e.nombre)
                        break
        if mejor and mejor[0] > 0:
            desplaz5 = mejor[0]
            recorte5.update(aplicado=True,
                            motivo=f"había un ATG en fase río arriba; el ATG real "
                                   f"es el primero tras el sitio {mejor[1]}",
                            aa_eliminados=mejor[0] // 3, sitio=mejor[1])

    if desplaz5:
        orf_completo = orf_completo[desplaz5:]
        if hebra == 1:
            ini += desplaz5
        else:
            fin -= desplaz5

    prot_completa = S.traduce(orf_completo)

    # --- ¿Hay una etiqueta fusionada en el extremo C? ----------------------
    etiquetas = []
    for nombre, pep in ETIQUETAS_PEPTIDO.items():
        k = prot_completa.find(pep)
        if k != -1:
            etiquetas.append((nombre, k, pep))
    etiquetas.sort(key=lambda t: t[1])

    recorte = {"aplicado": False, "motivo": "", "aa_eliminados": 0,
               "sitio": "", "residuos_entre": ""}
    cds = orf_completo

    if fin_orf is not None:
        # Recorte manual: fin_orf es 1-based sobre el donante.
        if hebra == 1:
            nt = fin_orf - ini
        else:
            nt = fin - fin_orf + 1
        if not (0 < nt <= len(orf_completo)):
            raise SystemExit(f"--fin-orf {fin_orf} cae fuera del ORF localizado "
                             f"({ini+1}-{fin}).")
        if nt % 3:
            raise SystemExit(f"--fin-orf {fin_orf} no deja un múltiplo de 3 "
                             f"({nt} nt).")
        cds = orf_completo[:nt]
        recorte.update(aplicado=True, motivo="posición indicada con --fin-orf",
                       aa_eliminados=(len(orf_completo) - nt) // 3)

    elif recortar and etiquetas:
        primer_aa = etiquetas[0][1]
        # Sitio de lanzadera en fase justo por delante de la etiqueta.
        ventana_ini = max(0, (primer_aa - 12) * 3)
        ventana = orf_completo[ventana_ini:primer_aa * 3]
        corte_nt = None
        sitio = ""
        for nombre in ("MluI", "NotI", "XhoI", "SalI", "AscI", "BamHI-HF",
                       "AgeI", "SgfI"):
            e = POR_NOMBRE.get(nombre)
            if not e:
                continue
            for rel in S.busca(ventana, e.diana):
                abs_nt = ventana_ini + rel
                if abs_nt % 3 == 0 and (corte_nt is None or abs_nt < corte_nt):
                    corte_nt, sitio = abs_nt, e.nombre
        if corte_nt is None:
            corte_nt, sitio = primer_aa * 3, "inicio de la etiqueta"
        residuos = prot_completa[corte_nt // 3:primer_aa]
        cds = orf_completo[:corte_nt]
        recorte.update(aplicado=True,
                       motivo=f"etiqueta {etiquetas[0][0]} fusionada en C-terminal",
                       aa_eliminados=(len(orf_completo) - corte_nt) // 3,
                       sitio=sitio, residuos_entre=residuos)

    if hebra == 1:
        despues = reg.seq[fin:fin + 300]
        antes = reg.seq[max(0, ini - 60):ini]
    else:
        despues = S.rc(reg.seq[max(0, ini - 300):ini])
        antes = S.rc(reg.seq[fin:fin + 60])

    return {
        "origen": origen, "inicio": ini, "fin": fin, "hebra": hebra,
        "etiqueta_rasgo": etiqueta_rasgo, "seq_con_stop": sub,
        "orf_completo": orf_completo, "prot_completa": prot_completa,
        "cds": cds, "tiene_stop_nativo": tiene_stop,
        "contexto_5p": antes, "contexto_3p": despues,
        "etiquetas_detectadas": [(n, k) for n, k, _ in etiquetas],
        "recorte": recorte, "recorte5": recorte5,
        "proteina": S.traduce(cds),
    }


# ===========================================================================
# Aceptor: región del minicírculo y ventana de MCS
# ===========================================================================
def mapea_aceptor(reg: Registro) -> dict:
    info = {"attB": [], "attP": [], "isceI": [], "promotor": [], "polya": [],
            "avisos": []}

    for r in reg.rasgos:
        et = (r.etiqueta or "").lower() + " " + r.clave.lower()
        if "attb" in et:
            info["attB"].append(r)
        elif "attp" in et:
            info["attP"].append(r)
        if "i-scei" in et or "i-sce" in et or "sceI".lower() in et:
            info["isceI"].append(r)
        if "promoter" in r.clave.lower() or "ef1" in et or "ef-1" in et:
            info["promotor"].append(r)
        if "polya" in et.replace(" ", "") or "poly_a" in et or "sv40" in et:
            info["polya"].append(r)

    # Respaldo por motivo si la anotación no los trae.
    for clave, motivo in (("attB", "attB_phiC31_min"), ("attP", "attP_phiC31_min")):
        if not info[clave]:
            pos = S.busca_ambas(reg.seq, MOTIVOS[motivo], reg.circular)
            for p in pos:
                info[clave].append(
                    Rasgo(clave, p, p + len(MOTIVOS[motivo]), 1,
                          f"{clave} (por motivo)"))
            if pos:
                info["avisos"].append(
                    f"{clave} no estaba anotado; localizado por motivo ΦC31 en {pos}.")
    if not info["isceI"]:
        pos = S.busca_ambas(reg.seq, MOTIVOS["I-SceI"], reg.circular)
        for p in pos:
            info["isceI"].append(
                Rasgo("I-SceI", p, p + 18, 1, "I-SceI (por motivo)"))

    if not info["attB"] or not info["attP"]:
        info["avisos"].append(
            "ATENCIÓN: no se han podido localizar attB y/o attP. Sin ellos no se "
            "puede comprobar que el casete caiga dentro del minicírculo. "
            "Anótalos en el GenBank y vuelve a ejecutar.")
        info["region"] = None
        return info

    b = info["attB"][0]
    p = info["attP"][0]
    # La región del minicírculo es la que va de un att al otro; en un plásmido
    # circular hay dos arcos: nos quedamos con el que contiene promotor y polyA.
    n = len(reg.seq)
    arcos = [(b.fin % n, p.inicio % n), (p.fin % n, b.inicio % n)]

    def contiene(arco, pos):
        a, z = arco
        return (a <= pos < z) if a <= z else (pos >= a or pos < z)

    def largo(arco):
        a, z = arco
        return (z - a) % n or n

    elegido = None
    refs = [r.inicio for r in info["promotor"] + info["polya"]]
    if refs:
        for arco in arcos:
            if all(contiene(arco, x) for x in refs):
                elegido = arco
                break
    if elegido is None:
        elegido = min(arcos, key=largo)
        info["avisos"].append(
            "La región del minicírculo se ha elegido por tamaño, no por "
            "contenido: comprueba a mano que promotor y polyA caen dentro.")

    info["region"] = elegido
    info["region_len"] = largo(elegido)
    info["contiene"] = contiene
    return info


def ventana_mcs(reg: Registro, mapa: dict) -> tuple[int, int] | None:
    """Intervalo utilizable entre el final del promotor y el inicio del polyA."""
    if not mapa["promotor"] or not mapa["polya"]:
        return None
    n = len(reg.seq)
    fin_prom = max(r.fin for r in mapa["promotor"]) % n
    ini_polya = min(r.inicio for r in mapa["polya"]) % n
    if (ini_polya - fin_prom) % n > n // 2:
        return None
    return fin_prom, ini_polya


# ===========================================================================
# Análisis de dianas
# ===========================================================================
def analiza_enzimas(aceptor: Registro, mapa: dict, ventana, inserto: str,
                    panel: list[Enzima], modo: str = "vector") -> list[dict]:
    filas = []
    n = len(aceptor.seq)
    contiene = mapa.get("contiene")
    region = mapa.get("region")

    for e in panel:
        pos_ac = S.busca_ambas(aceptor.seq, e.diana, aceptor.circular)
        pos_ins = S.busca_ambas(inserto, e.diana, False)
        en_ventana = []
        if ventana:
            a, z = ventana
            for p in pos_ac:
                dentro = (a <= p < z) if a <= z else (p >= a or p < z)
                if dentro:
                    en_ventana.append(p)
        en_region = [p for p in pos_ac if region and contiene(region, p)] \
            if region else []

        veredicto, motivo = "usable", ""
        if len(pos_ac) == 0:
            veredicto, motivo = "no", ("no está en el MCS" if modo == "mcs"
                                       else "no corta el aceptor")
        elif len(pos_ac) > 1 and modo != "mcs":
            veredicto, motivo = "no", f"{len(pos_ac)} dianas en el aceptor (no es única)"
        elif len(pos_ac) > 1:
            veredicto, motivo = "no", f"{len(pos_ac)} dianas dentro del MCS"
        elif ventana and not en_ventana:
            veredicto, motivo = "no", "su única diana cae fuera del MCS (promotor-polyA)"
        elif region and not en_region:
            veredicto, motivo = "no", "su única diana cae FUERA de la región attB-attP"
        if pos_ins:
            veredicto, motivo = "no", f"corta el inserto {len(pos_ins)} vez/veces"
        if e.dam == "siempre":
            veredicto, motivo = "no", "bloqueada siempre por metilación Dam"

        filas.append({
            "enzima": e, "pos_aceptor": pos_ac, "n_aceptor": len(pos_ac),
            "pos_inserto": pos_ins, "en_ventana": en_ventana,
            "en_region": en_region, "veredicto": veredicto, "motivo": motivo,
        })
    return filas


def parejas(filas: list[dict], ventana) -> list[dict]:
    usables = [f for f in filas if f["veredicto"] == "usable" and f["en_ventana"]]
    fuera = []
    for i, a in enumerate(usables):
        for b in usables[i + 1:]:
            ea, eb = a["enzima"], b["enzima"]
            if ea.saliente == 0 or eb.saliente == 0:
                continue  # queremos clonaje direccional, no romo
            sa, sb = ea.saliente_seq(), eb.saliente_seq()
            if sa == sb or sa == S.rc(sb):
                continue  # extremos compatibles -> religación/inversión
            pa, pb = a["en_ventana"][0], b["en_ventana"][0]
            if pa == pb:
                continue
            arriba, abajo = (a, b) if pa < pb else (b, a)
            ea2, eb2 = arriba["enzima"], abajo["enzima"]
            sep = abs(pa - pb)

            # Puntuación: lo que ya tienes > sin actividad star > sin riesgo Dam.
            punt = 0.0
            razones = []
            if ea2.nevera and eb2.nevera:
                punt += 1000
                razones.append("las dos en el congelador")
            else:
                punt += 300 * (ea2.nevera + eb2.nevera)
            for e_ in (ea2, eb2):
                if e_.nombre.endswith("-HF"):
                    punt += 100
                if e_.dam == "solapante":
                    punt -= 300
                    razones.append(f"{e_.nombre} puede bloquearla Dam")
                if e_.saliente in (2, -2):
                    punt -= 40      # salientes de 2 nt ligan peor
            punt += sep
            if not any(e_.nombre.endswith("-HF") for e_ in (ea2, eb2)):
                razones.append("ninguna es versión HF")
            fuera.append({
                "cinco": arriba, "tres": abajo,
                "ambas_nevera": ea2.nevera and eb2.nevera,
                "separacion": sep, "punt": punt, "razones": razones,
            })
    fuera.sort(key=lambda d: -d["punt"])
    return fuera


# ===========================================================================
# Primers
# ===========================================================================
def ajusta_ancla(seq: str, tm_obj: float, minimo: int = 18, maximo: int = 32,
                 desde_final: bool = False) -> str:
    """Recorta/alarga la zona de apareamiento para acercarse a la Tm objetivo."""
    mejor, mejor_d = None, 1e9
    for L in range(minimo, min(maximo, len(seq)) + 1):
        trozo = seq[-L:] if desde_final else seq[:L]
        t = S.tm_nn(trozo)
        if t != t:
            continue
        # Preferimos terminar en G/C (pinza 3')
        castigo = 0.0 if (trozo[-1] if not desde_final else trozo[-1]) in "GC" else 0.6
        d = abs(t - tm_obj) + castigo
        if d < mejor_d:
            mejor, mejor_d = trozo, d
    return mejor or (seq[:minimo] if not desde_final else seq[-minimo:])


def construye_primers(cds: str, enz5: Enzima, enz3: Enzima,
                      proteccion: str = PROTECCION_DEF,
                      tm_obj: float = 62.0,
                      kozak: bool = True,
                      stops: str = STOPS_DOBLE) -> dict:
    ancla_f = ajusta_ancla(cds, tm_obj, desde_final=False)
    cola_f = proteccion + enz5.diana + (KOZAK if kozak else "")
    fwd = cola_f + ancla_f

    fin_cds = cds[-33:]
    ancla_r_top = ajusta_ancla(fin_cds, tm_obj, desde_final=True)
    cola_r = proteccion + enz3.diana + S.rc(stops)
    rev = cola_r + S.rc(ancla_r_top)

    # Amplicón (hebra superior) = cola del directo + CDS + rc(cola del reverso)
    producto = cola_f + cds + S.rc(cola_r)

    return {
        "fwd": fwd, "rev": rev,
        "ancla_f": ancla_f, "ancla_r": ancla_r_top,
        "tm_ancla_f": S.tm_nn(ancla_f), "tm_ancla_r": S.tm_nn(S.rc(ancla_r_top)),
        "tm_total_f": S.tm_nn(fwd), "tm_total_r": S.tm_nn(rev),
        "producto": producto,
    }


# ===========================================================================
# Informe
# ===========================================================================
def _tabla(cabeceras, filas) -> str:
    out = ["| " + " | ".join(cabeceras) + " |",
           "|" + "|".join("---" for _ in cabeceras) + "|"]
    for f in filas:
        out.append("| " + " | ".join(str(x) for x in f) + " |")
    return "\n".join(out)


def _avisos_metilacion(secuencia_final: str, enzimas: list[Enzima]) -> list[str]:
    avisos = []
    for e in enzimas:
        for p in S.busca_ambas(secuencia_final, e.diana, False):
            ctx = secuencia_final[max(0, p - 4):p + len(e.diana) + 4]
            if "GATC" in ctx and e.dam == "solapante":
                avisos.append(
                    f"{e.nombre}: hay un GATC solapando su diana en el contexto "
                    f"`{ctx}` → Dam la bloquea. Cambia las bases de protección.")
            elif "GATC" in ctx and e.dam == "no" and "GATC" not in e.diana:
                avisos.append(
                    f"{e.nombre}: aparece un GATC junto a la diana (`{ctx}`). "
                    f"No consta sensibilidad a Dam, pero confírmalo en NEBcloner.")
            for w in ("CCAGG", "CCTGG"):
                if w in ctx:
                    avisos.append(
                        f"{e.nombre}: sitio Dcm ({w}) en el contexto `{ctx}`. "
                        f"Comprueba en NEBcloner si le afecta.")
    return sorted(set(avisos))


def informe(donante: Registro, aceptor: Registro, orf: dict, mapa: dict,
            ventana, filas: list[dict], pares: list[dict],
            elegido: dict | None, prim: dict | None,
            proteccion: str, modo: str = "vector") -> str:
    L = []
    ap = L.append
    n = len(aceptor.seq)

    ap("# Informe de diseño de clonaje — generado por `disena_clonaje.py`\n")
    ap("> Todo lo que sigue está calculado sobre los ficheros indicados. "
       "Ninguna secuencia está escrita a mano.\n")
    if modo == "mcs":
        ap("> ### ⚠️ Modo MCS suelto\n>\n"
           "> Se ha trabajado **sólo con la secuencia del MCS**, sin el mapa del "
           "plásmido parental completo. Por tanto **NO se ha podido comprobar**:\n>\n"
           "> 1. que cada diana sea **única en todo el plásmido parental** (si la "
           "enzima corta también en el esqueleto, el vector se parte en dos y el "
           "clonaje no sale);\n"
           "> 2. que el MCS caiga **dentro de la región attB–attP** (si no, el "
           "inserto acaba en el esqueleto que destruye la I-SceI y el minicírculo "
           "sale vacío);\n"
           "> 3. la **orientación** del MCS respecto al promotor EF1α.\n>\n"
           "> Los tres son condiciones necesarias. Vuelve a ejecutar con "
           "`--aceptor` en cuanto tengas el GenBank.\n")

    # --- Entradas
    ap("## 1. Entradas\n")
    ap(_tabla(["Papel", "Fichero", "Nombre", "Longitud", "Topología", "Rasgos"], [
        ["Donante", os.path.basename(donante.procedencia), donante.nombre,
         f"{len(donante)} pb", "circular" if donante.circular else "lineal",
         len(donante.rasgos)],
        ["Aceptor", os.path.basename(aceptor.procedencia), aceptor.nombre,
         f"{len(aceptor)} pb", "circular" if aceptor.circular else "lineal",
         len(aceptor.rasgos)],
    ]))
    ap("")

    # --- ORF
    ap("## 2. ORF del donante\n")
    cds = orf["cds"]
    prot = orf["proteina"]
    ap(_tabla(["Campo", "Valor"], [
        ["Cómo se ha localizado", orf["origen"]],
        ["Etiqueta del rasgo", orf["etiqueta_rasgo"] or "—"],
        ["Posición en el donante", f"{orf['inicio']+1}–{orf['fin']} "
                                   f"(hebra {'+' if orf['hebra']==1 else '−'})"],
        ["Longitud CDS sin stop", f"{len(cds)} pb"],
        ["Proteína", f"{len(prot)} aa"],
        ["Primeros 12 aa", prot[:12]],
        ["Últimos 12 aa", prot[-12:]],
        ["¿Múltiplo de 3?", "sí" if len(cds) % 3 == 0 else "NO — revisar"],
        ["¿ATG inicial?", "sí" if cds.startswith("ATG") else "NO — revisar"],
        ["ORF más largo encontrado", f"{len(orf['prot_completa'])} aa"],
        ["¿Ese ORF acaba en stop?", "sí" if orf["tiene_stop_nativo"] else
         "no (sigue en fase hasta el final del fichero)"],
        ["Stop interno prematuro", "sí — REVISAR" if "*" in prot else "no"],
        ["GC del CDS", f"{S.gc(cds):.1f} %"],
    ]))
    ap("")
    r5 = orf["recorte5"]
    if r5["aplicado"]:
        ap(f"> **Recorte 5' aplicado.** {r5['motivo']}. Se han descartado "
           f"{r5['aa_eliminados']} codones por delante del ATG real.\n>\n"
           "> ⚠️ Comprueba que los primeros aminoácidos de la tabla son el "
           "extremo N real de tu proteína; si no, usa `--inicio-orf`.\n")

    rec = orf["recorte"]
    if orf["etiquetas_detectadas"]:
        ap("**Etiqueta en fase en el extremo C del ORF:**\n")
        for nombre, pos in orf["etiquetas_detectadas"]:
            ap(f"- `{nombre}` empieza en el residuo {pos+1} del ORF largo.")
        ap("")
    if rec["aplicado"]:
        ap(f"> **Recorte aplicado.** Motivo: {rec['motivo']}. Se han quitado "
           f"**{rec['aa_eliminados']} aa** del extremo C "
           f"(corte en: {rec['sitio'] or 'posición indicada'}"
           + (f"; residuos de unión eliminados: `{rec['residuos_entre']}`"
              if rec["residuos_entre"] else "") + ").\n>\n"
           "> El CDS que se clona es **sólo el gen nativo**, y el primer reverso "
           "**aporta su propio codón stop**: la etiqueta no viaja al minicírculo. "
           "Es lo que se quiere para una copia de reemplazo terapéutica.\n>\n"
           "> ⚠️ **Comprueba que los últimos aminoácidos listados abajo son los "
           "del extremo C real de tu proteína.** Si no lo son, fuerza el corte "
           "con `--fin-orf <posición>`.\n")
    elif not orf["tiene_stop_nativo"]:
        ap("> ⚠️ El ORF no termina en stop y no se ha reconocido ninguna etiqueta "
           "conocida. Mira a mano qué hay por detrás antes de seguir, o indica el "
           "final con `--fin-orf`.\n")
    else:
        ap("> El ORF termina en su propio codón stop y no se ha detectado ninguna "
           "etiqueta: se clona tal cual.\n")

    # Zona rica en glicinas / repeticiones en el extremo 3'
    cola = cds[-300:]
    ap(f"- GC de los últimos 300 pb del CDS: **{S.gc(cola):.1f} %** "
       f"(las colas de glicinas de K1/K10 son ricas en GC y repetitivas: "
       f"afectan a la PCR y a la secuenciación).")
    tallo = S.peor_horquilla(cola[-60:])
    if tallo[0] >= 6:
        ap(f"- Repetición invertida de {tallo[0]} nt (`{tallo[1]}`) cerca del "
           f"extremo 3' del CDS.")
    ap("")

    # --- Aceptor
    ap("## 3. Aceptor: arquitectura\n")
    fil = []
    for clave, etiqueta in (("attB", "attB (ΦC31)"), ("attP", "attP (ΦC31)"),
                            ("isceI", "I-SceI"), ("promotor", "promotor"),
                            ("polya", "polyA")):
        for r in mapa[clave]:
            fil.append([etiqueta, r.etiqueta or r.clave,
                        f"{r.inicio+1}–{r.fin}", f"{len(r)} pb"])
    ap(_tabla(["Elemento", "Anotación", "Posición", "Tamaño"], fil or
              [["—", "nada anotado", "—", "—"]]))
    ap("")
    if mapa.get("region"):
        a, z = mapa["region"]
        ap(f"- **Región que acaba en el minicírculo (entre att):** {a+1}–{z} "
           f"→ **{mapa['region_len']} pb**.")
    if ventana:
        va, vz = ventana
        ancho = (vz - va) if (va <= vz and modo == "mcs") else ((vz - va) % n)
        etiq = ("**MCS analizado:**" if modo == "mcs" else
                "**Ventana de clonaje utilizable (fin del promotor → inicio del polyA):**")
        ap(f"- {etiq} {va+1}–{vz} → {ancho} pb.")
        hueco = aceptor.seq[va:vz] if va <= vz else aceptor.seq[va:] + aceptor.seq[:vz]
        atgs = S.busca(hueco, "ATG")
        if atgs:
            ap(f"- ⚠️ Hay {len(atgs)} `ATG` en la ventana, por delante de tu ORF "
               f"(posiciones relativas {atgs[:6]}). Comprueba si alguno crea un "
               f"uORF en la 5'UTR del transgén; si el sitio 5' elegido deja uno "
               f"por delante, usa el sitio más 3' posible.")
        else:
            ap("- Sin `ATG` espurios en la ventana por delante del ORF.")
    if modo == "mcs":
        truncadas = []
        seq_mcs = aceptor.seq
        for e in TODAS:
            d = e.diana
            for k in range(len(d) - 1, 3, -1):
                if seq_mcs.endswith(d[:k]) and not S.busca(seq_mcs, d):
                    truncadas.append((e.nombre, d, "final", d[:k]))
                    break
                if seq_mcs.startswith(d[-k:]) and not S.busca(seq_mcs, d):
                    truncadas.append((e.nombre, d, "principio", d[-k:]))
                    break
        vistas, limpio = set(), []
        for n_, d_, donde, trozo in truncadas:
            if d_ in vistas:
                continue
            vistas.add(d_)
            limpio.append((n_, d_, donde, trozo))
        if limpio:
            ap("- ⚠️ **Hay dianas cortadas por la mitad en los extremos de lo que "
               "has pegado**, lo que significa que el MCS real continúa más allá: "
               + "; ".join(f"`{n_}` ({d_}) — se ve `{trozo}` al {donde}"
                           for n_, d_, donde, trozo in limpio)
               + ". Pega el MCS completo o pasa el GenBank.")
    for av in mapa["avisos"]:
        ap(f"- ⚠️ {av}")
    ap("")

    # --- Enzimas
    ap("## 4. Dianas de restricción\n")
    if modo == "mcs":
        ap("Recuento sobre **el MCS que has pasado** y sobre el **inserto**. "
           "La columna «cortes aceptor» es aquí el MCS, no el plásmido: la "
           "unicidad en el parental completo queda sin comprobar.\n")
    else:
        ap("Recuento sobre el **plásmido parental entero** (circular), sobre la "
           "ventana promotor–polyA y sobre el **inserto**.\n")
    fil = []
    for f in sorted(filas, key=lambda f: (f["veredicto"] != "usable",
                                          not f["enzima"].nevera,
                                          f["enzima"].nombre)):
        e = f["enzima"]
        fil.append([
            ("**" + e.nombre + "**") if e.nevera else e.nombre,
            f"`{e.diana}`", e.tipo_extremo(),
            "sí" if e.nevera else "—",
            f["n_aceptor"],
            len(f["en_ventana"]),
            len(f["pos_inserto"]),
            "✅ usable" if f["veredicto"] == "usable" else f"❌ {f['motivo']}",
        ])
    ap(_tabla(["Enzima", "Diana", "Extremo", "En nevera", "Cortes aceptor",
               "En MCS", "Cortes inserto", "Veredicto"], fil))
    ap("\n(En negrita, las que ya están en el congelador.)\n")

    # --- Parejas
    ap("## 5. Parejas direccionales válidas\n")
    if not pares:
        ap("**Ninguna pareja válida.** Ninguna combinación cumple a la vez: "
           "diana única en el parental, dentro del MCS, ausente del inserto y "
           "con salientes incompatibles entre sí. Ve a la sección de alternativas "
           "del documento de diseño (ensamblaje Gibson/HiFi o síntesis).\n")
    else:
        fil = []
        for i, d in enumerate(pares[:12]):
            a, b = d["cinco"]["enzima"], d["tres"]["enzima"]
            fil.append([("**" if i == 0 else "") + f"{a.nombre} (5') + {b.nombre} (3')"
                        + ("**" if i == 0 else ""),
                        f"`{a.saliente_seq() or 'romo'}` / `{b.saliente_seq() or 'romo'}`",
                        "sí" if d["ambas_nevera"] else "no",
                        f"{d['separacion']} pb",
                        "; ".join(d["razones"]) or "—"])
        ap(_tabla(["Pareja (la 1.ª es la recomendada)", "Salientes",
                   "Ambas en nevera", "Separación", "Notas"], fil))
        ap("")

    # --- Primers
    if elegido and prim:
        a = elegido["cinco"]["enzima"]
        b = elegido["tres"]["enzima"]
        ap(f"## 6. Primers para {a.nombre} (5') + {b.nombre} (3')\n")
        ap("Estructura del directo: "
           f"`{proteccion}` protección + `{a.diana}` {a.nombre} + `{KOZAK}` Kozak "
           "+ ATG y siguientes bases del ORF.\n")
        ap("Estructura del reverso: "
           f"`{proteccion}` protección + `{b.diana}` {b.nombre} + "
           f"`{S.rc(STOPS_DOBLE)}` (= dos stops `{STOPS_DOBLE}` en la hebra "
           "codificante) + complementario inverso del final del ORF.\n")
        fil = [
            ["Directo", f"`{prim['fwd']}`", len(prim["fwd"]),
             f"{S.gc(prim['fwd']):.0f} %",
             f"{prim['tm_ancla_f']:.1f} °C", f"{prim['tm_total_f']:.1f} °C"],
            ["Reverso", f"`{prim['rev']}`", len(prim["rev"]),
             f"{S.gc(prim['rev']):.0f} %",
             f"{prim['tm_ancla_r']:.1f} °C", f"{prim['tm_total_r']:.1f} °C"],
        ]
        ap(_tabla(["Primer", "Secuencia 5'→3'", "nt", "GC",
                   "Tm zona de apareamiento", "Tm primer completo"], fil))
        ap("\n> Tm nearest-neighbour (SantaLucia 1998; 500 nM, 50 mM Na⁺). "
           "**Contrástalas en la calculadora de NEB con la polimerasa concreta** "
           "antes de pedir: Q5 y Phusion usan condiciones distintas.\n")
        ap(f"- Ciclado en dos tramos: **5 ciclos a Ta ≈ "
           f"{min(prim['tm_ancla_f'], prim['tm_ancla_r'])-2:.0f} °C** "
           f"(sólo aparea la zona homóloga) y después **25 ciclos a Ta ≈ "
           f"{min(prim['tm_total_f'], prim['tm_total_r'])-2:.0f} °C** "
           f"(ya aparea el primer entero).")
        h1, h2 = S.peor_horquilla(prim["fwd"]), S.peor_horquilla(prim["rev"])
        d1 = S.dimero_3p(prim["fwd"], prim["rev"])
        ap(f"- Horquilla máxima: directo {h1[0]} nt, reverso {h2[0]} nt "
           f"(≥6 nt merece revisión).")
        ap(f"- Complementariedad 3' directo↔reverso: {d1[0]} nt "
           f"{'(`'+d1[1]+'`)' if d1[0] else ''} (≥5 nt merece revisión).")
        # Kozak
        ctx = KOZAK + cds[:4]
        ap(f"- Contexto Kozak resultante: `{ctx}` → posición −3 = "
           f"`{ctx[3]}` (purina: correcto), posición +4 = `{cds[3]}`"
           + ("" if cds[3] == "G" else " (no es G; **no lo fuerces**: cambiaría "
              "el segundo aminoácido. Es un Kozak adecuado, no óptimo)."))
        ap("")

        # Producto y construcción
        amplicon = prim["producto"]
        inserto_digerido_len = len(amplicon) - 2 * len(proteccion)
        ap("### Tamaños esperados\n")
        fil = [
            ["Amplicón de PCR", f"{len(amplicon)} pb"],
            ["Inserto tras la doble digestión (aprox.)",
             f"~{inserto_digerido_len} pb"],
            ["CDS + 2 stops", f"{len(cds)+6} pb"],
        ]
        if mapa.get("region"):
            venta = (ventana[1] - ventana[0]) % n if ventana else 0
            fil.append(["Minicírculo estimado",
                        f"~{mapa['region_len'] - venta + inserto_digerido_len} pb"])
        elif modo == "mcs":
            fil.append(["Minicírculo estimado",
                        "no calculable sin el mapa completo del parental"])
        ap(_tabla(["Elemento", "Tamaño"], fil))
        ap("")

        # Metilación
        avisos = _avisos_metilacion(amplicon, [a, b])
        ap("### Metilación Dam/Dcm\n")
        if avisos:
            for x in avisos:
                ap(f"- ⚠️ {x}")
        else:
            ap(f"- Sin conflictos Dam/Dcm en el contexto de `{a.nombre}` ni de "
               f"`{b.nombre}` dentro del amplicón.")
        ap("")

        # Digestión diagnóstica
        ap("### Digestión diagnóstica del clon final\n")
        if modo == "mcs":
            ap("- No calculable en modo MCS suelto: hace falta el plásmido entero "
               "para contar las dianas del esqueleto. Con `--aceptor` se calcula.")
            sitios_restantes = []
            for f in filas:
                e = f["enzima"]
                for pmcs in f["en_ventana"]:
                    lado = ("5' del inserto" if pmcs < elegido["cinco"]["en_ventana"][0]
                            else ("3' del inserto"
                                  if pmcs > elegido["tres"]["en_ventana"][0] else None))
                    if lado:
                        sitios_restantes.append((e.nombre, lado))
            if sitios_restantes:
                ap("- Dianas del MCS que **sobreviven** en la construcción final "
                   "(las que quedan entre las dos usadas se pierden): "
                   + ", ".join(f"`{n}` ({l})" for n, l in sitios_restantes)
                   + ". Alguna de ellas, si es única en el parental, te sirve de "
                     "enzima de linearización para el diagnóstico.")
            ap("")
        contiene = mapa.get("contiene")
        region = mapa.get("region")
        for e in ([] if modo == "mcs" else
                  (POR_NOMBRE["PmeI"], POR_NOMBRE["AsiSI"])):
            pos_ac = S.busca_ambas(aceptor.seq, e.diana, True)
            dentro = [p for p in pos_ac if region and contiene(region, p)]
            fuera = [p for p in pos_ac if p not in dentro]
            ni = len(S.busca_ambas(amplicon, e.diana, False))
            total_mc = len(dentro) + ni
            total_par = len(pos_ac) + ni
            txt = (f"- `{e.nombre}` ({e.diana}): {len(pos_ac)} en el parental "
                   f"({len(dentro)} dentro de la región att, {len(fuera)} en el "
                   f"esqueleto) + {ni} en el inserto. ")
            if total_par == 1:
                txt += "→ **lineariza el plásmido recombinante**: control de tamaño limpio. "
            elif total_par == 0:
                txt += "→ no corta: no sirve como diagnóstico. "
            else:
                txt += f"→ {total_par} bandas en el recombinante. "
            if total_mc == 1:
                txt += "**Y lineariza también el minicírculo** (útil para el QC posterior)."
            elif total_mc == 0:
                txt += "No corta el minicírculo."
            else:
                txt += f"En el minicírculo daría {total_mc} bandas."
            ap(txt)
        if modo != "mcs":
            vect_len = len(aceptor) - ((ventana[1] - ventana[0]) % n if ventana else 0)
            ap(f"- La doble digestión `{a.nombre}` + `{b.nombre}` debe liberar el "
               f"inserto de ~{inserto_digerido_len} pb y dejar el vector de "
               f"~{vect_len} pb.")
        else:
            ap(f"- La doble digestión `{a.nombre}` + `{b.nombre}` debe liberar el "
               f"inserto de ~{inserto_digerido_len} pb.")
        hueco = elegido["separacion"]
        if hueco < 50:
            ap(f"- ⚠️ **Las dos dianas distan sólo {hueco} pb.** La doble "
               f"digestión libera un fragmento de ~{hueco} pb, invisible en gel: "
               f"no podrás distinguir en el gel un vector cortado dos veces de "
               f"uno cortado una sola vez. Consecuencias prácticas: (1) digiere "
               f"generosamente (≥2 h, exceso de enzima), (2) **desfosforila el "
               f"vector** — aquí la fosfatasa sí aporta, porque el fondo viene "
               f"del vector cortado una sola vez que se recirculariza, y (3) monta "
               f"siempre una ligación control sin inserto.")
        ap("")

    ap("---\n")
    ap("Generado sin conexión a bases de datos externas: contrasta los puntos "
       "marcados con ⚠️ antes de pedir oligos.")
    return "\n".join(L)


# ===========================================================================
# Autotest: construye un donante y un aceptor sintéticos y recorre el flujo
# ===========================================================================
def _seq_pseudoaleatoria(n: int, semilla: int, gc_obj: float = 0.5) -> str:
    import random
    r = random.Random(semilla)
    bases = "GC" if gc_obj > 0.5 else "AT"
    return "".join(r.choice("ACGT") for _ in range(n))


def _donante_sintetico() -> str:
    """pCMV6-Entry simulado: SgfI-ORF(sin stop)-MluI-Myc-DDK-stop."""
    import random
    r = random.Random(7)
    # ORF de 1755 pb sin stops internos, con cola rica en Gly al final.
    codones = [c for c, aa in S.CODIGO.items() if aa != "*"]
    cuerpo = "".join(r.choice(codones) for _ in range(500))
    cola_gly = "".join(r.choice(["GGC", "GGT", "GGA", "TCC", "TCT"])
                       for _ in range(83))
    cds = "ATG" + "TCTGTCCGCTAT" + cuerpo + cola_gly
    cds = cds[:1752]                       # 584 aa, sin stop
    myc = "GAACAAAAACTCATCTCAGAAGAGGATCTG"          # EQKLISEEDL
    ddk = "GATTACAAGGATGACGACGATAAG"                # DYKDDDDK
    relleno5 = _seq_pseudoaleatoria(900, 1)
    relleno3 = _seq_pseudoaleatoria(2600, 2)
    seq = (relleno5 + "GCGATCGCC" + cds + "ACGCGT" + myc + ddk + "TAA"
           + relleno3)
    seq = seq.replace("GCTAGC", "GCTAGA").replace("CTCGAG", "CTCGAC")
    # (se eliminan NheI/XhoI del relleno para que el ejemplo sea limpio)
    return (">pCMV6-KRT10_SIMULADO solo para autotest\n"
            + "\n".join(seq[i:i + 70] for i in range(0, len(seq), 70)) + "\n")


def _aceptor_sintetico() -> str:
    """pMC.EF1a-MCS-SV40polyA simulado, con anotaciones."""
    attB = MOTIVOS["attB_phiC31_min"]
    attP = MOTIVOS["attP_phiC31_min"]
    isce = MOTIVOS["I-SceI"]
    prom = _seq_pseudoaleatoria(1180, 11).replace("ATG", "ATA")
    mcs = "GAATTC" + "GCTAGC" + "GGATCC" + "CTCGAG" + "GTCGAC" + "GCGGCCGC"
    polya = _seq_pseudoaleatoria(135, 12).replace("ATG", "ATA")
    esqueleto = _seq_pseudoaleatoria(2200, 13)
    for d in ("GCTAGC", "GGATCC", "CTCGAG", "GAATTC", "GTCGAC", "GCGGCCGC",
              "GTTTAAAC", "GCGATCGC"):
        prom = prom.replace(d, "AGAGAG"[:len(d)] + "A" * (len(d) - 6))
        polya = polya.replace(d, "AGAGAG"[:len(d)] + "A" * (len(d) - 6))
        esqueleto = esqueleto.replace(d, "AGAGAG"[:len(d)] + "A" * (len(d) - 6))
    esqueleto = "GTTTAAAC" + esqueleto            # un PmeI único en el esqueleto

    partes = [("attB", attB), ("prom", prom), ("mcs", mcs), ("polya", polya),
              ("attP", attP), ("isce", isce), ("esq", esqueleto)]
    seq, coord = "", {}
    for nombre, s in partes:
        coord[nombre] = (len(seq), len(seq) + len(s))
        seq += s

    def loc(k):
        a, b = coord[k]
        return f"{a+1}..{b}"

    cab = [
        f"LOCUS       pMC_EF1a_MCS_SV40pA_SIM {len(seq)} bp DNA circular SYN",
        "DEFINITION  Simulacion de pMC.EF1a-MCS-SV40polyA para el autotest.",
        "FEATURES             Location/Qualifiers",
        f"     misc_recomb     {loc('attB')}",
        '                     /label="attB"',
        f"     promoter        {loc('prom')}",
        '                     /label="EF1alpha promoter"',
        f"     misc_feature    {loc('mcs')}",
        '                     /label="MCS"',
        f"     polyA_signal    {loc('polya')}",
        '                     /label="SV40 polyA"',
        f"     misc_recomb     {loc('attP')}",
        '                     /label="attP"',
        f"     misc_feature    {loc('isce')}",
        '                     /label="I-SceI site"',
        "ORIGIN",
    ]
    cuerpo = []
    for i in range(0, len(seq), 60):
        tramo = seq[i:i + 60].lower()
        bloques = " ".join(tramo[j:j + 10] for j in range(0, len(tramo), 10))
        cuerpo.append(f"{i+1:>9} {bloques}")
    return "\n".join(cab + cuerpo + ["//", ""])


def autotest() -> int:
    import tempfile
    fallos = []
    with tempfile.TemporaryDirectory() as td:
        pd = os.path.join(td, "donante.fa")
        pa = os.path.join(td, "aceptor.gb")
        open(pd, "w").write(_donante_sintetico())
        open(pa, "w").write(_aceptor_sintetico())

        don, ac = lee(pd), lee(pa)
        orf = encuentra_orf(don)
        mapa = mapea_aceptor(ac)
        vent = ventana_mcs(ac, mapa)
        filas = analiza_enzimas(ac, mapa, vent, orf["cds"], TODAS)
        pares = parejas(filas, vent)

        def check(nombre, cond, detalle=""):
            print(f"  [{'ok ' if cond else 'FALLO'}] {nombre}"
                  + (f"  ({detalle})" if detalle and not cond else ""))
            if not cond:
                fallos.append(nombre)

        print("Autotest de disena_clonaje.py\n")
        check("se lee el GenBank con sus rasgos", len(ac.rasgos) == 6,
              f"{len(ac.rasgos)} rasgos")
        check("attB y attP localizados", bool(mapa["attB"] and mapa["attP"]))
        check("I-SceI localizado", bool(mapa["isceI"]))
        check("región attB-attP acotada", mapa.get("region") is not None)
        check("ventana MCS acotada", vent is not None)
        check("el ORF largo incluye la etiqueta",
              len(orf["prot_completa"]) > 584, f"{len(orf['prot_completa'])} aa")
        check("recorte de la etiqueta aplicado", orf["recorte"]["aplicado"],
              orf["recorte"]["motivo"])
        check("el corte cae en el sitio de lanzadera MluI",
              orf["recorte"]["sitio"] == "MluI", orf["recorte"]["sitio"])
        check("recorte 5' aplicado (ATG en fase río arriba)",
              orf["recorte5"]["aplicado"], orf["recorte5"]["motivo"])
        check("el ATG real se ancla al sitio SgfI/AsiSI",
              orf["recorte5"]["sitio"] in ("SgfI", "AsiSI"),
              orf["recorte5"]["sitio"])
        check("CDS recortado a 584 aa", len(orf["proteina"]) == 584,
              f"{len(orf['proteina'])} aa")
        check("el CDS empieza por la Met real",
              orf["proteina"].startswith("MSVRY"), orf["proteina"][:8])
        check("etiqueta Myc detectada",
              any(e[0] == "Myc" for e in orf["etiquetas_detectadas"]))
        check("etiqueta DDK/FLAG detectada",
              any(e[0].startswith("DDK") for e in orf["etiquetas_detectadas"]))
        check("sin stop interno", "*" not in orf["proteina"])

        por = {f["enzima"].nombre: f for f in filas}
        check("NheI-HF sale usable", por["NheI-HF"]["veredicto"] == "usable",
              por["NheI-HF"]["motivo"])
        check("XhoI sale usable", por["XhoI"]["veredicto"] == "usable",
              por["XhoI"]["motivo"])
        check("PmeI descartada (fuera de la región att)",
              por["PmeI"]["veredicto"] == "no")
        check("BclI descartada por Dam", por["BclI"]["veredicto"] == "no")
        check("hay parejas direccionales", len(pares) > 0, f"{len(pares)}")

        nheI_xhoI = any({d["cinco"]["enzima"].nombre, d["tres"]["enzima"].nombre}
                        == {"NheI-HF", "XhoI"} for d in pares)
        check("NheI-HF + XhoI entre las parejas", nheI_xhoI)
        check("no se proponen parejas con salientes iguales",
              all(d["cinco"]["enzima"].saliente_seq() !=
                  d["tres"]["enzima"].saliente_seq() for d in pares))

        if pares:
            el = pares[0]
            pr = construye_primers(orf["cds"], el["cinco"]["enzima"],
                                   el["tres"]["enzima"])
            amp = pr["producto"]
            check("el amplicón empieza por el primer directo",
                  amp.startswith(pr["fwd"]))
            check("el amplicón termina en el reverso",
                  amp.endswith(S.rc(pr["rev"])))
            check("el CDS viaja íntegro", orf["cds"] in amp)
            ini = amp.index("ATG")
            prot = S.traduce(amp[ini:])
            check("un único stop, justo al final del ORF",
                  prot.index("*") == len(orf["proteina"]),
                  f"stop en {prot.index('*')}, ORF {len(orf['proteina'])}")
            check("la etiqueta Myc-DDK NO viaja",
                  "GAACAAAAACTCATCTCAGAAGAGGATCTG" not in amp)
            check("Tm de las zonas de apareamiento emparejadas (<5 °C)",
                  abs(pr["tm_ancla_f"] - pr["tm_ancla_r"]) < 5,
                  f"{pr['tm_ancla_f']:.1f} vs {pr['tm_ancla_r']:.1f}")
            txt = informe(don, ac, orf, mapa, vent, filas, pares, el, pr,
                          PROTECCION_DEF)
            check("el informe se genera", len(txt) > 2000, f"{len(txt)} car.")
            check("el informe no deja marcadores sin rellenar",
                  "{" not in txt and "None" not in txt)

        # --- Modo MCS suelto, con el MCS real del pMC.EF1a-MCS-SV40polyA ---
        print("\n  · modo --mcs (MCS real del parental)")
        mcs_real = S.limpia("tctagagctagcgaattcgaatttaaatcggatccgcggccgcgtcga")
        ac2 = Registro("MCS", mcs_real, False, [], "(--mcs)")
        mapa2 = {"attB": [], "attP": [], "isceI": [], "promotor": [],
                 "polya": [], "avisos": [], "region": None, "contiene": None}
        vent2 = (0, len(mcs_real))
        cds_limpio = ("ATG" + "GCTGGTACCTTAGGCACTACC" * 80)
        cds_limpio = cds_limpio[:len(cds_limpio) // 3 * 3]
        filas2 = analiza_enzimas(ac2, mapa2, vent2, cds_limpio, TODAS, modo="mcs")
        pares2 = parejas(filas2, vent2)
        por2 = {f["enzima"].nombre: f for f in filas2}

        check("XhoI NO está en este MCS",
              por2["XhoI"]["veredicto"] == "no" and not por2["XhoI"]["en_ventana"])
        check("AsiSI y PmeI tampoco están",
              not por2["AsiSI"]["en_ventana"] and not por2["PmeI"]["en_ventana"])
        for nom in ("XbaI", "NheI-HF", "BamHI-HF"):
            check(f"{nom} sí está en el MCS", bool(por2[nom]["en_ventana"]))
        check("NotI y EcoRI localizadas en el MCS",
              bool(por2["NotI"]["en_ventana"]) and bool(por2["EcoRI"]["en_ventana"]))
        check("la pareja recomendada es NheI-HF (5') + BamHI-HF (3')",
              pares2 and pares2[0]["cinco"]["enzima"].nombre == "NheI-HF"
              and pares2[0]["tres"]["enzima"].nombre == "BamHI-HF",
              f"{pares2[0]['cinco']['enzima'].nombre}+{pares2[0]['tres']['enzima'].nombre}"
              if pares2 else "ninguna")
        check("XbaI+BamHI queda por detrás (riesgo Dam)",
              any("Dam" in " ".join(d["razones"]) for d in pares2
                  if d["cinco"]["enzima"].nombre == "XbaI"))
        check("nunca se empareja NheI con XbaI (mismo saliente CTAG)",
              not any({d["cinco"]["enzima"].nombre, d["tres"]["enzima"].nombre}
                      == {"NheI-HF", "XbaI"} for d in pares2))
        check("sin ATG espurios en el MCS", not S.busca(mcs_real, "ATG"))
        pr2 = construye_primers(cds_limpio, pares2[0]["cinco"]["enzima"],
                                pares2[0]["tres"]["enzima"])
        check("el directo lleva NheI + Kozak + ATG",
              pr2["fwd"].startswith(PROTECCION_DEF + "GCTAGC" + KOZAK + "ATG"))
        check("el reverso lleva BamHI + los dos stops",
              pr2["rev"].startswith(PROTECCION_DEF + "GGATCC" + S.rc(STOPS_DOBLE)))
        txt2 = informe(don, ac2, orf, mapa2, vent2, filas2, pares2, pares2[0],
                       pr2, PROTECCION_DEF, modo="mcs")
        check("el informe avisa de lo que no puede comprobar",
              "Modo MCS suelto" in txt2 and "attB" in txt2)
        check("detecta la diana SalI truncada al final",
              "SalI" in txt2 and "truncada" in txt2.lower()
              or "cortadas por la mitad" in txt2)

    print()
    if fallos:
        print(f"{len(fallos)} FALLO(S): " + ", ".join(fallos))
        return 1
    print("Todas las comprobaciones pasan.")
    return 0


# ===========================================================================
def main() -> int:
    p = argparse.ArgumentParser(
        description="Diseño de clonaje de un cDNA en un vector parental de minicírculo.",
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent("""
        Ejemplo:
          python3 disena_clonaje.py \\
              --donante ../secuencias/pCMV6-KRT10.gb \\
              --aceptor ../secuencias/pMC.EF1a-MCS-SV40polyA.gb \\
              --salida ../diseno/informe_KRT10.md
        """))
    p.add_argument("--donante", help="FASTA/GenBank del plásmido donante")
    p.add_argument("--aceptor", help="FASTA/GenBank del vector parental")
    p.add_argument("--mcs", default=None,
                   help="secuencia del MCS (o ruta a un fichero con ella). "
                        "Con --aceptor, acota la ventana de clonaje. Sin él, "
                        "trabaja sólo con el MCS y avisa de lo que no puede "
                        "comprobar")
    p.add_argument("--gen", default=None, help="filtra el CDS por este nombre")
    p.add_argument("--fin-orf", type=int, default=None, dest="fin_orf",
                   help="posición 1-based del último nt del ORF nativo en el "
                        "donante (fuerza el recorte a mano)")
    p.add_argument("--inicio-orf", type=int, default=None, dest="inicio_orf",
                   help="posición 1-based del A del ATG real en el donante")
    p.add_argument("--sin-recorte", action="store_true",
                   help="no recortar aunque se detecte una etiqueta fusionada")
    p.add_argument("--pareja", default=None,
                   help="fuerza una pareja, p. ej. 'NheI-HF,XhoI'")
    p.add_argument("--proteccion", default=PROTECCION_DEF,
                   help=f"bases de protección 5' (por defecto {PROTECCION_DEF})")
    p.add_argument("--tm", type=float, default=62.0, help="Tm objetivo de la zona de apareamiento")
    p.add_argument("--sin-kozak", action="store_true",
                   help="no añadir GCCACC delante del ATG")
    p.add_argument("--salida", default=None, help="fichero .md de salida")
    p.add_argument("--autotest", action="store_true",
                   help="ejecuta las comprobaciones internas y sale")
    a = p.parse_args()

    if a.autotest:
        return autotest()
    if not a.donante or not (a.aceptor or a.mcs):
        p.error("hacen falta --donante y (--aceptor o --mcs), o bien --autotest")

    don = lee(a.donante)
    orf = encuentra_orf(don, gen=a.gen, fin_orf=a.fin_orf,
                        inicio_orf=a.inicio_orf,
                        recortar=not a.sin_recorte)

    mcs_seq = None
    if a.mcs:
        mcs_seq = S.limpia(open(a.mcs, encoding="utf-8").read()
                           if os.path.exists(a.mcs) else a.mcs)
        malas = set(mcs_seq) - set("ACGTN")
        if malas:
            p.error(f"la secuencia del MCS tiene bases no reconocidas: "
                    f"{sorted(malas)[:8]}")
        if len(mcs_seq) < 10:
            p.error("la secuencia del MCS es demasiado corta")

    if a.aceptor:
        modo = "vector"
        ac = lee(a.aceptor)
        mapa = mapea_aceptor(ac)
        vent = ventana_mcs(ac, mapa)
        if mcs_seq:
            golpes = S.busca(ac.seq, mcs_seq, ac.circular)
            golpes_rc = S.busca(ac.seq, S.rc(mcs_seq), ac.circular)
            if len(golpes) == 1:
                vent = (golpes[0], golpes[0] + len(mcs_seq))
                mapa["avisos"].append(
                    "La ventana de clonaje se ha acotado con el MCS que has pasado "
                    f"(posición {golpes[0]+1}).")
            elif len(golpes_rc) == 1:
                vent = (golpes_rc[0], golpes_rc[0] + len(mcs_seq))
                mapa["avisos"].append(
                    "El MCS que has pasado aparece en el aceptor en la hebra "
                    "CONTRARIA. Se ha usado para acotar la ventana, pero "
                    "**comprueba la orientación**: el sitio 5' del inserto es el "
                    "que queda más cerca del promotor EF1alfa, que con esta "
                    "orientación es el del final de tu cadena, no el del principio.")
            else:
                mapa["avisos"].append(
                    f"El MCS que has pasado no aparece exactamente una vez en el "
                    f"aceptor ({len(golpes)} en directa, {len(golpes_rc)} en "
                    f"inversa): se ignora y se usa la ventana promotor-polyA.")
    else:
        modo = "mcs"
        ac = Registro("MCS_suelto", mcs_seq, False, [], "(--mcs)")
        mapa = {"attB": [], "attP": [], "isceI": [], "promotor": [], "polya": [],
                "avisos": ["Sin GenBank del parental: unicidad en el plásmido "
                           "entero y contención en attB-attP SIN COMPROBAR."],
                "region": None, "contiene": None}
        vent = (0, len(mcs_seq))

    filas = analiza_enzimas(ac, mapa, vent, orf["cds"], TODAS, modo=modo)
    pares = parejas(filas, vent)

    elegido = None
    if a.pareja:
        quiero = {x.strip() for x in a.pareja.split(",")}
        for d in pares:
            if {d["cinco"]["enzima"].nombre, d["tres"]["enzima"].nombre} == quiero:
                elegido = d
                break
        if elegido is None:
            print(f"AVISO: la pareja {a.pareja} no es válida según el análisis; "
                  f"se usa la mejor disponible.", file=sys.stderr)
    if elegido is None and pares:
        elegido = pares[0]

    prim = construye_primers(
        orf["cds"], elegido["cinco"]["enzima"], elegido["tres"]["enzima"],
        proteccion=a.proteccion, tm_obj=a.tm, kozak=not a.sin_kozak) \
        if elegido else None

    txt = informe(don, ac, orf, mapa, vent, filas, pares, elegido, prim,
                  a.proteccion, modo=modo)
    if a.salida:
        os.makedirs(os.path.dirname(os.path.abspath(a.salida)), exist_ok=True)
        open(a.salida, "w", encoding="utf-8").write(txt)
        print(f"Informe escrito en {a.salida}")
    else:
        print(txt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
