# Clonaje de shRNA (sh13 y shSCR) en pSI-H1-CMV-GFP (MNSI500A-1)

## 0. Verificación *in silico* (hecha sobre tu archivo .dna)

**Vector:** 6.877 pb, promotor H1 (2712–2928), CMV-GFP, **resistencia NeoR/KanR** (no lleva AmpR).

| Sitio | Secuencia | Posición | Nº de cortes en el plásmido |
|---|---|---|---|
| BamHI | GGATCC | 2929 | **1 (único)** |
| EcoRI | GAATTC | 2938 | **1 (único)** |

Región del policlonaje (el H1 termina justo antes del BamHI):

```
...GAGACCACTT GGATCC TCT GAATTC TTCGATTCTGC...
        H1 ↑    BamHI      EcoRI
```

La doble digestión BamHI+EcoRI sólo libera un fragmento de **9 pb** (`GATCCTCTG`).

**Oligos:** los cuatro son de 65 nt y los dos pares anillan de forma perfecta (comprobado). El dúplex resultante tiene 61 pb de doble cadena más dos extremos cohesivos:

```
sh13:
5'-GATC CAATGACTGCCTGGCTTCCTTT CTTCCTGTCAGA AAAGGAAGCCAGGCAGTCATT TTTTTG    -3'
3'-     GTTACTGACGGACCGAAGGAAA GAAGGACAGTCT TTTCCTTCGGTCCGTCAGTAA AAAAACTTAA-5'
     ↑ compatible BamHI                                                   ↑ compatible EcoRI
         sentido (21 nt)        bucle (12 nt)   antisentido (21 nt)    term. Pol III
```

- Sentido y antisentido son complementarios exactos en ambas construcciones (verificado).
- shSCR es el *scramble* clásico de MISSION/pLKO (`CCTAAGGTTAAGTCGCCCTCG`).
- Tras la ligación **se regeneran los dos sitios** (BamHI y EcoRI). Esto es útil para el cribado, pero tiene una consecuencia crítica (ver punto 1).

---

## 1. Por qué NO puedes usar tal cual tu protocolo de CRISPR

Tu protocolo (px458 / BbsI) es un **Golden Gate**: digestión y ligación simultáneas con ciclos a 37 °C/23 °C. Eso funciona porque BbsI es una enzima de tipo IIS que **corta fuera de su sitio de reconocimiento**, de modo que al ligar el inserto el sitio desaparece y el producto ya no se vuelve a cortar.

Aquí BamHI y EcoRI son de tipo II clásicas y **sus sitios se reconstruyen al ligar**. Si haces ciclos de digestión+ligación en un tubo, la enzima volverá a cortar cada producto correcto y no obtendrás nada.

**Lo que sí se conserva de tu protocolo:** el paso 1.1 de fosforilación + anillado con T4 PNK (programa "guías CRISPR"). Es perfectamente válido aquí y lo reutilizamos.
**Lo que cambia:** digestión del vector por separado → purificación en gel → ligación clásica con T4 ligasa.

---

## 2. Materiales

- Oligos a **100 µM** en agua o TE (sh13_TOP, sh13_BOT, shSCR_TOP, shSCR_BOT)
- T4 PNK + tampón de ligasa T4 10× (lleva ATP)
- **FastDigest BamHI (FD0054) y FastDigest EcoRI (FD0274)** de Thermo + 10× FastDigest Green Buffer
- T4 DNA ligasa + su tampón (alícuotas frescas: el ATP se degrada al congelar/descongelar)
- Kit de purificación en gel, agarosa, bacterias competentes (DH5α o Stbl3)
- **Kanamicina 50 µg/mL** (⚠️ no ampicilina)

---

## 3. DÍA 1 — Digestión del vector (Thermo FastDigest, 20 µL)

**Opción A — FastDigest (recomendada).** Las FastDigest son 100 % compatibles entre sí en un único tampón, así que la doble digestión va en un solo tubo. Es la línea que ya usáis en el protocolo de CRISPR.

| Componente | Volumen |
|---|---|
| **10× FastDigest Green Buffer** | 2 µL |
| pSI-H1-CMV-GFP (**1 µg**) | x µL |
| FastDigest **BamHI** (FD0054) | 1 µL |
| FastDigest **EcoRI** (FD0274) | 1 µL |
| H₂O libre de nucleasas | hasta **20 µL** |

