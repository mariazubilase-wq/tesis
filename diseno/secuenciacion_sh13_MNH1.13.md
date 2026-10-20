# Lectura de la secuenciación — clones MNH1.13.1 a 13.5 (constructo 2)

Cinco ficheros `.ab1` de un 3500 (KB 1.4.2.4, POP7, BDTv3), cebador directo
sobre el H1. Analizados contra el recombinante esperado
`pSI-H1 + sh13` (vector hasta 2929 + oligo TOP + vector desde 2939).

> ## Veredicto: **ninguno de los cinco sirve.** Hay que volver a empezar el cribado.

---

## 1. Resumen

| Clon | Lectura | Qué ha salido | Sirve |
|---|---|---|---|
| **13.1** | 1093 nt, Q media 39 | Inserto presente, pero **deleción de 3 nt (`GGC`) en el brazo sentido** | ❌ |
| **13.2** | — | **Reacción fallida**, sin señal | sin datos |
| **13.3** | 1089 nt, Q media 39 | **Sin inserto, y deleción de 794 pb que se lleva el attP** | ❌❌ |
| **13.4** | — | **Reacción fallida**, sin señal | sin datos |
| **13.5** | — | **Reacción fallida**, sin señal | sin datos |

---

## 2. Las tres reacciones fallidas (13.2, 13.4, 13.5)

No son clones malos: **son secuenciaciones que no han salido.** El basecaller
devuelve `NNNNN` y Q = 0 en los cinco únicos puntos que llama.

La traza cruda lo confirma — hay electroforesis, pero no hay señal:

| Clon | Bases | Pico máximo por canal | Lectura |
|---|---|---|---|
| 13.1 | 1093 | 427 / 470 / 476 / 393 | débil pero legible |
| **13.3** | 1089 | **2098 / 2248 / 1919 / 1577** | fuerte |
| 13.2 | 5 | 59 / 49 / 240 / 233 | ruido |
| 13.4 | 5 | 29 / 19 / 58 / 16 | **ruido puro** |
| 13.5 | 5 | 49 / 39 / 98 / 113 | ruido |

Fíjate además en la diferencia entre 13.1 (≈430) y 13.3 (≈2100): **hay un factor
5 de señal entre dos reacciones de la misma tanda.** Eso apunta a que el DNA no
va cuantificado o va muy desigual. Antes de repetir: cuantifica (Nanodrop o
Qubit) y normaliza todos los clones a la misma concentración.

---

## 3. Clon 13.1 — deleción de 3 nt en el tallo

```
esperado  GGATCC AATGACTGCCTGGCTTCCTTT CTTCCTGTCAGA AAAGGAAGCCAGGCAGTCATT TTTTT G AATTC
lectura   GGATCC AATGACTGCCT···TTCCTTT CTTCCTGTCAGA AAAGGAAGCCAGGCAGTCATT TTTTT G AATTC
                            ↑↑↑
                      faltan 3 nt (GGC)
```

Todo lo demás está perfecto: BamHI y EcoRI regeneradas, bucle íntegro,
**brazo antisentido (la guía) íntegro**, terminador con sus 5 T.

### Y la deleción es real, no un artefacto de la horquilla

Es la duda obligada: las horquillas comprimen la señal en Sanger y producen
deleciones falsas. Dos comprobaciones dicen que aquí no:

1. **Calidad alta justo en el punto.** Q = 49, 44, 53 en las bases que flanquean
   la deleción, con Q media de 48,5 en los 40 nt del tallo. Una compresión
   produce llamadas dudosas, no Q≈50.
2. **El espaciado entre picos es regular.** Mediana global 12,0 puntos; en los
   45 nt del tallo el máximo es 15. **No hay ningún hueco ancho**, que es la
   firma de una base que el llamador se ha saltado. Las bases no están porque no
   existen.

Es exactamente el modo de fallo que el diseño anticipaba (§7 de
`diseno_sh13_pSI_H1.md`): *«el tallo de 21 pb es el punto donde E. coli
delecciona, y una deleción parcial no se ve en ningún gel»*.

> **No lo uses, aunque la guía esté intacta.** El tallo queda con un bulto de
> 3 nt y el procesamiento por Dicer deja de ser el que has diseñado. Lo que
> midas con él no te dirá si sh13 funciona.

---

## 4. Clon 13.3 — el grave

No lleva inserto, y además ha perdido **794 pb del vector**:

