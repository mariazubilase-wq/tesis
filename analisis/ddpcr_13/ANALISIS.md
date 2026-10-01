# Análisis ddPCR #13 (WT2 / MUT1 · #13 1NM y 0,5NM)

Archivo de origen: `datos/086e01d8-2026-10-01_dpcr_13_1y05nm_20261001_100050_208.xlsx`
(One-Step RT-ddPCR Advanced Kit for Probes, 2 targets por pocillo: Target 1 = FAM, Target 2 = VIC).
Todo se reproduce con `python3 analiza_ddpcr.py` (genera `resultados/` y `figuras/`).

## Qué se hizo, paso a paso

1. **Lectura.** 13 pocillos × 2 targets = 26 filas. El pocillo **B01** no tiene nombre de muestra
   (4 copias/µL, 6107 gotas): se excluye por ser probablemente un NTC/vacío no etiquetado.
2. **Target dominante por pocillo.** En cada pocillo se conserva solo el target con más copias/µL.
   Resultado coherente en los 12 pocillos: **WT2 → Target 2 (VIC)**, **MUT1 → Target 1 (FAM)**.
   El otro target (señal cruzada) es 0,15–2,8 % del dominante
   (`resultados/1_target_dominante_por_pocillo.csv`; Fig. 1 y 2).
3. **Media de réplicas biológicas.** Cada condición tiene 2 pocillos (n = 2); se calcula media, SD
   muestral (ddof = 1), mínimo y máximo (`2_medias_replicas.csv`; Fig. 3).
4. **Normalización.** Cada condición se divide por la media de su control negativo del mismo genotipo:
   WT2 #13 (1 y 0,5NM) ÷ media de `wt2 c-`; MUT1 #13 (1 y 0,5NM) ÷ media de `mut1 c-`.
   Se da el cociente («veces vs c-», c- = 1), con SD propagada
   (`fold·√[(SD_m/m)² + (SD_c/c)²]`) y los cocientes de cada réplica individual (puntos en la Fig. 4).
   (`3_normalizado_vs_control.csv`).
5. **Análisis de sensibilidad sin A06** (ver avisos): ficheros y figuras con sufijo `b` / `_sin_A06`.

## Resultados (copias/µL del target dominante)

| Genotipo | Condición | Pocillos | Media | SD |
|---|---|---|---:|---:|
| WT2 | c- | A09, A10 | 1538,1 | 411,0 |
| WT2 | #13 0,5NM | A03, A04 | 1759,7 | 22,0 |
| WT2 | #13 1NM | A01, A02 | 1341,1 | 268,7 |
| MUT1 | c- | A11, A12 | 3180,3 | 1140,8 |
| MUT1 | #13 0,5NM | A07, A08 | 2004,1 | 663,7 |
| MUT1 | #13 1NM | A05, A06 | 761,9 | 1040,0 |

**Normalizado vs c- (veces):**

| Genotipo | Condición | Todos los datos | Sin A06 |
|---|---|---:|---:|
| WT2 | #13 0,5NM | 1,14 ± 0,31 | 1,14 ± 0,31 |
| WT2 | #13 1NM | 0,87 ± 0,29 | 0,87 ± 0,29 |
| MUT1 | #13 0,5NM | 0,63 ± 0,31 | 0,63 ± 0,31 |
| MUT1 | #13 1NM | **0,24 ± 0,34** | **0,47** (n = 1, sin SD) |

Lectura: en WT2 no hay cambio claro respecto al control (≈ 0,9–1,1). En MUT1 hay descenso en las
dos dosis (0,63 y 0,24–0,47), pero **con n = 2 y esta dispersión no es concluyente**.

## Avisos / limitaciones

- **A06 (MUT1 #13 1NM) es un valor atípico:** 26,5 copias/µL con 394 positivos de 17 658 gotas,
  frente a 1497 en su réplica A05 (≈ 56× menos). Puede ser fallo técnico (pipeteo/RT) o efecto real
  extremo; no lo he excluido de la tabla principal, pero doy el análisis con y sin él.
  Es lo que hace que la SD de ese grupo (1040) supere a la media.
- **Controles muy variables:** `mut1 c-` (3987 vs 2374) y `wt2 c-` (1247 vs 1829) difieren mucho entre
  réplicas, y eso se traslada a todos los cocientes. A09 tiene además pocas gotas (9052, < 10 000).
- **n = 2 por grupo:** las SD son poco fiables y no se hizo ningún test estadístico.
- La señal cruzada de A08 (43 copias/µL, 2,8 %) y A06 es algo mayor que en el resto; no afecta a la conclusión.
- No se aplicó corrección por gotas ni por ARN de entrada; se usan las copias/µL que da QuantaSoft.
- Las medias son aritméticas de copias/µL; la normalización es cociente de medias (no media de cocientes).

## Figuras (`figuras/`)

| Fichero | Contenido |
|---|---|
| `fig1_targets_por_pocillo.png` | Los dos targets en cada pocillo (escala log) |
| `fig2_target_dominante.png` | Target conservado por pocillo |
| `fig3_medias_replicas.png` / `fig3b_…_sin_A06.png` | Media ± SD con réplicas |
| `fig4_normalizado.png` / `fig4b_…_sin_A06.png` | Veces vs control negativo |
| `fig5_gotas.png` | Control de calidad: gotas aceptadas por pocillo |
