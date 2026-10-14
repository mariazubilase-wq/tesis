// Genera el caso práctico simulado (Orden EDU/1603/2009, Castilla y León)
// adaptado del "Informe Tipo DIS-I" (Andalucía).
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

// ---------- DATOS DEL CASO (ficticios) ----------
const ALUMNA = 'A. G. M. (alumna ficticia)';
const CENTRO = 'CEIP «Ejemplo» (centro ficticio)';
const EOE = 'Equipo de Orientación Educativa y Psicopedagógica de Valladolid (ficticio)';
const datosAlumna = [
  [null, 'DEL ALUMNO/A:'],
  ['Nombre y apellidos', ALUMNA],
  ['F. nacimiento / Edad', '25/08/2007  —  8 años'],
  ['Nº hermanos / Lugar que ocupa', '2  —  2º lugar'],
  ['Padre / tutor legal', 'J. G. R.'],
  ['Madre / tutora legal', 'M. M. L.'],
  ['Domicilio / Localidad', 'C/ Ejemplo, 1  —  Valladolid (47000)'],
  ['Etapa educativa / Curso', 'Educación Primaria  —  2º (repite curso)'],
];
const datosCentro = [
  ['Nombre del centro / Código', `${CENTRO}  —  47000000`],
  ['Dirección / Localidad', 'C/ Escuela, s/n  —  Valladolid (47000)'],
  ['Tutor/a', 'Tutora de 2º A'],
];

const doc = [];

// ---------- PORTADA ----------
doc.push(
  p('', { before: 1800 }),
  p('CASO PRÁCTICO SIMULADO', { bold: true, size: 36, align: AlignmentType.CENTER }),
  p('Documentos del proceso de evaluación psicopedagógica y dictamen de escolarización', { size: 24, align: AlignmentType.CENTER, before: 200 }),
  p('ORDEN EDU/1603/2009, de 20 de julio (Castilla y León) — Anexos I a V', { bold: true, size: 22, align: AlignmentType.CENTER, before: 200 }),
  p('', { before: 600 }),
  box('Aviso', [
    'Ejemplo con fines exclusivamente didácticos (asignatura Atención a la Diversidad).',
    'Adaptado del «Informe Tipo DIS-I» (modelo andaluz de valoración psicopedagógica, datos anonimizados) a los modelos de documentos de la Orden EDU/1603/2009 de Castilla y León.',
    'Todos los nombres, centros, direcciones y fechas son ficticios. Los datos marcados con * se han completado para poder rellenar los modelos de Castilla y León.',
  ]),
  p('', { before: 300 }),
  box('Resumen del caso', [
    'Alumna de 8 años que repite 2º de Educación Primaria. Presenta dificultades persistentes en lectoescritura y lenguaje oral pese al refuerzo educativo.',
    'Recorrido: Derivación (Anexo I) → Autorización familiar (Anexo II) → Informe psicopedagógico (Anexo III) → Dictamen de escolarización (Anexo IV) → Opinión de la familia: DE ACUERDO (Anexo V).',
    'Resultado: ACNEE – discapacidad intelectual leve. Escolarización en centro ordinario con apoyo de PT y AL y adaptación curricular significativa en Lengua y Matemáticas.',
  ]),
  br(),
);

// ---------- ANEXO I ----------
doc.push(...titulo('ANEXO I', 'DOCUMENTO DE DERIVACIÓN', '(Solicitud de intervención del profesorado especialista en orientación educativa)'));
doc.push(sec('1.- DATOS PERSONALES DEL ALUMNO/A'));
doc.push(kv([
  ...datosAlumna.slice(1),
  ['Curso/nivel de inicio de la escolarización', '1º de Educación Infantil (3 años)'],
  ['Curso/nivel en que ingresó en el centro', '1º de Educación Infantil'],
  ['Repetición/es', `${NO} NO   ${SI} SÍ — 2º de Educación Primaria (curso 2015/16)`],
  [null, 'Incidencias escolares significativas'],
  ['', 'Asistencia regular. Sin incidencias de conducta. Dificultades en lectoescritura y lenguaje desde Educación Infantil.'],
  [null, 'Circunstancias relevantes y significativas del entorno familiar'],
  ['', 'Familia de nivel sociocultural bajo, interesada y colaboradora; acude al centro cuando se le cita. Expectativas bajas respecto a la alumna.'],
  ['Informes previos', `${SI} NO   ${NO} SÍ (psicopedagógico / médico / otros)`],
], 3600));
doc.push(sec('2.- DATOS DE IDENTIFICACIÓN DEL CENTRO'));
doc.push(kv(datosCentro, 3600));

