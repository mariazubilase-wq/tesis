# Diseño de clonaje — KRT10 (desde pCMV6-KRT10) en `pMC.EF1α-MCS-SV40polyA`

**Constructo 1 de los tres previstos: el minicírculo de reemplazo.**
Documento de diseño cerrado, para llevar al banco.

---

## 0. Qué se construye, en una frase

Se amplifica **únicamente la pauta abierta de lectura de KRT10** desde el plásmido
pCMV6-KRT10, con colas que aportan Kozak, dos codones stop y dos dianas de
restricción distintas, y se inserta **en fase única y dirigida dentro del MCS que
el fabricante colocó entre el promotor EF1α y la señal SV40 polyA**, es decir,
dentro de la región attB–attP que acabará siendo el minicírculo.

Resultado: `attB/P → EF1α → [Kozak-ATG-KRT10-stop] → SV40 polyA →` minicírculo de
**≈ 3,2–3,5 kb** sin esqueleto bacteriano.

---

## 1. Qué está verificado y qué no

Conviene que esto quede dicho antes que nada, porque condiciona la forma del
documento.

**No he podido acceder a los mapas reales.** La política de red de esta sesión
bloquea systembio.com, origene.com, NCBI y los distribuidores. No voy a escribir
de memoria una secuencia de cebador de 40 nt para un proyecto cuyo objeto es
precisamente una mutación puntual: sería inventármela.

Así que el diseño va en dos piezas:

| Pieza | Qué contiene | Estado |
|---|---|---|
| **Este documento** | Todas las decisiones de diseño, la lógica, los protocolos y los controles | Cerrado |
| **`herramientas/disena_clonaje.py`** | Calcula las secuencias literales de los cebadores y todos los tamaños a partir de **tus** dos ficheros | Escrito y probado (29/29 comprobaciones) |

Lo que sí está verificado por búsqueda: la existencia y el nombre del vector
parental, y el número de catálogo **MN502A-1** (aparece en la ficha de producto;
**confírmalo al pedir**, porque la serie MN5xx tiene variantes muy parecidas:
MN511A-1, MN512A-1, MN531A-1 son otros vectores).

**Lo que tienes que descargar antes de ejecutar la herramienta:**

1. El GenBank de `pMC.EF1α-MCS-SV40polyA` (SBI lo da con el vector; si no,
   pídeselo a soporte técnico: es un fichero, no un favor).
2. El GenBank de tu `pCMV6-KRT10`.

---

## 2. Los dos vectores

### 2.1 Donante: cuál de los dos pCMV6-KRT10 tienes (esto importa mucho)

OriGene vende KRT10 (NM_000421) en dos formatos, y **el diseño cambia según cuál
sea el tuyo**:

| Producto | Vector | Contenido | Trampa |
|---|---|---|---|
| `RC204500` (TrueORF) | pCMV6-Entry | ORF clonado **SgfI–MluI**, fusionado a **Myc-DDK** en C-terminal | **Le han quitado el codón stop.** El ORF sigue en fase hasta la etiqueta |
| `SC122561` (TrueClone) | pCMV6-XL | cDNA completo con sus UTR y su stop nativo | Arrastra 5'UTR y 3'UTR |

Las dos trampas son distintas y las dos importan:

- Si es el **RC204500**, la ORF más larga del fichero **no es KRT10**: es
  KRT10+enlace+Myc+DDK, unos 20 aa de más. Si clonas "el ORF" sin pensar, te
  llevas una K10 con una etiqueta de ~3 kDa pegada al **dominio de cola**, que es
  justo la región que participa en el ensamblaje del filamento. Para una copia de
  reemplazo terapéutica eso es inaceptable.
- Si es el **SC122561**, el riesgo es el contrario: arrastrar la 3'UTR endógena
  (ver §3.1, por qué no la quieres).

> **Dato útil:** **SgfI y AsiSI son isoesquizómeros** (ambas `GCGAT^CGC`, mismo
> corte). La AsiSI que ya tienes en el congelador (R0630S) corta el sitio SgfI del
> pCMV6-Entry, justo delante del ATG. No lo usaremos para clonar, pero sirve para
> linearizar el donante y para comprobar que el fichero que tienes es el que crees.

**El diseño de §3.2 resuelve las dos trampas a la vez** y funciona con cualquiera
de los dos clones, sin que tengas que decidir nada.

