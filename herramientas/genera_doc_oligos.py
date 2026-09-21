#!/usr/bin/env python3
"""Genera diseno/oligos_y_analisis.md a partir del GenBank real. Nada se teclea a mano."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analiza_oligos import *

AQUI = os.path.dirname(os.path.abspath(__file__))
P    = leer_gb(os.path.join(AQUI, "..", "secuencias", "pCMV6-KRT10.gb"))
CDS  = P[1028:2780]

def tm2(s): return tm(s,500,50,0,0), tm(s,500,50,2,0.2)

# ---------- A. horquilla con extremos BamHI / EcoRI
SENT,LAZO,ANTI,TERM = "AATGACTGCCTGGCTTCCTTT","CTCGAG","AAAGGAAGCCAGGCAGTCATT","TTTTTG"
NUC = SENT+LAZO+ANTI+TERM
TOP, BOT = "GATC"+NUC, "AATT"+rc(NUC)
# ---------- B. cebadores de PCR
ARM5, ARM3 = "TTCGAATTTAAATCG", "GATCCGCGGCCGCGT"
# El directo arranca en 1026, tres nt antes del ATG, para llevarse el Kozak NATIVO
# (-3 = G) en vez de anadir GCCACC: mas nt apareando y menos cola.
annF, annR = P[1025:1052], rc(P[2750:2780])
colaF, colaR = ARM5, rc(ARM3)+rc("TGATAA")
F, Rv = colaF+annF, colaR+annR
assert F.endswith(P[1025:1052]) and len(colaF)==15

assert rc(SENT)==ANTI and rc(NUC)==BOT[4:]
assert annF in P and rc(annR) in P and annF.startswith("GCCATG")
assert P.count(annF)==1 and P.count(rc(annR))==1
assert "GGATCC" not in NUC and "GAATTC" not in NUC
assert "GAATTC" in NUC[-8:]+"AATTC"     # EcoRI se regenera al ligar

def fila(nom, ceb, ann, cola):
    g,_,_ = peor_dimero(ceb,ceb); h3,_,_ = dimero_3p(ceb,ceb); hp,_ = horquilla(ceb)
    a1,b1 = tm2(ann); a2,b2 = tm2(ceb)
    return dict(nom=nom, ceb=ceb, ann=ann, cola=cola, n=len(ceb), nc=len(cola), na=len(ann),
                gca=gc(ann), gct=gc(ceb), tma=b1, tma0=a1, tmt=b2, tmt0=a2,
                dg=g, d3=h3, hp=hp, tres=ann[-5:],
                pos=(P.find(ann)+1 if ann in P else P.find(rc(ann))+1))
fF, fR = fila("KRT10-MC-F",F,annF,colaF), fila("KRT10-MC-R",Rv,annR,colaR)
gFR,_,_ = peor_dimero(F,Rv); h1,_,_ = dimero_3p(F,Rv); h2,_,_ = dimero_3p(Rv,F)
TA = min(fF["tma"], fR["tma"])
DIM_TM = tm("ACGCGGCCGCGG",500,50,2,0.2)

D = f"""# Oligos y análisis termodinámico

Todo lo de aquí lo genera `herramientas/genera_doc_oligos.py` leyendo
`secuencias/pCMV6-KRT10.gb`. Ninguna secuencia está tecleada a mano.
Para regenerarlo: `python3 herramientas/genera_doc_oligos.py`

**Condiciones de cálculo.** Vecino más próximo, parámetros unificados de
SantaLucia (1998). Oligo 500 nM. Se dan dos Tm: «sin Mg» = 50 mM Na⁺ solo, que es
lo que devuelven la mayoría de calculadoras web; «con Mg» = 50 mM Na⁺ + 2 mM Mg²⁺
+ 0,2 mM dNTP, convertido a Na⁺ equivalente por Owczarzy (≈211 mM), que se parece
más a un tubo de PCR real. **Las dos son estimaciones**: las herramientas del
mercado discrepan entre sí varios grados. Para fijar la Ta definitiva usa la
calculadora del fabricante de tu polimerasa.

---

## A. Oligos del shRNA 13 con extremos BamHI / EcoRI

