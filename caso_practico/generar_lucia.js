// Genera el caso práctico simulado (Orden EDU/1603/2009, Castilla y León)
// caso sencillo inventado (Lucía, 1º ESO, TEA).
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
const ALUMNA = 'Lucía Gómez Prieto (alumna ficticia)';
const CENTRO = 'IES «Ejemplo» (centro ficticio)';
const datosAlumna = [
  [null, 'DEL ALUMNO/A:'],
  ['Nombre y apellidos', ALUMNA],
  ['F. nacimiento / Edad', '02/05/2013  —  12 años'],
  ['Nº hermanos / Lugar que ocupa', '1  —  2º lugar'],
  ['Padre / tutor legal', 'Andrés Gómez'],
  ['Madre / tutora legal', 'Elena Prieto'],
  ['Domicilio / Localidad', 'C/ Ejemplo, 5  —  Valladolid'],
  ['Etapa educativa / Curso', 'ESO  —  1º'],
];
const datosCentro = [
  ['Nombre del centro', CENTRO],
  ['Localidad', 'Valladolid'],
  ['Tutor/a', 'Tutor de 1º A (profesor de Matemáticas)'],
];
const doc = [];

// ---------- PORTADA ----------
doc.push(
  p('', { before: 1400 }),
  p('EL CASO DE LUCÍA', { bold: true, size: 40, align: AlignmentType.CENTER }),
  p('Ejemplo ficticio y sencillo de los documentos de la Orden EDU/1603/2009 (Castilla y León)', { size: 24, align: AlignmentType.CENTER, before: 200 }),
  p('', { before: 500 }),
  box('¿Quién es Lucía?', [
    'Lucía tiene 12 años y acaba de empezar 1º de ESO. En Primaria sacaba buenas notas; era «muy suya», le apasiona la astronomía y tenía una sola amiga.',
    'En el instituto todo cambia: un profesor distinto cada hora, cambios de aula, trabajos en grupo y un recreo enorme. Lucía pasa los recreos sola, se bloquea cuando cambian un examen de fecha, interpreta literalmente lo que le dicen y ha tenido dos crisis de llanto en clase.',
    'El tutor pide ayuda al Departamento de Orientación.',
  ]),
  p('', { before: 200 }),
  box('El recorrido de Lucía por los documentos', [
    '1. Anexo I: el tutor la DERIVA al Departamento de Orientación.',
    '2. Anexo II: sus padres firman la AUTORIZACIÓN.',
    '3. Anexo III: la orientadora hace la EVALUACIÓN (observación, entrevistas, cuestionarios y pruebas) y el INFORME. Identifica necesidades compatibles con un TEA; la familia aporta después el diagnóstico clínico de Salud Mental Infanto-Juvenil.',
    '4. Anexo IV: DICTAMEN → centro ordinario, con apoyo de PT y AL y medidas organizativas. Sin adaptación curricular.',
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
  ...datosAlumna.slice(1),
  ['Repetición/es', `${SI} NO   ${NO} SÍ`],
  ['Incidencias escolares significativas', 'Dos crisis de llanto en clase por cambios imprevistos (cambio de aula y de fecha de examen). Pasa los recreos sola.'],
  ['Entorno familiar', 'Familia colaboradora. Cuentan que en casa también le cuestan mucho los cambios de planes.'],
  ['Informes previos', `${SI} NO   ${NO} SÍ`],
], 3400));
doc.push(sec('2.- DATOS DE IDENTIFICACIÓN DEL CENTRO'));
doc.push(kv(datosCentro, 3400));
doc.push(sec('3.- ASPECTOS A CONSIDERAR (solo en los que sobresale o tiene dificultad)'));
doc.push(table([6638, 1500, 1500], [
  [{ c: 'ASPECTOS', w: 6638, bold: true, fill: GRIS }, { c: 'SOBRESALE', w: 1500, bold: true, fill: GRIS }, { c: 'DIFICULTAD', w: 1500, bold: true, fill: GRIS }],
  ...[
    ['Memoria', 1, 0], ['Comprensión lectora (textos informativos)', 1, 0], ['Cálculo', 1, 0],
    ['Control del plan de trabajo / organización', 0, 1], ['Comportamiento en el aula (bloqueos ante cambios)', 0, 1],
    ['Relación con los compañeros', 0, 1], ['Integración en el grupo', 0, 1], ['Autoestima – autoconcepto', 0, 1],
    ['Otros: comprensión de bromas, ironías y dobles sentidos', 0, 1],
  ].map(([a, s, d]) => [{ c: a, w: 6638 }, { c: s ? SI : NO, w: 1500 }, { c: d ? SI : NO, w: 1500 }]),
]));
doc.push(sec('4.- ACTUACIONES REALIZADAS'));
doc.push(kv([
  [`${SI} Cambio metodológico`, 'Avisar con antelación de los cambios; escribir las tareas en la pizarra; dejarle elegir pareja en los trabajos.'],
  [`${SI} Acción tutorial`, 'Entrevistas con Lucía y con su familia; compañera-guía en el recreo.'],
], 3400));
doc.push(sec('5.- VALORACIÓN DE ESTAS MEDIDAS'));
doc.push(box('Valoración', 'Anticipar los cambios le ayuda, pero sigue aislada en el recreo, con ansiedad y con dificultades para trabajar en grupo y entender lo que no se le dice de forma literal.'));
doc.push(sec('6.- INTERVENCIÓN QUE SE SOLICITA'));
doc.push(box('Intervención', 'Evaluación psicopedagógica para conocer sus necesidades en comunicación, relación social y regulación emocional, y orientar al equipo docente.'));
doc.push(firma('En Valladolid, a 15 de octubre de 2025.      Sello del centro  ·  Director/a  ·  Tutor'));
doc.push(br());

