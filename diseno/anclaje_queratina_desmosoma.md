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
   (K10, K14) ni con vimentina.
3. Refuerzan ese enlace, sin sustituirlo, la **plakofilina 1 (PKP1)** —cuya cabeza une a
   la vez Dsg1, DSP y queratinas— y, estructuralmente, la **placoglobina (JUP)** y las
   colas citoplásmicas de **Dsc1a**.
4. La fuerza del enlace DSP–filamento **no es constante**: está regulada por
   fosforilación de un motivo GSR en el C-terminal de DSP (S2849). Hipofosforilada,
   la DSP agarra más fuerte; hiperfosforilada, el desmosoma se endocita.
5. En ausencia (o agregación) de queratinas, el desmosoma **se forma pero no ancla**,
   **se hace más pequeño**, **se endocita más rápido** y **las cadherinas desmosómicas
   pierden fuerza de unión** — tres mecanismos distintos, no uno.

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
| La cola C-terminal de DPI se asocia **directamente** con la cabeza N-terminal de las queratinas de **tipo II epidérmicas (K1, K2, K5, K6)**. No lo hace con queratinas de tipo I, ni con las de tipo II de epitelio simple, ni con vimentina. Identifican un tramo de **18 aminoácidos en la cabeza de K5**, conservado sólo entre tipo II epidérmicas, implicado en la unión | Kouklis *et al.*, J Cell Biol 1994 — [10.1083/jcb.127.4.1049](https://doi.org/10.1083/jcb.127.4.1049) |
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

## 3. Qué co-inmunoprecipitar: panel priorizado

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

## 4. Trampas técnicas del co-IP en este sistema (léelo antes de pedir nada)

### 4.1 La grande: queratinas y desmosomas son **insolubles en detergente**

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

### 4.2 El estado de diferenciación decide si el experimento existe

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

### 4.3 Especies y pesos moleculares

- Usa **cobaya o pollo para la IP y ratón/conejo para el blot** (o al revés). Progen
  vende sueros de cobaya contra casi todo este panel, y es la salida más limpia.
- **K10 corre a ~56,5 kDa**: justo encima de la cadena pesada de IgG (~50 kDa). Si
  inmunoprecipitas con ratón y revelas con ratón, no verás nada útil. Soluciones:
  secundario conformación-específico (TrueBlot / VeriBlot), o entrecruzar el anticuerpo
  a las bolas (DSS/BS3).
- **DSP es enorme** (DPI ~332 kDa, DPII ~260 kDa): gel de 4–6 % o gradiente / Tris-acetato
  3-8 %, transferencia húmeda larga. PG ~83 kDa, PKP1 ~80 kDa, Dsg1 ~160 kDa.

### 4.4 Controles que el tribunal va a pedir

- IgG de la misma especie e isotipo, misma cantidad.
- *Input* (5–10 %) de las dos fracciones.
- **IP recíproca.**
- **Control de mezcla**: lisar silvestre y mutante por separado y **mezclar los lisados
  después**. Las proteínas de filamento se asocian *post-lisis* con una facilidad
  notable; sin este control, una co-IP de citoesqueleto es discutible.
- Fondo genético negativo: knockdown de K1/K10, o una célula sin desmosomas.

### 4.5 Complementos que vale la pena montar en paralelo

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

## 5. Anticuerpos

Aviso honesto: **para casi todos estos, el fabricante documenta WB/IF/IHC y NO IP.**
Los sueros policlonales de cobaya suelen funcionar bien en IP, pero la ficha no lo
promete: hay que titular. Marco abajo qué está publicado en IP y qué no.

### 5.1 Publicados en IP de desmoplaquina en queratinocitos (Perl *et al.* 2023)

| Anticuerpo | Tipo | Nota |
|---|---|---|
| **NW6** (anti-DSP C-terminal) | Conejo | **De laboratorio (grupo de Kathleen Green, Northwestern), no comercial.** Se pide. Es *el* anticuerpo del campo para el C-terminal |
| **NW161** (anti-DSP N-terminal) | Conejo | Ídem |
| **11-5F** (anti-DSP C-terminal) | Ratón | De D. Garrod (Manchester). **Hibridoma disponible: ECACC 91121236** |
| anti-p-S2849-DSP; anti-doble-p-S2845/S2849 | Conejo | Péptido sintético 2843–2853 de DSP humana, hechos por 21st Century Biochemicals. Para el *readout* de fosforilación |
| **5G11** anti-Dsg3 | Ratón | Sigma-Aldrich |
| **1407** anti-placoglobina | **Pollo (IgY)** | Aves Labs. Excelente como lado "blot" tras una IP de ratón/conejo |

### 5.2 Comerciales, muy citados

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

### 5.3 Las dos parejas que yo montaría

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

## 6. Qué haría yo, en orden

1. **Western de fraccionamiento** (Tritón soluble/insoluble) en tu modelo mutante frente
   al corregido: DSP, K1, K10, PKP1, PG, Dsg1. Barato, rápido, y probablemente ya te dé
   el resultado principal (DSP desplazada al soluble).
2. **p-S2849-DSP** por WB e IF. El interruptor de afinidad.
3. **Dispasa** (fragmentación de monocapa). El desenlace funcional.
4. **PLA DSP–K1** en organotípico, con controles de siRNA.
5. **Co-IP** recíproca K1↔DSP, con entrecruzado reversible y control de mezcla.
   Ponerla al final, cuando ya sepas dónde está cada proteína.

Los pasos 1–3 se pueden hacer con lo que hay en casi cualquier laboratorio y sostienen
una figura entera. El 5 es el que se rompe si se hace primero.

---

## 7. Sobre el *readout* de rescate de tu minicírculo

Dos observaciones que salen directamente de la bibliografía de arriba y que afectan al
diseño de los tres constructos:

- **El minicírculo repone K10 (tipo I), pero el enlace con DSP lo hace K1 (tipo II).**
  El criterio de éxito no puede ser "hay K10". Tiene que ser: *K1 vuelve a filamentar,
  vuelve a llegar al desmosoma y vuelve a co-precipitar DSP*. Kouklis 1994.
- **El umbral no es el 100 %.** Con ~60 % de células competentes en queratina, la lámina
  epitelial aguanta el estrés (Bär 2014). Es un objetivo de eficiencia realista y
  defendible para el constructo, y conviene declararlo antes de medir.

---

*Bibliografía recuperada de **PubMed**. Cada referencia enlaza a su DOI.*