- **37 °C, 30 min.** El protocolo estándar de Thermo son 5–15 min, pero aquí los dos sitios están separados sólo por 3 pb y necesitas corte completo por ambos, así que alarga a 30 min.
- **No pases de 1 h** ni lo dejes toda la noche: las FastDigest no están pensadas para incubaciones largas y puedes empezar a ver actividad *star*.
- El **Green Buffer ya lleva tampón de carga y densificante**, así que los 20 µL se cargan directos en el gel sin añadir nada. (Si usas el FastDigest Buffer normal, añade tu tampón de carga antes de cargar.)
- No hace falta inactivar por calor, porque el siguiente paso es purificación en gel.
- **No defosforiles** el vector. Los oligos sintéticos no llevan fosfato en 5′ si no los fosforilas; si además quitas los fosfatos del vector, no ligará nada. Como la digestión es doble y con extremos incompatibles entre sí, el religado del vector vacío ya es bajo.

> **Rendimiento:** 1 µg digerido te deja, tras purificar en gel, unos 400–600 ng (≈ 20–25 ng/µL en 25 µL). Son 8–10 ligaciones de 50 ng, de sobra para las dos construcciones. Si quieres más margen, monta **dos tubos de 20 µL** en paralelo y júntalos en el gel — es mejor que sobrecargar un solo tubo, porque por encima de 1 µg de ADN en 20 µL la digestión deja de ser completa.

**Opción B — enzimas convencionales (ER0051 / ER0271).** No hay un tampón de Thermo que dé 100 % de actividad a BamHI y EcoRI a la vez: cada una tiene el suyo (Buffer BamHI y Buffer EcoRI). Hazla **secuencial**:

1. EcoRI 1 µL + 2 µL de 10× Buffer EcoRI + 1 µg de plásmido + H₂O hasta 20 µL → 37 °C, 1–2 h.
2. Limpia en columna, eluye en 16 µL.
3. Añade 2 µL de 10× Buffer BamHI + 1 µL de BamHI + H₂O hasta 20 µL → 37 °C, 1–2 h.
4. Gel y purificación como en la opción A.

