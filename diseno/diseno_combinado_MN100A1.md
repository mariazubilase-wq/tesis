# Diseño de clonaje — constructo combinado en `pMC.BESPX-MCS1` (MN100A-1)

**Constructo 3 de los tres previstos: reemplazo + silenciamiento en un solo
minicírculo.**

Documento de estrategia. **No está cerrado**: falta el GenBank completo de
MN100A-1 (ver §7). Lo que sí está cerrado es la decisión biológica de §1, que es
la que de verdad condiciona el constructo.

---

## 1. Lo primero, porque lo demás depende de esto

> ## ⚠️ El cDNA de KRT10 del constructo 1 **no sirve tal cual** para el combinado.
> ## Hay que hacerlo resistente a sh13 antes, y ahora ya sabemos exactamente cómo.

El razonamiento, que es corto:

- sh13 es **alelo-específico**: su guía es complementaria al alelo **mutante**
  (`...AATGAC**T**GCCTGGCTTCCTTT...`, con el `TGC` de R156C).
- Frente al alelo **silvestre** (`CGC`) la guía tiene **un único
  desapareamiento**, y está en la **posición 15** — no en la 10–11, que es donde
  discrimina de verdad (el detalle está en `diseno_sh13_pSI_H1.md` §2.1).
- El transgén de reemplazo **es silvestre**. O sea: **es exactamente el molde
  que sh13 reconoce con un solo desapareamiento mal colocado.**

Traducción al banco: si metes los dos casetes juntos sin tocar el cDNA, **el
shRNA se va a comer también tu copia de reemplazo**, que es justo lo contrario de
lo que el constructo pretende. Y lo peor es que el experimento *parecerá*
funcionar en el western de K10 total: baja el mutante y baja el silvestre, y el
resultado neto es que no has reemplazado nada.

Esto es lo que tu §4.2 pedía y lo que el §3.5 del documento de KRT10 aplazó
diciendo «todavía no sabéis qué shRNA gana». **Para sh13 ya se puede cerrar.**

### 1.1 Los cambios *wobble*, concretos

La ventana diana en el cDNA **silvestre** es:

```
      N154 D155 R156 L157 A158 S159 F160
      AAT  GAC  CGC  CTG  GCT  TCC  TTT
pos    1-3  4-6  7-9 10-12 13-15 16-18 19-21
```

Las terceras bases disponibles (las que se pueden cambiar sin tocar la proteína)
son las posiciones 3, 6, 12, 15, 18 y 21. Traducidas a posición **en la guía**
(que es `21 − n + 1`), dan 19, 16, **10**, **7**, 4 y 1.

La posición 12 del sentido cae en la **10 de la guía**: el punto de corte de
Ago2, el mejor sitio posible. Así que:

| Codón | Silvestre | Resistente | Aminoácido | Posición en el sentido | Posición en la guía |
|---|---|---|---|---|---|
| **L157** | `CTG` | **`CTC`** | Leu → Leu | 12 | **10** ← el que importa |
| **A158** | `GCT` | **`GCC`** | Ala → Ala | 15 | **7** |

Ventana resistente resultante:

```
silvestre   AATGAC CGC CTG GCT TCCTTT
mutante     AATGAC TGC CTG GCT TCCTTT   ← lo que sh13 reconoce
RESISTENTE  AATGAC CGC CTC GCC TCCTTT
                    ↑     ↑   ↑
                    7    12  15        → 3 desapareamientos frente a la guía
```

**Tres desapareamientos, uno de ellos en la posición 10.** El transgén queda
fuera del alcance de sh13 y la proteína es silvestre exacta, residuo por residuo.

Comprobado además que los cambios **no crean ninguna diana nueva** de las que se
usan en este clonaje (`AATGACCGCCTCGCCTCCTTT` no contiene GGATCC, GAATTC,
GCGGCCGC, GTCGAC, ACTAGT, GATATC ni CCATGG).

### 1.2 Dos regalos que vienen con esto