```
lectura   …GTATGAGACCACTTGGATC | TCGAGTTAATAATTCAGAAGAACTCGTCAAGAAGGCGATAG…
             fin del H1 (≈2932)  ╵  posición 3728 del vector (zona del KanR)
```

La unión cae sobre un `GGATC` que existe en las dos posiciones (2929 y ≈3723):
una recombinación entre repeticiones cortas, el mecanismo clásico.

Lo que se lleva por delante:

| Elemento | Posición | |
|---|---|---|
| SV40 poly(A) | 3221–3352 | **perdido** |
| SV40 ori | 3361–3528 | **perdido** |
| **attP** | **3616–3654** | **PERDIDO** |
| KanR | 3977–4537 | conservado |

> ### Sin attP no hay recombinación ΦC31, y sin recombinación no hay minicírculo.
> Este clon crece en kanamicina y da un miniprep de aspecto normal. Es
> indistinguible de uno bueno salvo que lo mires.

---

## 5. Qué hacer

### 5.1 Un test de restricción que caza la deleción grande, por 1 €

**HindIII es de corte único en pSI-H1 (3046) y cae dentro del tramo que 13.3 ha
perdido.** Eso la convierte en el cribado perfecto *antes* de secuenciar:

| Clon | HindIII |
|---|---|
| Correcto | **linealiza** — una banda de ~6,9 kb |
| Tipo 13.3 | **no corta** — sigue superenrollado |

Un gel con los minipreps digeridos con HindIII te descarta los deletados sin
gastar una sola reacción de secuenciación. **Hazlo primero, siempre.**

(Lo que HindIII *no* detecta es la deleción pequeña del tallo de 13.1. Para eso
sigue haciendo falta secuenciar — no hay atajo.)

### 5.2 Repetir el cribado

1. **Digiere con HindIII** todos los minipreps que tengas. Descarta los que no
   linealicen.
2. **Secuencia 8–10 de los que pasen.** Con una horquilla, una fracción
   importante de los clones sale deletada: cinco colonias es poca muestra.
3. **Cuantifica y normaliza el DNA** antes de mandarlo. Tres de cinco reacciones
   fallidas y un factor 5 de señal entre las dos que salieron no es casualidad.
4. **Pide también una lectura con cebador reverso.** Leer el tallo desde los dos
   lados es lo que convierte una deleción «muy probable» en una certeza, y
   además cubre el tramo que el cebador directo lee con peor calidad.

### 5.3 Si vuelve a salir deletado

Pasa a **Stbl3 a 30 °C**, que es el remedio clásico para repeticiones invertidas
inestables y ya estaba previsto en §3.4 del diseño. Crece más despacio, pero las
horquillas sobreviven.

---

## 6. Lo que esta tanda sí confirma

No todo es malo: **la estrategia de clonaje funciona.** El clon 13.1 tiene el
inserto en el sitio correcto, en la orientación correcta, con las dos dianas
regeneradas y el terminador completo. La ligación de oligos hibridados entre
BamHI y EcoRI hace lo que tiene que hacer. El problema es la estabilidad de la
horquilla en la cepa, que es un problema conocido y con solución conocida.

---

# Segunda tanda — MNH1SC.1 a SC.5

**5 de 5 fallidas.** Con la primera tanda, el balance es **8 reacciones fallidas
de 10**.

## 7. No es el cebador

> ## El cebador anilla perfectamente. El problema es el DNA molde.

La prueba es directa: **el mismo cebador dio dos lecturas impecables de ~1090
bases** (13.1 y 13.3), con Q≥20 en 924 bases cada una. Un cebador que no anilla
falla 10 de 10, no 2 de 10 con lecturas de libro.

### Lo que dicen las trazas crudas

Medido sobre el envolvente de los cuatro canales, con el ruido de fondo de cada
fichero como referencia:

| Muestra | Bases | Q≥20 | Pico | Ruido | S/R | ¿Hay escalera? |
|---|---|---|---|---|---|---|
| **MNH1.13.1** | 1093 | **924** | 476 | 3 | 159 | **sí — 3221 scans** |
| **MNH1.13.3** | 1089 | **924** | 2248 | 22 | 102 | **sí — 10744 scans** |
| MNH1.13.2 | 5 | 0 | 240 | 2 | 120 | no — 54 scans |
| MNH1.13.4 | 5 | 0 | 58 | 20 | 2,9 | no — 0 scans |
| MNH1.13.5 | 5 | 0 | 113 | 6 | 18,8 | no — 0 scans |
| MNH1SC.1 | 5 | 0 | 91 | 33 | 2,8 | no — 0 scans |
| MNH1SC.2 | 5 | 0 | 98 | 29 | 3,4 | no — 0 scans |
| MNH1SC.3 | 5 | 0 | 115 | 2 | 57,5 | no — 0 scans |
| MNH1SC.4 | 133 | **0** | 576 | 2 | 288 | no — 536 scans |
| MNH1SC.5 | 5 | 0 | 72 | 3 | 24,0 | no — 0 scans |

