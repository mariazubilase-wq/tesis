# Lista de cebadores

Todos verificados sobre los mapas reales (`MN502A-1`, 5985 pb · `MNSI500A-1`,
6877 pb). **Únicos en su plásmido**, sin homopolímeros ≥5. Tm por vecino más
próximo (SantaLucia 1998) en condiciones de PCR: 50 mM K⁺, 2 mM Mg²⁺, 0,8 mM
dNTP, 0,25 µM de cebador.

**Pedir todos desalados, escala 25 nmol, resuspender a 100 µM en TE.**
Hoja de pedido lista: `pedido_oligos_minicirculos.docx` (nomenclatura `MN_`,
la misma de tus pedidos anteriores).

| En este documento | En la hoja de pedido |
|---|---|
| K10seq-F / K10seq-R | `MN_K10seq_F` / `MN_K10seq_R` |
| H1seq-F / H1seq-R | `MN_H1seq_F` / `MN_H1seq_R` |
| H1col-F / H1col-R | `MN_H1col_F` / `MN_H1col_R` |
| sh13-F | `MN_sh13_F` |

### Los que ya tenías, comprobados

| Nombre | nt | Tm | Dónde cae |
|---|---|---|---|
| `MN_EF1a_F` | 23 | 57,6 °C | **MN502A-1 pos 1256** — lee desde 133 nt antes del inserto. **Sirve** para la unión 5' de KRT10 |
| `MN_H1_F` | 25 | 58,7 °C | pSI-H1 pos 2838 — lee desde 67 nt antes del BamHI. Sirve, pero con poca carrerilla ante la horquilla |
| `MN_vc_R` | 16 | 51,1 °C | MN502A-1 pos 835, reverso — lee **hacia atrás**, hacia attB. No toca el inserto |

`MN_EF1a_F` hace el mismo trabajo que `MN_K10seq_F` para secuenciar. Pide
`MN_K10seq_F` igualmente porque es el que **casa en Tm con `MN_K10seq_R`** para
la PCR de colonia (ΔTm 2 °C frente a 9 °C).

---

## Los que ya tienes

| Nombre | Para qué |
|---|---|
| `ClonK10MC_F` / `ClonK10MC_R` | **Clonaje** de KRT10 en MN502A-1 por ensamblaje por homología. Ya usados |
| `sh13_TOP` / `sh13_BOT` | **El propio inserto** de sh13: se hibridan y se ligan entre BamHI y EcoRI. No son cebadores |

---

## Para el minicírculo de KRT10 (pMC.EF1α · MN502A-1)

| Nombre | Secuencia 5'→3' | nt | Tm | GC | Pos. |
|---|---|---|---|---|---|
| **K10seq-F** | `TCAGCCGGCTCTCCACGCTTTGCCT` | 25 | 68,5 °C | 64 % | 1275–1299 |
| **K10seq-R** | `TGCCTGACAACGGGCCACAACTCCT` | 25 | 66,5 °C | 60 % | 1602–1626 |

**Dos cebadores, tres trabajos.** Los dos caen en el vector (EF1α y WPRE),
flanqueando el sitio de inserción:

1. **PCR de colonia por tamaño** — anillamiento 62 °C, extensión 2,5 min:

   | Banda | Qué es |
   |---|---|
   | **352 pb** | vector vacío o religado |
   | **~2112 pb** | **KRT10 dentro** ← el bueno |

   A prueba de arrastre: el amplicón de In-Fusion sólo lleva del vector las
   posiciones 1396–1425, y ninguno de los dos cebadores cae ahí. **Ni el
   producto de PCR remanente ni `pCMV6-KRT10` pueden dar banda.**

2. **K10seq-F secuencia la unión 5'** — empieza a leer 112 nt antes: cubre la
   unión, el Kozak y el inicio del ORF.
3. **K10seq-R secuencia la unión 3'** — empieza a leer 191 nt después: cubre los
   dos codones de parada y la unión.

> Las dos lecturas **no cubren el CDS entero**: queda un hueco de ~260 nt en
> medio. Hace falta un cebador interno, pendiente de `secuencias/pCMV6-KRT10.gb`.

---

## Para pSI-H1 (MNSI500A-1) — sh13 y scramble

### Cebadores del vector

| Nombre | Secuencia 5'→3' | nt | Tm | GC | Pos. |
|---|---|---|---|---|---|
| **H1col-F** | `AGGGGAGTGGCGCCCTGCAAT` | 21 | 65,5 °C | 67 % | 2817–2837 |
| **H1col-R** | `TTAGCCAGAGAGCTCCCAGGCTCAGA` | 26 | 64,3 °C | 58 % | 2991–3016 |
| **H1seq-F** | `TGCGCCCTGGCAGGAAGATGGCTGT` | 25 | 68,6 °C | 64 % | 2785–2809 |
| **H1seq-R** | `AGTCACACAACAGACGGGCACACACT` | 26 | 64,5 °C | 54 % | 3070–3095 |

