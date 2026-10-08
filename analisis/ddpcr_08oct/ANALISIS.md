# Análisis ddPCR 08-oct (MUT1 · c-, #13 0,5NM y #13 1NM)

Origen: `datos/3f0c5c05-2026-10-08_20261008_090822_665.xlsx` (2 targets por pocillo, Target 1 = FAM, Target 2 = VIC)
y la libreta del RNA (`datos/libreta_RNA_ngul.jpg`). Todo se reproduce con `python3 analiza_ddpcr_08oct.py`;
el Excel conjunto (E1 + E2) se genera con `../genera_excel.py`.

## Diseño
- Todas las muestras son **MUT1**. El número al final del nombre (`mut1 c- 1`, `#13 1 2`, `#13 0,5 1`…) es la **réplica
  biológica** (1 o 2); los pocillos con el mismo nombre son **réplicas técnicas** (2 por biológica).
- Pocillos: A01–A04 c-, A05–A08 #13 1NM, A09–A12 #13 0,5NM.

## Método
1. **Target dominante por pocillo**: se conserva el de más copias/µL. En los 12 pocillos es el Target 1 (FAM);
   el otro es 0,2–3,0 % (`1_target_dominante_por_pocillo.csv`; Fig. 1 y 2).
2. **Pocillos excluidos** (`0_pocillos_excluidos.csv`): B01 y B02 (sin nombre, 0 copias T1 y <1 copia T2: vacíos/NTC) y
   B03 «wt3» (Target 2 saturado: 9323 de 9323 gotas positivas = 10⁶ copias/µL; no es MUT1).
3. **Técnicas → biológicas**: media de los 2 pocillos de cada réplica biológica (`2a_replicas_biologicas*.csv`, con la SD técnica; Fig. 3).
4. **Biológicas → condición**: media ± SD de las 2 réplicas biológicas (n = 2) (`2b_medias_condicion*.csv`; Fig. 4).
5. **Corrección por RNA**: libreta en ng/µL por réplica biológica (c- 0,70 / 0,62 · #13 1NM 0,52 / 0,80 · #13 0,5NM 0,52 / 0,79).
   Se interpreta que el «×2» anotado ya está aplicado en esos valores; al ser un factor común, **no cambia los cocientes vs c-**,
   solo la escala absoluta. Magnitud: copias/µL ÷ ng/µL de RNA (Fig. 6). Se da sin corregir y corregido.
6. **Normalización** contra la media del c- (de sus 2 biológicas) (`3_normalizado_vs_control*.csv`), con las dos barras de error:
   `SD_propagada` (incluye la incertidumbre del c-) y `SD_propia` (SD de las réplicas de cada grupo ÷ media del c-; el c- también
   lleva su SD) (Fig. 7).

## Resultados
| Condición | Media (copias/µL) | SD | Veces vs c- | SD propia | SD propagada |
|---|---:|---:|---:|---:|---:|
| c- | 2214 | 417 | 1 | 0,19 | – |
| #13 0,5NM | 1552 | 262 | 0,70 | 0,12 | 0,18 |
| #13 1NM | 1268 | 793 | 0,57 | 0,36 | 0,37 |

**Corregido por RNA** (copias/µL ÷ ng/µL):

| Condición | Media | SD | Veces vs c- | SD propia | SD propagada |
|---|---:|---:|---:|---:|---:|
| c- | 3340 | 346 | 1 | 0,10 | – |
| #13 0,5NM | 2413 | 304 | 0,72 | 0,09 | 0,12 |
| #13 1NM | 1823 | 655 | 0,55 | 0,20 | 0,20 |

Lectura: #13 reduce la señal de MUT1 respecto al c- a ~0,7 (0,5NM) y ~0,55 (1NM), con dosis-respuesta en el mismo sentido. Con n = 2 biológicas
y esta dispersión no es concluyente; no se hizo test estadístico.

## Avisos
- **Mucha variación entre biológicas en #13 1NM**: bio1 = 707 y bio2 = 1829 copias/µL (la técnica dentro de cada una es estrecha, SD 60–100).
  Es lo que da la SD de 793; la variación está entre biológicas, no en la técnica.
- **Pocas gotas** en A09–A12 (#13 0,5NM): 7 600–8 500 (< 10 000). El c- también tiene variación entre biológicas (2509 vs 1919).
- El cruce de señal (Target 2) sube a ~3 % en A11–A12; no afecta a la conclusión.
- La foto de la libreta estaba girada 90°; los valores se leyeron tal cual (ver `datos/libreta_RNA_ngul.jpg`).
