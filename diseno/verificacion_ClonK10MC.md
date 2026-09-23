# Verificación de la pareja `ClonK10MC_F` / `ClonK10MC_R`

Cebadores para amplificar la ORF de KRT10 desde `pCMV6-KRT10` y clonarla por
In-Fusion en `pMC.EF1α-MCS-SV40polyA` abierto con **BamHI**.

```
ClonK10MC_F  5'-TTCGAATTTAAATCG GCC ATGTCTGTTCGATACAGCTCAAGC-3'        (42 nt)
             └─ brazo vector ─┘ └K┘ └──── apareo con la ORF ────┘

ClonK10MC_R  5'-ACGCGGCCGCGGATC TTATCA GTATCTTGGTCCCTTAGATGAAGACTCGCC-3'  (51 nt)
             └─ brazo vector ─┘ └stops┘ └────── apareo con la ORF ──────┘
```

**Veredicto: correctos.** 0 fallos, 3 avisos. Reproducible con:

```bash
python3 herramientas/verifica_oligos.py \
    --donante secuencias/pCMV6-KRT10.dna \
    --mcs tctagagctagcgaattcgaatttaaatcggatccgcggccgcgtcga \
    --enzima BamHI-HF \
    --f TTCGAATTTAAATCGGCCATGTCTGTTCGATACAGCTCAAGC \
    --r ACGCGGCCGCGGATCTTATCAGTATCTTGGTCCCTTAGATGAAGACTCGCC
```

## Lo comprobado sobre el fichero real

| Comprobación | Resultado |
|---|---|
| BamHI corta una sola vez **en el MCS** | sí, `GGATCC` en 30..35, corte `G^GATCC` |
| Brazo 5' de F = 15 nt a la izquierda del corte | `TTCGAATTTAAATCG` — exacto |
| Brazo 3' de R = rc de los 15 nt a la derecha | `ACGCGGCCGCGGATC` — exacto |
| Zona de apareo de F | 1026..1052, **única**, Tm 62,5 °C |
| Zona de apareo de R | 2751..2780, **única**, Tm 62,2 °C |
| Diferencia de Tm entre las dos | **0,4 °C** |
| Amplicón | 1791 pb, GC 55,3 % |
| Inserto neto en el minicírculo | 1761 pb = GCC + 1752 (ORF) + TGATAA |
| Pauta de lectura | 584 aa, sin stops internos, termina en `…SSSKGPRY` |
| Proteína frente al donante | **idéntica** |
| Myc-DDK | **excluido** (R para en el último codón `TAC`, antes de MluI) |
| Doble stop `TGATAA` | presente y en pauta |
| ATG aguas arriba dentro del MCS | ninguno |
| Kozak resultante | `TCGGCC|ATGT` → **−3 = G, purina** |
| Diana BamHI tras la ligación | **destruida** (`…TGATAA|GATCC…`, no reconstituye `GGATCC`) |

### Dos detalles que no son obvios

**1. El `GCC` no es un Kozak inventado: es el nativo.** El pCMV6 lleva
`…GCGATCGCC|ATG`. Al poner `GCC` delante del ATG se reconstruye el mismo
contexto −1/−2/−3 que tiene el gen en su plásmido de origen (−3 = G). No hace
falta `GCCACC`: `GCCACC` daría −3 = A, igual de purina. Sin ninguno de los dos
el minicírculo quedaría `…AAATCG|ATG` con −3 = T, que sí es débil.

Efecto secundario bueno: como ese `GCC` **también existe en el molde**, F no
aparea 24 nt sino **27**, y la Tm sube.

**2. La unión 3' no reconstituye BamHI.** `…TACTGATAA` + `GATCCGCGGCCGCGTCGA`
deja `TAAGATCC`, no `GGATCC`. El clon correcto no corta con BamHI y el vector
religado sí: digestión diagnóstica gratis.

## Los tres avisos

1. **`+4 = T`.** Inevitable: es la primera base del segundo codón (`TCT`, Ser2).
   Cambiarla alteraría la proteína. El pCMV6 tiene la misma T y expresa bien.
2. **Tramo al 76 % de GC** (posiciones 1351..1650 del amplicón, la cola rica en
   glicina). 40 ventanas de 20 nt repetidas en el amplicón. Es el riesgo real de
   esta PCR: patinazo de la polimerasa y deleciones internas.
3. **Falta el GenBank del parental.** El MCS de 48 nt es un dato aportado a mano
   (§0.B del diseño de los tres constructos). Los brazos son correctos *para ese
   MCS*; que BamHI corte **una sola vez en todo el vector** no se puede
   comprobar sin el mapa. Con él:
   `--aceptor secuencias/pMC.EF1a-MCS-SV40polyA.gb`.

## Antes de encargar / antes de montar

- **Cotejar el MCS contra el GenBank del parental.** Es lo único que puede
  invalidar los brazos.
- **Comprobar que BamHI es único en el vector entero**, no sólo en el MCS.
- **Purificar en gel el vector linealizado** y llevar un control sin inserto:
  corte único ⇒ recirculariza.
- **DpnI + purificación en gel del producto de PCR.** El molde `pCMV6-Entry` es
  **Kan/Neo** (rasgo 4874..5668 del propio fichero) y el parental de SBI también
  se selecciona con kanamicina: el molde que sobreviva da colonias que parecen
  clones.
- **Polimerasa para molde difícil** (PrimeSTAR GXL, o Q5 con GC enhancer) por el
  tramo al 76 % de GC.
- **Secuenciación de plásmido completo** de 2–3 candidatos, no sólo Sanger de
  las uniones: lo que falla en esta cola son deleciones internas.

## Lo que esta pareja **no** hace

Amplifica la secuencia **nativa**: no lleva las 5 mutaciones silenciosas del
blindaje (§2 del diseño). Es una decisión legítima —con la especificidad de
alelo verificada el shRNA respeta la copia silvestre— pero implica que el
transgén y el endógeno son indistinguibles por qPCR. Si se quiere esa medida,
hay que endurecer antes (paso B.1) o encargar el fragmento sintético.