**Ocho reacciones no tienen producto de extensión. No es que sea débil: no
existe.**

### El caso MNH1SC.4, que es el que lo demuestra

Es la muestra más informativa de las diez. Tiene un **pico de 576 — más alto que
13.1, que leyó 1093 bases.** Y sin embargo:

- No llama ni una sola base con Q≥20.
- La señal ocupa **536 scans de ~15 900**: un chorro aislado al principio de la
  carrera (scan ≈2057), no una escalera.
- De sus 133 bases «llamadas», sólo **15 caen sobre un pico de verdad**; el resto
  son ruido que el llamador interpreta como bases.
- **0 de 24** fragmentos de 15 nt de esa lectura existen en pSI-H1.

O sea: un **blob de colorante libre** y nada más. Si el problema fuera el cebador,
no habría ni eso.

## 8. Qué está pasando entonces

El patrón —unas pocas reacciones perfectas, la mayoría con cero producto, y
amplitudes que van de 58 a 2248 (**un factor 39**) entre reacciones que deberían
ser idénticas— sólo tiene una familia de causas: **el molde**.

Por orden de probabilidad:

1. **Va poco DNA.** La causa número uno. Para un plásmido de 6,9 kb hacen falta
   del orden de 300–600 ng por reacción; comprueba qué pide exactamente tu
   servicio.
2. **Hay inhibidores arrastrados del miniprep.** RNasa A residual, sales de
   guanidina, etanol, o resina de la columna. **Es la explicación clásica de
   «mismo protocolo, señal completamente distinta entre tubos».**
3. **Eluido en TE.** El EDTA quela el Mg²⁺ y frena la polimerasa. Eluye en agua
   o en EB.
4. **Cuantificación por Nanodrop.** Lee RNA y nucleótidos libres como si fueran
   DNA: puedes creer que mandas 400 ng y mandar 60.

Y hay un dato que apunta a algo sistemático: **la tanda SC falló entera, las
cinco.** Eso no es azar de pipeteo. Misma sesión de minipreps, mismo tampón de
elución, o un tubo de cebador mal diluido.

## 9. Qué hacer antes de volver a mandar

1. **Cuantifica con Qubit, no con Nanodrop.** Y mira los dos ratios:
   A260/A280 ≈ 1,8 y **A260/A230 > 2,0**. Un 230 bajo es carryover de guanidina
   o etanol, y es justo lo que mata estas reacciones.
2. **Normaliza todos los clones** a la concentración que pida el servicio. No
   mandes «lo que salga».
3. **Re-eluye en agua o EB**, nunca en TE.
4. **Mete un control conocido en la misma placa**: vuelve a mandar el DNA de
   13.3, que ya leyó a 2248 de pico. Es el experimento que separa las dos
   hipótesis de un plumazo:
   - control lee, el resto no → **es tu DNA**
   - no lee nada → es el servicio, el cebador o la química
5. **Pregunta al servicio si ellos vieron señal.** Si en su control interno todo
   fue bien, el problema entró con las muestras.

> **Lo que NO hay que hacer:** rediseñar el cebador. Funciona. Cambiarlo te
> costaría dos semanas y volverías al mismo sitio.

---

# 10. El dato que lo cierra: colonias PCR-positivas

Con la información nueva —**SC = scramble** (control negativo, otro inserto) y
**lo mismo pasa con el minicírculo de KRT10, con colonias positivas por PCR**—
el diagnóstico deja de ser una inferencia y pasa a ser una deducción.

| | sh13 | scramble | KRT10 |
|---|---|---|---|
| Vector | pSI-H1 | pSI-H1 | pMC.EF1α |
| Inserto | horquilla | horquilla distinta | cDNA de 1,76 kb |
| Cebador de secuenciación | H1 | H1 | otro |
| Colonia por PCR | — | — | **positiva** |
| Secuenciación | 3/5 sin señal | **5/5 sin señal** | sin señal |

