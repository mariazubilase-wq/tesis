# Producción de minicírculos — sistema de System Biosciences (cepa ZYCY10P3S2T)

**Desarrolla la §8 del documento de clonaje.** Qué hace el sistema, cómo se ejecuta
en tu laboratorio, qué controles son obligatorios, qué cuesta y qué alternativas hay.

---

## 0. En una frase

El minicírculo no se "purifica" ni se "sintetiza": **se fabrica dentro de la
bacteria**. Tú transformas el plásmido parental ya verificado en una cepa de
*E. coli* modificada, le añades **L-arabinosa**, y la propia bacteria (a) recombina
el plásmido en dos círculos y (b) destruye el que lleva el esqueleto bacteriano.
Lo que sacas con una maxiprep normal es, mayoritariamente, el minicírculo.

Coste real de la operación una vez montada: **una tarde de trabajo y ~20 € de
fungible por preparación**. El gasto está todo en la compra inicial.

---

## 1. Qué está verificado y qué no

| Afirmación | Estado |
|---|---|
| Mecanismo (φC31, I-SceI, arabinosa, LacY A177C) | Publicado: Kay, He y Chen, *Nat Biotechnol* 2010 |
| Rendimiento 3,4–4,8 mg/L de cultivo | **Cifra del artículo original.** Es la mejor de las publicadas; no la tomes como lo que vas a obtener tú |
| Esquema del protocolo (30 °C, 16 h, +medio de inducción, 5–5,5 h) | Ficha y manual del fabricante, consultados por búsqueda |
| **Precios** | **Listados sueltos de distribuidores, septiembre de 2026.** Orientativos: varían por país, IVA y descuento académico. Pide presupuesto |
| Composición exacta del medio de inducción del kit | **No verificada.** SBI no publica la fórmula. Lo que sí está publicado es la versión "casera" (§7.3) |

**Lo que tienes que hacer tú antes de ejecutar nada:** descargar el **manual de
producción de minicírculos de SBI** (`Minicircle-production-manual-V8`, PDF público
en su web) y seguirlo al pie de la letra. Este documento te explica *por qué* hace
cada cosa y *qué comprobar*; no lo sustituye.

---

## 2. El mecanismo: qué tiene esa bacteria dentro

El nombre de la cepa **es** su genotipo, y conviene leerlo porque explica el
protocolo entero:

| Trozo del nombre | Qué es | Para qué |
|---|---|---|
| **10P** | **10 copias** del casete `BAD→φC31 integrasa`, integradas en 3 loci del cromosoma (2 en Δ*endA*, 4 en *araD*, 4 en *galK*) | Recombina attB × attP |
| **3S** | **3 copias** en tándem del casete `BAD→I-SceI`, en el locus *UMU* | Destruye el esqueleto |
| **2T** | **2 copias** del **transportador** de arabinosa `LacY A177C`, constitutivo | Que la inducción sea uniforme en toda la población |

Tres consecuencias prácticas que salen directamente de ahí:

1. **`BAD` es el promotor del operón de la arabinosa.** Por eso se induce con
   L-arabinosa y por eso no puede haber glucosa en el medio (represión por
   catabolito). No cambies el medio por uno que lleve glucosa.
2. **`LacY A177C` es la clave silenciosa del sistema.** El transportador de
   arabinosa silvestre da inducción "todo o nada": unas bacterias se inducen y
   otras no, y las no inducidas te dejan parental sin recombinar. Esta mutación
   hace la entrada de arabinosa independiente de la inducción, y con eso la
   población se induce de golpe. Es la razón por la que esta cepa funciona y las
   anteriores rendían poco.
3. **Δ*endA*** — la cepa no tiene endonucleasa I. Buena calidad de DNA en la
   maxiprep, como cualquier cepa de clonaje decente.

### 2.1 Qué pasa cuando añades arabinosa

```
   PARENTAL  ──attB──[ EF1α · KRT10 · SV40pA ]──attP──[ KanR · ori · 32×I-SceI ]──
                              │
                     φC31 integrasa (attB × attP)
                              ↓
   MINICÍRCULO                        +      ESQUELETO (círculo aparte)
   ──attR──[ EF1α·KRT10·SV40pA ]──           ──attL──[ KanR · ori · 32×I-SceI ]──
   sin dianas I-SceI  →  SOBREVIVE           32 dianas I-SceI  →  DESTRUIDO
```