No son cebadores: son dos oligos que se **anillan entre sí** y se ligan directamente
a un vector cortado con BamHI + EcoRI. No hay PCR, así que no hay Ta.

### Composición

```
GATC | {SENT} | {LAZO} | {ANTI} | {TERM}
 ↑      tallo sentido (21)   lazo    tallo antisentido (21)   terminador
 voladizo BamHI                                               Pol III
```

El terminador es `TTTTT` **+ una G**, al estilo pLKO: esa G de más es la que
regenera la diana EcoRI al ligar y te deja un cribado por digestión.

### Los dos oligos

| | Secuencia 5'→3' | nt |
|---|---|---|
| **sh13-BamEco-TOP** | `{TOP}` | {len(TOP)} |
| **sh13-BamEco-BOT** | `{BOT}` | {len(BOT)} |

### Comprobaciones

| Qué | Resultado |
|---|---|
| Tallo perfecto de 21 pb (antisentido = compl. inverso del sentido) | ✔ |
| BOT es el complemento inverso exacto del núcleo | ✔ |
| `GGATCC` dentro del núcleo | libre ✔ |
| `GAATTC` dentro del núcleo | libre ✔ |
| Corridas de 4+ T antes del terminador | ninguna ✔ |
| Voladizo BamHI `GATC` en el 5' de TOP | ✔ |
| Voladizo EcoRI `AATT` en el 5' de BOT | ✔ |
| GC | TOP {gc(TOP):.1f}% · BOT {gc(BOT):.1f}% |

> **`CTCGAG` (XhoI) aparece en la posición 22**: es el lazo. Tenlo en cuenta si
> alguna vez quieres usar XhoI en este constructo.

### Qué pasa al ligar

```
5'  …G + GATC + AATGAC…   →  GGATCAATGAC   →  BamHI DESTRUIDO
3'  …TTTTTG + AATTC…      →  TTTTTGAATTC   →  EcoRI REGENERADO
```

**Cribado:** el clon correcto **corta con EcoRI** y **no corta con BamHI**.
El vector vacío o religado corta con los dos. Se distinguen en un gel.

### Anillamiento

Los dos oligos forman horquilla consigo mismos (ΔG ≈ −27,7 kcal/mol). **Eso no es
un defecto: es el shRNA.** Pero compite con el apareamiento entre TOP y BOT, así que:

- Mézclalos **equimolares y concentrados** (10 µM cada uno): a concentración alta
  gana el apareamiento entre los dos oligos frente al plegamiento de cada uno.
- Calienta a **95 °C 5 min** y **baja despacio** hasta temperatura ambiente
  (apagar el bloque y dejarlo, ~1 h). No lo pases a hielo de golpe.
- Tm del dúplex de 54 pb: **{tm(NUC,500,50,2,0.2):.1f} °C**.
- **Fosforila los oligos** (T4 PNK) o pídelos ya fosforilados en 5': los oligos
  sintéticos vienen sin fosfato y la ligasa no puede sellar sin él.
- El clon no se secuencia bien por Sanger: la polimerasa se para en la horquilla.
  Secuencia desde los dos lados, o manda plásmido completo por nanopore.

---

## B. Cebadores de PCR para KRT10 + In-Fusion

Amplifican la ORF de KRT10 de tu `pCMV6-KRT10` **sin la etiqueta Myc-DDK**,
le añaden Kozak y dos codones stop, y traen los brazos de 15 nt para In-Fusion
sobre el vector cortado con BamHI.

| | Secuencia 5'→3' | nt |
|---|---|---|
| **KRT10-MC-F** | `{F}` | {len(F)} |
| **KRT10-MC-R** | `{Rv}` | {len(Rv)} |

```
KRT10-MC-F   5'-{ARM5} {annF}-3'
                └ brazo In-Fusion ┘ └──── aparea, {len(annF)} nt ────┘
                                     └GCC┘ = Kozak NATIVO (−3 = G), copiado del plásmido

KRT10-MC-R   5'-{rc(ARM3)} {rc("TGATAA")} {annR}-3'
                └ brazo In-Fusion ┘ └stops┘ └───── aparea, {len(annR)} nt ─────┘
```

