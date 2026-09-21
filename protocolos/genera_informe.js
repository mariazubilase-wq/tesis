const {
  Document, Packer, Paragraph, TextRun, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, LevelFormat,
} = require('docx');
const fs = require('fs');

const W = 9070;   // A4 con márgenes de 2,5 cm

const P = (text, o = {}) => new Paragraph({
  spacing: { before: o.before ?? 0, after: o.after ?? 160, line: 276 },
  children: [new TextRun({ text, bold: o.bold, size: o.size ?? 22, font: "Calibri" })],
});

const RICH = (runs, o = {}) => new Paragraph({
  spacing: { before: o.before ?? 0, after: o.after ?? 160, line: 276 },
  children: runs.map(r => typeof r === 'string'
    ? new TextRun({ text: r, size: 22, font: "Calibri" })
    : new TextRun({ text: r.t, bold: r.b, size: 22, font: "Calibri" })),
});

const H = (text, o = {}) => new Paragraph({
  spacing: { before: o.before ?? 320, after: 140 },
  children: [new TextRun({ text, bold: true, size: 22, font: "Calibri" })],
});

function cell(text, { widths, i, bold, fill, align, size } = {}) {
  return new TableCell({
    width: { size: widths[i], type: WidthType.DXA },
    shading: fill ? { type: ShadingType.CLEAR, fill, color: "auto" } : undefined,
    margins: { top: 50, bottom: 50, left: 80, right: 80 },
    children: [new Paragraph({
      alignment: align ?? AlignmentType.LEFT,
      spacing: { after: 0, line: 240 },
      children: [new TextRun({ text: String(text), bold, size: size ?? 18, font: "Calibri" })],
    })],
  });
}

function table(headers, rows, widths, aligns, size) {
  const al = aligns || headers.map((_, i) => i === 0 ? AlignmentType.LEFT : AlignmentType.CENTER);
  const b = { style: BorderStyle.SINGLE, size: 4, color: "000000" };
  return new Table({
    width: { size: W, type: WidthType.DXA },
    columnWidths: widths,
    borders: { top: b, bottom: b, left: b, right: b, insideHorizontal: b, insideVertical: b },
    rows: [
      new TableRow({
        tableHeader: true,
        children: headers.map((h, i) => cell(h, { widths, i, bold: true, fill: "D9D9D9", align: AlignmentType.CENTER, size })),
      }),
      ...rows.map(r => new TableRow({
        children: r.map((c, i) => cell(c, { widths, i, align: al[i], size })),
      })),
    ],
  });
}

const SPACER = (h = 160) => new Paragraph({ spacing: { after: h }, children: [] });

const ANCHO8 = [1500, 1450, 950, 1120, 1000, 900, 1100, 1050];

const children = [];

// ---------- encabezado ----------
children.push(new Paragraph({
  spacing: { after: 60 },
  children: [new TextRun({ text: "TRATAMIENTO DE LAS MUESTRAS DEL UCM: CANTIDADES Y RATIOS EMPLEADOS", bold: true, size: 26, font: "Calibri" })],
}));
children.push(P("María Zubieta Laseca. Pruebas del 3 de agosto de 2026.", { after: 260 }));

children.push(P("Este documento completa el informe que os mandé el 6 de agosto. Allí os contaba qué había hecho con cada muestra y cómo habían quedado las células, pero no detallaba las cantidades. Aquí van las diluciones, lo que acaba recibiendo cada pocillo y los ratios de cada condición, por si queréis revisar los cálculos."));
children.push(P("He partido de las concentraciones que nos disteis en el correo del 13 de julio, con la corrección de Marta del día 15 (DOTAP al 1 % en las muestras 2 y 3, no al 4 %)."));

