const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  LevelFormat, Footer, PageNumber
} = require('docx');
const fs = require('fs');

const ACCENT = "1F4E79";
const SOFT   = "F2F2F2";
const W = 9740;             // A4 vertical menos márgenes

const P = (text, o = {}) => new Paragraph({
  spacing: { before: o.before ?? 0, after: o.after ?? 100, line: 264 },
  alignment: o.align,
  children: [new TextRun({ text, bold: o.bold, italics: o.italics, size: o.size ?? 20, color: o.color, font: "Calibri" })],
});

const RICH = (runs, o = {}) => new Paragraph({
  spacing: { before: o.before ?? 0, after: o.after ?? 100, line: 264 },
  children: runs.map(r => typeof r === 'string'
    ? new TextRun({ text: r, size: o.size ?? 20, font: "Calibri" })
    : new TextRun({ text: r.t, bold: r.b, italics: r.i, size: o.size ?? 20, font: "Calibri" })),
});

const H1 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 280, after: 120 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: ACCENT, space: 3 } },
  children: [new TextRun({ text, bold: true, size: 25, color: ACCENT, font: "Calibri" })],
});

const BUL = (runs) => new Paragraph({
  numbering: { reference: "vinetas", level: 0 },
  spacing: { after: 60, line: 264 },
  children: runs.map(r => typeof r === 'string'
    ? new TextRun({ text: r, size: 20, font: "Calibri" })
    : new TextRun({ text: r.t, bold: r.b, italics: r.i, size: 20, font: "Calibri" })),
});

function cell(text, { widths, i, bold, fill, align, size } = {}) {
  return new TableCell({
    width: { size: widths[i], type: WidthType.DXA },
    shading: fill ? { type: ShadingType.CLEAR, fill, color: "auto" } : undefined,
    margins: { top: 40, bottom: 40, left: 70, right: 70 },
    children: [new Paragraph({
      alignment: align ?? AlignmentType.LEFT,
      spacing: { after: 0, line: 228 },
      children: [new TextRun({ text: String(text), bold, size: size ?? 17, font: "Calibri",
                               color: bold && fill === ACCENT ? "FFFFFF" : undefined })],
    })],
  });
}

function table(headers, rows, widths, aligns, size) {
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
        children: headers.map((h, i) => cell(h, { widths, i, bold: true, fill: ACCENT, align: AlignmentType.CENTER, size })),
      }),
      ...rows.map((r, ri) => new TableRow({
        children: r.map((c, i) => cell(c, { widths, i, fill: ri % 2 ? SOFT : undefined, align: al[i], size })),
      })),
    ],
  });
}

const SPACER = (h = 120) => new Paragraph({ spacing: { after: h }, children: [] });

const NOTA = (titulo, texto) => new Table({
  width: { size: W, type: WidthType.DXA },
  columnWidths: [W],
  borders: {
    top: { style: BorderStyle.SINGLE, size: 2, color: "9CC2E5" },
    bottom: { style: BorderStyle.SINGLE, size: 2, color: "9CC2E5" },
    left: { style: BorderStyle.SINGLE, size: 18, color: "2E74B5" },
    right: { style: BorderStyle.SINGLE, size: 2, color: "9CC2E5" },
    insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
  },
  rows: [new TableRow({ children: [new TableCell({
    width: { size: W, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: "EAF1F8", color: "auto" },
    margins: { top: 90, bottom: 90, left: 150, right: 130 },
    children: [new Paragraph({ spacing: { after: 0, line: 252 }, children: [
      new TextRun({ text: titulo + " ", bold: true, size: 19, color: "1F4E79", font: "Calibri" }),
      new TextRun({ text: texto, size: 19, font: "Calibri" }),
    ]})],
  })]})],
});

// ================= CONTENIDO =================
const children = [];

children.push(new Paragraph({
  spacing: { after: 40 },
  children: [new TextRun({ text: "Muestras UCM, tanda de julio de 2026", bold: true, size: 34, color: ACCENT, font: "Calibri" })],
}));
children.push(new Paragraph({
  spacing: { after: 180 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 10, color: ACCENT, space: 6 } },
  children: [new TextRun({ text: "Condiciones ensayadas en transfección · ensayo del 3 de agosto de 2026 · María Zubieta Laseca, Universidad de Salamanca", size: 21, color: "595959", font: "Calibri" })],
}));