doc.push(sec('3.- ASPECTOS A CONSIDERAR EN EL ALUMNO/A (sólo aquellos en los que sobresale o manifiesta dificultades en este momento)'));
const aspectos = [
  ['Capacidad intelectual', 0, 1], ['Memoria', 0, 1], ['Atención – concentración', 0, 1],
  ['Autoestima – autoconcepto', 0, 1], ['Ritmo de aprendizaje', 0, 1], ['Motivación e interés', 0, 0],
  ['Comportamiento en el aula / centro', 0, 0], ['Control del plan de trabajo / técnicas y hábitos de estudio', 0, 1],
  ['Comprensión lectora', 0, 1], ['Composición y expresión escrita', 0, 1],
  ['Razonamiento y comprensión: organización de ideas', 0, 1], ['Razonamiento y comprensión: resolución de problemas', 0, 1],
  ['Razonamiento y comprensión: razonamiento', 0, 1], ['Razonamiento y comprensión: cálculo', 0, 1],
  ['Relación: con el profesorado', 0, 0], ['Relación: con los compañeros', 1, 0],
  ['Relación: con su familia', 0, 0], ['Relación: integración en el grupo', 1, 0],
  ['Áreas (indicar): Lengua Castellana y Literatura; Matemáticas', 0, 1],
];
doc.push(table([6638, 1500, 1500], [
  [{ c: 'ASPECTOS', w: 6638, bold: true, fill: GRIS }, { c: 'SOBRESALE', w: 1500, bold: true, fill: GRIS }, { c: 'DIFICULTAD', w: 1500, bold: true, fill: GRIS }],
  ...aspectos.map(([a, s, d]) => [{ c: a, w: 6638 }, { c: s ? SI : NO, w: 1500 }, { c: d ? SI : NO, w: 1500 }]),
]));

doc.push(sec('4.- ACTUACIONES REALIZADAS PARA INTENTAR DAR RESPUESTA A LAS NECESIDADES EDUCATIVAS'));
doc.push(kv([
  [`${NO} Actividades de recuperación`, '—'],
  [`${SI} Refuerzo en el área de Lengua`, 'Priorización de objetivos/contenidos: lectoescritura básica. Agrupamientos: pequeño grupo, dentro y fuera del aula. Temporalización*: 3 sesiones semanales. Responsables: maestra de refuerzo y tutora.'],
  [`${SI} Refuerzo en el área de Matemáticas`, 'Priorización: numeración y cálculo básico. Agrupamientos: pequeño grupo. Temporalización*: 2 sesiones semanales. Responsables: maestra de refuerzo.'],
  [`${SI} Utilización de materiales y recursos diferentes`, 'Fichas de lectoescritura de nivel inferior; material manipulativo.'],
  [`${SI} Cambio metodológico`, 'Ubicación cerca de la tutora; instrucciones cortas; refuerzo social de los logros.'],
  [`${SI} Acción tutorial`, 'Entrevistas con la madre (3 en el curso pasado y 1 en el actual*).'],
  [`${NO} Participación en programas específicos`, '—'],
  [`${NO} Adaptaciones curriculares`, '—'],
  [`${SI} Otras`, 'Permanencia de un año más en 2º de Educación Primaria.'],
], 4200));

doc.push(sec('5.- BREVE VALORACIÓN DE LO QUE HA SUPUESTO LA ADOPCIÓN DE ESTAS MEDIDAS'));
doc.push(box('Valoración', 'Las medidas han mejorado la motivación y la participación de la alumna, pero los avances en lectura, escritura y lenguaje oral son mínimos. Persiste un desfase de más de un curso respecto a su grupo, a pesar de la repetición.'));
doc.push(sec('6.- DESCRIPCIÓN DE LA INTERVENCIÓN QUE SE SOLICITA'));
doc.push(box('Intervención', 'Realización de la evaluación psicopedagógica para determinar si presenta necesidades específicas de apoyo educativo, orientar la respuesta educativa y valorar la necesidad de apoyos especializados (PT y/o AL).'));
doc.push(sec('7.- OTRAS CONSIDERACIONES'));
doc.push(box('Otras consideraciones', 'La madre refiere que la alumna tardó en empezar a hablar. No existen informes médicos ni psicopedagógicos previos.'));
doc.push(firma('En Valladolid, a 10 de noviembre de 2015*.      Sello del centro  ·  Director/a del centro  ·  Tutor/a'));
doc.push(br());