// ---------- ANEXO II ----------
doc.push(...titulo('ANEXO II', 'AUTORIZACIÓN DE LOS PADRES O TUTORES LEGALES PARA LA REALIZACIÓN DE LA EVALUACIÓN PSICOPEDAGÓGICA'));
doc.push(kv([
  ['Don', 'Andrés Gómez'], ['Doña', 'Elena Prieto'],
  ['Como padre/madre de la alumna', ALUMNA],
  ['Dirección / Población', 'C/ Ejemplo, 5  —  Valladolid'],
]));
doc.push(p(''));
doc.push(p('AUTORIZAMOS a que nuestra hija sea derivada al:', { bold: true, size: 22 }));
doc.push(p(`${NO} Equipo de Orientación Educativa de: —`));
doc.push(p(`${SI} Departamento de Orientación de: ${CENTRO}`));
doc.push(p('para realizarle las valoraciones que se consideren adecuadas y determinar, en su caso, sus necesidades específicas de apoyo educativo y la respuesta más adecuada.'));
doc.push(firma('En Valladolid, a 17 de octubre de 2025.      Firma del padre  ·  Firma de la madre'));
doc.push(br());

// ---------- ANEXO III ----------
doc.push(...titulo('ANEXO III', 'INFORME PSICOPEDAGÓGICO'));
doc.push(kv([['Fecha de realización del informe', '05 / 12 / 2025']]));
doc.push(sec('DATOS DE IDENTIFICACIÓN DEL ALUMNO'));
doc.push(kv(datosAlumna));
doc.push(sec('1.- DATOS DEL EOE / DEPARTAMENTO DE ORIENTACIÓN'));
doc.push(kv([
  [`${SI} Departamento de Orientación de`, CENTRO],
  ['Profesionales que han participado', 'Orientadora del centro; profesora de Audición y Lenguaje (valoración de la comunicación)'],
], 3400));
doc.push(sec('2.- DATOS DEL CENTRO'));
doc.push(kv(datosCentro));
doc.push(sec('3.- MOTIVOS DE LA EVALUACIÓN'));
doc.push(kv([
  ['Solicitado por', 'El tutor (Anexo I)'],
  ['Situación tipo', `${SI} Otras: dificultades de adaptación, relación social y regulación emocional al empezar la ESO`],
], 3400));
doc.push(sec('4.- INFORMACIÓN PREVIA DISPONIBLE'));
doc.push(kv([[`${SI} Informe médico`, 'Durante la evaluación, la orientadora recomienda a la familia consultar con el pediatra. Informe de Salud Mental Infanto-Juvenil (25/11/2025): Trastorno del Espectro Autista, grado 1 (necesita apoyo), sin discapacidad intelectual.']], 3400));
doc.push(sec('5.- TÉCNICAS Y PRUEBAS UTILIZADAS'));
doc.push(kv([
  [`${SI} Análisis documental`, 'Expediente de Primaria; documento de derivación.'],
  [`${SI} Observación`, 'En clase, en un trabajo en grupo y en el recreo (3 días).'],
  [`${SI} Entrevistas`, 'Con Lucía, con sus padres, con el tutor y con la tutora de 6º de Primaria.'],
  [`${SI} Pruebas estándar`, 'Prueba de inteligencia (rango medio-alto); cuestionarios de cribado de TEA para familia y profesorado (puntuación significativa); valoración del uso social del lenguaje (pragmática) por la profesora de AL; cuestionario de ansiedad.'],
], 3400));
doc.push(sec('6.- HISTORIA PERSONAL DEL ALUMNO'));
doc.push(kv([
  ['Historia escolar', 'Infantil y Primaria en el mismo colegio, sin medidas de apoyo ni repeticiones. Notas altas. En Primaria la describen como «tímida y muy suya».'],
  ['Salud', 'Diagnóstico clínico de TEA grado 1. Hipersensibilidad al ruido (le molestan el timbre y el comedor).'],
  ['Capacidades', 'Capacidad intelectual medio-alta, con muy buena memoria. Lenguaje formal correcto y vocabulario rico, pero interpreta de forma literal, le cuesta entender ironías y mantener una conversación que no sea sobre sus temas de interés.'],
  ['Adaptación y relación social', 'Quiere tener amigas pero no sabe cómo acercarse; pasa los recreos sola. Le cuesta interpretar gestos y emociones de los demás. Alta ansiedad ante los cambios y la incertidumbre; baja autoestima («soy rara»).'],
  ['Nivel de competencia curricular', 'El de 1º de ESO en todas las materias. Destaca en Matemáticas y Biología y Geología.'],
  ['Estilo de aprendizaje', 'Motivación ALTA en sus temas de interés; aceptación de normas ALTA; resistencia a la frustración BAJA; prefiere trabajar SOLA; aprende mejor por vía VISUAL; necesita rutinas y anticipación.'],
], 3400));
doc.push(sec('7.- CONTEXTO EDUCATIVO'));
doc.push(kv([
  ['Relación profesor / compañeros', `Profesorado: ${SI} ADECUADAS   ·   Compañeros: ${SI} INADECUADAS (aislamiento, alguna burla)`],
  ['Características del aula y del grupo', '26 alumnos; grupo hablador; clima aceptable.'],
  ['Recursos del centro', 'Orientadora, profesorado de PT y de AL, programa de alumnado ayudante.'],
], 3400));
doc.push(sec('8.- CONTEXTO FAMILIAR'));
doc.push(box('Contexto familiar', 'Padres y un hermano mayor (16 años). Familia muy implicada y preocupada por su felicidad más que por las notas. Colaboran con el centro.'));
doc.push(sec('9.- CONTEXTO SOCIAL'));
doc.push(box('Contexto social', 'Acude al planetario y a un taller de astronomía los sábados. Existe una asociación de familias de personas con autismo en la provincia.'));
doc.push(sec('10.- CATEGORIZACIÓN (ATDI)'));
doc.push(kv([['Grupo principal', 'ACNEE'], ['Tipología', 'Trastornos del espectro autista (TEA)*'], ['Categoría', 'TEA grado 1, sin discapacidad intelectual*']], 3400));
doc.push(p('* Comprobad el nombre exacto de la tipología y la categoría en la clasificación ATDI vigente.', { italics: true, size: 16 }));
doc.push(sec('11.- NECESIDADES ESPECÍFICAS DE APOYO EDUCATIVO'));
doc.push(kv([
  ['Relación interpersonal y adaptación social', `${SI} Habilidades sociales   ${SI} Trabajo en grupo   ${SI} Habilidades de comunicación`],
  ['Equilibrio afectivo-emocional', `${SI} Estabilidad emocional (ansiedad ante cambios)   ${SI} Autoconcepto y autoestima   ${SI} Empatía (comprender emociones ajenas)`],
  ['Comunicativo-lingüísticas', `${SI} Uso social del lenguaje (pragmática): lenguaje no literal, conversación`],
  ['Aspectos cognitivos', `${SI} Trabajo reflexivo y autodirigido (organización y planificación)`],
  ['Curriculares', 'No presenta desfase. No necesita adaptación de contenidos.'],
], 3400));
doc.push(sec('12.- ORIENTACIONES PARA LA PROPUESTA CURRICULAR'));
doc.push(kv([
  ['Medidas', 'Medidas ordinarias y organizativas. No necesita adaptación curricular significativa.'],
  ['Modalidad recomendada', 'Centro ordinario.'],
  ['Programas específicos', 'Habilidades sociales y comunicación (PT y AL); gestión de la ansiedad y las emociones (orientadora).'],
  ['Organización y acceso', 'Anticipar siempre los cambios (horario visual, avisos por escrito); un «lugar tranquilo» al que pueda ir si se agobia; recreos con actividades estructuradas (club de ajedrez o de la biblioteca); sentarla lejos de la puerta y del ruido.'],
  ['Metodología', 'Instrucciones claras, literales y por escrito; evitar ironías en las instrucciones; trabajos en pareja o en grupos pequeños con roles definidos; aprovechar sus intereses (astronomía) para motivarla; exámenes con preguntas sin dobles sentidos.'],
  ['Recursos', 'PT: 1 sesión semanal; AL: 1 sesión semanal; seguimiento quincenal de la orientadora. Alumnado ayudante en el recreo.'],
], 3400));
doc.push(sec('13.- ORIENTACIONES A LA FAMILIA'));
doc.push(box('Familia', 'Anticipar en casa los cambios de rutina; usar la agenda para coordinarse con el centro; apoyar sus intereses como vía para relacionarse; contactar con la asociación de familias si lo desean.'));
doc.push(sec('14.- SEGUIMIENTO Y REVISIÓN'));
doc.push(box('Seguimiento', 'Reunión mensual del tutor con la orientadora el primer trimestre, y trimestral después. Revisión del informe al acabar la ESO o si cambia su situación.'));
doc.push(kv([['Información a la familia', `${SI} CONFORMIDAD   ${NO} DISCONFORMIDAD`]], 3400));
doc.push(br());

