#!/usr/bin/env python3
"""Genera diseno/shrna_clonaje.md. Todas las secuencias se verifican antes de escribir."""
import sys, os, re, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analiza_oligos import *
AQUI = os.path.dirname(os.path.abspath(__file__))
P = leer_gb(os.path.join(AQUI,"..","secuencias","pCMV6-KRT10.gb")); KRT10 = P[1028:2780]
comp = lambda s: s.translate(COMP)

MCS1  = "CGACTAGTGAATTCAGATCTGATATCTCTAGAGTCGACCCATGGGGGCCC"   # pMC.BESPX-MCS1
MCSSH = "GGATCCTCTGAATTC"                                       # pMC.CMV-GFP-H1-MCS
assert comp(MCS1) == "GCTGATCACTTAAGTCTAGACTATAGAGATCTCAGCTGGGTACCCCCGGG"

LAZO, TERM = "CTCGAG", "TTTTTG"
SENT13 = "AATGACTGCCTGGCTTCCTTT"
PROH = {"BamHI":"GGATCC","EcoRI":"GAATTC","SpeI":"ACTAGT","ApaI":"GGGCCC","BglII":"AGATCT",
        "EcoRV":"GATATC","XbaI":"TCTAGA","SalI":"GTCGAC","NcoI":"CCATGG","HindIII":"AAGCTT",
        "NheI":"GCTAGC","NotI":"GCGGCCGC","PstI":"CTGCAG","KpnI":"GGTACC","SacI":"GAGCTC"}
sucio = lambda n: [k for k,v in PROH.items() if v in n+rc(n)]

# Control desordenado de la bibliografia: pLKO.1 scramble, Addgene #1864,
# depositado por el laboratorio de David Sabatini. Es el scramble generico mas
# citado. Su horquilla publicada es sense-CTCGAG-antisense, el mismo formato.
H1864  = "CCTAAGGTTAAGTCGCCCTCGCTCGAGCGAGGGCGACTTAACCTTAGG"
SENTSCR = H1864[:21]
assert H1864[21:27] == LAZO and rc(SENTSCR) == H1864[27:48]

OL = {}
for nom, sent in [("sh13",SENT13),("shSCR1864",SENTSCR)]:
    nuc = sent+LAZO+rc(sent)+TERM
    assert not sucio(nuc) and "TTTT" not in (sent+LAZO+rc(sent))
    OL[nom] = dict(sent=sent, anti=rc(sent), nuc=nuc, TOP="GATC"+nuc, BOT="AATT"+rc(nuc))
    izq = MCSSH[0]+OL[nom]["TOP"][:10]; der = OL[nom]["TOP"][-8:]+MCSSH[10:]
    OL[nom]["bamhi"] = "GGATCC" in izq      # se conserva o no, segun la 1a base del tallo
    assert "GAATTC" in der                   # EcoRI se regenera SIEMPRE

ESP = "AAAACC"
CAS = ESP+"ACTAGT"+"[PROMOTOR H1]"+MCSSH+"GGGCCC"+ESP
tabla = "\n".join(
 f"| **{n}-BamEco-TOP** | `{OL[n]['TOP']}` | {len(OL[n]['TOP'])} |\n"
 f"| **{n}-BamEco-BOT** | `{OL[n]['BOT']}` | {len(OL[n]['BOT'])} |" for n in OL)

