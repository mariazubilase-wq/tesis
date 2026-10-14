# Diseño de clonaje — sh13 en `pMC.SI-H1-MCS` (MNSI500A-1)

**Constructo 2 de los tres previstos: el minicírculo de silenciamiento.**

Verificado contra el mapa real `MNSI500A-1-pSI-H1-EcoRI-BamH1-CMV-GFP`
(SnapGene, 6877 pb, verificación Feb 2015).

---

## 0. Qué se construye, en una frase

Un dúplex de oligos sintéticos que codifica una horquilla alelo-específica
(sh13) se liga entre **BamHI y EcoRI**, inmediatamente por detrás del promotor
**H1** del vector parental, dentro de la ventana attB–attP que acaba en el
minicírculo.

No hay PCR. No hay polimerasa. Dos oligos, un hibridado, una ligación.

---

## 1. El vector, comprobado sobre el mapa

| Rasgo | Posición | Nota |
|---|---|---|
| 32 sitios I-SceI en tándem | 1..731 | se quedan en el esqueleto |
| **attB (ΦC31)** | 741..775 | **límite 5' de lo que acaba en el minicírculo** |
| CMV | 883..1232 | marcador GFP del parental |
| GFP | 1247..2005 | ídem |
| WPRE | 2012..2552 | |
| 3'dLTR | 2674..3149 | el H1 va embebido aquí (origen lentiviral) |
| **H1 (completo)** | 2712..2928 | |
| **H1 core (promotor mínimo)** | 2836..2926 | |
| **BamHI** | **2929..2934** | **única en todo el plásmido** ✔ |
| relleno | 2935..2937 (`tct`) | 3 pb que se pierden al digerir |
| **EcoRI** | **2938..2943** | **única en todo el plásmido** ✔ |
| SV40 poly(A) | 3221..3352 | |
| **attP (ΦC31)** | 3616..3654 | **límite 3'** |
| KanR | 3977..4537 | esqueleto |
| EcoE1 ori | 4840..6877 | esqueleto |

**Las dos comprobaciones que importan, y las dos salen bien:**

1. **El casete H1→shRNA (2712–2943) cae holgadamente dentro de attB–attP
   (775–3616).** Acabará en el minicírculo. Esto es la restricción
   arquitectónica principal y aquí no hay duda.
2. **BamHI y EcoRI son ambas de corte único en los 6877 pb.** Verificado:

   ```bash
   python3 lee_snapgene.py MNSI500A-1_pSI-H1.dna --dianas
   ```

   Nada de digestiones parciales ambiguas, nada de fragmentos sorpresa.

**La orientación también sale bien:** el core del H1 acaba en 2926 y BamHI
empieza en 2929. El promotor transcribe **hacia** el sitio de clonaje, así que
la hebra TOP es la que se transcribe. Es lo que hace falta.

---

## 2. Los oligos, desmontados

```
sh13_TOP (65 nt)
GATCC AATGACTGCCTGGCTTCCTTT CTTCCTGTCAGA AAAGGAAGCCAGGCAGTCATT TTTTT G
└─1─┘ └────────2──────────┘ └─────3────┘ └────────4──────────┘ └─5─┘ │
                                                                      └6

sh13_BOT (65 nt)
AATTC AAAAA AATGACTGCCTGGCTTCCTTT TCTGACAGGAAG AAAGGAAGCCAGGCAGTCATT G
└─1'┘
```

| # | Qué es | Secuencia | Longitud |
|---|---|---|---|
| 1 | Saliente BamHI | `GATC` + `C` | 4 nt romos + 1 |
| 2 | **Hebra sentido** (pasajera) | `AATGACTGCCTGGCTTCCTTT` | 21 nt |
| 3 | Bucle | `CTTCCTGTCAGA` | 12 nt |
| 4 | **Hebra antisentido** (guía) | `AAAGGAAGCCAGGCAGTCATT` | 21 nt |
| 5 | Terminador pol III | `TTTTT` | 5 nt |
| 6 | Base de cierre | `G` | pareja del `C` de BamHI |
| 1' | Saliente EcoRI | `AATT` + `C` | |

**Comprobado en silico, y las tres comprobaciones pasan:**

- `antisentido == complementaria-invertida(sentido)` → **sí**, exacto, sin
  desapareamientos internos. La horquilla cierra limpia (21 pb de tallo).
