# Paper K1 / K10 — vigilancia estequiométrica del citoesqueleto de queratinas

> Documento de trabajo. Resume la discusión sobre enfoque, bibliografía, figuras,
> controles y protocolos. Fecha: 2026-10-08.

---

## 1. Tesis central (el reenfoque)

**No vender:** "K1 necesita K10; sin él se degrada" ni "K1 se empareja con K14".
Las dos cosas tienen precedente en ratón (ver §2).

**Vender:**

> La cantidad de K1 no la fija su expresión, sino la **disponibilidad estequiométrica
> de partner tipo I**. Al superar ese techo, una **vigilancia autofágica** elimina
> *todo* el pool de K1 — incluido el que ya era estable. K14 puede emparejarse con K1
> pero no sostiene el techo; solo K10 lo eleva, y la diferenciación lo hace de forma
> fisiológica.

Marco conceptual: **control de calidad estequiométrico** aplicado a filamentos
intermedios. Existe para ribosoma, proteasoma, histonas. Para queratinas, no descrito.

**Títulos candidatos**
- *Partner supply, not expression, sets keratin 1 abundance: autophagic surveillance of unpaired K1 in human keratinocytes*
- *Stoichiometric surveillance of the keratin cytoskeleton: unpaired keratin 1 triggers autophagic clearance of the entire K1 pool*

### El dato que vertebra el paper

Añadir K1 **reduce** el K1 total por debajo del parental. Esto no es un artefacto:
es la predicción de un sistema donde k_deg depende del propio nivel de K1.

```
[K1]ss = k_síntesis / k_degradación
```

`k_deg` **no es constante**: es función de la fracción de K1 sin emparejar.
Si subes la síntesis 5× pero k_deg sube 10×, el estado estacionario cae a la mitad
del parental. No hay cupo ni setpoint — es aritmética con una k_deg variable.
El sistema es **no lineal y autoamplificante**: más K1 → más huérfano → se degrada
más rápido *todo* el K1.

**Tres mecanismos compatibles, hay que separarlos:**

| Mecanismo | Predicción distintiva |
|---|---|
| **Titración del partner** — el K14 libre es finito; el K1 ectópico lo consume y el K1 previamente protegido se queda sin protector | Co-expresar K14 rescata |
| **Inducción de la maquinaria** — el K1 huérfano *activa* la autofagia, no solo la satura; una vía inducida se come todo el K1 presente | Flujo autofágico (LC3-II, p62) elevado en transfectado vs parental |
| **Agrefagia / co-degradación** — el K1 huérfano nuclea agregados que reclutan K1 soluble, incluido el de filamentos estables; nucleación cooperativa = umbral | Agregados de K1 + p62 al bloquear autofagia |

Apuesta: hay algo de inducción y algo de agrefagia.

---

## 2. Estado de la bibliografía

*Según PubMed.* **Lee el Reichelt 2001 completo antes de diseñar nada más** — es tu
competidor directo y tu mejor aliado a la vez.

### Ya descrito (en ratón)

