# Protocolos

## `Tratamiento_muestras_UCM.docx`

Desarrollo del apartado de tratamiento del informe enviado a la UCM el
06/08/2026, para las muestras de la tanda de julio de 2026.

Se construye cruzando tres fuentes:

| Fuente | Qué aporta |
|---|---|
| `PRIMERA_PRUEBA_MICROSCOPÍA...pdf` (informe del 06/08) | Condiciones reales del ensayo y resultados. **Fuente principal** |
| Correo UCM 13/07 + corrección 15/07 | Composición y concentraciones de cada muestra |
| `MATERIALES_UCM.docx` (notas del 03/08) | Volúmenes pipeteados |

Una tabla por muestra, con el pipeteo, la dosis y la concentración por pocillo
y los ratios **ME:pDNA** y **DOTAP:pDNA**. El ME:DOTAP no va en tabla porque es
constante dentro de cada muestra.

Escrito en primera persona y sin formato de plantilla, para que case con el
informe del 06/08, que es lo que la UCM ya ha leído de esta misma autora.

«ME» significa cosas distintas según la muestra: lípido total en la 1,
microemulsión completa en la 2 y liposomas en la 4 y la 5.

### Base de los cálculos

- **Volumen final del pocillo: 100 µl** (el complejo son 10 µl, el 10 %).
- pDNA nominal (0,3 / 0,6 µg, etc.), como en el informe ya enviado. Los
  volúmenes pipeteados dan valores hasta un 2 % distintos.
- Muestra 2: densidad ≈ 1 g/mL para el ratio ME:pDNA.

### La contradicción de la muestra 4

El correo del 13/07 dice que cada liofilizado contiene **10 µg de DOTAP** y
también que lo enviado equivale a **10 µg de liposomas**. Es imposible: con
liposomas a 10 mg/mL y DOTAP a 1 mg/mL, el DOTAP es el 10 % de los liposomas,
así que 10 µg de liposomas llevarían 1 µg de DOTAP.

Lo resuelve el informe del 06/08: *«habíais liofilizado 10 µl de estos
liposomas»*. 10 µl son 100 µg de liposomas y 10 µg de DOTAP, que es la cifra
buena. En el correo pone µg donde debía poner µl.

Es la única contradicción aritmética del correo. El 4 % de DOTAP de las
muestras 2 y 3 ya lo corrigieron ellas el 15/07, y el 1 % sí cuadra con el
ratio 1000:1 que declaran.

### Discrepancias entre las notas del 03/08 y el informe del 06/08

Se ha seguido el informe, que es lo que la UCM ya tiene, salvo en la muestra 4,
donde María confirmó después lo que hizo realmente: resuspendió en **20 µl** y
tomó **2 µl** por pocillo, en triplicado. Como 2/20 es la misma fracción que
1/10, la dosis por pocillo no cambia respecto a lo que decía el informe; lo que
estaba mal descrito era el método.

| | Notas 03/08 | Informe 06/08 |
|---|---|---|
| Balanceo | 15 min | **20 min** |
| Réplicas | «para 4 réplicas» | **triplicado** |
| Muestra 2 | 4 condiciones | **2** (el vial traía 100 µl, no 1 mL) |
| Muestra 4 | — | 10 µl de resuspensión, 1 µg de pDNA |

## `genera_informe.js`

Script que genera el `.docx`. Para regenerarlo tras editar el texto:

```bash
cd protocolos
npm install docx      # solo la primera vez
node genera_informe.js
```