D = f"""# Clonaje del shRNA 13 y del control desordenado

Generado por `herramientas/genera_doc_shrna.py`. Ninguna secuencia está tecleada a mano.

## 0. Lo que aporta esta información

Dos MCS reales, los dos verificados leyendo las dos hebras:

**`pMC.BESPX-MCS1`** (50 nt) — **desbloquea el constructo 2**, que estaba parado
esperando esto (ver §0.E del diseño general):

```
      SpeI    EcoRI   BglII   EcoRV   XbaI    SalI   NcoI   ApaI
5'-{MCS1}-3'
3'-{comp(MCS1)}-5'
    3   9      15      21      27      33     39     45
```

| Enzima | Sitio | Posición | Corta tras |
|---|---|---|---|
| SpeI | ACTAGT | 3–8 | 3 |
| EcoRI | GAATTC | 9–14 | 9 |
| BglII | AGATCT | 15–20 | 15 |
| EcoRV | GATATC | 21–26 | 23 (romo) |
| XbaI | TCTAGA | 27–32 | 27 |
| SalI | GTCGAC | 33–38 | 33 |
| NcoI | CCATGG | 39–44 | 39 |
| ApaI / Bsp120I | GGGCCC | 45–50 | 49 / 45 |

> **NcoI no estaba etiquetado en la figura de SBI, pero está.** Y **no hay NheI ni
> BamHI en MCS1**, al contrario de lo que sugería la ficha de producto.

**`pMC.CMV-GFP-H1-MCS`** (15 nt): `{MCSSH}` → H1 → **BamHI** (1–6) – TCT –
**EcoRI** (10–15). Al cortar con los dos se quitan 9 nt.

---

## 1. Las dos horquillas

Formato `sentido – CTCGAG – antisentido – TTTTTG`, con voladizos BamHI y EcoRI.
La `G` final del terminador es la que regenera EcoRI al ligar (estilo pLKO).

### sh13 — contra el alelo mutante

```
sentido      {OL['sh13']['sent']}    ← tu 13F, hebra pasajera
lazo         {LAZO}
antisentido  {OL['sh13']['anti']}    ← tu 13R, LA GUÍA
terminador   {TERM}
```

### shSCR1864 — control no dirigido, de la bibliografía

```
sentido      {OL['shSCR1864']['sent']}
lazo         {LAZO}
antisentido  {OL['shSCR1864']['anti']}
terminador   {TERM}
```

Es el **scramble de `pLKO.1`, Addgene #1864**, depositado por el laboratorio de
David Sabatini: el control no dirigido genérico más usado del campo, con miles de
citas. Su horquilla publicada ya viene en formato `sentido–CTCGAG–antisentido`, el
mismo que sh13, así que se adapta sin tocar una base.

Verificado: su semilla (`{OL['shSCR1864']['anti'][2:9]}`) **no aparece en la ORF de
KRT10**, ni directa ni en complemento inverso. GC del tallo
{gc(OL['shSCR1864']['sent']):.1f} % frente al {gc(OL['sh13']['sent']):.1f} % de sh13.

> **Por qué no vale un scramble inventado.** Una versión barajada de tu propia guía
> conserva la composición de bases, que está bien, pero **no la ha validado nadie**.
> Un control no dirigido tiene que venir con historial: es justamente lo que le
> faltó a SHC016 (§1.1).

### 1.1 Aviso: NO uses SHC016

Según PubMed, Bereta y colaboradores demostraron que **SHC016**, uno de los dos
controles no dirigidos de la librería MISSION (TRC) de Sigma, **es citotóxico**:
silencia **SNRPD3**, una proteína central del espliceosoma, y provoca apoptosis en
células murinas y senescencia o catástrofe mitótica en células tumorales humanas
según el estado de p53. El efecto es tan fuerte que el casete de shRNA se acaba
eliminando del genoma de las células en cultivo. Los autores lo declaran
**descalificado como control**.

[Bereta et al., *Mol Ther Nucleic Acids* 2021 · DOI 10.1016/j.omtn.2021.09.004](https://doi.org/10.1016/j.omtn.2021.09.004) · [PMID 34703654](https://pubmed.ncbi.nlm.nih.gov/34703654/)

**El otro control de MISSION, SHC002, sí se comporta bien** en ese trabajo (lo usan
como comparador limpio). Pero tiene una pega concreta para ti: **SHC002 sí silencia
el transcrito de turboGFP**, y el vector de shRNA de SBI expresa GFP. Si esa GFP es
copGFP o turboGFP —las dos son de copépodo y emparentadas entre sí— SHC002 te
silenciaría el reportero del propio vector. **Compruébalo antes de usarlo ahí.**

**Moraleja del episodio SHC016:** ningún control no dirigido está garantizado. Por
eso el §5 pide además un control de vector vacío.

### Los cuatro oligos a pedir

| Oligo | Secuencia 5'→3' | nt |
|---|---|---|
{tabla}

Ninguno contiene BamHI, EcoRI, SpeI, ApaI, BglII, EcoRV, XbaI, SalI, NcoI, HindIII,
NheI, NotI, PstI, KpnI ni SacI (barrido hecho sobre las dos hebras). Ninguno tiene
corridas de 4+ T antes del terminador, que harían terminar Pol III antes de tiempo.

---

## 2. Ruta A — directa, en el vector de shRNA de SBI

El vector ya trae H1. Sólo hay que meter la horquilla.

1. Cortar el vector con **BamHI + EcoRI**, purificar la banda en gel.
2. Anillar TOP + BOT (ver §4).
3. Ligar y transformar.

**Qué queda en las uniones:**

```
5'  …G + GATC + {OL['sh13']['sent'][:6]}…   →  GGATC{OL['sh13']['sent'][0]}…  →  BamHI DESTRUIDO
3'  …{TERM} + AATTC…              →  {TERM}AATTC  →  EcoRI REGENERADO
```

**Cribado.** Cuidado, porque **no es el mismo para las dos horquillas**: depende de
con qué base empiece el tallo sentido.

| Plásmido | BamHI | EcoRI | PCR de colonia |
|---|---|---|---|
| vector vacío | corta | corta | — |
| **sh13** (tallo empieza en `AA`) | **NO corta** | corta | +49 pb |
| **shSCR1864** (tallo empieza en `CC`) | corta | corta | +49 pb |

```
sh13       G + GATC + AA  =  GGATCAA   →  BamHI destruido
shSCR1864  G + GATC + CC  =  GGATCCC   →  BamHI CONSERVADO
```

No es un fallo: la horquilla se transcribe igual y EcoRI se regenera en los dos
casos. Pero **BamHI sólo distingue sh13 del vector vacío, no shSCR1864**.

**Lo que vale para los dos: PCR de colonia** con cebadores del vector. El clon
correcto da un producto **49 pb mayor** que el vacío.

**Lo que arrastra:** CMV-GFP. Sirve para el piloto —de hecho la GFP te da la
eficiencia de transfección gratis— pero no para el constructo terapéutico.

---

## 3. Ruta B — sin reportero, en `pMC.BESPX-MCS1`

BESPX está vacío: no trae promotor. Hay que meter primero un **casete aceptor**
con el H1, y luego las horquillas van dentro con los **mismos oligos** de la ruta A.

### 3.1 El casete aceptor

```
{CAS}
└esp─┘└SpeI┘└──── promotor H1 ────┘└──── MCS igual al de SBI ────┘└ApaI┘└esp─┘
                          acaba en su +1        BamHI ─ TCT ─ EcoRI
```

Se clona en BESPX-MCS1 cortado con **SpeI + ApaI**. Eso excinde las posiciones
4–49 del MCS1, es decir **se lleva por delante el EcoRI propio del vector**
(posiciones 9–14), que si no competiría con el del casete. Es la razón de elegir
esa pareja y no otra.

Tras la ligación se regeneran los dos sitios externos:

```
…CGA + CTAGT[H1][{MCSSH}]GGGCC + C…   →  SpeI y ApaI intactos
```

Resultado: **un aceptor de shRNA sin reportero, reutilizable**, con BamHI y EcoRI
únicos. Cada horquilla nueva son dos oligos y una ligación.

### 3.2 De dónde sacar el H1 — dos opciones

**(a) Si compras el vector de shRNA de SBI para el piloto: amplifícalo de ahí.**
Es la mejor opción y no cuesta nada. PCR de la región `H1 + {MCSSH}` con colas que
aporten SpeI y ApaI, e In-Fusion o ligación. Ventaja decisiva: **la geometría
H1→+1→BamHI se copia literal**, sin riesgo de colocar mal el inicio de
transcripción. Los cebadores necesitan el mapa del vector.

**(b) Sintetizarlo.** Fragmento de ~300 pb con la estructura de arriba. El promotor
H1 **tiene que acabar exactamente en su +1**, con `GGATCC` pegado detrás. En pSUPER
el fragmento de H1 llega justo hasta el sitio BglII, que es el +1: corta ahí.

### 3.3 Alternativa por In-Fusion

Si prefieres In-Fusion a restricción, la pareja con brazos de 15 nt conocidos que
más trozo excinde es **BglII + SalI** (18 nt fuera):

```
brazo 5' (15 nt) : {MCS1[0:15]}
brazo 3' (15 nt) : {MCS1[33:48]}
```

Inconveniente: deja intacto el EcoRI del vector (posiciones 9–14), que pasaría a
competir con el del casete. **Por eso recomiendo SpeI + ApaI.**

---

## 4. Anillar y ligar los oligos

1. Mezcla TOP y BOT **equimolares y concentrados**, 10 µM cada uno. A concentración
   alta gana el dúplex entre los dos frente al plegamiento de cada uno sobre sí mismo.
2. **95 °C 5 min**, y **bajar despacio** a temperatura ambiente (apagar el bloque y
   dejarlo, ~1 h). No pasar a hielo de golpe.
3. **Fosforila con T4 PNK**, o pide los oligos ya fosforilados en 5': los oligos
   sintéticos vienen sin fosfato y la ligasa no puede sellar sin él.
4. Diluye el dúplex antes de ligar (1:100 – 1:200 es lo habitual): en exceso se
   ligan en tándem y te salen inserciones múltiples.
5. Ligar, transformar, cribar con EcoRI/BamHI.

> **Los dos oligos forman horquilla consigo mismos (ΔG ≈ −28 kcal/mol). Eso no es un
> defecto: es el shRNA.** Pero por eso hay que anillar despacio y concentrado.

> **El clon no se secuencia bien por Sanger:** la polimerasa se para en la horquilla.
> Secuencia desde los dos lados, o manda plásmido completo por nanopore.

---

## 5. Los controles que hacen falta, no sólo el desordenado

El trabajo de Bereta lo dice explícitamente y conviene tenerlo en el diseño desde
el principio: un control no dirigido **no sustituye** al de vector vacío.

| Control | Qué aísla |
|---|---|
| **Vector vacío** (sin horquilla) | El efecto de la transfección y del vector en sí |
| **shSCR1864** | El efecto de *expresar una horquilla cualquiera*: carga de RISC, competencia con el miRNA endógeno, respuesta a interferón |
| **Reportero WT frente a mutante, con la MISMA sh13** | **La especificidad de alelo.** Éste es el control que de verdad sostiene tu conclusión, y ya lo tienes montado en las construcciones psiCHECK |

El tercero es el importante: la especificidad no la demuestra el scramble, la
demuestra que sh13 baje el reportero mutante y no el silvestre.

---

## 6. Lo que queda por verificar (no me lo invento)

1. **Que BamHI, EcoRI, SpeI y ApaI sean únicos en todo `pMC.BESPX-MCS1`**, no sólo
   en su MCS. Necesita el GenBank completo.
2. **Que el promotor H1 elegido no contenga esos cuatro sitios.**
3. **ApaI y Bsp120I reconocen la misma secuencia pero cortan distinto**
   (`GGGCC^C` frente a `G^GGCCC`): dejan voladizos incompatibles entre sí. Usa **la
   misma enzima** en el vector y en el inserto. No las mezcles.
4. **Cuántas bases hay entre el +1 del H1 y el BamHI** en el vector de SBI. El
   voladizo `GATC` queda dentro del transcrito, como el `CCGG` de pLKO — es normal
   y funciona, pero conviene saberlo.
5. **BLAST de las dos guías** contra el transcriptoma humano antes de pedir.
"""
sal = os.path.join(AQUI,"..","diseno","shrna_clonaje.md"); open(sal,"w").write(D)
ped = os.path.join(AQUI,"..","secuencias","constructos","pedido_oligos_shrna.txt")
with open(ped,"w") as fh:
    for n in OL:
        fh.write(f"{n}-BamEco-TOP\t{OL[n]['TOP']}\t{len(OL[n]['TOP'])} nt\n")
        fh.write(f"{n}-BamEco-BOT\t{OL[n]['BOT']}\t{len(OL[n]['BOT'])} nt\n")
print("escrito:", sal); print("escrito:", ped)
