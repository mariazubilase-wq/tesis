// Genera el caso práctico simulado (Orden EDU/1603/2009, Castilla y León)
// caso sencillo inventado (Pablo, 1º ESO).
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  ShadingType, AlignmentType, BorderStyle, PageBreak, Header, Footer,
} = require('docx');

const W = 9638; // ancho útil A4 con márgenes de 2 cm
const GRIS = 'D9D9D9';
const FONT = 'Arial';
const SI = '☒', NO = '☐';

const t = (text, o = {}) => new TextRun({ text, font: FONT, size: o.size || 19, bold: o.bold, italics: o.italics, color: o.color });
const p = (text, o = {}) => new Paragraph({
  alignment: o.align, spacing: { before: o.before ?? 40, after: o.after ?? 40 },
  children: Array.isArray(text) ? text : [t(text, o)],
});

function cell(content, width, o = {}) {
  const paras = (Array.isArray(content) ? content : [content]).map(c =>
    typeof c === 'string' ? p(c, { bold: o.bold, size: o.size, italics: o.italics }) : c);
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    columnSpan: o.span,
    shading: o.fill ? { type: ShadingType.CLEAR, color: 'auto', fill: o.fill } : undefined,
    margins: { top: 40, bottom: 40, left: 90, right: 90 },
    children: paras,
  });
}

// Tabla genérica: rows = array de arrays de {c, w, bold, fill, span}
function table(cols, rows) {
  return new Table({
    width: { size: W, type: WidthType.DXA },
    columnWidths: cols,
    rows: rows.map(r => new TableRow({
      children: r.map(x => cell(x.c, x.w, x)),
    })),
  });
}
const head = (text) => [{ c: text, w: W, bold: true, fill: GRIS, span: undefined }];
// Tabla etiqueta/valor a 2 columnas
function kv(pairs, l = 3000) {
  return table([l, W - l], pairs.map(([a, b]) =>
    a === null ? [{ c: b, w: W, bold: true, fill: GRIS, span: 2 }]
      : [{ c: a, w: l, bold: true }, { c: b, w: W - l }]));
}
// Bloque: título gris + texto
function box(title, body) {
  const rows = [[{ c: title, w: W, bold: true, fill: GRIS }]];
  rows.push([{ c: Array.isArray(body) ? body : [body], w: W }]);
  return table([W], rows);
}
const sec = (text) => p(text, { bold: true, size: 21, before: 220, after: 80 });
const titulo = (a, b, c) => [
  p(a, { bold: true, size: 24, align: AlignmentType.CENTER, before: 120 }),
  p(b, { bold: true, size: 26, align: AlignmentType.CENTER }),
  ...(c ? [p(c, { size: 18, align: AlignmentType.CENTER, italics: true })] : []),
  p(''),
];
const firma = (txt) => p(txt, { italics: true, before: 160 });
const br = () => new Paragraph({ children: [new PageBreak()] });

// ---------- DATOS DEL CASO (todo inventado) ----------
const ALUMNO = 'Pablo Ruiz Sanz (alumno ficticio)';
const CENTRO = 'IES «Ejemplo» (centro ficticio)';
const DO = 'Departamento de Orientación del IES «Ejemplo»';
const datosAlumno = [
  [null, 'DEL ALUMNO/A:'],
  ['Nombre y apellidos', ALUMNO],
  ['F. nacimiento / Edad', '14/03/2013  —  12 años'],
  ['Nº hermanos / Lugar que ocupa', '1  —  1º lugar'],
  ['Padre / tutor legal', 'Javier Ruiz'],
  ['Madre / tutora legal', 'Laura Sanz'],
  ['Domicilio / Localidad', 'C/ Ejemplo, 3  —  Valladolid'],
  ['Etapa educativa / Curso', 'ESO  —  1º'],
];
const datosCentro = [
  ['Nombre del centro', CENTRO],
  ['Localidad', 'Valladolid'],
  ['Tutor/a', 'Tutora de 1º B (profesora de Lengua)'],
];
const doc = [];