> **Un problema que aparece en tres construcciones distintas, con dos vectores
> distintos y cebadores distintos, no puede ser un cebador.** Lo único que
> comparten las tres es el paso que va de la colonia al tubo que mandas: el
> miniprep.

Y la PCR de colonia lo remata: **la construcción está en la bacteria.** Entre
«la colonia es correcta» y «la secuenciación no da nada» sólo queda el miniprep
y la cuantificación.

> ⚠️ **Un matiz sobre esa PCR de colonia.** Si la hiciste con **dos cebadores del
> inserto**, el positivo no prueba que el clon sea bueno: amplifica igual el
> plásmido donante o el producto de PCR que quedó en el banco (está avisado en
> §11 del diseño de KRT10). Si usaste **uno del vector y otro del inserto**, el
> positivo sí vale. Merece la pena mirar cuál de las dos hiciste.

## 11. El primer experimento, que es gratis

**Corre 2 µL de cada miniprep en un gel de agarosa al 0,8 %.**

| Lo que ves | Qué significa |
|---|---|
| Banda de plásmido clara y nítida | Hay DNA → el problema es pureza o cantidad enviada |
| Banda muy débil o nada | **Hay poco DNA** → ahí está la respuesta |
| Mancha difusa por debajo | RNA sin digerir — y el Nanodrop lo cuenta como DNA |

Esto, más un Qubit, resuelve la pregunta en una tarde y sin gastar
secuenciaciones. **Hazlo antes que ninguna otra cosa.**

Comprueba también el rendimiento: estos parentales de minicírculo **no son
plásmidos pUC de alto número de copia**. Si de un miniprep estándar sacas menos
de ~100 ng/µL, crece 5 mL en vez de 2 y eluye en 30 µL en lugar de 50.

---

# 12. Cebadores nuevos

**No porque el actual esté roto** —dio dos lecturas de 1090 bases— sino porque
los nuevos arreglan dos cosas reales:

- El cebador actual empieza a leer **~54 nt antes del BamHI**, y de esos los
  primeros ~13 son N. Entra en la horquilla casi sin carrerilla. El nuevo le da
  **120 nt**.
- **No tienes lectura reversa.** Es la que convierte la deleción de 13.1 de «muy
  probable» en certeza, y la que cubre el lado 3' del inserto.

Todos verificados sobre las secuencias reales: **únicos en su plásmido**, sin
homopolímeros ≥5, anclaje 3' correcto y Tm calculada por vecino más próximo
(50 mM Na⁺, 0,25 µM).

### Para pSI-H1 — valen igual para sh13 y para el scramble

| | Secuencia 5'→3' | nt | Tm | GC | Posición | Lee desde |
|---|---|---|---|---|---|---|
| **H1seq-F** | `TGCGCCCTGGCAGGAAGATGGCTGT` | 25 | 58,8 °C | 64 % | 2785 | 120 nt antes |
| **H1seq-R** | `AGTCACACAACAGACGGGCACACACT` | 26 | 54,7 °C | 54 % | 3070 | 126 nt después |

`H1seq-R` tiene la Tm algo baja porque la zona (R/U5 del dLTR) es rica en AT; no
hay nada mejor ahí. A 50 °C de anillamiento va bien.

### Para el minicírculo de KRT10 (MN502A-1)

| | Secuencia 5'→3' | nt | Tm | GC | Posición | Lee |
|---|---|---|---|---|---|---|
| **K10seq-F** | `TCAGCCGGCTCTCCACGCTTTGCCT` | 25 | 58,6 °C | 64 % | 1275 | unión 5' desde 112 nt antes |
| **K10seq-R** | `TGCCTGACAACGGGCCACAACTCCT` | 25 | 56,7 °C | 60 % | 1602 | unión 3' desde 190 nt después |

**Las dos juntas no cubren el CDS entero.** Con ~900 bases útiles por lectura,
F llega hasta ≈790 del inserto y R retrocede hasta ≈1050: queda un **hueco de
unos 260 nt en medio**. Para cerrarlo hace falta **un cebador interno del CDS**,
que puedo diseñar en cuanto esté `secuencias/pCMV6-KRT10.gb` en el repositorio.

Para verificar el clon, con F y R basta: cubren las dos uniones, el Kozak, el
inicio del ORF y los dos codones de parada.

## 13. Cómo mandarlo la próxima vez

1. **Gel + Qubit** de todos los minipreps (§11). Descarta los que no se vean.
2. **A260/A230 > 2,0.** Si está bajo, vuelve a pasar por columna: es carryover
   de guanidina o etanol y es lo que mata la reacción.
