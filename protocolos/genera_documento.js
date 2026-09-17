const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  LevelFormat, convertInchesToTwip, Header, Footer, PageNumber
} = require('docx');
const fs = require('fs');

const ACCENT = "1F4E79";
const LIGHT  = "DCE6F1";
const SOFT   = "F2F2F2";
const W = 9020;

// ---------- helpers ----------
const P = (text, o = {}) => new Paragraph({
  spacing: { before: o.before ?? 0, after: o.after ?? 120, line: 276 },
  alignment: o.align,
  indent: o.indent,
  border: o.border,
  shading: o.shading,
  children: [new TextRun({ text, bold: o.bold, italics: o.italics, size: o.size ?? 21, color: o.color, font: "Calibri" })],
});

const RICH = (runs, o = {}) => new Paragraph({
  spacing: { before: o.before ?? 0, after: o.after ?? 120, line: 276 },
  alignment: o.align,
  indent: o.indent,
  shading: o.shading,
  border: o.border,
  children: runs.map(r => typeof r === 'string'
    ? new TextRun({ text: r, size: 21, font: "Calibri" })
    : new TextRun({ text: r.t, bold: r.b, italics: r.i, size: r.size ?? 21, color: r.c, font: "Calibri" })),
});

const H1 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 360, after: 160 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: ACCENT, space: 4 } },
  children: [new TextRun({ text, bold: true, size: 28, color: ACCENT, font: "Calibri" })],
});

const H2 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_2,
  spacing: { before: 240, after: 100 },
  children: [new TextRun({ text, bold: true, size: 23, color: "2E74B5", font: "Calibri" })],
});

const BUL = (text, o = {}) => new Paragraph({
  numbering: { reference: "vinetas", level: o.level ?? 0 },
  spacing: { after: 70, line: 276 },
  children: [new TextRun({ text, size: 21, font: "Calibri", bold: o.bold })],
});

const BULRICH = (runs, o = {}) => new Paragraph({
  numbering: { reference: "vinetas", level: o.level ?? 0 },
  spacing: { after: 70, line: 276 },
  children: runs.map(r => typeof r === 'string'
    ? new TextRun({ text: r, size: 21, font: "Calibri" })
    : new TextRun({ text: r.t, bold: r.b, italics: r.i, size: 21, font: "Calibri" })),
});

const NUM = (text) => new Paragraph({
  numbering: { reference: "pasos", level: 0 },
  spacing: { after: 90, line: 276 },
  children: [new TextRun({ text, size: 21, font: "Calibri" })],
});

function cell(text, { widths, i, bold, fill, align, italics, size } = {}) {
  return new TableCell({
    width: { size: widths[i], type: WidthType.DXA },
    shading: fill ? { type: ShadingType.CLEAR, fill, color: "auto" } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: [new Paragraph({
      alignment: align ?? AlignmentType.LEFT,
      spacing: { after: 0, line: 240 },
      children: [new TextRun({ text: String(text), bold, italics, size: size ?? 19, font: "Calibri",
                               color: bold && fill === ACCENT ? "FFFFFF" : undefined })],
    })],
  });
}

function table(headers, rows, widths, aligns) {
  const al = aligns || headers.map((_, i) => i === 0 ? AlignmentType.LEFT : AlignmentType.CENTER);
  return new Table({
    width: { size: W, type: WidthType.DXA },
    columnWidths: widths,
    borders: {
      top:    { style: BorderStyle.SINGLE, size: 4, color: ACCENT },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: ACCENT },
      left:   { style: BorderStyle.SINGLE, size: 2, color: "BFBFBF" },
      right:  { style: BorderStyle.SINGLE, size: 2, color: "BFBFBF" },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: "BFBFBF" },
      insideVertical:   { style: BorderStyle.SINGLE, size: 2, color: "BFBFBF" },
    },
    rows: [
      new TableRow({
        tableHeader: true,
        children: headers.map((h, i) => cell(h, { widths, i, bold: true, fill: ACCENT, align: AlignmentType.CENTER })),
      }),
      ...rows.map((r, ri) => new TableRow({
        children: r.map((c, i) => cell(c, { widths, i, fill: ri % 2 ? SOFT : undefined, align: al[i] })),
      })),
    ],
  });
}