- `sh13_BOT == AATT + complementaria-invertida(sh13_TOP sin el GATCC) + G` →
  **sí**. Los dos oligos son estrictamente complementarios en los 60 nt
  centrales, con los dos salientes correctos en los extremos.
- Al ligar, **las dos dianas se regeneran**: `G`+`GATCC` = `GGATCC`, y
  `G`+`AATTC` = `GAATTC`. Esto no es accidental y conviene aprovecharlo (§5).

### 2.1 Dónde cae la mutación — leer esto antes de pedir nada

La hebra sentido traducida en pauta 1 da:

```
AAT GAC TGC CTG GCT TCC TTT
 N   D   C   L   A   S   F
```

`N-D-**C**-L-A-S` es el motivo de inicio del dominio 1A de las queratinas de
tipo I, que en silvestre es `N-D-**R**-L-A-S`. O sea: **el `TGC` de la posición
7–9 es el codón 156 mutado** (`CGC`→`TGC`, que es exactamente `c.466C>T` =
R156C). El shRNA solapa la mutación: es alelo-específico, como tiene que ser.

**Pero hay un dato que hay que mirar de frente.** El nucleótido mutado es el
**primero** del codón, o sea la **posición 7 de los 21** contando desde el 5' de
la hebra sentido. Trasladado a la guía, que es la que hace el trabajo, eso es la
**posición 15 desde su extremo 5'**:

```
guía   5'- A  A  A  G  G  A  A  G  C  C  A  G  G  C  A  G  T  C  A  T  T -3'
           1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21
                                                      ↑
                        posición 15: aquí está el desapareamiento con el alelo WT
                        (frente al WT, que lleva G en vez de A)
```

La posición que mejor discrimina alelos es la **10–11**, donde cae el corte de
Ago2. La 15 funciona en algunos casos descritos, pero es claramente peor sitio.
**Esto no es motivo para no clonarlo** —de los 19 candidatos hay que probar
varios y éste es uno— pero sí es motivo para:

- **No dar por hecha la discriminación.** El ensayo de alelo-especificidad
  (ddPCR mutante vs WT) manda, y para sh13 manda más que para uno con el
  desapareamiento en 10–11.
- **Esperar que la discriminación sea el punto débil antes que la potencia.**
  Un shRNA con el *mismatch* en 15 suele bajar bien el mutante **y también algo
  el silvestre**.

> ⚠️ **Confirmación pendiente.** La asignación de la diana a `c.466C>T` está
> deducida de la propia secuencia del oligo (el motivo `NDRLAS` del dominio 1A
> es inconfundible), **no contrastada contra el GenBank de KRT10**, que no está
> en el repositorio y al que este contenedor no tiene acceso de red. Confírmalo
> en un segundo en cuanto pongas `secuencias/pCMV6-KRT10.gb`:
>
> ```bash
> grep -o AATGACTGCCTGGCTTCCTTT <(python3 -c "...")   # o simplemente búscalo en SnapGene
> ```
>
> Búscala directamente en SnapGene (Edit → Find → `AATGACTGCCTGGCTTCCTTT`), o
> desde el repositorio:
>
> ```bash
> python3 herramientas/lee_snapgene.py secuencias/pCMV6-KRT10.dna --fasta /tmp/k10.fa
> grep -o -b AATGACTGCCTGGCTTCCTTT <(tr -d '\n' < /tmp/k10.fa)   # mutante
> grep -o -b AATGACCGCCTGGCTTCCTTT <(tr -d '\n' < /tmp/k10.fa)   # silvestre (CGC)
> ```
>
> Lo que tiene que salir: **tu clon de OriGene es silvestre**, así que la que
> debe aparecer —una sola vez— es la segunda, la de `CGC`. Si aparece la
> primera, el clon no es WT y eso cambia todo el diseño del constructo 1.
> Y la posición que devuelve `grep -b` te da de regalo la confirmación de que
> el codón afectado es el 156.

---

## 3. Protocolo

### 3.1 Hibridado de los oligos

Pide los dos oligos en escala estándar (25 nmol), **purificación por desalado es
suficiente** — son 65 nt, y para un dúplex que se liga no hace falta PAGE.