3. **Eluye en agua o EB**, nunca en TE.
4. **Normaliza** a lo que pida el servicio.
5. **Manda el DNA de 13.3 como control** en la misma placa. Leyó con pico de
   2248: si vuelve a leer y los demás no, es el DNA; si no lee nada, es el
   servicio.
6. **Pide las dos direcciones** con H1seq-F y H1seq-R.

---

# 14. ¿Está mal el plásmido de KRT10?

## 14.1 Lo primero: una lectura sin señal no puede decirlo

Es el punto que conviene fijar antes que nada. **Una reacción sin producto de
extensión no es un veredicto sobre la construcción: es una reacción que no ha
ocurrido.** No dice que el plásmido esté mal, ni que esté bien. No dice nada.

Si el `.ab1` del K10 tiene la misma pinta que los ocho de aquí —traza plana, Q=0,
`NNNNN`— entonces **no hay ninguna evidencia en contra del plásmido**. Lo único
que sabes de él es que la PCR de colonia dio positivo, que es evidencia *a favor*.

## 14.2 Y hay una explicación específica para el de K10

Comprobado sobre la secuencia real de MN502A-1, buscando los sitios de los
cebadores que los servicios ofrecen por defecto:

| Cebador universal | ¿Está en MN502A-1? | ¿Está en pSI-H1? |
|---|---|---|
| **T7** | **NO** | NO |
| **SP6** | **NO** | NO |
| **M13F (−21)** | **NO** | NO |
| **M13R** | **NO** | sí |
| **CMV-F** | **NO** | sí |
| **BGH-R** | **NO** | NO |
| **EF1a-F (el estándar)** | **NO** | NO |
| WPRE-R | sí | sí |
| SV40pA-R | sí | sí |

> ### En MN502A-1 no hay T7, ni SP6, ni M13, ni CMV-F, ni BGH-R.
> Si pediste la secuenciación con un cebador universal —y **CMV-F, T7 y M13F son
> el valor por defecto de casi todos los servicios**— el resultado sería
> exactamente cero señal. No por el plásmido: porque no hay dónde anillar.

Y hay un detalle que lo hace más probable todavía: **el EF1a-F estándar tampoco
está.** Ese cebador apunta al EF1α de longitud completa con su intrón 1, y este
vector lleva **el EF1α corto de 546 pb**. Es el error perfecto: pides «el de
EF1α», el servicio tiene uno en stock, y no aparea.

**Es la primera pregunta que hay que contestar: ¿qué cebador se usó?** Si fue
uno universal, ya está explicado y el plásmido no tiene nada que ver.

## 14.3 El test que responde a tu pregunta sin secuenciar

**Digiere con NotI.** Hay tres dianas (772, 1416, 2813) y una de ellas queda
justo detrás del inserto:

| | Vector vacío | Con KRT10 dentro |
|---|---|---|
| NotI, 3 fragmentos | 3944 · 1397 · **644** | 3944 · **2404** · 1397 |

**La banda de 644 pb se convierte en 2404 pb.** Un solo corte te dice si el
inserto está, y además lo mide. Las tres bandas se separan bien al 0,8 %.

Como confirmación añadida, **BamHI**: en el recombinante correcto la diana se
destruye en la unión 3' (queda `AGATCC`), así que **no debe cortar**. El vector
vacío linealiza.

> Salvedad: esto supone que el cDNA de KRT10 no lleva un `GCGGCCGC` ni un
> `GGATCC` internos. Ya confirmaste que no tiene `ACTAGT` ni `CCATGG`;
> comprueba estos dos de paso en el GenBank.

## 14.4 Entonces, ¿qué creo?

**Que el plásmido está bien, con las reservas de siempre.** Los tres indicios
apuntan en esa dirección:

1. La PCR de colonia dio positivo.
2. No hay ni una sola observación que incrimine al plásmido — sólo ausencia de
   datos.
3. Hay una causa alternativa concreta y comprobable (§14.2) que explica el fallo
   entero sin necesidad de que nada esté mal.

Las dos reservas, por honestidad:

- **Si la PCR de colonia llevaba dos cebadores del inserto**, el positivo no
  vale (§10).
- **Si el `.ab1` del K10 sí tiene señal** y lo que pasa es que la secuencia no
  cuadra, entonces estamos ante otra cosa y hay que mirarla. Dos candidatos:
  un clon mal ensamblado, o la **cola de glicinas de K10** —repetitiva y muy
  GC— haciendo patinar a la polimerasa. Se distinguen fácil: la cola de glicinas
  da una lectura **limpia que se degrada de golpe** al llegar a la repetición,
  no una lectura rara desde el principio.