const SPACER = (h = 160) => new Paragraph({ spacing: { after: h }, children: [] });

// Caja de nota
const NOTA = (titulo, texto) => new Table({
  width: { size: W, type: WidthType.DXA },
  columnWidths: [W],
  borders: {
    top:    { style: BorderStyle.SINGLE, size: 2, color: "9CC2E5" },
    bottom: { style: BorderStyle.SINGLE, size: 2, color: "9CC2E5" },
    left:   { style: BorderStyle.SINGLE, size: 18, color: "2E74B5" },
    right:  { style: BorderStyle.SINGLE, size: 2, color: "9CC2E5" },
    insideHorizontal: { style: BorderStyle.NONE },
    insideVertical: { style: BorderStyle.NONE },
  },
  rows: [new TableRow({
    children: [new TableCell({
      width: { size: W, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: "EAF1F8", color: "auto" },
      margins: { top: 120, bottom: 120, left: 160, right: 140 },
      children: [new Paragraph({
        spacing: { after: 0, line: 264 },
        children: [
          new TextRun({ text: titulo + " ", bold: true, size: 20, color: "1F4E79", font: "Calibri" }),
          new TextRun({ text: texto, size: 20, font: "Calibri" }),
        ],
      })],
    })],
  })],
});

// ---------- contenido ----------
const children = [];

// Portada / cabecera
children.push(new Paragraph({
  spacing: { after: 60 },
  children: [new TextRun({ text: "PROTOCOLO DETALLADO", bold: true, size: 19, color: "808080", font: "Calibri" })],
}));
children.push(new Paragraph({
  spacing: { after: 100 },
  children: [new TextRun({ text: "Tratamiento de las muestras: complejos microemulsión/DNA", bold: true, size: 40, color: ACCENT, font: "Calibri" })],
}));
children.push(new Paragraph({
  spacing: { after: 240 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: ACCENT, space: 8 } },
  children: [new TextRun({ text: "Ensayo de dosis-respuesta en cultivo celular", size: 24, color: "595959", font: "Calibri" })],
}));

children.push(table(
  ["Campo", "Dato"],
  [
    ["Fecha del ensayo", "3 de agosto de 2026"],
    ["Responsable", "María Zubieta Laseca"],
    ["Documento de origen", "MATERIALES_UCM.docx (notas de laboratorio)"],
    ["Contenido", "Muestras 1, 2, 4 y 5 + control positivo"],
    ["Vehículo ensayado", "Microemulsión (ME), en dos preparaciones de distinta concentración"],
  ],
  [2400, 6620],
  [AlignmentType.LEFT, AlignmentType.LEFT]
));

children.push(SPACER(240));

// 1. Objeto
children.push(H1("1. Objeto de este documento"));
children.push(P("Este documento desarrolla, ordena y explica las notas de laboratorio del 3 de agosto de 2026, de modo que cualquier persona ajena al ensayo pueda entender exactamente qué se hizo con cada muestra sin necesidad de contexto previo."));
children.push(P("Respecto a las notas originales se han introducido tres tipos de añadidos, siempre señalados como tales:"));
children.push(BULRICH([{ t: "Desarrollo de las tablas de pipeteo", b: true }, ": las tablas originales se reproducen tal cual, y se añade en cada caso una segunda tabla con la dosis que realmente recibe cada pocillo (valores calculados a partir de los datos originales)."]));
children.push(BULRICH([{ t: "Explicación del procedimiento", b: true }, ": los pasos abreviados en las notas se escriben completos y en orden."]));
children.push(BULRICH([{ t: "Puntos pendientes de confirmar", b: true }, ": todo aquello que las notas no especifican se recoge, sin inventar, en el apartado 10."]));
children.push(SPACER(80));
children.push(NOTA("Importante:", "los valores marcados como «calculado» son derivaciones aritméticas de los datos de las notas, no medidas independientes. Conviene revisarlos antes de enviar el documento a terceros."));