// ---------- ANEXO II ----------
doc.push(...titulo('ANEXO II', 'AUTORIZACIÓN DE LOS PADRES O TUTORES LEGALES PARA LA REALIZACIÓN DE LA EVALUACIÓN PSICOPEDAGÓGICA'));
doc.push(kv([
  ['Don', 'J. G. R.'],
  ['Doña', 'M. M. L.'],
  ['Como padre/madre/tutor legal del alumno/a', ALUMNA],
  ['Dirección / Población / C.P.', 'C/ Ejemplo, 1  —  Valladolid  —  47000'],
  ['Tel. fijo / móvil / correo', '983 000 000  /  600 000 000  /  familia@ejemplo.es'],
]));
doc.push(p(''));
doc.push(p('AUTORIZAMOS a que nuestra hija sea derivada al:', { bold: true, size: 22 }));
doc.push(p(`${SI} Equipo de Orientación Educativa de: ${EOE}`));
doc.push(p(`${NO} Departamento de Orientación de: —`));
doc.push(p('para realizarle las valoraciones que se consideren adecuadas y determinar, en el caso que corresponda, sus necesidades específicas de apoyo educativo y poder dar la respuesta más adecuada a las mismas.'));
doc.push(firma('En Valladolid, a 16 de noviembre de 2015*.      Nombre y firma padre/tutor legal  ·  Nombre y firma madre/tutora legal'));
doc.push(p('Observaciones: Se ruega adjuntar cualquier informe (médico, psicológico, pedagógico) que pueda tener relación con la valoración planteada. → La familia indica que no dispone de informes previos.', { italics: true, before: 200 }));
doc.push(br());

// ---------- ANEXO III ----------
doc.push(...titulo('ANEXO III', 'INFORME PSICOPEDAGÓGICO'));
doc.push(kv([['Nº de expediente', '0000/2016*'], ['Fecha de realización del informe', '14 / 01 / 2016']]));
doc.push(sec('DATOS DE IDENTIFICACIÓN DEL ALUMNO'));
doc.push(kv(datosAlumna));

doc.push(sec('1.- DATOS DE IDENTIFICACIÓN DEL EOE / DEPARTAMENTO DE ORIENTACIÓN'));
doc.push(kv([
  [`${SI} Equipo de Orientación Educativa de`, EOE],
  [`${NO} Departamento de Orientación de`, '—'],
  [null, 'Profesionales que han participado en la evaluación psicopedagógica'],
  ['Orientador/a del EOE', 'Especialidad: Orientación educativa (Psicología/Pedagogía)'],
  ['Maestra de Audición y Lenguaje del EOE', 'Especialidad: Audición y Lenguaje'],
], 4200));
doc.push(sec('2.- DATOS DE IDENTIFICACIÓN DEL CENTRO'));
doc.push(kv(datosCentro));

doc.push(sec('3.- MOTIVOS DE LA EVALUACIÓN'));
doc.push(kv([
  ['Solicitado por', 'Tutora, con el visto bueno de la dirección (documento de derivación, Anexo I)'],
  [null, 'Situación tipo'],
  ['', `${NO} Nueva escolarización   ${NO} Cambio de modalidad   ${NO} Cambio de centro/etapa   ${NO} Revisión o seguimiento   ${NO} Repetición extraordinaria   ${SI} Otras: dificultades persistentes en lectoescritura y lenguaje tras comprobar la ineficacia de las medidas ordinarias de atención a la diversidad.`],
]));
doc.push(sec('4.- INFORMACIÓN PREVIA DISPONIBLE'));
doc.push(kv([[`${NO} Informe médico  ${NO} Informe psicopedagógico  ${NO} Otros`, 'No existen informes previos.']], 5200));

doc.push(sec('5.- TÉCNICAS Y PRUEBAS UTILIZADAS'));
doc.push(kv([
  [`${SI} Análisis de información y documental`, 'Expediente académico; documento de derivación; cuestionario de la tutora sobre desarrollo personal, escolar, estilo de aprendizaje y clima de aula.'],
  [`${SI} Observación`, 'Durante la evaluación (4 sesiones, del 17/11/2015 al 12/01/2016); en el aula; en el patio; muestra de lenguaje espontáneo.'],
  [`${SI} Entrevistas`, 'Con la tutora y con la madre de la alumna.'],
  [`${SI} Pruebas psicopedagógicas estándar`, 'WISC-IV (inteligencia); PROLEC-R (procesos lectores); PROESC (procesos de escritura); ITPA (aptitudes psicolingüísticas, aplicado por la maestra de AL).'],
], 4200));