1. **Resuelve la ddPCR transgén vs endógeno.** Era el problema que el §3.5 del
   documento de KRT10 intentaba arreglar cambiando el propio codón 156. Esta vía
   es mejor: **deja el codón 156 como silvestre auténtico** (`CGC`) y pone la
   firma en 157/158. Así la ddPCR alelo-específica de la posición 466 sigue
   leyendo lo que tiene que leer, y además puedes diseñar una sonda
   transgén-específica sobre `CTCGCC`.
2. **Es un fragmento sintético pequeño.** Los dos cambios están a 3 pb uno del
   otro, en el nucleótido ~470 de un CDS de ~1,75 kb. Exactamente el escenario
   que el §3.5 anticipaba: **encargar sintético sólo el fragmento que lleva los
   cambios y sustituirlo** sobre el constructo 1 ya validado, en vez de rehacer
   el clonaje entero.

> **Si al final gana otro shRNA de los 19, estos dos cambios no valen.** Los
> *wobble* se diseñan contra una diana concreta. Este diseño es para sh13. Por
> eso el orden correcto sigue siendo: validar sh13 primero (constructo 2), y
> sólo entonces encargar el fragmento resistente.

---

## 2. El vector de destino

`pMC.BESPX-MCS1` (MN100A-1) es el parental **sin promotor**. Eso es exactamente
lo que hace falta aquí: los dos casetes entran **completos, cada uno con su
propio promotor**, y el vector no aporta ninguno que pudiera interferir.

### 2.1 El MCS1, mapeado

```
         3      9      15     21     27     33     39     45
    CGACTAGTGAATTCAGATCTGATATCTCTAGAGTCGACCCATGGGGGCCC
      └SpeI─┘└EcoRI┘└BglII┘└EcoRV┘└XbaI─┘└SalI─┘└NcoI─┘└ApaI─┘
```