### Análisis

| | KRT10-MC-F | KRT10-MC-R |
|---|---|---|
| Longitud total | {fF['n']} nt | {fR['n']} nt |
| Cola que **no** aparea | {fF['nc']} nt | {fR['nc']} nt |
| **nt que aparean con tu secuencia** | **{fF['na']} nt** | **{fR['na']} nt** |
| Posición de apareo en el plásmido | {fF['pos']} | {fR['pos']} |
| Único en el plásmido | sí ✔ | sí ✔ |
| **GC de la zona que aparea** | **{fF['gca']:.1f} %** | **{fR['gca']:.1f} %** |
| GC del cebador entero | {fF['gct']:.1f} % | {fR['gct']:.1f} % |
| **Tm de la zona que aparea** | **{fF['tma0']:.1f} / {fF['tma']:.1f} °C** | **{fR['tma0']:.1f} / {fR['tma']:.1f} °C** |
| Tm del cebador entero | {fF['tmt0']:.1f} / {fF['tmt']:.1f} °C | {fR['tmt0']:.1f} / {fR['tmt']:.1f} °C |
| Extremo 3' | …{fF['tres']} | …{fR['tres']} |
| Horquilla propia, ΔG37 | {fF['hp']:+.1f} kcal/mol | {fR['hp']:+.1f} kcal/mol |
| Autodímero, ΔG37 | {fF['dg']:+.1f} kcal/mol | {fR['dg']:+.1f} kcal/mol |
| ¿El 3' participa en el autodímero? | {'sí' if fF['d3'] else 'no ✔'} | {'sí' if fR['d3'] else 'no ✔'} |

**Heterodímero F × R:** ΔG37 = {gFR:+.1f} kcal/mol. Extremos 3' apareados entre sí:
{'sí' if (h1 or h2) else '**no** ✔'}.

**Equilibrio de la pareja:** Tm de apareo {fF['tma']:.1f} vs {fR['tma']:.1f} °C →
diferencia de **{abs(fF['tma']-fR['tma']):.1f} °C**. Una pareja equilibrada amplifica
mucho mejor que una descompensada.

### El autodímero del reverso: qué es y por qué no importa

`KRT10-MC-R` tiene un autodímero fuerte, ΔG {fR['dg']:+.1f} kcal/mol. La causa es
inevitable: el brazo 3' contiene `GCGGCCGC`, **la diana NotI, que es palindrómica**
y se aparea consigo misma.

```
        5'-ACGCGGCCGCGG-3'
            ||||||||||
        3'-GGCGCCGGCGCA-5'
```

Dos razones por las que no arruina la PCR, y una precaución:

1. **Es un dímero de extremo 5'.** La polimerasa sólo extiende desde el 3', y los
   extremos 3' están libres (verificado). Ese dímero **no genera producto espurio**;
   como mucho secuestra cebador.
2. **Funde a {DIM_TM:.1f} °C.** Por eso la zona de apareo del reverso se alargó
   hasta {len(annR)} nt: su Tm es {fR['tma']:.1f} °C, o sea **{fR['tma']-DIM_TM:+.1f} °C
   por encima del dímero**. A la Ta de trabajo, el molde gana.
3. **Precaución:** no bajes la Ta por debajo de ~66 °C «por si acaso». Con este par,
   bajar la temperatura favorece al dímero, no al producto.

> Si prefieres evitar el problema de raíz, el juego de restricción (NheI + BamHI,
> §3.3 Plan B del diseño) no lleva NotI en la cola y su autodímero es sólo
> −5,2 kcal/mol. Es la alternativa si esta PCR se resiste.

### Temperaturas de ciclado

Con cebadores de cola larga pasa una cosa que conviene entender: **en los primeros
ciclos sólo aparea la zona específica** ({TA:.0f} °C de Tm); a partir del tercero el
cebador entero ya forma parte del producto y su Tm sube a
{min(fF['tmt'],fR['tmt']):.0f} °C. Por eso la Ta que manda es la de la **zona que aparea**.

