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
  children: [new TextRun({ text: "Tratamiento detallado de cada muestra · ensayo del 3 de agosto de 2026 · María Zubieta Laseca, Universidad de Salamanca", size: 21, color: "595959", font: "Calibri" })],
}));

children.push(P("Este documento desarrolla el apartado de tratamiento del informe que os enviamos el 6 de agosto: dosis y concentración por pocillo y ratios ME:pDNA, ME:DOTAP y DOTAP:pDNA de cada condición ensayada. Los resultados se resumen en una línea al final de cada muestra; el registro fotográfico está en aquel informe."));
children.push(P("Las concentraciones de partida son las de vuestro correo del 13 de julio, con la corrección del 15 de julio (DOTAP al 1 % en las muestras 2 y 3)."));
children.push(SPACER(60));
children.push(NOTA("Verificación:", "las concentraciones deducidas de nuestras anotaciones de pipeteo coinciden con las vuestras (37 mg/mL de lípido total en la muestra 1; 10 mg/mL de liposomas en la muestra 5), y el DOTAP al 1 % de la muestra 2 reproduce exactamente vuestro ratio 1000:1."));

// ---- 1. CONDICIONES GENERALES ----
children.push(H1("1. Condiciones generales del ensayo"));
children.push(BUL([{ t: "Células. ", b: true }, "Queratinocitos inmortalizados KerCT, placa de 96 pocillos, unas 8.000 células por pocillo."]));
children.push(BUL([{ t: "Volumen del pocillo. ", b: true }, "100 µl finales. Los 10 µl de complejo suponen el 10 % de ese volumen. Todas las concentraciones de este documento se calculan sobre esos 100 µl."]));
children.push(BUL([{ t: "Plásmido. ", b: true }, "pMAX-GFP, stock propio a 583 ng/µl. La muestra 2 es la excepción: ya incorpora pDNA y no se le añadió ninguno."]));
children.push(BUL([{ t: "Complejación (muestras 1, 4 y 5). ", b: true }, "Muestra y pDNA diluidos por separado en DMEM sin FBS a volúmenes iguales, mezclados y acomplejados 20 minutos con balanceo suave a temperatura ambiente. Después, 10 µl de complejo por pocillo."]));
children.push(BUL([{ t: "Réplicas. ", b: true }, "Condiciones por triplicado en las muestras 1 y 5. Cada mezcla de 40 µl se repartió en alícuotas de 10 µl."]));
children.push(BUL([{ t: "Lectura. ", b: true }, "Fluorescencia de toda la placa cada 12 h durante 48 h."]));
children.push(SPACER(60));
children.push(RICH([{ t: "Qué significa «ME» en cada tabla. ", b: true }, "El ratio ME:pDNA se refiere al ", { t: "lípido total", b: true }, " en la muestra 1, a la ", { t: "microemulsión completa", b: true }, " en la muestra 2 y a los ", { t: "liposomas", b: true }, " en las muestras 4 y 5. El ratio ME:DOTAP es constante dentro de cada muestra porque lo fija la formulación."], { size: 19 }));

// ---- 2. LAS MUESTRAS ----
children.push(H1("2. Las muestras y el uso que se les ha dado"));
children.push(table(
  ["Muestra", "Formulación", "Datos empleados en los cálculos", "Uso"],
  [
    ["1", "Microemulsión O/A, DOTAP + DOPE", "Lípido total 37 mg/mL · DOTAP 3,4 mg/mL · ζ +38 mV · 32 nm", "12 condiciones"],
    ["2", "Microemulsión A/O con pDNA encapsulado", "pDNA 10 µg/mL · DOTAP 1 % (10 mg/mL) · ~20 nm", "2 condiciones (ver apartado 4)"],
    ["3", "Microemulsión A/O sin pDNA", "DOTAP 1 %, igual que la muestra 2", "No ensayada"],
    ["4", "Liposomas DOTAP + DOPE liofilizados, trehalosa 10 %", "Liofilizado de 10 µl: 100 µg de liposomas y 10 µg de DOTAP · ~150 nm", "1 condición"],
    ["5", "Liposomas DOTAP + DOPE sin liofilizar, trehalosa 10 %", "Liposomas 10 mg/mL · DOTAP 1 mg/mL", "6 condiciones"],
  ],
  [850, 2600, 4090, 2200],
  [AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.LEFT, AlignmentType.LEFT]
));