children.push(P("Detalle de cómo se ha diluido y empleado cada muestra: dosis y concentración por pocillo y ratios ME:pDNA, ME:DOTAP y DOTAP:pDNA de cada condición. Las concentraciones de partida son las de vuestro correo del 13 de julio, con la corrección del 15 de julio (DOTAP al 1 % en las muestras 2 y 3)."));
children.push(SPACER(60));
children.push(NOTA("Verificación:", "las concentraciones deducidas de nuestras propias anotaciones coinciden con las vuestras (37 mg/mL de lípido total en la muestra 1; 10 mg/mL de liposomas en la muestra 5), y el DOTAP al 1 % de la muestra 2 reproduce exactamente vuestro ratio 1000:1."));

// ---- 1. MUESTRAS ----
children.push(H1("1. Las muestras y el uso que se les ha dado"));
children.push(table(
  ["Muestra", "Formulación", "Datos empleados en los cálculos", "Uso"],
  [
    ["1", "Microemulsión O/A, DOTAP + DOPE", "Lípido total 37 mg/mL · DOTAP 3,4 mg/mL · ζ +38 mV · 32 nm", "12 condiciones"],
    ["2", "Microemulsión A/O con pDNA encapsulado", "pDNA 10 µg/mL · DOTAP 1 % (10 mg/mL) · ~20 nm", "4 condiciones"],
    ["3", "Microemulsión A/O sin pDNA", "DOTAP 1 %, igual que la muestra 2", "No utilizada; se conserva íntegra"],
    ["4", "Liposomas DOTAP + DOPE liofilizados, trehalosa 10 %", "10 µg de DOTAP por liofilizado · ~150 nm", "1 condición"],
    ["5", "Liposomas DOTAP + DOPE sin liofilizar, trehalosa 10 %", "Liposomas 10 mg/mL · DOTAP 1 mg/mL", "6 condiciones"],
  ],
  [850, 2600, 4090, 2200],
  [AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.LEFT, AlignmentType.LEFT]
));
children.push(SPACER(100));
children.push(RICH([{ t: "Qué significa «ME» en cada tabla. ", b: true }, "Nuestras notas internas usaban «ME» para todas las muestras. Aquí el ratio ME:pDNA se refiere al ", { t: "lípido total", b: true }, " en la muestra 1, a la ", { t: "microemulsión completa", b: true }, " en la muestra 2 y a los ", { t: "liposomas", b: true }, " en la muestra 5. El ratio ME:DOTAP es constante en cada muestra porque lo fija la formulación."], { size: 19 }));

// ---- 2. PROCEDIMIENTO ----
children.push(H1("2. Procedimiento (muestras 1 y 5)"));
children.push(P("Muestra diluida en DMEM sin FBS hasta 20 µl en un eppendorf; pDNA (stock propio a 583 ng/µl) diluido en DMEM sin FBS hasta 20 µl en otro; se añade el primero sobre el segundo; 15 minutos de balanceo suave a temperatura ambiente; 10 µl del complejo a cada uno de los 4 pocillos. Cada mezcla de 40 µl cubre las 4 réplicas, de modo que cada pocillo recibe la cuarta parte de lo pipeteado."));
children.push(P("La muestra 2 no requiere complejación —ya lleva el pDNA— y se añadió directamente al medio; se comprobó antes que no quedaba flotando por su carácter oleoso."));
children.push(SPACER(60));
children.push(NOTA("Base de cálculo de las concentraciones:", "en las muestras 1 y 5 se toma un volumen final de 110 µl por pocillo (100 µl de medio + 10 µl de complejo). En la muestra 2 los volúmenes finales son exactos y constan en su tabla."));