// ---------- PORTADA ----------
doc.push(
  p('', { before: 1600 }),
  p('EL CASO DE PABLO', { bold: true, size: 40, align: AlignmentType.CENTER }),
  p('Ejemplo ficticio y sencillo de los documentos de la Orden EDU/1603/2009 (Castilla y León)', { size: 24, align: AlignmentType.CENTER, before: 200 }),
  p('', { before: 500 }),
  box('¿Quién es Pablo?', [
    'Pablo tiene 12 años y acaba de empezar 1º de ESO. En Primaria iba bien, aunque hablaba algo alto y a veces «no se enteraba».',
    'En el instituto hay más profesores, más ruido y más clases expositivas. En octubre la tutora nota que no sigue las explicaciones, pide que le repitan las cosas y está bajando sus notas.',
    'Tras la evaluación, el otorrino confirma una hipoacusia (pérdida auditiva) bilateral moderada y le ponen audífonos.',
  ]),
  p('', { before: 200 }),
  box('El recorrido de Pablo por los documentos', [
    '1. Anexo I: la tutora pide ayuda al Departamento de Orientación (DERIVACIÓN).',
    '2. Anexo II: sus padres firman la AUTORIZACIÓN.',
    '3. Anexo III: la orientadora hace el INFORME PSICOPEDAGÓGICO.',
    '4. Anexo IV: se emite el DICTAMEN → centro ordinario con apoyo de Audición y Lenguaje y equipo FM.',
    '5. Anexo V: la familia está DE ACUERDO.',
  ]),
  p('', { before: 200 }),
  p('Todo es inventado (nombres, centro, fechas y datos). Ejemplo con fines didácticos; no es un documento oficial.', { italics: true, align: AlignmentType.CENTER, size: 18 }),
  br(),
);

// ---------- ANEXO I ----------
doc.push(...titulo('ANEXO I', 'DOCUMENTO DE DERIVACIÓN', '(Solicitud de intervención del profesorado especialista en orientación educativa)'));
doc.push(sec('1.- DATOS PERSONALES DEL ALUMNO/A'));
doc.push(kv([
  ...datosAlumno.slice(1),
  ['Repetición/es', `${SI} NO   ${NO} SÍ`],
  ['Incidencias escolares significativas', 'Ninguna en Primaria. En 1º de ESO no sigue las explicaciones orales y sus notas bajan.'],
  ['Entorno familiar', 'Familia muy implicada. Comenta que en casa pone la tele muy alta.'],
  ['Informes previos', `${SI} NO   ${NO} SÍ`],
], 3400));
doc.push(sec('2.- DATOS DE IDENTIFICACIÓN DEL CENTRO'));
doc.push(kv(datosCentro, 3400));
doc.push(sec('3.- ASPECTOS A CONSIDERAR (solo en los que sobresale o tiene dificultad)'));
doc.push(table([6638, 1500, 1500], [
  [{ c: 'ASPECTOS', w: 6638, bold: true, fill: GRIS }, { c: 'SOBRESALE', w: 1500, bold: true, fill: GRIS }, { c: 'DIFICULTAD', w: 1500, bold: true, fill: GRIS }],
  ...[
    ['Capacidad intelectual', 0, 0], ['Atención – concentración', 0, 1], ['Motivación e interés', 1, 0],
    ['Comprensión lectora', 1, 0], ['Comportamiento en el aula / centro', 1, 0], ['Relación con los compañeros', 0, 1],
    ['Áreas: Inglés (comprensión oral), Geografía e Historia', 0, 1], ['Otros: comprensión de explicaciones orales', 0, 1],
  ].map(([a, s, d]) => [{ c: a, w: 6638 }, { c: s ? SI : NO, w: 1500 }, { c: d ? SI : NO, w: 1500 }]),
]));
doc.push(sec('4.- ACTUACIONES REALIZADAS'));
doc.push(kv([
  [`${SI} Cambio metodológico`, 'Se le sienta en primera fila; se escriben en la pizarra las tareas y fechas de exámenes.'],
  [`${SI} Acción tutorial`, 'Entrevista con Pablo y con su familia (octubre).'],
], 3400));
doc.push(sec('5.- VALORACIÓN DE ESTAS MEDIDAS'));
doc.push(box('Valoración', 'Mejora algo en primera fila, pero sigue perdiendo información cuando hay ruido o el profesor habla de espaldas.'));
doc.push(sec('6.- INTERVENCIÓN QUE SE SOLICITA'));
doc.push(box('Intervención', 'Evaluación psicopedagógica para conocer el origen de sus dificultades y orientar la respuesta educativa. Se sugiere a la familia una revisión auditiva.'));
doc.push(firma('En Valladolid, a 20 de octubre de 2025.      Sello del centro  ·  Director/a  ·  Tutora'));
doc.push(br());