doc.push(sec('6.- DATOS Y ASPECTOS RELEVANTES DE LA HISTORIA PERSONAL DEL ALUMNO'));
doc.push(table([1900, 3600, 2138, 2000], [
  [{ c: 'HISTORIA ESCOLAR — Escolarización previa (dos últimos cursos)', w: W, bold: true, fill: GRIS, span: 4 }],
  [{ c: 'Curso académico', w: 1900, bold: true }, { c: 'Centro', w: 3600, bold: true }, { c: 'Etapa / Curso', w: 2138, bold: true }, { c: 'Medidas adoptadas', w: 2000, bold: true }],
  [{ c: '2013/14', w: 1900 }, { c: CENTRO, w: 3600 }, { c: 'Primaria / 1º', w: 2138 }, { c: `${SI} Refuerzo educativo`, w: 2000 }],
  [{ c: '2014/15', w: 1900 }, { c: CENTRO, w: 3600 }, { c: 'Primaria / 2º', w: 2138 }, { c: `${SI} Refuerzo educativo`, w: 2000 }],
]));
doc.push(kv([
  [null, 'CURSO ACTUAL (2015/16)'],
  ['Modalidad de escolarización', 'Ordinaria'],
  ['Medidas adoptadas', `${SI} Refuerzo educativo (Lengua y Matemáticas)  ${NO} Apoyos especializados  ${NO} Programas  ${NO} Adaptación curricular  ${SI} Otras: permanencia de un año más en 2º`],
  ['Otros aspectos de la historia escolar', 'Ha estado escolarizada siempre en el mismo centro, con asistencia regular.'],
  [null, 'DESARROLLO GENERAL'],
  ['Condiciones personales de salud, diagnósticos…', 'No hay datos clínicos relevantes. Visión y audición funcionales.'],
  ['Desarrollo de capacidades: cognitivas', 'WISC-IV: CI total = 70 (zona muy baja, funcionamiento intelectual compatible con discapacidad intelectual leve). Comprensión verbal 77 (pc 6), Razonamiento perceptivo 71 (pc 3), Memoria de trabajo 72 (pc 3), Velocidad de procesamiento 93 (promedio bajo). La diferencia entre índices (22 puntos) permite interpretar el CIT con fiabilidad. El aspecto más debilitado es el razonamiento perceptivo.'],
  ['Psicomotoras', 'Desarrollo psicomotor funcional: buena coordinación general, equilibrio, tono, motricidad fina y lateralidad definida. No necesita atención específica. Autónoma en desplazamientos, aseo, alimentación y uso de materiales.'],
  ['Lingüísticas', 'Sin problemas de articulación, pero con dificultades expresivas y comprensivas: estructuras oracionales inadecuadas para su edad, vocabulario pobre, dificultades de conciencia fonológica (no segmenta frases en palabras ni palabras en sílabas) y de comprensión de frases complejas. ITPA: rendimiento medio 2 desviaciones típicas por debajo de la media (más afectadas la asociación auditiva, la memoria secuencial auditiva y la expresión verbal).'],
  ['Lectura (PROLEC-R)', 'Dificultades en los cuatro procesos lectores: identificación de letras, procesos léxicos (ruta visual y fonológica), sintácticos y semánticos (comprensión de oraciones, de textos y oral). Dificultades de precisión y de velocidad.'],
  ['Escritura (PROESC)', 'Dificultades en el dictado de sílabas, palabras (ortografía arbitraria y reglada) y pseudopalabras; en acentos y mayúsculas; y en la planificación (escritura de un cuento y de una redacción).'],
  [null, 'ADAPTACIÓN Y RELACIÓN SOCIAL'],
  ['Autonomía, autoconcepto, autoestima, habilidades sociales…', 'Pide ayuda cuando la necesita y tiene autonomía personal y social. Se relaciona bien con adultos e iguales y está totalmente integrada en el grupo; en el patio juega con distintos compañeros. Muestra inseguridad y baja confianza en sí misma: necesita aprobación por cada logro, aunque no se da fácilmente por vencida.'],
  [null, 'NIVEL DE COMPETENCIA CURRICULAR'],
  ['', 'Según la tutora, se sitúa en el inicio de 1º de Educación Primaria en Lengua y Matemáticas (desfase superior a un curso respecto a su grupo).'],
], 3200));

