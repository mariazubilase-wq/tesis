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

// ========== PORTADA ==========
children.push(new Paragraph({
  spacing: { after: 60 },
  children: [new TextRun({ text: "INFORME DE TRATAMIENTO DE MUESTRAS", bold: true, size: 19, color: "808080", font: "Calibri" })],
}));
children.push(new Paragraph({
  spacing: { after: 100 },
  children: [new TextRun({ text: "Muestras UCM, tanda de julio de 2026", bold: true, size: 40, color: ACCENT, font: "Calibri" })],
}));
children.push(new Paragraph({
  spacing: { after: 240 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: ACCENT, space: 8 } },
  children: [new TextRun({ text: "Condiciones ensayadas en transfección · ensayo del 3 de agosto de 2026", size: 24, color: "595959", font: "Calibri" })],
}));

children.push(table(
  ["Campo", "Dato"],
  [
    ["Ensayo realizado el", "3 de agosto de 2026"],
    ["Responsable", "María Zubieta Laseca — Universidad de Salamanca"],
    ["Muestras recibidas", "Envío de la UCM de 13 de julio de 2026 (muestras 1 a 5)"],
    ["Muestras utilizadas", "1, 2, 4 y 5. La muestra 3 no se ha utilizado todavía."],
    ["Plásmido empleado", "Stock propio a 583 ng/µl (salvo la muestra 2, que ya incorpora pDNA)"],
    ["Objeto", "Detallar diluciones, concentraciones y dosis efectivamente ensayadas con cada muestra"],
  ],
  [2300, 6720],
  [AlignmentType.LEFT, AlignmentType.LEFT]
));

children.push(SPACER(240));

// ========== 1. OBJETO ==========
children.push(H1("1. Objeto"));
children.push(P("Este documento recoge, muestra por muestra, el tratamiento que se ha dado en nuestro laboratorio a las formulaciones enviadas por la UCM: cómo se han diluido, qué cantidades se han empleado, qué dosis recibe finalmente cada pocillo y a qué ratio DOTAP/pDNA corresponde cada condición."));
children.push(P("Las cantidades se expresan de dos formas complementarias: tal como se pipetean en la práctica (lo que permite reproducir el ensayo) y como dosis efectiva por pocillo, que es la magnitud comparable entre muestras. Los ratios DOTAP/pDNA se calculan a partir de las concentraciones facilitadas por la UCM en el correo del 13 de julio, con la corrección del 15 de julio (DOTAP al 1 % en las muestras 2 y 3, no al 4 %)."));
children.push(SPACER(80));
children.push(NOTA("Comprobación previa:", "las concentraciones que se dedujeron de nuestras propias anotaciones coinciden con las facilitadas por la UCM — 37 mg/mL de lípido total en la muestra 1 y 10 mg/mL de liposomas en la muestra 5 —, y el DOTAP al 1 % de la muestra 2 reproduce exactamente el ratio 1000:1 indicado en el correo. Los cálculos de este documento parten, por tanto, de datos verificados por partida doble."));

// ========== 2. IDENTIFICACIÓN ==========
children.push(H1("2. Las muestras y el uso que se les ha dado"));
children.push(P("Resumen de las cinco formulaciones recibidas, con los datos de la UCM que se han utilizado para los cálculos:"));
children.push(table(
  ["Muestra", "Formulación", "Datos empleados en los cálculos", "Uso"],
  [
    ["1", "Microemulsión O/A (fase externa acuosa), DOTAP + DOPE", "Lípido total 37 mg/mL; DOTAP 3,4 mg/mL; ζ +38 mV; gotícula 32 nm", "Ensayada: 12 condiciones"],
    ["2", "Microemulsión A/O (fase externa oleosa) con pDNA encapsulado", "pDNA 10 µg/mL; DOTAP 1 % (10 mg/mL); ratio fijo 1000:1; glóbulo ~20 nm", "Ensayada: 4 condiciones"],
    ["3", "Microemulsión A/O sin pDNA", "DOTAP 1 %, igual que la muestra 2", "No utilizada"],
    ["4", "Liposomas catiónicos DOTAP + DOPE, liofilizados, trehalosa 10 %", "10 µg de DOTAP por liofilizado; tamaño ~150 nm", "Ensayada: 1 condición (datos incompletos, ver apartado 8)"],
    ["5", "Liposomas catiónicos DOTAP + DOPE, sin liofilizar, trehalosa 10 %", "Liposomas 10 mg/mL; DOTAP 1 mg/mL", "Ensayada: 6 condiciones"],
  ],
  [900, 2400, 3320, 2400],
  [AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.LEFT, AlignmentType.LEFT]
));
children.push(SPACER(140));
children.push(RICH([{ t: "Nota sobre la terminología. ", b: true }, "En nuestras anotaciones internas se empleó «ME» como abreviatura genérica para todas las muestras. En este documento cada una se nombra según su naturaleza real: microemulsión en las muestras 1 a 3 y liposomas catiónicos en las muestras 4 y 5."]));