// 2. Convenciones
children.push(H1("2. Convenciones y abreviaturas"));
children.push(table(
  ["Abreviatura", "Significado", "Observación"],
  [
    ["ME", "Microemulsión", "Vehículo ensayado. Se emplean dos preparaciones distintas, de distinta concentración (ver más abajo). Su naturaleza oleosa condiciona el ensayo de la muestra 2."],
    ["DNA", "Plásmido a transfectar", "Stock a 583 ng/µl en todos los ensayos"],
    ["DMEM sin FBS", "Medio de dilución de los complejos", "Sin suero, para no interferir en la formación del complejo"],
    ["T ambiente", "Temperatura ambiente", "—"],
    ["Réplica", "Pocillo independiente de una misma condición", "Todas las mezclas de las muestras 1 y 5 se preparan para 4 réplicas"],
  ],
  [1500, 3000, 4520],
  [AlignmentType.LEFT, AlignmentType.LEFT, AlignmentType.LEFT]
));
children.push(SPACER(120));
children.push(RICH([{ t: "Nomenclatura de las condiciones. ", b: true }, "En las muestras 1 y 5 cada condición se nombra por lo que recibe ", { t: "cada pocillo", i: true }, ", no por lo que se pipetea en el eppendorf. Así, la condición «0,25 µl + 0,3 µg DNA» significa que cada pocillo recibe 0,25 µl de ME y 0,3 µg de DNA, aunque en el eppendorf se pipeteen 1 µl de ME y 2 µl de DNA (cantidad para las 4 réplicas)."]));

children.push(RICH([{ t: "Dos preparaciones distintas de microemulsión. ", b: true }, "Las muestras 1 y 5 no emplean la misma preparación de ME, y por eso cada una nombra sus condiciones de una forma: la muestra 1 por volumen y la muestra 5 por masa. Las concentraciones que se deducen de las cantidades anotadas son:"], { before: 120 }));
children.push(table(
  ["Muestra", "Concentración de la ME (calculada)", "Equivalencia que consta en las notas"],
  [
    ["Muestra 1", "37 µg/µl", "0,25 µl ≡ 9,25 µg"],
    ["Muestra 5", "10 µg/µl", "1 µl ≡ 10 µg"],
    ["Muestras 2 y 4", "No consta", "—"],
  ],
  [1800, 3500, 3720],
  [AlignmentType.LEFT, AlignmentType.CENTER, AlignmentType.CENTER]
));
children.push(SPACER(100));
children.push(P("Por tanto, las dosis de ME de la muestra 1 y las de la muestra 5 no son directamente comparables en volumen: hay que compararlas en masa o mediante el ratio ME:DNA.", { italics: true, size: 19 }));

// 3. Procedimiento común
children.push(H1("3. Procedimiento común (muestras 1 y 5)"));
children.push(P("Las muestras 1 y 5 comparten exactamente el mismo esquema de trabajo; solo cambian las cantidades. El procedimiento es:"));
children.push(NUM("Preparar un eppendorf con la ME diluida en DMEM sin FBS, hasta un volumen final de 20 µl."));
children.push(NUM("Preparar un segundo eppendorf con el DNA (stock 583 ng/µl) diluido en DMEM sin FBS, hasta un volumen final de 20 µl."));
children.push(NUM("Añadir el contenido del tubo de ME sobre el tubo de DNA (este orden es el indicado en las notas: «las ME al de DNA»). Volumen final del complejo: 40 µl."));
children.push(NUM("Incubar 15 minutos en balanceo suave a temperatura ambiente, para permitir la formación del complejo ME/DNA."));
children.push(NUM("Añadir 10 µl del complejo a cada pocillo. Los 40 µl alcanzan por tanto para 4 pocillos, es decir, las 4 réplicas de esa condición."));
children.push(SPACER(80));
children.push(NOTA("Cálculo de la dosis por pocillo:", "puesto que cada mezcla de 40 µl se reparte entre 4 pocillos, cada pocillo recibe la cuarta parte de lo pipeteado. Por ejemplo, 1 µl de ME en el eppendorf equivale a 0,25 µl de ME por pocillo; 2 µl de DNA a 583 ng/µl (1.166 ng) equivalen a 291,5 ng (~0,3 µg) por pocillo."));

// 4. Muestra 1
children.push(H1("4. Muestra 1 — Barrido de dosis de ME a dos dosis fijas de DNA"));
children.push(H2("4.1. Qué se ensaya"));
children.push(P("Se combinan 6 dosis crecientes de ME (0,25 / 0,5 / 0,75 / 1,5 / 2 / 2,5 µl por pocillo) con 2 dosis de DNA (0,3 y 0,6 µg por pocillo), dando 12 condiciones. Cada condición se prepara por cuadruplicado."));
children.push(P("El volumen de DNA es el que cambia entre los dos bloques (2 µl para 0,3 µg y 4 µl para 0,6 µg); el volumen total de cada eppendorf se mantiene siempre en 20 µl ajustando con DMEM sin FBS."));