doc.push(sec('Estilo de aprendizaje'));
const est = [
  ['Atención y concentración', 'BAJA'], ['Motivación', 'MEDIA'], ['Nivel de autonomía (en el trabajo)', 'BAJA'],
  ['Aceptación de normas', 'ALTA'], ['Resistencia a la frustración', 'MEDIA'], ['Actitud', 'ALTA'],
  ['Memoria', 'BAJA'], ['Actitud ante las ayudas y apoyos', 'ALTA'], ['Actitud ante actividades que domina', 'ALTA'],
  ['Actitud ante actividades difíciles', 'MEDIA'], ['Capacidad de trabajo', 'MEDIA'],
];
const opts = ['NULA', 'BAJA', 'MEDIA', 'ALTA'];
const cw = [3638, 1500, 1500, 1500, 1500];
doc.push(table(cw, [
  ...est.map(([a, v]) => [{ c: a, w: cw[0] }, ...opts.map((o, i) => ({ c: `${o === v ? SI : NO} ${o}`, w: cw[i + 1] }))]),
  [{ c: 'Preferencias de agrupamiento', w: cw[0] }, ...['SOLO', 'PAREJA', 'PEQ-GRUPO', 'GR-GRUPO'].map((o, i) => ({ c: `${o === 'SOLO' ? SI : NO} ${o}`, w: cw[i + 1] }))],
  [{ c: 'Terminación de las tareas', w: cw[0] }, ...['NUNCA', 'CASI NUNCA', 'A VECES', 'SIEMPRE'].map((o, i) => ({ c: `${o === 'A VECES' ? SI : NO} ${o}`, w: cw[i + 1] }))],
  [{ c: 'Preferencia en los tipos de lenguajes', w: cw[0] }, ...['VISUAL', 'AUDITIVA', 'MANIPULAT.', 'MIXTA'].map((o, i) => ({ c: `${o === 'MIXTA' ? SI : NO} ${o}`, w: cw[i + 1] }))],
]));
doc.push(kv([
  ['Refuerzos a los que responde', `${SI} MATERIALES   ${NO} ACTIVIDAD   ${SI} SOCIALES`],
  ['Ritmo de aprendizaje', `${SI} LENTO   ${NO} NORMAL   ${NO} RÁPIDO`],
  ['Áreas en que muestra más interés', 'Educación Artística, Educación Física*'],
  ['Áreas en que muestra menos interés', 'Lengua Castellana y Literatura*'],
  ['Otros aspectos a considerar', 'Trabaja mejor con luz natural y cerca de la tutora. Se distrae con facilidad; mejora si se le presta atención puntual. Resuelve por ensayo-error. Necesita que le recuerden lo que tiene que hacer. Recuerda mejor lo que ve, oye, lee y escribe.'],
], 3638));

doc.push(sec('7.- DATOS Y ASPECTOS RELEVANTES, EN EL PROCESO DE ENSEÑANZA/APRENDIZAJE, DEL CONTEXTO EDUCATIVO'));
doc.push(kv([
  ['Relación profesor/alumno', `${NO} INADECUADAS   ${NO} ADECUADAS   ${SI} BUENAS`],
  ['Relación con compañeros', `${NO} INADECUADAS   ${NO} ADECUADAS   ${SI} BUENAS`],
  ['Características del aula', 'Organización variable (individual, pequeño grupo, gran grupo). La alumna está situada en una posición especial, cerca de la tutora. Los materiales y la secuencia de actividades se adaptan a sus posibilidades.'],
  ['Características del grupo/clase', 'Total de alumnos: 22*. Alumnado con necesidades educativas: 2*. Clima de aula: bueno.'],
  [null, 'Recursos generales y específicos para la atención al alumnado con necesidades específicas de apoyo educativo'],
  ['Recursos personales del centro', 'Tutora; maestra de refuerzo; maestra de Pedagogía Terapéutica (PT) y maestra de Audición y Lenguaje (AL) del centro*.'],
  ['Recursos organizativos y didácticos', 'Horario de apoyos coordinado con la tutoría; materiales de lectoescritura adaptados.'],
], 3200));

doc.push(sec('8.- DATOS Y ASPECTOS RELEVANTES DEL CONTEXTO FAMILIAR'));
doc.push(kv([
  ['Estructura familiar', 'Padre, madre, un hermano mayor, la alumna y una hermana menor.'],
  ['Relaciones familiares', 'Adecuadas.'],
  ['Nivel socio-cultural', 'Bajo.'],
  ['Pautas educativas familiares', 'La familia ha asumido las dificultades de su hija; actitud interesada.'],
  ['Expectativas respecto a la alumna', 'Bajas.'],
  ['Colaboración con el centro', 'Buena: acuden al centro cuando se les cita.'],
], 3200));
doc.push(sec('9.- DATOS Y ASPECTOS RELEVANTES DEL CONTEXTO SOCIAL'));
doc.push(box('Recursos del contexto social', 'El barrio cuenta con biblioteca municipal y actividades extraescolares del ayuntamiento*; actualmente la alumna no participa en ellas.'));

doc.push(sec('10.- CATEGORIZACIÓN (clasificación de la aplicación ATDI)'));
doc.push(kv([
  ['Grupo principal', 'ACNEE — Alumnado con necesidades educativas especiales'],
  ['Tipología', 'Discapacidad psíquica'],
  ['Categoría', 'Discapacidad intelectual leve'],
  ['Grupo secundario', '—'],
], 3200));