- La **recombinación φC31** entre `attB` y `attP` parte el plásmido en dos círculos.
  Las dos uniones híbridas resultantes se llaman `attL` y `attR`; **una queda en el
  minicírculo y la otra en el esqueleto** — cuál de las dos depende de la
  orientación de los sitios en tu mapa, y eso decide el cebador del control de QC
  (§5.3).
- La **I-SceI** es una meganucleasa de 18 pb. Su diana no existe en el genoma de
  *E. coli* ni en tu casete: sólo en el esqueleto, **32 veces**. El esqueleto se
  hace picadillo. Y el parental que no llegó a recombinar también lleva esas 32
  dianas, así que **también se destruye**: por eso el sistema es limpio y no
  simplemente "enriquecido".
- Lo que queda intacto en la bacteria es el minicírculo. Es un círculo de DNA
  **no replicativo** (se ha quedado sin origen de replicación), así que no se
  amplifica más: lo que hay es lo que se recombinó. De ahí que el cultivo tenga que
  estar denso *antes* de inducir.

### 2.2 Por qué no es perfecto

Siempre queda algo de parental y de esqueleto. Puede ser un 1 % o puede ser un
30 %, según cómo haya ido la inducción. **Esto no es un detalle de manual: en tu
proyecto invalida el experimento.** Si comparas silenciamiento del promotor entre
minicírculo y plásmido y tu "minicírculo" lleva 20 % de parental, estás comparando
una mezcla contra un plásmido. Por eso la §5 de este documento es obligatoria, no
recomendable.

---

## 3. Por qué minicírculo, en este proyecto concreto

Lo general (lo dice cualquier ficha):

- **Sin esqueleto bacteriano → sin silenciamiento.** Los motivos CpG no metilados
  del esqueleto reclutan metilación y heterocromatinización del transgén, y además
  activan TLR9. Es la razón de que un plásmido normal exprese unos días y luego se
  apague. El minicírculo mantiene expresión **semanas**.
- **Más pequeño → más moléculas por microgramo y mejor entrada.** Con ~3,3 kb
  frente a los ~6,5 kb del parental, el mismo µg son casi **el doble de moléculas**.
- **Sin gen de resistencia a antibiótico.** Argumento de bioseguridad que te vale
  para el capítulo de discusión.

Lo específico de una ictiosis epidermolítica, que es lo que de verdad decide:

| Hecho | Consecuencia |
|---|---|
| El minicírculo es **episomal y no replicativo** | Se diluye a cada división celular |
| El queratinocito **basal** divide | Ahí la expresión se pierde: publicado ~14 días en células en división |
| El queratinocito **suprabasal diferenciado** no divide | Ahí se mantiene: meses en células que no dividen |
| K10 se necesita **precisamente en el suprabasal** | **La biología juega a tu favor**: la célula donde quieres el transgén es la que no lo diluye |

Y la limitación honesta, que conviene escribir en la tesis antes de que te la
escriban en el tribunal: **un minicírculo no cura una ictiosis**. La epidermis se
renueva desde la célula basal, que sí divide, así que el efecto es temporal por
construcción. Lo que un minicírculo sí es:

1. **Una herramienta de prueba de concepto excelente** — demuestras que el
   reemplazo de K10 corrige el fenotipo celular, sin el ruido del silenciamiento y
   sin integrar nada.
2. **Un formato preclínico realista para piel**, que es un órgano al que se puede
   volver a dosificar (a diferencia del hígado o el pulmón). Repetir dosis tópica o
   intradérmica no es una fantasía.
3. **La base de una versión persistente**, si hiciera falta: existen minicírculos
   con elemento **S/MAR**, que se replican episómicamente y resisten la dilución.
   Es un vector más grande y más delicado; menciónalo como vía futura, no lo
   intentes ahora.

---

## 4. El flujo completo, desde donde te deja el documento de clonaje

### Fase 0 — Requisitos previos

- Plásmido parental con KRT10 **secuenciado entero** (§7 del documento de clonaje).
  En particular, **attB y attP intactos**: una deleción ahí es silenciosa en el
  clonaje y catastrófica aquí.
- **ZYCY10P3S2T**. Comprada, o cedida por otro grupo (§9: la licencia lo permite
  entre investigadores sin ánimo de lucro).