// ---------- condiciones generales ----------
children.push(H("CONDICIONES GENERALES"));
children.push(P("Todas las pruebas se hicieron en una placa de 96 pocillos con queratinocitos inmortalizados KerCT, sembrados en torno a 8.000 células por pocillo, y la fluorescencia se evaluó cada 12 h durante 48 h. El volumen final de cada pocillo fue de 100 µl, de los cuales 10 µl son el complejo añadido, es decir el 10 %. Todas las concentraciones que aparecen más abajo están calculadas sobre esos 100 µl."));
children.push(P("El plásmido es el pMAX-GFP, de un stock nuestro a 583 ng/µl. La muestra 2 es la excepción, porque ya lleva el pDNA dentro y no le añadí ninguno."));
children.push(P("En las muestras 1, 4 y 5 diluí por un lado la muestra y por otro el pDNA en DMEM sin FBS a volúmenes iguales, los mezclé y los dejé acomplejarse 20 minutos con balanceo suave a temperatura ambiente. Después añadí 10 µl del complejo a cada pocillo. Las condiciones de las muestras 1 y 5 se hicieron por triplicado."));

children.push(H("LAS MUESTRAS Y EL USO QUE LES HE DADO"));
children.push(table(
  ["Muestra", "Formulación", "Datos empleados en los cálculos", "Uso"],
  [
    ["1", "Microemulsión O/A, DOTAP + DOPE", "Lípido total 37 mg/mL, DOTAP 3,4 mg/mL, ζ +38 mV, 32 nm", "12 condiciones"],
    ["2", "Microemulsión A/O con pDNA encapsulado", "pDNA 10 µg/mL, DOTAP 1 % (10 mg/mL), unos 20 nm", "2 condiciones"],
    ["3", "Microemulsión A/O sin pDNA", "DOTAP 1 %, igual que la muestra 2", "No ensayada"],
    ["4", "Liposomas DOTAP + DOPE liofilizados, trehalosa 10 %", "100 µg de liposomas con 10 µg de DOTAP, unos 150 nm", "1 condición"],
    ["5", "Liposomas DOTAP + DOPE sin liofilizar, trehalosa 10 %", "Liposomas 10 mg/mL, DOTAP 1 mg/mL", "6 condiciones"],
  ],
  [800, 2450, 3820, 2000],
  [AlignmentType.CENTER, AlignmentType.LEFT, AlignmentType.LEFT, AlignmentType.LEFT]
));

// ---------- muestra 1 ----------
children.push(H("MUESTRA 1: microemulsión de fase externa acuosa (O/A)"));
children.push(P("El DOTAP son 3,4 mg/mL de los 37 mg/mL de lípido total, así que la relación entre microemulsión y DOTAP es de 10,9:1 en todas las condiciones. Probé seis cantidades de microemulsión con dos de pDNA, doce condiciones en total."));
children.push(table(
  ["Condición (por pocillo)", "Pipeteo ME+DMEM / pDNA+DMEM (µl)", "ME (µg)", "[ME] (µg/mL)", "DOTAP (µg)", "pDNA (µg)", "ME:pDNA", "DOTAP:pDNA"],
  [
    ["9,25 µg ME + 0,3 µg",  "1+19 / 2+18",  "9,25",  "92,5",  "0,85", "0,3", "30,8:1",  "2,8:1"],
    ["18,5 µg ME + 0,3 µg",  "2+18 / 2+18",  "18,5",  "185",   "1,70", "0,3", "61,7:1",  "5,7:1"],
    ["27,75 µg ME + 0,3 µg", "3+17 / 2+18",  "27,75", "277,5", "2,55", "0,3", "92,5:1",  "8,5:1"],
    ["55,5 µg ME + 0,3 µg",  "6+14 / 2+18",  "55,5",  "555",   "5,10", "0,3", "185:1",   "17:1"],
    ["74 µg ME + 0,3 µg",    "8+12 / 2+18",  "74",    "740",   "6,80", "0,3", "246,7:1", "22,7:1"],
    ["92,5 µg ME + 0,3 µg",  "10+10 / 2+18", "92,5",  "925",   "8,50", "0,3", "308,3:1", "28,3:1"],
    ["9,25 µg ME + 0,6 µg",  "1+19 / 4+16",  "9,25",  "92,5",  "0,85", "0,6", "15,4:1",  "1,4:1"],
    ["18,5 µg ME + 0,6 µg",  "2+18 / 4+16",  "18,5",  "185",   "1,70", "0,6", "30,8:1",  "2,8:1"],
    ["27,75 µg ME + 0,6 µg", "3+17 / 4+16",  "27,75", "277,5", "2,55", "0,6", "46,3:1",  "4,3:1"],
    ["55,5 µg ME + 0,6 µg",  "6+14 / 4+16",  "55,5",  "555",   "5,10", "0,6", "92,5:1",  "8,5:1"],
    ["74 µg ME + 0,6 µg",    "8+12 / 4+16",  "74",    "740",   "6,80", "0,6", "123,3:1", "11,3:1"],
    ["92,5 µg ME + 0,6 µg",  "10+10 / 4+16", "92,5",  "925",   "8,50", "0,6", "154,2:1", "14,2:1"],
  ],
  ANCHO8
));
children.push(SPACER(140));
children.push(RICH([{ t: "RESULTADO: ", b: true }, "hubo muerte celular en las doce condiciones (36 pocillos) durante las primeras 12 h, y a las 48 h no había expresión de GFP en ninguna. Tal como la probé, la muestra resultó tóxica independientemente del ratio."]));
children.push(P("Sobre los ratios que vosotras habíais caracterizado en gel, la serie de 0,3 µg de pDNA los cubre casi todos. Los 55,5 µg de microemulsión dan exactamente vuestro 17:1, y los 92,5 µg dan 28,3:1, muy cerca de vuestro 27:1. El 7:1 queda entre los 18,5 µg (5,7:1) y los 27,75 µg (8,5:1). La serie de 0,6 µg de pDNA baja por debajo de ese rango, de 1,4:1 a 14,2:1."));