doc.push(sec('11.- IDENTIFICACIÓN DE LAS NECESIDADES ESPECÍFICAS DE APOYO EDUCATIVO'));
doc.push(kv([
  [null, 'Necesidades de tipo personal'],
  ['Aspectos cognitivos', `${SI} Estrategias de focalización y atención  ${SI} Memoria  ${SI} Estructuración de la información/comprensión  ${SI} Capacidad de razonamiento  ${SI} Mejorar los hábitos de estudio`],
  ['Equilibrio personal o afectivo-emocional', `${SI} Autoconcepto y autoestima  ${SI} Autonomía personal (en el trabajo)`],
  ['Relación interpersonal y adaptación social', `${SI} No presenta`],
  ['Desarrollo psicomotor', `${SI} No presenta`],
  ['Desarrollo comunicativo-lingüístico', `${SI} Expresión oral (no articulación)  ${SI} Comprensión oral  ${SI} Desarrollo morfosintáctico  ${SI} Nivel semántico/vocabulario  ${SI} Expresión y composición escrita`],
  [null, 'Necesidades de tipo curricular'],
  ['', 'Desfase curricular significativo en Lengua y Matemáticas (nivel de inicio de 1º). Necesita trabajar todos los procesos de lectura y escritura.'],
  [null, 'Aspectos de tipo socio-familiar a considerar'],
  ['', 'Bajas expectativas familiares: conviene implicar a la familia y transmitirle expectativas realistas pero positivas.'],
], 3200));

doc.push(sec('12.- ORIENTACIONES PARA LA PROPUESTA CURRICULAR'));
doc.push(kv([
  ['Adecuación curricular / adaptaciones', 'Adaptación curricular significativa (ACS) en Lengua Castellana y Literatura y Matemáticas, buscando el máximo desarrollo de las competencias clave. Coordinación de tutora, PT y AL en su elaboración y seguimiento.'],
  ['Modalidad de escolarización recomendada', 'Centro ordinario con apoyos.'],
  ['Programas específicos', 'Estimulación cognitiva (atención, memoria, razonamiento); lectoescritura (conciencia fonológica, conversión grafema-fonema, comprensión); lenguaje oral (AL); autoestima y autonomía en el trabajo.'],
  ['Adaptaciones de acceso', 'Ubicación cerca de la tutora y con luz natural. No precisa equipamiento específico.'],
  ['Adaptaciones en metodología y actividades', 'Instrucciones cortas y sencillas, con apoyo visual; partir de lo concreto y funcional; tareas breves que aseguren el éxito; refuerzo social y material; recordarle los pasos de la tarea; enfoque comprensivo en la lectoescritura.'],
  ['Recursos personales y materiales', 'PT: 4 sesiones semanales*; AL: 2 sesiones semanales*; preferentemente dentro del aula. Materiales de lectoescritura adaptados.'],
  ['Ámbito extraescolar', 'Animación a la lectura en la biblioteca municipal; actividades lúdicas y de juego con iguales.'],
], 3200));

doc.push(sec('13.- ORIENTACIONES A LA FAMILIA'));
doc.push(box('Orientaciones a la familia', [
  'Leer juntos 10-15 minutos al día y jugar con palabras (rimas, adivinanzas, separar sílabas).',
  'Reforzar los logros y el esfuerzo, no solo los resultados. Evitar la sobreprotección y dar solo la ayuda necesaria.',
  'Mantener rutinas y límites claros y coherentes. Tener expectativas realistas pero positivas.',
  'Mantener reuniones trimestrales con la tutora para coordinarse.',
]));
doc.push(sec('14.- PROPUESTA DE SEGUIMIENTO Y REVISIÓN'));
doc.push(box('Seguimiento', 'Seguimiento trimestral por la tutora, PT y AL, con asesoramiento del EOE. Revisión del informe al final de la etapa o cuando cambie de forma significativa la situación de la alumna.'));
doc.push(firma('En Valladolid, a 14 de enero de 2016.      Sello del EOE  ·  Nombre y firma de los profesionales que han intervenido'));
doc.push(kv([
  ['Información al profesorado tutor', 'Fecha: 14/01/2016  —  Firma: tutora'],
  ['Información a la familia, que manifiesta su', `${SI} CONFORMIDAD   ${NO} DISCONFORMIDAD   con la propuesta realizada`],
], 3600));
doc.push(p('Los datos de este informe están recogidos con autorización de la familia y son estrictamente confidenciales…', { italics: true, size: 16, before: 120 }));
doc.push(br());