### Cebadores específicos de cada horquilla

| Nombre | Secuencia 5'→3' | nt | Tm | GC |
|---|---|---|---|---|
| **sh13-F** | `CTTGGATCCAATGACTGCCTGGCTTCCTTT` | 30 | 64,4 °C | 50 % |
| **shSC-F** | *pendiente — ver §«La regla»* | | | |

### Qué hace cada combinación

| Pareja | Anillam. | Resultado |
|---|---|---|
| **H1col-F + H1col-R** | 60 °C | **200 pb** sin inserto · **256 pb** una horquilla · **312 pb** dos en tándem |
| **sh13-F + H1seq-R** | 62 °C | **226 pb sólo si está sh13**. Con el scramble, nada |
| **shSC-F + H1seq-R** | — | lo mismo para el scramble |
| **H1seq-F + H1seq-R** | — | **secuenciación** en las dos direcciones (120 nt antes / 127 nt después) |

---

## La regla para hacer el del scramble (y el de cualquier horquilla futura)

```
   shXX-F  =  5'- CTTGGATCC + [los 21 nt del brazo SENTIDO de esa horquilla] -3'
                  └── fijo ──┘  └────────── lo que cambia ──────────┘
```

Los 9 nt fijos son vector (`…CTT` + la diana BamHI `GGATCC`, que se regenera al
ligar). Los 21 siguientes son el brazo sentido, o sea **los nucleótidos 6 a 26
del oligo TOP**, justo detrás del `GATCC`.

Para sh13 eso da `CTTGGATCC` + `AATGACTGCCTGGCTTCCTTT`. **Mándame el
`shSC_TOP` y lo compruebo** (Tm, unicidad y tamaño exacto), pero la regla la
puedes aplicar tú ahora mismo.

---

## Por qué el extremo 3' va en el brazo y no en el bucle

**Corrige un diseño anterior mío que estaba mal.** El primer `sh13-R` que
propuse anclaba su extremo 3' en el bucle (`CTTCCTGTCAGA`):

> ❌ **El bucle es casi con seguridad el mismo en sh13 y en el scramble.** Y como
> la especificidad de cebado la manda el extremo 3', ese cebador tenía 12 nt de
> apareamiento 3' perfecto con el scramble → **falso positivo**. Inútil justo
> para lo que se pedía.

El brazo es lo único que cambia entre las dos horquillas, así que ahí tiene que
ir el 3'. De paso el cebador queda **a prueba de arrastre**: el otro cebador de
la pareja está en el vector, así que **los oligos sobrantes de la ligación no
pueden dar banda** por mucho que queden en la placa.

> ⚠️ **Artefacto esperado, no te asustes:** como los dos brazos de la horquilla
> son complementarios, `sh13-F` aparea también en el brazo antisentido y se ceba
> contra sí mismo, dando una banda de **~63 pb**. Es inevitable en cualquier
> cebador de horquilla. Queda lejos de los 226 pb y no estorba. Anillar a 62 °C
> la reduce.

---

## Cómo encajan los dos ensayos

No son alternativos, se complementan:

| | ¿Hay inserto? | ¿Cuál es? | ¿Hay concatémeros? |
|---|---|---|---|
| **H1col-F + H1col-R** | sí | no | **sí** |
| **shXX-F + H1seq-R** | sí | **sí** | no |

El específico da un sí/no limpio y te dice **cuál** de las dos horquillas es
—que es lo que importa si procesas sh13 y el scramble en paralelo—, pero si
entraran dos copias en tándem el cebador aparea en la primera y da banda igual.

El de tamaño es el que **caza los concatémeros**, que es un modo de fallo real
(oligos fosforilados, exceso de dúplex en la ligación) y hasta ahora no lo
estabas cribando con nada.

**Lo práctico:** criba con el específico, y pasa los positivos por el de tamaño
antes de secuenciar. O haz los dos a la vez, que son dos tubos.

---

## Limitación anotada

`H1col-R` y `H1seq-R` están en 2991 y 3070, o sea **fuera del fragmento BglII
(2639–2988)** que se mueve al constructo combinado. Estas parejas sirven para
cribar clones en pSI-H1, **no** para cribar el combinado. Para eso, los
diagnósticos del §4 de `diseno_combinado_MN100A1.md`.
