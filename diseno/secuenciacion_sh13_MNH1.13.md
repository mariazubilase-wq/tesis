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