### 2.2 Aceptor: `pMC.EF1α-MCS-SV40polyA`

Ya trae promotor y polyA montados, así que **sólo hay que meter el CDS**. Es el
vector correcto para este constructo, y por dos razones, no una:

1. **La conocida:** el CMV se silencia al diferenciarse el queratinocito, y el
   transgén de reemplazo tiene que expresarse precisamente en la célula
   diferenciada. EF1α se mantiene.
2. **La que conviene añadir:** las queratinas son heterodímeros obligados de tipo
   I + tipo II. **K10 es tipo I y necesita a K1 como pareja.** Un exceso masivo de
   K10 sin K1 que la acompañe deja K10 sin aparear, que se degrada o agrega. Aquí
   no quieres el promotor más fuerte posible: quieres **restaurar un nivel
   fisiológico**. Un EF1α "moderado" es una virtud, no una limitación.

**Restricción arquitectónica que no se puede negociar:** el casete tiene que caer
**dentro de la región attB–attP**. Un sitio fuera de ahí manda el inserto al
esqueleto que la I-SceI destruye, y el minicírculo sale vacío. La herramienta
comprueba esto explícitamente para cada enzima y lo marca como
`❌ su única diana cae FUERA de la región attB-attP`.

**A confirmar en el mapa:** si el EF1α de este vector es el completo (con el
intrón A endógeno) o el núcleo corto sin intrón. No es cosmético: vas a expresar
un **cDNA sin intrones**, y un intrón en el transcrito mejora el procesamiento y
la exportación del mRNA. Si es el corto, tenlo en cuenta al interpretar niveles.

---

## 3. Decisiones de diseño

### 3.1 Se clona el CDS, no el cDNA completo

Sólo `ATG … último codón`. Nada de UTR. Tres razones:

1. **Tamaño.** El rendimiento de minicírculo cae con el inserto. La 3'UTR de KRT10
   añadiría ~1 kb a cambio de nada.
2. **Regulación que no controlas.** La 3'UTR endógena lleva sitios de miRNA y
   elementos de estabilidad. Precisamente en queratinocito diferenciado no sabes
   qué hacen.
3. **La razón buena, y es de diseño experimental.** Si el transgén termina en
   **SV40 polyA** en vez de en la 3'UTR de KRT10, entonces el mRNA del transgén y
   el endógeno **tienen extremos 3' distintos**, y puedes discriminarlos por qPCR
   trivialmente (§9). Si clonases la 3'UTR nativa, perderías esa discriminación —
   que es exactamente el experimento que tu documento pide en §4.1 para averiguar
   si la caída de K10 al diferenciar en la línea lentiviral es silenciamiento del
   promotor o biología.

### 3.2 El codón stop lo aporta el cebador reverso

**Esta es la decisión que hace el diseño robusto.** El cebador reverso:

- aparea contra los **últimos codones del CDS de KRT10**, sin incluir el stop, y
- **lleva dos codones stop en tándem (`TAA TGA`) en su cola.**

Consecuencias:

- Si tu clon es el **RC204500** (sin stop, con Myc-DDK): la etiqueta **no viaja**,
  porque el stop lo pones tú antes de llegar a ella. Obtienes K10 nativa.
- Si tu clon es el **SC122561** (con stop nativo): el stop nativo queda fuera del
  apareamiento y lo sustituye el tuyo. Mismo resultado.
- **Dos stops en vez de uno** son un seguro barato contra la lectura a través del
  primero (*readthrough*), que en un transgén sobreexpresado no es despreciable.

Un solo diseño para los dos clones, sin ramas.

### 3.3 Kozak

Se añade `GCCACC` inmediatamente delante del `ATG`. Deja la posición −3 como
purina, que es lo que de verdad manda.

**Lo que NO hay que hacer:** forzar una `G` en la posición +4 para tener el Kozak
"de libro" `GCCACCATGG`. La +4 es la primera base del segundo codón: tocarla
**cambia el segundo aminoácido de tu proteína**. En un constructo de reemplazo
terapéutico eso no se hace por un consenso de traducción. La herramienta te dice
qué base te queda en +4 y te avisa de que la dejes en paz.

### 3.4 Sin etiquetas

