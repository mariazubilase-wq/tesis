# Protocolos

## `Informe_muestras_UCM_ensayo_03-08-2026.docx`

Desarrollo del apartado de tratamiento del informe enviado a la UCM el
06/08/2026, para las muestras de la tanda de julio de 2026.

Se construye cruzando tres fuentes:

| Fuente | Qué aporta |
|---|---|
| `PRIMERA_PRUEBA_MICROSCOPÍA...pdf` (informe del 06/08) | Condiciones reales del ensayo y resultados. **Fuente principal** |
| Correo UCM 13/07 + corrección 15/07 | Composición y concentraciones de cada muestra |
| `MATERIALES_UCM.docx` (notas del 03/08) | Volúmenes pipeteados |

Una tabla por muestra, con el pipeteo, la dosis y la concentración por pocillo
y los tres ratios: **ME:pDNA**, **ME:DOTAP** y **DOTAP:pDNA**.

«ME» significa cosas distintas según la muestra: lípido total en la 1,
microemulsión completa en la 2 y liposomas en la 4 y la 5.

### Base de los cálculos

- **Volumen final del pocillo: 100 µl** (el complejo son 10 µl, el 10 %).
- pDNA nominal (0,3 / 0,6 µg, etc.), como en el informe ya enviado. Los
  volúmenes pipeteados dan valores hasta un 2 % distintos.
- Muestra 2: densidad ≈ 1 g/mL para el ratio ME:pDNA.

### Discrepancias entre las notas del 03/08 y el informe del 06/08

Se ha seguido el informe, que es lo que la UCM ya tiene:

| | Notas 03/08 | Informe 06/08 |
|---|---|---|
| Balanceo | 15 min | **20 min** |
| Réplicas | «para 4 réplicas» | **triplicado** |
| Muestra 2 | 4 condiciones | **2** (el vial traía 100 µl, no 1 mL) |
| Muestra 4 | — | **10 µl de resuspensión, 1 µg de pDNA** |

## `genera_informe.js`

Script que genera el `.docx`. Para regenerarlo tras editar el texto:

```bash
cd protocolos
npm install docx      # solo la primera vez
node genera_informe.js
```