// ---- 3. MUESTRA 1 ----
children.push(H1("3. Muestra 1 — Microemulsión O/A · ME:DOTAP 10,9:1"));
children.push(table(
  ["Condición (por pocillo)", "Pipeteo ME+DMEM / pDNA+DMEM (µl)", "ME (µg)", "[ME] (µg/mL)", "DOTAP (µg)", "pDNA (µg)", "ME:pDNA", "ME:DOTAP", "DOTAP:pDNA"],
  [
    ["9,25 µg ME + 0,3 µg",  "1+19 / 2+18",  "9,25",  "92,5",  "0,85", "0,3", "30,8:1",  "10,9:1", "2,8:1"],
    ["18,5 µg ME + 0,3 µg",  "2+18 / 2+18",  "18,5",  "185",   "1,70", "0,3", "61,7:1",  "10,9:1", "5,7:1"],
    ["27,75 µg ME + 0,3 µg", "3+17 / 2+18",  "27,75", "277,5", "2,55", "0,3", "92,5:1",  "10,9:1", "8,5:1"],
    ["55,5 µg ME + 0,3 µg",  "6+14 / 2+18",  "55,5",  "555",   "5,10", "0,3", "185:1",   "10,9:1", "17:1"],
    ["74 µg ME + 0,3 µg",    "8+12 / 2+18",  "74",    "740",   "6,80", "0,3", "246,7:1", "10,9:1", "22,7:1"],
    ["92,5 µg ME + 0,3 µg",  "10+10 / 2+18", "92,5",  "925",   "8,50", "0,3", "308,3:1", "10,9:1", "28,3:1"],
    ["9,25 µg ME + 0,6 µg",  "1+19 / 4+16",  "9,25",  "92,5",  "0,85", "0,6", "15,4:1",  "10,9:1", "1,4:1"],
    ["18,5 µg ME + 0,6 µg",  "2+18 / 4+16",  "18,5",  "185",   "1,70", "0,6", "30,8:1",  "10,9:1", "2,8:1"],
    ["27,75 µg ME + 0,6 µg", "3+17 / 4+16",  "27,75", "277,5", "2,55", "0,6", "46,3:1",  "10,9:1", "4,3:1"],
    ["55,5 µg ME + 0,6 µg",  "6+14 / 4+16",  "55,5",  "555",   "5,10", "0,6", "92,5:1",  "10,9:1", "8,5:1"],
    ["74 µg ME + 0,6 µg",    "8+12 / 4+16",  "74",    "740",   "6,80", "0,6", "123,3:1", "10,9:1", "11,3:1"],
    ["92,5 µg ME + 0,6 µg",  "10+10 / 4+16", "92,5",  "925",   "8,50", "0,6", "154,2:1", "10,9:1", "14,2:1"],
  ],
  [1550, 1450, 900, 1100, 950, 850, 1000, 1000, 940], null, 16
));
children.push(SPACER(80));
children.push(RICH([{ t: "Resultado. ", b: true }, "Muerte celular en las 12 condiciones (36 pocillos) en las primeras 12 h y ausencia de expresión de GFP a 48 h. Tal como se ha probado, la muestra resultó tóxica con independencia del ratio."], { size: 19 }));
children.push(SPACER(60));
children.push(NOTA("Frente a vuestros ratios de referencia:", "la serie de 0,3 µg de pDNA cubre el intervalo que habéis caracterizado en gel — 55,5 µg de ME equivale exactamente a vuestro 17:1 y 92,5 µg a 28,3:1, próximo a vuestro 27:1; vuestro 7:1 cae entre 18,5 µg (5,7:1) y 27,75 µg (8,5:1). La serie de 0,6 µg explora por debajo, de 1,4:1 a 14,2:1."));