Ni Myc-DDK, ni HA, ni GFP fusionada. La cola C-terminal de K10 es funcional. Si en
algún momento necesitas seguir la proteína, la vía correcta es un anticuerpo
frente a K10 o una etiqueta en un constructo **aparte**, declaradamente no
terapéutico.

### 3.5 Los cambios *wobble* NO van en esta versión

Tu §4.2 los pide para el constructo combinado, y tiene razón. Pero aquí **no**, y
conviene razonar por qué, porque la geometría lo decide sola:

- El shRNA es **alelo-específico**: tiene que solapar la mutación. R156C es
  `c.466C>T`, o sea el **nucleótido 466 del CDS** — un 27 % dentro de un CDS de
  ~1,75 kb. Está en mitad del inserto.
- Un cambio en mitad del inserto **no se puede introducir con un cebador de los
  extremos**. Haría falta PCR de extensión solapante (dos fragmentos y una tercera
  PCR) o síntesis del fragmento.
- Y sobre todo: **todavía no sabéis qué shRNA gana.** Están los 19 siRNA en
  evaluación, con discrepancias HEK293T vs queratinocito sin resolver. Los cambios
  wobble se diseñan **contra una diana concreta**. Introducirlos ahora es
  adivinar.

**Plan correcto, que además es el que tu propio documento recomienda en §2:**
clona ahora la versión nativa y **valida el reemplazo solo**. Cuando el shRNA esté
elegido, la versión resistente se hace sobre este mismo constructo, y ahí la vía
limpia es **encargar sintético sólo el fragmento que lleva los cambios** y
sustituirlo, en vez de rehacer el clonaje entero.

Un detalle que te servirá entonces: para hacer el reemplazo resistente **también
puedes cambiar el propio codón 156** (`CGC → CGT/CGA/CGG`, todos siguen siendo
Arg). Mantienes la proteína silvestre exacta y encima el transgén deja de ser
indistinguible del alelo WT endógeno en la ddPCR alelo-específica, lo cual es una
ventaja, no un problema.

### 3.6 Elección de la pareja de enzimas

De las seis del congelador:

| Enzima | Papel en este diseño |
|---|---|
| **NheI-HF** (`G^CTAGC`) | **Candidata preferente para el extremo 5'** |
| **XhoI** (`C^TCGAG`) | **Candidata preferente para el extremo 3'** |
| **BamHI-HF** (`G^GATCC`) | Alternativa de 5' si NheI no está en el MCS o corta el CDS |
| XbaI (`T^CTAGA`) | **Evitar** |
| AsiSI (`GCGAT^CGC`) | **Reservar** para diagnóstico |
| PmeI (`GTTT^AAAC`) | **Reservar** para diagnóstico |

Los porqués:

- **NheI + XhoI:** salientes `CTAG` y `TCGA`, incompatibles entre sí → clonaje
  direccional de verdad, el vector no puede recircularizarse y el inserto no puede
  entrar invertido. Además NheI-HF y BamHI-HF son versiones HF, sin actividad
  *star*.
- **XbaI se descarta por partida doble:** genera el mismo saliente `CTAG` que
  NheI (religación cruzada si usas las dos), y la bloquea la metilación Dam si
  queda como `GATCTAGA` o `TCTAGATC` — **sin dar ninguna señal: simplemente no
  corta**.
- **AsiSI y PmeI son cortadores de 8 pb: no los gastes en el clonaje.** Son
  demasiado valiosos como enzimas de diagnóstico, porque casi con seguridad cortan
  una sola vez y linearizan limpiamente el clon final. Reservarlas es una decisión
  deliberada.
- **BamHI no la bloquea Dam** aunque su diana `GGATCC` contenga `GATC`. Es la
  excepción que tu documento sospechaba: no todo lo que contiene GATC está
  bloqueado.
- **AsiSI tampoco la bloquea Dam**, pese a contener `GATC`. La prueba práctica es
  que todo el sistema PrecisionShuttle de OriGene se basa en cortar con SgfI (su
  isoesquizómero) plásmido crecido en cepas Dam⁺ corrientes; si estuviera
  bloqueada, no funcionaría nunca. Sí la bloquea la metilación **CpG**, irrelevante
  en DNA de *E. coli*. (Esto cierra uno de los puntos que dejabas pendientes en
  §8; confírmalo igualmente en NEBcloner, que cuesta un minuto.)

