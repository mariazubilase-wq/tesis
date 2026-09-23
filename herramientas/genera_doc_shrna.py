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

random.seed(20260923)
guia = rc(SENT13)
while True:
    l = list(guia[1:-2]); random.shuffle(l)
    g = guia[0]+"".join(l)+guia[-2:]; s = rc(g); nuc = s+LAZO+g+TERM
    if sucio(nuc) or "TTTT" in (s+LAZO+g): continue
    if g[2:9] in KRT10 or rc(g[2:9]) in KRT10: continue
    if abs(gc(s)-gc(SENT13)) > 5 or s == SENT13: continue
    SENTSCR = s; break

OL = {}
for nom, sent in [("sh13",SENT13),("shSCR",SENTSCR)]:
    nuc = sent+LAZO+rc(sent)+TERM
    assert not sucio(nuc) and "TTTT" not in (sent+LAZO+rc(sent))
    OL[nom] = dict(sent=sent, anti=rc(sent), nuc=nuc, TOP="GATC"+nuc, BOT="AATT"+rc(nuc))
    izq = MCSSH[0]+OL[nom]["TOP"][:8]; der = OL[nom]["TOP"][-8:]+MCSSH[10:]
    assert "GGATCC" not in izq and "GAATTC" in der

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

### shSCR — control desordenado

```
sentido      {OL['shSCR']['sent']}
lazo         {LAZO}
antisentido  {OL['shSCR']['anti']}
terminador   {TERM}
```

El control **no es una secuencia cualquiera**: es la guía de sh13 **barajada**, así
que conserva su composición de bases y su GC ({gc(OL['shSCR']['sent']):.1f} % frente a
{gc(OL['sh13']['sent']):.1f} %). Comprobado además que su semilla (`{OL['shSCR']['anti'][2:9]}`)
**no aparece en la ORF de KRT10**, ni directa ni en complemento inverso.

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

**Cribado sin secuenciar:** el clon correcto **corta con EcoRI y no con BamHI**;
el vector vacío o religado corta con los dos.

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

## 5. Lo que queda por verificar (no me lo invento)

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