- Un **matraz de 2 L** libre. No es un chiste: en el paso de inducción el volumen
  se dobla (§4.2), y 400 ml en un matraz de 500 ml no airean.
- Incubador de agitación que **mantenga 30 °C**, no sólo 37 °C.

### Fase 1 — Transformar la cepa productora

Igual que cualquier transformación, con tres matices:

- **20–100 ng** de plásmido parental verificado. No hace falta más.
- Recuperación y crecimiento **a 30 °C**, no a 37 °C.
- Selección en **LB/kanamicina 50 µg/ml**.
- **Haz stock de glicerol de 3–4 colonias en cuanto crezcan**, antes de nada. Es
  lo que hace que no tengas que volver a comprar células competentes nunca: de aquí
  en adelante cada producción arranca de una estría del stock. *Anota la fecha y la
  colonia; verifica el stock por digestión diagnóstica una vez.*

> **No construyas en esta cepa** (ya estaba en el documento de clonaje). Clona en
> DH5α, verifica, y sólo entonces pasa a ZYCY10P3S2T. Un plásmido parental viviendo
> en la cepa productora está expuesto a fugas basales del promotor BAD.

### Fase 2 — La producción propiamente dicha (2 días)

| Cuándo | Qué | Detalle |
|---|---|---|
| **D1, mañana** | Colonia fresca → **2 ml LB/Kan**, 30 °C, 250 rpm, 4–6 h | Arranque. También vale 1 h si la colonia es grande |
| **D1, tarde** | Pasar 0,5–1 ml a **200 ml LB/Kan** en matraz de 2 L | Relación de volumen generosa: la aireación importa |
| **D1 → D2** | **16 h, 30 °C, 250 rpm** | Toda la noche. Debe quedar denso |
| **D2, mañana** | Añadir **200 ml de medio de inducción** (arabinosa) al mismo matraz | El volumen pasa a 400 ml. **Sin kanamicina** |
| **D2** | **5–5,5 h a 30 °C** (el artículo original usa 32 °C) | Aquí es donde ocurre todo |
| **D2, tarde** | Centrifugar 1.500 × g, 15 min | Sedimento: maxiprep ya, o congelar a −20 °C |
| **D2/D3** | **Maxiprep** + tratamiento de DNasa dependiente de ATP | §4.3 |

### Fase 3 — Purificación

- Sirve **cualquier maxiprep de columna** (Qiagen, Macherey-Nagel, Zymo…). No hay
  nada mágico en el kit de SBI. Si vas a transfectar queratinocitos primarios o a
  hacer algo *in vivo*, usa una versión **libre de endotoxinas**; es el punto donde
  merece la pena gastar.
- **Tratamiento con DNasa dependiente de ATP** (la "Plasmid-Safe" o equivalente,
  que es lo que el kit de SBI llama su reactivo de re-purificación): degrada DNA
  **lineal** y respeta el circular cerrado. Elimina (a) el DNA genómico arrastrado
  y (b) **los fragmentos lineales del esqueleto cortado por I-SceI**. En este
  sistema no es un lujo de pureza: es parte del método.
- Cuantifica con **Qubit**, no con NanoDrop. El NanoDrop cuenta cualquier ácido
  nucleico, incluido el RNA y los restos de esqueleto; aquí eso te miente
  justamente en la dirección que no quieres.

### Fase 4 — Rendimiento que puedes esperar

El artículo original da **3,4–4,8 mg por litro** de cultivo para minicírculos de
2,2–6,0 kb. Traducido a una preparación de 200 ml: **0,7–1 mg en el mejor caso**.
Cuenta en la práctica con **200–600 µg**, que para un proyecto de cultivo celular
es muchísimo: son decenas de nucleofecciones. Si sacas menos de 50 µg, algo ha
fallado en la inducción (§6).

---

## 5. QC del minicírculo: los cinco controles

Los cuatro primeros ya estaban en el documento de clonaje; aquí van con el cómo.

### 5.1 Gel

Corre en paralelo: parental sin inducir | preparación de minicírculo | marcador.
Debes ver **una especie claramente más pequeña**. Ojo: el DNA circular
superenrollado **no corre a su tamaño real**, así que el gel es cualitativo. No
midas tamaños aquí.

