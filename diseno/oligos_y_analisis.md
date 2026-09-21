# Oligos y análisis termodinámico

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
GATC | AATGACTGCCTGGCTTCCTTT | CTCGAG | AAAGGAAGCCAGGCAGTCATT | TTTTTG
 ↑      tallo sentido (21)   lazo    tallo antisentido (21)   terminador
 voladizo BamHI                                               Pol III
```

El terminador es `TTTTT` **+ una G**, al estilo pLKO: esa G de más es la que
regenera la diana EcoRI al ligar y te deja un cribado por digestión.

### Los dos oligos

| | Secuencia 5'→3' | nt |
|---|---|---|
| **sh13-BamEco-TOP** | `GATCAATGACTGCCTGGCTTCCTTTCTCGAGAAAGGAAGCCAGGCAGTCATTTTTTTG` | 58 |
| **sh13-BamEco-BOT** | `AATTCAAAAAAATGACTGCCTGGCTTCCTTTCTCGAGAAAGGAAGCCAGGCAGTCATT` | 58 |

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
| GC | TOP 46.6% · BOT 43.1% |

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
- Tm del dúplex de 54 pb: **79.7 °C**.
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
| **KRT10-MC-F** | `TTCGAATTTAAATCGGCCATGTCTGTTCGATACAGCTCAAGC` | 42 |
| **KRT10-MC-R** | `ACGCGGCCGCGGATCTTATCAGTATCTTGGTCCCTTAGATGAAGACTCGCC` | 51 |

```
KRT10-MC-F   5'-TTCGAATTTAAATCG GCCATGTCTGTTCGATACAGCTCAAGC-3'
                └ brazo In-Fusion ┘ └──── aparea, 27 nt ────┘
                                     └GCC┘ = Kozak NATIVO (−3 = G), copiado del plásmido

KRT10-MC-R   5'-ACGCGGCCGCGGATC TTATCA GTATCTTGGTCCCTTAGATGAAGACTCGCC-3'
                └ brazo In-Fusion ┘ └stops┘ └───── aparea, 30 nt ─────┘
```

### Análisis

| | KRT10-MC-F | KRT10-MC-R |
|---|---|---|
| Longitud total | 42 nt | 51 nt |
| Cola que **no** aparea | 15 nt | 21 nt |
| **nt que aparean con tu secuencia** | **27 nt** | **30 nt** |
| Posición de apareo en el plásmido | 1026 | 2751 |
| Único en el plásmido | sí ✔ | sí ✔ |
| **GC de la zona que aparea** | **51.9 %** | **50.0 %** |
| GC del cebador entero | 42.9 % | 54.9 % |
| **Tm de la zona que aparea** | **62.5 / 69.8 °C** | **62.2 / 69.7 °C** |
| Tm del cebador entero | 67.1 / 74.7 °C | 73.8 / 81.6 °C |
| Extremo 3' | …CAAGC | …TCGCC |
| Horquilla propia, ΔG37 | -3.7 kcal/mol | -2.5 kcal/mol |
| Autodímero, ΔG37 | -7.4 kcal/mol | -17.1 kcal/mol |
| ¿El 3' participa en el autodímero? | no ✔ | no ✔ |

**Heterodímero F × R:** ΔG37 = -6.1 kcal/mol. Extremos 3' apareados entre sí:
**no** ✔.

**Equilibrio de la pareja:** Tm de apareo 69.8 vs 69.7 °C →
diferencia de **0.2 °C**. Una pareja equilibrada amplifica
mucho mejor que una descompensada.

### El autodímero del reverso: qué es y por qué no importa

`KRT10-MC-R` tiene un autodímero fuerte, ΔG -17.1 kcal/mol. La causa es
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
2. **Funde a 65.4 °C.** Por eso la zona de apareo del reverso se alargó
   hasta 30 nt: su Tm es 69.7 °C, o sea **+4.3 °C
   por encima del dímero**. A la Ta de trabajo, el molde gana.
3. **Precaución:** no bajes la Ta por debajo de ~66 °C «por si acaso». Con este par,
   bajar la temperatura favorece al dímero, no al producto.

> Si prefieres evitar el problema de raíz, el juego de restricción (NheI + BamHI,
> §3.3 Plan B del diseño) no lleva NotI en la cola y su autodímero es sólo
> −5,2 kcal/mol. Es la alternativa si esta PCR se resiste.

### Temperaturas de ciclado

Con cebadores de cola larga pasa una cosa que conviene entender: **en los primeros
ciclos sólo aparea la zona específica** (70 °C de Tm); a partir del tercero el
cebador entero ya forma parte del producto y su Tm sube a
75 °C. Por eso la Ta que manda es la de la **zona que aparea**.

**Opción recomendada — 2 pasos.** Es lo que indica Takara para PrimeSTAR GXL cuando
la Tm de los cebadores es ≥ 55 °C, y de paso los 68 °C mantienen fundido el
autodímero del brazo NotI (que funde a 65 °C):

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
66 °C   15 s           Ta sobre la zona que aparea (Tm 69.7 °C)
68 °C   2 min
── 25 ciclos ──
98 °C   10 s
68 °C   15 s           el cebador entero ya está incorporado
68 °C   2 min
──────────────
68 °C   5 min
```

> **No bajes de 66 °C.** Con esta pareja, bajar la Ta favorece al autodímero del
> reverso (65 °C) más que al producto. Si la PCR no sale, **sube** antes
> de bajar, o haz un gradiente de 66–74 °C.

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
| `sh13-BamEco-TOP` | 58 | 25 nmol, desalado. **Pídelo fosforilado en 5'** o fosforila con PNK |
| `sh13-BamEco-BOT` | 58 | ídem |
| `KRT10-MC-F` | 42 | 25 nmol, desalado |
| `KRT10-MC-R` | 51 | 25 nmol, desalado |

Para oligos de 50–60 nt, el desalado estándar vale; la purificación PAGE sólo
merece la pena si la síntesis sale mal. Los cuatro juntos no deberían pasar de 30–40 €.

---

## D. Lo que este análisis NO puede decirte

1. **Si hay off-targets.** No tengo acceso a BLAST desde aquí. Pasa las dos guías
   y los dos cebadores por BLAST contra el genoma/transcriptoma humano antes de pedir.
2. **La Ta real de tu termociclador.** Los cálculos son estimaciones; los bloques
   calibran distinto. Si la primera PCR no sale limpia, haz un gradiente de
   66–74 °C.
3. **Si tu MCS es correcto.** Los brazos de In-Fusion salen de los 48 nt que
   aportaste tú, no de un mapa (ver §0.B del diseño). Cotéjalos con el GenBank.