// ---- 3. MUESTRA 1 ----
children.push(H1("3. Muestra 1 — Microemulsión O/A · ME:DOTAP 10,9:1"));
children.push(table(
  ["Condición (por pocillo)", "Pipeteo ME+DMEM / pDNA+DMEM (µl)", "ME (µg)", "[ME] (µg/mL)", "DOTAP (µg)", "pDNA (ng)", "ME:pDNA", "ME:DOTAP", "DOTAP:pDNA"],
  [
    ["0,25 µl + 0,3 µg", "1+19 / 2+18",  "9,25",  "84",  "0,85", "291,5", "32:1",  "10,9:1", "2,9:1"],
    ["0,5 µl + 0,3 µg",  "2+18 / 2+18",  "18,5",  "168", "1,70", "291,5", "63:1",  "10,9:1", "5,8:1"],
    ["0,75 µl + 0,3 µg", "3+17 / 2+18",  "27,75", "252", "2,55", "291,5", "95:1",  "10,9:1", "8,7:1"],
    ["1,5 µl + 0,3 µg",  "6+14 / 2+18",  "55,5",  "505", "5,10", "291,5", "190:1", "10,9:1", "17,5:1"],
    ["2 µl + 0,3 µg",    "8+12 / 2+18",  "74",    "673", "6,80", "291,5", "254:1", "10,9:1", "23,3:1"],
    ["2,5 µl + 0,3 µg",  "10+10 / 2+18", "92,5",  "841", "8,50", "291,5", "317:1", "10,9:1", "29,2:1"],
    ["0,25 µl + 0,6 µg", "1+19 / 4+16",  "9,25",  "84",  "0,85", "583",   "16:1",  "10,9:1", "1,5:1"],
    ["0,5 µl + 0,6 µg",  "2+18 / 4+16",  "18,5",  "168", "1,70", "583",   "32:1",  "10,9:1", "2,9:1"],
    ["0,75 µl + 0,6 µg", "3+17 / 4+16",  "27,75", "252", "2,55", "583",   "48:1",  "10,9:1", "4,4:1"],
    ["1,5 µl + 0,6 µg",  "6+14 / 4+16",  "55,5",  "505", "5,10", "583",   "95:1",  "10,9:1", "8,7:1"],
    ["2 µl + 0,6 µg",    "8+12 / 4+16",  "74",    "673", "6,80", "583",   "127:1", "10,9:1", "11,7:1"],
    ["2,5 µl + 0,6 µg",  "10+10 / 4+16", "92,5",  "841", "8,50", "583",   "159:1", "10,9:1", "14,6:1"],
  ],
  [1250, 1500, 950, 1150, 1000, 950, 1000, 1050, 890], null, 16
));
children.push(SPACER(100));
children.push(NOTA("Frente a vuestros ratios de referencia:", "la serie de 0,3 µg de pDNA cubre el intervalo que habéis caracterizado en gel — 1,5 µl equivale a 17,5:1 (vuestro 17:1) y 2,5 µl a 29,2:1 (próximo a 27:1); vuestro 7:1 cae entre 0,5 µl (5,8:1) y 0,75 µl (8,7:1). La serie de 0,6 µg explora por debajo, de 1,5:1 a 14,6:1."));

// ---- 4. MUESTRA 2 ----
children.push(H1("4. Muestra 2 — Microemulsión A/O con pDNA encapsulado · ME:DOTAP 100:1"));
children.push(P("Condiciones nombradas «µl de microemulsión + µl de medio». Partiendo de pocillos con 100 µl de medio: en 100+100 no se retira nada, en 50+50 se retiran 50 µl, en 50+150 se añaden 50 µl y en 25+75 se retiran 25 µl. El ratio DOTAP:pDNA lo fija la formulación, de modo que solo varían la dosis absoluta y la dilución: las parejas 100+100 / 50+50 y 50+150 / 25+75 comparten concentración pero no cantidad.", { size: 19 }));
children.push(table(
  ["Condición", "ME (µl)", "Vol. final (µl)", "ME (% v/v)", "pDNA (µg)", "DOTAP (µg)", "ME:pDNA", "ME:DOTAP", "DOTAP:pDNA"],
  [
    ["100 + 100", "100", "200", "50 %", "1,00", "1.000", "100.000:1", "100:1", "1000:1"],
    ["50 + 50",   "50",  "100", "50 %", "0,50", "500",   "100.000:1", "100:1", "1000:1"],
    ["50 + 150",  "50",  "200", "25 %", "0,50", "500",   "100.000:1", "100:1", "1000:1"],
    ["25 + 75",   "25",  "100", "25 %", "0,25", "250",   "100.000:1", "100:1", "1000:1"],
  ],
  [1300, 950, 1100, 1000, 1000, 1050, 1400, 1050, 890], null, 16
));
children.push(SPACER(100));
children.push(NOTA("Dos apuntes:", "el ratio ME:pDNA de esta muestra asume densidad ≈ 1 g/mL para la microemulsión; confirmadnos si preferís otro valor. Y la carga de DOTAP por pocillo (250–1.000 µg) es dos o tres órdenes de magnitud mayor que en la muestra 1 (0,85–8,5 µg), consecuencia del ratio 1000:1 de la formulación; lo señalamos porque condiciona cualquier lectura de viabilidad."));