### 5.2 Digestión que linearice

Es el control de tamaño de verdad. **Y aquí hay una trampa específica de este
sistema que conviene ver antes de gastar enzima:**

> Una enzima con diana única **en el esqueleto** no corta el minicírculo — en el
> minicírculo esa diana **ya no existe**. Y una enzima con diana única en la región
> att lineariza limpiamente el minicírculo, pero sobre el parental puede dar otro
> patrón.

Esto es útil: **elige una enzima de cada tipo y tienes un test de dos colores.**
La herramienta `disena_clonaje.py` ya te dice de cada diana si cae dentro o fuera
de attB–attP, que es exactamente esta distinción. Las reservadas **AsiSI** y
**PmeI** son las candidatas; comprueba en el informe cuál cae dónde.

| Enzima | Sobre el parental | Sobre el minicírculo puro |
|---|---|---|
| Diana única **dentro** de att | Lineariza al tamaño del parental (~6,5 kb) | Lineariza a ~3,2–3,5 kb |
| Diana única **en el esqueleto** | Lineariza | **No corta**: sigue circular |

### 5.3 PCR de la unión att híbrida → **positiva**

La unión `attR` (o `attL`, según tu mapa) **sólo existe si la recombinación
ocurrió**. Un cebador a cada lado: el producto es la prueba directa de que hay
minicírculo. Mira el GenBank para saber cuál de las dos uniones se queda tu
minicírculo y diseña sobre esa.

### 5.4 qPCR del esqueleto (KanR u *ori*) → **negativa o residual, y cuantificada**

El control que de verdad importa y el que casi todo el mundo se salta. No basta con
"no sale banda": **cuantifica**. Una qPCR de KanR normalizada contra una qPCR del
casete te da el **% de parental remanente** en la preparación.

- Curva patrón: diluciones del **plásmido parental sin inducir**.
- Declara el número en la tesis. Un ≤1–2 % es bueno; >10 % obliga a repetir la
  producción antes de usar ese lote para comparar con plásmido.

### 5.5 Endotoxina (sólo si vas a queratinocito primario o piel)

Los queratinocitos primarios son sensibles y responden a LPS. Kit de maxiprep
libre de endotoxinas y, si el experimento es un equivalente 3D o un injerto,
mídela (ensayo LAL).

---

## 6. Las trampas, por orden de frecuencia

1. **Incubar a 37 °C.** La recombinación y el plegado de las enzimas están
   optimizados a 30–32 °C. A 37 °C el rendimiento cae.
2. **Kanamicina durante la inducción.** No la pongas: el medio de inducción va sin
   antibiótico. Y no puedes seleccionar el minicírculo con antibiótico nunca —
   no lleva gen de resistencia, ése es el objetivo.
3. **Matraz pequeño.** 400 ml después de la inducción. Sin aireación no hay
   inducción homogénea.
4. **pH.** La versión casera del medio de inducción requiere **ajustar a pH 7,0–7,3
   con NaOH**; el cultivo denso ha acidificado el medio y la inducción sufre. El
   medio comercial del kit ya viene tamponado.
5. **Cultivo poco denso al inducir.** El minicírculo no se replica: lo que hay es
   lo que se recombinó. Si la noche no ha crecido bien, no compenses alargando la
   inducción — vuelve a empezar.
6. **Glucosa en el medio.** Reprime el promotor BAD. LB normal no lleva; algunos
   medios ricos sí. Míralo.
7. **Saltarse la DNasa dependiente de ATP.** Te llevas el esqueleto troceado en la
   preparación y lo cuantificas como si fuera minicírculo.
8. **Re-estriar la cepa muchas veces.** Trabaja siempre desde el stock de glicerol
   congelado, no desde una placa de hace tres semanas.
9. **Cuantificar con NanoDrop y comparar dosis en µg.** Ver §7.1.

---

## 7. El día a día: cuánto necesitas y cuánto cuesta

### 7.1 La equivalencia molar, que es el error clásico

Si comparas minicírculo contra plásmido parental **a igual masa**, estás dando casi
el doble de copias del minicírculo, y entonces no sabes si la diferencia es la
ausencia de esqueleto o la dosis. **Compara en moles.**

