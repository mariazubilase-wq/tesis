# Búsqueda de novedad — paper K1/K10

> Evaluación bibliográfica del plan `plan_paper_K1_K10.md`.
> Fuente: PubMed (vía MCP) + búsqueda web. Fecha: 2026-10-08.
> **Atribución: la información bibliográfica de este documento proviene de PubMed.**

---

## Resumen ejecutivo

**El marco conceptual central del plan está publicado desde 1988–1989, en dos
papers que el plan no cita.** Y el "dato que vertebra el paper" —que añadir una
queratina tipo I reduce el pool endógeno preexistente— también tiene precedente
directo en 1989.

Esto **no mata el paper**, pero obliga a reescribir §1 (tesis), §2 (bibliografía)
y los títulos candidatos. Lo que queda novedoso es real y publicable, pero es
**la vía, la cuantificación y la jerarquía de partners**, no el concepto.

Además, dos de los cuatro puntos que el plan lista como "NO descrito — tu hueco
real" (§2) son **incorrectos**: existe literatura abundante, y en un caso un
paper que **contradice** el modelo propuesto.

---

## 1. Los dos precedentes críticos que faltan en el plan

### 🔴 Kulesh DA, Ceceña G, Darmon YM, Vasseur M, Oshima RG (1989)
*Posttranslational regulation of keratins: degradation of mouse and human
keratins 18 and 8.* Mol Cell Biol 9:1553–65.
[DOI](https://doi.org/10.1128/mcb.9.4.1553-1565.1989) · PMC362572

Según PubMed, textualmente:

- K18 expresada sola en fibroblastos → *"K18 protein which is degraded relatively
  rapidly without the formation of filaments"*.
- K8 sola → *"degraded in a fashion similar to that seen previously for K18"*.
- K8 + K18 → *"resulted in stabilization of both K18 and K8"*, con filamentos
  normales. Conclusión: un tipo I + un tipo II es *"both necessary and sufficient"*.
- **Y lo decisivo:** un K18 **truncado** (sin la cola C-terminal y sin una región
  del rod) expresado en células endodérmicas parietales **que sí expresan
  queratinas** → *"resulted in destabilization of endogenous Endo A and Endo B
  and inhibition of the formation of typical keratin filament structures"*.
- Conclusión del paper: *"cells that normally express keratins contain a
  proteolytic system similar to that found in experimentally manipulated
  fibroblasts which degrades keratin proteins **not found in their normal
  polymerized state**"*.

**Qué pre-empta, punto por punto:**

| Elemento del plan | Estado |
|---|---|
| Fig. 2 — el sobredisparo: añadir queratina tipo I baja el pool endógeno | **Descrito** (con truncado, 1989) |
| Fig. 6 — "lo que protege es la incorporación al filamento, no la unión" | **Descrito** ("not found in their normal polymerized state") |
| Marco de "vigilancia" de queratinas no ensambladas | **Descrito** ("a proteolytic system... which degrades") |
| Degradación *en trans* del pool endógeno preexistente | **Descrito** |

**Consecuencia grave para el control del tag (§6 del plan).** El constructo de
Kulesh que desestabilizaba el pool endógeno era un K18 **sin cola C-terminal**.
El constructo disponible es K1-Myc-DDK, con el tag en C-terminal **tapando la
cola de K1**. Un revisor que conozca Kulesh 1989 dirá: *"lo que ves es tu tag
reproduciendo el experimento del truncado de 1989"*. El control del tag deja de
ser "urgente" y pasa a ser **bloqueante**: sin K1 sin tag (o con tag N-terminal),
la figura estrella es indistinguible de ese artefacto.

### 🔴 Domenjoud L, Jorcano JL, Breuer B, Alonso A (1988)
*Synthesis and fate of keratins 8 and 18 in nonepithelial cells transfected with
cDNA.* Exp Cell Res 179:352–61.
[DOI](https://doi.org/10.1016/0014-4827(88)90274-1)

Frase final del abstract, según PubMed:

> *"These results demonstrate that **assembly in heterocomplexes stabilizes
> keratins against cellular degradation**, helping to explain why **excess pools
> of simple keratins have never been detected**."*

Eso es, literalmente, la tesis "la cantidad de queratina no la fija su expresión
sino la disponibilidad de partner". En 1988.

También: expresadas individualmente K8 y K18 *"failed to polymerize... but formed
granular aggregates"*, y *"the expression of one of these two keratins did not
induce the synthesis of its partner"* (relevante: descarta inducción
compensatoria del partner, un control que el plan no contempla).

**Por tanto el título candidato #1 del plan** —*"Partner supply, not expression,
sets keratin 1 abundance"*— **es casi la frase de Domenjoud 1988.** Hay que
reformularlo.

---

## 2. Correcciones a §2 "NO descrito — tu hueco real"

El plan lista cuatro huecos. Dos son falsos, dos se sostienen.

### ❌ "Degradación de queratinas por autofagia/p62 en queratinocitos: búsqueda sin resultados"

`keratin AND autophagy` en PubMed = **146 resultados**. Hay un campo consolidado
de autofagia en queratinocitos (grupos de Eckhart/Tschachler en Viena, de
Hoste/van Loo en Gante). Decir "sin resultados" en un manuscrito sería fatal.

Y el paper más directamente relevante **va en contra del modelo del plan**:

**Jaeger K, Sukseree S, Zhong S, ... Rice RH, Eckhart L (2019).** *Cornification
of nail keratinocytes requires autophagy for bulk degradation of intracellular
proteins while sparing components of the cytoskeleton.* Apoptosis 24:62–73.
[DOI](https://doi.org/10.1007/s10495-018-1505-4) · PMC6373260

Según PubMed: Atg7 deletado en epitelios K14+, proteómica de uña corneificada.
Resultado textual: *"the amounts of cytoskeletal proteins of the keratin and
keratin-associated protein families, cytolinker proteins and desmosomal proteins
were **either unaltered or decreased** in nails of mice lacking epithelial
autophagy"*. Lo que sí se acumula es *"a broad range of enzymes"*, y sobre todo
*"the subunits of the proteasome and of the TRiC/CCT chaperonin"*. Conclusión:
*"its substrate specificity depends on the **accessibility of proteins outside of
the cytoskeleton**"*.

Traducción: **hay publicado que las queratinas NO son sustrato de autofagia** —
que la autofagia en corneificación perdona el citoesqueleto.

Esto es a la vez el mayor riesgo de la Fig. 3 y su mejor oportunidad. El
experimento de Jaeger es **corneificación normal, in vivo, en uña**. El del plan
es **desbalance de partner, en cultivo, con queratina huérfana**. Son condiciones
distintas y la distinción es defendible — pero hay que plantearla de frente en el
manuscrito, antes de que la plantee el revisor. "No hay nada publicado" no es una
opción.

### ❌ "Búsqueda sobre E3 ligasas de queratinas → si puedes nombrar la ligasa, subes otro escalón de revista"

**La ligasa ya está nombrada, y en Nature Genetics.**

- **Lin Z, Li S, Feng C, ... Yang Y, Tan X (2016).** *Stabilizing mutations of
  KLHL24 ubiquitin ligase cause loss of keratin 14 and human skin fragility.*
  Nat Genet 48:1508–16. [DOI](https://doi.org/10.1038/ng.3701)
  → KLHL24 es el receptor de sustrato de una ligasa cullin3–RBX1. Mutaciones de
  codón de inicio dan KLHL24-ΔN28, más estable por abolición de la
  autoubiquitinación. *"We have further identified keratin 14 (KRT14) as a KLHL24
  substrate and found that KLHL24-ΔN28 induces excessive ubiquitination and
  degradation of KRT14."* Confirmado en ratón knock-in. Fenotipo: epidermolisis
  bullosa.

- **Logli E, Marzuolo E, D'Agostino M, ... Condorelli AG (2022).**
  *Proteasome-mediated degradation of keratins 7, 8, 17 and 18 by mutant KLHL24
  in a foetal keratinocyte model.* Hum Mol Genet 31:1308–24.
  [DOI](https://doi.org/10.1093/hmg/ddab318) · PMC9029237
  → ΔN28-KLHL24 reduce K7, K8, K17, K18 *"via proteasome degradation"* en
  queratinocitos fetales **humanos**. Además: defectos de red de queratina y
  menor resiliencia bajo estrés térmico.

Implicaciones: (a) existe un sistema ubiquitina-proteasoma dedicado a queratinas,
caracterizado, en piel humana, con enfermedad asociada → es el candidato obvio
para la rama proteasomal del modelo de dos fases (§6 del plan); (b) un revisor
preguntará si KLHL24 media la degradación del K1 huérfano — conviene adelantarse;
(c) "nombrar la ligasa" ya no sube de revista por sí solo. Lo que subiría es
nombrar una ligasa **cuya actividad dependa del estado de emparejamiento**.

### ✅ "Estabilidad de proteína K1 según partner en queratinocitos humanos"

**Se sostiene.** No encontré nada sobre K1/K10 específicamente, en queratinocito
humano, con lectura de estabilidad de proteína. Los precedentes de 1988–89 son
K8/K18 en fibroblastos; Reichelt 2001 es ratón e in vivo. Es la parte más
defendible del hueco.

### ✅ "Medida cuantitativa de afinidad/capacidad K1–K10 vs K1–K14"

**Se sostiene.** No hay medidas comparadas de afinidad o capacidad entre pares.
Lo único próximo es in silico y sobre otra pregunta:

**Huang TL, Chou CC (2022).** *Effect of mutations on the hydrophobic interactions
of the hierarchical molecular structure and mechanical properties of epithelial
keratin 1/10.* Int J Biol Macromol 212:442–50.
[DOI](https://doi.org/10.1016/j.ijbiomac.2022.05.160)
→ Dinámica molecular del dominio 1B de K1/K10, mutaciones F231L y S233L de PPK.
Útil como cita estructural; no compite.

### ✅ "Conexión anclaje desmosómico ↔ degradación de una queratina concreta"

**Se sostiene.** No encontré nada. El tratamiento del plan en §8 (panel, no línea
de investigación) sigue siendo el juicio correcto.

---

## 3. El marco de "control de calidad estequiométrico" está más maduro de lo que asume el plan

El plan dice: *"Existe para ribosoma, proteasoma, histonas. Para queratinas, no
descrito."* El marco tiene nombre propio, mecanismos y ligasas identificadas:

- **Sung MK, Porras-Yakushi TR, Reitsma JM, ... Deshaies RJ (2016).** *A conserved
  quality-control pathway that mediates degradation of unassembled ribosomal
  proteins.* eLife 5:e19105. [DOI](https://doi.org/10.7554/eLife.19105)
  → Bautizan la vía **ERISQ** (*excess ribosomal protein quality control*).
  Rpl26 sobreproducida *"fails to assemble into ribosomes and is degraded"* por
  Tom1 (homólogo humano **Huwe1**). Clave: *"Tom1 directly ubiquitinates
  unassembled RPs primarily via **residues that are concealed in mature
  ribosomes**"*. Y: *tom1* muestra *"exceptional accumulation of
  detergent-insoluble proteins"* e *"hypersensitivity to imbalances in
  production"*.

- **Yanagitani K, Juszkiewicz S, Hegde RS (2017).** *UBE2O is a quality control
  factor for orphans of multiprotein complexes.* Science 357:472–75.
  [DOI](https://doi.org/10.1126/science.aan0178) · PMC5549844
  → *"Imbalances in the synthesis of individual subunits result in orphans."*
  UBE2O reconoce *"juxtaposed basic and hydrophobic patches on unassembled
  proteins"*. **α-globina que no se ensambla con β-globina → ubiquitinada por
  UBE2O.**

**Lo bueno:** la analogía α-globina/β-globina ≈ K1/K10 es el mejor párrafo de
introducción disponible — pareja obligada, el huérfano se elimina, hay
maquinaria dedicada. Mucho más fuerte que ribosoma o histonas.

**Lo malo:** "control de calidad estequiométrico de huérfanos" ya no es un marco
vacante. La novedad tiene que ser más fina y hay una buena: **en los dos casos
publicados el sustrato es un monómero y la salida es proteasomal. En queratinas
el sustrato oligomeriza y polimeriza, y por eso la salida debería ser
autofágica/agregativa.** Ese es un argumento de verdad, y encaja exactamente con
el modelo de dos fases de §6 y con el resultado parcial de cloroquina.

**Y una predicción regalada:** en ERISQ y en UBE2O la señal de degradación son
superficies que quedan **ocultas al ensamblar**. Eso predice que la señal de
degradación de K1 debería estar en la interfaz de dimerización con K10. Mapearla
convertiría el paper en algo bastante más ambicioso que JID.

---

## 4. Reichelt 2001 — confirmado, con un matiz que el plan pasa por alto

Verificado textualmente en PubMed (PMC37324,
[DOI](https://doi.org/10.1091/mbc.12.6.1557)): *"the amount of K1 was reduced"*;
*"in the absence of its natural partner we observed the formation of a minor
amount of novel K1/14/15 filaments as revealed by immunogold electron
microscopy"*; *"K5/14 persisted suprabasally at elevated protein levels, whereas
their mRNAs remained restricted to the basal keratinocytes. This indicated a
novel mechanism regulating keratin turnover."*

El plan lo tiene bien. **El matiz:** el fenómeno recíproco también está ahí —
K5/K14 **estabilizados** suprabasalmente. Si el mecanismo es titración de K14 por
K1 huérfano, en el K10-null el K14 debería estar **más** ocupado y más estable:
encaja. Pero conviene comprobar que el modelo de titración explica las dos caras
a la vez, porque es el primer sitio donde Magin (revisor probable) mirará.

---

## 5. Lo que queda realmente novedoso — ranking honesto

**Alto (esto es el paper):**

1. **El sobredisparo con K1 silvestre, en queratinocito humano.** Kulesh lo vio
   con un **truncado** dominante-negativo. Que ocurra con proteína silvestre, por
   pura estequiometría, sin mutación, es conceptualmente distinto y más limpio:
   deja de ser "una proteína defectuosa envenena la red" y pasa a ser "la
   abundancia está fijada por el suministro de partner". **Condicionado al
   control del tag.**
2. **La identidad de la vía** para una queratina huérfana: autofagia/p62 vs
   proteasoma, con validación genética. Nadie lo ha asignado y hay literatura
   publicada que apunta en contra (Jaeger 2019). Resolverlo es contribución real.
3. **Jerarquía cuantitativa de partners** (K10 vs K14 para K1), medida de
   capacidad y no sólo de existencia. Reichelt demostró que el par alternativo
   existe; nadie ha medido que sea de menor capacidad.
4. **La diferenciación como elevador fisiológico del techo, y el cruce de
   cohesión mecánica a tiempos largos** (§5 del plan). La predicción del cruce es
   genuinamente no trivial y no tiene precedente. Es la mejor idea del plan.

**Medio:**

5. Reconciliar agregación (Fischer/Eckhart) vs aclaramiento como dos salidas del
   mismo desbalance, moduladas por capacidad autofágica. Buena síntesis — pero es
   discusión, no dato.
6. Eje desmosoma ↔ degradación. Hueco real; el tratamiento como panel es correcto.

**Bajo / ya ocupado:**

7. "K1 necesita K10" → Reichelt 2001.
8. "K1 se empareja con K14" → Reichelt 2001, por inmuno-EM (más duro que co-IF).
9. "El ensamblaje protege a las queratinas de la degradación" → Domenjoud 1988,
   Kulesh 1989.
10. "Una queratina huérfana se degrada" → Kulesh 1989, Domenjoud 1988.
11. "Control de calidad estequiométrico de huérfanos de complejos" → Sung 2016,
    Yanagitani 2017.
12. "Hay una ligasa que degrada queratinas" → Lin 2016, Logli 2022.

---

## 6. Cambios concretos que pide el plan

1. **§2 — reescribir "NO descrito".** Dos de cuatro puntos son falsos. Añadir
   Kulesh 1989 y Domenjoud 1988 a "Ya descrito", y Jaeger 2019 + KLHL24 como
   contexto obligatorio.
2. **§1 — reformular la tesis y los títulos.** El título #1 es casi la frase de
   Domenjoud 1988. Reorientar hacia lo que es nuevo: la **vía** y la **no
   linealidad**. P. ej. *"Autophagic clearance of unpaired keratin 1 makes
   partner supply rate-limiting for K1 abundance in human keratinocytes"*, o
   centrar el título en el sobredisparo trans-dominante con proteína silvestre.
3. **§11 — subir Kulesh 1989 al nivel de Reichelt 2001 en prioridad de lectura.
   Kulesh es el competidor más peligroso de los dos**, porque tiene el dato del
   sobredisparo en trans y la frase sobre el estado polimerizado.
4. **§6 — el control del tag pasa de urgente a bloqueante.** Justificación
   explícita: el constructo de Kulesh que desestabilizaba el pool endógeno
   carecía precisamente de la cola C-terminal que el Myc-DDK tapa.
5. **§6 — añadir KLHL24/CUL3** como candidato mecanístico de la rama proteasomal
   y como control que un revisor pedirá.
6. **Fig. 3 — diseñar contra Jaeger 2019**, no ignorándolo. Decir en el
   manuscrito por qué desbalance de partner ≠ corneificación normal.
7. **Introducción — usar α-globina/UBE2O** como analogía principal en vez de
   ribosoma/histonas. Y considerar el experimento de mapeo de la señal de
   degradación en la interfaz con K10.
8. **Añadir un control que el plan no tiene:** Domenjoud mostró que expresar una
   queratina **no induce** la síntesis de su partner. Verificarlo (qPCR de KRT14
   en K1-OE) cierra una alternativa gratis.

---

## 7. Riesgos de precedente que no pude cerrar

- **Ensamblaje K1/K14 in vitro (Hatzfeld & Franke, Hatzfeld & Weber, Steinert;
  años 80–90).** Las búsquedas por términos MeSH no recuperan bien esta
  literatura: es anterior a la indexación moderna y usa otro vocabulario
  ("compatibilidad de pares tipo I/tipo II", "reconstitución in vitro"). **Hay
  que ir a mano.** Si alguno ya midió que K1/K14 polimeriza con menor eficiencia
  que K1/K10, la Fig. 5 pierde su primera mitad y queda sólo la de capacidad.
  Este es el hueco de verificación más importante que queda.
- **"UV-Induced Keratin 1 Proteolysis Mediates UV-Induced Skin Damage"** —
  preprint en bioRxiv (226308), no indexado en PubMed. Conviene leerlo: es
  proteólisis de K1 por otra ruta, y si está publicado ya en algún sitio hay que
  citarlo y distinguirse.
- **Literatura de Mallory-Denk bodies (K8/K18 en hígado).** Las búsquedas
  combinadas no dieron, pero el campo existe y es el ejemplo clásico de
  agregados de queratina con p62. Vale una pasada específica para la discusión.
  Lo que sí salió: Jang KH et al. 2019 FASEB J
  ([DOI](https://doi.org/10.1096/fj.201800263RR)), sobre acetilación/metilación y
  **estabilidad** de K8/K18 variantes de enfermedad hepática — precedente de
  "modificación postraduccional controla estabilidad de queratina".

---

## Fuentes

Bibliografía recuperada de **PubMed**. DOIs enlazados en el texto.

Búsqueda web complementaria:
- [Proteasome-mediated degradation of keratins 7, 8, 17 and 18 by mutant KLHL24](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9029237/)
- [UV-Induced Keratin 1 Proteolysis Mediates UV-Induced Skin Damage (bioRxiv)](https://www.biorxiv.org/content/10.1101/226308.full.pdf)
- [Cornification of nail keratinocytes requires autophagy... while sparing components of the cytoskeleton](https://www.researchgate.net/publication/329669516_Cornification_of_nail_keratinocytes_requires_autophagy_for_bulk_degradation_of_intracellular_proteins_while_sparing_components_of_the_cytoskeleton)
- [Loss of keratin 10 leads to MAPK activation, increased keratinocyte turnover...](https://pubmed.ncbi.nlm.nih.gov/15482487/)
- [The signaling involved in autophagy machinery in keratinocytes](https://doi.org/10.18632/oncotarget.9330)
