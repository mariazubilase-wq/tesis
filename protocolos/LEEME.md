# Protocolos

## `Informe_muestras_UCM_ensayo_03-08-2026.docx`

Informe dirigido al grupo de la UCM que envió las muestras (tanda de julio de
2026), detallando cómo se ha tratado cada una en el ensayo del 03/08/2026.

Se construye cruzando dos fuentes:

- las notas de laboratorio propias (`MATERIALES_UCM.docx`), que dan los
  volúmenes pipeteados;
- el correo de la UCM del 13/07/2026 con la corrección del 15/07/2026, que da
  la composición y las concentraciones de cada muestra.

Una tabla por muestra, con el pipeteo, la dosis y la concentración por pocillo
y los tres ratios: **ME:pDNA**, **ME:DOTAP** y **DOTAP:pDNA**. Este último es
la magnitud con la que la UCM caracteriza sus formulaciones. El apartado 8
recoge las desviaciones y las consultas pendientes.

«ME» significa cosas distintas según la muestra: lípido total en la 1,
microemulsión completa en la 2 y liposomas en la 4 y la 5. El documento lo
advierte.

Supuestos que conviene revisar antes de enviarlo:

- **Volumen final del pocillo: 110 µl** (100 µl de medio + 10 µl de complejo)
  en las muestras 1 y 5. De ahí salen las concentraciones en µg/mL.
- **Muestra 4: pDNA a 50 ng/µl** en la resuspensión. Es el valor coherente con
  el ratio 10:1 de la UCM; el de 100 ng/µl daría 5:1.
- **Muestra 2: densidad ≈ 1 g/mL** para calcular el ratio ME:pDNA.

### Qué muestra es cada cosa

| Muestra | Formulación | Uso |
|---|---|---|
| 1 | Microemulsión O/A, DOTAP + DOPE (lípido total 37 mg/mL, DOTAP 3,4 mg/mL) | 12 condiciones |
| 2 | Microemulsión A/O con pDNA encapsulado (10 µg/mL, DOTAP 1 %, ratio fijo 1000:1) | 4 condiciones |
| 3 | Microemulsión A/O sin pDNA | No utilizada |
| 4 | Liposomas liofilizados (10 µg DOTAP por liofilizado) | 1 condición, registro incompleto |
| 5 | Liposomas sin liofilizar (10 mg/mL, DOTAP 1 mg/mL) | 6 condiciones |

> Las muestras 4 y 5 son liposomas, no microemulsiones: las notas internas
> usaban «ME» como abreviatura genérica para todas.

Tres concentraciones deducidas de las notas propias coinciden con las que da
la UCM (37 µg/µl en la muestra 1, 10 µg/µl en la muestra 5, y el DOTAP al 1 %
de la muestra 2 reproduce su ratio 1000:1).

## `genera_informe.js`

Script que genera el `.docx`. Para regenerarlo tras editar el texto:

```bash
cd protocolos
npm install docx      # solo la primera vez
node genera_informe.js
```