children.push(H2("4.2. Ejemplo desarrollado: condición «0,25 µl + 0,3 µg DNA»"));
children.push(P("Tal como figura en las notas originales:"));
children.push(BUL("Eppendorf A: 19 µl DMEM sin FBS + 1 µl ME"));
children.push(BUL("Eppendorf B: 18 µl DMEM sin FBS + 2 µl DNA (583 ng/µl)"));
children.push(BUL("Se añade A sobre B, 15 min de balanceo suave a T ambiente"));
children.push(BUL("10 µl del complejo a cada uno de los 4 pocillos"));
children.push(P("Resultado por pocillo: 0,25 µl de ME (equivalentes a 9,25 µg de ME según las notas) y ~0,3 µg de DNA.", { before: 60 }));

children.push(H2("4.3. Tabla de pipeteo (volúmenes en µl, para 4 réplicas)"));
children.push(P("Reproducción literal de la tabla de las notas originales.", { italics: true, size: 19, after: 100 }));
children.push(table(
  ["Condición (por pocillo)", "DMEM para ME", "ME", "DNA (583 ng/µl)", "DMEM para DNA"],
  [
    ["0,25 µl + 0,3 µg DNA", "19", "1", "2", "18"],
    ["0,5 µl + 0,3 µg DNA",  "18", "2", "2", "18"],
    ["0,75 µl + 0,3 µg DNA", "17", "3", "2", "18"],
    ["1,5 µl + 0,3 µg DNA",  "14", "6", "2", "18"],
    ["2 µl + 0,3 µg DNA",    "12", "8", "2", "18"],
    ["2,5 µl + 0,3 µg DNA",  "10", "10", "2", "18"],
    ["0,25 µl + 0,6 µg DNA", "19", "1", "4", "16"],
    ["0,5 µl + 0,6 µg DNA",  "18", "2", "4", "16"],
    ["0,75 µl + 0,6 µg DNA", "17", "3", "4", "16"],
    ["1,5 µl + 0,6 µg DNA",  "14", "6", "4", "16"],
    ["2 µl + 0,6 µg DNA",    "12", "8", "4", "16"],
    ["2,5 µl + 0,6 µg DNA",  "10", "10", "4", "16"],
  ],
  [2820, 1700, 1000, 1900, 1600]
));

children.push(SPACER(200));
children.push(H2("4.4. Dosis recibida por cada pocillo (calculado)"));
children.push(P("Valores derivados de la tabla anterior dividiendo entre las 4 réplicas. La masa de ME se obtiene de la equivalencia que dan las propias notas (0,25 µl ≡ 9,25 µg), que corresponde a la preparación de microemulsión a 37 µg/µl empleada en esta muestra.", { italics: true, size: 19, after: 100 }));
children.push(table(
  ["Condición", "ME/pocillo (µl)", "ME/pocillo (µg)", "DNA/pocillo (ng)", "Ratio ME:DNA (m/m)"],
  [
    ["0,25 µl + 0,3 µg", "0,25", "9,25",  "291,5", "~32:1"],
    ["0,5 µl + 0,3 µg",  "0,5",  "18,5",  "291,5", "~63:1"],
    ["0,75 µl + 0,3 µg", "0,75", "27,75", "291,5", "~95:1"],
    ["1,5 µl + 0,3 µg",  "1,5",  "55,5",  "291,5", "~190:1"],
    ["2 µl + 0,3 µg",    "2",    "74",    "291,5", "~254:1"],
    ["2,5 µl + 0,3 µg",  "2,5",  "92,5",  "291,5", "~317:1"],
    ["0,25 µl + 0,6 µg", "0,25", "9,25",  "583",   "~16:1"],
    ["0,5 µl + 0,6 µg",  "0,5",  "18,5",  "583",   "~32:1"],
    ["0,75 µl + 0,6 µg", "0,75", "27,75", "583",   "~48:1"],
    ["1,5 µl + 0,6 µg",  "1,5",  "55,5",  "583",   "~95:1"],
    ["2 µl + 0,6 µg",    "2",    "74",    "583",   "~127:1"],
    ["2,5 µl + 0,6 µg",  "2,5",  "92,5",  "583",   "~159:1"],
  ],
  [2320, 1700, 1700, 1700, 1600]
));