// ---------- ANEXO II ----------
doc.push(...titulo('ANEXO II', 'AUTORIZACIÓN DE LOS PADRES O TUTORES LEGALES PARA LA REALIZACIÓN DE LA EVALUACIÓN PSICOPEDAGÓGICA'));
doc.push(kv([
  ['Don', 'Javier Ruiz'], ['Doña', 'Laura Sanz'],
  ['Como padre/madre del alumno', ALUMNO],
  ['Dirección / Población', 'C/ Ejemplo, 3  —  Valladolid'],
]));
doc.push(p(''));
doc.push(p('AUTORIZAMOS a que nuestro hijo sea derivado al:', { bold: true, size: 22 }));
doc.push(p(`${NO} Equipo de Orientación Educativa de: —`));
doc.push(p(`${SI} Departamento de Orientación de: ${CENTRO}`));
doc.push(p('para realizarle las valoraciones que se consideren adecuadas y determinar, en su caso, sus necesidades específicas de apoyo educativo y la respuesta más adecuada.'));
doc.push(firma('En Valladolid, a 22 de octubre de 2025.      Firma del padre  ·  Firma de la madre'));
doc.push(p('Observaciones: la familia aportará el informe del otorrino (ORL) en cuanto lo tenga.', { italics: true, before: 200 }));
doc.push(br());

