"""Tabla de enzimas de restricción usada por el diseñador.

corte = nº de bases desde el inicio de la diana hasta el corte en la hebra
superior. saliente > 0  -> extremo 5' cohesivo de esa longitud
          saliente < 0  -> extremo 3' cohesivo
          saliente == 0 -> romo
dam / dcm: "no" | "solapante" | "siempre"  (sensibilidad conocida NEB)
nevera: True si está en el congelador del laboratorio (lista NEB fechada)
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Enzima:
    nombre: str
    diana: str
    corte: int
    saliente: int
    dam: str = "no"
    dcm: str = "no"
    nevera: bool = False
    ref: str = ""
    nota: str = ""

    def saliente_seq(self) -> str:
        """Secuencia del saliente generado, leída 5'->3' en la hebra que lo lleva."""
        if self.saliente > 0:
            return self.diana[self.corte:self.corte + self.saliente]
        if self.saliente < 0:
            n = -self.saliente
            return self.diana[self.corte - n:self.corte]
        return ""

    def tipo_extremo(self) -> str:
        if self.saliente > 0:
            return f"5' {self.saliente} nt ({self.saliente_seq()})"
        if self.saliente < 0:
            return f"3' {-self.saliente} nt ({self.saliente_seq()})"
        return "romo"


# --- En el congelador (NEB, con referencia) --------------------------------
PANEL_NEVERA = [
    Enzima("NheI-HF",  "GCTAGC",   1,  4, nevera=True, ref="R3131S"),
    Enzima("BamHI-HF", "GGATCC",   1,  4, nevera=True, ref="R3136S",
           nota="la diana contiene GATC pero NO la bloquea Dam"),
    Enzima("XhoI",     "CTCGAG",   1,  4, nevera=True, ref="R0146S"),
    Enzima("AsiSI",    "GCGATCGC", 5, -2, nevera=True, ref="R0630S",
           nota="isoesquizómero de SgfI; contiene GATC pero NO la bloquea Dam; "
                "sí la bloquea la metilación CpG (irrelevante en E. coli)"),
    Enzima("XbaI",     "TCTAGA",   1,  4, dam="solapante", nevera=True, ref="R0145S",
           nota="bloqueada por Dam si el sitio queda como GATCTAGA o TCTAGATC"),
    Enzima("PmeI",     "GTTTAAAC", 4,  0, nevera=True, ref="R0560S"),
]

# --- Enzimas habituales de MCS que habría que comprar ----------------------
PANEL_EXTRA = [
    Enzima("SgfI",    "GCGATCGC", 5, -2, nota="isoesquizómero de AsiSI (usa AsiSI)"),
    Enzima("MluI",    "ACGCGT",   1,  4),
    Enzima("EcoRI",   "GAATTC",   1,  4),
    Enzima("EcoRV",   "GATATC",   3,  0),
    Enzima("HindIII", "AAGCTT",   1,  4),
    Enzima("NotI",    "GCGGCCGC", 2,  4),
    Enzima("SalI",    "GTCGAC",   1,  4),
    Enzima("KpnI",    "GGTACC",   5, -4),
    Enzima("SacI",    "GAGCTC",   5, -4),
    Enzima("SpeI",    "ACTAGT",   1,  4),
    Enzima("BglII",   "AGATCT",   1,  4),
    Enzima("BclI",    "TGATCA",   1,  4, dam="siempre",
           nota="inservible salvo en cepa dam-"),
    Enzima("ClaI",    "ATCGAT",   2,  2, dam="solapante"),
    Enzima("NruI",    "TCGCGA",   3,  0, dam="solapante"),
    Enzima("SwaI",    "ATTTAAAT", 4,  0),
    Enzima("PacI",    "TTAATTAA", 5, -4),
    Enzima("AscI",    "GGCGCGCC", 2,  4),
    Enzima("FseI",    "GGCCGGCC", 6, -4),
    Enzima("SbfI",    "CCTGCAGG", 6, -4),
    Enzima("PstI",    "CTGCAG",   5, -4),
    Enzima("NsiI",    "ATGCAT",   5, -4),
    Enzima("SmaI",    "CCCGGG",   3,  0),
    Enzima("XmaI",    "CCCGGG",   1,  4),
    Enzima("ApaI",    "GGGCCC",   5, -4, dcm="solapante"),
    Enzima("StuI",    "AGGCCT",   3,  0, dcm="solapante"),
    Enzima("NdeI",    "CATATG",   2,  2),
    Enzima("AgeI",    "ACCGGT",   1,  4),
    Enzima("BspEI",   "TCCGGA",   1,  4),
    Enzima("BsiWI",   "CGTACG",   1,  4),
    Enzima("BstBI",   "TTCGAA",   2,  2),
    Enzima("SnaBI",   "TACGTA",   3,  0),
    Enzima("AflII",   "CTTAAG",   1,  4),
    Enzima("BsrGI",   "TGTACA",   1,  4),
    Enzima("MfeI",    "CAATTG",   1,  4),
    Enzima("PvuI",    "CGATCG",   4, -2),
    Enzima("SphI",    "GCATGC",   5, -4),
    Enzima("NcoI",    "CCATGG",   1,  4),
    Enzima("PvuII",   "CAGCTG",   3,  0),
]

TODAS = PANEL_NEVERA + PANEL_EXTRA
POR_NOMBRE = {e.nombre: e for e in TODAS}

# Motivos de referencia del sistema de minicírculos y de etiquetas.
MOTIVOS = {
    "I-SceI": "TAGGGATAACAGGGTAAT",
    "attB_phiC31_nucleo": "GGCTTGTCGACGACGGCGGTCTCCGTCGTCAGGATCAT",
    "attB_phiC31_min": "GTGCCAGGGCGTGCCCTTGGGCTCCCCGGGCGCG",
    "attP_phiC31_min": "GTAGTGCCCCAACTGGGGTAACCTTTGAGTTCTCTCAGTTGGGGG",
    "TTG_nucleo_att": "TTG",
}

# Péptidos que delatan una etiqueta en el donante (se buscan traducidos).
ETIQUETAS_PEPTIDO = {
    "Myc": "EQKLISEEDL",
    "DDK/FLAG": "DYKDDDDK",
    "HA": "YPYDVPDYA",
    "His6": "HHHHHH",
    "V5": "GKPIPNPLLGLDST",
}