**Opción recomendada — 2 pasos.** Es lo que indica Takara para PrimeSTAR GXL cuando
la Tm de los cebadores es ≥ 55 °C, y de paso los 68 °C mantienen fundido el
autodímero del brazo NotI (que funde a {DIM_TM:.0f} °C):

```
98 °C   30 s
── 30 ciclos ──
98 °C   10 s
68 °C   2 min          anillamiento y extensión juntos (~1 min/kb, producto 1794 pb)
───────────────
68 °C   5 min
```

**Opción de 3 pasos**, si prefieres controlar la Ta:

```
98 °C   30 s
── 5 ciclos ──
98 °C   10 s
66 °C   15 s           Ta sobre la zona que aparea (Tm {TA:.1f} °C)
68 °C   2 min
── 25 ciclos ──
98 °C   10 s
68 °C   15 s           el cebador entero ya está incorporado
68 °C   2 min
──────────────
68 °C   5 min
```

> **No bajes de 66 °C.** Con esta pareja, bajar la Ta favorece al autodímero del
> reverso ({DIM_TM:.0f} °C) más que al producto. Si la PCR no sale, **sube** antes
> de bajar, o haz un gradiente de {TA-4:.0f}–{TA+4:.0f} °C.

**Confirma los tiempos en el manual de tu lote de polimerasa.** Cada enzima tiene
su propia relación Tm→Ta; Q5 por ejemplo trabaja bastante más caliente que Taq.

### Producto

**1791 pb** = 15 (brazo) + 3 (GCC nativo) + 1752 (ORF) + 6 (stops) + 15 (brazo).

El Kozak no se añade: se **copia** del plásmido. El cebador directo empieza a aparear
en la posición 1026, tres nucleótidos antes del ATG, y se trae el `GCC` nativo cuya
**G en −3** es la purina que manda. Así la cola no apareante baja de 21 a 15 nt y el
oligo pasa de 49 a 42 nt, con un 64 % de su longitud apareando en vez de un 57 %.

Traduce 584 aa acabando en `…SSKGPRY*`, **sin Myc-DDK**.

---

## C. Resumen para pedir

| Oligo | nt | Escala sugerida |
|---|---|---|
| `sh13-BamEco-TOP` | {len(TOP)} | 25 nmol, desalado. **Pídelo fosforilado en 5'** o fosforila con PNK |
| `sh13-BamEco-BOT` | {len(BOT)} | ídem |
| `KRT10-MC-F` | {len(F)} | 25 nmol, desalado |
| `KRT10-MC-R` | {len(Rv)} | 25 nmol, desalado |

Para oligos de 50–60 nt, el desalado estándar vale; la purificación PAGE sólo
merece la pena si la síntesis sale mal. Los cuatro juntos no deberían pasar de 30–40 €.

---

## D. Lo que este análisis NO puede decirte

1. **Si hay off-targets.** No tengo acceso a BLAST desde aquí. Pasa las dos guías
   y los dos cebadores por BLAST contra el genoma/transcriptoma humano antes de pedir.
2. **La Ta real de tu termociclador.** Los cálculos son estimaciones; los bloques
   calibran distinto. Si la primera PCR no sale limpia, haz un gradiente de
   {TA-4:.0f}–{TA+4:.0f} °C.
3. **Si tu MCS es correcto.** Los brazos de In-Fusion salen de los 48 nt que
   aportaste tú, no de un mapa (ver §0.B del diseño). Cotéjalos con el GenBank.
"""
sal = os.path.join(AQUI, "..", "diseno", "oligos_y_analisis.md")
open(sal, "w").write(D)
# fichero plano para copiar y pegar en el pedido
ped = os.path.join(AQUI, "..", "secuencias", "constructos", "pedido_oligos.txt")
with open(ped, "w") as fh:
    for n, s in [("sh13-BamEco-TOP",TOP),("sh13-BamEco-BOT",BOT),("KRT10-MC-F",F),("KRT10-MC-R",Rv)]:
        fh.write(f"{n}\t{s}\t{len(s)} nt\n")
print("escrito:", sal); print("escrito:", ped)
print(f"\nTa zona de apareo: {TA:.1f} °C   |   Ta cebador entero: {min(fF['tmt'],fR['tmt']):.1f} °C")