// ---------- ANEXO III ----------
doc.push(...titulo('ANEXO III', 'INFORME PSICOPEDAGÓGICO'));
doc.push(kv([['Fecha de realización del informe', '28 / 11 / 2025']]));
doc.push(sec('DATOS DE IDENTIFICACIÓN DEL ALUMNO'));
doc.push(kv(datosAlumno));
doc.push(sec('1.- DATOS DEL EOE / DEPARTAMENTO DE ORIENTACIÓN'));
doc.push(kv([
  [`${SI} Departamento de Orientación de`, CENTRO],
  ['Profesionales que han participado', 'Orientadora del centro; maestra de Audición y Lenguaje'],
], 3400));
doc.push(sec('2.- DATOS DEL CENTRO'));
doc.push(kv(datosCentro));
doc.push(sec('3.- MOTIVOS DE LA EVALUACIÓN'));
doc.push(kv([
  ['Solicitado por', 'La tutora (Anexo I)'],
  ['Situación tipo', `${SI} Otras: dificultades para seguir las explicaciones orales al empezar la ESO`],
], 3400));
doc.push(sec('4.- INFORMACIÓN PREVIA DISPONIBLE'));
doc.push(kv([[`${SI} Informe médico`, 'Informe de Otorrinolaringología (10/11/2025): hipoacusia neurosensorial bilateral moderada. Se adaptan audífonos.']], 3400));
doc.push(sec('5.- TÉCNICAS Y PRUEBAS UTILIZADAS'));
doc.push(kv([
  [`${SI} Análisis documental`, 'Expediente de Primaria e informe médico.'],
  [`${SI} Observación`, 'En el aula (Lengua e Inglés) y en el recreo.'],
  [`${SI} Entrevistas`, 'Con Pablo, con su familia y con la tutora.'],
  [`${SI} Pruebas estándar`, 'Prueba de inteligencia (rango medio); prueba de comprensión lectora (rango medio); valoración del lenguaje oral por la maestra de AL.'],
], 3400));
doc.push(sec('6.- HISTORIA PERSONAL DEL ALUMNO'));
doc.push(kv([
  ['Historia escolar', 'Primaria en el CEIP «Ejemplo» sin medidas de apoyo ni repeticiones. Notas buenas.'],
  ['Salud', 'Hipoacusia bilateral moderada, diagnosticada en noviembre de 2025. Lleva audífonos.'],
  ['Capacidades', 'Capacidad intelectual media. Buena lectura y escritura. Pequeños errores al pronunciar algunos sonidos (s/z) y vocabulario algo limitado en temas académicos.'],
  ['Adaptación y relación social', 'Educado y responsable. Últimamente evita hablar en grupo y está más callado porque «no se entera de las bromas». Le preocupa que vean los audífonos.'],
  ['Nivel de competencia curricular', 'El de 1º de ESO. Sus dificultades vienen de no oír bien, no de no saber.'],
  ['Estilo de aprendizaje', 'Atención media (se cansa por el esfuerzo de escuchar); motivación ALTA; ritmo NORMAL; prefiere trabajar en PAREJA; aprende mejor por vía VISUAL; responde a refuerzos SOCIALES.'],
], 3400));
doc.push(sec('7.- CONTEXTO EDUCATIVO'));
doc.push(kv([
  ['Relación profesor / compañeros', `Profesorado: ${SI} BUENAS   ·   Compañeros: ${SI} ADECUADAS`],
  ['Características del aula y del grupo', 'Aula ruidosa (da a la calle); 27 alumnos; clima bueno.'],
  ['Recursos del centro', 'Orientadora, maestra de AL a tiempo parcial y profesorado de PT.'],
], 3400));
doc.push(sec('8.- CONTEXTO FAMILIAR'));
doc.push(box('Contexto familiar', 'Padres y una hermana pequeña. Familia muy colaboradora, con expectativas altas y realistas. Han acudido a todas las citas.'));
doc.push(sec('9.- CONTEXTO SOCIAL'));
doc.push(box('Contexto social', 'Juega al baloncesto en un club del barrio. La asociación local de personas sordas ofrece orientación a familias.'));
doc.push(sec('10.- CATEGORIZACIÓN (ATDI)'));
doc.push(kv([['Grupo principal', 'ACNEE'], ['Tipología', 'Discapacidad auditiva'], ['Categoría', 'Hipoacusia moderada']], 3400));
doc.push(sec('11.- NECESIDADES ESPECÍFICAS DE APOYO EDUCATIVO'));
doc.push(kv([
  ['Comunicativo-lingüísticas', `${SI} Comprensión oral   ${SI} Expresión oral/articulación (s/z)   ${SI} Vocabulario`],
  ['Afectivo-emocionales', `${SI} Autoconcepto y autoestima (aceptar los audífonos)`],
  ['Relación social', `${SI} Habilidades de comunicación en grupo`],
  ['Curriculares', 'No presenta desfase: sigue el currículo de 1º de ESO sin adaptación de contenidos.'],
], 3400));
doc.push(sec('12.- ORIENTACIONES PARA LA PROPUESTA CURRICULAR'));
doc.push(kv([
  ['Medidas', 'Medidas ordinarias y de acceso. No necesita adaptación curricular significativa.'],
  ['Modalidad recomendada', 'Centro ordinario.'],
  ['Programa específico', 'Lenguaje oral y vocabulario académico con la maestra de AL.'],
  ['Adaptaciones de acceso', 'Equipo FM (micrófono para el profesor conectado a sus audífonos); sentarse en primera fila y lejos de la ventana.'],
  ['Metodología', 'Hablar de frente y sin taparse la boca; apoyar las explicaciones con esquemas, pizarra o vídeos subtitulados; repetir las preguntas de los compañeros; exámenes con instrucciones por escrito.'],
  ['Recursos', 'Maestra de AL: 2 sesiones semanales. Equipo FM (préstamo de la Dirección Provincial).'],
], 3400));
doc.push(sec('13.- ORIENTACIONES A LA FAMILIA'));
doc.push(box('Familia', 'Animar a Pablo a usar siempre los audífonos; revisiones periódicas con el otorrino; hablarle de frente y sin ruido de fondo; contactar con la asociación de personas sordas si lo desean.'));
doc.push(sec('14.- SEGUIMIENTO Y REVISIÓN'));
doc.push(box('Seguimiento', 'Reunión trimestral de la tutora, la AL y la orientadora. Revisión del informe al acabar la ESO o si cambia su audición.'));
doc.push(kv([['Información a la familia', `${SI} CONFORMIDAD   ${NO} DISCONFORMIDAD`]], 3400));
doc.push(br());

