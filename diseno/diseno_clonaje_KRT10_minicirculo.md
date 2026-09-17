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

### 3.6 El MCS real y la elección de la pareja de enzimas

El MCS del parental es (48 nt facilitados):

```
        1      7      13     16     21        30     36       44
        TCTAGAGCTAGCGAATTCGAATTTAAATCGGATCCGCGGCCGCGTCGA…
        └XbaI─┘└NheI─┘└EcoRI┘
                      └BstBI┘
                           └──SwaI──┘
                                    └BamHI┘
                                          └──NotI──┘
                                                   └SalI (truncada)

EF1α  ──────────────────────────────────────────────────────►  SV40 polyA
```

| # | Enzima | Diana | Posición | Saliente | ¿En el congelador? |
|---|---|---|---|---|---|
| 1 | **XbaI** | `T^CTAGA` | 1–6 | `CTAG` | **sí** |
| 2 | **NheI-HF** | `G^CTAGC` | 7–12 | `CTAG` | **sí** |
| 3 | EcoRI | `G^AATTC` | 13–18 | `AATT` | no |
| 4 | BstBI | `TT^CGAA` | 16–21 | `CG` | no |
| 5 | SwaI | `ATTT^AAAT` | 21–28 | romo | no |
| 6 | **BamHI-HF** | `G^GATCC` | 30–35 | `GATC` | **sí** |
| 7 | NotI | `GC^GGCCGC` | 36–43 | `GGCC` | no |
| 8 | SalI | `G^TCGAC` | 44– | `TCGA` | no |

**Esto obliga a corregir la recomendación anterior.** En el documento previo
proponía **NheI + XhoI**; **en este MCS no hay XhoI**. Tampoco hay AsiSI ni PmeI.
De tus seis enzimas, sólo tres están aquí: **XbaI, NheI y BamHI**.

Tres observaciones antes de elegir:

- **Lo que has pegado termina en `GTCGA`, que es una diana SalI (`GTCGAC`) cortada
  por la mitad.** El MCS sigue un poco más allá de donde copiaste. Sin
  consecuencias para el diseño, pero conviene saberlo.
- **BstBI solapa con EcoRI** (`GAATTCGAA`): usar una destruye la otra. Irrelevante
  aquí, pero no cuentes con las dos.
- **SwaI no es PmeI.** `ATTT^AAAT` frente a `GTTT^AAAC`. Tu PmeI no corta aquí.

#### La pareja

> ## **NheI-HF (extremo 5') + BamHI-HF (extremo 3')**

Por qué esta y no otra:

1. **Las dos están ya en tu congelador.** Cero coste, cero espera.
2. **Salientes incompatibles**, `CTAG` frente a `GATC` → clonaje direccional real:
   el vector no se recirculariza y el inserto no puede entrar invertido.
3. **Las dos son versiones HF**, sin actividad *star*. Y como todas las HF de NEB
   están formuladas para CutSmart, **la doble digestión va en un solo tubo con
   rCutSmart** (confírmalo en NEBcloner, pero es lo esperable).
4. **Ninguna de las dos tiene problema de metilación en este contexto.** Lo he
   comprobado sobre tu secuencia: el entorno de NheI (`TAGAGCTAGCGAAT`) está
   limpio, y aunque el de BamHI contiene un `GATC` —dentro de su propia diana—
   **a BamHI no la bloquea Dam**.
5. **Deja `NotI` y `SalI` intactas por detrás del inserto.** NotI es un cortador de
   8 pb: si es única en el parental, es tu enzima de linearización para el
   diagnóstico. Estás conservando deliberadamente una herramienta de control.

**Por qué no XbaI**, aun estando en el congelador y siendo la más 5':

- Genera **el mismo saliente `CTAG` que NheI** → no puedes usar las dos.
- **La bloquea la metilación Dam si queda como `GATCTAGA`.** Por detrás tiene `GC`,
  así que ese lado está limpio, **pero lo que hay inmediatamente por delante no me
  lo has dado**: si el vector termina en `…GA` justo antes del `TCTAGA`, XbaI
  sencillamente no corta, y **no da ninguna señal de que no ha cortado**. NheI no
  tiene ese riesgo.
- No es versión HF.

#### Qué hacer si el CDS de KRT10 lleva una de las dos dianas

