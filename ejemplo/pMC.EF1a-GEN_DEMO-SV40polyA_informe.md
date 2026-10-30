# Clonaje in silico — pMC.EF1a-GEN_DEMO-SV40polyA

Generado por `herramientas/simula_clonaje.py`. **No sustituye a la secuenciación del clon**: lo que predice es lo que *debería* salir.

## 1. Piezas

| Pieza | Tamaño | Procedencia |
|---|---:|---|
| Molde de la PCR | 336 pb (amplicón) | PCR sobre donante sintético de demostración |
| Vector aceptor | 1916 pb | vector sintético de demostración (NO es el vector real) |
| Inserto digerido | 318 pb | amplicón cortado |
| **Producto** | **2211 pb** | circular |

## 2. PCR

| | Directo | Reverso |
|---|---|---|
| Secuencia 5'→3' | `CACCACGCTAGCGCCACCATGTTTCCTCATGCAATTCAAAACCATGTCCG` | `CACCACGGATCCTCATTAATGAGCCGGTATGCAGGTGTATTGG` |
| Longitud | 50 nt | 43 nt |
| Cola 5' (no aparea) | 18 nt | 15 nt |
| Apareamiento | 32 nt | 28 nt |
| Tm apareamiento | 62.7 °C | 61.4 °C |
| Tm cebador completo | 73.3 °C | 69.6 °C |
| GC | 52 % | 51 % |

Amplicón: **336 pb**, GC 48 %. Tras digerir: **318 pb**.

## 3. Uniones del clon final

Esto es lo que tiene que aparecer al secuenciar (24 nt a cada lado):

```
unión 5'  …AAGGCTGCAACTCATCGATCTAGAGCTAGCGCCACCATGTTTCCTCAT…
                                   ^ aquí empieza la diana de NheI-HF (GCTAGC)
unión 3'  …ACCTGCATACCGGCTCATTAATGAGGATCCGCGGCCGCGTCGAAACTT…
                                   ^ aquí empieza la diana de BamHI-HF (GGATCC)
```

## 4. El ORF que queda clonado

- Posición en el plásmido: 313–615
- Longitud: 303 pb = 100 aminoácidos + stop
- Primeros 12 aa: `MFPHAIQNHVRN`
- Últimos 12 aa: `RDFSQYTCIPAH`

**Míralos.** Es la comprobación de 10 segundos que evita clonar algo que no es lo que crees.

## 5. Digestiones diagnósticas del producto

| Enzima | Cortes | Fragmentos (pb) |
|---|---:|---|
| NheI-HF | 1 | 2211 |
| BamHI-HF | 1 | 2211 |
| XbaI | 1 | 2211 |
| **NheI-HF + BamHI-HF** | 2 | 1893, 318 |

La doble digestión libera el inserto (318 pb) del esqueleto: es el cribado más directo, y en el vector vacío da una sola banda del tamaño del plásmido (1916 pb).

## 6. Rasgos del producto

| Inicio | Fin | Hebra | Tipo | Etiqueta |
|---:|---:|:---:|---|---|
| 1 | 34 | + | misc_recomb | attB |
| 75 | 294 | + | promoter | promoter_EF1a |
| 301 | 306 | + | misc_feature | unión 5' (NheI-HF) |
| 302 | 619 | + | misc_feature | inserto |
| 302 | 344 | + | primer_bind | cebador directo |
| 307 | 312 | + | regulatory | Kozak |
| 313 | 615 | + | CDS | GEN_DEMO |
| 313 | 615 | + | CDS | ORF del inserto |
| 588 | 619 | − | primer_bind | cebador reverso |
| 619 | 624 | + | misc_feature | unión 3' (BamHI-HF) |
| 638 | 706 | + | polyA_signal | polyA_SV40 |
| 767 | 811 | + | misc_recomb | attP |
| 812 | 1411 | + | rep_origin | rep_origin |
| 1412 | 2211 | + | CDS | KanR |

## 7. Avisos

- rasgo «MCS» del vector descartado: cae en el fragmento que se sustituye
