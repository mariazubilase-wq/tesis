# Anclaje queratina–desmosoma: búsqueda bibliográfica y diseño de co-inmunoprecipitación

**Contexto:** ictiosis epidermolítica (IE), mutaciones dominantes en *KRT1* / *KRT10*.
Documento de trabajo: qué proteína ancla qué, qué dice la literatura sobre por qué el
desmosoma es más débil en la IE, qué parejas merece la pena co-inmunoprecipitar y con
qué anticuerpos.

Toda la bibliografía procede de **PubMed**; cada referencia lleva su DOI.

---

## 0. Resumen en cinco frases

1. La proteína que **toca físicamente la queratina** en el desmosoma es la
   **desmoplaquina (DSP)**: su cola C-terminal (tres dominios de repeticiones de
   plaquina, PRD-A/B/C) une el **dominio cabeza N-terminal de las queratinas de tipo II**.
2. En epidermis suprabasal eso significa **K1**, no K10: la unión es específica de
   queratinas de tipo II epidérmicas (K1, K2, K5, K6) y **no ocurre con las de tipo I**
   (K10, K14) ni con vimentina. Ojo a la orientación: es la **cola C-terminal de DSP**
   contra la **cabeza N-terminal de la queratina** (§1.7). K10 ancla de forma indirecta,
   como pareja obligada del heterodímero (§1.8).
3. Refuerzan ese enlace, sin sustituirlo, la **plakofilina 1 (PKP1)** —cuya cabeza une a
   la vez Dsg1, DSP y queratinas— y, estructuralmente, la **placoglobina (JUP)** y las
   colas citoplásmicas de **Dsc1a**.
4. La fuerza del enlace DSP–filamento **no es constante**: está regulada por
   fosforilación de un motivo GSR en el C-terminal de DSP (S2849). Hipofosforilada,
   la DSP agarra más fuerte; hiperfosforilada, el desmosoma se endocita.
5. En ausencia (o agregación) de queratinas, el desmosoma **se forma pero no ancla**,
   **se hace más pequeño**, **se endocita más rápido** y **las cadherinas desmosómicas
   pierden fuerza de unión** — tres mecanismos distintos, no uno.