// ---- 5. MUESTRA 4 ----
children.push(H1("5. Muestra 4 — Liposomas liofilizados · ME:DOTAP 10:1"));
children.push(P("El liofilizado se resuspendió en 20 µl de disolución de pDNA a 50 ng/µl, siguiendo vuestro procedimiento de rehidratar el liofilizado con la propia cantidad objetivo de material genético. De esa resuspensión se tomó 1 µl y se llevó a 10 µl de DMEM sin FBS."));
children.push(table(
  ["Concepto", "Valor", "Observación"],
  [
    ["Resuspensión del liofilizado", "20 µl de pDNA a 50 ng/µl", "Rehidratación directa con el pDNA"],
    ["DOTAP", "10 µg", "Contenido declarado del liofilizado"],
    ["pDNA", "1,00 µg", "20 µl × 50 ng/µl"],
    ["Liposomas (ME)", "100 µg", "Deducido del DOTAP y del ratio 10:1 de la formulación"],
    ["ME:pDNA", "100:1", "—"],
    ["ME:DOTAP", "10:1", "Fijado por la formulación"],
    ["DOTAP:pDNA", "10:1", "Coincide con el ratio que habéis evaluado"],
    ["Aplicación", "1 µl de la resuspensión en 10 µl de DMEM sin FBS", "Equivale a 0,5 µg de DOTAP y 50 ng de pDNA"],
  ],
  [2900, 3300, 3540],
  [AlignmentType.LEFT, AlignmentType.LEFT, AlignmentType.LEFT]
));
children.push(SPACER(100));
children.push(NOTA("Dos salvedades:", "la concentración de la disolución de pDNA empleada en la resuspensión está pendiente de contrastar con el registro de laboratorio; el valor de 50 ng/µl es el coherente con el ratio 10:1. Y la masa de liposomas depende de qué cifra del liofilizado sea la correcta (ver consultas): si contuviera 1 µg de DOTAP en lugar de 10 µg, el ratio DOTAP:pDNA sería 1:1 y no 10:1."));

// ---- 6. MUESTRA 5 ----
children.push(H1("6. Muestra 5 — Liposomas sin liofilizar · ME:DOTAP 10:1"));
children.push(table(
  ["Condición (por pocillo)", "Pipeteo lip.+DMEM / pDNA+DMEM (µl)", "Liposomas (µg)", "[ME] (µg/mL)", "DOTAP (µg)", "pDNA (ng)", "ME:pDNA", "ME:DOTAP", "DOTAP:pDNA"],
  [
    ["10 µg + 0,1 µg", "4+16 / 0,7+19,3", "10", "91",  "1,0", "102",   "98:1",  "10:1", "9,8:1"],
    ["10 µg + 0,2 µg", "4+16 / 1,4+18,6", "10", "91",  "1,0", "204",   "49:1",  "10:1", "4,9:1"],
    ["20 µg + 0,2 µg", "8+12 / 1,4+18,6", "20", "182", "2,0", "204",   "98:1",  "10:1", "9,8:1"],
    ["20 µg + 0,4 µg", "8+12 / 2,7+17,3", "20", "182", "2,0", "393,5", "51:1",  "10:1", "5,1:1"],
    ["20 µg + 0,1 µg", "8+12 / 0,7+19,3", "20", "182", "2,0", "102",   "196:1", "10:1", "19,6:1"],
    ["10 µg + 0,4 µg", "4+16 / 2,7+17,3", "10", "91",  "1,0", "393,5", "25:1",  "10:1", "2,5:1"],
  ],
  [1250, 1500, 950, 1150, 1000, 950, 1000, 1050, 890], null, 16
));
children.push(SPACER(100));
children.push(NOTA("Frente a vuestro ratio de referencia:", "las condiciones 10 µg + 0,1 µg y 20 µg + 0,2 µg equivalen a 9,8:1, es decir, a vuestro 10:1. Las demás lo flanquean: 19,6:1 por encima y 5,1:1, 4,9:1 y 2,5:1 por debajo."));