// ========== 3. CONVENCIONES ==========
children.push(H1("3. Datos comunes y forma de leer las tablas"));
children.push(BULRICH([{ t: "Plásmido. ", b: true }, "Stock propio a 583 ng/µl, el mismo en todas las condiciones. La muestra 2 es la excepción: el pDNA ya viene incorporado en la formulación y no se le añade ninguno."]));
children.push(BULRICH([{ t: "Medio de dilución. ", b: true }, "DMEM sin FBS en todos los casos en los que se forma complejo (muestras 1, 4 y 5) y en el control positivo."]));
children.push(BULRICH([{ t: "Réplicas. ", b: true }, "Las mezclas de las muestras 1 y 5 se preparan para 4 réplicas: se hace un volumen único de 40 µl y se reparten 10 µl a cada uno de los 4 pocillos."]));
children.push(BULRICH([{ t: "Dosis por pocillo. ", b: true }, "Es, por tanto, la cuarta parte de lo pipeteado. Las condiciones se nombran siempre por lo que recibe cada pocillo, no por lo que hay en el eppendorf."]));
children.push(BULRICH([{ t: "Ratio DOTAP/pDNA. ", b: true }, "Calculado en masa/masa a partir del contenido en DOTAP que indica la UCM para cada formulación, para poder compararlo directamente con los ratios que ellas han caracterizado."]));

// ========== 4. PROCEDIMIENTO ==========
children.push(H1("4. Procedimiento de formación de complejos (muestras 1 y 5)"));
children.push(P("Ambas muestras se han tratado con el mismo esquema; solo cambian las cantidades:"));
children.push(NUM("Eppendorf A: la muestra (microemulsión o liposomas) diluida en DMEM sin FBS hasta 20 µl."));
children.push(NUM("Eppendorf B: el pDNA diluido en DMEM sin FBS hasta 20 µl."));
children.push(NUM("Se añade A sobre B. Volumen final del complejo: 40 µl."));
children.push(NUM("15 minutos en balanceo suave a temperatura ambiente."));
children.push(NUM("10 µl del complejo a cada uno de los 4 pocillos."));
children.push(SPACER(60));
children.push(NOTA("Desviación respecto a vuestro protocolo:", "el tiempo de balanceo empleado ha sido de 15 minutos, frente a los 20 minutos que indicáis para las muestras 3, 4 y 5. Se detalla en el apartado 12."));

// ========== 5. MUESTRA 1 ==========
children.push(H1("5. Muestra 1 — Microemulsión O/A"));
children.push(P("Se han ensayado 6 volúmenes de microemulsión cruzados con 2 cantidades de pDNA, es decir, 12 condiciones por cuadruplicado."));

