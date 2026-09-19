# Diseño de los tres constructos — KRT10 c.466C>T (p.Arg156Cys)

Documento cerrado, para llevar al banco. Todo lo que aparece aquí está calculado
por `herramientas/disena_tres_constructos.py` a partir del GenBank real de
`secuencias/pCMV6-KRT10.gb` y del MCS del vector parental. Nada está escrito de
memoria. Ejecuta el script y te lo vuelve a imprimir todo.

```bash
python3 herramientas/disena_tres_constructos.py
```

---

## 0. Lo que el análisis ha confirmado (y lo que ha cambiado)

| Hecho | Estado |
|---|---|
| Tu donante es el **RC204500 (TrueORF)**: ORF **sin codón stop**, fusionada a Myc-DDK | Confirmado (SgfI en 1020, MluI en 2781, STOP sólo en 2874) |
| ORF de KRT10 útil = **1029..2780**, 1752 nt, 584 aa, acaba en **…SKGPRY** | Confirmado, traducida sin stops internos |
| `c.466C>T` = **codón 156 CGC→TGC = p.Arg156Cys** | Confirmado |
| `13F` es la hebra **sentido (pasajera)**; `13R` es la **guía** | Confirmado por complementariedad y por alineamiento al mRNA mutante |
| La mutación cae en la **posición 13 de la guía funcional de 19 nt** | Confirmado — de ahí el "13" del nombre |
| La cola C-terminal de KRT10 es **71 % GC y masivamente repetitiva** | Confirmado — condiciona toda la estrategia |

**Lo que cambia respecto a lo que teníamos escrito:** la pareja NheI + BamHI ya no
es necesaria. Con In-Fusion basta **un solo corte con BamHI**, y —esto es lo
importante— **los dos brazos de 15 nt caen íntegramente dentro del MCS de 48 nt
que me diste**, así que el diseño del constructo 1 está completo sin necesidad del
GenBank del vector.

---

## 1. La mutación y por qué importa dónde cae

`c.466C>T` cambia el codón 156 de `CGC` (Arg) a `TGC` (Cys), en pleno **motivo de
iniciación de la hélice del dominio 1A**:

```
…Thr-Met-Gln-Asn-Leu-Asn-Asp-[Arg156]-Leu-Ala-Ser-Tyr-Leu-Asp-Lys-Val-Arg-Ala…
```

Es el punto caliente clásico de la ictiosis epidermolítica, y es dominante
negativo: la K10 mutante envenena el filamento. Por eso silenciar **sólo** el alelo
mutante es el planteamiento correcto.

### Dónde cae la mutación en tu guía

```
guía funcional 13R (19 nt)   3'←  …  ─────────────  →5'
posición                      19  …  13  …  11 10  …  2 1
                                       ↑        ↑
                              la mutación   sitio de corte de Ago2
```

- Frente al **mRNA mutante**: **0 desapareamientos**. Diana perfecta. ✔
- Frente al **mRNA silvestre endógeno**: **1 desapareamiento, en la posición 13**.

**Éste es el punto débil del diseño y hay que decirlo claro.** La discriminación de
un solo nucleótido es máxima cuando el desapareamiento cae en el **centro de la
guía (posiciones 10–11)**, donde corta Ago2, o en la **semilla (2–8)**. La posición
13 está en la región 3' suplementaria, que es **tolerante** a desapareamientos. Es
muy probable que esta guía también degrade el alelo sano, al menos parcialmente.

No es motivo para tirar el diseño: es motivo para **no construir una sola horquilla**.
Ver §4.

---

## 2. Blindaje de la copia de reemplazo (obligatorio)

Si el shRNA no discrimina bien, tu copia de reemplazo —que es silvestre— también
se silencia. Hay que hacerla inmune con **mutaciones silenciosas**.

```
              c.460 ────────────────────────── c.480
silvestre     AAT GAC CGC CTG GCT TCC TAC
endurecida    AAT GAC CGG CTC GCC AGC TAC
              Asn Asp Arg Leu Ala Ser Tyr     ← proteína IDÉNTICA (verificado
                                                 sobre los 584 aa completos)
```

Cinco cambios, todos sinónimos:

| Posición (plásmido) | Cambio | Codón | Aminoácido | Posición en la guía |
|---|---|---|---|---|
| 1496 | C→G | CGC→CGG | Arg156 | 13 |
| 1499 | G→C | CTG→CTC | Leu157 | 11 |
| 1502 | T→C | GCT→GCC | Ala158 | 8 |
| 1503 | T→A | TCC→AGC | Ser159 | 5 |
| 1504 | C→G | TCC→AGC | Ser159 | 4 |

Resultado: la guía queda con **6 desapareamientos contra el transgén (posiciones
3, 4, 5, 8, 11, 13)** — cuatro dentro de la semilla y uno en el sitio de corte.
Ningún siRNA sobrevive a eso. **El transgén es completamente inmune.**

> **No se toca c.466.** Ahí va la C silvestre: es lo que estás restituyendo.

> Los 5 cambios **no crean ni destruyen ninguna diana de 6 pb**, así que la
> verificación es por Sanger con un cebador, no por digestión.

---

## 3. Constructo 1 — minicírculo de reemplazo

### 3.1 Estrategia: un solo corte, In-Fusion, cero incógnitas

```
MCS (48 nt)   TCTAGAGCTAGCGAATTCGAATTTAAATCGGATCCGCGGCCGCGTCGA
              XbaI  NheI  EcoRI   SwaI    BamHI NotI      (SalI?)
                                        ↑
                                  corte único G^GATCC (entre 30 y 31)

brazo 5' (15 nt) : TTCGAATTTAAATCG      ← dentro del MCS ✔
brazo 3' (15 nt) : GATCCGCGGCCGCGT      ← dentro del MCS ✔
```

**Por qué BamHI solo y no NheI + BamHI:** con NheI el brazo de 15 nt se saldría del
MCS hacia el extremo 3' del promotor EF1α, que no tenemos. Con BamHI los dos
brazos están dentro de lo conocido. Es la única pareja que permite cerrar el
diseño hoy.

**Contrapartida:** un corte único puede recircular. Se resuelve con tres cosas, no
negociables:
1. **Purificar en gel** el vector linearizado (elimina el superenrollado sin cortar).
2. Llevar siempre un **control sin inserto** en la reacción de In-Fusion.
3. Cribar 8 colonias.

**Regalo:** la diana BamHI **queda destruida** en el clon correcto (queda partida
por el inserto). Digestión diagnóstica gratis: el clon bueno **no** corta con BamHI;
el vector religado **sí**. Y BamHI está **libre** dentro de la ORF de KRT10.

### 3.2 El inserto

```
[GCCACC] [ATG …1752 nt de KRT10 endurecida… TAC] [TGA TAA]      = 1764 pb
 Kozak    ORF completa, proteína idéntica a P13645   dos stops
```

Secuencia completa en `secuencias/constructos/inserto_C1_KRT10_endurecido.fa`.
Con los brazos ya puestos, en `inserto_C1_con_brazos_InFusion.fa`.

Kozak `GCCACC`: la posición −3 es A (purina, que es la que manda). La +4 es T y no
se puede cambiar sin tocar Met-Ser. Es un Kozak fuerte estándar.

Dos stops `TGATAA`: TGA seguido de TAA, sin ningún ATG críptico.

### 3.3 Cómo conseguir el inserto — dos planes

#### Plan A (recomendado): encargarlo sintético

```
5'-TTCGAATTTAAATCG · GCCACC · ATG…KRT10 endurecida…TAC · TGATAA · GATCCGCGGCCGCGT-3'
   ── brazo 5' ────                                              ── brazo 3' ───
```

Una sola reacción de In-Fusion y has terminado. Sin PCR, sin mutagénesis, sin
amplificar las repeticiones.

**Texto para el presupuesto (cópialo tal cual):**

> Fragmento de gen lineal, doble cadena, secuencia adjunta (1794 pb).
> La secuencia codificante debe traducir **exactamente** la proteína UniProt
> **P13645** (584 aa). Si la región rica en glicina del extremo 3' requiere
> reducción de complejidad para poder sintetizarse, **usad únicamente
> sustituciones sinónimas y sólo en esa región**; el resto de la pauta debe
> mantener los codones nativos. Los 21 nt correspondientes a c.460–c.480 están
> modificados a propósito y **no deben re-optimizarse**.