Es la única incógnita que queda, y es real: en un CDS de ~1,75 kb la probabilidad
de que aparezca un `GGATCC` o un `GCTAGC` ronda el 35 % para cada uno. **Compruébalo
antes de pedir oligos** — es instantáneo:

```bash
python3 disena_clonaje.py --donante ../secuencias/pCMV6-KRT10.gb \
        --mcs tctagagctagcgaattcgaatttaaatcggatccgcggccgcgtcga
```

| Situación | Qué hacer |
|---|---|
| Ninguna corta | **NheI-HF + BamHI-HF.** Adelante, no compras nada |
| **BamHI** corta el CDS | **NheI-HF + NotI-HF.** NotI es de 8 pb: ~97 % de probabilidad de estar ausente del CDS. Hay que comprarla (NEB R3189) |
| **NheI** corta el CDS | **EcoRI-HF + BamHI-HF** (R3101). Descarta XbaI salvo que confirmes su contexto Dam en el mapa |
| Cortan las dos | **EcoRI-HF + NotI-HF** |
| Cortan casi todas | Plan B: ensamblaje Gibson (§4) |

La herramienta ordena las parejas por sí misma con este criterio (las del
congelador primero, premiando HF y penalizando el riesgo Dam) y te marca la
recomendada.

#### Una comprobación que tienes que hacer en el mapa

**La orientación.** He supuesto que el MCS está escrito en el sentido de la
transcripción, es decir que **XbaI queda del lado del promotor EF1α y SalI del lado
del SV40 polyA**. Es lo normal, pero es una suposición sobre un dato que no tengo.

Si fuera al revés, **los papeles se invierten**: BamHI iría en el cebador directo y
NheI en el reverso. La regla es sencilla: **el sitio del cebador directo es el que
queda más cerca del EF1α.** Míralo una vez en el GenBank y ya está. (Si le pasas
`--aceptor` junto con `--mcs`, la herramienta localiza el MCS en el plásmido y te
avisa si aparece en la hebra contraria.)

#### Qué se pierde y qué sobrevive

Al clonar entre NheI (7) y BamHI (30) **desaparecen EcoRI, BstBI y SwaI**, que
quedan en medio. Sobreviven **XbaI** por delante y **NotI + SalI** por detrás.
Perder SwaI —un cortador de 8 pb— es el único peaje, y se compensa de sobra con
quedarte NotI.

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

Con la pareja elegida, los cebadores quedan **completos salvo la zona que aparea
contra KRT10**, que es lo único que depende de una secuencia que no tengo:

**Directo (5'→3'):**

```
CACCAC      GCTAGC      GCCACC      ATG NNNNNNNNNNNNNNNNNN
└protección └NheI-HF    └Kozak      └inicio del CDS (18–21 nt, Tm ≈ 62 °C)
```

**Reverso (5'→3'):**

```
CACCAC      GGATCC      TCATTA                     NNNNNNNNNNNNNNNNNNNNN
└protección └BamHI-HF   └ = TAA TGA en la hebra    └complementario inverso del
                          codificante (dos stops)    final del CDS, SIN su stop
```

Notas sobre cada bloque:

- **6 bases de protección.** Las enzimas cortan mal en el extremo de un fragmento.
  He comprobado que `CACCAC` pegado a `GCTAGC` y a `GGATCC` **no crea ningún
  `GATC` nuevo ni ningún sitio Dcm (`CCWGG`)**.
- **`TCATTA` es el complementario inverso de `TAATGA`.** En el cebador reverso los
  stops van escritos al revés. Verificado reconstruyendo el amplicón.