// 5. Muestra 2
children.push(H1("5. Muestra 2 — ME añadidas directamente al medio"));
children.push(H2("5.1. Qué se ensaya"));
children.push(P("A diferencia de las muestras 1 y 5, aquí no se prepara un complejo en DMEM sin FBS: la ME se añade directamente al medio del pocillo. Lo que se varía es el volumen de ME y el volumen de medio en el que queda diluida."));
children.push(RICH([{ t: "Comprobación previa obligatoria. ", b: true }, "Las notas insisten en verificar, antes que ninguna otra cosa, que al añadir la ME al medio ", { t: "no queda flotando en la superficie", b: true }, " por su naturaleza oleosa. Es la primera comprobación del ensayo, previa a cualquier otra."]));

children.push(H2("5.2. Cómo se leen las condiciones"));
children.push(P("El nombre de cada condición tiene la forma «µl de ME + µl de medio final en el pocillo». Partiendo de pocillos con 100 µl de medio, se ajusta el volumen retirando o añadiendo medio antes de incorporar la ME."));
children.push(table(
  ["Condición", "Ajuste del medio", "ME a añadir", "Volumen final", "Dilución ME:medio"],
  [
    ["100 + 100", "No se retira nada", "100 µl", "200 µl", "1:1"],
    ["50 + 50",   "Retirar 50 µl",     "50 µl",  "100 µl", "1:1"],
    ["50 + 150",  "Añadir 50 µl",      "50 µl",  "200 µl", "1:3"],
    ["25 + 75",   "Retirar 25 µl",     "25 µl",  "100 µl", "1:3"],
  ],
  [1500, 2200, 1500, 1720, 2100]
));
children.push(SPACER(120));
children.push(P("Las dos primeras columnas («Condición» y «Ajuste del medio») y la de ME proceden literalmente de las notas; el volumen final y la dilución son cálculos añadidos.", { italics: true, size: 19 }));
children.push(NOTA("Diseño del ensayo:", "las condiciones están emparejadas dos a dos. 100+100 y 50+50 comparten la misma dilución (1:1) pero difieren en la cantidad absoluta de ME; lo mismo ocurre con 50+150 y 25+75 (1:3). Esto permite separar el efecto de la dosis absoluta del efecto de la concentración."));

// 6. Muestra 4
children.push(H1("6. Muestra 4 — ME+DNA en volumen mínimo"));
children.push(P("Las notas recogen esta muestra en una sola línea:"));
children.push(RICH([{ t: "«Echar 1 µl ME+DNA a 10 µl de DMEM sin FBS»", i: true }], { indent: { left: 360 }, shading: { type: ShadingType.CLEAR, fill: SOFT, color: "auto" } }));
children.push(P("La lectura más directa es que se parte de la mezcla ME+DNA ya formada y se toma 1 µl, que se diluye en 10 µl de DMEM sin FBS antes de aplicarlo: es el formato de volumen más reducido de todo el ensayo. La anotación es escueta, por lo que conviene confirmar esta interpretación.", { before: 100 }));
children.push(NOTA("Pendiente de detallar:", "las notas no indican la composición ni la concentración de esa mezcla «ME+DNA» previa, ni el tiempo de incubación, ni el número de réplicas, ni el volumen aplicado finalmente a cada pocillo. Ver apartado 10."));

// 7. Muestra 5
children.push(H1("7. Muestra 5 — Barrido cruzado de masa de ME y masa de DNA"));
children.push(H2("7.1. Qué se ensaya"));
children.push(P("Mismo procedimiento que la muestra 1 (apartado 3), pero aquí las condiciones se expresan en masa de ME (10 y 20 µg por pocillo) cruzada con tres dosis de DNA (0,1 / 0,2 / 0,4 µg por pocillo), lo que da 6 condiciones. Cada una se prepara para 4 réplicas."));