children.push(H2("5.1. Pipeteo (volúmenes en µl, para 4 réplicas)"));
children.push(table(
  ["Condición (por pocillo)", "DMEM para la ME", "ME", "pDNA (583 ng/µl)", "DMEM para el pDNA"],
  [
    ["0,25 µl + 0,3 µg", "19", "1", "2", "18"],
    ["0,5 µl + 0,3 µg",  "18", "2", "2", "18"],
    ["0,75 µl + 0,3 µg", "17", "3", "2", "18"],
    ["1,5 µl + 0,3 µg",  "14", "6", "2", "18"],
    ["2 µl + 0,3 µg",    "12", "8", "2", "18"],
    ["2,5 µl + 0,3 µg",  "10", "10", "2", "18"],
    ["0,25 µl + 0,6 µg", "19", "1", "4", "16"],
    ["0,5 µl + 0,6 µg",  "18", "2", "4", "16"],
    ["0,75 µl + 0,6 µg", "17", "3", "4", "16"],
    ["1,5 µl + 0,6 µg",  "14", "6", "4", "16"],
    ["2 µl + 0,6 µg",    "12", "8", "4", "16"],
    ["2,5 µl + 0,6 µg",  "10", "10", "4", "16"],
  ],
  [2620, 1800, 1000, 1900, 1700]
));

children.push(SPACER(200));
children.push(H2("5.2. Dosis por pocillo y ratio DOTAP/pDNA"));
children.push(P("Calculado con lípido total 37 µg/µl y DOTAP 3,4 µg/µl de microemulsión.", { italics: true, size: 19, after: 100 }));
children.push(table(
  ["Condición", "ME (µl)", "Lípido total (µg)", "DOTAP (µg)", "pDNA (ng)", "DOTAP/pDNA"],
  [
    ["0,25 µl + 0,3 µg", "0,25", "9,25",  "0,85", "291,5", "2,9:1"],
    ["0,5 µl + 0,3 µg",  "0,5",  "18,5",  "1,70", "291,5", "5,8:1"],
    ["0,75 µl + 0,3 µg", "0,75", "27,75", "2,55", "291,5", "8,7:1"],
    ["1,5 µl + 0,3 µg",  "1,5",  "55,5",  "5,10", "291,5", "17,5:1"],
    ["2 µl + 0,3 µg",    "2",    "74",    "6,80", "291,5", "23,3:1"],
    ["2,5 µl + 0,3 µg",  "2,5",  "92,5",  "8,50", "291,5", "29,2:1"],
    ["0,25 µl + 0,6 µg", "0,25", "9,25",  "0,85", "583",   "1,5:1"],
    ["0,5 µl + 0,6 µg",  "0,5",  "18,5",  "1,70", "583",   "2,9:1"],
    ["0,75 µl + 0,6 µg", "0,75", "27,75", "2,55", "583",   "4,4:1"],
    ["1,5 µl + 0,6 µg",  "1,5",  "55,5",  "5,10", "583",   "8,7:1"],
    ["2 µl + 0,6 µg",    "2",    "74",    "6,80", "583",   "11,7:1"],
    ["2,5 µl + 0,6 µg",  "2,5",  "92,5",  "8,50", "583",   "14,6:1"],
  ],
  [2020, 1000, 1700, 1500, 1400, 1400]
));
children.push(SPACER(160));
children.push(NOTA("Correspondencia con vuestros ratios de referencia:", "la serie de 0,3 µg de pDNA cubre el intervalo que habéis caracterizado por retardo en gel. La condición de 1,5 µl equivale a 17,5:1 (vuestro 17:1) y la de 2,5 µl a 29,2:1 (próxima a vuestro 27:1); vuestro 7:1 queda entre las condiciones de 0,5 µl (5,8:1) y 0,75 µl (8,7:1). La serie de 0,6 µg de pDNA explora deliberadamente por debajo, entre 1,5:1 y 14,6:1."));

// ========== 6. MUESTRA 2 ==========
children.push(H1("6. Muestra 2 — Microemulsión A/O con pDNA encapsulado"));
children.push(P("Al llevar el pDNA ya incorporado en la fase acuosa interna, esta muestra no requiere formación previa de complejo: se ha añadido directamente sobre el medio del pocillo. Lo que se ha variado es el volumen de microemulsión y el volumen de medio en el que queda diluida."));
children.push(RICH([{ t: "Comprobación previa. ", b: true }, "Antes de nada se verificó que, al añadirla al medio, la microemulsión no quedaba flotando en la superficie por su carácter oleoso."]));