> **No pidas los oligos fosforilados en 5'.** Es el error caro de este montaje.
> Si los oligos llevan fosfato, el dúplex se liga a sí mismo en concatémeros y
> te llena la placa de clones con dos y tres horquillas en tándem. Sin fosfato,
> el único fosfato disponible es el de los extremos del vector, y **cada
> plásmido sólo puede incorporar un inserto**. El nick que queda lo repara
> *E. coli* tras la transformación.

1. Resuspende cada oligo a **100 µM** en TE (no en agua: el pH importa).
2. Mezcla en un tubo de PCR:

   | | µL |
   |---|---|
   | sh13_TOP 100 µM | 5 |
   | sh13_BOT 100 µM | 5 |
   | Tampón de hibridado 10× (100 mM Tris pH 8, 1 M NaCl, 10 mM EDTA) | 5 |
   | H₂O | 35 |
   | **Total** | **50** (10 µM de dúplex) |

3. En el termociclador: **95 °C 5 min**, después **rampa hasta 25 °C a
   −0,1 °C/s** (si el equipo no hace rampas: 95 °C 5 min en un vaso con agua y
   dejar enfriar el vaso entero en el banco, ~45 min. Funciona igual de bien).
4. Diluye 1:200 en TE → **50 nM**, que es la concentración de trabajo.

### 3.2 Digestión del vector

Una sola digestión doble; las dos enzimas son únicas.

| | µL |
|---|---|
| pSI-H1 (MNSI500A-1), 2 µg | x |
| rCutSmart 10× | 5 |
| BamHI-HF | 1 |
| EcoRI-HF | 1 |
| H₂O hasta | 50 |

**37 °C, 2 h.** Las dos son HF y las dos van en rCutSmart: un tubo, un buffer,
sin digestiones secuenciales.

> **No desfosforiles el vector.** Con salientes incompatibles (`GATC` frente a
> `AATT`) no se recirculariza solo, y si lo desfosforilas **te quedas sin los
> únicos fosfatos del montaje** —los oligos no los llevan— y la ligación no
> ocurre. Es el segundo error caro, y es silencioso: sales con cero colonias y
> sin saber por qué.

Purifica en gel: el vector cortado son ~6874 pb y el relleno que sale son 3 pb,
que no vas a ver. Un gel al 0,8 % sólo te sirve para confirmar que hay **una
sola banda** (lineal) y que no queda circular sin cortar. Si ves dos bandas,
alarga la digestión.

### 3.3 Ligación

| | Inserto | Control sin inserto |
|---|---|---|
| Vector digerido (~50 ng) | x | x |
| Dúplex 50 nM | 1 µL | — |
| T4 ligasa buffer 10× | 2 | 2 |
| T4 DNA ligasa | 1 | 1 |
| H₂O hasta | 20 | 20 |

**16 °C toda la noche**, o 25 °C 1 h si tienes prisa.

**El control sin inserto no es opcional.** Es lo que te dice si la digestión
doble funcionó. Si el control te da colonias, es que una de las dos enzimas no
cortó y el vector se está recircularizando.

### 3.4 Transformación

**En una cepa de clonaje normal (DH5α, Stbl3 si quieres ir sobre seguro con la
horquilla), NO en ZYCY10P3S2T.** La cepa productora es sólo para el paso de
inducción, al final. Construir en ella es un error que cuesta semanas.

> Las horquillas de 21 pb son estables en DH5α, pero si en la secuenciación
> aparecen deleciones recurrentes dentro del tallo, pasa a **Stbl3 a 30 °C**,
> que es el remedio clásico.

---

## 4. Cribado y validación

### 4.1 El problema de cribar un inserto de 60 pb

Un inserto de 60 pb **no se distingue en un gel** del vector vacío (6874 frente
a 6934 pb). Las PCR de colonia tampoco ayudan mucho. Las dos vías que sí
funcionan:

| Método | Qué hace | Veredicto |
|---|---|---|
| **Secuenciación directa** | Cebador sobre el H1 (o el de reverso del dLTR) | **Lo correcto.** Barato, inequívoco, y además te confirma que el tallo no tiene deleciones |
| Digestión diagnóstica | — | **No sirve aquí.** BamHI y EcoRI se regeneran al ligar, así que cortan igual en vacío y en recombinante |

**Secuencia 6–8 colonias.** Es menos trabajo que cualquier alternativa, y es la
única que detecta la deleción parcial del tallo, que es el modo de fallo real de
este constructo.