- **La zona de apareamiento se ajusta por Tm**, no por longitud fija, y se prefiere
  terminar en G o C (pinza 3').

### 5.1b Cómo quedan las uniones en el clon final

Sirve de lista de comprobación cuando te llegue la secuencia:

**Unión 5'** (la NheI se regenera):

```
…EF1α… TCTAGA G CTAGC GCCACC ATG TCT …
       └XbaI  └─NheI─┘ └Kozak└ATG del CDS
        (sobrevive, del vector)
```

**Unión 3'** (la BamHI se regenera):

```
… última base del CDS  TAA TGA  G GATCC  GCGGCCGC  GTCGAC … SV40 polyA
                       └2 stops └─BamHI─┘ └─NotI──┘ └SalI─┘
                                          (sobreviven, del vector)
```

Si al secuenciar ves exactamente esto, el clonaje ha salido.

### 5.2 Cómo obtener las secuencias literales

**Ahora mismo, sólo con el donante y el MCS** (no hace falta el GenBank del
parental para obtener los cebadores):

```bash
cd herramientas
python3 disena_clonaje.py \
    --donante ../secuencias/pCMV6-KRT10.gb \
    --mcs tctagagctagcgaattcgaatttaaatcggatccgcggccgcgtcga \
    --salida  ../diseno/informe_KRT10.md
```

**Cuando tengas el GenBank del parental** (necesario antes de digerir, porque es lo
único que demuestra que las dianas son únicas en todo el plásmido y que el MCS cae
dentro de attB–attP):

```bash
python3 disena_clonaje.py \
    --donante ../secuencias/pCMV6-KRT10.gb \
    --aceptor ../secuencias/pMC.EF1a-MCS-SV40polyA.gb \
    --mcs tctagagctagcgaattcgaatttaaatcggatccgcggccgcgtcga \
    --salida  ../diseno/informe_KRT10.md
```

Devuelve un informe con los cebadores completos, sus Tm, GC, horquillas, dímeros
3', los tamaños de amplicón/inserto/vector/minicírculo, los avisos de metilación y
las digestiones diagnósticas. Sin conexión a internet.

Opciones útiles:

| Opción | Para qué |
|---|---|
| `--mcs <seq>` | Trabajar sólo con el MCS, sin el GenBank del parental |
| `--pareja NheI-HF,BamHI-HF` | Forzar una pareja concreta |
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
- **NheI-HF y BamHI-HF son las dos versiones HF, así que van en rCutSmart en un
  solo tubo.** Confírmalo en NEBcloner igualmente, que cuesta un minuto.
- El molde de la digestión del inserto es **producto de PCR, no metilado**: la
  metilación Dam sólo condiciona el corte del **vector**, y ahí ya está comprobado
  que ni NheI ni BamHI tienen problema en este contexto.
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
4. **Digestión diagnóstica** en dos frentes:
   - **NheI-HF + BamHI-HF** → debe liberar el inserto (~1,8 kb).
   - **Una enzima que linearice.** La candidata natural es **NotI**, que sobrevive
     justo por detrás del inserto y es cortador de 8 pb — siempre que sea única en
     el parental. Si no la tienes, **AsiSI o PmeI** sirven igual si resultan ser
     únicas en el plásmido: ninguna de las dos está en el MCS, así que dependen de
     lo que haya en el resto del vector. La herramienta te lo cuenta en cuanto le
     pases el GenBank, y distingue si la diana cae en el esqueleto o dentro de la
     región att — **sólo esta última sirve luego para el QC del minicírculo**, que
     ya no tiene esqueleto.

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
- ❌ Contar con XhoI, AsiSI o PmeI para clonar en este MCS → **no están en él**.
- ❌ Confundir SwaI (`ATTTAAAT`) del MCS con tu PmeI (`GTTTAAAC`).
- ❌ Gastar en el clonaje una enzima que te sirva de diagnóstico (NotI sobrevive
  por detrás del inserto: consérvala).
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

**Para cerrar los cebadores (hoy, sólo necesitas el donante):**

1. Poner el GenBank de `pCMV6-KRT10` en `secuencias/`.
2. Ejecutar la herramienta en modo `--mcs` (§5.2) y **mirar los primeros y últimos
   12 aminoácidos que imprime** (§5.3).
3. Ver si el CDS lleva `GCTAGC` o `GGATCC` y aplicar la tabla de §3.6. Si no lleva
   ninguna, **pides los oligos y no compras ninguna enzima**.

**Antes de tocar el banco:**

4. Conseguir el GenBank del parental y volver a ejecutar con `--aceptor`. Es lo
   único que comprueba que las dianas son **únicas en todo el plásmido** y que el
   MCS cae **dentro de attB–attP**. Sin eso no se digiere.
5. Confirmar en el mapa la **orientación del MCS** respecto a EF1α (§3.6).
6. Comprobar los marcadores de resistencia de los dos plásmidos (§6.5).
7. Pedir la polimerasa de alta fidelidad, DpnI y rSAP (§10).
8. Confirmar el número de catálogo del parental al pedir (§1).