children.push(H2("6.1. Preparación de los pocillos"));
children.push(P("Partiendo de pocillos con 100 µl de medio, se ajustó el volumen antes de incorporar la muestra. Las condiciones se nombran «µl de microemulsión + µl de medio».", { after: 100 }));
children.push(table(
  ["Condición", "Ajuste del medio", "ME añadida", "Volumen final"],
  [
    ["100 + 100", "No se retira nada", "100 µl", "200 µl"],
    ["50 + 50",   "Retirar 50 µl",     "50 µl",  "100 µl"],
    ["50 + 150",  "Añadir 50 µl",      "50 µl",  "200 µl"],
    ["25 + 75",   "Retirar 25 µl",     "25 µl",  "100 µl"],
  ],
  [1900, 2700, 2100, 2320]
));

children.push(SPACER(200));
children.push(H2("6.2. Dosis por pocillo"));
children.push(P("Calculado con pDNA 10 µg/mL y DOTAP al 1 % (10 µg/µl).", { italics: true, size: 19, after: 100 }));
children.push(table(
  ["Condición", "ME (µl)", "pDNA (µg)", "DOTAP (µg)", "DOTAP/pDNA"],
  [
    ["100 + 100", "100", "1,00", "1.000", "1000:1"],
    ["50 + 50",   "50",  "0,50", "500",   "1000:1"],
    ["50 + 150",  "50",  "0,50", "500",   "1000:1"],
    ["25 + 75",   "25",  "0,25", "250",   "1000:1"],
  ],
  [1900, 1600, 1800, 1800, 1920]
));
children.push(SPACER(140));
children.push(P("El ratio es fijo, al venir determinado por la propia formulación; lo que varía entre condiciones es la dosis absoluta y la dilución. Las parejas 100+100 / 50+50 y 50+150 / 25+75 comparten dilución (1:1 y 1:3 respectivamente) pero difieren en cantidad absoluta, lo que permite separar ambos efectos."));
children.push(SPACER(60));
children.push(NOTA("Observación:", "la carga de DOTAP por pocillo de esta muestra (250–1.000 µg) es dos o tres órdenes de magnitud superior a la de la muestra 1 (0,85–8,5 µg), consecuencia directa del ratio 1000:1 de la formulación. Lo señalamos porque condiciona la lectura de cualquier resultado de viabilidad."));

// ========== 7. MUESTRA 3 ==========
children.push(H1("7. Muestra 3 — Microemulsión A/O sin pDNA"));
children.push(P("No se ha utilizado en este ensayo; se conserva íntegra."));
children.push(P("Queda pendiente emplearla como control sin material genético y para ensayar la formación de complejos por interacción electrostática siguiendo el procedimiento que describís (volumen determinado de muestra más la cantidad deseada de pDNA, 20 minutos de balanceo suave)."));

// ========== 8. MUESTRA 4 ==========
children.push(H1("8. Muestra 4 — Liposomas liofilizados"));
children.push(P("De esta muestra se ensayó una única condición. La anotación de laboratorio recoge que se tomó 1 µl de la mezcla liposomas + pDNA y se llevó a 10 µl de DMEM sin FBS."));
children.push(SPACER(60));
children.push(NOTA("Información incompleta:", "no quedó registrado el volumen en el que se resuspendió el liofilizado ni la cantidad de pDNA empleada en esa resuspensión, por lo que no podemos calcular con fiabilidad la dosis por pocillo ni el ratio DOTAP/pDNA de esta condición. Preferimos indicarlo antes que dar una cifra que no podemos sostener. La condición se repetirá dejando constancia de ambos datos."));

// ========== 9. MUESTRA 5 ==========
children.push(H1("9. Muestra 5 — Liposomas sin liofilizar"));
children.push(P("Se han ensayado 2 cantidades de liposomas cruzadas con 3 de pDNA, es decir, 6 condiciones por cuadruplicado. El procedimiento es el del apartado 4."));

