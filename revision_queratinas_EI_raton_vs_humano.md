# Queratinas epidérmicas humano vs. ratón y modelos murinos de ichtiosis epidermolítica (EI)

Revisión bibliográfica — 27 octubre 2026

> Fuente principal de la bibliografía: **PubMed** (búsquedas en PubMed/MEDLINE), complementada con búsqueda web para recursos de cepas (MGI, MRC Harwell). Cada referencia va con su DOI enlazado.

---

## 0. Respuesta corta a tus cuatro preguntas

1. **¿Mi mutación afecta menos a K10 de ratón, o cualquier mutación en Krt10 afecta menos en ratón?**
   Las dos cosas son ciertas pero en niveles distintos, y hay que separarlas:
   - **Si tu alelo es una mutación causante de EI (dominante-negativa en humano), el het sin fenotipo es un problema de UMBRAL, no de tipo de alelo.** El efecto dominante-negativo de las queratinas es **dependiente de dosis**: el het expresa ~50 % de proteína mutante, el homocigoto ~100 %. Si el ratón amortigua más (§1.4), el 50 % cae por debajo del umbral patogénico y el 100 % lo supera. Hay demostración directa de este umbral: Bickenbach et al. concluyeron que **"se requería una concentración crítica de la K1 humana mutante, por encima de la MK1 endógena, para alterar la integridad estructural"** ([DOI](https://doi.org/10.1046/j.1432-0436.1996.6120129.x)); y en Dsk12 los homocigotos son más severos que los het al nacer ([DOI](https://doi.org/10.1038/sj.jid.5700241)). Lo que sigue siendo obligatorio verificar es si la proteína mutante **se produce y se incorpora al filamento en el het** — un missense puede desestabilizarse y degradarse, y entonces actúa como hipomorfo aunque por secuencia sea una mutación "dominante" (§2bis).
   - **Que el homocigoto sea viable y con fenotipo leve-moderado SÍ es, en parte, una diferencia de especie documentada.** El K10-null verdadero de ratón tiene una epidermis sorprendentemente normal al nacer y de adulto muestra hiperproliferación **sin citólisis**, porque K5/K14 persisten suprabasalmente y forman filamentos K1/K14/K15 que rescatan la integridad (Reichelt et al. 2001, [DOI](https://doi.org/10.1091/mbc.12.6.1557); Reichelt & Magin 2002, [DOI](https://doi.org/10.1242/jcs.115.13.2639)). En el humano K10-null homocigoto, en cambio, se inducen fuertemente K6/K16/K17 **pero no compensan** y el fenotipo es severo ([DOI](https://doi.org/10.1093/hmg/ddl028)). O sea: mismo genotipo nulo, ratón tolera mucho mejor que humano, y el mecanismo tiene nombre.

2. **Cuántos modelos murinos de EI hay (K10 y K1).**
   Unos **10–12 modelos/líneas publicados** en total (ver §3): ~6–7 para K10 y ~4–5 para K1, más 2 de *Krt2* en el espectro EI superficial/IBS. Pero el dato relevante es otro: **casi todos son transgénicos sobreexpresores o knockouts; knock-ins de punto en el locus endógeno murino hay prácticamente uno bueno para K1 (Dsk12, Krt1 S194P) y no hay un equivalente canónico publicado para Krt10.** Ese es el hueco.

3. **Cómo es el KO de K10 y si aporta publicar un KO con fenotipo distinto.**
   Hay **dos líneas "KO" de K10 que se confunden constantemente en la literatura** y que tienen fenotipos opuestos (§4). Publicar "otro KO de K10" a secas aporta poco. Publicar **por qué tu alelo da un fenotipo distinto al de las líneas existentes** aporta bastante, y es un paper mecanístico, no descriptivo.

4. **Requisitos para que un modelo de EI sea publicable e interesante.** §6.

---

## 1. Queratinas epidérmicas: humano vs. ratón

### 1.1 Lo conservado
- El esqueleto básico es el mismo: **K5/K14 basal** y **K1/K10 suprabasal** (par tipo II / tipo I obligado). Las familias de queratinas tienen ~54 genes funcionales tanto en humano como en ratón (Vijayaraj, Söhl & Magin 2007, [DOI](https://doi.org/10.1385/1-59745-165-7:203)).
- K1 y K10 son las proteínas más abundantes de la epidermis superior en ambas especies, y en ambas su mutación produce fragilidad suprabasal (Wallace et al. 2012, [DOI](https://doi.org/10.1242/jcs.097139)).
- La ortología K1↔Krt1 y K10↔Krt10 es clara, y los dominios de varilla (donde caen las mutaciones de EI) están muy conservados.

### 1.2 Lo que NO es equivalente — y que afecta directamente a tu interpretación

| Elemento | Humano | Ratón | Consecuencia para EI |
|---|---|---|---|
| **K2 (KRT2)** | Capa espinosa alta de **casi todo el cuerpo** | Restringida a **oreja, planta y regiones interescamas de la cola** (Herzog, Winter & Schweizer 1994, [DOI](https://doi.org/10.1111/1523-1747.ep12371757)) | El "repuesto" tipo II de K1 tiene geografía distinta: en ratón el tronco piloso carece de K2, pero la planta sí la tiene. Los sitios que fallan no son los mismos. |
| **K77 (KRT77 / "K1b")** | Se **apaga tras el nacimiento**; queda en conductos de glándula sudorípara ecrina | **Se mantiene en epidermis adulta** e infundíbulo folicular | El ratón adulto tiene un parálogo tipo II extra en epidermis que el humano no tiene. Y es funcionalmente intercambiable con K1: en el *Krt77*-KO **sube K1 y rescata** el fenotipo (2024, [DOI](https://doi.org/10.1016/j.bbamcr.2024.119881)). Amortiguación extra en ratón del lado tipo II. |
| **K9** | Palmoplantar (zonas de carga/fricción) | Prácticamente restringida a **almohadillas plantares**; en planta de ratón K1/K9/K10 predominan solo en footpads, mientras el resto de la planta es K2/K10 (2015, [DOI](https://doi.org/10.1016/j.jdermsci.2015.10.008)) | La "compensación local" difiere por sitio corporal. Fenotipar solo dorso es insuficiente. |
| **K6** | *KRT6A/B/C* | *mK6α/mK6β*, que **evolucionaron de forma independiente** tras la divergencia de especies y con regulación distinta (Takahashi et al. 1998, [DOI](https://doi.org/10.1006/geno.1998.5476)) | La respuesta de queratinas de herida (K6/K16/K17), que es el principal mecanismo compensatorio humano, no es directamente comparable entre especies. |
| **Arquitectura epidérmica** | Epidermis interfolicular gruesa (5–10 capas nucleadas), pelo escaso, zonas de carga mecánica (palmas, plantas, bipedismo) | Epidermis fina (2–3 capas), pelaje denso, cuadrupedismo | Mucho menos estrés de cizalla sobre la epidermis interfolicular del ratón. Bickenbach et al. ya observaron que el epitelio de almohadilla plantar (sin folículos) **ampollaba** mientras la piel pilosa no, y concluyeron que los folículos estabilizan/protegen la epidermis del trauma ([DOI](https://doi.org/10.1046/j.1432-0436.1996.6120129.x)). |
| **Recambio epidérmico** | Más lento | Más rápido | Los queratinocitos citolíticos se eliminan antes; menos acumulación de daño. En *K10−/−* el tránsito está acelerado y los label-retaining cells desaparecen (Reichelt et al. 2004, [DOI](https://doi.org/10.1111/j.0022-202X.2004.23426.x)). |
| **Modificadores genéticos** | Fondos humanos heterogéneos | El fenotipo de los mutantes de queratina **depende del fondo** (de letalidad embrionaria a casi nada), lo que implica modificadores no identificados (Vijayaraj et al. 2007, [DOI](https://doi.org/10.1385/1-59745-165-7:203)) | **Tu fondo genético puede ser la explicación completa.** Ver §5. |

### 1.3 La piel palmoplantar: NO es una inversión, son dos compartimentos

> **Corrección.** Una versión previa de esta sección afirmaba que "el hub K1/K10 está invertido" entre especies y que por eso los modelos de *Krt10* dan fenotipo plantar. **Era una simplificación incorrecta**, y la falsa de inmediato un dato: **los modelos murinos de K1 también tienen fenotipo en almohadillas.** La explicación real es más fina y requiere distinguir dos compartimentos dentro de la planta del ratón.

#### El dato que yo había aplanado
La planta murina **no es homogénea**. Del estudio del doble KO ([DOI](https://doi.org/10.1016/j.jdermsci.2015.10.008)): *"K2 y K10 son las queratinas suprabasales más prominentes en plantas normales de ratón **con la excepción de las almohadillas, donde predominan K1, K9 y K10**"*.

Aplicando el apareamiento obligado tipo II + tipo I — K1(II) con K10(I) y con K9(I); K2(II) con K10(I):

| Compartimento | Queratinas | Filamentos | ¿Equivalente humano? |
|---|---|---|---|
| **Almohadillas** (*footpads*) del ratón | K1, K9, K10 | **K1/K10 + K1/K9** | **Sí**, composición parecida a palma/planta humana |
| **Planta interalmohadilla** del ratón | K2, K10 | **K2/K10** | **No tiene equivalente humano claro** |
| **Palmoplantar humana** | K1, K9, K10, (K2) | **K1/K9** dominante | — |

#### Lo que predice, y lo que de hecho se observa
- **K10 mutante** es tipo I en **los dos** compartimentos (K1/K10 y K2/K10) → debería afectar **toda la planta**.
- **K1 mutante** es tipo II en las almohadillas (K1/K10 y K1/K9) pero **no participa en el compartimento K2/K10** → debería afectar **almohadillas**, con la zona interalmohadilla relativamente amortiguada por K2/K10.

Y la literatura confirma **las dos cosas, no una**:
- **Modelos de K1 con fenotipo en almohadillas:** en Dsk12 (*Krt1* S194P) el fenotipo se detectó **por hiperpigmentación de las almohadillas** en heterocigotos, con ampollas e hiperqueratosis después ([DOI](https://doi.org/10.1038/sj.jid.5700241)). Y en el transgénico de K1 humana mutante, *"el epitelio de almohadilla plantar, que carece de folículos pilosos, mostró ampollas en la capa espinosa"* ([DOI](https://doi.org/10.1046/j.1432-0436.1996.6120129.x)).
- **Modelos de K10 con fenotipo plantar:** los heterocigotos `Krt10^tm1Tmm` desarrollan descamación y engrosamiento *"principalmente en los pies"*; los de Arin, hiperqueratosis en las patas ([DOI](https://doi.org/10.1083/jcb.152.3.645)); y en el KO homocigoto de K10 **se perdía toda la K2e de la epidermis plantar**, *"señalando a la K10 como su pareja"* ([DOI](https://doi.org/10.1242/jcs.110.18.2175)).

**Respuesta directa a la pregunta: no, deberías ver alteración plantar en los modelos de K1 *y* en los de K10 — y así es.** Mi formulación anterior era errónea.

#### Dónde está la divergencia real entre especies
No en una inversión de hub, sino en **cuánto participa K10 en la piel de carga**:

| | Mutación en **K1** | Mutación en **K10** |
|---|---|---|
| **Humano** | QPP prominente ✔ | Palmas y plantas **respetadas** |
| **Ratón** | Fenotipo en almohadillas ✔ | Fenotipo **en toda la planta** |

La regla humana ([OMIM #113800](https://omim.org/entry/113800)) es que *"la queratodermia palmoplantar es un rasgo más prominente en pacientes con BCIE con mutaciones en KRT1 que en los que tienen mutaciones en KRT10"*, porque **K1 es la principal pareja de K9 en la epidermis palmoplantar**; y K9 es un tipo I **exclusivo de epidermis palmoplantar terminalmente diferenciada** humana (su mutación causa la QPP epidermolítica de Vörner, hotspot en el codón 163 de *KRT9*, [revisión](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2018.00645/full)).

Es decir: en humano la piel palmoplantar **se apoya en K9** y puede prescindir en buena medida de K10 → *KRT10* la respeta. En ratón, K10 **es la tipo I de toda la planta**, en ambos compartimentos → *Krt10* sí la afecta. **K1 afecta la piel de carga en las dos especies**; lo que divergen es K10.

**Y el compartimento K2/K10 interalmohadilla es el único exclusivamente K10-dependiente — y no tiene equivalente humano.** Por tanto, la parte del fenotipo plantar de tu ratón que venga de ahí **no es traducible a la clínica humana**. Eso es una limitación que conviene que escribas tú antes de que lo escriba un revisor.

**Capa anatómica adicional:** las patas del ratón son **lampiñas y de carga**, el único sitio sin protección folicular — Bickenbach atribuyó a los folículos un papel estabilizador frente al trauma ([DOI](https://doi.org/10.1046/j.1432-0436.1996.6120129.x)). Por eso las patas son el sitio donde *cualquier* queratinopatía suprabasal murina se manifiesta antes, con independencia del gen.

#### El experimento que sale de aquí (y que es barato)
Mapea la **distribución de la lesión dentro de la planta**: almohadillas vs. zona interalmohadilla, con inmunofluorescencia de K1, K2, K9 y K10 en paralelo.
- Si tu K10 mutante afecta **también** la interalmohadilla → coherente con envenenamiento del sistema K2/K10, y es el compartimento sin paralelo humano.
- Si se limita a las almohadillas → está actuando sobre K1/K10 y K1/K9, lo más parecido a la situación humana.
- Comparar esa distribución con la de un modelo de K1 (Dsk12 está publicado) te da un contraste interpretable con datos ya existentes.

Es una histología dirigida, sobre tejido que probablemente ya tienes, y responde a una pregunta mecanística concreta. Buen candidato a figura.

> ⚠️ Cautelas: (1) la regla *KRT1*→QPP / *KRT10*→respeta palmas es una **tendencia, no una ley** — hay casos de *KRT10* con QPP, y solapa con *KRT9*; cítala como tendencia. (2) La asignación de queratinas por compartimento viene esencialmente de **un** estudio ([DOI](https://doi.org/10.1016/j.jdermsci.2015.10.008)); confírmala con tus propias tinciones antes de construir un argumento sobre ella.

### 1.4 Mensaje de esta sección
El ratón tiene **más redundancia tipo II en epidermis adulta** (Krt77 + Krt2 en sitios específicos), **mantiene K5/K14 suprabasales** cuando falta K10, y **soporta mucho menos carga mecánica** en la epidermis interfolicular. Las tres cosas empujan en la misma dirección: **un defecto de K1/K10 se expresa más débilmente en ratón que en humano**, sobre todo en piel dorsal pilosa, y sobre todo en modo pérdida-de-función.

---

## 2. Dominante-negativo vs. pérdida de función: el eje que explica tu fenotipo

Esto es lo que, en mi lectura, resuelve tu duda. La EI humana tiene **dos genéticas distintas**:

- **EI dominante (la clásica, ~1/200.000–300.000).** Missense en varilla → proteína mutante que **se incorpora al filamento y lo envenena** (dominante-negativo). Fuchs, Esteves & Coulombe demostraron el mecanismo en ratón transgénico ([DOI](https://doi.org/10.1073/pnas.89.15.6906)).
- **EI recesiva.** Alelos nulos bialélicos de *KRT10*. Heterocigotos **normales**, homocigotos severos (Müller et al. 2006, [DOI](https://doi.org/10.1093/hmg/ddl028)). Existen además casos de **self-improving EI** por alelos con splicing "leaky" y K10 residual — ojo, el reporte más citado de esto (Frommherz et al., Br J Dermatol 2019, [DOI](https://doi.org/10.1111/bjd.18325)) está **retractado**, úsalo solo con esa advertencia.
- Y un tercer mecanismo aparte: **ichtiosis with confetti**, frameshifts de *KRT10* al mismo marco alternativo que generan una cola rica en arginina que redirige K10 al **nucléolo**; el fenotipo revierte por recombinación mitótica (Choate et al. 2010, Science, [DOI](https://doi.org/10.1126/science.1192280); Burger et al. 2011, [DOI](https://doi.org/10.1111/j.1365-2133.2011.10639.x)). No es un simple null ni un simple dominante-negativo.

**Importante:** si tu alelo es una mutación *causante de EI* (missense dominante en humano), tu patrón **no** se explica diciendo "es un alelo recesivo". Lo que observas es que **la dominancia se pierde en el ratón**, y eso tiene tres explicaciones posibles que hay que ordenar — umbral de dosis, desequilibrio de expresión alélica del knock-in, o dilución del pool tipo I específica de ratón (§2bis).

Lo que sí sigue siendo cierto del marco anterior: la pérdida de función de *KRT10* es recesiva en **ambas** especies (portadores humanos nulos normales, Müller et al. [DOI](https://doi.org/10.1093/hmg/ddl028)), así que **si tu missense se degrada en lugar de incorporarse al filamento, el fenotipo que verás será indistinguible del de un hipomorfo** — y esa es la primera cosa que hay que excluir a nivel de proteína, no de genotipo.

---

## 2bis. Una mutación dominante humana que en ratón solo se manifiesta en homocigosis: precedentes y causas

Este es tu escenario exacto, y **tiene un precedente publicado y muy bueno**.

### 2bis.1 El precedente: el knock-in humanizado de K12 L132P (distrofia corneal de Meesmann)
Allen et al. generaron un **knock-in humanizado** con la mutación **K12-Leu132Pro**, una mutación dominante-negativa *severa* de una enfermedad **autosómica dominante** humana. Resultado ([DOI](https://doi.org/10.1093/hmg/ddw001)):
- **No había cambios evidentes en lámpara de hendidura.**
- **Los homocigotos** sí mostraban fenotipos histológicos y ultraestructurales de fragilidad epitelial, agregados citoplásmicos de queratina, perfil de queratinas alterado, inducción de chaperonas, marcadores apoptóticos de UPR (CHOP, caspasa 12) y **apoptosis aumentada ×17**.
- Los autores validaron los hallazgos en córnea de **paciente** con la misma mutación (MS, inmunohistoquímica) → el modelo era fiel aunque el fenotipo requiriese homocigosis.
- Y lo publicaron en *Human Molecular Genetics* declarando explícitamente: *"aunque el fenotipo más severo se observa en los ratones homocigotos, este modelo proporcionará un banco de pruebas para terapias, no solo para distrofias corneales sino también para **otras queratinopatías causadas por mutaciones similares**"*.

Es del laboratorio de **W.H.I. McLean**, el grupo de referencia en genética de queratinas. **Que tu fenotipo esté en el homocigoto no te impide publicar: hay precedente directo, en buena revista, con esa misma limitación asumida y argumentada.**

### 2bis.2 Otros precedentes de dominancia incompleta/dependiente de dosis en queratinas
- **Bickenbach et al. 1996 (K1 humana mutante en ratón):** se necesita una **concentración crítica** de queratina mutante sobre la endógena para romper la integridad; los neonatos **homocigotos para el transgén** tenían piel más gruesa e índice de marcaje aumentado y colapso de la red perinuclear ([DOI](https://doi.org/10.1046/j.1432-0436.1996.6120129.x)).
- **Dsk12 (Krt1 S194P):** aunque es dominante, los **homocigotos son más severos que los heterocigotos** al nacer → efecto gradual de dosis dentro del propio ratón ([DOI](https://doi.org/10.1038/sj.jid.5700241)).
- **"Dominantes parciales" en humano:** OMIM recoge para *KRT14* una mutación que actúa como *partial dominant*, con heterocigotos de enfermedad localizada más leve y homocigotos de enfermedad más severa. La dominancia de las queratinas **no es binaria ni siquiera en humano**.
- **Mutaciones dominantes latentes hasta el estrés:** en el modelo de piel humanizada de paquioniquia congénita con *KRT6A* **N171K** (una mutación dominante inequívoca), **la piel regenerada era fenotípicamente normal** y solo desarrolló rasgos de PC sostenidos **tras un estímulo hiperproliferativo agudo (tape stripping)** ([PubMed 21150925](https://pubmed.ncbi.nlm.nih.gov/21150925/)). Un het "sin fenotipo" sin desafío mecánico puede ser un **falso negativo**.

### 2bis.3 Las tres hipótesis para tu het, en orden de prioridad

| | Hipótesis | Predicción | Cómo se descarta |
|---|---|---|---|
| **1** | **Desequilibrio de expresión alélica del knock-in** (cassette de selección residual, cicatriz loxP/FRT en intrón, splicing/poliadenilación alterados, silenciamiento): el alelo mutante se expresa por debajo del WT → la fracción mutante efectiva en el het es **<50 %**. En el homocigoto no hay WT que diluya, así que el fenotipo aparece. | Ratio alélico mutante:WT < 1 en piel | **RNA-seq/pirosecuenciación alelo-específica + Western cuantitativo.** Es un artefacto frecuente y **explicaría tu patrón completo por sí solo**: hay que excluirlo antes de cualquier afirmación sobre especie. |
| **2** | **Umbral de dosis con amortiguación mayor en ratón** (la hipótesis "de especie"). 50 % de mutante por debajo del umbral, 100 % por encima. | Ratio alélico ~1:1, proteína mutante presente e incorporada en el het, pero sin agregados ni citólisis; homocigoto con agregados | Cruces de sensibilización: **alelo mutante / null** (*Krt10*<sup>mut/−</sup>, el mutante pasa a ser el ~100 % del pool con una sola copia) y **mutante en fondo *Krt77*<sup>−/−</sup> o *Krt2*<sup>−/−</sup>**. Si *Krt10*<sup>mut/−</sup> fenocopia al homocigoto → umbral confirmado. |
| **3** | **Dilución del pool tipo I específica de ratón.** En ratón K5/K14 **persisten suprabasalmente** y forman filamentos K1/K14/K15 ([DOI](https://doi.org/10.1091/mbc.12.6.1557)); más Krt77 y K2 como parejas tipo II extra. La K10 mutante puede ser desplazada/diluida en ratón y no en humano. | K14/K15 suprabasales elevados en el het | IF/Western por capa y sitio; comparar con queratinocitos humanos editados con **la misma sustitución** en organotípico 3D. |

Y transversal a las tres: **¿se está produciendo e incorporando la proteína mutante?** Un missense puede desestabilizarse y degradarse vía proteostasis/chaperonas — el propio paper de K12 encontró **inducción de chaperonas y UPR**, lo que indica que la célula está gestionando activamente la proteína mutante. Si en tu het la K10 mutante se degrada, tienes un hipomorfo funcional pese a ser una mutación "dominante" por secuencia. **Western + inmuno-EM en el het son el experimento que ordena todo lo demás.**

### 2bis.4 Qué necesito saber de tu alelo para afinar esto
1. **Qué mutación exactamente** (¿R156H/R156C del motivo de iniciación de hélice 1A? ¿2B? ¿linker L12?). El motivo de iniciación de 1A está hiperconservado entre especies, lo que **debilita** la hipótesis "en ratón ese residuo es distinto" y **refuerza** la de umbral/dosis. Los dominios distintos tienen severidades distintas en humano.
2. **¿Knock-in humanizado o sustitución del codón equivalente en el *Krt10* murino?** Un exón humanizado puede expresarse peor o emparejar peor con la K1 murina.
3. **¿Queda cassette de selección, neo, o sitios loxP/FRT en el locus?**
4. **¿Qué fenotipo tiene el homocigoto: con agregados de tonofilamentos y citólisis, o hiperproliferación sin citólisis?** Esto decide si es dominante-negativo con umbral (agregados) o si fenocopia al K10-null (sin citólisis, ver §4).

## 2ter. El alelo R156C ya tiene modelo murino: Arin et al. 2001 — y reproduce tu patrón exacto

Según PubMed, el texto completo de **Arin MJ, Longley MA, Wang XJ, Roop DR**, *Focal activation of a mutant allele defines the role of stem cells in mosaic skin disorders*, J Cell Biol 2001;152:645 ([DOI](https://doi.org/10.1083/jcb.152.3.645), PMC2195990) establece lo siguiente:

### 2ter.1 Equivalencia de numeración
El paper confirma que el hotspot humano es el **codón 156 de *KRT10***, un residuo de arginina evolutivamente muy conservado, hotspot por metilación de CpG y desaminación; y que el codón equivalente en el ***Krt10* murino es el 154**. Es decir:

> **R156C humana ≡ R154C murina.** Si trabajas con "R156C", en nomenclatura de alelo murino tu mutación es **R154C**. Comprueba cómo está anotada tu línea: puede estar publicada o depositada bajo R154C y no la encontrarás buscando "R156C".

### 2ter.2 Qué hicieron y qué obtuvieron
- **Knock-in por recombinación homóloga en el locus endógeno** de *Krt10* (BAC de 129SVJ, mutagénesis por PCR, reemplazo del codón 154 Arg→Cys), con **cassette PGKneo flanqueado por loxP insertado en el intrón 1**.
- Generaron **dos líneas**: `+/mut^neo` (neo retenido) y `+/mut` (neo escindido in vitro con Cre antes de la inyección), más el sistema **inducible** cruzando con CrePR1 (Cre–receptor de progesterona truncado, activable con RU486 tópico).

**Y aquí está lo que te importa, literalmente del paper:**
- *"el cassette neo suprime la expresión del alelo mutante. En consecuencia, los animales desarrollan un **fenotipo muy leve, principalmente restringido a piel expuesta a estrés mecánico**"*.
- *"El análisis de RNA reveló que el mRNA del alelo mutante estaba **significativamente reducido al 35–40 % de los niveles del alelo salvaje**"*.
- Al cruzar esos hets para obtener **homocigotos**: *"mostraron un fenotipo muy severo al nacer con ampollas y erosiones extensas, y **murieron poco después**"*, con desintegración completa del estrato espinoso y K10 abundante en capas suprabasales (toda procedente de alelos mutantes → **el mRNA mutante sí se traduce**).
- Conclusión de los autores: *"la presencia de K10 salvaje en los heterocigotos `+/mut^neo` es **suficiente para superar los efectos del nivel reducido de K10 mutante**"*, y *"**la severidad del fenotipo clínico correlaciona con el nivel de expresión del alelo mutante**"*.
- Los hets/quimeras con **neo escindido** sí tenían lesiones queratósicas focales en patas desde el nacimiento, que progresaban a hiperqueratosis gruesas.

### 2ter.3 Las tres consecuencias para tu tesis
1. **Mi hipótesis nº1 (desequilibrio de expresión alélica por cassette residual) no es teórica: es el mecanismo publicado y medido de este mismísimo alelo.** Un neo en el intrón 1 bajó el mutante al 35–40 % y eso bastó para borrar el fenotipo del heterocigoto. **Si tu línea conserva cassette, neo, o incluso solo la cicatriz loxP/FRT en un intrón, tienes la explicación completa de tu patrón, ya validada en la literatura para R154C.** Esto pasa a ser la primera cosa que debes comprobar, no la tercera.
2. **Tu homocigoto es viable; los de Arin con neo morían al nacer.** Esa es una diferencia real y es tu dato más interesante: sugiere que tu alelo mutante se expresa **aún por debajo del 35–40 %**, o que el fondo genético amortigua más. Un **R156C viable en homocigosis** es precisamente la herramienta que falta (los modelos severos son letales y no sirven para ensayos terapéuticos longitudinales).
3. **El encuadre "primer modelo de R156C" está ocupado.** Reposiciona: no es un modelo nuevo de EI, es un **punto nuevo en la serie alélica de dosis** del mismo alelo. Arin ya dejó escrito que *"la mejora del fenotipo de EHK puede lograrse mediante supresión parcial del alelo mutante"* — tu línea es la validación genética in vivo de ese umbral, y eso es exactamente lo que necesita un programa de siRNA/edición alelo-específica.

> **Encuadre sugerido, revisado:** *"Una serie alélica de dosis de Krt10 R154C define el umbral de K10 mutante necesario para la ichtiosis epidermolítica, y proporciona un modelo viable en homocigosis para ensayo de supresión alelo-específica."* Cuantifica el ratio mutante:WT en tus hets y homocigotos y correlacionalo con fenotipo: esa curva dosis–respuesta es el paper.

### 2ter.4 La curva dosis–respuesta de Arin, en números

Tomando como unidad la expresión de **un** alelo WT = 100:

| Genotipo | K10 WT | K10 mutante | **Ratio mut/total** | Fenotipo |
|---|---|---|---|---|
| `+/+` | 200 | 0 | 0 | Normal |
| `+/mut^neo` (germinal) | 100 | **35–40** | **~0,27** | **Muy leve**, restringido a piel con estrés mecánico |
| `+/mut` neo escindido (**quimeras**) | 100 | ~100 | **~0,5** | Lesiones queratósicas **focales en patas al nacer** → hiperqueratosis gruesas marrones |
| `mut^neo/mut^neo` | 0 | ~70–80 | **1,0** | **Letal al nacer**, desintegración completa del estrato espinoso |
| **Humano R156C/+** | 50 % | 50 % | **~0,5** | **EI severa generalizada** |

**Dos lecturas que son el corazón del paper:**

1. **Manda el ratio, no la cantidad absoluta.** El homocigoto `mut^neo/mut^neo` tiene **menos** proteína mutante en términos absolutos (~75 unidades) que el het limpio (~100) y sin embargo pasa de "lesiones en patas" a **letal**. La diferencia no es cuánta proteína mutante hay, sino que **no queda K10 salvaje con la que copolimerizar**. Es literalmente la conclusión de los autores: hay que *"alterar el ratio de proteína salvaje a mutante"*.
2. **El umbral murino está entre 0,5 y 1,0; el humano está por debajo de 0,5.** A ratio 0,5 el ratón solo tiene enfermedad focal en patas; el humano con el mismo ratio tiene EI severa generalizada. **Esa es la diferencia de especie, cuantificada**, y se puede defender con datos publicados. Es el argumento que necesitas para tu discusión.

### 2ter.5 Un hueco real en el paper
Por mi lectura del texto completo, el paper caracteriza: (a) el **het germinal con neo** (muy leve), (b) el **homocigoto con neo** (letal), y (c) **quimeras** derivadas de clones ES con neo escindido (lesiones focales en patas). Lo que **no** describe en detalle es el fenotipo completo de una **línea germinal heterocigota limpia (`+/R154C` sin neo)** en todos los sitios corporales y a lo largo de la vida. Si tu línea CRISPR es exactamente eso, **puedes estar llenando un hueco que la literatura dejó abierto desde 2001**. Verifícalo leyendo las figuras del original ([PMC2195990](https://pmc.ncbi.nlm.nih.gov/articles/PMC2195990/)).

### 2ter.6 Si tu alelo es CRISPR + HDR (sin cassette): qué cambia

**La hipótesis del cassette deja de aplicar**, y por tanto tu het "debería" expresar ~50 % de mutante y comportarse como las quimeras de Arin, es decir **con lesiones focales en patas al nacer**. Que no tenga nada es una discrepancia que hay que explicar. Causas específicas de un knock-in CRISPR, por orden de probabilidad:

1. **Mutaciones silenciosas / de bloqueo del PAM en el donador.** Es la práctica estándar para evitar el recorte repetido, y es el **equivalente moderno del cassette de Arin**: pueden romper un *exonic splicing enhancer* o crear un sitio críptico de splicing y bajar o alterar el mRNA. ⚠️ **Por eso hay que secuenciar el cDNA, no solo el gDNA alrededor del corte.**
2. **Indeles o HDR parcial** en el alelo editado, o **deleciones grandes on-target / pérdida de heterocigosidad** en el sitio de corte (bien documentado en embriones editados).
3. **Mosaicismo del fundador**: confirma transmisión germinal y secuencia el alelo transmitido completo.
4. **Integración aberrante del donador** (concatémeros, inserción parcial): número de copias por ddPCR/Southern o lectura larga.
5. **Fondo genético.** Los de Arin eran 129SVJ × C57BL/6. Si el tuyo es B6 puro, los modificadores no son los mismos (§1.2).
6. **Dónde y cuándo has mirado.** Las lesiones de Arin estaban **en las patas, al nacer**, y el fenotipo del het con neo estaba *"restringido a piel expuesta a estrés mecánico"*. Fenotipar dorso piloso de adulto da negativo por diseño.

**Y el enigma de tu homocigoto, que es tu mejor dato.** Un homocigoto CRISPR limpio tendría ratio 1,0 **y ~200 unidades** de proteína mutante — es decir, **más** mutante que el homocigoto letal de Arin (~75 unidades). Debería ser igual o peor, y el tuyo es **viable**. Eso deja pocas salidas: o tu alelo se expresa muy por debajo de lo esperado (vuelta a los puntos 1–4), o el fondo rescata, o tu homocigoto es fenotípicamente más leve que el de Arin por una razón que aún no está descrita. **Cualquiera de las tres es un resultado, y la tercera sería el paper.**

### 2ter.7 Y el detalle químico que sí es específico de R156**C**
R156C introduce una **cisteína libre** en el motivo de iniciación de hélice de 1A. Las queratinas usan puentes disulfuro de forma funcional (p. ej. [los disulfuros dependientes de K14 regulan la homeostasis epidérmica](https://elifesciences.org/articles/53165.pdf)), así que una Cys ectópica puede formar **disulfuros no nativos** y agregados **covalentemente entrecruzados**, resistentes al proteasoma y dependientes de autofagia para su eliminación. Es una diferencia mecanística real frente a R156H (que no aporta tiol) y un ángulo propio y poco explorado. Para verlo: **geles no reductores vs reductores (±DTT/βME)** y fraccionamiento soluble/insoluble.

## 2quater. ¿Por qué vías se degrada una queratina? (y cómo distinguirlas de un problema de expresión)

**Distinción previa, importante:** lo del cassette/desequilibrio alélico ocurre a nivel de **mRNA** (transcripción/estabilidad del transcrito) — en Arin el mutante estaba al 35–40 % *de mRNA*. La degradación proteica es una **hipótesis distinta**. Ambas bajan la proteína mutante efectiva, pero se distinguen con un experimento simple: **ratio alélico de mRNA vs ratio de proteína**. Si el mRNA está 1:1 y la proteína mutante está baja → degradación. Si el mRNA ya está desbalanceado → es expresión, no degradación.

### 2quater.1 Vía ubicuitina–proteasoma (UPS): la mejor documentada
- **Las queratinas son sustrato rutinario del UPS.** El silenciamiento de **Hsp40/DNAJ** en queratinocitos humanos **aumenta** los niveles de K5, K14 y **K10** y **reduce la ubicuitinación** de queratinas **sin cambiar su expresión génica** → Hsp40 dirige queratinas al UPS ([DOI](https://doi.org/10.3892/ijmm.2011.826)).
- **Hay una E3 ligasa descrita específicamente para K10: MDM2.** En infección por VZV, MDM2 se une a KRT10 y lo dirige a degradación **vía ubicuitina–proteasoma**; bloquear la degradación de K10 reduce la propagación viral ([DOI](https://doi.org/10.1016/j.jid.2019.08.448)). Es la referencia más directa para "cómo se degrada K10".
- **La fosforilación es el interruptor.** El E1^E4 de HPV16 provoca **hiperfosforilación + ubicuitinación** de queratinas (incluidas las de diferenciación), dirigiéndolas a degradación proteasomal; y la acumulación de esas estructuras **deteriora la función del proteasoma** ([DOI](https://doi.org/10.1242/jcs.061978)).
- **Evidencia directa en una queratinopatía:** en queratinocitos de pacientes con EBS (*KRT5*), pretratar con el **inhibidor del proteasoma MG132** y con el inhibidor de **p38-MAPK SB203580** **aumentó** la proporción de células con agregados, *"sugiriendo un papel de los proteasomas y de la fosforilación en la eliminación de la queratina mutada"*. Las chaperonas químicas **TMAO y 4-PBA reducían** los agregados, y HSPA1A colocalizaba con K5 fosforilada ([DOI](https://doi.org/10.1038/jid.2011.93)). **Este es el experimento modelo a replicar con tu alelo.**
- **Cullina-3/KLHL24** es otra ruta: mutaciones de ganancia de función en el adaptador de E3 **KLHL24** causan EBS con cardiomiopatía degradando queratinas (K7, K8, K17, K18 y K14) por el proteasoma ([DOI](https://doi.org/10.1093/hmg/ddab318)). Demuestra que una ligasa concreta puede vaciar el pool de queratinas in vivo.

### 2quater.2 Chaperonas y respuesta a proteínas mal plegadas
No es una vía de degradación en sí, pero decide el destino: el knock-in de **K12 L132P** mostró **inducción de genes de chaperonas** y marcadores **apoptóticos de UPR (CHOP, caspasa 12)** con apoptosis ×17 ([DOI](https://doi.org/10.1093/hmg/ddw001)). En el modelo celular de EBS por K14 mutante se indujo **BiP**, fosforilación de c-Jun y apoptosis por caspasas 3 y 8 — y, crucialmente, **los agregados de K14 mutante ubicuitinada suprimían la función del proteasoma 20S en lugar de ser degradados por él** ([DOI](https://doi.org/10.1074/jbc.M307242200)).

### 2quater.3 Autofagia / agrefagia
Es la vía **esperable para agregados grandes** (el proteasoma no procesa agregados insolubles; la ruta canónica es p62/SQSTM1–NBR1 → LC3 → lisosoma), y es complementaria del UPS: en glándula de Harder, la deleción de *Atg7* acumula **proteínas ubicuitinadas y agregados positivos para SQSTM1/p62**, y la inhibición del proteasoma era **más tóxica en células deficientes en autofagia** ([DOI](https://doi.org/10.4161/15548627.2014.978221)). La autofagia es además funcionalmente relevante en queratinocitos ([DOI](https://doi.org/10.1080/15548627.2020.1816342)).
**Pero sé honesta en la tesis:** en mis búsquedas **no he encontrado una demostración directa de aclaramiento de agregados de queratina mutante por autofagia/agrefagia en queratinocitos**. Es una laguna real de la literatura — y por tanto una oportunidad, sobre todo con una mutación que introduce una Cys (§2ter.4).

### 2quater.4 La vía que se olvida y que probablemente domina in vivo: diferenciación terminal
En la epidermis, la K10 de las capas altas **no se degrada: se entrecruza**. La proteómica del corneocito muestra que **K1, K10 y loricrina son componentes prominentes de la envuelta cornificada**, incorporados por transglutaminasas, y que también forman parte de la red de queratina unida por disulfuros del corneocito ([DOI](https://doi.org/10.1021/acs.jproteome.6b00108)). O sea: la ruta principal de "eliminación" de K10 mutante in vivo es **cornificación + descamación**, más la **citólisis de la propia célula afectada**.
Esto tiene una consecuencia de especie directa: Arin señala que **la epidermis murina se renueva cada 8–10 días** ([DOI](https://doi.org/10.1083/jcb.152.3.645)), más rápido que la humana; y los ratones K10−/− muestran **recambio de queratinocitos acelerado** con pérdida de células retenedoras de marca ([DOI](https://doi.org/10.1111/j.0022-202X.2004.23426.x)). Un recambio más rápido = menos tiempo para acumular daño por proteína mutante. **Esta es una vía de "amortiguación murina" que no es degradación proteolítica y que casi nadie discute.**

### 2quater.5 Cómo distinguirlas experimentalmente
| Pregunta | Experimento |
|---|---|
| ¿Expresión o degradación? | **Ratio alélico de mRNA (pirosecuenciación) vs ratio de proteína (Western/MS)** |
| ¿La proteína mutante existe y dónde está? | **Fraccionamiento soluble/insoluble (Tritón → urea/SDS)**. ⚠️ Un Western de RIPA estándar puede "perder" la queratina agregada en el pellet y parecer degradación. Carga siempre la fracción insoluble. |
| ¿Proteasoma o lisosoma/autofagia? | Queratinocitos primarios de tus ratones + **MG132/bortezomib** vs **bafilomicina A1/cloroquina**: cuál rescata la proteína mutante |
| ¿Vida media? | **Chase con cicloheximida**, mutante vs WT |
| ¿Está ubicuitinada? | **IP de K10 + anti-ubicuitina**; y si quieres la ligasa, candidatos MDM2 y adaptadores de cullina-3 |
| ¿Agrefagia? | Colocalización de agregados con **p62/SQSTM1 y LC3**, y flujo de LC3-II |
| ¿Disulfuros por la Cys nueva? | **Geles no reductores vs reductores (±DTT)**; especies de alto peso molecular que colapsan al reducir |
| ¿Chaperonas/UPR? | HSPA1A, BiP, CHOP, caspasa 12; y rescate con **4-PBA o TMAO** |
| ¿Se elimina por recambio/descamación? | Cinética de BrdU/EdU, células retenedoras de marca, grosor y recambio del estrato córneo |

## 3. Catálogo de modelos murinos de EI

### 3.1 Krt10

| # | Modelo | Tipo de alelo | Fenotipo | Ref. |
|---|---|---|---|---|
| 1 | Fuchs, Esteves & Coulombe 1992 | **Transgénico** K10 humana mutante (sobreexpresión) | Fenotipo EHK: citólisis suprabasal, agregación de tonofilamentos, hiperproliferación basal. Primera demostración del mecanismo. | [DOI](https://doi.org/10.1073/pnas.89.15.6906) |
| 2 | Porter et al. 1996 — **Krt10<sup>tm1Tmm</sup>** | Gene targeting que deja una **K10 truncada (K10T)**, no un null limpio | **Homocigotos: fragilidad cutánea severa, mueren al poco de nacer** (deshidratación por ampollas generalizadas). **Heterocigotos: normales al nacer, desarrollan hiperqueratosis con la edad**, sobre todo en patas. | [DOI](https://doi.org/10.1083/jcb.132.5.925) |
| 2b | Caracterización de K10T | — | K10T solo se empareja con K1; K6/K16/K17 forman agregados, no filamentos, y **no compensan**; pérdida total de K2e en planta de homocigotos. | Reichelt et al. 1997, [DOI](https://doi.org/10.1242/jcs.110.18.2175) |
| 2c | Barrera en la línea tm1Tmm | — | TEWL basal ×8 en homocigotos neonatos; heterocigotos adultos con reparación de barrera retardada; esfingomielinasa ácida reducida. Lípidos de SC alterados con ultraestructura lamelar normal. | Jensen et al. 2000, [DOI](https://doi.org/10.1046/j.1523-1747.2000.00103.x); Reichelt et al. 1999, [DOI](https://doi.org/10.1046/j.1523-1747.1999.00702.x) |
| 3 | Reichelt, Büssow, Grund & Magin 2001 — **K10 null verdadero** | Null limpio | **Epidermis neonatal normal**, sin fragilidad ni respuesta de herida. K5/K14 persisten suprabasalmente (a nivel de proteína, no de mRNA) y se forman filamentos K1/K14/K15. | [DOI](https://doi.org/10.1091/mbc.12.6.1557) |
| 3b | K10−/− adulto | Null | **Sin citólisis**; hiperproliferación basal, aumento de tamaño celular, tránsito acelerado, inducción de c-Myc, ciclina D1, 14-3-3σ, K6/K16. | Reichelt & Magin 2002, [DOI](https://doi.org/10.1242/jcs.115.13.2639) |
| 3c | K10−/− y tumores | Null | DMBA/TPA → **menos papilomas** que WT; primer modelo en que perder una queratina reduce tumorigénesis. | Reichelt et al. 2004, [DOI](https://doi.org/10.1111/j.0022-202X.2004.23426.x) |
| 4 | Takahashi & Coulombe 1996 | Transgénico **inducible** (cassette regulable, inducción con éster de forbol) | Fenotipo ampolloso inducible tipo EHK, dependiente de trauma mecánico. | [DOI](https://doi.org/10.1073/pnas.93.25.14776) |
| 5 | **Arin, Longley, Wang & Roop 2001 — knock-in R154C en el locus endógeno de *Krt10* (= R156C humana)** ⚠️ **ESTE ES TU ALELO** | **Knock-in de punto por recombinación homóloga** en el *Krt10* murino: codón 154 Arg→Cys. Dos líneas: `+/mut^neo` (cassette neo retenido) y `+/mut` (neo escindido). Más versión Cre-inducible (CrePR1/RU486) | Ver §2ter — detalle completo. Resumen: la línea **con neo** expresa el alelo mutante al **35–40 %** del WT y tiene fenotipo **muy leve, restringido a piel con estrés mecánico**; sus **homocigotos mueren al nacer** con desintegración del estrato espinoso. Los **quimeras/hets con neo escindido** tienen lesiones queratósicas focales en patas desde el nacimiento. Modelo de **mosaicismo**: las áreas fenotípicas persisten de por vida. | [DOI](https://doi.org/10.1083/jcb.152.3.645); revisión Arin & Roop 2004, [DOI](https://doi.org/10.1159/000079990) |
| 6 | Krt1−/−;Krt10−/− doble KO | Doble null | Letal postnatal por fragilidad. Sorpresa: **la estratificación y la barrera de agua son casi independientes de los filamentos K1/K10**; ausencia total de IF suprabasales, sin compensación por K5/K14; alteración de desmoplaquina, Dsc1, Dsg1 e integridad nuclear. | Wallace et al. 2012, [DOI](https://doi.org/10.1242/jcs.097139) |
| 7 | Krt2−/−;Krt10−/− doble KO | Doble null | **Viables**; acantosis e hiperqueratosis en epidermis interfootpad de la planta; subida masiva de K1, K9 y K16. Demuestra que K2+K10 son los que sostienen la planta murina. | 2015, [DOI](https://doi.org/10.1016/j.jdermsci.2015.10.008) |

### 3.2 Krt1

| # | Modelo | Tipo | Fenotipo | Ref. |
|---|---|---|---|---|
| 1 | Bickenbach et al. 1996 | Transgénico K1 humana con **deleción de 60 residuos en 2B** | Recapitula **las dos fases clínicas**: neonatos con ampollas, adultos con hiperqueratosis escamosa, gránulos de queratohialina irregulares. Efecto dosis-dependiente del transgén. Ampollas en almohadilla plantar pero no en piel pilosa. **Único modelo transgénico que reprodujo la morfología del EHK adulto en su momento.** | [DOI](https://doi.org/10.1046/j.1432-0436.1996.6120129.x) |
| 2 | Serie transgénica de Roop/Rothnagel | Transgénicos K1/K10 mutantes | Revisados en Rothnagel et al. 1993, [DOI](https://doi.org/10.1001/archderm.1993.04540010008001) (ver también Leigh & Lane 1993, PMID 7504434) | — |
| 3 | **Dsk12 (dark skin 12) — Krt1 S194P** | **Missense de punto en el locus endógeno**, mutagénesis química, **dominante** | **Heterocigotos afectados**: a los 2 días ampollas y erosiones intraepidérmicas en zonas de trauma, a las 2 semanas hiperqueratosis significativa; hiperpigmentación de almohadillas. Recapitula EHK humano en patología macro, histología y genética. **Es el mejor "verdadero" modelo murino de EI dominante.** | McGowan et al. 2006, [DOI](https://doi.org/10.1038/sj.jid.5700241) |
| 4 | Krt1−/− (Roth et al. 2012) | Null | **Letalidad perinatal**, defecto de barrera, aumento prenatal de **IL-18, S100A8/A9**; el rescate parcial con depleción de IL-18 coloca a K1 **aguas arriba de una red inflamatoria**; firma transcriptómica parecida a eccema atópico y psoriasis (y distinta de la de Krt5−/−/EBS). | [DOI](https://doi.org/10.1242/jcs.116574) |
| 5 | Krt1−/−;Krt10−/− | Doble null | Ver arriba. | [DOI](https://doi.org/10.1242/jcs.097139) |

### 3.3 En el espectro EI (útiles como comparadores)
- **Dsk10 — mutación en *Krt2e*** (misma pantalla de mutagénesis de Barsh): modelo del extremo "EI superficial"/ichtiosis bullosa de Siemens.
- ***Krt2−/−***: existe y se usó para el doble KO con *Krt10* ([DOI](https://doi.org/10.1016/j.jdermsci.2015.10.008)).
- ***Krt77−/−***: sin fenotipo cutáneo, rescatado por subida de K1 ([DOI](https://doi.org/10.1016/j.bbamcr.2024.119881)).
- Fuera de queratinas pero con histología confundible con EHK: **plakoglobina−/−** ([DOI](https://doi.org/10.1006/dbio.1996.0346)).
- Nota de recursos: MGI lista decenas de alelos de *Krt10* (muchos de consorcios tipo IMPC, sin fenotipado cutáneo dermatológico publicado). Para el censo definitivo: consulta directa de **MGI** (alleles de Krt10 y Krt1) e **IMSR**; la cepa `Balb/c.Cg-Krt10<tm1Tmm>/H` está en el MRC Harwell/National Mouse Archive.

### 3.4 Conclusión del censo
- Cantidad total: **~12 modelos** relevantes.
- **CORRECCIÓN IMPORTANTE:** sí existe un knock-in de punto en el locus endógeno de *Krt10* que reproduce la mutación dominante humana más frecuente: **Arin et al. 2001, R154C murina = R156C humana** ([DOI](https://doi.org/10.1083/jcb.152.3.645)). Una versión previa de este documento afirmaba lo contrario; era incorrecto. Esto **elimina la novedad de "primer knock-in de R156C"** y obliga a reposicionar cualquier modelo nuevo de ese alelo (§2ter).
- **Lo que sí falta**: un modelo de **EI recesiva humana** que recapitule la severidad humana (el null murino es demasiado leve); y un alelo R156C **viable en homocigosis** utilizable como banco de pruebas terapéutico — los homocigotos de Arin mueren al nacer.

---

## 4. "El KO de K10": aclara con cuál te comparas

Esto es importante porque buena parte de la confusión bibliográfica viene de aquí:

| | **Krt10<sup>tm1Tmm</sup>** (Porter 1996) | **K10 null** (Reichelt 2001) |
|---|---|---|
| Alelo | Produce **K10 truncada (K10T)** que se incorpora al filamento → comportamiento **dominante-negativo parcial** | **Null limpio**, sin proteína |
| Homocigoto | Fragilidad severa, **letal neonatal**, TEWL ×8 | **Viable**, epidermis neonatal normal, adulto con hiperproliferación **sin citólisis** |
| Heterocigoto | **Desarrolla hiperqueratosis con la edad** | Sin fenotipo descrito |
| Paralelo humano | EI dominante | Portador humano KRT10-null → normal; homocigoto humano → severo (**discordante con el ratón**) |

**Dos conclusiones prácticas para ti:**
1. Si tu homocigoto es **viable con fenotipo**, se parece al null de Reichelt, no al tm1Tmm — y eso refuerza la hipótesis "mi alelo es pérdida de función".
2. El contraste tm1Tmm vs. null es la prueba de concepto de que **en el mismo gen y la misma especie, el tipo de alelo decide el fenotipo mucho más que la especie**. Es el argumento central que necesitas para tu discusión.

---

## 5. Cómo distinguir experimentalmente "mi mutación" de "la especie"

Orden de prioridad, de más informativo y barato a más costoso:

> Nota: si tu alelo es una mutación causante de EI (missense dominante), lee esto junto con **§2bis.3**, que ordena las tres hipótesis específicas para ese caso. El bloque A sigue siendo el primer paso.

**A. Caracterizar el alelo (imprescindible, y responde el 80% de la pregunta)**
1. **¿Hay mRNA mutante, y en qué proporción respecto al WT?** RT-qPCR/pirosecuenciación **alelo-específica** en piel. Un ratio mutante:WT <1 (cassette residual, splicing alterado) explicaría el het normal sin invocar nada de especie — es la hipótesis nº1 de §2bis.3.
2. **¿Hay proteína mutante, y a qué nivel?** Western con anticuerpo pan-K10, y si es posible detección específica de la forma mutante; cuantificar K10 total en het vs WT vs homo. En EI dominante humana la clave es que la mutante **se expresa e incorpora**.
3. **¿Se incorpora al filamento o se agrega?** Inmunofluorescencia + **inmuno-EM / doble inmunogold** (como hicieron con K10T, [DOI](https://doi.org/10.1242/jcs.110.18.2175)). Si no hay agregados de tonofilamentos, no hay dominante-negativo, punto.
4. **¿Splicing aberrante?** RT-PCR de la región + secuenciación del amplicón. Un sitio donador "leaky" cambia toda la interpretación (es el mecanismo propuesto en los fenotipos humanos autolimitados).
5. **Conservación del residuo**: alinea K10 humana vs. murina en la posición mutada y su contexto (motivos de frontera de hélice, L12 linker). Si el residuo o su entorno no está conservado, tienes un argumento directo de "en ratón esta mutación no es equivalente" — y un paper de 2024 sobre variantes del **linker L12 de KRT10** te da marco para discutir dominio-dependencia del fenotipo.

**B. Desenmascarar el fenotipo (si A dice que sí hay proteína mutante)**
6. **Sitio corporal**: no te quedes en dorso. Fenotipa **almohadillas plantares, planta interfootpad, oreja, cola (escama vs. interescama)** — ahí cambian K2, K9 y la protección folicular. Bickenbach vio ampollas en footpad y no en piel pilosa ([DOI](https://doi.org/10.1046/j.1432-0436.1996.6120129.x)).
7. **Estrés mecánico controlado**: tape stripping, fricción estandarizada, herida por punch. Las queratinopatías murinas son fenotipos de estrés, no constitutivos (Bouameur & Magin 2017, [DOI](https://doi.org/10.1007/978-3-319-49674-0_7)).
8. **TPA/éster de forbol tópico**: es lo que usó Coulombe para inducir el fenotipo en su modelo inducible ([DOI](https://doi.org/10.1073/pnas.93.25.14776)).
9. **Curva temporal**: el fenotipo del het tm1Tmm **aparece con la edad**. Si solo has mirado neonatos/jóvenes, mira a 6–12 meses.
10. **Barrera**: TEWL basal y reparación tras disrupción, hidratación de SC, dye exclusion, perfil de ceramidas. Los hets tm1Tmm eran "normales" clínicamente pero tenían **reparación de barrera retardada** ([DOI](https://doi.org/10.1046/j.1523-1747.2000.00103.x)). Un fenotipo subclínico sigue siendo un fenotipo publicable.
11. **Fondo genético**: cruza a un segundo fondo (p. ej. C57BL/6 ↔ BALB/c o FVB). Los mutantes de queratina cambian de letal a casi-normal según fondo ([DOI](https://doi.org/10.1385/1-59745-165-7:203)); si tu het aparece en otro fondo, has encontrado un modificador y eso es un paper en sí.
12. **Sensibilización por dosis**: cruza tu alelo contra *Krt10*<sup>+/−</sup> (hemicigosis: alelo mutante + null) y contra *Krt1*<sup>+/−</sup>. Si el fenotipo aparece, confirmas dominante-negativo dependiente de dosis relativa. Y cruza contra *Krt77*<sup>−/−</sup> o *Krt2*<sup>−/−</sup> para quitar la amortiguación específica de ratón — este es el experimento que **mide directamente cuánta de la diferencia es de especie**.
13. **Compensadores**: cuantifica K5/K14/K15 suprabasales, K6/K16/K17, K1, K2, K9, K77 por sitio. Si tu homocigoto sube K5/K14 suprabasal como el null de Reichelt, ya tienes el mecanismo de tolerancia murina.

**C. Puentes a humano**
14. Queratinocitos humanos (de paciente si los hay, o HaCaT/iPSC-keratinocytes editados con la misma variante) y **organotípicos 3D**: compara el mismo cambio de aminoácido en contexto humano vs. murino. Es la prueba limpia de "especie, no alelo".

---

## 6. Qué hace que un modelo murino de EI sea publicable e *interesante*

### 6.1 Requisitos mínimos (el "umbral de entrada")
- **Causalidad genética establecida**: alelo definido a nivel de secuencia, en el locus endógeno idealmente, con expresión a nivel fisiológico. Sobreexpresión transgénica ya no se acepta bien como modelo de enfermedad dominante en 2026 — los transgénicos de los 90 fueron pioneros, pero el estándar actual es knock-in/CRISPR.
- **Hallmarks morfológicos de EI demostrados**, no solo "piel escamosa":
  - histología: hiperqueratosis, acantosis, **citólisis suprabasal**, gránulos de queratohialina irregulares;
  - **ultraestructura (TEM) con agregación/clumping de tonofilamentos** — en EI esto es el criterio diagnóstico, y el inmuno-EM que demuestra que los agregados contienen K1/K10 es el estándar de la literatura;
  - inmunofluorescencia de la red de filamentos.
- **Función de barrera cuantificada**: TEWL, dye exclusion, hidratación de SC, idealmente lípidos/ceramidas.
- **Perfil de compensación** de queratinas (K6/K16/K17, K5/K14, K2, K9) por sitio y edad.
- **Rigor**: littermate controls, fondo genético declarado y puro, ambos sexos, curso temporal, n adecuado y potencia, ciego en la evaluación histológica, cumplimiento **ARRIVE 2.0**, aprobación ética.
- **Disponibilidad**: alelo registrado en **MGI** con nomenclatura correcta y cepa depositada (EMMA/INFRAFRONTIER, JAX o MRC Harwell). Un modelo que nadie puede pedir se cita poco.

### 6.2 Qué lo convierte en *interesante* (el "valor añadido")
Necesitas al menos **uno** de estos, y lo ideal es dos:

1. **Mecanismo, no descripción.** Los papers de modelos de queratina que más se citan no dicen "hice un ratón que se parece a la enfermedad", dicen *por qué*: K1 aguas arriba de IL-18/S100A8/A9 e inflamación tipo eccema/psoriasis ([DOI](https://doi.org/10.1242/jcs.116574)); K10 regulando proliferación vía c-Myc ([DOI](https://doi.org/10.1242/jcs.115.13.2639)); K1/K10 dispensables para estratificación y barrera de agua pero necesarios para desmosomas y la integridad nuclear ([DOI](https://doi.org/10.1242/jcs.097139)).
2. **Explicar variabilidad clínica humana.** Dominante vs. recesiva, EI anular, EI superficial, autolimitada, ichtiosis with confetti. Un modelo que explique *por qué* una variante concreta da un fenotipo concreto encaja con la línea de trabajo de "residuos expuestos en superficie de K10 y base estructural de la variación fenotípica".
3. **Plataforma preclínica.** Esto es lo que hoy más se valora, y es donde la EI tiene demanda real: edición génica alelo-específica (CRISPR/base editing, TALEN sobre el alelo mutante), siRNA/ASO alelo-específicos, con la lógica de que la **supresión parcial del alelo mutante puede bastar** porque el heterocigoto null es normal. Hay precedentes directos en el campo (TALEN sobre *KRT10* en queratinocitos de paciente y xenoinjerto; siRNA alelo-específico en K12 corneal) pero **no un modelo murino de knock-in endógeno con eficacia tópica demostrada**. Un modelo con **fenotipo medible, cuantificable y reversible** vale mucho más que un modelo severo-letal.
4. **Mosaicismo y células madre.** El modelo inducible por Cre de Arin & Roop convirtió un modelo en un hallazgo conceptual (ausencia de presión selectiva contra mutaciones de K10 en células madre epidérmicas → por qué existen formas en mosaico de EHK y no de EBS) ([DOI](https://doi.org/10.1083/jcb.152.3.645)).
5. **Resolver una discrepancia de la literatura.** Si tu alelo da un fenotipo que contradice al de las líneas existentes, y lo explicas, eso es publicable per se.
6. **Fenotipo controlable**: inducible, sitio-específico, o adulto en vez de letal neonatal. Los modelos letales perinatales (Krt1−/−, Krt10 tm1Tmm homo, doble KO) **limitan todo estudio terapéutico**. Un homocigoto **viable con fenotipo**, como el tuyo, es precisamente lo que la comunidad necesita y lo que esos modelos no dan.

### 6.3 ¿Aporta publicar "otro KO de K10 con fenotipo distinto"?
- **Como KO a secas: no.** Hay dos líneas publicadas y ~8 papers de caracterización. Un tercer null sin más es incremental.
- **Sí aporta, y bastante, si el ángulo es uno de estos:**
  - **"Mismo gen, alelos distintos, fenotipos distintos"**: comparar de frente tu alelo con el null y con K10T y mostrar la relación estructura-alelo-fenotipo. Es el marco que la literatura ya validó y tú tendrías el tercer punto de la curva.
  - **Modelo de EI recesiva humana**: tu genética (het normal, homo afectado) es la genética de la EI recesiva, y **no hay un buen modelo murino de EI recesiva** que reproduzca la severidad humana. Si tu homocigoto es más severo que el null de Reichelt, eso es novedad; si es más leve, la novedad es el mecanismo de tolerancia.
  - **Homocigoto viable como plataforma terapéutica** (ver 6.2.3) — justo porque los demás se mueren.
  - **Modificadores de fondo genético**, si el fenotipo cambia al cambiar de fondo.
  - **Biología nueva**: inflamación/IL-18, autofagia y proteostasis, microbioma cutáneo, envejecimiento, carcinogénesis (hay precedente: K10−/− hace **menos** tumores, [DOI](https://doi.org/10.1111/j.0022-202X.2004.23426.x)).

### 6.4 Mi recomendación sobre cómo encuadrar tu paper
No lo plantees como "modelo murino de EI" (competirías con Dsk12 y con 10 modelos previos). Plantéalo como:

> **"Knock-in de la mutación [X] de *Krt10*: la dominancia en la ichtiosis epidermolítica es dependiente de umbral y está amortiguada en el ratón."**

Eso convierte tu "problema" (het sin fenotipo) en el **resultado central**, usa el homocigoto viable como la herramienta que los modelos letales no ofrecen, y hace del cruce *Krt10*<sup>mut/−</sup> / *Krt77*<sup>−/−</sup> / *Krt2*<sup>−/−</sup> el experimento que **cuantifica** qué parte es especie y qué parte es alelo. Es un paper mecanístico con mensaje, no un modelo descriptivo más.

Y usa el precedente de K12 L132P ([DOI](https://doi.org/10.1093/hmg/ddw001)) explícitamente en la discusión: te da cobertura bibliográfica para la limitación (fenotipo en homocigosis) y el encuadre que los revisores ya aceptaron en *Hum Mol Genet* — "banco de pruebas para terapias de queratinopatías causadas por mutaciones similares". Refuerza mucho el argumento si, como hicieron ellos, **validas en tejido/queratinocitos de paciente** con la misma mutación.

---

## 7. Lagunas y advertencias sobre esta revisión

- **No he podido confirmar** la existencia de un knock-in de punto publicado en el locus endógeno de *Krt10* que modele una mutación dominante humana. Antes de afirmarlo en tu tesis, haz una consulta directa en **MGI (alelos de Krt10)** e **IMSR**, y una búsqueda en bioRxiv — el servidor de bioRxiv no estaba accesible en esta sesión.
- El paper de **Frommherz et al. 2019 (Br J Dermatol)** sobre EI autolimitada por *KRT10* bialélico está marcado como **publicación retractada** en PubMed. No lo cites como evidencia primaria.
- El **censo exacto de modelos** depende de dónde pongas el límite (¿cuentan los dobles KO? ¿los transgénicos de los 90? ¿los alelos IMPC sin fenotipado dermatológico?). He dado el rango y el criterio.
- Para el *Krt2−/−* no he localizado el paper original de generación de la línea; está confirmado indirectamente por el cruce *Krt2−/−;Krt10−/−*.

---

## 8. Bibliografía (orden de uso)

Toda la bibliografía se recuperó de **PubMed**.

**Humano / genética de EI**
1. Müller FB, Huber M, et al. A human keratin 10 knockout causes recessive epidermolytic hyperkeratosis. *Hum Mol Genet* 2006. [DOI](https://doi.org/10.1093/hmg/ddl028)
2. Choate KA, Lu Y, Zhou J, et al. Mitotic recombination in patients with ichthyosis causes reversion of dominant mutations in KRT10. *Science* 2010;330:94-7. [DOI](https://doi.org/10.1126/science.1192280)
3. Burger B, Spoerri I, et al. Natural course and clinical manifestations of ichthyosis with confetti caused by a novel KRT10 mutation. *Br J Dermatol* 2012;166:434-9. [DOI](https://doi.org/10.1111/j.1365-2133.2011.10639.x)
4. Frommherz L, et al. Skin fragility caused by biallelic KRT10 mutations: self-improving epidermolytic ichthyosis. *Br J Dermatol* 2020;182:780-5. **[RETRACTADO]** [DOI](https://doi.org/10.1111/bjd.18325)
5. Leigh IM, Lane EB. Mutations in the genes for epidermal keratins in epidermolysis bullosa and epidermolytic hyperkeratosis. *Arch Dermatol* 1993;129:1571-7. PMID 7504434
6. Jonkman MF, et al. Effects of keratin 14 ablation... *J Invest Dermatol* 1996;107:764-9 — contiene la observación de que **"el pronóstico de la ablación de K14 es mucho mejor en humano que en ratón"**, un precedente explícito de diferencia de especie en queratinopatías. [DOI](https://doi.org/10.1111/1523-1747.ep12365805)

**Comparativa humano / ratón**
7. Herzog F, Winter H, Schweizer J. The large type II 70-kDa keratin of mouse epidermis is the ortholog of human keratin K2e. *J Invest Dermatol* 1994;102:165-70. [DOI](https://doi.org/10.1111/1523-1747.ep12371757)
8. Takahashi K, Yan B, et al. The two functional keratin 6 genes of mouse... evolved independently from their human orthologs. *Genomics* 1998;53:170-83. [DOI](https://doi.org/10.1006/geno.1998.5476)
9. The loss of keratin 77 in murine skin is functionally compensated by keratin 1. *Biochim Biophys Acta Mol Cell Res* 2025. [DOI](https://doi.org/10.1016/j.bbamcr.2024.119881)
10. Vijayaraj P, Söhl G, Magin TM. Keratin transgenic and knockout mice: functional analysis and validation of disease-causing mutations. *Methods Mol Biol* 2007;360:203-51. [DOI](https://doi.org/10.1385/1-59745-165-7:203)
11. Bouameur JE, Magin TM. Lessons from animal models of cytoplasmic intermediate filament proteins. *Subcell Biochem* 2017;82:171-230. [DOI](https://doi.org/10.1007/978-3-319-49674-0_7)

**Modelos K10**
12. Fuchs E, Esteves RA, Coulombe PA. Transgenic mice expressing a mutant keratin 10 gene reveal the likely genetic basis for epidermolytic hyperkeratosis. *PNAS* 1992;89:6906-10. [DOI](https://doi.org/10.1073/pnas.89.15.6906)
13. Porter RM, et al. Gene targeting at the mouse cytokeratin 10 locus: severe skin fragility and changes of cytokeratin expression. *J Cell Biol* 1996;132:925. [DOI](https://doi.org/10.1083/jcb.132.5.925)
14. Reichelt J, et al. Out of balance: consequences of a partial keratin 10 knockout. *J Cell Sci* 1997;110:2175. [DOI](https://doi.org/10.1242/jcs.110.18.2175)
15. Reichelt J, Doering T, et al. Normal ultrastructure, but altered stratum corneum lipid and protein composition in a mouse model for epidermolytic hyperkeratosis. *J Invest Dermatol* 1999;113:329-34. [DOI](https://doi.org/10.1046/j.1523-1747.1999.00702.x)
16. Jensen JM, Schütze S, et al. Impaired cutaneous permeability barrier function, skin hydration, and sphingomyelinase activity in keratin 10 deficient mice. *J Invest Dermatol* 2000;115:708-13. [DOI](https://doi.org/10.1046/j.1523-1747.2000.00103.x)
17. Reichelt J, Büssow H, Grund C, Magin TM. Formation of a normal epidermis supported by increased stability of keratins 5 and 14 in keratin 10 null mice. *Mol Biol Cell* 2001;12:1557. [DOI](https://doi.org/10.1091/mbc.12.6.1557)
18. Reichelt J, Magin TM. Hyperproliferation, induction of c-Myc and 14-3-3σ, but no cell fragility in keratin-10-null mice. *J Cell Sci* 2002;115:2639. [DOI](https://doi.org/10.1242/jcs.115.13.2639)
19. Reichelt J, et al. Loss of keratin 10 leads to MAPK activation, increased keratinocyte turnover, and decreased tumor formation in mice. *J Invest Dermatol* 2004. [DOI](https://doi.org/10.1111/j.0022-202X.2004.23426.x)
20. Takahashi K, Coulombe PA. A transgenic mouse model with an inducible skin blistering disease phenotype. *PNAS* 1996;93:14776-81. [DOI](https://doi.org/10.1073/pnas.93.25.14776)
21. Arin MJ, Roop DR (Cao T, et al.). Focal activation of a mutant allele defines the role of stem cells in mosaic skin disorders. *J Cell Biol* 2001;152:645. [DOI](https://doi.org/10.1083/jcb.152.3.645)
22. Arin MJ, Roop DR. Inducible mouse models for inherited skin diseases: implications for skin gene therapy. *Cells Tissues Organs* 2004;177:160-8. [DOI](https://doi.org/10.1159/000079990)
23. Wallace L, et al. Deletion of K1/K10 does not impair epidermal stratification but affects desmosomal structure and nuclear integrity. *J Cell Sci* 2012;125. [DOI](https://doi.org/10.1242/jcs.097139)
24. Keratins K2 and K10 are essential for the epidermal integrity of plantar skin. *J Dermatol Sci* 2015. [DOI](https://doi.org/10.1016/j.jdermsci.2015.10.008)

**Modelos K1**
25. Bickenbach JR, Longley MA, et al. A transgenic mouse model that recapitulates the clinical features of both neonatal and adult forms of epidermolytic hyperkeratosis. *Differentiation* 1996;61:129-39. [DOI](https://doi.org/10.1046/j.1432-0436.1996.6120129.x)
26. McGowan KA, Aradhya S, Fuchs H, Hrabé de Angelis M, Barsh GS. A mouse keratin 1 mutation causes dark skin and epidermolytic hyperkeratosis. *J Invest Dermatol* 2006;126:1013-6. [DOI](https://doi.org/10.1038/sj.jid.5700241)
27. Roth W, et al. Keratin 1 maintains skin integrity and participates in an inflammatory network in skin through interleukin-18. *J Cell Sci* 2012;125:5269. [DOI](https://doi.org/10.1242/jcs.116574)
28. Rothnagel JA, Greenhalgh DA, et al. Transgenic models of skin diseases. *Arch Dermatol* 1993;129:1430-6. PMID 7694550

**Dominancia dependiente de dosis / knock-ins de mutaciones dominantes (§2bis)**
29. Allen EHA, Courtney DG, Atkinson SD, et al. (lab. McLean/Moore). Keratin 12 missense mutation induces the unfolded protein response and apoptosis in Meesmann epithelial corneal dystrophy. *Hum Mol Genet* 2016;25:1176-91. **Precedente clave: knock-in humanizado de una mutación dominante con fenotipo en homocigotos, publicado y defendido como banco de pruebas terapéutico.** [DOI](https://doi.org/10.1093/hmg/ddw001)
30. Garcia M, et al. Development of skin-humanized mouse models of pachyonychia congenita — *KRT6A* N171K: piel regenerada fenotípicamente normal que solo manifiesta PC tras tape stripping. [PubMed 21150925](https://pubmed.ncbi.nlm.nih.gov/21150925/)
31. [OMIM *KRT14* (148066)](https://omim.org/entry/148066) — mutación descrita como *partial dominant*: heterocigotos leves/localizados, homocigotos severos.

**Degradación y proteostasis de queratinas (§2quater)**
32. Yamazaki S, Uchiumi A, Katagata Y. Hsp40 regulates the amount of keratin proteins via ubiquitin-proteasome pathway in cultured human cells. *Int J Mol Med* 2012;29:165-8. [DOI](https://doi.org/10.3892/ijmm.2011.826)
33. Tommasi C, Rogerson C, et al. Kallikrein-mediated cytokeratin 10 degradation is required for varicella zoster virus propagation in skin. *J Invest Dermatol* 2020;140:774-784 — **MDM2 ubicuitina K10 y lo dirige al proteasoma**. [DOI](https://doi.org/10.1016/j.jid.2019.08.448)
34. McIntosh PB, et al. E1^E4-mediated keratin phosphorylation and ubiquitylation. *J Cell Sci* 2010;123:2810-22. [DOI](https://doi.org/10.1242/jcs.061978)
35. Chamcheu JC, Navsaria H, et al. Chemical chaperones protect EBS keratinocytes from heat stress-induced keratin aggregation: involvement of HSPs and MAP kinases. *J Invest Dermatol* 2011;131:1684-91 — **MG132 y SB203580 aumentan agregados; TMAO y 4-PBA los reducen**. [DOI](https://doi.org/10.1038/jid.2011.93)
36. Logli E, et al. Proteasome-mediated degradation of keratins 7, 8, 17 and 18 by mutant KLHL24. *Hum Mol Genet* 2022;31:1308-24. [DOI](https://doi.org/10.1093/hmg/ddab318)
37. Yoneda K, et al. An autocrine/paracrine loop linking keratin 14 aggregates to TNFα-mediated cytotoxicity. *J Biol Chem* 2004;279:7296-303 — los agregados **inhiben** el proteasoma 20S en lugar de ser degradados. [DOI](https://doi.org/10.1074/jbc.M307242200)
38. Koenig U, et al. Autophagy facilitates secretion and protects against degeneration of the Harderian gland. *Autophagy* 2015;11:298-313 — complementariedad UPS/autofagia, agregados p62⁺. [DOI](https://doi.org/10.4161/15548627.2014.978221)
39. Qiang L, et al. Keratinocyte autophagy enables the activation of keratinocytes and fibroblasts and facilitates wound healing. *Autophagy* 2021;17:2128-43. [DOI](https://doi.org/10.1080/15548627.2020.1816342)
40. Proteomic analysis of loricrin knockout mouse epidermis. *J Proteome Res* 2016 — K1, K10 y loricrina como componentes prominentes de la envuelta cornificada. [DOI](https://doi.org/10.1021/acs.jproteome.6b00108)
41. [Keratin 14-dependent disulfides regulate epidermal homeostasis — eLife](https://elifesciences.org/articles/53165.pdf)

**Comparadores**
42. Bierkamp C, et al. Embryonic heart and skin defects in mice lacking plakoglobin. *Dev Biol* 1996;180:780-5. [DOI](https://doi.org/10.1006/dbio.1996.0346)
43. Ness SL, et al. Mouse keratin 4 is necessary for internal epithelial integrity. *J Biol Chem* 1998;273:23904-11. [DOI](https://doi.org/10.1074/jbc.273.37.23904)

**Recursos web consultados**
- [MGI — Krt1 (MGI:96698)](https://www.informatics.jax.org/marker/MGI:96698)
- [MRC Harwell National Mouse Archive — Balb/c.Cg-Krt10tm1Tmm/H](https://archive.har.mrc.ac.uk/stock?id=3154)
- [Gene editing–mediated disruption of EI-associated KRT10 alleles restores filament stability in keratinocytes — J Invest Dermatol](https://www.jidonline.org/article/S0022-202X(19)31475-7/fulltext)
- [Mutations affecting keratin 10 surface-exposed residues highlight the structural basis of phenotypic variation in EI — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0022202X15601518)
- [Variants in the L12 linker domain of KRT10 are causal to atypical epidermolytic ichthyosis (2024)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11484123/)
- [Current strategies for the gene therapy of ichthyosis (revisión)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8910354/)
- [Differential evolution of the epidermal keratin cytoskeleton in terrestrial and aquatic mammals — Mol Biol Evol](https://academic.oup.com/mbe/article/36/2/328/5184281)