Ese último párrafo es crítico: si el algoritmo del proveedor "optimiza" tu ventana
endurecida, puede devolverte los codones nativos y te cargas el blindaje.

**Por qué hace falta ese aviso**, cuantificado:

| Región | Longitud | GC | Ventanas de 20 nt repetidas |
|---|---|---|---|
| Cabeza rica en Gly (c.1–430) | 430 nt | 56,7 % | 0 |
| Dominio varilla (c.431–1290) | 860 nt | 46,5 % | 0 |
| **Cola rica en Gly (c.1291–1752)** | **462 nt** | **71,0 %** | **64** |

La cola es lo que un proveedor marcará como "secuencia compleja". También es la
región que **recombina en *E. coli***, así que vigila deleciones en cada clon.

#### Plan B: desde tu propio plásmido (sin presupuesto)

Dos pasos, los dos con In-Fusion:

**B.1 — Endurecer el donante.** PCR inversa sobre los 6633 pb del pCMV6 con
cebadores espalda contra espalda cuyas colas llevan el bloque endurecido; DpnI;
In-Fusion recircula por el solapamiento de 15 nt. **Un tubo, los 5 cambios a la vez.**

```
KRT10-hard-F  5'-CGGCTCGCCAGCTAC TTGGACAAAGTTCGGGCTCTGG-3'   (37 nt, Tm 57 °C)
KRT10-hard-R  5'-GTAGCTGGCGAGCCG GTCATTCAGATTCTGCATGGT-3'   (36 nt, Tm 51 °C)
                 └ bloque endurecido ┘
```

Producto: `pCMV6-KRT10(endurecido)`, un recurso permanente. Verifica por Sanger.

**B.2 — Pasarlo al minicírculo.**

```
KRT10-MC-F  5'-TTCGAATTTAAATCG GCCACC ATGTCTGTTCGATACAGCTCAAGC-3'  (45 nt)
KRT10-MC-R  5'-ACGCGGCCGCGGATC TTATCA GTATCTTGGTCCCTTAGATGA-3'    (42 nt)
               └ brazo vector ┘ └stops┘ └── apareo con la ORF ──┘
```

PCR con **PrimeSTAR GXL** (mismo ecosistema que tu In-Fusion, y es la que aguanta
moldes difíciles). In-Fusion sobre el vector cortado con BamHI y purificado en gel.

**Riesgo de B.2:** la polimerasa patina en la cola repetitiva. Criba por PCR de
colonia buscando tamaño completo y manda **secuenciación de plásmido completo**
(nanopore, 20–30 €) de 2–3 candidatos. Cuenta con descartar alguno.

### 3.4 Unión final

```
…tctagagctagcgaattcgaatttaaatcg │ GCCACCATG…TACTGATAA │ gatccgcggccgcgtcga…
                        EF1α ──→                                   ──→ SV40 polyA
```

Minicírculo resultante: **≈ 3,2–3,5 kb**, sin esqueleto bacteriano, sin reportero.

---

## 4. Constructo 2 — minicírculo de shRNA

### 4.1 No construyas una sola horquilla

Por lo dicho en §1: tu guía tiene el desapareamiento discriminante en la posición
13, que es permisiva. Construir una sola y esperar que discrimine es apostar la
tesis a una tirada. Las cuatro horquillas de abajo son **cuatro parejas de oligos,
unos 60 € en total y una tarde de trabajo**. Es la mejor relación
información/esfuerzo de todo el proyecto.

### 4.2 Las cuatro horquillas

Formato `sentido – CTCGAG – antisentido – TTTTT`, tallo perfecto de 21 pb
(verificado por código en las cuatro).

| Nombre | Qué prueba |
|---|---|
| **sh466-A** | Tu siRNA exacto, formato estándar pLKO/pSUPER |
| **sh466-B** | El mismo, orientación invertida: el extremo 5' de la guía lo fija el +1 de Pol III, no el corte de Dicer. Para una guía alelo-específica, un 5' preciso mantiene el registro de la semilla |
| **sh466-P10** | Rediseño con la mutación en la **posición 10** de la guía, en el sitio de corte de Ago2. **Éste es el que yo esperaría que discrimine mejor** |
| **shSCR** | Control desordenado, mismo %GC, sin semilla presente en KRT10 ni dianas de restricción |

