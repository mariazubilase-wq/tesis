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

## 6. La oportunidad que el plan no ve

`intermediate filament degron` en PubMed = **0 resultados**.
`degron buried interface orphan quality control` = **0 resultados**.

**No se ha mapeado un determinante de degradación en ninguna proteína de filamento
intermedio.** Y el campo general ya fijó el estándar de qué cuenta como mecanismo:

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
11. **Nuevo: mapeo del degrón en la interfaz con K10.** Si 1–5 salen bien, esto es
    lo que sube de tier.

---

## 9. Resumen para decidir

- **¿Se puede publicar?** Sí. No como está planteado, y no en el sitio que el plan
  espera por defecto.
- **¿El concepto es novedoso?** No. Está publicado en 1988–89 y el plan lo vende
  como tesis central. Hay que reescribir §1 y los dos títulos candidatos.
- **¿El mecanismo es novedoso?** Sí, y más de lo que el plan cree: la
  dependencia de carga, la inducción, la identidad de la vía, la regla
  monómero/polímero y el degrón están todos libres. Pero ninguno está demostrado
  aún.
- **¿Cuál es el riesgo real?** No la prioridad. **El tag y el clon.** Dos
  confundidores que convierten el resultado estrella en ininterpretable, y uno de
  ellos reproduce la arquitectura exacta del artefacto de 1989.
- **¿Qué hacer primero?** Tag, CHX chase, inducible. En ese orden. Tres
  experimentos que caben en un trimestre y que determinan si esto es JID o IJMS.
- **¿Qué cambiaría el techo?** El degrón. Nadie ha mapeado uno en ningún filamento
  intermedio, y el marco general (ERISQ, UBE2O) ya predice dónde buscarlo.

---

*Bibliografía recuperada de PubMed. DOIs enlazados en el texto.*
