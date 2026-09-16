# Protocolos

## `Tratamiento_muestras_ME-DNA_03-08-2026.docx`

Versión desarrollada y explicada de las notas de laboratorio del 03/08/2026
(`MATERIALES_UCM.docx`), pensada para enviar a una persona ajena al ensayo.

Contiene, para cada muestra (1, 2, 4 y 5) y para el control positivo:

- el procedimiento escrito paso a paso,
- la tabla de pipeteo **reproducida literalmente** de las notas,
- una tabla adicional con la dosis que recibe **cada pocillo**, calculada
  dividiendo entre las 4 réplicas,
- las abreviaturas y la nomenclatura de las condiciones.

El apartado 10 recoge lo que las notas no especifican y conviene completar
antes de enviarlo (significado de «ME», línea celular, formato de placa,
lectura del experimento, ausencia de la muestra 3, etc.).

> Los valores marcados como «calculado» son derivaciones aritméticas de las
> notas, no medidas independientes.

## `genera_documento.js`

Script que genera el `.docx` anterior. Para regenerarlo tras editar el texto:

```bash
cd protocolos
npm install docx      # solo la primera vez
node genera_documento.js
```