// ---------- ANEXO IV ----------
doc.push(...titulo('ANEXO IV', 'DICTAMEN DE ESCOLARIZACIÓN'));
doc.push(kv([['Fecha del dictamen', '10 / 12 / 2025']]));
doc.push(sec('DATOS DE IDENTIFICACIÓN DEL ALUMNO'));
doc.push(kv(datosAlumna));
doc.push(sec('1.- PROPUESTA REALIZADA POR'));
doc.push(kv([[`${SI} Departamento de Orientación de`, CENTRO]], 3400));
doc.push(sec('2.- INFORMACIÓN APORTADA POR LA FAMILIA'));
doc.push(kv([[`${SI} Informe médico`, 'Informe de Salud Mental Infanto-Juvenil: TEA grado 1.'], [`${NO} Calificación de discapacidad`, 'No solicitada.']], 3400));
doc.push(sec('4.- MOTIVO DEL DICTAMEN'));
doc.push(p(`${NO} Nueva escolarización   ${NO} Cambio de etapa   ${NO} Cambio de centro   ${NO} Revisión   ${SI} Otros: identificación como ACNEE en 1º de ESO`));
doc.push(sec('5.- SÍNTESIS DE LA EVALUACIÓN'));
doc.push(box('Síntesis', 'Alumna con capacidad medio-alta y buen rendimiento académico. Tiene dificultades en la comunicación social, la flexibilidad ante los cambios y la regulación de la ansiedad, que afectan a su integración y bienestar en el instituto.'));
doc.push(sec('6.- CATEGORIZACIÓN (ATDI)'));
doc.push(kv([['Grupo / Tipología / Categoría', 'ACNEE — Trastornos del espectro autista — TEA grado 1*']], 3400));
doc.push(sec('8.- ORIENTACIONES: AUTONOMÍA, PROGRAMAS Y APOYOS'));
doc.push(kv([
  ['Autonomía en la comunicación', 'Necesidad de ayuda BAJA  —  Ayudas: horario y agenda visual'],
  ['Autonomía en desplazamientos y personal', 'Sin necesidad de ayuda'],
  ['Programas específicos', `${SI} Precisa: habilidades sociales y comunicación; gestión emocional`],
  ['Apoyos especializados', `${SI} Pedagogía Terapéutica (PT)   ${SI} Audición y Lenguaje (AL)   ${NO} Intérprete de Lengua de Signos   ${NO} ATE   ${NO} Fisioterapia   ${NO} Adaptación curricular`],
], 3400));
doc.push(sec('9.- PROPUESTA DE MODALIDAD DE ESCOLARIZACIÓN'));
doc.push(kv([
  ['Etapa / Curso', 'ESO — 1º'],
  [`${SI}`, 'Escolarización en centro ordinario'],
  [`${NO}`, 'Centro ordinario preferente  /  Centro de educación especial  /  Aula sustitutoria  /  Combinada'],
  ['Revisión de la modalidad', 'Al finalizar la ESO o si cambia su situación.'],
], 2400));
doc.push(firma('En Valladolid, a 10 de diciembre de 2025.      Vº Bº del Director/a  ·  Firma de la orientadora  ·  Sello del centro'));
doc.push(br());

