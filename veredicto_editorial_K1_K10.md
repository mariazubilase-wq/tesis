# Veredicto editorial — paper K1/K10

> Lectura del plan como lo leería un editor de revista: no "¿está descrito?" sino
> "¿hay un avance mecanístico declarable, y sobrevive a revisión?".
> Complementa `busqueda_novedad_K1_K10.md`. Fecha: 2026-10-08.
> Bibliografía de **PubMed**; DOIs enlazados.

---

## 1. La pregunta que hace un editor primero

*"¿Cuál es el avance, en una frase, y por qué no podía escribirse antes?"*

El plan responde hoy: *"la cantidad de K1 la fija la disponibilidad de partner, no
su expresión"*. **Ese es el problema.** Esa frase se podía escribir en 1988 —
Domenjoud la escribió ([DOI](https://doi.org/10.1016/0014-4827(88)90274-1)). Un
editor con el campo en la cabeza la lee y hace desk reject sin mandar a revisión.

Pero la frase está mal elegida, porque **el plan propone en realidad un mecanismo
distinto del publicado**, y no lo está vendiendo. Lo que sigue es la separación
entre fenómeno (ocupado) y mecanismo (libre).

---

## 2. Fenómeno vs mecanismo: qué modelo tiene cada uno

### El modelo de 1988–89 (Domenjoud, Kulesh): binario y constitutivo

Lo que esos papers establecen, leído con cuidado:

- Una molécula de queratina está **o en filamento (estable) o fuera (degradada)**.
- La degradación es **constitutiva**: *"cells that normally express keratins
  contain a proteolytic system"*. Es limpieza de fondo, una propiedad del estado
  de la molécula.
- La constante de degradación es **fija**. No depende de la carga del sistema.
- **No hay mecanismo.** Kulesh dice *"proteolytic system"* porque en 1989 no podía
  decir más: no hay proteasa identificada, ni ubiquitina, ni autofagia, ni
  receptor. Es una caja negra nombrada.
- **Y el dato de trans no es estequiométrico.** El K18 que desestabilizaba el pool
  endógeno era un **truncado** sin cola C-terminal y sin parte del rod. Eso es un
  dominante-negativo clásico: se incorpora, envenena la red, y los restos se
  aclaran. El mecanismo es **sabotaje estructural**, no competencia por partner.
  Kulesh **nunca** mostró que *más proteína silvestre* dé *menos proteína total*.

**Predicción del modelo binario:** añades K1 → el exceso se recorta → el total
**se estanca en el techo** que sostiene el K14 disponible. El K1 que ya estaba
protegido **sigue protegido**.

### El modelo del plan: capacidad limitada, inducible, autoamplificante

- `k_deg` **no es constante**: es función de la fracción sin emparejar.
- El sistema tiene **retroalimentación positiva**: más K1 → más huérfano → se
  degrada más rápido *todo* el K1, incluido el previamente estable.
- Tres submecanismos distinguibles: titración del partner, **inducción** de la
  maquinaria, agrefagia/co-degradación con nucleación cooperativa.

**Predicción del modelo del plan:** añades K1 → el total cae **por debajo del
parental**. No monotónico. El pool preexistente **no está protegido**.

### Dónde está la línea

| | 1988–89 | Plan |
|---|---|---|
| Huérfano inestable | ✅ descrito | — |
| Partner estabiliza | ✅ descrito | — |
| Hace falta estado polimerizado | ✅ insinuado (con truncado) | limpio con K10 no-ensamblable |
| **k_deg función de la carga** | ❌ | **libre** |
| **Total cae por debajo del basal** | ❌ | **libre** |
| **El huérfano induce su propia vía** | ❌ | **libre** |
| **Identidad de la vía (autofagia/p62 vs proteasoma)** | ❌ ("proteolytic system") | **libre y disputado** |
| **Regla de partición monómero/polímero** | ❌ | **libre** |
| **Jerarquía cuantitativa de partners** | ❌ | **libre** |
| **Degrón / determinante de reconocimiento** | ❌ | **libre, y en todo el campo de FI** |

**La frase editorialmente defendible es ésta:**

> *El aclaramiento de K1 no emparejada no es limpieza constitutiva del exceso: es
> un proceso dependiente de carga que reajusta a la baja el pool completo de K1,
> incluido el ya ensamblado.*

Kulesh es dueño de *"la queratina huérfana es inestable"*. **Nadie es dueño de
*"el aclaramiento es regulado, dependiente de carga, y redefine la abundancia de
todo el pool"*.** Lo primero es un fenómeno. Lo segundo es un mecanismo. Y la
diferencia es exactamente lo que separa un desk reject de un paper.

---

## 3. El problema serio: la novedad vive en los experimentos que faltan

Siendo duro — y esto es lo que diría un editor tras leer §3 del plan:

Los tres datos que distinguen el modelo nuevo del de 1989 **no están hechos**:

| Dato discriminante | Estado |
|---|---|
| CHX chase: ¿sube k_deg con la carga? | **pendiente** (§11.2) |
| Dosis-respuesta inducible: ¿cae por debajo del parental de forma graduada? | **pendiente** (§6, artefacto de clon) |
| Flujo autofágico elevado en transfectado vs parental (¿inducción?) | **pendiente** (§4 Fig. 3) |

Lo que **sí** hay —Westerns de estado estacionario en clones, cloroquina parcial,
dispasa— es compatible con el modelo de 1989 **y** con artefacto de clon **y** con
artefacto de tag. Los tres a la vez.

Dicho de otro modo: el plan tiene razón en que el CHX chase *"decide si hay
paper"*, pero subestima por qué. No es sólo una validación. **Es el único dato que
convierte un resultado de 1989 en un resultado de 2026.**

---

## 4. Donde muere el manuscrito en revisión (y no es por novedad)

Un editor manda a revisión y los revisores probables son Magin, Leube, Coulombe,
Eckhart. Esto es lo que escriben:

**🔴 Revisor 1, párrafo 2 — el tag.** *"El constructo lleva Myc-DDK en C-terminal,
enmascarando la cola de K1. El constructo que en Kulesh et al. 1989
desestabilizaba el pool endógeno de queratinas carecía precisamente de la cola
C-terminal. Los autores no pueden distinguir vigilancia estequiométrica de un
dominante-negativo por enmascaramiento de cola."*

Esto no es una petición de revisión: es un **rechazo**. No hay respuesta posible
sin el experimento. El plan lo marca como "lo más urgente" en §6 — es correcto,
pero la justificación es más fuerte de lo que el plan sabe: no es que el tag
*podría* interferir, es que **el tag reproduce la arquitectura del control
positivo histórico del artefacto**.

**🔴 Revisor 1, párrafo 3 — el clon.** Clon estable vs parental sin pasar, para el
resultado estrella. Rechazo. Inducible o varios clones + policlonal. El plan lo
sabe (§6).

**🟠 Revisor 2 — prioridad.** *"La estabilización mutua de queratinas tipo I y II
y la degradación del miembro no emparejado están establecidas (Domenjoud 1988,
Kulesh 1989). Los autores deberían explicar qué añaden."* **Contestable** — con el
argumento de §2 de este documento, y sólo si los datos cinéticos existen. Sin
ellos, no.

**🟠 Revisor 3 (Eckhart, si va a JID) — la vía.** *"Jaeger et al. 2019 mostró por
proteómica que la deleción de Atg7 en epitelios no aumenta las queratinas en uña
corneificada; la especificidad de sustrato de la autofagia depende de la
accesibilidad fuera del citoesqueleto"*
([DOI](https://doi.org/10.1007/s10495-018-1505-4)). Contestable: corneificación
normal in vivo ≠ desbalance de partner en cultivo. **Pero hay que escribirlo en el
manuscrito antes de que lo escriba él.**

**🟠 Todos — "autofagia" no es un mecanismo.** Cloroquina parcial + bafilomicina es
*farmacología*, y un rescate parcial con un solo inhibidor se lee como *"la vía no
está establecida"*. El plan tiene razón en que la parcialidad es informativa, pero
eso sólo funciona **después** de la validación genética (ATG7/ATG5, p62). Antes,
se lee como experimento incompleto. **La validación genética no es opcional para
una afirmación mecanística.**

---

## 5. Veredicto por revista

Probabilidades honestas, con la decisión que tomaría el editor:

| Paquete | JCB | JID | J Cell Sci / LSA | Exp Dermatol / IJMS |
|---|---|---|---|---|
| **Datos actuales** (estado estacionario, clones, tag, CQ parcial, dispasa) | desk reject | desk reject o reject tras revisión | reject tras revisión | **aceptable** |
| **+ CHX chase, control de tag, inducible con dosis-respuesta, flujo** | desk reject | **~40–50 % tras revisión mayor** | ~50 % | seguro |
| **+ validación genética de autofagia + Fig. 6 (K10 que une pero no polimeriza)** | ~25–30 % | **probable** | **probable** | — |
| **+ mapeo del degrón** | **otro paper, mejor** → EMBO J / Nat Commun | — | — | — |

El §10 del plan se califica solo bien: *"Exp Dermatol, IJMS (Q2) — donde caerías
solo con Westerns de estado estacionario + co-IP + NanoBiT"*. Correcto. El salto a
JID no lo da una figura más: lo da **pasar de estado estacionario a cinética**.

---

## 6. La oportunidad — versión corregida

> ⚠️ **Corrección de una versión anterior de este documento.** Afirmé que
> `intermediate filament degron` = 0 resultados en PubMed demostraba que *"no se ha
> mapeado un determinante de degradación en ninguna proteína de filamento
> intermedio"*. **Ese negativo no valía.** "Degron" es jerga del campo de
> ubiquitina; nadie publica *"mapeamos el degrón de una queratina"*, publica *"el
> dominio X es necesario para la acumulación"*. Buscando por los términos reales,
> el mapeo existe — y está en *Cell*. Ver §6-bis.

### 6-bis. Lo que sí está mapeado (y yo había dado por libre)

**🔴 Lu X, Lane EB (1990).** *Retrovirus-mediated transgenic keratin expression in
cultured fibroblasts: specific domain functions in keratin stabilization and
filament formation.* Cell 62:681–96.
[DOI](https://doi.org/10.1016/0092-8674(90)90114-t)

Textual, según PubMed — y nótese que separan tres niveles:

> *"Three levels of assembly show a different stringency for the involvement of
> individual keratin domains: **protein accumulation requires the alpha helix
> domains**; stable filament formation additionally requires both N- and
> C-terminal domains of either one of the two interacting keratins...; and higher
> order organization of the cytoplasmic network depends on **correct type I–type II
> pairing** of keratins."*

Es decir: **mapeo por dominios de qué necesita una queratina para acumularse** —
o sea, para escapar a la degradación — publicado en Cell en 1990. Y además
disocian acumulación / ensamblaje estable / organización de red, que es justo la
lógica de la Fig. 6 del plan.

Y hay toda una literatura de deleciones sobre el destino de FI truncadas:

- **Hatzfeld M, Weber K (1990).** *Tailless keratins assemble into regular
  intermediate filaments in vitro.* J Cell Sci 97:317–24.
  [DOI](https://doi.org/10.1242/jcs.97.2.317) → la cola **no** es necesaria para
  formar filamentos, ni en tipo I ni en tipo II.
- **Bader BL, Magin TM, Freudenmann M, Stumpp S, Franke WW (1991).** *Intermediate
  filaments formed de novo from tail-less cytokeratins in the cytoplasm and in the
  nucleus.* J Cell Biol 115:1293–307.
  [DOI](https://doi.org/10.1083/jcb.115.5.1293) → pares sin cola forman FI
  regulares, pero **se acumulan en el núcleo**; sin cola *y* sin cabeza dan
  depósitos no fibrilares nucleares; sin cabeza sola se quedan en citoplasma.
- **Andreoli JM, Trevor KT (1994).** *Fate of a headless vimentin protein in stable
  cell cultures: soluble and cytoskeletal forms.* Exp Cell Res 214:177–88.
  [DOI](https://doi.org/10.1006/excr.1994.1247) → vimentina sin cabeza expresada
  hasta **7× el endógeno**, mayoritariamente **soluble**, *"without deleterious
  cellular effects"*. **Una FI no ensamblada que NO se degrada.** Contraejemplo
  directo a "no ensamblado = degradado", y relevante para la rama "soluble" de la
  Fig. 1 del plan.

### 6-ter. Qué queda libre de verdad, dicho con precisión

No esto: *"nadie ha mapeado un determinante de degradación en una FI"* — falso.

Sí esto, que es más estrecho pero sigue siendo real y no lo cubre Lu & Lane:

1. **Resolución de residuo, no de dominio.** Lu & Lane trabajan con deleciones de
   dominios completos y atribuyen la acumulación al rod. Nadie ha bajado a
   residuos.
2. **Ningún determinante se ha ligado a una maquinaria concreta.** Lu & Lane
   describen el requisito; no hay ligasa, ni receptor, ni vía asociada a ese
   dominio.
3. **Nadie ha mostrado que lo que se lee sea la ocupación del partner.** "Requiere
   el rod para acumularse" es compatible con "necesita plegarse bien". La
   hipótesis de ERISQ/UBE2O es distinta y más fuerte: que la señal es una
   **superficie de la interfaz de heterodimerización** que el partner entierra, y
   que su exposición es lo que se reconoce.

Esa tercera es la que vale, y es la que explicaría la jerarquía K10 > K14 sin
postularla. Pero hay que plantearla **citando a Lu & Lane como punto de partida**,
no como hueco virgen. Y el marco general ya fijó el estándar de qué cuenta como
mecanismo:

- **ERISQ** (Sung et al. 2016, eLife, [DOI](https://doi.org/10.7554/eLife.19105)):
  Tom1/Huwe1 ubiquitina proteínas ribosómicas no ensambladas *"primarily via
  residues that are **concealed in mature ribosomes**"*.
- **UBE2O** (Yanagitani, Juszkiewicz & Hegde 2017, Science,
  [DOI](https://doi.org/10.1126/science.aan0178)): reconoce *"juxtaposed basic and
  hydrophobic patches on unassembled proteins"*. α-globina sin β-globina →
  ubiquitinada.

En los dos casos el principio es el mismo: **la señal de degradación es una
superficie que el ensamblaje entierra.** Eso da una hipótesis concreta y
comprobable para K1: *el determinante de degradación está en la interfaz de
heterodimerización con K10.*

Por qué esto lo cambia todo, en lenguaje de editor:

1. Deja de ser "caracterizamos un fenómeno" y pasa a ser **"identificamos cómo la
   célula lee la estequiometría de queratinas"**. Eso es mecanismo.
2. **Explica la jerarquía de partners sin postularla.** Si K14 entierra la interfaz
   sólo parcialmente, el techo bajo deja de ser una observación y se vuelve una
   consecuencia. Eso cierra la Fig. 5 de verdad.
3. **Generaliza a 54 queratinas** y a los filamentos intermedios en general. Un
   editor compra generalidad.
4. Es un experimento acotado: mutagénesis de la interfaz 1A/2B en K1 y medir
   estabilidad. No requiere un modelo nuevo.

Y conecta con lo que ya hay en casa: el mutante de K10 de §6/Fig. 6 es el
experimento recíproco. Los dos brazos del mismo mecanismo.

**Pero con la guardia alta, a la luz de §6-bis:** Lu & Lane ya atribuyeron la
acumulación al rod por deleción de dominios. Una mutagénesis de interfaz que
reduzca la estabilidad se leerá, por defecto, como *"has desestabilizado el
plegamiento del rod, que es lo que Lu & Lane ya dijo"*. Para que el experimento
signifique lo que se quiere que signifique hacen falta dos controles que el marco
ERISQ/UBE2O impone:

- una mutación de interfaz que **mantenga** el plegamiento y la capacidad de unir
  K10 pero cambie la superficie expuesta (no un desestabilizante genérico), y
- demostrar que el efecto **desaparece en ausencia de la maquinaria** (p62/ATG7, o
  la ligasa), que es lo que separa "lee la interfaz" de "está mal plegado".

Sin esos dos, el mapeo no sube de tier: repite 1990 con más resolución.

---

## 7. Las dos formas en que el paper se cae

Conviene tenerlas escritas antes de invertir meses.

**Colapso 1 — el CHX chase sale plano.** Si la vida media de K1 es igual en
parental y transfectado, el total bajo es transcripcional, traduccional o de clon.
**No hay paper.** El plan ya lo dice y tiene razón.

**Colapso 2 — el que el plan no contempla.** Si con sistema inducible el K1 total
**se estanca** en vez de caer por debajo del parental, el resultado es
*exactamente* Domenjoud/Kulesh: techo por disponibilidad de partner, degradación
constitutiva del exceso. Sigue siendo un dato correcto y publicable, pero es
**confirmación en células humanas de un resultado de 1988**. Eso es Exp Dermatol.
El sobredisparo por debajo del basal no es un detalle cuantitativo: **es la
totalidad de la novedad mecanística.**

Corolario práctico: la dosis-respuesta inducible no es un control del artefacto de
clon. Es **el experimento que define qué paper estás escribiendo**. Merece el mismo
rango que el CHX chase en §11, no estar enterrada en §6 como mitigación de riesgo.

---

## 8. Reordenación de §11 según valor editorial

El orden del plan es razonable pero no está ordenado por *qué decide el destino
del manuscrito*. Propuesta:

1. **Control del tag** (K1 sin tag o N-terminal). Bloqueante. Sin esto nada de lo
   demás es interpretable, y es el primer párrafo del rechazo. *El plan lo pone
   tercero.*
2. **CHX chase parental vs transfectado.** Decide si hay mecanismo nuevo.
3. **Inducible con dosis-respuesta.** Decide **cuál** de los dos mecanismos tienes
   → decide la revista. *El plan lo tiene como mitigación, no como experimento.*
4. **Flujo autofágico transfectado vs parental.** Inducción vs saturación: es el
   submecanismo más vendible de los tres de §1.
5. **Validación genética de autofagia** (ATG7/ATG5, p62). Convierte farmacología
   en mecanismo. *El plan lo pone noveno — demasiado tarde.*
6. Reanálisis del material existente (Western de K1/K10 en las líneas de dispasa).
   Barato, ya está en casa, y da la cadena causal de §5.
7. Fraccionamiento + IF con pre-extracción.
8. qPCR 3'UTR vs ORF-tag.
9. Co-expresión K14 vs K10.
10. Dispasa a tiempos largos → el cruce.
11. **Nuevo: mapeo del determinante en la interfaz con K10**, con los dos controles
    de §6-ter (mutación que conserve plegamiento y unión; dependencia de
    maquinaria). Si 1–5 salen bien, esto es lo que sube de tier. Leer Lu & Lane
    1990 antes de diseñarlo.

---

## 9. Resumen para decidir

- **¿Se puede publicar?** Sí. No como está planteado, y no en el sitio que el plan
  espera por defecto.
- **¿El concepto es novedoso?** No. Está publicado en 1988–89 y el plan lo vende
  como tesis central. Hay que reescribir §1 y los dos títulos candidatos.
- **¿El mecanismo es novedoso?** Sí: la dependencia de carga, la inducción, la
  identidad de la vía y la regla monómero/polímero están libres. Pero ninguno está
  demostrado aún.
- **¿Y el mapeo del determinante?** Libre **sólo a resolución de residuo y ligado a
  maquinaria**. El mapeo por dominios está hecho desde 1990 (Lu & Lane, *Cell*):
  la acumulación requiere el rod. Ver §6-bis y §6-ter.
- **¿Cuál es el riesgo real?** No la prioridad. **El tag y el clon.** Dos
  confundidores que convierten el resultado estrella en ininterpretable. El del
  tag, eso sí, es **más contestable de lo que yo dije**: ver §10.
- **¿Qué hacer primero?** Tag, CHX chase, inducible. En ese orden. Tres
  experimentos que caben en un trimestre y que determinan si esto es JID o IJMS.
- **¿Qué cambiaría el techo?** Mostrar que lo que se lee es **la ocupación del
  partner** y no el plegamiento: interfaz + dependencia de maquinaria. Eso sí no
  lo tiene nadie, y ERISQ/UBE2O predicen dónde buscarlo.

---

## 10. Corrección al §6 del plan: el tag no es lo que el plan dice que es

El plan justifica el riesgo del tag así: *"Myc-DDK va en C-terminal → tapa la cola
de K1, que es justo la región implicada en interacciones con desmoplaquina"*.

**Eso es incorrecto.** Según PubMed:

**Meng JJ, Bornslaeger EA, Green KJ, Steinert PM, Ip W (1997).** *Two-hybrid
analysis reveals fundamental differences in direct interactions between
desmoplakin and cell type-specific intermediate filaments.* J Biol Chem
272:21495–503. [DOI](https://doi.org/10.1074/jbc.272.34.21495)

Textual: el C-terminal de desmoplaquina *"interact[s] with at least two regions of
the **head domain** of the type II epidermal keratin K1"*, y *"the interaction
between DPCT and K1 **requires the keratin head domain**"*.

La región de K1 relevante para desmoplaquina es la **cabeza**, que el tag
C-terminal deja libre.

**Esto es, en conjunto, buena noticia, y reordena el riesgo:**

| Objeción | Estado real |
|---|---|
| "El tag tapa el sitio de desmoplaquina" | **Falso** (Meng 1997: es la cabeza) |
| "El tag impide el ensamblaje" | **Improbable**: la cola no es necesaria para formar FI, ni in vitro (Hatzfeld & Weber 1990) ni en células (Bader/Magin 1991) |
| "El tag causa la degradación que atribuyes a la falta de K10" | **Improbable por la vía esperada**: la acumulación requiere el **rod**, no la cola (Lu & Lane 1990) |
| "El tag perturba la localización" | **Real y poco intuitivo**: las queratinas sin cola se acumulan en el **núcleo** (Bader/Magin 1991). Mirar la IF con esto en mente |
| "Es el truncado de Kulesh otra vez" | **Contestable**: el de Kulesh perdía cola **y parte del rod**; es el rod lo que gobierna la acumulación |

Consecuencia práctica: la objeción del tag **se puede responder con citas**, no
sólo con un experimento nuevo. Eso rebaja el riesgo de rechazo del párrafo 2 de
Revisor 1 que describí en §4 — sigo recomendando el control de K1 sin tag porque es
barato y blinda la figura principal, pero deja de ser el bloqueante absoluto que
dije. **El clon, en cambio, sigue siéndolo.**

Y hay que corregir el plan en dos sitios más: su §6 afirma que el tag compromete
*"cualquier afirmación sobre anclaje desmosómico"* — lo contrario es lo cierto, el
sitio de DP queda libre; y su §8 propone el eje desmosómico sin saber que el
contacto DP–K1 está mapeado a la cabeza, lo cual **ayuda** a ese bloque.

---

*Bibliografía recuperada de PubMed. DOIs enlazados en el texto.*