// ---------- ANEXO IV ----------
doc.push(...titulo('ANEXO IV', 'DICTAMEN DE ESCOLARIZACIÓN'));
doc.push(kv([['Nº de expediente', '0000/2016*'], ['Fecha de realización del dictamen', '20 / 01 / 2016*']]));
doc.push(sec('DATOS DE IDENTIFICACIÓN DEL ALUMNO'));
doc.push(kv(datosAlumna));
doc.push(sec('1.- PROPUESTA REALIZADA POR'));
doc.push(kv([[`${SI} Equipo de Orientación Educativa de`, EOE], [`${NO} Departamento de Orientación de`, '—']], 4200));
doc.push(sec('2.- OTROS DATOS DEL ALUMNO/A — Información aportada por la familia'));
doc.push(kv([
  [`${NO} Calificación de minusvalía`, 'No aporta.'],
  [`${NO} Informe médico`, 'No aporta.'],
  [`${NO} Informe de Centro Base`, 'No aporta.'],
  [`${NO} Otros informes`, '—'],
], 4200));
doc.push(sec('3.- DATOS DE IDENTIFICACIÓN DEL CENTRO (escolarización actual)'));
doc.push(kv(datosCentro));
doc.push(sec('4.- MOTIVO DEL DICTAMEN'));
doc.push(p(`${NO} Nueva escolarización   ${NO} Cambio de etapa   ${NO} Cambio de centro   ${NO} Revisión-modificación   ${SI} Otros: identificación como ACNEE tras la evaluación psicopedagógica.`));
doc.push(sec('5.- SÍNTESIS DE LA EVALUACIÓN PSICOPEDAGÓGICA'));
doc.push(kv([
  ['Apreciación global del desarrollo, madurez y desarrollo social', 'Alumna de 8 años con desarrollo motor y autonomía personal adecuados, bien integrada socialmente, con baja autoestima y un desarrollo cognitivo y lingüístico inferior al esperado para su edad.'],
  ['Datos relevantes de la evaluación', 'CIT 70 (WISC-IV), compatible con discapacidad intelectual leve. ITPA: 2 DT por debajo de la media. Dificultades en todos los procesos de lectura y escritura.'],
  ['Estilo de aprendizaje', 'Atención y memoria bajas; ritmo lento; dependiente en el trabajo; responde bien a refuerzos sociales y materiales y a las ayudas.'],
  ['Nivel de competencia curricular', 'Inicio de 1º de Educación Primaria en Lengua y Matemáticas.'],
  ['Aspectos relevantes en la enseñanza-aprendizaje', 'Familia colaboradora con expectativas bajas. Buen clima de aula y buena relación con la tutora y los compañeros.'],
], 3600));
doc.push(sec('6.- CATEGORIZACIÓN (ATDI)'));
doc.push(kv([['Grupo principal', 'ACNEE'], ['Tipología', 'Discapacidad psíquica'], ['Categoría', 'Discapacidad intelectual leve'], ['Grupo secundario', '—']], 3200));
doc.push(sec('7.- IDENTIFICACIÓN DE LAS NECESIDADES ESPECÍFICAS DE APOYO EDUCATIVO'));
doc.push(kv([
  ['Necesidades de tipo personal', 'Atención, memoria, razonamiento y comprensión; autoestima y autonomía en el trabajo; lenguaje oral expresivo y comprensivo.'],
  ['Necesidades de tipo curricular', 'Desfase significativo en Lengua y Matemáticas; lectoescritura.'],
  ['Aspectos de tipo sociofamiliar', 'Elevar las expectativas familiares y mantener la colaboración con el centro.'],
], 3200));
doc.push(sec('8.- ORIENTACIONES PARA LA PROPUESTA CURRICULAR'));
const aw = [3638, 1000, 1000, 1000, 3000];
doc.push(table(aw, [
  [{ c: 'Ámbitos de funcionalidad', w: aw[0], bold: true, fill: GRIS }, { c: 'NULO', w: aw[1], bold: true, fill: GRIS }, { c: 'BAJO', w: aw[2], bold: true, fill: GRIS }, { c: 'MEDIO', w: aw[3], bold: true, fill: GRIS }, { c: 'Ayudas técnicas que requiere', w: aw[4], bold: true, fill: GRIS }],
  ...[['Autonomía en la comunicación', 1], ['Autonomía en los desplazamientos', 0], ['Autonomía personal (aseo, esfínteres…)', 0]].map(([a, n]) =>
    [{ c: a, w: aw[0] }, { c: n === 0 ? SI : NO, w: aw[1] }, { c: n === 1 ? SI : NO, w: aw[2] }, { c: NO, w: aw[3] }, { c: 'Ninguna', w: aw[4] }]),
]));
doc.push(p('(Grado de necesidad de ayuda en cada ámbito.)', { italics: true, size: 16 }));
doc.push(kv([
  [null, 'Estimación de los programas específicos'],
  [`${SI} Precisa`, 'Estimulación cognitiva; lectoescritura; lenguaje oral; autoestima.'],
  [null, 'Estimación de los apoyos educativos especializados y propuestas de adaptación'],
  [`${NO} Intérprete de Lengua de Signos`, '—'],
  [`${NO} Ayudante Técnico Educativo`, '—'],
  [`${NO} Atención fisioterapéutica`, '—'],
  [`${SI} Apoyo de Pedagogía Terapéutica – PT`, '4 sesiones semanales*, preferentemente dentro del aula.'],
  [`${SI} Apoyo de Audición y Lenguaje – AL`, '2 sesiones semanales*.'],
  [`${SI} Adaptaciones curriculares`, 'ACS en Lengua Castellana y Literatura y Matemáticas.'],
], 4200));
doc.push(sec('9.- PROPUESTA DE MODALIDAD DE ESCOLARIZACIÓN'));
doc.push(kv([
  ['Etapa / Curso', 'Educación Primaria — 2º'],
  [`${SI}`, 'Escolarización en centro ordinario'],
  [`${NO}`, 'Escolarización en centro ordinario preferente'],
  [`${NO}`, 'Específica en centro de educación especial'],
  [`${NO}`, 'Específica en aula sustitutoria de centro de educación especial'],
  [`${NO}`, 'Combinada'],
  ['Revisión de la modalidad', 'Al finalizar la etapa o ante cambios significativos.'],
], 2200));
doc.push(sec('10.- OBSERVACIONES'));
doc.push(box('Observaciones', 'Continúa en su centro y grupo actual. Los apoyos de PT y AL se realizarán preferentemente dentro del aula ordinaria, con alguna sesión individual fuera del aula para el trabajo específico de lenguaje.'));
doc.push(firma('En Valladolid, a 20 de enero de 2016*.      Vº Bº del Director/a  ·  Nombre y firma del Orientador/a  ·  Sello del EOE'));
doc.push(br());