// ---------- muestra 2 ----------
children.push(H("MUESTRA 2: microemulsión de fase externa oleosa (A/O) con pDNA encapsulado"));
children.push(P("En el vial solo había unos 100 µl, no el mililitro que indicabais en el correo, y además gasté una parte en ver cómo se mezclaba la microemulsión con el medio. Por eso solo pude hacer dos condiciones, y ninguna de ellas la de 100 µl + 100 µl que habíais probado vosotras."));
children.push(P("En los dos casos mezclé en un eppendorf la microemulsión y el medio que tocaban, dando toques con los dedos para homogeneizar. Después retiré el medio de los pocillos y lo sustituí por esa mezcla. Antes de nada comprobé que la microemulsión no se quedaba flotando por lo oleosa que es."));
children.push(table(
  ["Condición", "ME (µl)", "Medio (µl)", "Vol. final (µl)", "ME (% v/v)", "pDNA (µg)", "DOTAP (µg)"],
  [
    ["50 + 50", "50", "50", "100", "50 %", "0,50", "500"],
    ["25 + 75", "25", "75", "100", "25 %", "0,25", "250"],
  ],
  [1350, 1100, 1200, 1300, 1250, 1400, 1470], null, 20
));
children.push(SPACER(140));
children.push(RICH([{ t: "RESULTADO: ", b: true }, "también hubo mucha muerte celular a partir de las primeras 12 h, y en las 48 h que estuve mirando no encontré ninguna célula verde."]));
children.push(P("Una cosa que llama la atención es el DOTAP que entra en cada pocillo con esta muestra, entre 250 y 500 µg, dos órdenes de magnitud por encima de la muestra 1, que va de 0,85 a 8,5 µg. Es consecuencia directa del ratio 1000:1 de la formulación, pero condiciona bastante la lectura de la toxicidad."));

// ---------- muestra 3 ----------
children.push(H("MUESTRA 3: microemulsión A/O sin pDNA"));
children.push(P("No la probé. Al ser de composición parecida a la muestra 2, preferí ver primero qué tal iba aquella. La tengo entera."));