| Enzima | Diana | Posición | Saliente |
|---|---|---|---|
| SpeI | `A^CTAGT` | 3–8 | `CTAG` |
| EcoRI | `G^AATTC` | 9–14 | `AATT` |
| BglII | `A^GATCT` | 15–20 | `GATC` |
| EcoRV | `GAT^ATC` | 21–26 | **romo** |
| XbaI | `T^CTAGA` | 27–32 | `CTAG` |
| SalI | `G^TCGAC` | 33–38 | `TCGA` |
| **NcoI** | `C^CATGG` | 39–44 | `CATG` |
| ApaI | `GGGCC^C` | 45–50 | `GGCC` (3') |

Dos cosas que no están en la ficha del fabricante y conviene saber:

- **Hay una NcoI (39–44) que el esquema no etiqueta.** Está ahí, entre SalI y
  ApaI. Es útil: no corta ninguno de los dos casetes (§2.2).
- **SpeI y XbaI dejan el mismo saliente `CTAG`.** No se pueden usar como pareja
  direccional, igual que pasaba con XbaI/NheI en el constructo 1. Pero sí son
  compatibles con NheI y AvrII, lo cual abre opciones.
- **BglII deja `GATC`**, o sea **compatible con BamHI** — y por tanto con el
  casete H1-sh13, que va flanqueado de BamHI/BglII.

### 2.2 Cuáles de estas enzimas sirven de verdad

Comprobado contra los dos casetes reales. ⚠ = corta dentro, inservible:

| Enzima | Casete A (EF1α→SV40pA) | Casete B (H1→sh13) | ¿Utilizable? |
|---|---|---|---|
| **SpeI** | limpia | limpia | ✅ |
| EcoRI | ⚠ 1× | ⚠ 1× | ❌ |
| BglII | ⚠ 3× | ⚠ 1× | ❌ |
| **EcoRV** | limpia | limpia | ✅ |
| XbaI | ⚠ 1× | limpia | ❌ para A |
| SalI | ⚠ 1× | limpia | ❌ para A |
| **NcoI** | limpia | limpia | ✅ |
| ApaI | limpia | ⚠ 1× | ❌ para B |

**Sólo quedan tres enzimas limpias para los dos: SpeI, EcoRV y NcoI.** Y hacen
falta tres uniones (vector–B, B–A, A–vector). Con tres enzimas y tres uniones no
hay margen: cualquier imprevisto en el cDNA de KRT10 (que no he podido
comprobar) deja el plan sin salida.

> **Y el cDNA de KRT10 todavía no está comprobado.** Las columnas de arriba son
> para los casetes **sin** el cDNA. Un CDS de 1,75 kb rico en GC puede llevar
> perfectamente una SpeI o una NcoI — de hecho `CCATGG` es un motivo frecuente.
> Compruébalo en cuanto tengas el GenBank.

**Conclusión: la restricción no es la vía aquí.** Lo cual nos lleva a §3.

---

## 3. Estrategia

### Plan A — ensamblaje de 3 piezas (In-Fusion / NEBuilder HiFi) ← recomendado

Es la vía natural, y además **es la que ya estás usando**: los cebadores
`ClonK10MC_F/R` del constructo 1 son de ensamblaje por homología, no de
restricción (ver el §14 del documento de KRT10). O sea que el kit y el método ya
están en la casa.

```
   MN100A-1 linearizado (1 corte)
            │
            ├── PCR del casete B  (H1 → sh13 → TTTTT)        ~350 pb
            └── PCR del casete A  (EF1α → KRT10r → SV40pA)   ~3,4 kb
```

**Linearización: EcoRV, corte único y romo**, en el centro del MCS1. Deja SpeI,
EcoRI y BglII por delante y XbaI, SalI, NcoI y ApaI por detrás, **todas intactas
para el diagnóstico posterior**. Con ensamblaje por homología el saliente da
igual, así que la ventaja de un corte romo y central es gratis.

Cada fragmento se amplifica con colas de **15 nt** homólogas a lo que le toca al
lado, exactamente como en el constructo 1.

### Plan B — por pasos, aprovechando que el casete B es extraíble

Si la PCR del casete B da problemas (**y es probable que los dé**: un tallo de
21 pb es un molde desagradable, la polimerasa patina), hay una salida limpia que
evita amplificar la horquilla:

1. **El casete H1-sh13 sale por digestión BglII** del constructo 2 (dos dianas,
   2639 y 2988, que lo flanquean; fragmento de ~350 pb — ver
   `diseno_sh13_pSI_H1.md` §5).
2. Ese fragmento **liga directamente en la BglII del MCS1** (`GATC` con `GATC`).
3. Después se mete el casete A por ensamblaje en la EcoRV o la SpeI que quedan.

Coste: no es direccional (mismo saliente en los dos extremos), así que hay que
cribar la orientación por PCR. Ventaja: **cero PCR sobre la horquilla**.

### 3.1 La orientación de los dos casetes

Es una decisión real y hay que tomarla a conciencia:

| Disposición | Qué pasa | Veredicto |
|---|---|---|
| **Tándem, H1 primero** `→H1-sh13→ →EF1α-KRT10r→` | El terminador `TTTTT` corta la pol III; la pol II arranca limpia por detrás | ✅ **Recomendado** |
| Divergente (cabeza con cabeza) `←H1-sh13` `EF1α-KRT10r→` | Funciona, muy usado, pero interferencia leve entre promotores adyacentes | Alternativa aceptable |
| **Convergente (cola con cola)** | Las dos polimerasas chocan de frente | ❌ **Nunca** |

Recomendación: **tándem con el casete pol III por delante**. Es la disposición
clásica de los vectores duales tipo pSUPER, el terminador de la pol III es
eficiente y no hay repeticiones invertidas que inviten a recombinar.

### 3.2 La comprobación arquitectónica, que es la de siempre

**Los dos casetes tienen que caer dentro de attB–attP.** En MN100A-1 el MCS1
está ahí por diseño, así que *a priori* sí, pero hay que verlo en el mapa: el
inserto total son ~3,8 kb, y conviene confirmar que el minicírculo resultante
(~4 kb) es el que esperas. Es la restricción principal y no se da por supuesta
(§7).

---

## 4. Validación, por capas

El combinado es el único constructo donde hace falta demostrar que **las dos
mitades funcionan a la vez y no se estorban**:

| Capa | Ensayo | Qué tiene que salir |
|---|---|---|
| 1. Estructura | Secuenciación completa del inserto | Los dos casetes, en tándem, con los *wobble* |
| 2. Reemplazo solo | Transfección en célula sin el alelo mutante | K10 ectópica alta — **el shRNA no debe tocarla** |
| 3. Silenciamiento solo | ddPCR alelo-específica | Mutante abajo, WT endógeno ~igual |
| 4. Las dos juntas | Queratinocito del paciente | Mutante abajo **y** K10 total recuperada |

> **La capa 2 es la que justifica todo el §1.** Si la K10 ectópica baja en una
> célula que no tiene alelo mutante, es que los *wobble* no bastaron y el shRNA
> está atacando el transgén. Es el control que hay que hacer **antes** de meterse
> en queratinocito de paciente, y es barato.

---

## 5. Orden de trabajo

No se puede construir esto hasta que los otros dos estén validados, y el motivo
no es burocrático:

1. **Constructo 1** — valida el reemplazo (K10 ectópica, sin etiqueta, funcional).
2. **Constructo 2** — valida sh13 (y decide si sh13 gana, con el aviso de la
   posición 15 encima de la mesa).
3. **Sólo entonces:** encargar el fragmento sintético resistente (§1.1),
   sustituirlo en el constructo 1, y ensamblar el combinado.

Saltarse el paso 2 significa diseñar los *wobble* contra un shRNA que puede no
ser el elegido. Y eso ya está dicho en `diseno_clonaje_KRT10_minicirculo.md`
§3.5 — no ha cambiado.

---

## 6. Lo que NO hay que hacer

- ❌ **Meter el cDNA silvestre nativo en el combinado.** El shRNA se lo come (§1).
- ❌ Poner los casetes en convergente.
- ❌ Contar con EcoRI, BglII, XbaI, SalI o ApaI del MCS1 para el clonaje: todas
  cortan dentro de uno de los dos casetes (§2.2).
- ❌ Diseñar los *wobble* antes de saber si sh13 es el shRNA elegido.
- ❌ Dar por hecho que el MCS1 cae dentro de attB–attP sin mirar el mapa.
- ❌ Amplificar por PCR la horquilla si se puede evitar (Plan B).
- ❌ Construir en ZYCY10P3S2T.

---

## 7. Lo que necesito para cerrar este documento

Una sola cosa, y es la misma de siempre:

> **El GenBank / SnapGene completo de `pMC.BESPX-MCS1` (MN100A-1).**

El MCS1 que me has pasado está mapeado y verificado (§2.1), pero con 50 pb no se
puede comprobar lo que de verdad decide el diseño:

| Qué falta | Para qué |
|---|---|
| Posición de **attB y attP** | Confirmar que los dos casetes caen dentro del minicírculo |
| **Unicidad real** de SpeI, EcoRV y NcoI en los ~4 kb del plásmido | Ahora mismo sólo sé que son únicas *dentro del MCS1* |
| Tamaño total y posición del MCS1 | Calcular el tamaño del minicírculo final |
| Si lleva o no polyA propio por detrás del MCS1 | Decide si el casete A necesita traerse el SV40 polyA o no |

Con el `.dna` en `secuencias/` esto se resuelve en un comando:

```bash
python3 herramientas/lee_snapgene.py secuencias/pMC.BESPX-MCS1.dna --dianas
```

Y lo segundo, cuando puedas: **`secuencias/pCMV6-KRT10.gb`**, para comprobar que
el cDNA no lleva SpeI, EcoRV ni NcoI (§2.2) y para confirmar la diana de sh13
(`diseno_sh13_pSI_H1.md` §2.1).