> Pide la secuenciación con un cebador que aparee **por delante del H1**, a
> ≥80 nt del inserto. La horquilla da una caída de señal clásica al llegar al
> tallo; con margen por delante la lectura entra limpia.

### 4.2 Lo que tiene que decir la secuencia

```
...H1 core... GGATCC AATGACTGCCTGGCTTCCTTT CTTCCTGTCAGA AAAGGAAGCCAGGCAGTCATT TTTTT GAATTC ...
              └BamHI┘ └──── sentido ─────┘ └── bucle ──┘ └──── antisentido ──┘ └ter┘ └EcoRI┘
```

Las tres cosas que hay que mirar, en este orden:

1. **El tallo tiene los 21 pb completos en los dos brazos.** Es lo que se pierde
   si hay recombinación.
2. **Los 5 T del terminador están.** Si quedan 4, el pol III termina mal y el
   transcrito lleva cola extra.
3. **BamHI y EcoRI están regeneradas.** Si no lo están, hay un indel en la
   unión.

---

## 5. La ventaja que hay que no tirar

**Al regenerarse BamHI y EcoRI, el casete H1→sh13 queda extraíble.** Esto no es
un detalle estético: es lo que hace barato el constructo 3.

Y hay algo mejor. En el mapa hay **dos dianas BglII que flanquean todo el casete**:

| BglII | Posición | Dónde cae |
|---|---|---|
| 1ª | 2639 | por delante del H1 (que empieza en 2712) |
| 2ª | 2988 | por detrás del EcoRI (2943) |
| 3ª | 3579 | fuera, junto a attP — **ojo, hay una tercera** |

Un corte BglII libera un fragmento de **~355 pb que contiene el H1 completo + la
horquilla + su terminador**: el casete entero, listo para mover. Como BglII deja
saliente `GATC`, **es directamente compatible con BamHI y BglII** del vector de
destino.

El pero: BglII **no es única** (hay 3 dianas), así que una digestión completa da
tres fragmentos. Se resuelve mirando el gel —los tamaños son muy distintos— y
cortando la banda de ~355 pb. Para el constructo 3 lo recomendable sigue siendo
PCR + ensamblaje (ver `diseno_combinado_MN100A1.md` §3), pero esta vía existe y
es la red de seguridad si la PCR de la horquilla da problemas (que los da: el
tallo de 21 pb es un molde desagradable).

---

## 6. Inducción del minicírculo

Idéntica al constructo 1 — ver §9 de `diseno_clonaje_KRT10_minicirculo.md`. Los
mismos controles de QC:

| Comprobación | Qué tiene que salir |
|---|---|
| PCR/qPCR del **esqueleto** (KanR u ori) | negativa o residual |
| PCR del casete H1-shRNA | positiva |
| Gel del minicírculo | banda única, muy por debajo del parental |

El minicírculo de sh13 será **pequeño** (~2,9 kb de ventana attB–attP frente a
los 6877 del parental), lo cual juega a favor en la transfección.

---

## 7. Lo que NO hay que hacer

- ❌ **Pedir los oligos fosforilados.** → concatémeros.
- ❌ **Desfosforilar el vector.** → cero ligación, sin aviso.
- ❌ **Cribar por digestión.** BamHI y EcoRI se regeneran: no distinguen.
- ❌ **Cribar por tamaño en gel.** 60 pb sobre 6874 no se ven.
- ❌ Construir en ZYCY10P3S2T.
- ❌ Dar por buena la alelo-especificidad sin el ensayo, **sobre todo con el
  desapareamiento en la posición 15** (§2.1).
- ❌ Secuenciar con un cebador que empiece a 20 nt del tallo.

---

## 8. Lo que queda por tu parte

1. Poner `MNSI500A-1_pSI-H1.dna` en `secuencias/` (no se versiona, ver
   `secuencias/LEEME.md`).
2. **Confirmar la diana de sh13 contra el cDNA de KRT10** (§2.1). Es la única
   incógnita real de este documento.
3. Pedir los dos oligos **sin fosforilar**, desalado, 25 nmol.
4. Decidir si sh13 entra en la tanda de candidatos a validar o si esperas al
   resultado de los 19 siRNA. El clonaje es barato y rápido; la decisión es
   tuya y depende de cuánto pese el aviso de la posición 15.