```
sh466-A    5'-AATGACTGCCTGGCTTCCTTT CTCGAG AAAGGAAGCCAGGCAGTCATT TTTTT-3'
sh466-B    5'-AAAGGAAGCCAGGCAGTCATT CTCGAG AATGACTGCCTGGCTTCCTTT TTTTT-3'
sh466-P10  5'-ATCTGAATGACTGCCTGGCTT CTCGAG AAGCCAGGCAGTCATTCAGAT TTTTT-3'
shSCR      5'-AATTGGGTCCCTGTTCTCACT CTCGAG AGTGAGAACAGGGACCCAATT TTTTT-3'
```

**sh466-P10** usa la ventana 1483..1503 del mRNA mutante. Su guía tiene 1
desapareamiento contra el silvestre **en la posición 10**, justo donde corta Ago2,
y 3 desapareamientos contra el transgén endurecido, todos en la semilla → el
transgén sigue siendo inmune a esta horquilla también.

Oligos con voladizos AgeI/EcoRI listos para anillar: ver la salida del script y
`secuencias/constructos/horquillas.fa`.

### 4.3 Promotor: H1, no U6

**H1 es la elección correcta, y no sólo por seguridad.** Hay dos argumentos y el
segundo es el bueno:

1. U6 es mucho más fuerte y satura Exportina-5, compitiendo con el miRNA endógeno
   del queratinocito. SBI usa H1 en sus propios minicírculos de shRNA.
2. **La discriminación alélica es dosis-dependiente.** A concentración saturante de
   guía, el alelo silvestre —que sólo tiene 1 desapareamiento— también se corta.
   Menos guía = mejor discriminación. Con una guía cuyo desapareamiento está en una
   posición permisiva, **bajar la dosis no es una concesión, es parte del diseño.**

Si la potencia se queda corta, U6 es un cambio directo del mismo casete.

### 4.4 Cómo montarlo

Casete: `[SpeI] AgeI – promotor H1 – horquilla – TTTTT – [MluI]`

- **AgeI + EcoRI**: para meter y cambiar horquillas con oligos anillados (formato
  pLKO clásico, documentadísimo).
- **SpeI + MluI**: para trasplantar el casete entero al constructo 3.
  Las dos están **libres** dentro de la ORF de KRT10 y ninguna está en el MCS.

> **Golden Gate queda descartado**: BbsI corta en c.1728 y Esp3I en c.1104 de la
> ORF de KRT10. Lo he comprobado. Por eso AgeI/EcoRI y no BsmBI.

**Encarga el casete aceptor completo** (H1 + un relleno entre AgeI y EcoRI + los
flancos SpeI/MluI + los brazos In-Fusion) como fragmento sintético de ~300 pb, ~60 €.
Una In-Fusion en `pMC.BESPX-MCS1` y tienes tu **fábrica de shRNA**, reutilizable
para toda la tesis. Cada horquilla posterior son dos oligos y una ligación.

> **Lo único que falta aquí:** los dos brazos de 15 nt para BESPX-MCS1, porque SBI
> sólo ha publicado los nombres de las enzimas (NheI/SpeI y Bsp120I), no la
> secuencia. Pide el GenBank a soporte técnico — es un correo. Alternativa sin
> mapa: pide el casete con flancos **NheI** y **Bsp120I** y clona por restricción
> clásica, que es lo que SBI documenta.

---

## 5. Constructo 3 — los dos juntos

### 5.1 Topología

```
attB ─┤ H1 → shRNA → TTTTT ├──┤ EF1α → Kozak-KRT10endurecida-TGATAA → SV40pA ├─ attP
         ←── orientación divergente ──→
```

Promotores **espalda contra espalda**. Es la disposición estándar para dos unidades
de transcripción en un vector: evita que Pol III lea hacia el polyA y evita la
colisión frontal de las dos polimerasas.

### 5.2 Cómo montarlo — In-Fusion de 3 piezas

Ésta es la parte elegante: **el constructo 3 usa exactamente las mismas piezas y el
mismo corte que el 1.** No hay que rehacer nada.