// ---------- muestra 4 ----------
children.push(H("MUESTRA 4: liposomas liofilizados"));
children.push(P("El liofilizado son 100 µg de liposomas con 10 µg de DOTAP. Lo rehidraté directamente con la disolución de pDNA, como nos indicabais. Empecé con 10 µl, pero no se disolvía bien, así que acabé llevándolo a 20 µl, con 1 µg de pDNA en total. De ahí cogí 2 µl para cada pocillo, que es la décima parte del liofilizado, y lo hice por triplicado."));
children.push(table(
  ["Condición (por pocillo)", "Resuspensión / alícuota", "Liposomas (µg)", "[ME] (µg/mL)", "DOTAP (µg)", "pDNA (µg)", "ME:pDNA", "DOTAP:pDNA"],
  [
    ["10 µg ME + 0,1 µg", "20 µl / 2 µl", "10", "100", "1,0", "0,1", "100:1", "10:1"],
  ],
  ANCHO8
));
children.push(SPACER(140));
children.push(RICH([{ t: "RESULTADO: ", b: true }, "tampoco hubo expresión de GFP, pero las células se veían mejor que con las microemulsiones. A las 12 h se apreciaban los liposomas todavía sin internalizar y a las 48 h la diferencia era clara."]));
children.push(P("Esta condición es exactamente la misma que la primera de la muestra 5, 10 µg de liposomas con 0,1 µg de pDNA a 10:1, así que lo único que cambia entre las dos es la liofilización. Os dejo apuntado que a 10 µl el liofilizado no acababa de redisolverse y a 20 µl sí, por si os sirve para las próximas tandas."));

// ---------- muestra 5 ----------
children.push(H("MUESTRA 5: liposomas sin liofilizar"));
children.push(P("Aquí probé dos cantidades de liposomas con tres de pDNA, seis condiciones por triplicado."));
children.push(table(
  ["Condición (por pocillo)", "Pipeteo lip.+DMEM / pDNA+DMEM (µl)", "Liposomas (µg)", "[ME] (µg/mL)", "DOTAP (µg)", "pDNA (µg)", "ME:pDNA", "DOTAP:pDNA"],
  [
    ["10 µg ME + 0,1 µg", "4+16 / 0,7+19,3", "10", "100", "1,0", "0,1", "100:1", "10:1"],
    ["10 µg ME + 0,2 µg", "4+16 / 1,4+18,6", "10", "100", "1,0", "0,2", "50:1",  "5:1"],
    ["10 µg ME + 0,4 µg", "4+16 / 2,7+17,3", "10", "100", "1,0", "0,4", "25:1",  "2,5:1"],
    ["20 µg ME + 0,1 µg", "8+12 / 0,7+19,3", "20", "200", "2,0", "0,1", "200:1", "20:1"],
    ["20 µg ME + 0,2 µg", "8+12 / 1,4+18,6", "20", "200", "2,0", "0,2", "100:1", "10:1"],
    ["20 µg ME + 0,4 µg", "8+12 / 2,7+17,3", "20", "200", "2,0", "0,4", "50:1",  "5:1"],
  ],
  ANCHO8
));
children.push(SPACER(140));
children.push(RICH([{ t: "RESULTADO: ", b: true }, "de nuevo no hubo nada de expresión de GFP. Las células, en cambio, se mantuvieron sanas y apenas hubo muerte celular. Otra vez parecía que los liposomas se iban internalizando con el tiempo, y fue igual en todas las condiciones."]));

// ---------- control ----------
children.push(H("CONTROL POSITIVO"));
children.push(P("Puse ViaFect: 2,4 µl con 0,7 µl de pDNA, unos 408 ng, y 37 µl de DMEM sin FBS, 10 minutos y 10 µl a cada pocillo. A cada pocillo le llegaron unos 0,6 µl de ViaFect y 0,1 µg de pDNA, la misma cantidad de pDNA que las condiciones más bajas de las muestras 4 y 5. No es un control muy bueno, pero sirvió para ver cómo se veía la fluorescencia."));

const doc = new Document({
  creator: "María Zubieta Laseca",
  title: "Tratamiento de las muestras del UCM",
  styles: { default: { document: { run: { font: "Calibri", size: 22 } } } },
  sections: [{
    properties: { page: { margin: { top: 1417, right: 1417, bottom: 1417, left: 1417 } } },
    children,
  }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync("Tratamiento_muestras_UCM.docx", b);
  console.log("OK", b.length, "bytes");
});