children.push(H2("9.1. Pipeteo (volúmenes en µl, para 4 réplicas)"));
children.push(table(
  ["Condición (por pocillo)", "DMEM para liposomas", "Liposomas", "pDNA (583 ng/µl)", "DMEM para el pDNA"],
  [
    ["10 µg + 0,1 µg", "16", "4", "0,7", "19,3"],
    ["10 µg + 0,2 µg", "16", "4", "1,4", "18,6"],
    ["20 µg + 0,2 µg", "12", "8", "1,4", "18,6"],
    ["20 µg + 0,4 µg", "12", "8", "2,7", "17,3"],
    ["20 µg + 0,1 µg", "12", "8", "0,7", "19,3"],
    ["10 µg + 0,4 µg", "16", "4", "2,7", "17,3"],
  ],
  [2620, 1900, 1300, 1700, 1500]
));

children.push(SPACER(200));
children.push(H2("9.2. Dosis por pocillo y ratio DOTAP/pDNA"));
children.push(P("Calculado con liposomas 10 µg/µl y DOTAP 1 µg/µl.", { italics: true, size: 19, after: 100 }));
children.push(table(
  ["Condición", "Liposomas (µl)", "Liposomas (µg)", "DOTAP (µg)", "pDNA (ng)", "DOTAP/pDNA"],
  [
    ["10 µg + 0,1 µg", "1", "10", "1,0", "102",   "9,8:1"],
    ["10 µg + 0,2 µg", "1", "10", "1,0", "204",   "4,9:1"],
    ["20 µg + 0,2 µg", "2", "20", "2,0", "204",   "9,8:1"],
    ["20 µg + 0,4 µg", "2", "20", "2,0", "393,5", "5,1:1"],
    ["20 µg + 0,1 µg", "2", "20", "2,0", "102",   "19,6:1"],
    ["10 µg + 0,4 µg", "1", "10", "1,0", "393,5", "2,5:1"],
  ],
  [2020, 1600, 1600, 1300, 1200, 1300]
));
children.push(SPACER(160));
children.push(NOTA("Correspondencia con vuestro ratio de referencia:", "dos de las seis condiciones (10 µg + 0,1 µg y 20 µg + 0,2 µg) equivalen a 9,8:1, es decir, al 10:1 que habéis evaluado. Las demás lo flanquean: 19,6:1 por encima y 5,1:1, 4,9:1 y 2,5:1 por debajo."));

// ========== 10. CONTROL ==========
children.push(H1("10. Control positivo"));
children.push(P("Como referencia de transfección se empleó ViaFect:"));
children.push(table(
  ["Componente / paso", "Cantidad"],
  [
    ["ViaFect", "2,4 µl"],
    ["pDNA (583 ng/µl)", "0,7 µl (≈ 408 ng)"],
    ["DMEM sin FBS", "37 µl"],
    ["Incubación", "10 minutos"],
    ["Volumen aplicado", "10 µl por pocillo"],
    ["Dosis por pocillo", "≈ 0,6 µl de ViaFect y ≈ 102 ng de pDNA"],
  ],
  [3400, 5620],
  [AlignmentType.LEFT, AlignmentType.LEFT]
));
children.push(SPACER(140));
children.push(P("La dosis de pDNA del control (≈ 0,1 µg por pocillo) coincide con la más baja de la muestra 5, de modo que ambas condiciones son directamente comparables."));