> ### ⚠️ CORRECCIÓN (importante, leer antes que nada)
>
> **Los puntos 1 y 2 de arriba, tal y como se escribieron en la primera versión de este
> documento, estaban basados en literatura superada.** La versión corregida está en
> **§1.7bis**, y afecta también a §1.1, §1.8, §8 y §9.
>
> **Resumen de la corrección:** la cola C-terminal de DSP **no** une la cabeza N-terminal
> de las queratinas de tipo II con especificidad de tipo. Une el **coil 1 del dominio rod
> central**, con **especificidad amplia** (K5/K14, K1/K10, desmina, vimentina) y **alta
> afinidad (nM) por filamentos YA ENSAMBLADOS**; las cabezas y colas son **prescindibles**
> para esa unión.
> Favre *et al.*, PLoS One 2018 — [10.1371/journal.pone.0205038](https://doi.org/10.1371/journal.pone.0205038)
>
> La preferencia por la **cabeza de tipo II** sigue siendo real, pero pertenece a **PKP1
> y placoglobina**, no a DSP.

---

## 1. La cadena de anclaje, eslabón por eslabón

```
   Dsg1-4 / Dsc1-3          (cadherinas desmosómicas, transmembrana)
        │  cola citoplásmica
   Placoglobina (JUP) ── Plakofilinas (PKP1-3)      (placa armadillo)
        │                        │
        └──────── DESMOPLAQUINA (DSP) ─────────┐
                     cola C-term (PRD-A/B/C)   │
                                               ▼
                      cabeza N-term de queratina de TIPO II  (K1 en suprabasal)
                                               │
                                    heterodímero obligado
                                               ▼
                                         K10 (tipo I)
```

### 1.1 Desmoplaquina — el anclaje verdadero

| Hallazgo | Referencia |
|---|---|
| ⚠️ **SUPERADO — ver §1.7bis.** La cola C-terminal de DPI se asocia con la cabeza N-terminal de las queratinas de **tipo II epidérmicas**, y no con las de tipo I ni con vimentina. Ensayos de solución y *ligand blot* con **queratina recombinante no ensamblada** | Kouklis *et al.*, J Cell Biol 1994 — [10.1083/jcb.127.4.1049](https://doi.org/10.1083/jcb.127.4.1049) |
| El dominio C-terminal de DPI especifica si se une a redes de queratina o de vimentina | Stappenbeck & Green, J Cell Biol 1993 — [10.1083/jcb.123.3.691](https://doi.org/10.1083/jcb.123.3.691) |
| Desplazar la DSP de la membrana (expresando su N-terminal) **desengancha los haces de filamentos intermedios** y altera el ensamblaje de la unión. Prueba funcional de que DSP es necesaria | Bornslaeger *et al.*, J Cell Biol 1996 — [10.1083/jcb.134.4.985](https://doi.org/10.1083/jcb.134.4.985) |
| Doble híbrido: diferencias fundamentales en la unión directa DSP–filamento según el tipo de filamento intermedio | Meng *et al.*, J Biol Chem 1997 — [10.1074/jbc.272.34.21495](https://doi.org/10.1074/jbc.272.34.21495) |
| **Estructura**: DPCT son 3 dominios PRD (A, B, C) de 4,5 repeticiones de 38 aa cada uno; plegamiento globular con un **surco básico conservado** propuesto como sitio de unión al filamento | Choi *et al.*, Nat Struct Biol 2002 — [10.1038/nsb818](https://doi.org/10.1038/nsb818) |
| Estructura de PRD-A+B y arquitectura global de DPCT por SAXS (alargada, no lineal, Dmax 178 Å) | Kang *et al.*, PLoS One 2016 — [10.1371/journal.pone.0147641](https://doi.org/10.1371/journal.pone.0147641) |
| **KO epidérmico de DSP**: el número de desmosomas es igual que en el silvestre, pero **carecen de filamentos de queratina**, y eso basta para que fallen. El estrés mecánico separa las células | Vasioukhin *et al.*, Nat Cell Biol 2001 — [10.1038/ncb1201-1076](https://doi.org/10.1038/ncb1201-1076) |
| Una mutación recesiva en *DSP* (cardiomiopatía + fragilidad cutánea + pelo) **deteriora la unión de DSP a queratinas epidérmicas y a desmina** | Favre *et al.*, Br J Dermatol 2018 — [10.1111/bjd.16832](https://doi.org/10.1111/bjd.16832) |
| Epidermólisis ampollosa acantolítica letal (*DSP*): desmosomas anómalos y **desconexión de los filamentos de queratina del desmosoma** | McGrath & Mellerio, Dermatol Clin 2010 — [10.1016/j.det.2009.10.015](https://doi.org/10.1016/j.det.2009.10.015) |
| Ensayo GFP para medir asociación plaquina–filamento intermedio (método útil si quieres cuantificar afinidad en vez de sólo co-IP) | Favre *et al.*, Methods Enzymol 2015 — [10.1016/bs.mie.2015.06.017](https://doi.org/10.1016/bs.mie.2015.06.017) |

> **Consecuencia directa para la IE.** El contacto molecular es
> **DSP ↔ cabeza de K1**. K10 es de tipo I: no une DSP por sí misma. Una mutación en
> *KRT10* rompe el anclaje **indirectamente**, secuestrando a K1 en agregados y
> privándola de la capacidad de formar filamento. Una mutación en *KRT1* puede además
> romperlo **directamente** si cae en el dominio cabeza/V1.
> Esto define el mejor *readout* de rescate de tu minicírculo: no basta con demostrar
> que hay K10 silvestre; hay que demostrar que **K1 vuelve a filamentar y vuelve a
> co-precipitar DSP**.

### 1.2 El enlace está regulado por fosforilación (y esto es medible)

Justo por debajo del sitio de unión al filamento, la DSP tiene un motivo repetido
**glicina-serina-arginina (GSR)**. Su estado de fosforilación decide la fuerza del
enlace:

- **DSP hipofosforilada → más afinidad por el filamento → más adhesión y más rigidez
  del epitelio.** El mutante constitutivamente hipofosforilado **S2849G** resiste más
  estrés mecánico.
- **GSK3β + PRMT-1** fosforilan; **PP2A-B55α** desfosforila.
  Perl *et al.*, Sci Rep 2023 — [10.1038/s41598-023-37874-8](https://doi.org/10.1038/s41598-023-37874-8)
- **Queratinocitos sin queratinas**: Rack1 queda libre → **PKC-α hiperactiva** →
  **DSP hiperfosforilada** → los desmosomas **se endocitan a velocidad acelerada** →
  las láminas epiteliales se rompen con el estrés. Se rescata reexpresando K5/K14,
  inhibiendo PKC-α o bloqueando la endocitosis.
  Kröger *et al.*, J Cell Biol 2013 — [10.1083/jcb.201208162](https://doi.org/10.1083/jcb.201208162)

> **Hipótesis contrastable para tu tesis, y barata de medir:**
> en tu modelo de IE, ¿está aumentada la **p-S2849-DSP**? ¿La baja el minicírculo de
> reemplazo? Es un Western/IF cuantitativo, no requiere co-IP, y conecta genotipo con
> fenotipo adhesivo por un mecanismo publicado.

### 1.3 Plakofilina 1 — el amplificador suprabasal

| Hallazgo | Referencia |
|---|---|
| El **dominio cabeza** de PKP1 interacciona con **desmogleína 1, desmoplaquina y queratinas**, y su sobreexpresión aumenta drásticamente el reclutamiento de proteínas desmosómicas a la membrana | Hatzfeld *et al.*, J Cell Biol 2000 — [10.1083/jcb.149.1.209](https://doi.org/10.1083/jcb.149.1.209) |
| La "proteína banda 6" (= PKP1) es un miembro de la familia armadillo y **las queratinas purificadas se le unen en ensayo de *overlay*** | Hatzfeld *et al.*, J Cell Sci 1994 — [10.1242/jcs.107.8.2259](https://doi.org/10.1242/jcs.107.8.2259) |
| Mapeo fino: quitar ~1 % de la secuencia de DSP abolía su localización desmosómica; 86 residuos N-terminales bastan para dirigirla. PKP1 une DSP y Dsc1a | Smith & Fuchs, J Cell Biol 1998 — [10.1083/jcb.141.5.1229](https://doi.org/10.1083/jcb.141.5.1229) |
| **Pérdida de PKP1 en humanos** (displasia ectodérmica-fragilidad cutánea): desmosomas **pequeños y mal formados**, espacios intercelulares ensanchados y **conexiones reducidas con el citoesqueleto de queratina** | McGrath *et al.*, Nat Genet 1997 — [10.1038/ng1097-240](https://doi.org/10.1038/ng1097-240); McGrath *et al.*, Br J Dermatol 1999 — [10.1046/j.1365-2133.1999.02667.x](https://doi.org/10.1046/j.1365-2133.1999.02667.x) |
| Bajar PKP1 reduce el ensamblaje desmosómico y el reclutamiento de DSP a los contactos | Sobolik-Delmaire *et al.*, Cell Commun Adhes 2007 — [10.1080/15419060701463082](https://doi.org/10.1080/15419060701463082) |
| Revisión de la familia plakofilina | Hatzfeld, BBA Mol Cell Res 2007 — [10.1016/j.bbamcr.2006.04.009](https://doi.org/10.1016/j.bbamcr.2006.04.009) |

PKP1 es **el compañero natural de K1/K10**: se expresa sobre todo en capas suprabasales,
el mismo compartimento donde se manifiesta la IE. Fenocopia parcialmente lo que
describes ("desmosomas más débiles porque las queratinas no anclan bien"), lo que la
convierte en un excelente **control positivo conceptual**.

### 1.4 PKP3 — por qué el desmosoma grande ancla más

PKP3 une las tres desmogleínas, Dsc3a/b, placoglobina, DSP y K18, y tiene **al menos dos
sitios de interacción con DSP**. Los autores proponen que las interacciones laterales
DSP–PKP **aumentan el tamaño del desmosoma y el número de puntos de anclaje disponibles
para las queratinas**.
Bonné *et al.*, J Cell Biol 2003 — [10.1083/jcb.200303036](https://doi.org/10.1083/jcb.200303036)

Esto explica por qué "desmosoma más pequeño" (lo que se ve en los KO de queratina, §2)
equivale literalmente a "menos anclajes".

### 1.5 Placoglobina y colas de cadherina — el andamio

- **PG-null**: menos desmosomas, **sin placa densa interna** y **con menos filamentos de
  queratina anclados**; β-catenina entra en el desmosoma pero no compensa del todo.
  Bierkamp *et al.*, Development 1999 — [10.1242/dev.126.2.371](https://doi.org/10.1242/dev.126.2.371)
- **Dsc1a (forma larga) sí, Dsc1b no**: la cola de la isoforma *a* basta para reclutar
  DSP y placoglobina y **anclar filamentos**.
  Troyanovsky *et al.*, Cell 1993 — [10.1016/0092-8674(93)90075-2](https://doi.org/10.1016/0092-8674(93)90075-2)
- PG es central en el mecanismo del pénfigo vulgar: sin PG no hay retracción de queratina
  ni pérdida de adhesión tras IgG-PV.
  Caldelari *et al.*, J Cell Biol 2001 — [10.1083/jcb.153.4.823](https://doi.org/10.1083/jcb.153.4.823)

### 1.6 Otros "anclajes" del mismo dominio cabeza (no confundir)

- **Periplaquina / envoplaquina**: periplaquina localiza en desmosomas, membrana
  interdesmosómica y filamentos intermedios; su cola une específicamente K8 y vimentina.
  DiColandrea *et al.*, J Cell Biol 2000 — [10.1083/jcb.151.3.573](https://doi.org/10.1083/jcb.151.3.573);
  Kazerounian *et al.*, Exp Dermatol 2002 — [10.1034/j.1600-0625.2002.110506.x](https://doi.org/10.1034/j.1600-0625.2002.110506.x)
- **Plectina** interacciona *in vitro* con DSP inmunoprecipitada y se asocia a la placa
  desmosómica en células polarizadas.
  Eger *et al.*, J Cell Sci 1997 — [10.1242/jcs.110.11.1307](https://doi.org/10.1242/jcs.110.11.1307)
- **BP230 (BPAG1)** une K5/K14 por secuencias distintas de las de DSP.
  Fontao *et al.*, Mol Biol Cell 2003 — [10.1091/mbc.e02-08-0548](https://doi.org/10.1091/mbc.e02-08-0548)
- **Transglutaminasas**: una **lisina muy conservada en el subdominio V1 de la cabeza de
  las queratinas de tipo II** (K1, K2e, K5, K6) las entrecruza covalentemente a la
  envuelta córnea. Es decir, **el mismo dominio cabeza de K1 sirve para dos anclajes
  distintos**; una mutación ahí golpea a los dos.
  Candi *et al.*, PNAS 1998 — [10.1073/pnas.95.5.2067](https://doi.org/10.1073/pnas.95.5.2067)

### 1.7 Orientación: qué extremo se une a qué (el error fácil de cometer)

Hay **dos C-terminales** en juego y se confunden con facilidad. La unión es
**antiparalela**:

```
   DESMOPLAQUINA          ─── rod ───[ C-TERMINAL: PRD-A / PRD-B / PRD-C ]
                                              ▲
                                              │  surco básico
                                              ▼
   QUERATINA TIPO II  [ N-TERMINAL: cabeza, subdominio V1 ]─── rod ───[ V2 cola ]
```

> **Es la COLA C-terminal de la DESMOPLAQUINA contra la CABEZA N-terminal de la
> QUERATINA.** Textual en Kouklis *et al.* 1994: *"the carboxy terminal 'tail' of DPI
> associates directly with the amino terminal 'head' of type II epidermal keratins"* —
> [10.1083/jcb.127.4.1049](https://doi.org/10.1083/jcb.127.4.1049).

La cabeza N-terminal de las queratinas de tipo II no es sólo el sitio de DSP: es un
**punto caliente funcional** compartido.

| Qué se une ahí | Referencia |
|---|---|
| Cola C-terminal de DSP | Kouklis 1994 [10.1083/jcb.127.4.1049](https://doi.org/10.1083/jcb.127.4.1049) |
| PKP1 (fuerte) y placoglobina (débil). Con K5 mutada: las dos se unen a versiones con **cabeza intacta**; PG pierde la unión al quitar los 157 residuos N-terminales | Smith & Fuchs 1998 [10.1083/jcb.141.5.1229](https://doi.org/10.1083/jcb.141.5.1229) |
| Entrecruzamiento por transglutaminasa a la envuelta córnea, por una **Lys conservada del subdominio V1** | Candi 1998 [10.1073/pnas.95.5.2067](https://doi.org/10.1073/pnas.95.5.2067) |

Y hay **precedente humano** de que romper esa cabeza rompe el anclaje, que es
exactamente el argumento que necesitas:

- Mutaciones en la cabeza de **K5** → EBS con pigmentación moteada, donde *"los
  filamentos de queratina parecen deficientes en su capacidad de anclarse a los
  desmosomas"*.
- Una mutación en esa misma región de **K1** → queratodermia palmoplantar no
  epidermolítica con **fragilidad de células suprabasales**.

Ambos, revisados en Smith & Fuchs 1998, bajo el epígrafe *"An Increased Importance of
the Type II Keratin Head Domain"*.

### 1.7bis ⚠️ CORREGIDO — qué une DSP realmente

**Lo que dice la evidencia más reciente y más directa**, por triple híbrido en levadura y
ensayos de unión por fluorescencia:

> El **coil 1 del dominio rod central** de K5/K14 **es necesario** para la interacción con
> el C-terminal de desmoplaquina, mientras que **sus dominios cabeza y cola son
> prescindibles**. Lo mismo con **K1/K10**, y con **desmina y vimentina**. La afinidad del
> C-terminal de DSP por filamentos **ya ensamblados** de K5/K14 y desmina está en el
> **rango nM**.
>
> Favre *et al.*, PLoS One 2018 — [10.1371/journal.pone.0205038](https://doi.org/10.1371/journal.pone.0205038)

```
   DESMOPLAQUINA         ───rod───[ C-TERMINAL: PRD-A / PRD-B / PRD-C ]
                                            ▲
                                            │  afinidad nM, especificidad AMPLIA
                                            ▼
   QUERATINA  [ cabeza V1 ]──[ COIL 1 ]──[ coil 2 ]──[ cola V2 ]
                                 ▲
                    aquí, y en tipo I igual que en tipo II
```

**Cómo se reconcilia con Kouklis 1994 y Meng 1997.** Los datos de "cabeza de tipo II"
salen de ensayos de solución y *overlay* con **queratina recombinante sin ensamblar**.
Los de coil 1 usan **filamentos ensamblados**, que es el sustrato fisiológico. Es
plausible que existan los dos contactos y que el que manda sobre un filamento real sea el
del rod. Para tus experimentos, **asume el modelo de Favre**.

**Qué SÍ conserva la preferencia por la cabeza de tipo II:** **PKP1** (fuerte) y
**placoglobina** (débil), según los ensayos de *overlay* con mutantes de K5 de Smith &
Fuchs 1998 ([10.1083/jcb.141.5.1229](https://doi.org/10.1083/jcb.141.5.1229)); y el
entrecruzamiento por transglutaminasa de la Lys del V1 (Candi 1998). Esa parte del §1.7
sigue en pie. **Lo que cambia es que ese sesgo de tipo II es de PKP1/PG, no de DSP.**

### 1.7ter Las tres consecuencias que esto tiene para la Parte 2

1. **No busques especificidad DSP–K1 frente a DSP–K10.** No la hay, y ya está publicado
   que no la hay. Tu documento de la Parte 2 (§3.4) tiene razón y esta versión del
   documento se corrige en ese sentido.
2. **Lo que DSP discrimina no es la identidad del compañero, es el ESTADO DE ENSAMBLAJE.**
   Alta afinidad por *filamentos ensamblados*. Ésa es la variable, y es justo la que
   separa tus dos clases de línea celular.
3. **Predicción directa**: un filamento **no canónico pero bien ensamblado** (K1/K14 en el
   KRT10-KO) debería anclarse al desmosoma **igual de bien** que K1/K10. Un filamento
   **canónico pero agregado** (R156C, 189del) **no**. Es exactamente lo que vio Reichelt
   2001 por inmunogold en ratón: filamentos K1/K14/K15 **unidos a desmosomas**.

### 1.8 ¿Y K10? Se une, pero de otra manera

K10 es de **tipo I**. Dos consecuencias:

1. ⚠️ **CORREGIDO (§1.7bis): K10 SÍ une la cola de DSP.** Favre 2018 lo muestra por
   coil 1, igual que K5/K14 y que desmina o vimentina. La afirmación anterior —que las
   queratinas de tipo I no unen DSP— procede de Kouklis 1994 con proteína no ensamblada y
   **no debe usarse**.
2. **Sí puede unir PKP1, de forma secundaria.** En los ensayos de *overlay*, PKP1 se une
   con fuerza a las de tipo II pero muestra *"appreciable association with the type I
   keratins"* (Smith & Fuchs 1998); coherente con que las queratinas purificadas se unan
   a la proteína banda 6 (Hatzfeld 1994, [10.1242/jcs.107.8.2259](https://doi.org/10.1242/jcs.107.8.2259))
   y con que la cabeza de PKP1 una queratinas en doble híbrido (Hatzfeld 2000,
   [10.1083/jcb.149.1.209](https://doi.org/10.1083/jcb.149.1.209)).

**Pero su papel dominante es otro, y es absoluto: K10 es el compañero obligado del
heterodímero.** Los filamentos de queratina son heteropolímeros estrictos de un tipo I +
un tipo II. Sin K10 funcional, K1 no hace filamento; y una K1 que no filamenta es una K1
que no tiene nada que entregar a la placa.

Por eso una mutación en *KRT10* produce **la misma enfermedad** que una en *KRT1*, aunque
K10 nunca toque la desmoplaquina: el anclaje que pierde es **100 % indirecto y 100 %
efectivo**. En el modelo Krt10⁻/⁻, K1 se empareja de forma compensatoria con K5/K14, pero
el resultado no sustituye a K1/K10 (Reichelt 1997,
[10.1242/jcs.110.18.2175](https://doi.org/10.1242/jcs.110.18.2175)).

---

## 2. Por qué el desmosoma es más débil cuando la queratina falla

Tu intuición es correcta, pero la literatura la desglosa en **tres mecanismos
independientes**. Merece la pena decirlo así en la tesis, porque cada uno se mide
distinto.

### (a) Mecánico: menos puntos de anclaje, desmosomas más pequeños

| Modelo | Qué le pasa al desmosoma | Referencia |
|---|---|---|
| **Krt1⁻/⁻;Krt10⁻/⁻** (doble KO, el más informativo para la IE) | Ausencia total de filamentos intermedios en epidermis suprabasal. **Desmoplaquina, Dsc1 y Dsg1 alterados; placoglobina sin cambios; desmosomas suprabasales más PEQUEÑOS** → las queratinas participan en la dinámica desmosómica. Además, pérdida prematura de núcleos y caída de emerina/lamina A-C/Sun1 | Wallace, Roberts-Thompson & Reichelt, J Cell Sci 2012 — [10.1242/jcs.097139](https://doi.org/10.1242/jcs.097139) |
| **Krt10⁻/⁻** (modelo clásico de hiperqueratosis epidermolítica) | K10 truncada queda restringida a complejos con K1; **K6/K16 no compensan** (forman agregados, no filamentos extendidos). Los grumos residuales de K1/K10T se sitúan **en la periferia y en los desmosomas, que mantienen arquitectura normal**. Pérdida total de K2e en planta | Reichelt *et al.*, J Cell Sci 1997 — [10.1242/jcs.110.18.2175](https://doi.org/10.1242/jcs.110.18.2175) |
| **Krt1⁻/⁻** | Pérdida de integridad cutánea + red inflamatoria IL-18 / S100A8 / S100A9, letalidad perinatal; firma transcripcional tipo eccema/psoriasis, distinta de la de Krt5⁻/⁻ | Roth *et al.*, J Cell Sci 2012 — [10.1242/jcs.116574](https://doi.org/10.1242/jcs.116574) |
| **KO de todas las queratinas de tipo II** | **Desmosomas significativamente más pequeños**, por acumulación de proteínas desmosómicas en el citoplasma → defecto de adhesión y hendiduras intercelulares. **Con ~60 % de células que expresan queratina basta para mantener la lámina epitelial bajo estrés** | Bär *et al.*, J Invest Dermatol 2014 — [10.1038/jid.2013.416](https://doi.org/10.1038/jid.2013.416) |

> **Ese 60 % es un dato de diseño para tu tesis de terapia génica.** Fija un umbral de
> corrección: no hace falta corregir todas las células, hace falta pasar de ~60 % de
> células con red de queratina competente. Es el número al que anclar el objetivo de
> eficiencia de transfección del minicírculo.

### (b) Señalización I: PKC-α → hiperfosforilación de DSP → endocitosis

Kröger *et al.* 2013 (arriba, §1.2). El desmosoma **sí se ensambla**, pero se retira de
la membrana más rápido. Medible con p-S2849-DSP y con ensayos de recambio.

### (c) Señalización II: p38MAPK → las cadherinas desmosómicas pierden fuerza de unión

| Hallazgo | Referencia |
|---|---|
| En queratinocitos sin queratinas, **la fuerza de unión de Dsg3 medida por AFM y su estabilidad en membrana (FRAP) están reducidas**, de forma dependiente de p38MAPK. Las queratinas controlan la propiedad adhesiva de la molécula individual, no sólo el andamiaje | Vielmuth *et al.*, J Invest Dermatol 2018 — [10.1016/j.jid.2017.08.033](https://doi.org/10.1016/j.jid.2017.08.033) |
| Las células sin queratinas ya tienen adhesión comprometida y p38MAPK activa en basal; inhibir p38MAPK **restaura** la cohesión | Vielmuth *et al.*, Front Immunol 2018 — [10.3389/fimmu.2018.00528](https://doi.org/10.3389/fimmu.2018.00528) |
| Dsg3 (no Dsg2) forma complejo con p38MAPK activa, sobre todo en la fracción no anclada al citoesqueleto | Hartlieb *et al.*, J Biol Chem 2014 — [10.1074/jbc.M113.489336](https://doi.org/10.1074/jbc.M113.489336) |

### Revisión de cabecera

**Hatzfeld, Keil & Magin**, *Desmosomes and Intermediate Filaments: Their Consequences
for Tissue Mechanics*. Cold Spring Harb Perspect Biol 2017 —
[10.1101/cshperspect.a029157](https://doi.org/10.1101/cshperspect.a029157).
Si sólo lees una, lee ésta. Tesis central: los desmosomas dan cohesión estable y las
queratinas determinan la mecánica celular pero **no generan tensión**.

Complementaria, orientada a enfermedad y a terapias (incluye siRNA contra queratinas
mutantes — pertinente a tu constructo 2):
Knöbel, O'Toole & Smith, *Keratins and skin disease*. Cell Tissue Res 2015 —
[10.1007/s00441-014-2105-4](https://doi.org/10.1007/s00441-014-2105-4)

---

## 3. Qué parejas mirar: panel priorizado

(Vale tanto para co-IF como para co-IP.)

### Nivel 1 — el enlace que de verdad importa

| IP | Blot | Qué contesta |
|---|---|---|
| **anti-K1** | **DSP**, K10, PKP1 | *La* pregunta: ¿sigue K1 agarrando desmoplaquina en el fondo mutante? Y ¿lo recupera el minicírculo? |
| **anti-DSP (C-term)** | **K1**, K10, PKP1, PG, Dsg1 | Recíproca. Obligatoria: una co-IP en un solo sentido con proteínas de citoesqueleto no convence a un tribunal |
| — (no es co-IP) | **p-S2849-DSP / total DSP** | Estado del interruptor de afinidad. El *readout* más barato y más informativo |

**Predicción explícita, derivada de Kouklis 1994:** K10 debería co-precipitar DSP sólo
**indirectamente**, vía su heterodímero obligado con K1. Es tu control de especificidad
interno — y si te sale K10↔DSP tan fuerte como K1↔DSP, sospecha de agregados.

### Nivel 2 — la placa

| IP | Blot |
|---|---|
| anti-PKP1 | K1, K10, DSP, Dsg1 |
| anti-PG (JUP) | DSP, Dsg1, PKP1 |
| anti-Dsg1 | PG, PKP1, DSP |

### Nivel 3 — el eje de señalización (si quieres mecanismo, no sólo descripción)

| IP | Blot | Referencia que lo justifica |
|---|---|---|
| anti-Rack1 | queratinas (K1/K10), PKC-α | Kröger 2013 |
| anti-Dsg3 | p38MAPK activa | Hartlieb 2014 |

---

## 4. Co-inmunofluorescencia: por qué es la técnica correcta, y cómo no estropearla

**Veredicto: para esta pregunta la co-IF es mejor opción que la co-IP.** Tres razones
que no son de comodidad:

1. **El fenotipo de la IE es espacial, y la co-IP es ciega a la geometría.** Lo que
   falla no es que las proteínas dejen de existir ni de tocarse en un tubo: es que los
   filamentos **se retraen del borde celular**, se agregan en grumos y dejan de llegar a
   la placa. Una co-IP negativa no distingue "no interaccionan" de "interaccionan igual
   pero en otro sitio". La IF lo ve directamente.
2. **Desaparece el problema de la insolubilidad** (§5.1). En IF no hay que solubilizar
   nada: al contrario, el metanol frío extrae el *pool* soluble y **deja el citoesqueleto
   y la placa juncional**, que es justo lo que quieres mirar. El talón de Aquiles de la
   co-IP aquí juega a tu favor.
3. **Los anticuerpos de §6 mejoran de golpe.** La pega que te puse — "validados en
   WB/IF/IHC pero no en IP" — **se evapora**: IF/IHC es precisamente lo que las fichas sí
   documentan. Pasas de anticuerpos "a testar" a anticuerpos "a usar".

### 4.1 El aviso importante: colocalización ≠ interacción, y aquí es peor de lo normal

**No cuantifiques un coeficiente de colocalización sobre bordes celulares.** Todo el
desmosoma (de membrana a membrana, placa a placa) mide entre ~100 y 200 nm: está
**por debajo del límite de difracción**. DSP, placoglobina, PKP1, Dsg1 y los extremos
de filamento caen todos dentro del mismo punto difractado. Un Pearson o un Manders de
DSP contra K1 en el borde te va a dar ~0,8 — y le daría lo mismo contra cualquier otra
proteína juncional. **No es un resultado.**

Cuánto hace falta para resolver de verdad la arquitectura de la placa: Stahley *et al.*
necesitaron **dSTORM** para separar los pares de placa y medir distancias
placa-a-placa de decenas de nm en queratinocitos primarios y en epidermis humana, y
encontraron que la distancia del dominio **C-terminal de DSP** (el que une queratina)
**cambia entre basal y suprabasal** y **se acorta en desmosomas hiperadhesivos mediados
por PKP1** — J Cell Sci 2016, [10.1242/jcs.185785](https://doi.org/10.1242/jcs.185785).
Esa misma arquitectura se reorganiza durante la maduración del desmosoma: Beggs *et al.*,
Tissue Barriers 2022, [10.1080/21688370.2021.2017225](https://doi.org/10.1080/21688370.2021.2017225).
Y en tejido de pacientes, la microscopía de superresolución (SIM) reveló agrupamiento
aberrante de proteínas desmosómicas y **desmosomas de menor tamaño** que la IF
convencional no distinguía: Stahley *et al.*, J Invest Dermatol 2016,
[10.1038/JID.2015.353](https://doi.org/10.1038/JID.2015.353).

### 4.2 Entonces, ¿qué se mide? Morfología, no coeficientes

Éstas sí son medidas defendibles con un confocal normal, y todas tienen respaldo en la
bibliografía del §2:

| Medida | Qué detecta | Respaldo |
|---|---|---|
| **Retracción**: distancia del frente de filamentos de K1 al borde celular (marcado con DSP) | El fenotipo central. Es el *readout* clásico del campo (retracción de queratina) | Caldelari 2001 [10.1083/jcb.153.4.823](https://doi.org/10.1083/jcb.153.4.823); Vielmuth 2018 [10.1016/j.jid.2017.08.033](https://doi.org/10.1016/j.jid.2017.08.033) |
| **Perfil de línea perpendicular al borde**: posición del pico de K1 frente al de DSP, e intensidad de K1 *en* el pico de DSP | Cuantifica lo anterior sin recurrir a colocalización | — |
| **DSP en membrana / DSP citoplásmica** | En ausencia de queratina, las proteínas desmosómicas **se acumulan en citoplasma** | Bär 2014 [10.1038/jid.2013.416](https://doi.org/10.1038/jid.2013.416) |
| **Tamaño, número e intensidad de los puntos de DSP por µm de borde** | Los desmosomas suprabasales son **más pequeños** sin K1/K10 | Wallace 2012 [10.1242/jcs.097139](https://doi.org/10.1242/jcs.097139); Bär 2014 |
| **Agregados de queratina**: número, área, posición (perinuclear vs periférica) | El fenotipo directo de la mutación dominante negativa | Reichelt 1997 [10.1242/jcs.110.18.2175](https://doi.org/10.1242/jcs.110.18.2175) |
| **Ratio p-S2849-DSP / DSP total en membrana** | El interruptor de afinidad (§1.2). Es IF cuantitativa, no colocalización | Kröger 2013 [10.1083/jcb.201208162](https://doi.org/10.1083/jcb.201208162); Perl 2023 [10.1038/s41598-023-37874-8](https://doi.org/10.1038/s41598-023-37874-8) |
| **Especificidad de capa** (sólo en organotípico/cortes) | K1/K10 y Dsg1 son suprabasales: la IF lo demuestra y la co-IP no | — |

### 4.3 Paneles concretos

Tres especies, tres colores, sin solapamiento. Los sueros de cobaya de Progen son de
uso estándar en IF de epidermis, y ahí sí están validados.

```
Panel A — EL PRINCIPAL (anclaje)
   cobaya  GP-K1            → K1          (Alexa 488)
   ratón   DP2.15 / 11-5F   → DSP         (Alexa 568)
   DAPI
   Medida: retracción, perfil de línea, tamaño/nº de puntos de DSP

Panel B — la placa accesoria
   cobaya  GP-K10           → K10
   ratón   PP1-5C2          → PKP1
   conejo  (anti-DSP conejo o NW6)  → DSP

Panel C — MECANISMO (el que más rinde por esfuerzo)
   conejo  anti-p-S2849-DSP → DSP fosforilada
   ratón   DP2.15           → DSP total
   cobaya  GP-K1            → K1
   Medida: ratio p/total en membrana, mutante vs corregido

Panel D — composición del desmosoma
   ratón   Dsg1-P124        → Dsg1
   cobaya  GP57             → placoglobina
   conejo  anti-DSP         → DSP
```

### 4.4 La fijación es la variable que decide si el experimento existe

Es donde se cae la mayoría de estos ensayos.

- **Queratinas y DSP**: **metanol anhidro a −20 °C, 3 min en hielo**. Es lo que usan
  Perl *et al.* 2023 para p-S2849-DSP y DSP total. Extrae el *pool* soluble y realza la
  señal juncional.
- **Combinado**: PFA 4 % 20 min a TA **seguido de** metanol frío 3 min, cuando un
  epítopo del panel necesita PFA (así hacen ellos con B55α). Prueba las dos y compáralas
  **antes** de montar el experimento entero.
- **Trampa de las cadherinas**: muchos monoclonales contra cadherinas desmosómicas sólo
  funcionan en metanol/acetona o en criosecciones, no en PFA. Si metes Dsg1 en el panel,
  verifica que tu fijación sirva para **todos** los epítopos a la vez. Si no hay una que
  sirva para todos, parte el panel en dos en lugar de forzarlo.
- **Nunca** Tritón antes de fijar si vas a medir el *pool* citoplásmico de DSP: lo
  estarías lavando.

### 4.5 Controles y adquisición

- **Secundarios cruzados-adsorbidos**, obligatorio con tres especies.
- **Secundarios solos** y **marcajes individuales** para descartar *bleed-through*
  (cobaya y ratón se cruzan con más facilidad de la que se admite).
- Adquirir en **confocal**, un plano z por el centro de la célula, con los bordes
  verticales y en el mismo plano focal. Bordes oblicuos = artefacto garantizado.
- **Mismos ajustes de adquisición** en todas las condiciones, y **análisis ciego**, con
  macro/script, no a mano.
- n ≥ 30 bordes por condición, ≥ 3 experimentos independientes.
- Control positivo de "anclaje roto": *knockdown* de queratina, o expresión del
  N-terminal de DSP, que desplaza la DSP endógena y desengancha los filamentos
  (Bornslaeger 1996, [10.1083/jcb.134.4.985](https://doi.org/10.1083/jcb.134.4.985)).

### 4.6 Lo que la co-IF no puede afirmar — y cómo cubrirlo

La co-IF demuestra **reclutamiento y geometría**, no interacción. Si necesitas afirmar
"interaccionan", dos salidas, y ninguna es la co-IP:

1. **PLA (*proximity ligation assay*)**, sobre los mismos portas, la misma fijación y la
   misma lógica de especies. Da proximidad < 40 nm con señal puntual y controles de
   siRNA limpios. Es lo que usan Perl 2023 para validar DSP–B55α en célula, en
   organotípico y en piel humana. **Es la continuación natural de tu co-IF**, y con los
   anticuerpos del panel A ya la tienes montada.
2. **Superresolución** (SIM, Airyscan, dSTORM) si tienes acceso: pasas de "colocalizan"
   a "están a X nm", que es lo que hizo defendible el trabajo de Stahley.
3. **TEM / inmunogold**, si lo tienes a mano. Sigue siendo el patrón oro para "el
   desmosoma está pero sin filamentos anclados" — es exactamente la figura que cerró el
   KO epidérmico de DSP (Vasioukhin 2001). Reichelt 1997 usó **doble inmunogold** en el
   modelo Krt10⁻/⁻ para distinguir K10 truncada de K6: una figura de TEM vale por media
   tesis en este tema.

---

## 5. Si además quieres co-IP: trampas técnicas de este sistema

### 5.1 La grande: queratinas y desmosomas son **insolubles en detergente**

Un lisado estándar de NP-40 o Tritón contiene sobre todo el *pool* **soluble y no
juncional**. Los filamentos de queratina y la placa desmosómica madura se van al
sedimento. Esto no es un detalle: es la razón número uno por la que esta co-IP sale
negativa y no significa nada.

Comprobación: Perl *et al.* 2023 lisan en **NP-40 0,2 %** (10 mM Tris-HCl pH 8, 100 mM
NaCl, 0,2 % NP-40, 10 % glicerol + inhibidores de proteasas), 30 min en hielo,
incubación con el anticuerpo toda la noche a 4 °C, proteína A/G-agarosa 1 h. Con ese
protocolo precipitan DSP–Dsg3 y DSP–B55α perfectamente… porque son el *pool* soluble.
Para queratinas hace falta más.

**Qué hacer:**

1. **Fraccionar siempre y analizar las dos fracciones**: Tritón-soluble frente a
   Tritón-insoluble (enriquecida en desmosomas/citoesqueleto), como en Hartlieb 2014.
   Por sí sola, esa redistribución ya es un resultado: si el anclaje se rompe, **DSP se
   desplaza hacia la fracción soluble**.
2. **Entrecruzamiento reversible antes de lisar**: DSP (ditiobis[succinimidil
   propionato], permeable a membrana, 0,5–1 mM, 30 min a TA, apagar con Tris 25 mM) o
   DTSSP (impermeable, para lo extracelular). Después se puede lisar con tampón más duro
   (RIPA) y **revertir el entrecruzado con DTT/β-ME** antes de cargar el gel.
3. **Alternativa**: solubilizar el sedimento con urea 8 M y **diluir por debajo de 1 M**
   antes de añadir el anticuerpo. Recupera material, pero pierde interacciones débiles.

### 5.2 El estado de diferenciación decide si el experimento existe

**K1, K10, Dsg1 y PKP1 son suprabasales.** En queratinocitos 2D a calcio bajo,
sencillamente no están. Opciones, de peor a mejor:

- Switch de calcio: 1,2 mM, 2–5 días (lo que usan Perl 2023 en NHEK).
- Interfase aire-líquido / organotípico 3D. Es lo que hace que el sistema se parezca a
  una epidermis, y lo que usan tanto Perl 2023 como Zaver 2023
  ([10.1172/jci.insight.170739](https://doi.org/10.1172/jci.insight.170739), un modelo
  organotípico CRISPR de enfermedad de Darier que es un buen patrón de diseño para una
  tesis de esta forma).
- Si usas HaCaT o N/TERT sin diferenciar: no vas a ver K1/K10. Verifícalo por Western
  antes de montar la co-IP.

**Ojo**: al diferenciar, las transglutaminasas entrecruzan proteínas covalentemente, lo
que complica el análisis y es parte de por qué el campo se ha movido hacia marcaje de
proximidad (Badu-Nkansah & Lechler, Mol Biol Cell 2020 —
[10.1091/mbc.E19-09-0542](https://doi.org/10.1091/mbc.E19-09-0542)).

### 5.3 Especies y pesos moleculares

- Usa **cobaya o pollo para la IP y ratón/conejo para el blot** (o al revés). Progen
  vende sueros de cobaya contra casi todo este panel, y es la salida más limpia.
- **K10 corre a ~56,5 kDa**: justo encima de la cadena pesada de IgG (~50 kDa). Si
  inmunoprecipitas con ratón y revelas con ratón, no verás nada útil. Soluciones:
  secundario conformación-específico (TrueBlot / VeriBlot), o entrecruzar el anticuerpo
  a las bolas (DSS/BS3).
- **DSP es enorme** (DPI ~332 kDa, DPII ~260 kDa): gel de 4–6 % o gradiente / Tris-acetato
  3-8 %, transferencia húmeda larga. PG ~83 kDa, PKP1 ~80 kDa, Dsg1 ~160 kDa.

### 5.4 Controles que el tribunal va a pedir

- IgG de la misma especie e isotipo, misma cantidad.
- *Input* (5–10 %) de las dos fracciones.
- **IP recíproca.**
- **Control de mezcla**: lisar silvestre y mutante por separado y **mezclar los lisados
  después**. Las proteínas de filamento se asocian *post-lisis* con una facilidad
  notable; sin este control, una co-IP de citoesqueleto es discutible.
- Fondo genético negativo: knockdown de K1/K10, o una célula sin desmosomas.

### 5.5 Complementos que vale la pena montar en paralelo

- **PLA *in situ*** (pareja DSP–K1). Es lo que usan Perl 2023 para validar el complejo
  DSP–B55α en célula y en piel humana, con controles de siRNA. Para una interacción de
  citoesqueleto, un PLA bien controlado convence más que una co-IP.
- **Ensayo de disociación con dispasa** (fragmentación de la monocapa tras inversión):
  cuantifica adhesión funcional y es el desenlace que de verdad importa. Protocolo en
  Perl 2023.
- **Ensayo de unión basado en GFP** para plaquina–filamento, si quieres afinidad y no
  sólo presencia (Favre 2015, Methods Enzymol).
- **BioID/TurboID sobre DSP**, si quieres una mirada sin sesgo al interactoma
  (Badu-Nkansah & Lechler 2020).

---

## 6. Anticuerpos

Aviso honesto: **para casi todos estos, el fabricante documenta WB/IF/IHC y NO IP.**
Los sueros policlonales de cobaya suelen funcionar bien en IP, pero la ficha no lo
promete: hay que titular. Marco abajo qué está publicado en IP y qué no.

### 6.1 Publicados en IP de desmoplaquina en queratinocitos (Perl *et al.* 2023)

| Anticuerpo | Tipo | Nota |
|---|---|---|
| **NW6** (anti-DSP C-terminal) | Conejo | **De laboratorio (grupo de Kathleen Green, Northwestern), no comercial.** Se pide. Es *el* anticuerpo del campo para el C-terminal |
| **NW161** (anti-DSP N-terminal) | Conejo | Ídem |
| **11-5F** (anti-DSP C-terminal) | Ratón | De D. Garrod (Manchester). **Hibridoma disponible: ECACC 91121236** |
| anti-p-S2849-DSP; anti-doble-p-S2845/S2849 | Conejo | Péptido sintético 2843–2853 de DSP humana, hechos por 21st Century Biochemicals. Para el *readout* de fosforilación |
| **5G11** anti-Dsg3 | Ratón | Sigma-Aldrich |
| **1407** anti-placoglobina | **Pollo (IgY)** | Aves Labs. Excelente como lado "blot" tras una IP de ratón/conejo |

### 6.2 Comerciales, muy citados

**Desmoplaquina**
- **DP2.15 / DP1+2-2.15** — reconoce DPI y DPII. Progen 61003 (cóctel), Millipore
  [CBL173](https://www.merckmillipore.com/INTL/en/product/Anti-Desmoplakin-1-2-Antibody-clone-DP2.15,MM_NF-CBL173),
  Thermo [690003S](https://www.thermofisher.com/antibody/product/Desmoplakin-1-2-Antibody-clone-DP1-2-2-15-Monoclonal/690003S),
  OriGene BM371. Validado WB/ICC/IHC; **IP no documentada**.
- **DP2.17** (anti-DP1) — Progen / Thermo [61024PROGEN](https://www.thermofisher.com/antibody/product/Desmoplakin-1-Antibody-clone-DP2-17-Monoclonal/61024PROGEN). ICC/IHC.
- **Cobaya policlonal anti-desmoplaquina 1** — Progen ["DP-1"](https://us.progen.com/anti-desmoplakin-1-guinea-pig-polyclonal-serum/dp-1).
  Reacta con DPI y DPII en Western. **Mi recomendación para el lado "blot"** cuando la IP
  sea de ratón o conejo.

**Plakofilina 1**
- **PP1-5C2** — Progen [65160](https://us.progen.com/anti-Plakophilin-1-mouse-monoclonal-PP1-5C2-supernatant/65160) / OriGene BM5110. Ratón IgG1. ELISA/IHC/WB. Reactivo en HaCaT, A-431.
- **PP1-2D6** — Progen 65161.
- **Cobaya policlonal** — Progen [GP-PP1](https://www.progen.com/anti-plakophilin-1-guinea-pig-polyclonal-serum/GP-PP1).

**Placoglobina**
- **GP57**, cobaya, N-terminal — Progen. Detecta el polipéptido de 83 kDa ("banda 5").

**Desmogleína 1**
- **Dsg1-P124** — Progen [651111](https://us.progen.com/anti-Desmoglein-1-mouse-monoclonal-Dsg1-P124-supernatant/651111).
  Detalle importante: está validado sobre **preparaciones citoesqueléticas de piel
  humana** (banda de 160 kDa) — justo la fracción en la que vas a trabajar.

**Queratina 1**
- **GP-K1**, cobaya — Progen. Específico de K1 en capas suprabasales de epitelios
  escamosos cornificados; negativo en esófago/duodeno.

**Queratina 10**
- **GP-K10**, cobaya — Progen. Suprabasal positivo, basal negativo.
- **DE-K10**, ratón — Thermo [MA5-13705](https://www.thermofisher.com/antibody/product/Cytokeratin-10-Antibody-clone-DE-K10-Monoclonal/MA5-13705),
  [Santa Cruz](https://www.scbt.com/p/cytokeratin-10-antibody-de-k10) (SCBT sí lista **IP**
  entre las aplicaciones; Thermo lista IF/IHC-P/WB).
- **RKSE60**, ratón — Thermo MUB0319P.
- **Poly19054**, conejo policlonal — [BioLegend](https://www.biolegend.com/de-de/products/purified-anti-keratin-10-antibody-13377).

### 6.3 Combinaciones recomendadas

**Para co-IF** (los paneles están en §4.3). Nota clave: **para esta aplicación todos los
anticuerpos de §6.2 están dentro de lo que el fabricante documenta** — IF/IHC es
justamente su validación declarada. No hace falta el material de laboratorio de §6.1,
salvo el anti-p-S2849-DSP, que sí hay que pedir o encargar como péptido.

**Para co-IP**, si acabas haciéndola:

```
Experimento A (directo):
   IP  : GP-K1 (cobaya, Progen)
   Blot: DP2.15 o 11-5F (ratón) + DE-K10 (ratón) + PP1-5C2 (ratón)

Experimento B (recíproco):
   IP  : 11-5F (ratón) o NW6 (conejo, pedir al grupo de Green)
   Blot: GP-K1 y GP-K10 (cobaya) + GP57 (cobaya, placoglobina)
```

Cero solapamiento de especies en ninguno de los dos sentidos, y el problema de la
cadena pesada a 50 kDa sobre la banda de K10 desaparece.

---

## 7. Qué haría yo, en orden

Con la co-IF como técnica principal:

1. **Poner a punto la fijación** (§4.4) con marcajes individuales, antes de nada.
   Metanol frío vs PFA→metanol, sobre los cinco epítopos del panel. Un día de trabajo
   que ahorra un mes.
2. **Co-IF Panel A (K1 + DSP)** en mutante frente a corregido, y cuantificar
   **retracción, perfil de línea y tamaño/nº de puntos de DSP** (§4.2). Ésta es la
   figura principal.
3. **Co-IF Panel C (p-S2849-DSP / DSP total / K1)**. Convierte una descripción en un
   mecanismo, y conecta con Kröger 2013 y Perl 2023.
4. **Western de fraccionamiento** (Tritón soluble/insoluble): DSP, K1, K10, PKP1, PG,
   Dsg1. Es el complemento bioquímico de la figura 2 — si el anclaje se rompe, DSP se
   desplaza al *pool* soluble. Barato y muy convincente junto a la IF.
5. **Dispasa** (fragmentación de monocapa). El desenlace funcional: demuestra que lo que
   ves al microscopio tiene consecuencia adhesiva.
6. **PLA DSP–K1** en organotípico, con controles de siRNA. Aquí es donde pasas de
   "colocalizan" a "están a menos de 40 nm".
7. Opcionales según acceso: **superresolución** (SIM/Airyscan) y **TEM**.
8. **Co-IP** sólo si un revisor la pide, y entonces con entrecruzado reversible y
   control de mezcla (§5).

Los pasos 1–5 se hacen con un confocal y un equipo de Western corrientes, y ya sostienen
un capítulo. El orden importa: el paso 1 es el que hunde el experimento si se salta.

---

## 8. Sobre el *readout* de rescate de tu minicírculo

Dos observaciones que salen directamente de la bibliografía de arriba y que afectan al
diseño de los tres constructos:

- **El minicírculo repone K10, pero lo que DSP reconoce es un FILAMENTO ENSAMBLADO**
  (§1.7bis), no una queratina concreta.
  El criterio de éxito no puede ser "hay K10". Tiene que ser: *K1 vuelve a filamentar,
  vuelve a llegar al desmosoma y vuelve a co-precipitar DSP*. Kouklis 1994.
- **El umbral no es el 100 %.** Con ~60 % de células competentes en queratina, la lámina
  epitelial aguanta el estrés (Bär 2014). Es un objetivo de eficiencia realista y
  defendible para el constructo, y conviene declararlo antes de medir.

---

---

## 9. Etiquetas en queratinas: dónde sí, dónde no, y qué validar

Pregunta concreta: *si sobreexpreso K1 con una etiqueta en el C-terminal, ¿estropeo el
desmosoma?* Respuesta corta: **el C-terminal es el extremo menos malo, pero no es
inocuo, y el problema mayor no es la etiqueta sino la sobreexpresión.**

### 9.1 La buena noticia: el C-terminal NO es el sitio de unión a DSP

El sitio de DSP es el **coil 1 del rod** (§1.7bis), y **ni la cabeza ni la cola hacen
falta** para esa unión — lo que refuerza la conclusión: una etiqueta terminal no toca el
sitio de DSP. Pero una etiqueta **N-terminal** seguiría siendo el desastre, porque taparía
(a) el sitio de **PKP1/placoglobina** y (b) la Lys del V1 que entrecruza la
transglutaminasa a la envuelta córnea, además de la superposición cabeza-cola del
ensamblaje.

Precedente directo y del mismo sistema: Smith & Fuchs etiquetaron desmoplaquina con FLAG
en C-terminal y **localizó perfectamente a los desmosomas**; la DSP completa con el FLAG
**en lugar de los primeros 29 residuos** fue **incapaz de asociarse a desmosomas**
(aunque seguía colocalizando con filamentos) —
[10.1083/jcb.141.5.1229](https://doi.org/10.1083/jcb.141.5.1229).
Misma lección, aplicada a queratina: **si hay que etiquetar, al C-terminal**.

### 9.2 La mala: la cola V2 de K1 no es inerte, y llega hasta la placa

Alterar la cola V2 de K1 causa **enfermedad humana**, y con un fenotipo que toca
precisamente al desmosoma:

| Lesión | Fenotipo | Referencia |
|---|---|---|
| Primera mutación descrita en una cola de queratina: frameshift en **V2 de KRT1** | Ictiosis hystrix Curth-Macklin. El análisis estructural mostró **fallo en el empaquetamiento de los filamentos**, **retracción del citoesqueleto del núcleo** y **fallo en la translocación de loricrina a las placas desmosómicas** | Sprecher *et al.*, J Invest Dermatol 2001 — [10.1046/j.1523-1747.2001.01292.x](https://doi.org/10.1046/j.1523-1747.2001.01292.x) |
| Frameshift que altera la cola de **KRT1** (1752insG) | Forma **atípica de hiperqueratosis epidermolítica**. El equivalente en KRT5 da una EBS leve | Sprecher *et al.*, J Invest Dermatol 2003 — [10.1046/j.1523-1747.2003.12084.x](https://doi.org/10.1046/j.1523-1747.2003.12084.x) |
| Mutación que altera por completo la cola de K1 | PPK difusa grave tipo IHCM; *"subraya la importancia funcional del dominio de cola no helicoidal"* | Richardson *et al.*, J Invest Dermatol 2006 — [10.1038/sj.jid.5700025](https://doi.org/10.1038/sj.jid.5700025) |
| Frameshift en V2 de KRT1 que sustituye la cola rica en Gly-Ser por 75 aa ricos en Ala | IHCM leve | Yang *et al.*, Clin Exp Dermatol 2020 — [10.1111/ced.14193](https://doi.org/10.1111/ced.14193) |

**Matiz que importa y que no hay que sobreleer:** todas esas lesiones son *frameshifts
que sustituyen o destruyen* la cola V2. **No** son una etiqueta pequeña añadida *después*
de una cola V2 intacta. No son el mismo daño. Pero establecen que **la cola de K1 tiene
función, y que esa función llega a la placa desmosómica** — así que una etiqueta ahí
**se valida, no se asume**.

El tamaño manda: Myc-DDK o HA (~1–3 kDa) no es lo mismo que GFP (~27 kDa) colgando de
una cola cuya función depende de bucles de glicina y del empaquetamiento lateral.

### 9.3 El riesgo mayor: la estequiometría, no la etiqueta

Las queratinas son **heterodímeros obligados**. Si sobreexpresas K1 por encima de la K10
disponible, la K1 sobrante **no tiene pareja** y agrega. Y un agregado de K1 sin pareja
**se parece a tu fenotipo de enfermedad**: es un falso positivo con muy buena pinta.

Smith & Fuchs documentaron esta clase exacta de artefacto con DSP: en las células más
brillantes, la relación citoplasma/desmosoma subía, *"consecuencia de la sobreexpresión
del transgén, que satura todos los sitios de unión desmosómicos y acumula el exceso de
proteína en el citoplasma"*. **En una co-IF esto se traduce en una regla dura: cuantifica
sólo en células de expresión baja o media, y declara el criterio antes de mirar.**

### 9.4 Qué hacer, en la práctica

- **Minicírculo terapéutico: sin etiqueta.** Tu propio diseño ya lo decidió —
  `diseno_clonaje_KRT10_minicirculo.md` §3.4 ("Sin etiquetas") y §11
  ("❌ Conservar la etiqueta Myc-DDK → cola C-terminal comprometida"). **Esa decisión era
  correcta, y ahora tiene bibliografía detrás.** Mantenla.
- **Si necesitas distinguir transgén de endógeno**, por orden de preferencia:
  1. **Marcar la célula, no la proteína**: reportero fluorescente en cassette aparte
     (P2A/IRES). Identificas la célula transfectada por el reportero y tiñes K1 con
     GP-K1. Para una co-IF que pregunta *dónde está el filamento*, suele ser la mejor
     respuesta: no tocas la proteína.
  2. **Etiqueta pequeña (HA/FLAG) en C-terminal, en un constructo APARTE y declarado no
     terapéutico**, sólo para localización.
  3. GFP en C-terminal: última opción, y sólo si (1) y (2) no sirven.
  - **Nunca en N-terminal.**
- **Checklist de validación de cualquier K1 etiquetada** — las tres, antes de creerte una
  sola imagen:
  1. ¿Se incorpora a filamentos indistinguibles de los endógenos **a expresión baja**?
     (doble marcaje anti-etiqueta + GP-K1)
  2. ¿Llega a bordes DSP-positivos igual que la no etiquetada? (medida de retracción,
     §4.2, etiquetada vs sin etiquetar en paralelo)
  3. ¿Rescata **igual de bien** que la versión sin etiqueta en el ensayo funcional
     (dispasa)?

  Si falla cualquiera de las tres, lo que tienes es un artefacto del reportero, no
  biología.

---

---

## 10. El experimento de Vasioukhin, explicado despacio

Merece una sección propia porque es **la base conceptual de todo lo demás**.

### 10.1 Qué hicieron y qué salió

KO de desmoplaquina **restringido a la epidermis** (el KO completo es letal embrionario).
Resultado, en la piel del animal:

- **El número de desmosomas era igual que en el silvestre.** Contados por microscopía
  electrónica, ahí estaban.
- **Pero no tenían filamentos de queratina anclados.**
- Bastaba con eso: el estrés mecánico separaba las células.
- Reintroducir un transgén de DSP revertía el defecto.

Vasioukhin *et al.*, Nat Cell Biol 2001 —
[10.1038/ncb1201-1076](https://doi.org/10.1038/ncb1201-1076)

### 10.2 Por qué importa tanto

**Disocia dos cosas que casi todo el mundo confunde: que el desmosoma *se ensamble* y
que el desmosoma *funcione*.** Las cadherinas se agrupan, la placa se forma, la unión
existe y se puede contar — y no sirve para nada.

De ahí sale la regla que condiciona tus medidas:

> **Lo que hace fuerte a un desmosoma no es existir, es tener el filamento enganchado.**
> Por eso en §4.2 te propongo medir *fracción de puntos de DSP con filamento asociado* y
> no *número de desmosomas*. Contar desmosomas puede darte un resultado normal en un
> tejido que se está despegando.

### 10.3 Cómo se traduce a la IE: es la imagen especular

| | Qué falta | Qué queda | Resultado |
|---|---|---|---|
| **KO de DSP** | El conector | El filamento (sano) y la unión | Desmosoma presente, sin anclar |
| **IE (KRT1/KRT10)** | El filamento competente | El conector (DSP normal) y la unión | Desmosoma presente, sin anclar |

Las dos lesiones atacan extremos opuestos del mismo enlace y **convergen en el mismo
estado final**. Por eso el KO de DSP es tu mejor control positivo conceptual, y por eso
el *readout* correcto es el mismo en los dos casos.

### 10.4 Tres matices que conviene no saltarse

1. **In vivo el número era normal; en cultivo, no.** Los queratinocitos DP-null *en
   cultivo* tenían **pocos** desmosomas. El fenotipo depende del contexto: tejido ≠
   monocapa. Consecuencia para ti: **no generalices de tu 2D al organotípico** sin
   comprobarlo en los dos.
2. **La pérdida de queratina y la de DSP no son idénticas.** Sin DSP, la unión queda
   estructuralmente presente. Sin queratinas, los desmosomas además se hacen **más
   pequeños** y las proteínas desmosómicas se acumulan en citoplasma (Bär 2014,
   [10.1038/jid.2013.416](https://doi.org/10.1038/jid.2013.416); Wallace 2012,
   [10.1242/jcs.097139](https://doi.org/10.1242/jcs.097139)) — porque hay además una
   retroalimentación por PKC-α y endocitosis (§1.2). O sea: en la IE esperas *ambas*
   cosas, desanclaje **y** cambio de tamaño.
3. **DSP no es sólo del desmosoma, funcionalmente.** En el KO también bajaron las uniones
   adherentes y se bloqueó la reorganización de actina y el sellado de membrana durante
   la formación de la lámina epitelial. Hay diálogo con el sistema actina/AJ; no asumas
   una separación limpia entre compartimentos.

---

## 11. Ideas para la parte 2: qué es interesante de verdad en los desmosomas

Ordenadas por **relación interés/coste**, no por vistosidad. Las tres primeras se hacen
con lo que ya necesitas para la parte 1.

### 11.1 ⭐ Hiperadhesión: ¿puede la IE alcanzar el estado adhesivo maduro?

**Esta es mi recomendación principal.**

Los desmosomas tienen **dos estados**: uno "débil" dependiente de calcio y uno maduro
**hiperadhesivo, independiente de calcio**, que es el que sostiene la epidermis real.
El interruptor entre ambos es **PKC**.

| Pieza | Referencia |
|---|---|
| Los desmosomas independientes de calcio son **hiperadhesivos**; el cambio entre estados **no implica cambio en la composición proteica**, sino activación/inhibición de **PKC** | Kimura, Merritt & Garrod, J Invest Dermatol 2007 — [10.1038/sj.jid.5700643](https://doi.org/10.1038/sj.jid.5700643) |
| La hiperadhesión **es un estado de intercambio proteico reducido** (FRAP de cadherinas, PG y DSP), y **el mutante DP S2849G** — el hipofosforilado, de alta afinidad por queratina — **reproduce ese bloqueo** | Bartle *et al.*, J Cell Biol 2020 — [10.1083/jcb.201906153](https://doi.org/10.1083/jcb.201906153) |
| **Sobreexpresar PKP1 fuerza el estado hiperadhesivo** y protege a los queratinocitos de la IgG de pénfigo | Tucker, Stahley & Kowalczyk, J Invest Dermatol 2014 — [10.1038/jid.2013.401](https://doi.org/10.1038/jid.2013.401) |
| Inducir hiperadhesión farmacológicamente con **Gö6976** (inhibidor de PKC) atenúa la acantólisis | Cirillo *et al.*, Exp Cell Res 2010 — [10.1016/j.yexcr.2009.10.005](https://doi.org/10.1016/j.yexcr.2009.10.005) |

**La hipótesis, que hasta donde alcanzan estas búsquedas nadie ha probado en ictiosis
queratinopáticas:**

> En la IE los queratinocitos **no consiguen adquirir el estado hiperadhesivo**, porque
> la hiperadhesión depende de la asociación DSP–queratina (Bartle 2020) y del tono de
> PKC-α (Kimura 2007), y ambos están alterados cuando la queratina agrega (Kröger 2013).

**Por qué me gusta tanto para tu tesis:**

- **Es barato.** Quelación con EGTA + el mismo ensayo de fragmentación que ya montas
  (§4.2/§5). No necesitas equipo nuevo.
- **Tiene brazo de rescate con dos herramientas publicadas**: Gö6976 y sobreexpresión de
  PKP1. Es decir, **te abre un ángulo de co-terapia** — algo que aportar además del
  minicírculo, que es justo lo que suele faltar en una tesis de terapia génica.
- **Da un desenlace funcional de verdad** para tu constructo: no "hay K10 silvestre",
  sino "la célula recupera la capacidad de hacer adhesión independiente de calcio".

Diseño mínimo: mutante vs corregido vs control → confluencia + Ca²⁺ alto varios días →
EGTA → fragmentación. Y luego el brazo farmacológico.

### 11.2 ⭐ El eje PKC-α → p-S2849-DSP, pero en fondo **mutante**, no nulo

Kröger 2013 lo estableció en células **sin ninguna queratina**. La IE es otra cosa: la
queratina **está, pero agregada**. Que Rack1 quede libre, que PKC-α se active y que DSP
se hiperfosforile en ese contexto **es una predicción razonable y no comprobada**.

Es prácticamente gratis si ya vas a montar el Panel C de §4.3. Y si sale, conecta tu
enfermedad con un mecanismo y con una diana.

### 11.3 Recambio proteico: FRAP de DSP-GFP

La consecuencia directa de Bartle 2020: los desmosomas maduros "encierran" a sus
proteínas. **¿Está acelerado el recambio de DSP en la IE?** Encaja además con el hallazgo
de Kröger de endocitosis acelerada. Coste medio: necesitas imagen en vivo.

### 11.4 Isoformas: ¿se retrasa el cambio a Dsg1/Dsc1?

Wallace 2012 vio que en Krt1⁻/⁻;Krt10⁻/⁻ **cambia la expresión de DSP, Dsc1 y Dsg1**
mientras la placoglobina no se toca. Pregunta barata: ¿está **retrasado o incompleto el
cambio de isoformas de diferenciación** (Dsg3→Dsg1, Dsc3→Dsc1) en tu modelo? Sólo
necesitas IF y qPCR a lo largo de una curva de diferenciación. Descriptivo, pero sólido
y publicable como parte de una caracterización.

### 11.5 La ambiciosa: ¿cuánta carga mecánica soporta la DSP en la IE?

Existen **sensores de tensión FRET sobre desmoplaquina**. El hallazgo de partida ya es
llamativo: **la DSP no está bajo tensión significativa en reposo, y sólo se carga
mecánicamente cuando la célula recibe estrés externo**, de forma transitoria y sensible a
la magnitud y orientación de la deformación.

Price *et al.*, Nat Commun 2018 — [10.1038/s41467-018-07523-0](https://doi.org/10.1038/s41467-018-07523-0)

Y hay evidencia reciente (preprint) de que las fuerzas de actomiosina inducen un **cambio
conformacional en el dominio plakina N-terminal de DSP**, de plegado a extendido:
Dong *et al.*, bioRxiv 2024 — [10.1101/2024.11.19.624364](https://doi.org/10.1101/2024.11.19.624364)
(preprint: cítalo como tal).

**La pregunta**: si la IE es una enfermedad de fallo bajo estrés mecánico, ¿**cambia el
reparto de carga sobre la DSP** cuando la queratina no ancla? Es la más interesante
científicamente y la más cara: necesitas el sensor, un sistema de estiramiento y
probablemente una colaboración. Si encuentras el laboratorio, es una tesis entera.

### 11.6 Paralelo farmacológico que ya funcionó en una enfermedad hermana

En la enfermedad de Darier, un modelo organotípico CRISPR mostró que la pérdida de SERCA2
desmonta proteínas desmosómicas y del citoesqueleto **vía exceso de señalización
MAPK/ERK**, y que **inhibir MEK rescata la integridad de la lámina de queratinocitos**.
Zaver *et al.*, JCI Insight 2023 — [10.1172/jci.insight.170739](https://doi.org/10.1172/jci.insight.170739)

Es el molde exacto de lo que podrías hacer en IE: modelo organotípico + multiómica +
diana quinasa. Y plantea la pregunta directa: **¿está ERK hiperactivo en la IE?** Un
Western de p-ERK cuesta un día.

### 11.7 Qué NO perseguiría

- **Contar desmosomas** como desenlace principal (§10.2).
- **Coeficientes de colocalización** en bordes celulares (§4.1).
- Reabrir el mapeo bioquímico DSP–queratina: está hecho, y hecho bien, entre 1993 y 2016.
  Tu valor añadido está en el **fondo genético de enfermedad y en el rescate**, no en
  redescubrir el enlace.

---

---

## 12. Aplicado al plan real de la Parte 2

Escrito después de leer `resumen_tesis_parte2.md`. Esta sección **sustituye a la §11**
como recomendación operativa: la §11 se escribió sin conocer el plan y proponía cosas que
ahora sé que no encajan.

### 12.1 Lo primero: tu §3.4 tenía razón y yo estaba equivocado

Tu documento dice *"no esperar que DSP prefiera K1 sobre K10 — la pregunta buena es de
arquitectura, no de afinidad"*, citando Favre 2018. **Correcto.** Este documento arrastraba
el modelo de 1994 y está corregido en §1.7bis. Consecuencia práctica: **retira de tu
planificación cualquier experimento de especificidad de unión DSP–K1 vs DSP–K10** — tu
Bloque A3 ya lo advertía, y hace bien.

### 12.2 El Bloque A3 tiene una hipótesis binaria disponible, y no la está usando

Tal como está escrito, A3 es descriptivo (*"¿los filamentos K1/K14 alcanzan la
membrana?"*). Con Favre 2018 se convierte en una predicción falsable:

> **Lo que DSP discrimina no es el compañero, es el estado de ensamblaje.**
>
> | Línea | Filamento | Predicción para el anclaje desmosómico |
> |---|---|---|
> | Parental dif. | K1/K10 canónico, ensamblado | normal |
> | **KRT10-KO** | K1/K14 **no canónico pero ensamblado** | **normal o casi** ⚠️ ver §12.2bis |
> | **R156C / 189del** | canónico pero **agregado** | **fallo** |

Esto separa *"qué queratina"* de *"hay filamento o no"* **con las líneas que ya tienes**, y
convierte A3 en un resultado en vez de una comprobación. Además da el titular que le falta
a tu Paper 1:

> **«La red suprabasal no canónica es competente para el anclaje desmosomal; lo que rompe
> el anclaje es el fallo de ensamblaje, no el cambio de pareja.»**

Encaja con el inmunogold de Reichelt 2001 (filamentos K1/K14/K15 **unidos a desmosomas**)
y lo extiende a humano, que es tu hueco declarado. Y da una lectura limpia del contraste
KO vs mutante que ya planteas en A5 como *"el experimento más discriminante"*.

**Cómo medirlo** (§4.2): retracción, perfil de línea perpendicular, fracción de puntos de
DSP con filamento asociado, tamaño y número de puntos de DSP. **No** coeficientes de
colocalización, **no** número de desmosomas a secas.

### 12.2bis ⚠️ Dato nuevo: el KRT10-KO **se rompe en dispasa**. Qué cambia y qué no

**No falsifica la predicción de §12.2, porque la dispasa no mide eso.** Pero obliga a
reordenar el argumento, y el resultado es mejor historia.

#### La dispasa y el anclaje no son el mismo eje

La fragmentación de monocapa integra **cuatro** cosas:

1. adhesión extracelular (compromiso Dsg/Dsc),
2. anclaje desmosoma–filamento,
3. **competencia mecánica del filamento en sí**,
4. uniones adherentes / actina.

La predicción de §12.2 era sobre **(2)**. Que se rompa dice que falla **alguna**, no cuál.
Es exactamente la distinción que hacen Hatzfeld, Keil & Magin: los desmosomas dan cohesión
intercelular, mientras que **las queratinas determinan la mecánica celular pero no generan
tensión** — dos contribuciones separables
([10.1101/cshperspect.a029157](https://doi.org/10.1101/cshperspect.a029157)).

#### La lectura más probable, y por qué es mejor resultado

> **La red K1/K14 se ancla bien, pero es mecánicamente inferior.**

Anclaje y mecánica quedan **disociados**. Una disociación vale más que un resultado
normal: convierte "la red no canónica funciona / no funciona" en "la red no canónica
**engancha pero no aguanta**", que es una afirmación mucho más específica y más difícil de
haber hecho antes.

Candidatos moleculares para esa inferioridad, todos comprobables con lo que ya tienes:

- **Empaquetamiento (*bundling*)**: la cola V2 de K10 y sus bucles de glicina están
  implicados en el empaquetamiento lateral; la cola de K14 es otra cosa. Precedente: el
  frameshift de la V2 de K1 causa **fallo de empaquetamiento** (Sprecher 2001,
  [10.1046/j.1523-1747.2001.01292.x](https://doi.org/10.1046/j.1523-1747.2001.01292.x)).
  Ya tienes en bibliografía el trabajo de bucles de glicina de la cola de K10.
- **Química de disulfuros**: meter K14 en una red suprabasal cambia el mapa de cisteínas.
  Feng & Coulombe mostraron que los disulfuros importan para la organización de redes
  K5/K14. **Tu tarea pendiente del "mapa comparativo de cisteínas" (§11 de tu documento)
  gana un segundo uso**, y el **WB no reductor de la fracción insoluble** que guardabas
  como control de R156C sirve para las dos preguntas en el mismo gel.
- **Cantidad**: Reichelt 2001 describe *"una cantidad **menor** de filamentos novedosos
  K1/K14/K15"*. Menos filamento es menos resistencia, sin necesidad de que sea peor
  filamento.

#### Y el titular que probablemente tienes delante: **ratón ≠ humano**

| | Fenotipo |
|---|---|
| ***Krt10*−/− ratón** | *"Hyperproliferation... **but no cell fragility**"*; la epidermis adulta **no mostró citólisis** — Reichelt & Magin, J Cell Sci 2002 — [10.1242/jcs.115.13.2639](https://doi.org/10.1242/jcs.115.13.2639) |
| **K10-null humano** (p.Q434X) | **Fenotipo grave**, clínicamente parecido a la EHK dominante; K6/K16/K17 inducidas pero **incapaces de compensar** — Müller *et al.*, Hum Mol Genet 2006 — [10.1093/hmg/ddl028](https://doi.org/10.1093/hmg/ddl028) |

**Tu KO humano se rompe. El ratón no se rompe. El humano con K10-null sí se rompe.**

Es decir: **tu línea está reproduciendo el fenotipo humano y no el murino**, que es
justamente el hueco que declara tu §3.3 (*"nunca se han demostrado filamentos K1/K14 en
epidermis o queratinocitos humanos"*). La pregunta deja de ser "¿compensa la red no
canónica?" y pasa a ser:

> **«¿Por qué la sustitución de queratinas rescata al ratón y no al humano?»**

Eso es mejor pregunta, tiene respuesta mecanística alcanzable (empaquetamiento, cantidad,
disulfuros, anclaje) y explica de paso una discrepancia que lleva veinte años en la
literatura sin abordarse.

#### El discriminador barato: **cómo** se rompe, no cuánto

Mira los **bordes de los fragmentos** de dispasa al microscopio:

| Modo de rotura | Qué implica |
|---|---|
| Separación **intercelular** limpia | fallo de **adhesión** (eje 1–2) |
| **Citólisis**: células rotas por el citoplasma | fallo del **filamento** (eje 3) |

La lesión humana de la IE es **citólisis suprabasal**, no despegue en la unión. Si tus
fragmentos muestran células rotas y no bordes limpios, tienes el eje 3 y la lectura de
arriba queda respaldada casi gratis.

#### Antes de construir sobre este resultado, fija tres cosas

1. **¿En qué estado de diferenciación?** Si fue en el 2D que según tu §4.4 **no induce
   K10**, la parental tampoco tenía K10 y la comparación era "sin K10" contra "casi sin
   K10". Que aun así se rompa significa que la diferencia viene de **otra cosa** (los
   clumps de K5/K14 de la parental, efecto clonal), no de K10. **Es el dato que más
   cambia la interpretación.**
2. **Curva, no punto.** Tu A2 ya lo pide. Un punto único puede estar saturado y entonces
   no puedes ordenar las líneas.
3. **Clones independientes.** Tu §0.2 ya lo pide. Un solo clon CRISPR no distingue "el
   KO se rompe" de "este clon se rompe".

#### Qué le hace esto al plan

**No cae §12.2: se vuelve más informativa**, porque ahora las dos salidas dicen algo.

| Resultado del anclaje (IF/TEM) | Lectura |
|---|---|
| **Anclaje conservado** + dispasa rota | Disociación limpia: el defecto es la **mecánica del filamento**. Es el buen resultado |
| **Anclaje perdido** + dispasa rota | La afinidad in vitro de Favre no se traduce, **o** los filamentos K1/K14 no están tan ensamblados como parecen — que enlaza de vuelta con "DSP prefiere filamento ensamblado" |

Y la **hiperadhesión** (§12.5) deja de ser un añadido y pasa a ser **el discriminador**:
si el KO no alcanza el estado independiente de calcio, el defecto incluye la unión; si lo
alcanza y aun así se rompe, el defecto es el filamento.

### 12.3 Desbloqueo de anticuerpos (tu Bloque 0.3, "el desbloqueo número uno")

Existe la serie de sueros policlonales de **cobaya** de Progen, que resuelve tu problema
de "los cuatro son de conejo":

| Diana | Referencia | Nota |
|---|---|---|
| **K14** | **GP-CK14** (cobaya) — [Progen](https://us.progen.com/anti-Keratin-K14-guinea-pig-polyclonal-serum/GP-CK14) | IHC y WB. **Éste es tu desbloqueo** |
| K15 | GP-CK15 / GP-K15 (cobaya) — [Progen](https://www.progen.com/anti-Keratin-K15-guinea-pig-polyclonal-serum/GP-K15) | |
| K5 | GP-K5 (cobaya) — Progen | |
| K1 | GP-K1 (cobaya) — Progen | ⚠️ **No lo compres si vas a usar GP-CK14**: mismo animal |
| K10 | GP-K10 (cobaya) o **DE-K10** (ratón) | Para pares con K1 usa el **de ratón** |

**Ojo con la combinatoria.** K1 aparece en todos tus pares de A1, así que K1 debe ser la
especie "ancla" y todos los compañeros deben diferir de ella:

```
K1 = CONEJO (el que ya tienes)
   + K14  → GP-CK14 (cobaya)   ó  LL002 (ratón)
   + K15  → GP-K15  (cobaya)   ó  clon de ratón
   + K5   → GP-K5   (cobaya)
   + K10  → DE-K10  (RATÓN)  ← control positivo en la parental
```

Para un **triple** marcaje hacen falta tres especies distintas: conejo (K1) + ratón (K14,
LL002) + cobaya (K15 o K5).

**Aviso práctico para el PLA:** las sondas Duolink de catálogo son **anti-conejo y
anti-ratón**. No he podido confirmar que exista sonda anti-cobaya lista para usar; si no
la hay, habría que conjugar con **Probemaker**. **Por eso, para PLA monta el par como
conejo + ratón**: K1 (conejo) + **K14 clon LL002** (ratón), que es monoclonal de ratón, muy
citado y validado en ICC/IF —
[Abcam ab7800](https://www.abcam.com/en-us/products/primary-antibodies/cytokeratin-14-antibody-ll002-ab7800),
[CST 48020](https://www.cellsignal.com/products/primary-antibodies/keratin-14-ll002-mouse-mab/48020).
Deja los de cobaya para co-IF y para el multiplexado del Odyssey.

Para el resto del panel de A3: DSP → **DP2.15** (ratón) o el policlonal de cobaya de
Progen; Dsg1 → **Dsg1-P124** (ratón, validado sobre preparaciones citoesqueléticas de piel
humana); placoglobina → **GP57** (cobaya). Detalles en §6.

### 12.4 ⚠️ El PLA NO demuestra heterodimerización

Tu Bloque A1 usa PLA para K1+K14 con recuento de puntos. **El PLA no puede sostener la
afirmación "K1 y K10 heterodimerizan con K14".**

El PLA da señal a **< 40 nm**. Dos queratinas en **filamentos adyacentes dentro de un haz**
están a esa distancia sin heterodimerizar. Un haz de filamentos dará PLA positivo
independientemente del emparejamiento. **El control de un solo primario no cubre esto**, y
tampoco lo cubre K1+K10 en la parental como positivo: los dos controles saldrían como
esperas y la conclusión seguiría sin estar demostrada.

Lo que el PLA sí demuestra, y que vale: **K1 y K14 están en la misma estructura
filamentosa y no en redes separadas**. Formúlalo así y es inatacable.

Para el **dímero** hacen falta lecturas bioquímicas:

- **Co-IP desde extracto desensamblado**: solubilizar la fracción insoluble en urea a
  concentración que disuelva el filamento pero preserve el dímero/tetrámero, y **diluir**
  por debajo del umbral antes de añadir el anticuerpo. Sin esto, cualquier co-IP de
  queratinas co-precipita el haz entero y no dice nada de emparejamiento.
- **Entrecruzamiento** seguido de análisis del tamaño de las especies entrecruzadas.
- **Control de mezcla obligatorio**: lisar parental y KO por separado y mezclar. Con
  proteínas de filamento, la asociación post-lisis es la regla, no la excepción.
- **Doble inmunogold** (tu A1 ya lo contempla): es lo que usó Reichelt 2001 y es el
  estándar que te pedirán para comparar con ese trabajo.

### 12.5 Regalo: hiperadhesión, gratis dentro de lo que ya vas a montar

Tu A3 dice *"correlato funcional: dispasa ± inhibidor de PKCα"*. El inhibidor de PKCα
canónico en este campo es **Gö6976** — y resulta que **Gö6976 es la herramienta publicada
para inducir el estado hiperadhesivo** (§11.1).

Es decir: **añadiendo un brazo de quelación con EGTA a un experimento que ya tienes
planificado**, conviertes "dispasa ± inhibidor de PKCα" en un ensayo de **hiperadhesión**,
que mide si tus líneas alcanzan el estado adhesivo maduro independiente de calcio. Coste
marginal: un reactivo que ya está en cualquier laboratorio.

**Y hay un motivo de fondo para que te importe**, porque conecta tus bloques A3 y A5:

- Los dos estados adhesivos son reversibles por señalización de **PKC y EGFR**
  (Kitajima, Kaohsiung J Med Sci 2013 — [10.1016/j.kjms.2012.08.001](https://doi.org/10.1016/j.kjms.2012.08.001)).
- La hiperadhesión es un estado de **intercambio proteico reducido**, y **el mutante DP
  S2849G** —el hipofosforilado, de alta afinidad por filamento— lo reproduce
  (Bartle, J Cell Biol 2020 — [10.1083/jcb.201906153](https://doi.org/10.1083/jcb.201906153)).
- Tu propia bibliografía ya incluye que **la inhibición de EGFR rescata la ultraestructura
  desmosomal y el anclaje de queratinas** en pénfigo (JID 2024).

> **La hiperadhesión es el puente mecanístico entre tu A5 (afatinib / erlotinib /
> trametinib) y tu A3 (desmosomas).** Si tu rescate farmacológico funciona, la pregunta
> "¿por qué?" tiene una respuesta medible: porque devuelve los desmosomas al estado
> hiperadhesivo. Eso convierte A3 de bloque descriptivo en **el mecanismo del rescate**, y
> es lo que sube el paper de *JID* a *JCI Insight* / *EMBO Mol Med*.

### 12.6 Dos apuntes menores sobre tu §3.4

- Sobre el JCS 2012 (*Deletion of K1/K10...*), los detalles concretos que te sirven como
  predicción para A3: **DSP, Dsc1 y Dsg1 alterados; placoglobina SIN cambios; desmosomas
  suprabasales más pequeños**. Que PG no se mueva y Dsg1/Dsc1 sí es un patrón específico
  que puedes buscar en tus líneas.
- Sobre el eje PKCα (JCB 2013): el sitio concreto es **S2849** del motivo GSR de DSP, y la
  fosfatasa que lo revierte es **PP2A-B55α**
  ([10.1038/s41598-023-37874-8](https://doi.org/10.1038/s41598-023-37874-8)). Para tu
  "DSP fosforilada" de A3, pide el anticuerpo **anti-p-S2849** y mide **ratio p/total en
  membrana**, no intensidad absoluta.
- Y un recordatorio de §11.2: Kröger 2013 trabajó con células **sin ninguna queratina**.
  Tu KRT10-KO **sí forma filamentos** (K1/K14, según tus datos preliminares). **No asumas
  que el eje PKCα se active igual**; en tu KO podría estar normal precisamente porque hay
  filamento. Eso sería un resultado, no un fracaso, y refuerza la tesis de §12.2.

### 12.8 Tres puntos abiertos: K10 residual, fragilidad del ratón, y NanoBiT en HEK293T

#### (a) "Algo tiene que expresar K10, si no el KO daría igual"

El argumento es bueno y corta por los dos lados. Formalmente: **el resultado de dispasa y
la frase "no se detecta K10" no pueden ser los dos ciertos tal cual.** O hay K10 por
debajo del límite de detección, o la diferencia viene de otra cosa. Las dos salidas son
informativas y baratas de distinguir.

**Candidato número uno a "otra cosa", y con precedente en tu propio campo: que el KO no
sea un nulo.** El *Krt10*⁻/⁻ clásico **no era un nulo**: hetero y homocigotos **expresaban
un péptido de K10 truncado (K10T), identificado por microsecuenciación**, y ese K10T
**seguía formando complejos con K1** (Reichelt 1997,
[10.1242/jcs.110.18.2175](https://doi.org/10.1242/jcs.110.18.2175)).

Un indel de CRISPR puede producir proteína truncada en vez de nada. Si tu línea fabrica
un K10 truncado, **no es "sin K10"**: puede ser dominante negativo o agregante, y eso
rompe la dispasa con independencia del estado de diferenciación.

Orden de comprobación, de más barato a menos:

1. **`KRT10` por qPCR en la parental 2D, al tiempo exacto de la dispasa.** Si el mRNA está
   y la proteína no se detecta, es sensibilidad o traducción, y la ventana existe. Si no
   está el mRNA, la parental no tiene programa de K10 y el fenotipo es otra cosa.
2. **¿Nulo o truncado?** Secuenciar el alelo editado, predecir el producto y buscarlo por
   WB **con un anticuerpo cuyo epítopo esté aguas arriba de la lesión** (si el epítopo cae
   detrás, un truncado se te escapa). Comprobar NMD por qPCR.
3. **Segundo clon independiente.** Sin esto, "el KO se rompe" y "este clon se rompe" no se
   distinguen. Ya está en tu §0.2.

#### (b) Cómo se midió "no hay fragilidad" en el ratón — y por qué es tu oportunidad

Lo que reporta Reichelt & Magin 2002 es que **la epidermis de ratones K10⁻/⁻ ADULTOS no
mostró citólisis** ([10.1242/jcs.115.13.2639](https://doi.org/10.1242/jcs.115.13.2639)).
Es decir: **histología de piel adulta no desafiada**. No es un ensayo de desafío mecánico.

"No hay fragilidad" es por tanto una afirmación más estrecha de lo que suena. **No** cubre:

- piel **neonatal** (los modelos de queratina suelen dar fenotipo perinatal y compensar
  después; el trabajo de 1997 sobre esa misma línea era en neonatos),
- **desafío mecánico** (prueba de fricción/frotado, el clásico en modelos de EBS),
- mecánica cuantitativa (tracción de explantes, ampolla por succión),
- **dispasa en queratinocitos primarios del ratón** ← el análogo directo de tu experimento.

> **Tienes el ratón y tienes el ensayo.** Dispasa sobre queratinocitos primarios de tu
> *Krt10* KO, **con el mismo protocolo** que la línea humana, es una comparación
> ratón-humano con **la misma lectura**, en vez de inferirla de dos papers con dos métodos
> distintos. Es probablemente el experimento más rentable que tienes ahora mismo.

⚠️ Dos controles de identidad antes: **¿cuál es tu línea de ratón?** Si es la de
Magin/Reichelt, expresa K10T truncado y **no es un nulo** — la misma pregunta de (a), en
el otro sistema. Y el fondo mixto negro/agutí de tu §2.2 importa: los fenotipos cutáneos
de estas redes son sensibles al fondo genético.

#### (c) NanoBiT en HEK293T: fortaleza y límite, según la pregunta

**Es el sistema correcto para una pregunta y el incorrecto para la otra.**

| Pregunta | ¿Sirve HEK293T? |
|---|---|
| ¿**Puede** K1 emparejarse con K14? (capacidad intrínseca) | **Sí, y es el sistema ideal**: sin K1/K10/K5/K14 endógenas compitiendo, lo único que hay es lo que transfectas |
| ¿**Elige** K1 a K14 en un queratinocito? (preferencia real) | **No.** Sin competencia de K5/K15/K6/K16/K17, sin las PTM ni las quinasas del queratinocito, sin desmosomas, sin diferenciación |

La segunda es la pregunta de tu Parte 2. Pero **la ausencia de fondo endógeno, que es la
limitación, se convierte en la mayor ventaja si se diseña como competición**:

```
   LgBiT-K1 + SmBiT-K10   (fijo, expresión baja)
      + K14 sin etiquetar, dosis creciente   → ¿cae la señal?
      + K5 / K15 / K6 sin etiquetar, dosis creciente
   y el recíproco:
   LgBiT-K1 + SmBiT-K14 + K10 sin etiquetar creciente
```

Eso convierte un "¿interaccionan sí o no?" en un **ranking cuantitativo de preferencia**,
que es justo lo que quieres — y que **no se puede hacer en un queratinocito** porque el
*pool* endógeno lo confunde. Si K10 desplaza a K14 con facilidad y K14 apenas desplaza a
K10, tienes una jerarquía, y esa jerarquía **predice** lo que pasa en el KO.

Extensión directa para las mutantes: **¿compite R156C-K10 por K1 tan bien como la WT?**
Es una medida del dominante negativo **a nivel de unión**, limpia de agregación si se hace
a expresión baja.

Notas específicas de HEK293T:

- **La trampa de los agregados es PEOR aquí, no mejor**: sobreexpresar queratinas en una
  célula no epitelial produce agregados por simple desequilibrio de pareja. Titular a la
  baja y verificar por IF que hay filamento y no grumo.
- **Comprobad el fondo de filamentos intermedios de la línea** (vimentina). Si queréis un
  fondo realmente vacío, el clásico del campo es **SW13/cl.2**, negativa para vimentina.
- El control **tipo I + tipo I** (§12.7 del plan) importa aún más aquí.
- **Los positivos hay que confirmarlos en fondo queratinocito**, idealmente en tu
  KRT10-KO: K1 presente, K10 ausente, y toda la competencia endógena puesta. Ése es el
  escenario real.

### 12.7 Qué NO mover de tu plan

Tu §7 y §8 están bien construidos. No toques: el orden de bloques, el criterio de parada
de "si la parental sigue sin expresar K10 → todo a 3D", ni el control obligatorio de
"hacer A1 también en la parental diferenciada". Ese último control es el que decide el
significado del paper y está bien identificado.

---

---

## 13. Cómo convertir esto en un paper Q1

### 13.0 Calibración, para no hablar de cosas distintas

**JID ya es Q1 en Dermatología** (primer cuartil de su categoría). Si el objetivo es
literalmente Q1, tu Paper 1 tal y como está planteado probablemente llegue. Así que la
pregunta útil es otra:

| Techo | Qué hace falta |
|---|---|
| **JID / J Cell Sci** (Q1) | Una caracterización sólida, bien controlada, con una novedad real. **Lo tienes casi.** |
| **JCI Insight / EMBO Mol Med** | Lo anterior **+ mecanismo + intervención que lo pone a prueba + relevancia humana** |
| **Nat Commun / JCB** | Lo anterior **+ un principio general**, no un fenómeno de una enfermedad |

Lo que sigue va dirigido al segundo escalón, que es el realista y ambicioso a la vez.

### 13.1 El diagnóstico: tu Paper 1 son tres papers con una gabardina

El título propuesto —*"emparejamiento no canónico, acoplamiento desmosomal y activación de
ERK reversible"*— son **tres afirmaciones unidas por una conjunción**. Un revisor de
segundo escalón lo lee como *"a collection of observations"* y lo baja de revista. No por
falta de datos: por falta de **una** pregunta.

**Los papers suben de categoría cortando, no añadiendo.** Todo lo que tienes cabe; lo que
hay que decidir es cuál es la afirmación y cuáles son las columnas que la sostienen.

### 13.2 La afirmación: úsala como título

> **«La sustitución de queratinas rescata al ratón pero no al humano: la red no canónica
> K1/K14 se ensambla y se ancla al desmosoma, pero es mecánicamente incompetente.»**

Por qué ésta y no otra:

1. **Resuelve una discrepancia de veinte años** que nadie ha abordado: el *Krt10*⁻/⁻ de
   ratón **no tiene fragilidad celular** ([J Cell Sci 2002](https://doi.org/10.1242/jcs.115.13.2639))
   y el K10-null humano da **fenotipo grave tipo EHK** ([Hum Mol Genet 2006](https://doi.org/10.1093/hmg/ddl028)).
   Un paper que explica por qué dos modelos del mismo gen dan resultados opuestos vale más
   que uno que caracteriza uno de los dos.
2. **Es mecanística y jerárquica**: separa **ensamblaje**, **anclaje** y **mecánica** en
   tres niveles independientes. Las disociaciones venden; las descripciones no.
3. **Sólo tú puedes hacerla.** Tienes líneas humanas isogénicas **y** ratones knock-in con
   **las mismas** mutaciones. Esa combinación es rara y es tu ventaja competitiva real.
4. **Engancha con la Parte 1**: si la sustitución endógena no funciona, el reemplazo
   génico no es una opción entre varias, es **la** opción. Convierte tus dos partes en una
   tesis y no en dos trabajos pegados.

### 13.3 Las tres palancas que deciden el techo

**Palanca 1 — Resolver la diferenciación, o irse a 3D sin discutirlo.**
Es la vía crítica y ya lo tienes bien identificado. Ningún revisor acepta conclusiones
sobre biología suprabasal en un sistema que no expresa K10. **Nota realista:** tu
cronograma le da mes 0–1; puede comerse tres. Planifica el 3D como sistema primario desde
ya, en paralelo, no como plan B.

**Palanca 2 — Meter el ratón DENTRO del Paper 1.** ⭐ La más importante.
Ahora mismo el ratón vive en la Parte 1. Si Paper 1 se queda en cultivo, **su techo es
JID**. La comparación ratón–humano **con la misma lectura y la misma mutación** es lo que
lo sube de escalón. Y el experimento concreto es barato: **dispasa en queratinocitos
primarios de tu *Krt10* KO, mismo protocolo que la línea humana** (§12.8b).

**Palanca 3 — UNA intervención que pone a prueba el mecanismo.**
No un cribado de fármacos: **una** predicción, **un** compuesto, **un** resultado. El
contraste que ya identificaste —el fármaco sobre el **KO** (sin agregados) frente al
**mutante** (con agregados)— es exactamente eso. Si el inhibidor normaliza uno y no el
otro, has separado el eje proliferativo del mecánico **con una sola intervención**. Eso es
una figura final de revista alta.

### 13.4 Esqueleto de figuras

Seis figuras, un arco: **se construye → se ancla → falla → el ratón no falla → por qué →
se puede corregir.**

| Fig. | Afirmación | Qué la sostiene |
|---|---|---|
| **1** | El KO humano construye una red suprabasal **no canónica** | Co-IF K1+K14/K15/K5 con el panel multiespecie (§12.3); PLA **formulado como "mismo filamento"** (§12.4); jerarquía de preferencia por **NanoBiT en competición** (§12.8c); doble inmunogold. **Con la parental diferenciada como control obligatorio** |
| **2** | Esa red **se ancla al desmosoma con normalidad** | Retracción, perfil de línea, fracción de puntos de DSP con filamento, tamaño/nº de puntos (§4.2); TEM de inserción de filamentos; hiperadhesión (§12.5) |
| **3** | **Pero es mecánicamente incompetente** ← el pivote | Dispasa **en curva**; **modo de rotura** (citólisis vs separación intercelular, §12.2bis); solubilidad Tritón; barrera funcional en 3D |
| **4** | **El ratón tolera lo que el humano no** | Mismos ensayos en queratinocitos primarios de tu *Krt10* KO; histología ± desafío mecánico; neonato y adulto |
| **5** | **Por qué**: empaquetamiento, cantidad, química de la red | TEM de *bundling*; cuantificación de filamento; WB **no reductor** de la fracción insoluble; mapa de cisteínas (§12.2bis) |
| **6** | **Se puede corregir**, y el nivel al que actúa | EGFR/MEK sobre 2D y 3D; **contraste KO vs mutante**; lecturas de las figs. 2–3 repetidas bajo fármaco |

Fíjate en que **no hay figura de proliferación ni de Rb**. Eso es deliberado: es otra
historia, y tu línea celular no puede sostenerla (§4.3 de tu documento). Va a discusión, o
a otro paper.

### 13.5 Qué cortar del Paper 1

- **El eje proliferación/Rb.** Fuera. Línea inmortalizada con el eje anulado.
- **La comparación K1 vs K10 mutante.** Ya la cortaste bien (confusor de clase de lesión).
- **El KRT1-KO y el Paper 3.** Que sigan siendo paper aparte / capítulo. **No los bolteés
  al Paper 1**: añaden una segunda pregunta y bajan el techo.
- **Todo lo que empiece por "además observamos".** Si no sostiene una de las seis figuras,
  va a suplementario.

### 13.6 La lista de rechazo: lo que lo tumba por muy buena que sea la historia

Esto no sube el techo; **evita que te tiren el paper**. Es innegociable.

1. **Clones independientes** (2–3 por genotipo) o pools policlonales. Sin esto, "réplica
   biológica" = "réplica del mismo clon" y es pseudorreplicación. Ya está en tu §0.2.
2. **Confusor de dosis.** ddPCR en todas las líneas de sobreexpresión + normalizar.
   **Consejo estratégico: lidera con el KO**, que no tiene problema de dosis, y usa las
   líneas de sobreexpresión como apoyo, no como figura principal.
3. **Control de "compensación vs estado por defecto"**: hacer la Fig. 1 **también en la
   parental diferenciada**. Ya lo tienes identificado como el control que decide el
   significado. Es el primer sitio donde va a mirar un revisor.
4. **Validación de diferenciación por tanda**, con criterios de aceptación fijados **a
   priori**, y tandas descartadas antes de analizarlas. Ya lo tienes.
5. **Cuantificación en ciego**, con macro, y bloqueo por tanda.
6. **¿Nulo o truncado?** (§12.8a). Si tu KO expresa un K10 truncado y sale en revisión,
   cae el paper entero. Resuélvelo ahora.

### 13.7 Los dos añadidos de mayor rendimiento

**(a) Tejido humano de paciente.** Si consigues piel de un paciente con EI recesiva
(K10-null), aunque sea archivo, y muestras **el mismo emparejamiento no canónico en
epidermis humana real**, subes un escalón entero. Es la casilla de "relevancia humana" que
separa J Cell Sci de JCI Insight, y tu grupo está conectado clínicamente. **Es lo primero
que pediría.**

**(b) El dato de tu compañera, bien enmarcado.** La jerarquía de preferencia por NanoBiT
en competición (§12.8c) es una figura cuantitativa que casi nadie tiene para queratinas.
Acordad autoría y diseño **ahora**, no cuando estén los datos.

### 13.8 Evaluación honesta del techo

- **Con las figuras 1–3 bien hechas y controladas**: JID o J Cell Sci. Sólido, Q1,
  publicable. **Es el suelo, y es un buen suelo.**
- **Añadiendo la figura 4 (ratón)**: entras en territorio de JCI Insight / EMBO Mol Med,
  porque dejas de describir un modelo y pasas a resolver una contradicción del campo.
- **Añadiendo 5 y 6 (mecanismo + rescate)**: consolidas ese escalón.
- **Con tejido humano de paciente encima**: es cuando la conversación con un editor de
  revista general deja de ser ridícula.

Lo que **no** te va a llevar arriba, por mucho que lo hagas bien: más caracterización de
las líneas, más marcadores, más condiciones. El techo lo fija **la pregunta**, no el
número de paneles.

---

*Bibliografía recuperada de **PubMed**. Cada referencia enlaza a su DOI.*