// ---- 4. MUESTRA 2 ----
children.push(H1("4. Muestra 2 — Microemulsión A/O con pDNA encapsulado · ME:DOTAP 100:1"));
children.push(RICH([{ t: "Volumen recibido. ", b: true }, "El vial contenía unos 100 µl, no el 1 mL indicado en vuestro correo. Como parte se empleó en comprobar cómo se mezclaba la microemulsión con el medio, solo pudieron ensayarse dos condiciones en lugar de la batería prevista, y no la de 100 µl + 100 µl que habíais probado vosotras."]));
children.push(P("Procedimiento: se mezclaron en un eppendorf la microemulsión y el medio de cada condición, dando toques para homogeneizar; después se retiró el medio de los pocillos y se sustituyó por la mezcla. Se comprobó antes que la microemulsión no quedaba flotando por su carácter oleoso.", { size: 19 }));
children.push(table(
  ["Condición", "ME (µl)", "Medio (µl)", "Vol. final (µl)", "ME (% v/v)", "pDNA (µg)", "DOTAP (µg)", "ME:pDNA", "ME:DOTAP", "DOTAP:pDNA"],
  [
    ["50 + 50", "50", "50", "100", "50 %", "0,50", "500", "100.000:1", "100:1", "1000:1"],
    ["25 + 75", "25", "75", "100", "25 %", "0,25", "250", "100.000:1", "100:1", "1000:1"],
  ],
  [1050, 800, 900, 1050, 950, 900, 950, 1300, 950, 890], null, 16
));
children.push(SPACER(80));
children.push(RICH([{ t: "Resultado. ", b: true }, "Mucha muerte celular a partir de las primeras 12 h y ninguna célula fluorescente en las 48 h evaluadas."], { size: 19 }));
children.push(SPACER(60));
children.push(NOTA("Dos apuntes:", "el ratio ME:pDNA asume densidad ≈ 1 g/mL para la microemulsión; decidnos si preferís otro valor. Y la carga de DOTAP por pocillo (250–500 µg) es dos órdenes de magnitud mayor que en la muestra 1 (0,85–8,5 µg), consecuencia del ratio 1000:1 de la formulación."));

// ---- 5. MUESTRA 3 ----
children.push(H1("5. Muestra 3 — Microemulsión A/O sin pDNA"));
children.push(P("No ensayada: al ser de composición similar a la muestra 2, se prefirió ver primero cómo se comportaba aquella. Se conserva íntegra."));

// ---- 6. MUESTRA 4 ----
children.push(H1("6. Muestra 4 — Liposomas liofilizados · ME:DOTAP 10:1"));
children.push(P("El liofilizado corresponde a 10 µl de liposomas, es decir, 100 µg de liposomas con 10 µg de DOTAP. Se rehidrató directamente con la disolución de pDNA, según vuestro procedimiento."));
children.push(table(
  ["Concepto", "Valor", "Observación"],
  [
    ["Resuspensión del liofilizado", "10 µl de agua + pDNA, 1 µg en total", "Rehidratación directa con el pDNA"],
    ["Liposomas (ME)", "100 µg", "10 µl × 10 mg/mL"],
    ["DOTAP", "10 µg", "10 µl × 1 mg/mL"],
    ["pDNA", "1,00 µg", "—"],
    ["ME:pDNA / ME:DOTAP / DOTAP:pDNA", "100:1 / 10:1 / 10:1", "El 10:1 coincide con el ratio que habéis evaluado"],
    ["Aplicación", "1 µl de la resuspensión en 10 µl de DMEM sin FBS", "Equivale a 1 µg de DOTAP y 0,1 µg de pDNA"],
  ],
  [3100, 3200, 3440],
  [AlignmentType.LEFT, AlignmentType.LEFT, AlignmentType.LEFT]
));
children.push(SPACER(80));
children.push(RICH([{ t: "Resultado. ", b: true }, "Sin expresión de GFP, pero las células se vieron en mejor estado que con las microemulsiones. A las 12 h se apreciaban liposomas aparentemente sin internalizar, con diferencia clara a las 48 h."], { size: 19 }));
children.push(SPACER(60));
children.push(NOTA("Sobre el contenido del liofilizado:", "la descripción dice que cada liofilizado contiene 10 µg de DOTAP y, más abajo, que la cantidad enviada equivale a «10 µg de liposomas liofilizados». Ambas cosas no encajan: siendo el DOTAP el 10 % de los liposomas (1 mg/mL sobre 10 mg/mL), 10 µg de liposomas contendrían 1 µg de DOTAP, y para llegar a 10 µg harían falta 100 µg de liposomas. Hemos partido de que se liofilizaron 10 µl de liposomas —100 µg, con 10 µg de DOTAP—, que es lo que nos indicasteis y lo que hace cuadrar el ratio 10:1. Confirmadnos si no fuera así, porque de ello depende todo el cálculo de esta muestra. Al margen de esto, es posible que 10 µl fuera un volumen de resuspensión demasiado pequeño: al repetir la condición nos interesa saber qué volumen recomendáis."));