// ---------- ANEXO V ----------
doc.push(...titulo('ANEXO V', 'OPINIÓN DE LA FAMILIA RESPECTO A LA PROPUESTA DEL DICTAMEN DE ESCOLARIZACIÓN'));
doc.push(sec('A.- Centros de la zona con recursos'));
doc.push(box('Centros', `${CENTRO} (su centro actual), con profesorado de PT y AL.`));
doc.push(sec('B.- Preferencias de centro de los padres'));
doc.push(kv([['1º Centro', CENTRO]], 2400));
doc.push(sec('C.- Opinión de los padres'));
doc.push(p('Andrés Gómez y Elena Prieto, padre y madre de Lucía, hemos sido informados por el Departamento de Orientación de la evaluación psicopedagógica, de la modalidad de escolarización propuesta y de los servicios educativos de la zona.'));
doc.push(p(`${SI} Estar de acuerdo`, { bold: true, size: 24, before: 160 }));
doc.push(p(`${NO} Estar en desacuerdo`, { size: 22 }));
doc.push(firma('En Valladolid, a 12 de diciembre de 2025.      Firma del padre  ·  Firma de la madre'));

const out = new Document({
  styles: { default: { document: { run: { font: FONT, size: 19 } } } },
  sections: [{
    properties: { page: { margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    headers: { default: new Header({ children: [p('El caso de Lucía — Orden EDU/1603/2009 (Castilla y León) — EJEMPLO FICTICIO, NO ES UN DOCUMENTO OFICIAL', { size: 15, italics: true, color: '666666' })] }) },
    children: doc,
  }],
});
Packer.toBuffer(out).then(b => { fs.writeFileSync(__dirname + '/Caso_Lucia_Orden_EDU_1603_2009.docx', b); console.log('ok'); });