**Mándame los `.ab1` del K10** y te lo digo en un minuto: distinguir «sin señal»
de «señal con secuencia que no cuadra» es inmediato, y son dos diagnósticos
completamente distintos.

---

# 15. La PCR de colonia era de dos cebadores del inserto

Confirmado. Entonces **ese positivo hay que retirarlo como evidencia**, y en tu
caso concreto el motivo es más fuerte de lo habitual.

## 15.1 Por qué aquí no vale nada

El constructo 1 se montó por **ensamblaje por homología**. Eso significa que en
la mezcla de transformación había, por diseño, **un producto de PCR purificado
del cDNA de KRT10** en cantidad grande. Y ese amplicón:

- lleva el CDS entero, así que **da positivo con dos cebadores del inserto**;
- viaja en la placa, en la punta, en el palillo;
- y encima arrastra trazas de su propio molde, `pCMV6-KRT10`, que también da
  positivo.

> **Una PCR de colonia con dos cebadores del inserto, sobre una placa de
> ensamblaje, da positivo aunque la colonia no tenga el plásmido que buscas.**
> No está midiendo el clon: está midiendo el arrastre.

Esto no dice que tus clones sean malos. Dice que **no están comprobados**. Es
una diferencia importante: no hay evidencia en contra, pero ahora tampoco a
favor.

## 15.2 La PCR que sí lo prueba — y no cuesta nada más

**Los dos cebadores de secuenciación del §12 sirven también de PCR de colonia.**
Uno cae en el EF1α y el otro en el WPRE, o sea **los dos en el vector, flanqueando
el sitio de inserción**:

```
   EF1α ─────[K10seq-F]──────▶ │ inserto │ ◀──────[K10seq-R]───── WPRE
            1275                 1411                1626
```

| Resultado | Producto | Qué es |
|---|---|---|
| **352 pb** | vector vacío o religado | descártalo |
| **~2112 pb** | **KRT10 dentro** | el que buscas |
| sin banda | sin plásmido / colonia mala | repite |

Las dos bandas son **imposibles de confundir** en un gel al 1 %.

Y lo que lo hace a prueba de arrastre: el amplicón de In-Fusion sólo lleva del
vector las posiciones **1396–1411 y 1411–1425**. **Ninguno de los dos cebadores
cae ahí** (están en 1275–1299 y 1602–1626). Así que **ni el producto de PCR
remanente ni `pCMV6-KRT10` pueden dar banda**: les falta el vector a los dos
lados.

Extensión de 2,5 min y anillamiento a 55 °C. Como la banda buena son 2,1 kb,
usa una polimerasa decente, no la de colonia más barata.

> **Dos cebadores, tres trabajos**: cribado por tamaño, lectura de la unión 5' y
> lectura de la unión 3'. No hay que pedir nada más.

## 15.3 Orden de trabajo para el minicírculo de KRT10

1. **PCR de colonia con K10seq-F + K10seq-R** sobre las colonias que guardaste.
   Banda de 2,1 kb → sigue. Banda de 352 pb → tíralo.
2. **NotI** sobre el miniprep de las que pasen: la banda de 644 pb del vacío
   tiene que haberse convertido en **2404 pb** (§14.3).
3. **Gel + Qubit** del miniprep antes de mandar nada (§11).
4. **Secuencia con K10seq-F y K10seq-R**, que cubren las dos uniones, el Kozak,
   el inicio del ORF y los dos codones de parada.

Los pasos 1 y 2 cuestan una tarde y un gel, y te dicen si tienes clon **antes**
de volver a gastar en secuenciación. Dado que el cribado original no era válido,
empezar por ahí no es desconfianza: es que ese dato todavía no existe.

## 15.4 Y lo mismo para sh13 y el scramble

Si el cribado de esos también fue con dos cebadores del inserto, tiene el mismo
problema — agravado porque ahí el «inserto» son 60 pb de oligo hibridado, y los
oligos sobrantes de la ligación dan positivo igual.

Para esos **no se puede hacer PCR de unión** (no cabe un cebador dentro de 60 pb).
El cribado válido es el que ya está en §5.1: **HindIII primero** para descartar
los deletados grandes, y **secuenciación con H1seq-F + H1seq-R** para lo demás.
No hay atajo.