// ---- 7. MUESTRA 5 ----
children.push(H1("7. Muestra 5 — Liposomas sin liofilizar · ME:DOTAP 10:1"));
children.push(table(
  ["Condición (por pocillo)", "Pipeteo lip.+DMEM / pDNA+DMEM (µl)", "Liposomas (µg)", "[ME] (µg/mL)", "DOTAP (µg)", "pDNA (µg)", "ME:pDNA", "ME:DOTAP", "DOTAP:pDNA"],
  [
    ["10 µg ME + 0,1 µg", "4+16 / 0,7+19,3", "10", "100", "1,0", "0,1", "100:1", "10:1", "10:1"],
    ["10 µg ME + 0,2 µg", "4+16 / 1,4+18,6", "10", "100", "1,0", "0,2", "50:1",  "10:1", "5:1"],
    ["10 µg ME + 0,4 µg", "4+16 / 2,7+17,3", "10", "100", "1,0", "0,4", "25:1",  "10:1", "2,5:1"],
    ["20 µg ME + 0,1 µg", "8+12 / 0,7+19,3", "20", "200", "2,0", "0,1", "200:1", "10:1", "20:1"],
    ["20 µg ME + 0,2 µg", "8+12 / 1,4+18,6", "20", "200", "2,0", "0,2", "100:1", "10:1", "10:1"],
    ["20 µg ME + 0,4 µg", "8+12 / 2,7+17,3", "20", "200", "2,0", "0,4", "50:1",  "10:1", "5:1"],
  ],
  [1550, 1450, 900, 1100, 950, 850, 1000, 1000, 940], null, 16
));
children.push(SPACER(80));
children.push(RICH([{ t: "Resultado. ", b: true }, "Sin expresión de GFP en ninguna condición, pero las células se mantuvieron sanas y apenas hubo muerte celular. De nuevo se apreció internalización progresiva de los liposomas. El comportamiento fue consistente en todas las condiciones."], { size: 19 }));

// ---- 8. CONTROL ----
children.push(H1("8. Control positivo"));
children.push(P("ViaFect 2,4 µl + 0,7 µl de pDNA (≈ 408 ng) + 37 µl de DMEM sin FBS, 10 minutos, 10 µl por pocillo. Por pocillo: ≈ 0,6 µl de ViaFect y ≈ 0,1 µg de pDNA, la misma dosis de pDNA que las condiciones más bajas de las muestras 4 y 5. Sirvió de referencia visual de la fluorescencia, aunque su eficiencia no fue alta."));

// ---- 9. CONSULTAS ----
children.push(H1("9. Consultas"));
children.push(BUL([{ t: "Muestra 2, volumen disponible. ", b: true }, "¿Podríais enviarnos más cantidad? Con los 100 µl recibidos no se pudo reproducir vuestra condición de 100 µl + 100 µl ni ampliar el número de condiciones."]));
children.push(BUL([{ t: "Muestra 2, pDNA encapsulado. ", b: true }, "Entendemos que es el pMAX-GFP que os enviamos hace unos meses, el mismo que hemos usado en el resto de muestras. ¿Nos lo confirmáis?"]));
children.push(BUL([{ t: "Muestra 4, volumen de resuspensión. ", b: true }, "Resuspendimos el liofilizado en 10 µl, que quizá sea poco. ¿Qué volumen recomendáis?"]));
children.push(BUL([{ t: "Toxicidad de las microemulsiones. ", b: true }, "Las muestras 1 y 2 resultaron tóxicas en todas las condiciones ensayadas, mientras que las formulaciones liposomales no lo fueron. Si consideráis que merece la pena seguir con ellas, podemos ensayar dosis por debajo de los 9,25 µg de ME por pocillo o tiempos de exposición más cortos; decidnos qué preferís."]));
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
