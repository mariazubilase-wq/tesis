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