**La elección final la decide el mapa**, y la herramienta la hace por ti: exige
que la diana sea **única en todo el plásmido parental**, que caiga **dentro de la
ventana promotor–polyA**, que esté **dentro de la región attB–attP** y que **no
corte el inserto**. Sólo propone parejas con salientes incompatibles.

---

## 4. Estrategia: restricción direccional, y qué hacer si no sale

**Plan A — doble digestión direccional.** Es lo correcto aquí: un solo casete, un
MCS pequeño, y ya tienes las enzimas.

**Plan B — ensamblaje Gibson / NEBuilder HiFi.** Si la herramienta te dice que no
hay ninguna pareja válida (porque el CDS de KRT10 corta todo lo que hay en el MCS,
que es un desenlace perfectamente posible en un CDS de 1,75 kb rico en GC).
Ventaja: no depende de las dianas. Coste: un kit más, y sigue necesitando la
polimerasa de alta fidelidad. Tu §5 ya lo señalaba para el constructo combinado;
aquí es la red de seguridad.

**Plan C — encargar el inserto sintético.** Un fragmento de ~1,8 kb con los
extremos que quieras, secuencia-verificado. Resuelve de golpe la falta de
polimerasa HF, el riesgo de deslizamiento de la polimerasa en la cola de glicinas
y, más adelante, los cambios wobble. El pero: **la cola rica en glicinas de K1/K10
es repetitiva y muy GC**, y hay proveedores que la rechazan o la cobran como
"secuencia compleja". Pide presupuesto antes de contar con ello.

---

## 5. Los cebadores

### 5.1 Estructura

**Directo (5'→3'):**

```
CACCAC      GCTAGC      GCCACC      ATG NNN NNN NNN ...
└protección └NheI-HF    └Kozak      └inicio del CDS (18–24 nt, Tm ≈ 62 °C)
```

**Reverso (5'→3'):**

```
CACCAC      CTCGAG      TCATTA                      NNN NNN NNN ...
└protección └XhoI       └ = TAA TGA en la hebra      └complementario inverso del
                          codificante (dos stops)      final del CDS, SIN su stop
```

Notas sobre cada bloque:

- **6 bases de protección.** Las enzimas cortan mal en el extremo de un fragmento.
  `CACCAC` está elegido para no crear `GATC` (trampa Dam) ni `CCWGG` (Dcm) al
  pegarse a la diana. La herramienta revisa este contexto y avisa si aparece.
- **`TCATTA` es el complementario inverso de `TAATGA`.** En el cebador reverso los
  stops se escriben al revés. Comprobado sobre el amplicón reconstruido.