// ========== 11. RESUMEN ==========
children.push(H1("11. Resumen de los ratios DOTAP/pDNA ensayados"));
children.push(table(
  ["Muestra", "Condiciones", "DOTAP por pocillo", "pDNA por pocillo", "Ratio DOTAP/pDNA", "Vuestra referencia"],
  [
    ["1", "12", "0,85 – 8,5 µg", "0,29 y 0,58 µg", "1,5:1 – 29,2:1", "7:1, 17:1, 27:1"],
    ["2", "4", "250 – 1.000 µg", "0,25 – 1,0 µg", "1000:1 (fijo)", "1000:1"],
    ["3", "—", "—", "—", "No utilizada", "—"],
    ["4", "1", "Sin determinar", "Sin determinar", "Sin determinar", "10:1"],
    ["5", "6", "1,0 y 2,0 µg", "0,10 – 0,39 µg", "2,5:1 – 19,6:1", "10:1"],
  ],
  [900, 1200, 1800, 1700, 1700, 1720],
  [AlignmentType.CENTER, AlignmentType.CENTER, AlignmentType.CENTER, AlignmentType.CENTER, AlignmentType.CENTER, AlignmentType.CENTER]
));
children.push(SPACER(140));
children.push(P("En las muestras 1 y 5 el diseño se ha construido de modo que los ratios que vosotras habéis caracterizado queden dentro del intervalo ensayado, con condiciones por encima y por debajo que permitan situarlos."));

// ========== 12. DESVIACIONES ==========
children.push(H1("12. Desviaciones respecto a lo indicado por la UCM"));
children.push(BULRICH([{ t: "Tiempo de balanceo: 15 minutos en lugar de 20. ", b: true }, "Para las muestras 1 y 5 se emplearon 15 minutos de balanceo suave a temperatura ambiente. Vuestro procedimiento indica 20 minutos para las muestras 3, 4 y 5. Si consideráis que la diferencia puede afectar a la formación del complejo, repetiremos las condiciones con el tiempo que nos indiquéis."]));
children.push(BULRICH([{ t: "Muestra 4: registro incompleto. ", b: true }, "No se anotó el volumen de resuspensión del liofilizado ni la cantidad de pDNA empleada, por lo que la condición no es interpretable cuantitativamente y se repetirá."]));
children.push(BULRICH([{ t: "Muestra 3: no ensayada. ", b: true }, "Se conserva íntegra para los ensayos de formación de complejo y como control sin material genético."]));
children.push(BULRICH([{ t: "Corrección del DOTAP. ", b: true }, "Todos los cálculos de las muestras 2 y 3 se han hecho con el DOTAP al 1 % que nos indicasteis el 15 de julio, no con el 4 % del correo inicial."]));

// ========== 13. CONSULTAS ==========
children.push(H1("13. Consultas"));
children.push(BULRICH([{ t: "Muestra 4: contenido real del liofilizado. ", b: true }, "En la descripción figura que cada liofilizado contiene 10 µg de DOTAP y, más abajo, que la cantidad enviada es «liofilizado equivalente a 10 µg de liposomas liofilizados». Con liposomas a 10 mg/mL y DOTAP a 1 mg/mL, 10 µg de liposomas contendrían 1 µg de DOTAP, no 10 µg. ¿Nos confirmáis cuál de las dos cifras es la correcta? De ello depende el ratio al que estemos trabajando, con un factor de 10 de diferencia."]));
children.push(BULRICH([{ t: "Muestra 4: volumen de resuspensión recomendado. ", b: true }, "Al repetir la condición, ¿hay algún volumen de resuspensión que recomendéis, o es indiferente mientras se respete el ratio?"]));
children.push(BULRICH([{ t: "Muestra 2: identidad del pDNA encapsulado. ", b: true }, "¿Nos confirmáis qué plásmido se encapsuló, para asegurarnos de que la lectura es comparable con la de las demás muestras, en las que empleamos nuestro stock propio?"]));
children.push(BULRICH([{ t: "Tiempo de complejación en la muestra 1. ", b: true }, "El correo no especifica tiempo de balanceo para esta muestra. ¿Recomendáis también 20 minutos?"]));
// ---------- documento ----------
const doc = new Document({
  creator: "María Zubieta Laseca",
  title: "Muestras UCM julio 2026 — informe de tratamiento",
  description: "Condiciones ensayadas con las muestras UCM en el ensayo del 03/08/2026",
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
            new TextRun({ text: "Muestras UCM julio 2026 · ensayo 03/08/2026 · pág. ", size: 17, color: "808080", font: "Calibri" }),
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
  fs.writeFileSync("Informe_muestras_UCM_ensayo_03-08-2026.docx", b);
  console.log("OK", b.length, "bytes");
});