children.push(H2("7.2. Ejemplo desarrollado: condición «10 µg ME + 0,1 µg DNA»"));
children.push(BUL("Eppendorf A: 16 µl DMEM sin FBS + 4 µl ME"));
children.push(BUL("Eppendorf B: 19,3 µl DMEM sin FBS + 0,7 µl DNA (583 ng/µl)"));
children.push(BUL("Se añade A sobre B, 15 min de balanceo suave a T ambiente"));
children.push(BUL("10 µl del complejo a cada uno de los 4 pocillos"));

children.push(H2("7.3. Tabla de pipeteo (volúmenes en µl, para 4 réplicas)"));
children.push(P("Reproducción literal de la tabla de las notas originales.", { italics: true, size: 19, after: 100 }));
children.push(table(
  ["Condición (por pocillo)", "DMEM para ME", "ME", "DNA (583 ng/µl)", "DMEM para DNA"],
  [
    ["10 µg ME + 0,1 µg DNA", "16", "4", "0,7", "19,3"],
    ["10 µg ME + 0,2 µg DNA", "16", "4", "1,4", "18,6"],
    ["20 µg ME + 0,2 µg DNA", "12", "8", "1,4", "18,6"],
    ["20 µg ME + 0,4 µg DNA", "12", "8", "2,7", "17,3"],
    ["20 µg ME + 0,1 µg DNA", "12", "8", "0,7", "19,3"],
    ["10 µg ME + 0,4 µg DNA", "16", "4", "2,7", "17,3"],
  ],
  [2820, 1700, 1000, 1900, 1600]
));

children.push(SPACER(200));
children.push(H2("7.4. Dosis recibida por cada pocillo (calculado)"));
children.push(table(
  ["Condición", "ME/pocillo (µl)", "ME/pocillo (µg)", "DNA/pocillo (ng)", "Ratio ME:DNA (m/m)"],
  [
    ["10 µg + 0,1 µg", "1", "10", "102",   "~98:1"],
    ["10 µg + 0,2 µg", "1", "10", "204",   "~49:1"],
    ["20 µg + 0,2 µg", "2", "20", "204",   "~98:1"],
    ["20 µg + 0,4 µg", "2", "20", "393,5", "~51:1"],
    ["20 µg + 0,1 µg", "2", "20", "102",   "~196:1"],
    ["10 µg + 0,4 µg", "1", "10", "393,5", "~25:1"],
  ],
  [2320, 1700, 1700, 1700, 1600]
));
children.push(SPACER(160));
children.push(NOTA("Preparación distinta a la de la muestra 1:", "la microemulsión empleada aquí está a 10 µg/µl (1 µl por pocillo ≡ 10 µg), frente a los 37 µg/µl de la muestra 1. De ahí que 2 µl por pocillo supongan aquí 20 µg de ME, mientras que en la muestra 1 ese mismo volumen equivale a 74 µg. Las dos muestras solo son comparables en masa de ME o por el ratio ME:DNA."));

// 8. Control positivo
children.push(H1("8. Control positivo (ViaFect)"));
children.push(P("En las notas aparece anotado a continuación de la muestra 4. Composición y procedimiento:"));
children.push(table(
  ["Componente / paso", "Cantidad"],
  [
    ["ViaFect", "2,4 µl"],
    ["DNA (583 ng/µl)", "0,7 µl (≈ 408 ng)"],
    ["DMEM sin FBS", "37 µl"],
    ["Incubación", "10 minutos (frente a los 15 min de los complejos ME/DNA)"],
    ["Volumen aplicado", "10 µl por pocillo"],
    ["Dosis por pocillo (calculado)", "≈ 0,6 µl de ViaFect y ≈ 102 ng de DNA"],
  ],
  [3400, 5620],
  [AlignmentType.LEFT, AlignmentType.LEFT]
));
children.push(SPACER(140));
children.push(P("La dosis de DNA por pocillo del control (≈ 0,1 µg) coincide con la dosis más baja de la muestra 5, lo que permite comparar directamente ambas condiciones."));