Antes de montarla, comprueba la pareja en la calculadora [DoubleDigest de Thermo](https://www.thermofisher.com/order/catalog/product/B30) por si tu lote admite Tango; si el tanto por ciento de actividad no es 100/100, quédate con la digestión secuencial.

**Purificación en gel (importante):**
1. Corre los 50 µL en gel de agarosa al 0,8 %.
2. Corta la banda de ~6,9 kb (el fragmento de 9 pb se va con el frente) y purifícala con kit.
3. Eluye en 25–30 µL y cuantifica (Nanodrop). Deberías tener ≥ 30 ng/µL.

> Control recomendado: carga en paralelo 200 ng de plásmido sin digerir. La diferencia entre superenrollado (sin cortar) y lineal te confirma que la digestión fue completa.

---

## 4. DÍA 1 — Fosforilación y anillado de los oligos

Igual que tu protocolo de CRISPR (Protocolo A). Un tubo por shRNA:

| Componente | Volumen |
|---|---|
| Oligo TOP 100 µM | 1 µL |
| Oligo BOT 100 µM | 1 µL |
| Tampón ligasa T4 10× | 1 µL |
| T4 PNK | 0,5 µL |
| H₂O | 6,5 µL |
| **Total** | **10 µL** |

Termociclador (programa "guías CRISPR"):
- 37 °C — 30 min (fosforilación)
- 95 °C — 5 min (desnaturalización)
- Rampa hasta 25 °C a **5 °C/min** (anillado)
- 4 °C ∞

**Dilución:** diluye **1:250** (2 µL + 498 µL de agua), igual que en tu protocolo. El dúplex sin diluir está en exceso enorme y provoca concatémeros (inserciones múltiples en tándem), que es el error más frecuente en este clonaje.

> Guarda el dúplex concentrado a −20 °C; aguanta meses. La dilución 1:250 prepárala fresca.

---

## 5. DÍA 1 — Ligación

Tres tubos por construcción:

| Componente | **L1** (ligación) | **L2** (control vector solo) | **L3** (control sin ligasa) |
|---|---|---|---|
| Vector digerido+purificado (50 ng) | x µL | x µL | x µL |
| Dúplex diluido 1:250 | 2 µL | — | 2 µL |
| Tampón ligasa T4 10× | 2 µL | 2 µL | 2 µL |
| T4 ligasa | 1 µL | 1 µL | — |
| H₂O | hasta 20 µL | hasta 20 µL | hasta 20 µL |

- **16 °C toda la noche** (mejor rendimiento) o **temperatura ambiente 1–2 h**.
- L2 te dice cuánto fondo tienes por vector mal cortado/religado. Si L2 da tantas colonias como L1, repite la digestión.

> El dúplex ligado no lleva fosfato en uno de los extremos de cada cadena si no fosforilaste; al haber usado PNK sí los lleva, así que la ligación es covalente en las cuatro uniones. (Si algún día se te olvida el PNK, también funciona: quedan dos mellas que repara la bacteria, sólo baja algo la eficiencia.)

---

## 6. DÍA 2 — Transformación

1. Descongela 50 µL de competentes en hielo.
2. Añade **2–5 µL** de la ligación. Mezcla con la punta, no pipetees arriba y abajo.
3. Hielo 30 min → choque térmico **42 °C 45 s** → hielo 2 min.
4. Añade 450 µL de SOC/LB sin antibiótico → **37 °C, 45–60 min, 220 rpm**.
5. Siembra 100 µL en LB-**kanamicina 50 µg/mL**. Guarda el resto por si salen pocas colonias (centrifuga suave, resuspende en 100 µL y siembra).
6. 37 °C toda la noche.

> Si el constructo da problemas de recombinación por el LTR, usa **Stbl3** y crece a 30 °C.

---

## 7. DÍA 3 — Cribado

### 7.1 PCR de colonia (rápido)

Cebadores diseñados sobre tu secuencia:

| | Secuencia (5'→3') | Posición | Tm |
|---|---|---|---|
| **H1-F** | `GAGTGGCGCCCTGCAATATTTGCATG` | 2821–2846 | ~61 °C |
| **pSI-R** | `TGAGGCTTAAGCAGTGGGTTCC` | 3021–3042 (rev) | ~57 °C |

- Ta = 58 °C, extensión 30 s.
- **Vacío: 222 pb — con inserto: 278 pb.** Resuélvelo en agarosa al 2,5–3 %.
- Si ves una banda claramente mayor (~334 pb o más) → inserción doble/concatémero: descártala.

### 7.2 Digestión diagnóstica (alternativa, sobre miniprep)

Como los dos sitios se regeneran, BamHI+EcoRI sobre el clon correcto libera un fragmento de **65 pb** que el vector vacío no tiene (en el vacío son 9 pb, invisibles). Hace falta gel al 3 % o acrilamida al 10 %.

### 7.3 Secuenciación (obligatoria)

Manda 4–6 clones positivos con el cebador **H1-F**. El inserto empieza ~83 pb después del cebador, así que la lectura lo cubre con buena calidad.

**Qué comprobar en la secuencia:**
- Una sola copia del dúplex.
- Que el tramo de **5 T seguidas** (terminador de Pol III) está intacto. Es el sitio donde más deleciones aparecen, porque las polimerasas y *E. coli* resbalan en homopolímeros.
- Las dos secuencias esperadas:
  - **sh13:** `GGATCCAATGACTGCCTGGCTTCCTTTCTTCCTGTCAGAAAAGGAAGCCAGGCAGTCATTTTTTTGAATTC`
  - **shSCR:** `GGATCCCCTAAGGTTAAGTCGCCCTCGCTTCCTGTCAGACGAGGGCGACTTAACCTTAGGTTTTTGAATTC`

---

## 8. Resolución de problemas

| Problema | Causa probable | Solución |
|---|---|---|
| Muchas colonias también en L2 (vector solo) | Digestión incompleta (sólo cortó una enzima) | Sube a 45 min (sin pasar de 1 h) y baja el ADN a 0,5 µg; corta la banda por la parte baja para no arrastrar plásmido superenrollado, que migra cerca |
| Pocas o ninguna colonia en L1 | Vector sobre-purificado o poco; dúplex mal anillado | Sube a 100 ng de vector; comprueba el dúplex en gel al 3 % (debe ir como banda única de ~65 pb) |
| Insertos en tándem | Exceso de dúplex | Diluye 1:500 o 1:1000 en vez de 1:250 |
| Deleción en las 5 T | Deslizamiento en el homopolímero | Normal; cribar más clones. Stbl3 a 30 °C ayuda |
| Clones correctos por PCR pero sin silenciamiento | Hebra guía mal cargada | Comprobar por RT-qPCR; valorar invertir sentido/antisentido |

---

## 9. Resumen de tiempos

| Día | Tarea |
|---|---|
| 1 (mañana) | Digestión del vector (30 min) + anillado de oligos (1 h) |
| 1 (tarde) | Gel y purificación del vector → ligación a 16 °C O/N |
| 2 | Transformación → placas O/N |
| 3 | PCR de colonia, picar positivos → cultivos O/N |
| 4 | Miniprep → mandar a secuenciar |