```
copias ∝ masa / (pares de bases × 650)

minicírculo KRT10 ≈ 3,3 kb   →  1 µg ≈ 2,8 × 10¹¹ moléculas
parental con KRT10 ≈ 6,5 kb  →  1 µg ≈ 1,4 × 10¹¹ moléculas
                                 (confirma los dos tamaños en tu mapa)
```

Regla práctica: **para igualar moléculas, da al parental ~2× la masa del
minicírculo.** Y declara en el pie de figura que la comparación es molar. Esto por
sí solo distingue un experimento publicable de uno discutible.

### 7.2 Cuánto DNA gasta cada cosa

| Experimento | DNA por punto | Comentario |
|---|---|---|
| Nucleofección de queratinocitos (10⁶ células) | 0,5–2 µg | El método de elección: ~50 % de eficiencia en queratinocito primario, muy por encima de la lipofección |
| Lipofección en placa de 24 pocillos | 0,25–0,5 µg | Para HEK293T y puesta a punto |
| Un experimento completo con réplicas y controles | 20–50 µg | |
| **Una preparación de 200 ml** | **200–600 µg** | **Da para 10–20 experimentos** |

Es decir: **produces pocas veces**. Una preparación por constructo, alicuotada a
−20 °C, te cubre meses. No montes un sistema de producción continuo.

### 7.3 Dinero: qué comprar de verdad

**Precios orientativos de listados de distribuidores, septiembre de 2026.** Varían
por país; pide presupuesto con descuento académico.

| Ref. | Producto | Precio listado | ¿Imprescindible? |
|---|---|---|---|
| `MN502A-1` | Vector parental `pMC.EF1α-MCS-SV40polyA`, 10 µg | ~**950 $** (un listado) | **Sí.** Es el punto de partida, y se compra una vez |
| `MN900A-1` | **ZYCY10P3S2T competentes** | ~**680 €** | **Sí.** O consíguela cedida |
| `MN850A-1` | Solución de arabinosa 20 % | Bajo | **No.** L-arabinosa a granel cuesta céntimos |
| `MN920A-1` | **Kit MC-Easy completo** (5 preps): cepa + medio de inducción + kit de re-purificación + agua libre de endotoxinas | ~**1.285–1.296 €** | **No, pero cómodo** |
| `MN910A-1` | MC-Easy **sin** células competentes | Menor | Si ya tienes la cepa |

**Las dos rutas:**

| | **Ruta kit** | **Ruta mínima** (recomendada) |
|---|---|---|
| Compras | `MN502A-1` + `MN920A-1` | `MN502A-1` + `MN900A-1` + L-arabinosa a granel |
| Coste inicial | ≈ **2.100–2.200 €** | ≈ **1.500–1.600 €** |
| Medio de inducción | Viene hecho | **200 ml LB + 200 µl de arabinosa al 20 %, ajustado a pH 7,0–7,3 con NaOH.** Publicado |
| Purificación | Kit de SBI, 5 preps | Tu maxiprep habitual + DNasa dependiente de ATP |
| Se agota | **Sí, a las 5 preparaciones** | **No** |

La ruta mínima ahorra ~600 € y, sobre todo, **no se agota**: con el stock de
glicerol de §4.1 y arabinosa a granel, el coste marginal de cada producción baja a
**el precio de una maxiprep, ~15–25 €**. Si tu grupo va a hacer los tres
constructos previstos (reemplazo, shRNA, combinado) y sus variantes, la diferencia
es grande.

Si compras el kit, que sea por una razón concreta: que nadie en el laboratorio
haya hecho esto antes y quieras eliminar variables la primera vez. Es un argumento
legítimo.

### 7.4 Lo que se te va a olvidar presupuestar

| Concepto | Orden de magnitud |
|---|---|
| Kit de maxiprep **libre de endotoxinas** | 200–400 € la caja |
| DNasa dependiente de ATP (si vas por la ruta mínima) | ~200 € |
| Secuenciación nanoporo del parental (tipo Plasmidsaurus) | 15–25 € por plásmido |
| Cebadores del QC (unión att + esqueleto) | ~20 € |
| Reactivo de nucleofección de queratinocitos | **El gasto recurrente real**: cientos de € por caja de 24 reacciones |

Dicho de otro modo: **el minicírculo no es lo caro de tu proyecto. Lo caro es
metérselo a las células.**

---

## 8. Alternativas, por si el sistema de SBI no encaja