- **La zona de apareamiento se ajusta por Tm**, no por longitud fija, y se prefiere
  terminar en G o C (pinza 3').

### 5.2 Cómo obtener las secuencias literales

```bash
cd herramientas
python3 disena_clonaje.py \
    --donante ../secuencias/pCMV6-KRT10.gb \
    --aceptor ../secuencias/pMC.EF1a-MCS-SV40polyA.gb \
    --salida  ../diseno/informe_KRT10.md
```

Devuelve un informe con los cebadores completos, sus Tm, GC, horquillas, dímeros
3', los tamaños de amplicón/inserto/vector/minicírculo, los avisos de metilación y
las digestiones diagnósticas. Sin conexión a internet.

Opciones útiles:

| Opción | Para qué |
|---|---|
| `--pareja NheI-HF,XhoI` | Forzar una pareja concreta |
| `--fin-orf N` | Forzar el último nt del ORF nativo, si el recorte automático de la etiqueta no acierta |
| `--inicio-orf N` | Forzar el ATG real, si hay un ATG en fase río arriba |
| `--proteccion XXXXXX` | Cambiar las bases de protección |
| `--autotest` | Comprobaciones internas (29) |

### 5.3 Dos cosas que la herramienta hace y conviene que sepas

Ambas salieron al probarla contra un pCMV6-Entry simulado, y ambas te habrían
mordido:

1. **En un clon pCMV6-Entry, el ORF más largo del fichero incluye la etiqueta.**
   La herramienta detecta el péptido Myc (`EQKLISEEDL`) y DDK (`DYKDDDDK`),
   localiza el sitio de lanzadera **MluI** en fase que hay delante y recorta ahí.
   Te dice cuántos aminoácidos ha quitado y qué residuos de unión ha eliminado.
2. **Un `ATG` en fase río arriba alarga el ORF por delante.** La herramienta ancla
   el ATG real al primer `ATG` en fase que hay tras el sitio **SgfI/AsiSI**, que es
   la arquitectura real del pCMV6-Entry.

En los dos casos **imprime los primeros y los últimos 12 aminoácidos** de lo que
va a clonar. **Míralos.** Es la comprobación de 10 segundos que evita clonar algo
que no es K10.

---

## 6. Protocolo de banco

### 6.1 PCR del inserto

- **Polimerasa de alta fidelidad. Obligatorio.** Q5, Phusion o Platinum SuperFi.
  Taq **no sirve** aquí, por dos motivos: su tasa de error (Q5 es ~280× más fiel
  según NEB) hace que sobre 1,75 kb una fracción grande de moléculas lleve al
  menos una sustitución — en un proyecto cuyo objeto **es una mutación puntual**,
  eso es inaceptable — y además añade una A terminal que estorba en un clonaje por
  extremos cohesivos.
- **Molde: poquísimo.** 1–10 pg de plásmido. Más molde = más arrastre.
- **Extremo 3' rico en GC.** Añade el potenciador GC de Q5 o 3 % de DMSO, y
  alarga la extensión (≈30 s/kb → ~60 s).
- **Ciclado en dos tramos:** 5 ciclos a la Ta de la zona de apareamiento (sólo
  aparea la parte homóloga) y después 25 ciclos a la Ta del cebador completo (ya
  aparea entero). La herramienta calcula las dos temperaturas.
- **Digiere la reacción con DpnI antes de nada.** El molde viene de *E. coli* y
  está metilado por Dam; el amplicón no. DpnI destruye el molde y deja intacto el
  producto. **Esto importa especialmente aquí** (ver §6.5).
- Corre en gel y **purifica la banda**.

### 6.2 Digestiones

- Digiere **por separado** el amplicón purificado y el vector parental.
- Comprueba en NEBcloner que las dos enzimas son compatibles en **rCutSmart**; si
  lo son, doble digestión en un tubo (es lo más probable con las seis de NEB, pero
  compruébalo, no lo asumas).
- **Digiere generosamente:** ≥2 h, exceso de enzima. La razón está en §6.3.
- Purifica los dos productos.

### 6.3 Desfosforilación: matiz importante

Tu §5 daba por bloqueante la falta de fosfatasa. **Con matices:**

- En teoría, una doble digestión direccional con salientes incompatibles no puede
  recircularizarse, así que la fosfatasa sobra.
- En la práctica **no**, y por una razón concreta: **las dos dianas del MCS estarán
  separadas por unas pocas decenas de pb**. El fragmento que libera la doble
  digestión es minúsculo e **invisible en gel**, así que **no puedes distinguir en
  el gel un vector cortado dos veces de uno cortado una sola vez**. El vector
  cortado una sola vez sí se recirculariza, y es tu fondo de colonias vacías.
- Conclusión: **no es tan bloqueante como la polimerasa, pero cómprala** (rSAP es
  la más cómoda: se inactiva a 65 °C y no hay que purificar). El inserto no se ve
  afectado: las enzimas de restricción dejan extremos 5'-fosfato, así que aporta él
  los fosfatos de la ligación.
- Y en cualquier caso, **monta siempre una ligación control sin inserto**. Te dice
  el fondo real, que es el único número que importa.

### 6.4 Ligación y transformación

- T4 DNA ligasa, relación molar inserto:vector ≈ 3:1, 16 °C toda la noche o
  temperatura ambiente 1 h.
- Controles: (a) vector digerido sin ligasa, (b) vector digerido + ligasa sin
  inserto.
- Transforma en una cepa de clonaje corriente (DH5α o similar). **No clones
  directamente en ZYCY10P3S2T**: esa cepa es para producir minicírculo, no para
  construir. Pasa el plásmido ya verificado a ZYCY10P3S2T al final.

### 6.5 Cribado — y un aviso que puede ahorrarte una semana

**Comprueba los marcadores de resistencia de los dos plásmidos.** El pCMV6-Entry
es **kanamicina/neomicina** y los parentales de minicírculo de SBI son, muy
probablemente, **también kanamicina**. Si es así, **la selección no discrimina
entre tu construcción y el plásmido donante arrastrado en la PCR**: las colonias
de arrastre crecen igual de bien y contienen un plásmido que expresa KRT10, de
modo que hasta una PCR con cebadores del inserto da positivo.

Defensas, por orden de importancia:

1. **DpnI sobre la reacción de PCR** (§6.1). Es la buena.
2. **Purificar la banda en gel**, no usar el producto en bruto.
3. **PCR de colonia con un cebador del vector + uno del inserto**: un cebador
   directo en el **EF1α** del pMC y un reverso dentro de KRT10. El donante no tiene
   EF1α → no amplifica. Esto distingue construcción real de arrastre; una PCR con
   dos cebadores del inserto, no.
4. **Digestión diagnóstica** con las enzimas de clonaje (libera el inserto) y con
   **PmeI o AsiSI** (lineariza; tamaño limpio). La herramienta calcula cuántas
   bandas esperar de cada una, y distingue si la diana cae en el esqueleto o dentro
   de la región att — sólo esta última sirve luego para el QC del minicírculo.

---

## 7. Verificación del clon

No des por bueno nada antes de esto:

1. **Secuencia completa del inserto y de las dos uniones.** El inserto son ~1,75
   kb: con Sanger hacen falta 3–4 lecturas más las uniones. **La cola de glicinas,
   repetitiva y muy GC, es exactamente donde Sanger falla** — y es también donde
   una polimerasa puede haber deslizado. Pide química para GC si hace falta.
2. **Mejor todavía: secuenciación del plásmido entero** por nanoporo (tipo
   Plasmidsaurus). Cuesta parecido a cuatro reacciones Sanger, cubre el vector
   completo y **detecta reordenamientos que las lecturas de Sanger del inserto no
   ven**, incluidas deleciones en la región att, que aquí serían fatales y
   silenciosas.
3. **Comprueba explícitamente** que: (a) el ATG está donde debe con su Kozak,
   (b) hay dos stops y no hay etiqueta detrás, (c) **attB y attP están intactos**,
   y (d) la traducción del inserto coincide con K10 silvestre de referencia,
   incluido el número de repeticiones de glicina de la cola.

> Sobre (d): el dominio de cola de K1/K10 tiene **polimorfismo de longitud** en el
> número de repeticiones ricas en glicina. Que tu clon difiera del RefSeq en esa
> región puede ser un alelo normal, no un error de PCR. Anótalo y decide a
> conciencia; no lo "corrijas" por reflejo.

---

## 8. De plásmido parental a minicírculo

1. Transforma el parental verificado en **ZYCY10P3S2T**.
2. Induce con **L-arabinosa** siguiendo el manual de SBI al pie de la letra
   (incluida la bajada de temperatura). No improvises concentraciones: el
   rendimiento es sensible y el protocolo está publicado.
3. **QC del minicírculo — los cuatro controles:**

   | Control | Qué esperas |
   |---|---|
   | Gel del preparado | Una especie, claramente menor que el parental |
   | Digestión que linearice | Banda única al tamaño calculado (~3,2–3,5 kb) |
   | PCR sobre la **unión att híbrida** | **Positiva** — esa unión sólo existe si la recombinación ocurrió |
   | PCR/qPCR del **esqueleto** (KanR u ori) | **Negativa o residual** — cuantifica el parental remanente |

   La recombinación attB × attP genera dos uniones híbridas (attL y attR); el
   minicírculo se queda con una de ellas, cuál depende de la orientación de los
   sitios en el mapa — mira el GenBank y diseña los cebadores sobre la que le
   toque. El tercer control y el cuarto son los que de verdad importan: el tercero
   demuestra que hay minicírculo, y el cuarto que **no** estás transfectando parental sin
   recombinar. Un preparado "de minicírculo" con parental residual invalida
   cualquier comparación de silenciamiento del promotor, porque el parental sí
   lleva esqueleto bacteriano (que es justo lo que dispara el silenciamiento).

4. **Entrega:** minicírculo es DNA y no atraviesa una barrera epidérmica intacta.
   Para equivalentes 3D, **electropora o transfecta los queratinocitos en monocapa
   antes de sembrarlos**, no el equivalente ya formado (tu §4.4).

---

## 9. Lo que este diseño te habilita: qPCR específica de transgén

Consecuencia directa de clonar **CDS + SV40 polyA** y no la 3'UTR nativa. El mRNA
del transgén y el endógeno tienen extremos 3' distintos, así que:

| Ensayo | Directo | Reverso | Mide |
|---|---|---|---|
| **Transgén** | final del CDS de KRT10 | dentro del **SV40 polyA** | sólo el minicírculo |
| **Endógeno** | final del CDS de KRT10 | dentro de la **3'UTR de KRT10** | sólo el alelo propio |
| **Total** | dentro del CDS | dentro del CDS | los dos |

Con esos tres ensayos cierras de una vez el experimento que tu §4.1 pide: **qPCR
del transgén ± diferenciación**. Si el mRNA del transgén cae al diferenciar, es el
vector (silenciamiento del promotor); si se mantiene y lo que cae es la proteína,
es biología. Y como el par es idéntico salvo por el cebador reverso, las
eficiencias son comparables.

Ojo con un detalle: el transgén es **cDNA sin intrones**, así que los cebadores
que abarcan intrones no sirven para discriminar, y **el DNA plasmídico del propio
minicírculo amplifica en la qPCR**. Trata la muestra con DNasa y monta el control
sin retrotranscriptasa: aquí no es una formalidad, es imprescindible.

---

## 10. Reactivos: qué falta de verdad

| Reactivo | ¿Bloquea? | Comentario |
|---|---|---|
| **Polimerasa de alta fidelidad** | **Sí, de verdad** | Q5 / Phusion / Platinum SuperFi. No hay sustituto |
| **DpnI** | Casi | Sin ella, arrastre de donante con la misma resistencia (§6.5) |
| **Fosfatasa (rSAP)** | No, pero cómprala | Matizado en §6.3: con dianas próximas es tu única defensa contra el vector cortado una vez |
| T4 DNA ligasa, kit de gel, competentes | Comprueba que hay | Rutina |
| **ZYCY10P3S2T** | Sí, para producir | Sólo a investigadores sin ánimo de lucro |
| Kit Gibson/HiFi | Sólo si Plan B | — |

La colección heredada de Thermo/Fermentas sin fechar: como ya decías, **sólo como
respaldo**, y con digestión control de DNA de lambda antes de confiar en ella.

---

## 11. Lo que NO hay que hacer

Recopilado, porque todas son decisiones que parecen razonables:

- ❌ Clonar el cDNA completo con su 3'UTR → pierdes la discriminación transgén/endógeno.
- ❌ Conservar la etiqueta Myc-DDK → cola C-terminal comprometida.
- ❌ Usar XbaI junto con NheI → mismo saliente `CTAG`.
- ❌ Gastar AsiSI o PmeI en el clonaje → las necesitas de diagnóstico.
- ❌ Usar Taq para el inserto.
- ❌ Clonar en cualquier sitio único "que haya" → tiene que estar **dentro de attB–attP**.
- ❌ Forzar una G en la posición +4 del Kozak → cambia el segundo aminoácido.
- ❌ Introducir los cambios wobble antes de elegir el shRNA.
- ❌ Construir en ZYCY10P3S2T.
- ❌ Fiarse de una PCR de colonia con dos cebadores del inserto.

---

## 12. Nota sobre KRT1

Tu §7 deja abierto si empezar por KRT10 o por KRT1/189del, con un argumento fuerte
a favor de KRT1 (3 pb de diferencia en vez de 1, y el ratón het con fenotipo severo
rescatable). Este diseño es para KRT10, que es lo que has pedido, pero **es
transferible literalmente a KRT1**: mismo vector, misma estrategia, mismos
controles; sólo cambia el CDS. La herramienta acepta cualquier donante. Si acabáis
adelantando KRT1, no hay que rediseñar nada, sólo volver a ejecutarla.

---

## 13. Resumen de lo que queda por tu parte

1. Descargar los dos GenBank (§1).
2. Ejecutar la herramienta y **mirar los primeros y últimos 12 aminoácidos** (§5.3).
3. Confirmar en NEBcloner: compatibilidad en rCutSmart de la pareja elegida y
   sensibilidad a Dam/Dcm de lo que la herramienta marque con ⚠️.
4. Confirmar el número de catálogo del parental al pedir (§1).
5. Comprobar los marcadores de resistencia de los dos plásmidos (§6.5).
6. Pedir la polimerasa de alta fidelidad y DpnI (§10).