// ---------- ANEXO V ----------
doc.push(...titulo('ANEXO V', 'OPINIÓN DE LA FAMILIA RESPECTO A LA PROPUESTA DEL DICTAMEN DE ESCOLARIZACIÓN'));
doc.push(sec('A.- Centros de la zona con recursos para atender las necesidades educativas de la alumna'));
doc.push(box('Centros', [`${CENTRO} — dispone de PT y AL`, 'CEIP «Ejemplo 2» (ficticio) — dispone de PT y AL']));
doc.push(sec('B.- Preferencias de centro manifestadas por los padres'));
doc.push(kv([['1º Centro', CENTRO + ' (su centro actual)'], ['2º Centro', '—'], ['3º Centro', '—']], 2200));
doc.push(sec('C.- Opinión de los padres respecto a la modalidad de escolarización recogida en el dictamen'));
doc.push(p('D./Dña.: J. G. R. y M. M. L., en calidad de padre y madre de la alumna a la que se refiere este dictamen, somos informados por el Equipo de Orientación Educativa de la evaluación psicopedagógica realizada, de la modalidad de escolarización propuesta y de los servicios educativos de que dispone la zona.'));
doc.push(p('Respecto a la modalidad de escolarización expresada en el dictamen deseamos manifestar:', { before: 120 }));
doc.push(p(`${SI} Estar de acuerdo`, { bold: true, size: 24 }));
doc.push(p(`${NO} Estar en desacuerdo (especificar los motivos): —`, { size: 22 }));
doc.push(firma('En Valladolid, a 22 de enero de 2016*.      Nombre y firma padre/tutor legal  ·  Nombre y firma madre/tutora legal'));

const out = new Document({
  styles: { default: { document: { run: { font: FONT, size: 19 } } } },
  sections: [{
    properties: { page: { margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    headers: { default: new Header({ children: [p('Modelos de la Orden EDU/1603/2009 (Castilla y León) — EJEMPLO SIMULADO CON FINES DIDÁCTICOS, NO ES UN DOCUMENTO OFICIAL', { size: 15, italics: true, color: '666666' })] }) },
    footers: { default: new Footer({ children: [p('Datos ficticios. Adaptado del «Informe Tipo DIS-I» a la Orden EDU/1603/2009. Los datos con * se han completado para el ejemplo.', { size: 14, italics: true, color: '666666' })] }) },
    children: doc,
  }],
});
Packer.toBuffer(out).then(b => { fs.writeFileSync(__dirname + '/Caso_practico_Orden_EDU_1603_2009.docx', b); console.log('ok'); });