// 9. Resumen
children.push(H1("9. Resumen comparativo"));
children.push(table(
  ["Muestra", "Formato", "Variable ensayada", "Nº de condiciones", "Réplicas"],
  [
    ["1", "Complejo ME/DNA en DMEM sin FBS", "Dosis de ME (6) × dosis de DNA (2)", "12", "4"],
    ["2", "ME directa sobre el medio", "Volumen de ME y dilución en el medio", "4", "No consta"],
    ["4", "ME+DNA prediluida en volumen mínimo", "Formato de aplicación", "1", "No consta"],
    ["5", "Complejo ME/DNA en DMEM sin FBS", "Masa de ME (2) × masa de DNA (3)", "6", "4"],
    ["Control +", "ViaFect / DNA", "Referencia de transfección", "1", "No consta"],
  ],
  [1100, 2500, 2700, 1400, 1320],
  [AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.LEFT, AlignmentType.CENTER, AlignmentType.CENTER]
));
children.push(SPACER(140));
children.push(RICH([{ t: "Nota sobre la numeración: ", b: true }, "en las notas originales las muestras aparecen en el orden 1, 2, 5 y 4. Aquí se han reordenado de forma ascendente. ", { t: "La muestra 3 no figura porque no llegó a utilizarse", b: true }, "; la numeración salta de la 2 a la 4."]));

// 10. Pendientes
children.push(H1("10. Puntos pendientes de confirmar antes de enviar"));
children.push(P("Las notas originales son de uso interno y dan por supuesta información que un lector externo no tiene. Antes de enviar este documento conviene completar los siguientes puntos:"));
children.push(BULRICH([{ t: "Preparación de ME de las muestras 2 y 4", b: true }, ": al haber dos preparaciones distintas, conviene indicar cuál se usó en cada una de estas dos muestras y a qué concentración."]));
children.push(BULRICH([{ t: "Identidad del plásmido", b: true }, ": solo consta su concentración (583 ng/µl), no qué construcción es."]));
children.push(BULRICH([{ t: "Línea celular, formato de placa y densidad de siembra", b: true }, ": no constan. Los 100 µl de medio por pocillo de la muestra 2 y los 10 µl de complejo añadidos sugieren placa de 96 pocillos, pero conviene confirmarlo."]));
children.push(BULRICH([{ t: "Réplicas de las muestras 2 y 4", b: true }, ": solo se especifican las de las muestras 1 y 5 (4 réplicas)."]));
children.push(BULRICH([{ t: "Detalles de la muestra 4", b: true }, ": composición de la mezcla ME+DNA de partida, tiempo de incubación y volumen final aplicado."]));
children.push(BULRICH([{ t: "Tiempo de exposición y cambio de medio", b: true }, ": no consta cuánto tiempo permanecen los complejos sobre las células ni si se retiran."]));
children.push(BULRICH([{ t: "Lectura del experimento", b: true }, ": no consta qué se mide (expresión, viabilidad…), con qué método ni a qué tiempo."]));
children.push(BULRICH([{ t: "Control negativo", b: true }, ": solo se documenta el control positivo con ViaFect."]));

// ---------- documento ----------
const doc = new Document({
  creator: "María Zubieta Laseca",
  title: "Tratamiento de las muestras: complejos microemulsión/DNA",
  description: "Protocolo detallado del ensayo del 03/08/2026",
  numbering: {
    config: [
      {
        reference: "vinetas",
        levels: [
          { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 460, hanging: 240 } } } },
          { level: 1, format: LevelFormat.BULLET, text: "◦", alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 880, hanging: 240 } } } },
        ],
      },
      {
        reference: "pasos",
        levels: [
          { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 460, hanging: 300 } } } },
        ],
      },
    ],
  },
  styles: {
    default: { document: { run: { font: "Calibri", size: 21 } } },
  },
  sections: [{
    properties: {
      page: {
        margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 },
      },
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          border: { top: { style: BorderStyle.SINGLE, size: 2, color: "BFBFBF", space: 6 } },
          children: [
            new TextRun({ text: "Tratamiento de las muestras · ensayo 03/08/2026 · pág. ", size: 17, color: "808080", font: "Calibri" }),
            new TextRun({ children: [PageNumber.CURRENT], size: 17, color: "808080", font: "Calibri" }),
            new TextRun({ text: " de ", size: 17, color: "808080", font: "Calibri" }),
            new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 17, color: "808080", font: "Calibri" }),
          ],
        })],
      }),
    },
    children,
  }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync("Tratamiento_muestras_ME-DNA_03-08-2026.docx", b);
  console.log("OK", b.length, "bytes");
});