| Opción | Cuándo tiene sentido | Pega |
|---|---|---|
| **SBI ZYCY10P3S2T** (esto) | Laboratorio académico, varios constructos, control total | Inversión inicial; hay que aprenderlo |
| **Servicio a medida de SBI** | Quieres el minicírculo y no el sistema | Caro por lote, dependes del calendario del proveedor. Pide presupuesto a `services@systembio.com` |
| **PlasmidFactory** (Alemania) | Necesitas escala grande o grado preclínico/GMP | Sólo servicio; presupuesto a medida |
| **Nanoplasmid™ (NTC / Aldevron)** | Alternativa técnicamente elegante: esqueleto de ~500 pb con origen de replicación de RNA-OUT, **sin recombinación ni inducción** | Licencia comercial; la cepa no es de libre circulación académica |
| **DNA "doggybone" (dbDNA, Touchlight)** | Lineal, cerrado por horquillas, enzimático, sin bacteria | Servicio, no algo de banco |
| **Plásmido normal, y punto** | Puesta a punto, HEK293T, cribado de shRNA | **Se silencia al diferenciar.** Justo tu variable de interés |

**Para tu caso concreto y ahora mismo, la respuesta es SBI**: ya tienes el diseño
de clonaje hecho contra su vector parental, la licencia académica te cubre, y lo
que necesitas son microgramos, no miligramos. La conversación sobre Nanoplasmid o
GMP es de dentro de dos años, si el proyecto llega ahí.

Un apunte metodológico que sí merece la pena: hay protocolos recientes (2025) que
**eliminan pasos de limpieza posteriores a la inducción y reportan hasta 10× más
rendimiento**. Si el rendimiento se te queda corto, mira ahí antes de rediseñar
nada.

---

## 9. Licencia: leerlo antes, no después

**La cepa ZYCY10P3S2T y los plásmidos parentales sólo se venden a investigadores
sin ánimo de lucro.** Los usuarios comerciales sólo pueden comprar minicírculo ya
fabricado.

Para una tesis esto no es un problema. Pero **sí lo es el día que el trabajo se
quiera trasladar**, spin-off o licencia de por medio. Anótalo ahora en el capítulo
de materiales y que tu director lo sepa: no es una sorpresa agradable a los tres
años. La vía comercial existe (el servicio de fabricación), pero cambia el modelo
de costes por completo.

---

## 10. Lo que NO hay que hacer

- ❌ Construir o clonar en ZYCY10P3S2T. Se transforma ya verificado.
- ❌ Inducir a 37 °C.
- ❌ Poner kanamicina en el medio de inducción.
- ❌ Inducir en un matraz que no aguante el doble de volumen.
- ❌ Usar un medio con glucosa.
- ❌ Dar por bueno un minicírculo con un gel y nada más.
- ❌ Saltarse la **cuantificación** del parental remanente (§5.4) — y luego comparar
  con plásmido.
- ❌ Comparar minicírculo y plásmido **a igual masa**.
- ❌ Cuantificar con NanoDrop.
- ❌ Comprar el kit de 5 preparaciones sin haber mirado la ruta mínima.
- ❌ Transfectar el equivalente 3D ya formado (ya estaba en §8 del otro documento:
  se nucleofecta en monocapa, antes de sembrar).

---

## 11. Checklist de pedido

1. [ ] Confirmar la referencia del parental al pedir: `MN502A-1`. La serie MN5xx
       tiene variantes muy parecidas (`MN511A-1`, `MN512A-1`, `MN531A-1`).
2. [ ] Pedir a SBI el **GenBank** del parental con el pedido (lo necesitas para
       `disena_clonaje.py` y para saber qué unión att lleva tu minicírculo).
3. [ ] Decidir **ruta kit** o **ruta mínima** (§7.3).
4. [ ] Preguntar antes: **¿hay ya un ZYCY10P3S2T en el instituto?** Es lo primero
       que hay que descartar; la licencia académica permite la cesión y son 680 €.
5. [ ] Comprobar que hay incubador de agitación a 30 °C y matraz de 2 L.
6. [ ] Presupuestar el kit de maxiprep libre de endotoxinas.
7. [ ] Diseñar los cebadores del QC (unión att + KanR) **a la vez** que los de
       clonaje: es el mismo pedido de oligos y sale más barato.