// ---------- ANEXO IV ----------
doc.push(...titulo('ANEXO IV', 'DICTAMEN DE ESCOLARIZACIÓN'));
doc.push(kv([['Fecha del dictamen', '03 / 12 / 2025']]));
doc.push(sec('DATOS DE IDENTIFICACIÓN DEL ALUMNO'));
doc.push(kv(datosAlumno));
doc.push(sec('1.- PROPUESTA REALIZADA POR'));
doc.push(kv([[`${SI} Departamento de Orientación de`, CENTRO]], 3400));
doc.push(sec('2.- INFORMACIÓN APORTADA POR LA FAMILIA'));
doc.push(kv([[`${SI} Informe médico`, 'Informe ORL: hipoacusia bilateral moderada.'], [`${NO} Calificación de discapacidad`, 'En trámite.']], 3400));
doc.push(sec('4.- MOTIVO DEL DICTAMEN'));
doc.push(p(`${NO} Nueva escolarización   ${NO} Cambio de etapa   ${NO} Cambio de centro   ${NO} Revisión   ${SI} Otros: identificación como ACNEE en 1º de ESO`));
doc.push(sec('5.- SÍNTESIS DE LA EVALUACIÓN'));
doc.push(box('Síntesis', 'Alumno de capacidad media, con buen nivel curricular, motivado y con apoyo familiar. Su hipoacusia moderada le impide seguir las explicaciones orales en un aula ruidosa, y esto empieza a afectar a su autoestima y a su relación con los compañeros.'));
doc.push(sec('6.- CATEGORIZACIÓN (ATDI)'));
doc.push(kv([['Grupo / Tipología / Categoría', 'ACNEE — Discapacidad auditiva — Hipoacusia moderada']], 3400));
doc.push(sec('8.- ORIENTACIONES: AUTONOMÍA, PROGRAMAS Y APOYOS'));
doc.push(kv([
  ['Autonomía en la comunicación', 'Necesidad de ayuda BAJA  —  Ayuda técnica: equipo FM'],
  ['Autonomía en desplazamientos y personal', 'Sin necesidad de ayuda'],
  ['Programas específicos', `${SI} Precisa: lenguaje oral y vocabulario`],
  ['Apoyos especializados', `${SI} Audición y Lenguaje (AL)   ${NO} PT   ${NO} Intérprete de Lengua de Signos   ${NO} ATE   ${NO} Fisioterapia   ${NO} Adaptación curricular`],
], 3400));
doc.push(sec('9.- PROPUESTA DE MODALIDAD DE ESCOLARIZACIÓN'));
doc.push(kv([
  ['Etapa / Curso', 'ESO — 1º'],
  [`${SI}`, 'Escolarización en centro ordinario'],
  [`${NO}`, 'Centro ordinario preferente  /  Centro de educación especial  /  Aula sustitutoria  /  Combinada'],
  ['Revisión de la modalidad', 'Al finalizar la ESO o si cambia su situación.'],
], 2400));
doc.push(firma('En Valladolid, a 3 de diciembre de 2025.      Vº Bº del Director/a  ·  Firma de la orientadora  ·  Sello del centro'));
doc.push(br());

// ---------- ANEXO V ----------
doc.push(...titulo('ANEXO V', 'OPINIÓN DE LA FAMILIA RESPECTO A LA PROPUESTA DEL DICTAMEN DE ESCOLARIZACIÓN'));
doc.push(sec('A.- Centros de la zona con recursos'));
doc.push(box('Centros', `${CENTRO} (su centro actual), con maestra de AL y equipo FM disponible.`));
doc.push(sec('B.- Preferencias de centro de los padres'));
doc.push(kv([['1º Centro', CENTRO]], 2400));
doc.push(sec('C.- Opinión de los padres'));
doc.push(p('Javier Ruiz y Laura Sanz, padre y madre de Pablo, hemos sido informados por el Departamento de Orientación de la evaluación psicopedagógica, de la modalidad de escolarización propuesta y de los servicios educativos de la zona.'));
doc.push(p(`${SI} Estar de acuerdo`, { bold: true, size: 24, before: 160 }));
doc.push(p(`${NO} Estar en desacuerdo`, { size: 22 }));
doc.push(firma('En Valladolid, a 5 de diciembre de 2025.      Firma del padre  ·  Firma de la madre'));

const out = new Document({
  styles: { default: { document: { run: { font: FONT, size: 19 } } } },
  sections: [{
    properties: { page: { margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    headers: { default: new Header({ children: [p('El caso de Pablo — Orden EDU/1603/2009 (Castilla y León) — EJEMPLO FICTICIO, NO ES UN DOCUMENTO OFICIAL', { size: 15, italics: true, color: '666666' })] }) },
    children: doc,
  }],
});
Packer.toBuffer(out).then(b => { fs.writeFileSync(__dirname + '/Caso_Pablo_Orden_EDU_1603_2009.docx', b); console.log('ok'); });