```
vector cortado con BamHI  +  pieza 1 (KRT10)  +  pieza 2 (casete H1)
```

- **Pieza 1** = `[TTCGAATTTAAATCG] [Kozak-KRT10end-TGATAA] [solapamiento de 15 nt]`
- **Pieza 2** = `[mismo solapamiento] [SpeI-H1-shRNA-TTTTT-MluI, invertido] [GATCCGCGGCCGCGT]`

La pieza 2 se saca por PCR del constructo 2 ya validado (~350 pb, sin repeticiones,
PCR fácil) con cebadores que aportan los solapamientos. **El constructo 2 es la
fuente física del casete**, igual que habíamos previsto.

Los dos brazos externos son los mismos de §3.1, o sea **conocidos**. No hace falta
el GenBank del vector para el constructo 3 tampoco.

### 5.3 El riesgo conocido, dicho antes de empezar

Con esta topología el casete H1 queda **dentro de la 3'UTR del mRNA de KRT10**
(entre el stop y el SV40 polyA). Eso mete una horquilla de 21 pb en la 3'UTR, que
es un sustrato potencial de Dicer: si se corta ahí, el mRNA pierde la cola polyA y
se degrada, bajando la expresión del transgén.

Tres cosas al respecto:

1. **Es medible, no especulativo.** Western de K10 y qPCR del constructo 3 frente
   al constructo 1. Si la expresión cae, lo sabrás en una semana.
2. El transgén está endurecido, así que aunque se produzca shRNA desde la 3'UTR,
   **no se autosilencia**.
3. **La alternativa limpia** es colocar el casete H1 **aguas abajo del SV40 polyA**,
   fuera de la unidad de transcripción de EF1α pero dentro de attB–attP. Eso es lo
   que yo haría **en cuanto tengas el GenBank del vector**: PCR inversa del
   constructo 1 con cebadores que aterricen 20–50 pb después del polyA, e In-Fusion.
   Necesita 2 × 20 nt leídos del mapa, nada más.

**Mi recomendación:** monta el constructo 3 como en §5.2 (hoy, sin esperar a nadie),
mídelo, y si la expresión cae respecto al constructo 1, pásalo aguas abajo del polyA
cuando tengas el mapa. No bloquees el proyecto esperando un correo.

---

## 6. Orden de trabajo

| # | Qué | Depende de | Duración |
|---|---|---|---|
| 1 | Pedir GenBank de pMC.EF1α y pMC.BESPX-MCS1 a soporte SBI | — | 1 correo |
| 2 | Encargar: inserto KRT10 sintético, casete H1 aceptor, 4 parejas de oligos | — | 2–3 sem |
| 3 | **Constructo 1** — In-Fusion, cribado, secuenciación completa | 2 | 1 sem |
| 4 | **Constructo 2** ×4 horquillas + shSCR | 1, 2 | 1 sem |
| 5 | Cribar las 4 horquillas por qPCR alelo-específica en célula | 4 | 2 sem |
| 6 | **Constructo 3** con la horquilla ganadora | 3, 5 | 1 sem |
| 7 | Producción de minicírculo de cada uno | 3, 4, 6 | 4 días c/u |

El paso 5 es el que decide el proyecto. Todo lo demás es fontanería.

---

## 7. Lo que queda pendiente y no me he inventado

1. **Secuencia del promotor H1.** No la escribo de memoria: pídesela al proveedor
   ("promotor H1 humano, versión pSUPER de 231 pb") o cópiala del GenBank de pSUPER
   / pLKO.1 en Addgene. Un promotor mal transcrito de memoria es un pedido tirado.
2. **Brazos In-Fusion para pMC.BESPX-MCS1** (§4.4). Necesitan el GenBank.
3. **Base 49 del vector**, para confirmar si el MCS acaba en un sitio SalI.
4. **BLAST de las cuatro guías** contra el transcriptoma humano, buscando
   coincidencias de semilla. No tengo acceso a NCBI desde aquí. Hazlo antes de
   encargar los oligos: son diez minutos y te ahorra un off-target.
5. **Predicción de sitios crípticos de splicing** sobre la ORF endurecida. Cinco
   cambios sinónimos en 21 nt es riesgo bajo, pero pásalo por un predictor.