**Reichelt J, Büssow H, Grund C, Magin TM (2001).** *Formation of a normal epidermis
supported by increased stability of keratins 5 and 14 in keratin 10 null mice.*
Mol Biol Cell 12:1557–68. [DOI](https://doi.org/10.1091/mbc.12.6.1557)

Textual, en el ratón K10⁻/⁻:
- *"the amount of K1 was reduced"*
- *"in the absence of its natural partner we observed the formation of a minor amount
  of novel K1/14/15 filaments as revealed by immunogold electron microscopy"*
- K5/K14 persisten suprabasalmente con proteína elevada mientras sus mRNAs siguen
  restringidos a la basal → *"a novel mechanism regulating keratin turnover"*

O sea: **las dos observaciones que planteabas están descritas**, y la de K1/K14 por
inmuno-EM (más duro que co-IF). La idea de regulación postraduccional del turnover
según el partner está **planteada pero sin mecanismo**.

### Contexto relevante — agregación vs aclaramiento

- **Fischer H et al. (2014).** *Loss of keratin K2 expression causes aberrant
  aggregation of K10, hyperkeratosis, and inflammation.* J Invest Dermatol
  134:2579–88. [DOI](https://doi.org/10.1038/jid.2014.197)
  → K10 sin partner tipo II **se agrega** en lugar de desaparecer; y al revés,
  *"deletion of K10 alone caused clumping of K2"*. Conclusión:
  *"unbalanced expression of these keratins results in aggregate formation"*.
- **Fischer H et al. (2015).** *Keratins K2 and K10 are essential for the epidermal
  integrity of plantar skin.* J Dermatol Sci 81:10–6.
  [DOI](https://doi.org/10.1016/j.jdermsci.2015.10.008)
- **Roth W et al. (2012).** *Keratin 1 maintains skin integrity and participates in an
  inflammatory network in skin through interleukin-18.* J Cell Sci 125:5269–79.
  [DOI](https://doi.org/10.1242/jcs.116574) — K1⁻/⁻, cara funcional/inflamatoria.
- **Reichelt J, Magin TM (2002).** *Hyperproliferation, induction of c-Myc and
  14-3-3σ, but no cell fragility in keratin-10-null mice.* J Cell Sci 115:2639–50.
  [DOI](https://doi.org/10.1242/jcs.115.13.2639)
- **Reichelt J, Furstenberger G, Magin TM (2004).** *Loss of keratin 10 leads to MAPK
  activation, increased keratinocyte turnover, and decreased tumor formation in mice.*
  J Invest Dermatol 123:973–81. [DOI](https://doi.org/10.1111/j.0022-202X.2004.23426.x)

### Eje queratina–desmosoma (bidireccional, establecido)

- **Sumigray KD, Chen H, Lechler T (2011).** *Lis1 is essential for cortical
  microtubule organization and desmosome stability in the epidermis.* J Cell Biol
  194:631–42. [DOI](https://doi.org/10.1083/jcb.201104009)
  → perder estabilidad desmosómica da *"decreased attachment of keratin filaments"*
  y mayor recambio de componentes desmosómicos.
- **Spindler V et al. (2014).** *Plakoglobin but not desmoplakin regulates keratinocyte
  cohesion via modulation of p38MAPK signaling.* J Invest Dermatol 134:1655–64.
  [DOI](https://doi.org/10.1038/jid.2014.21)
  → silenciar placoglobina provoca colapso del filamento de queratina.

### NO descrito — tu hueco real

- Degradación de queratinas **por autofagia / p62** en queratinocitos: búsqueda sin
  resultados.
- Estabilidad de proteína K1 según partner en **queratinocitos humanos**.
- **Medida cuantitativa** de afinidad/capacidad K1–K10 vs K1–K14.
- Conexión del eje **anclaje desmosómico ↔ degradación** de una queratina concreta.

---

## 3. Lo que ya tienes

- Queratinocitos humanos inmortalizados: **K1 endógeno presente, K10 ausente** en
  estado indiferenciado. K5/K14 abundantes.
- **K1-Myc-DDK** estable (OriGene, tag **C-terminal** — ver §6, riesgo).
- Sobreexpresión estable de **K10 WT**, de **K10 mutado**, y **KO de K10**.
- qPCR de KRT1.
- Degradación de K1 reducida con **cloroquina** (parcial).
- Dispasa a 48 h de diferenciación: K1-OE se fragmenta; **K10 WT aguanta**,
  **K10 mutado y K10 KO se fragmentan**.
- NanoBiT planteado.

### Nomenclatura: cuidado

No digas "estrato basal" para células en cultivo. In vivo, K1 es marcador
**suprabasal**; en la capa basal sería anómalo. Lo tuyo es un cultivo en estado
**indiferenciado / bajo calcio**, y las líneas inmortalizadas tienen expresión
filtrada de marcadores de diferenciación — comportamiento conocido, no un hallazgo
sobre la capa basal. Llámalo "estado indiferenciado" y describe el K1 endógeno como
expresión de bajo nivel en ausencia de K10. El dato vale igual y no das flanco gratis.

---

## 4. Plan de figuras

### Fig. 1 — El sistema y la paradoja de partida
Queratinocitos indiferenciados: K1 presente, K10 ausente, K5/K14 abundantes.
**Fraccionamiento Tritón + IF** (§7.1, §7.2): ¿ese K1 endógeno está ensamblado o es
soluble? Deja planteada la pregunta: *¿qué lo mantiene vivo sin K10?*

- **Insoluble** → ensamblado, presumiblemente con K14 → justifica todo el bloque
  K1/K14 y el modelo de amortiguación por partner.
- **Soluble** → pool no ensamblado que escapa a la degradación → otro mecanismo
  (chaperonas, umbral de detección). También interesante, pero cambia el relato.

### Fig. 2 — El sobredisparo (figura estrella)
- K1 ectópico → K1 **total** por debajo del parental.
- **Dosis-respuesta** (inducible por dox, mejor que clones).
- **Cicloheximida chase**: vida media de K1 más corta al subir el K1 total.
- mRNA transgén y endógeno **por separado** → el efecto es postranscripcional.
- El dato elegante que ya tienes: al diferenciar, mRNA del transgén **baja** mientras
  su proteína **sube**.

### Fig. 3 — La vía: autofagia
- Cloroquina/bafilomicina, MG132, **y la combinación**.
- Partición soluble/insoluble en cada condición.
- **Flujo autofágico** (LC3-II, p62) transfectado vs parental → ¿el K1 huérfano
  *induce* la vía? Esta es la explicación mecanística del sobredisparo.
- Validación **genética**: ATG7/ATG5, p62 (KD o KO).
- Colocalización K1–p62/LC3; aparición de agregados de K1 al bloquear el flujo.

### Fig. 4 — K10 eleva el techo
- Co-expresión de K10 → K1 se estabiliza, vida media larga, pasa a fracción insoluble,
  deja de ir a autofagosomas.
- Contraparte fisiológica: diferenciación con K10 endógeno, mismo resultado.
- **Índice de estabilidad** = proteína / mRNA del transgén, en las cuatro condiciones.

### Fig. 5 — Por qué K14 no basta
- KO de K10: co-IF, co-IP K1/K14.
- **NanoBiT** comparando K1/K10 vs K1/K14 vs K5/K14.
- Experimento que lo cierra: **co-expresar K14 en vez de K10** → rescate parcial o nulo.
- Mensaje: el emparejamiento alternativo existe, es de menor capacidad, y por eso
  define un techo bajo en lugar de proteger el pool entero.

### Fig. 6 — opcional, sube de revista
- **K10 incapaz de ensamblar** (mutante de rod, o de EHK): si une pero no polimeriza y
  **no** rescata → lo que protege es la **incorporación al filamento**, no la unión.
- Y/o: cohesión mecánica (§5), organotípico 3D, queratinocitos de paciente con
  mutación en *KRT10*.

---

## 5. La dispasa: tu dato está mejor de lo que parece

**La dispasa de 48 h no es un experimento fallido, es un punto de la curva.**
Las K1-OE se rompen *precisamente porque tienen menos K1*. Eso es coherencia interna
del mecanismo: la cohesión mecánica sigue a la **cantidad de proteína K1**, no al
genotipo.

**Para convertirlo en dato duro:** Western de K1 de **la misma placa, al mismo tiempo,
en cada línea**. Con eso puedes representar **nº de fragmentos vs K1 proteína** en
todas las condiciones y tiempos → correlación cuantitativa. Dejas de tener una
colección de fenotipos y tienes una ley: *la cohesión escala con el K1 disponible,
independientemente de cómo llegues a ese nivel*.

**Puede que ya tengas la cadena causal completa.** K10 WT → monocapa fuerte;
K10 mutado y K10 KO → fragmentación. Si mides **K1 proteína en esas líneas** y sale
baja en el mutante y en el KO, cierras: *K10 funcional → K1 estable → cohesión
mecánica*. Mutante y KO coinciden en fenotipo, lo que apunta a pérdida de función y
no a efecto dominante del agregado. **Es reanálisis de material que ya tienes.**

### La predicción que hay que ir a buscar
A tiempos **largos** de diferenciación, cuando K10 endógeno ya está arriba y el K1
deja de degradarse, las K1-OE deberían pasar a ser **más fuertes que el parental**.
Un **cruce**: débiles a 48 h, fuertes a tiempo largo. Si sale, es figura de paper —
predicción no trivial del modelo que nadie esperaría.

**Dos controles sin los cuales no se sostiene:**
1. **Western de K10 endógeno en cada tiempo**, para elegir los tiempos con criterio.
2. **Marcadores de diferenciación emparejados** (involucrina, loricrina, TGM1).
   La dispasa depende de nº de desmosomas, DSG1, confluencia y estado de
   diferenciación. Tienes que poder decir *"a igual estado de diferenciación, la
   cohesión difiere"*. Si no, te dirán que la K1-OE simplemente se diferencia distinto.

---

## 6. Riesgos y controles críticos

### ⚠️ El tag C-terminal (lo más urgente)
Myc-DDK va en **C-terminal** → **tapa la cola de K1**, que es justo la región
implicada en interacciones con desmoplaquina y en el empaquetamiento del filamento
(glycine loops).

Dos consecuencias:
1. **Cualquier afirmación sobre anclaje desmosómico con K1-Myc-DDK está confundida de
   origen.** Un revisor del campo lo ve en diez segundos.
2. **Parte de la degradación que ves podría deberse al tag y no a la falta de K10.**

**Control obligatorio, toca el corazón del paper:** comparar K1 **sin tag** (o con tag
N-terminal) en el mismo ensayo. Y validar que el K1 etiquetado se incorpora a
filamentos normales en presencia de K10 (IF).

### ⚠️ Artefacto de clon
Clones estables = selección + tiempo en cultivo. Si comparas un clon contra el
parental sin pasar, parte de la caída puede ser del clon.
→ **Inducible (dox)**, o varios clones independientes + pool policlonal.
Sin esto, tu figura principal es atacable.

### ⚠️ Que k_deg no suba de verdad
El **cicloheximida chase parental vs transfectado** es el experimento que decide si
tienes paper o solo una observación. **Hazlo primero.**

### Niveles "no fisiológicos" — cómo se neutraliza
No es un problema del modelo, es de interpretación: dirán que ves control de calidad
genérico por sobrecarga.
- **Dosis-respuesta**: si es proporcional y no umbral-por-colapso, es regulación.
- **Comparar con el K1 endógeno diferenciado**: "mi K1 ectópico está a 0,5–2× del
  endógeno". Una frase en Methods.
- **Control de especificidad**: una proteína ectópica igual de abundante que no se
  degrade (GFP, o K5 con su partner presente).
- El argumento más fuerte: **el rescate por K10 ya es el control de especificidad**.
  Si fuera sobrecarga genérica, añadir *más* proteína la empeoraría, no la rescataría.
- **ddPCR** da la ratio transgén:endógeno a nivel de mRNA → "el transgén aporta 3,2×
  el mRNA endógeno". Inatacable.

### Endógeno vs exógeno — el alcance real del argumento
A la maquinaria de degradación **le da igual de qué gen venga** la proteína. Son
moléculas idénticas. Por tanto:

- **"Hay degradación de K1 sin K10"** → ya demostrado con el total. Si el endógeno se
  silenciara y no hubiera degradación, el transgén (CMV) daría K1 **alto**, no bajo.
- **"La degradación alcanza también al K1 endógeno preexistente"** → esto es lo nuevo,
  y *sí* necesita separar bandas **más** mRNA endógeno por 3'UTR:

| Modelo | mRNA endógeno | Proteína endógena | ¿Efecto en trans? |
|---|---|---|---|
| **A** — degradación en trans | normal | baja | **sí** (tu hipótesis) |
| **B** — silenciamiento + degradación solo del ectópico | baja | baja | no |

Los dos dan "proteína total por debajo del parental". Separar bandas en el Western
**no basta** — solo el mRNA endógeno los distingue.

**Alternativa más limpia que todo el lío de primers:** cicloheximida chase en parental
vs transfectado. Si la vida media de K1 se acorta, has medido el sobredisparo de
frente, sin depender de qué hace el promotor endógeno.

### Multiplicidad de vías de degradación — es lo normal
- **Proteasoma** → monómeros solubles, mal plegados, ubiquitinados individualmente.
  Vía por defecto de una subunidad huérfana.
- **Autofagia** (agrefagia, p62/NBR1) → oligómeros, agregados, filamentos. Un filamento
  intermedio ensamblado **no cabe** en el barril proteasomal.

Para K1 huérfano, modelo de **dos fases**: monómero → proteasoma; lo que oligomeriza →
agregado → autofagia. **Eso explica que la cloroquina reduzca la degradación pero no la
abola.** Ese resultado parcial no es un problema experimental, es un dato mecanístico.
No fuerces que "todo es autofagia": es más débil y probablemente falso.

Nota: **MG132 induce autofagia** como respuesta compensatoria, así que un rescate con
MG132 no prueba por sí solo que sea proteasomal → de ahí la validación genética.

---

## 7. Protocolos

### 7.1 Fraccionamiento Tritón + Western

El Tritón es solo **preparación de muestra**: en vez de un lisado por condición acabas
con dos, y los corres en un Western normal.

1. Lisis en tampón con **1% Tritón X-100** + inhibidores de proteasas. Centrifugar.
2. **Sobrenadante = S** (pool soluble). **Pellet = P** (citoesqueleto).
3. Lavado del pellet (muchos protocolos usan sal alta, ~1,5 M KCl, para quitar actina
   y proteínas asociadas).
4. Resuspender P en **urea 8 M** o Laemmli caliente con reductor. Las queratinas no
   salen con tampón suave.
5. Cargar **S y P en el mismo gel, carriles contiguos**.

**Layout del gel** — para cada condición, dos carriles:

| | Parental | K1-OE | K1-OE +K10 | K1-OE +CQ |
|---|---|---|---|---|
| | S / P | S / P | S / P | S / P |

**Anticuerpos**
- **anti-K1** → la lectura principal
- **anti-FLAG** → el K1 ectópico por separado
- **anti-K14**, **anti-K5** → partner + control de que P es de verdad citoesqueleto
- **anti-K10** → donde aplique
- **GAPDH** o **HSP90** → control de extracción: debe salir **solo en S**
- **p62** → bonus útil: al agregarse pasa de S a P

**Los dos errores que se cometen casi siempre**
1. **La carga.** No cargues "20 µg de cada fracción" — carga **el mismo porcentaje de
   la placa original** en cada carril (p. ej. 5% de S y 5% de P). Normalizar por
   proteína total destruye justo la información que buscas.
   Corolario: **no puedes usar housekeeping como control de carga por carril** (GAPDH
   solo existe en S). El experimento se normaliza a sí mismo:
   `% insoluble = P / (P+S)`, y comparas esa ratio entre condiciones. Más robusto que
   un housekeeping.
2. **La urea.** Si usas urea 8 M, **no hiervas** — carbamila las proteínas y estropea
   las bandas. Calienta a 37–50 °C. Si prefieres hervir, usa Laemmli con SDS +
   reductor.

Corre S y P **en el mismo gel y la misma membrana**, siempre. La lectura es una
proporción; comparar entre blots distintos no vale.

**Limitación:** "insoluble en Tritón" **mezcla filamento genuino con agregado**. El
blot da cantidad, no arquitectura. Por eso va con IF.

### 7.2 IF con pre-extracción (el truco que merece la pena)
Permeabiliza con **Tritón antes de fijar**, para lavar el pool soluble: lo que quede
teñido es lo **ensamblado**. Pon en paralelo la IF sin extraer y la pre-extraída →
equivalente in situ del fraccionamiento, célula a célula. Ves qué fracción de la señal
de K1 está incorporada **y la forma** (red filamentosa vs punteado agregado vs
difuso), que es lo que el blot no da.

- Fijación: **metanol** (o metanol/acetona) a −20 °C conserva bien la red de filamentos
  intermedios. PFA + permeabilización retiene más pool soluble y da fondo difuso.
- Aprovecha el tag: **anti-FLAG (ectópico) + anti-K1 (total)** en doble marcaje, para
  ver si colocalizan o si el ectópico va a sitios distintos.

### 7.3 qPCR / ddPCR endógeno vs transgén
El constructo es cDNA: solo **ORF + tag, sin UTRs**. Primers en la ORF amplifican
**las dos cosas**. Primers que cruzan unión exón-exón **tampoco** discriminan (el mRNA
endógeno ya está empalmado y el transgén es cDNA).

- **Endógeno específico** → primers en **3'UTR** (o 5'UTR). El transgén no los lleva.
- **Transgén específico** → un primer en la ORF + uno en el **vector/tag**, de modo que
  el amplicón cruce la unión ORF–DDK.
- **Control −RT obligatorio** + DNasa. Tienes plásmido en multicopia: la contaminación
  con DNA es un riesgo mucho mayor que en un experimento normal. En ddPCR es
  especialmente traicionero porque da números absolutos preciosos y falsos.
- Comprobar **eficiencias** de los dos pares si vas a comparar en la misma escala.
- **ddPCR** por lo que permite *decir*: copias absolutas → ratio transgén:endógeno.

### 7.4 Western: separar las dos bandas
Myc-DDK añade ~3 kDa sobre los ~67 de K1 → se resuelven, pero hay que trabajarlo:
**gel de bajo porcentaje y corrida larga**.

Demostrar explícitamente en figura:
- **anti-FLAG → solo la banda superior** (identifica el ectópico)
- **anti-K1 → ambas bandas**, cuantificadas **por separado en el mismo carril**

Eso es lo que demuestra "degrada incluso lo endógeno": la banda inferior en el clon
transfectado es menor que la banda única del parental.

---

## 8. Desmosomas: ¿merece la pena?

**Sí, pero como un panel, no como una línea de investigación.** Es todo o un párrafo —
no hay término medio bueno: el campo está muy poblado y es exigente (Waschke, Lechler,
Green, Magin) y un bloque a medias te atrae a un revisor de ese campo que pedirá tres
experimentos más.

**La versión floja:** "si K1 colapsa, ¿se resiente la adhesión?" Da una figura de
*so what?* decente pero no aporta mecanismo.

**La versión buena — el anclaje como causa, no como consecuencia:** tu pregunta
abierta es *por qué K14 no rescata*. Tercera opción además de afinidad y
estequiometría: **el filamento K1/K14 no se ancla bien**, y lo que protege a un
filamento no es estar polimerizado sino estar **anclado**. Eso convierte al desmosoma
en parte del mecanismo de proteostasis. Encaja con el mutante de K10 incapaz de
ensamblar: serían los dos brazos del mismo experimento. El eje anclaje↔filamento está
establecido como bidireccional (§2), pero **nadie lo ha conectado con la degradación**
de una queratina concreta.

**Pilotos baratos (una semana):**
1. **Dispasa** parental vs K1-OE vs +K10 (ya iniciado, ver §5).
2. **IF de desmoplaquina + DSG1/PKP1**: ¿los filamentos de K1 llegan al borde celular
   o se quedan perinucleares? ¿Cambia el patrón de DP?
3. **DP en fracción insoluble** — ya estás fraccionando, es un blot extra en las mismas
   muestras. Coste casi cero.

**Regla de decisión:** si 1 o 2 dan algo llamativo → Fig. 6, con constructo
N-terminal, y sube de revista (pasas de "una queratina se degrada" a "la adhesión
regula la proteostasis del citoesqueleto"). Si sale plano → una frase en la discusión.

---

## 9. Discusión: los tres párrafos que ganan el paper

1. **Explicas un resultado publicado y nunca explicado.** Reichelt 2001 vio K1 reducido
   y *"a minor amount"* de filamentos K1/K14/K15 en el K10⁻/⁻. Tu mecanismo dice por
   qué: el emparejamiento alternativo rescata una fracción pequeña y el resto se
   aclara. Pasas de competir con ese paper a explicarlo.
2. **Reconcilias dos observaciones opuestas.** Eckhart: las queratinas desbalanceadas
   **se agregan**. Tú: **desaparecen**. Síntesis: agregación y aclaramiento son dos
   salidas del mismo desbalance, y lo que decide cuál ves es la **capacidad
   autofágica**. Tu experimento de cloroquina lo demuestra. Unir dos literaturas con un
   experimento es muy buen material de discusión.
3. **Generalizas.** Control de calidad estequiométrico en filamentos intermedios, con
   implicación en queratodermias: en un paciente con *KRT10* mutado, la pérdida de K1
   no sería efecto secundario sino parte del mecanismo patogénico.

---

## 10. Revista

| Destino | Requisito |
|---|---|
| **J Invest Dermatol** | principal: marco dermatológico, mecanismo celular, Fig. 2 es su tipo de dato |
| **JCB**, **Life Science Alliance** | realistas con Fig. 6 completa |
| **J Cell Sci**, **Cell Death & Disease** | red de seguridad |
| *Exp Dermatol*, *IJMS* (Q2) | donde caerías solo con Westerns de estado estacionario + co-IP + NanoBiT |

---

## 11. Próximos pasos, en orden

1. **Leer Reichelt 2001 completo** antes de diseñar nada más.
2. **Cicloheximida chase** parental vs transfectado. *El experimento que decide si hay
   paper.*
3. **Control del tag**: K1 sin tag o N-terminal, mismo ensayo. *Toca el corazón del
   paper.*
4. **Reanalizar lo que ya tienes**: Western de K1 (y K10) en K10-WT-OE, K10-mutado y
   K10-KO → ¿correlaciona con la fragmentación en dispasa? (§5)
5. qPCR 3'UTR (endógeno) + ORF-tag (transgén), con −RT.
6. Fraccionamiento Tritón + IF con pre-extracción (Fig. 1 y lectura transversal).
7. Cloroquina + MG132 + combinación, con partición S/P. ¿Aparecen agregados K1/p62?
8. Dispasa a tiempos largos, con K10 endógeno y marcadores de diferenciación
   emparejados → buscar el **cruce**.
9. Validación genética de autofagia (ATG7/ATG5, p62).
10. Co-expresión K14 vs K10 → titración vs co-degradación, jerarquía de partners.

### Pendiente de decidir
- **¿Qué mutante de K10 es el que tienes?** (EHK, dominio rod, otro). Cambia cómo
  interpretas el fenotipo de la dispasa y si puedes usarlo como el "K10 incapaz de
  ensamblar" de la Fig. 6.
- Búsqueda bibliográfica sobre **control de calidad estequiométrico** en complejos
  proteicos y en filamentos intermedios → andamio de introducción y discusión.
- Búsqueda sobre **ensamblaje K1/K14 in vitro** (Hatzfeld/Weber, Steinert, años 90) →
  donde más riesgo de precedente queda.
- Búsqueda sobre **E3 ligasas de queratinas** → si puedes nombrar la ligasa, subes otro
  escalón de revista.

---

*Referencias bibliográficas recuperadas de PubMed. DOIs enlazados en §2.*