// ---- 7. CONTROL ----
children.push(H1("7. Control positivo"));
children.push(P("ViaFect 2,4 µl + 0,7 µl de pDNA (≈ 408 ng) + 37 µl de DMEM sin FBS, 10 minutos, 10 µl por pocillo. Por pocillo: ≈ 0,6 µl de ViaFect y ≈ 102 ng de pDNA, la misma dosis de pDNA que la condición más baja de la muestra 5."));

// ---- 8. DESVIACIONES Y CONSULTAS ----
children.push(H1("8. Desviaciones y consultas"));
children.push(P("Desviaciones respecto a vuestro procedimiento:", { bold: true, after: 70 }));
children.push(BUL([{ t: "Balanceo de 15 minutos en lugar de 20 ", b: true }, "en las muestras 1 y 5. Si creéis que puede afectar a la formación del complejo, repetimos con el tiempo que nos digáis."]));
children.push(BUL([{ t: "Muestra 4: una sola condición ensayada. ", b: true }, "La concentración exacta del pDNA empleado en la resuspensión está pendiente de contrastar con el registro de laboratorio."]));
children.push(BUL([{ t: "Muestra 3: no ensayada. ", b: true }, "Se conserva para los ensayos de formación de complejo y como control sin material genético."]));
children.push(SPACER(80));
children.push(P("Consultas:", { bold: true, after: 70 }));
children.push(BUL([{ t: "Muestra 4, contenido del liofilizado. ", b: true }, "La descripción dice que cada liofilizado contiene 10 µg de DOTAP y, más abajo, que la cantidad enviada es «liofilizado equivalente a 10 µg de liposomas liofilizados». Con liposomas a 10 mg/mL y DOTAP a 1 mg/mL, 10 µg de liposomas contendrían 1 µg de DOTAP. ¿Cuál de las dos cifras es la correcta? De ello depende que nuestra condición esté a 10:1 o a 1:1."]));
children.push(BUL([{ t: "Muestra 4, volumen de resuspensión. ", b: true }, "Resuspendimos el liofilizado en 20 µl. ¿Os parece adecuado o preferís otro volumen?"]));
children.push(BUL([{ t: "Muestra 2, identidad del pDNA encapsulado, ", b: true }, "para asegurar que la lectura es comparable con la del resto de muestras, donde usamos nuestro stock propio."]));
children.push(BUL([{ t: "Muestra 1, tiempo de complejación. ", b: true }, "El correo no lo especifica para esta muestra. ¿También 20 minutos?"]));

// ================= DOCUMENTO =================
const doc = new Document({
  creator: "María Zubieta Laseca",
  title: "Muestras UCM julio 2026 — informe de tratamiento",
  description: "Condiciones ensayadas con las muestras UCM en el ensayo del 03/08/2026",
  numbering: { config: [{
    reference: "vinetas",
    levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
               style: { paragraph: { indent: { left: 400, hanging: 220 } } } }],
  }]},
  styles: { default: { document: { run: { font: "Calibri", size: 20 } } } },
  sections: [{
    properties: {
      page: {
        margin: { top: 1000, right: 1080, bottom: 1000, left: 1080 },
      },
    },
    footers: { default: new Footer({ children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      border: { top: { style: BorderStyle.SINGLE, size: 2, color: "BFBFBF", space: 5 } },
      children: [
        new TextRun({ text: "Muestras UCM julio 2026 · ensayo 03/08/2026 · pág. ", size: 16, color: "808080", font: "Calibri" }),
        new TextRun({ children: [PageNumber.CURRENT], size: 16, color: "808080", font: "Calibri" }),
        new TextRun({ text: " de ", size: 16, color: "808080", font: "Calibri" }),
        new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: "808080", font: "Calibri" }),
      ],
    })]})},
    children,
  }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync("Informe_muestras_UCM_ensayo_03-08-2026.docx", b);
  console.log("OK", b.length, "bytes");
});
