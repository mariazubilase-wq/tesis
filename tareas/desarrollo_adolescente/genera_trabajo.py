"""Trabajo completo: hoja 1 horizontal con el mapa conceptual y, en vertical, la explicación.

Uso:  python3 genera_trabajo.py   (crea trabajo_final.docx junto a este script)
"""
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor

AQUI = Path(__file__).resolve().parent
ACENTO = RGBColor(0x22, 0x30, 0x3F)

doc = Document()
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(11)
normal.paragraph_format.space_after = Pt(5)
normal.paragraph_format.line_spacing = 1.12
for nivel, tam in ((1, 14), (2, 12)):
    h = doc.styles[f"Heading {nivel}"]
    h.font.name = "Calibri"
    h.font.size = Pt(tam)
    h.font.color.rgb = ACENTO
    h.paragraph_format.space_before = Pt(10 if nivel == 1 else 6)
    h.paragraph_format.space_after = Pt(3)

# ---------------------------------------------------------------- hoja 1: mapa
hoja1 = doc.sections[0]
hoja1.orientation = WD_ORIENT.LANDSCAPE
hoja1.page_width, hoja1.page_height = Cm(29.7), Cm(21)
hoja1.left_margin = hoja1.right_margin = Cm(1.5)
hoja1.top_margin = hoja1.bottom_margin = Cm(1.5)
doc.add_picture(str(AQUI / "mapa_conceptual.png"), width=Cm(26.5))
doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER

# ---------------------------------------------------------------- resto: texto
resto = doc.add_section(WD_SECTION.NEW_PAGE)
resto.orientation = WD_ORIENT.PORTRAIT
resto.page_width, resto.page_height = Cm(21), Cm(29.7)
resto.left_margin = resto.right_margin = Cm(2.5)
resto.top_margin = resto.bottom_margin = Cm(2.2)


def p(*trozos):
    """Párrafo justificado; los trozos entre ** ** van en negrita."""
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    for t in trozos:
        if t.startswith("**") and t.endswith("**"):
            par.add_run(t[2:-2]).bold = True
        else:
            par.add_run(t)
    return par


def vineta(*trozos):
    par = p(*trozos)
    par.style = doc.styles["List Bullet"]
    return par


doc.add_heading("Explicación del mapa conceptual", 1)
p("La adolescencia es el periodo en el que el niño se convierte en adulto a través de intensos cambios "
  "físicos, psíquicos y sociales (Casas y Ceñal, 2005). Coincide casi por completo con la Educación "
  "Secundaria, por lo que conocerla es imprescindible para comprender y orientar al alumnado. El mapa la "
  "organiza en una tabla: en las filas, las tres dimensiones de la personalidad (bio-física, psico-afectiva "
  "y socio-moral); en las columnas, las tres fases (temprana, de 11 a 13 años; media, de 14 a 17; y tardía, "
  "de 17 a 21) y, en la última, la influencia de las tecnologías digitales en cada dimensión. Hay que tener "
  "en cuenta que las fases son un continuo y que cada adolescente y cada dimensión llevan su propio ritmo, "
  "con posibles retrocesos en momentos de estrés.")

# ---------------------------------------------------------------- 1. desarrollo
doc.add_heading("1. Características del desarrollo adolescente", 1)

doc.add_heading("1.1. Dimensión bio-física", 2)
p("La pubertad comienza con cambios hormonales en el eje hipotálamo-hipófisis-gónadas que culminan en la "
  "capacidad reproductiva. El rango de normalidad es muy amplio: el 95 % de las chicas la inicia entre los "
  "8,5 y los 13 años y el 95 % de los chicos entre los 9,5 y los 14, y la edad de inicio se ha adelantado "
  "unos 3-4 meses por década en los últimos 150 años (Casas y Ceñal, 2005).")
vineta("**Adolescencia temprana:** ", "se caracteriza por un rápido crecimiento somático y la aparición de los "
       "caracteres sexuales secundarios (la menarquia llega, de media, a los 12,4 años). Estos cambios hacen "
       "que se pierda la imagen corporal infantil.")
vineta("**Adolescencia media:** ", "el crecimiento y la maduración sexual prácticamente han terminado y se alcanza "
       "alrededor del 95 % de la talla adulta. Como los cambios son ya mucho más lentos, el adolescente puede "
       "restablecer su imagen corporal.")
vineta("**Adolescencia tardía:** ", "el crecimiento ha terminado y son físicamente maduros.")

doc.add_heading("1.2. Dimensión psico-afectiva", 2)
vineta("**Adolescencia temprana:** ", "los cambios físicos generan una gran preocupación y curiosidad por la nueva "
       "imagen corporal. El pensamiento es totalmente concreto, por lo que no perciben las consecuencias "
       "futuras de sus actos. Creen ser el centro de una «audiencia imaginaria» que les observa constantemente, "
       "de ahí su gran sentido del ridículo, y su orientación es narcisista y egoísta.")
vineta("**Adolescencia media:** ", "empieza el pensamiento abstracto, aunque con el estrés vuelve a ser concreto. "
       "Se interesan por temas idealistas y disfrutan discutiendo ideas. Aparece una sensación de omnipotencia "
       "e invulnerabilidad («a mí no me va a pasar») que favorece conductas de riesgo como el consumo de "
       "alcohol, tabaco y drogas o los embarazos no deseados.")
vineta("**Adolescencia tardía:** ", "el pensamiento abstracto está plenamente establecido, aunque no todos lo "
       "alcanzan, y están orientados al futuro. Es una fase estable que puede alterarse con la llamada "
       "«crisis de los 21», cuando se enfrentan a las exigencias reales del mundo adulto.")

doc.add_heading("1.3. Dimensión socio-moral", 2)
vineta("**Adolescencia temprana:** ", "el grupo de amigos, normalmente del mismo sexo, ayuda a contrarrestar la "
       "inestabilidad de los cambios: en él se compara la propia normalidad y se busca la aceptación. Los "
       "contactos con el otro sexo son «exploratorios» y empiezan los primeros intentos de independencia e "
       "intimidad, pero sin grandes conflictos familiares.")
vineta("**Adolescencia media:** ", "la lucha por la emancipación está en plena efervescencia y pertenecer a un "
       "grupo adquiere una importancia altísima: el grupo dicta la forma de vestir, de hablar y de "
       "comportarse. Las opiniones de los amigos pesan más que las de los padres, aunque estos siguen siendo "
       "una referencia necesaria («los padres permanecen, el grupo cambia»). Algunos adolescentes, antes que "
       "quedarse solos, se unen a grupos marginales. Aumentan las relaciones con el otro sexo, sobre todo "
       "para comprobar la propia capacidad de atraer.")
vineta("**Adolescencia tardía:** ", "el grupo pierde importancia en favor de las amistades individuales, las "
       "relaciones familiares pasan a ser de adulto a adulto y las relaciones de pareja son estables, "
       "recíprocas y con proyectos de futuro.")

# ---------------------------------------------------------------- 2. digital
doc.add_heading("2. Influencia de las tecnologías digitales", 1)
p("La última columna del mapa recoge cómo influyen las tecnologías digitales en cada dimensión. Las fuentes no "
  "diferencian este impacto por fases, sino que hablan de la adolescencia en general, por eso aparece por "
  "dimensiones. El punto de partida es un uso masivo: el 98 % de los adolescentes tiene Internet en casa, "
  "casi uno de cada tres (31,9 %) lo usa de forma habitual desde antes de los 10 años, el 21,4 % dice estar "
  "«permanentemente conectado» y el 16,5 % pasa más de cuatro horas al día en Internet sin contar las tareas "
  "escolares (Save the Children, 2024). Además, el uso aumenta con la edad: más de cuatro horas diarias las "
  "pasa el 12 % de los adolescentes de 14 años y el 21 % de los de 16.")

doc.add_heading("2.1. En la dimensión bio-física", 2)
vineta("**Duermen menos:** ", "el 18,3 % de los adolescentes reconoce que deja de dormir por estar conectado, más "
       "las chicas (20,5 %) que los chicos (14,9 %) (Save the Children, 2024). Dormir poco o mal impide que el "
       "cerebro se concentre al día siguiente (Desmurget, 2020).")
vineta("**«Ocio paralizante»:** ", "así llaman algunos profesionales al ocio frente a las pantallas, porque limita "
       "las actividades que implican movimiento o relación física con otras personas. El 11,9 % reconoce que "
       "deja de hacer deporte o actividades extraescolares por estar conectado (Save the Children, 2024).")
vineta("**Cánones de belleza:** ", "las chicas siguen más trucos de belleza y de imagen en redes, lo que las "
       "enfrenta a cánones de belleza inalcanzables y a la cosificación de sus cuerpos (Save the Children, "
       "2024). Esto afecta a un cuerpo que, como hemos visto, acaba de cambiar y es fuente de preocupación.")

doc.add_heading("2.2. En la dimensión psico-afectiva", 2)
vineta("**Atención:** ", "un metaanálisis con más de 150.000 menores relaciona el uso de pantallas de ocio con el "
       "déficit de atención. Ver entre una y tres horas de televisión al día a los 14 años multiplica por 1,4 "
       "el riesgo de problemas de atención a los 16, y por 2,9 si se superan las tres horas. Basta con tener el "
       "móvil al alcance de la mano, aunque no se use, para rendir menos (Desmurget, 2020).")
vineta("**Malestar emocional:** ", "entre quienes pasan más de cuatro horas al día conectados, el 30,9 % siente "
       "siempre o casi siempre que las dificultades le superan, frente al 18,9 % del resto. Las chicas lo "
       "refieren el doble que los chicos (21,1 % frente a 9,8 %). No se puede afirmar que Internet sea la "
       "causa, pero la relación es clara (Save the Children, 2024).")
vineta("**Autoestima y «likes»:** ", "el «me gusta» es lo más parecido en el mundo digital a ser aceptado por el "
       "grupo, pero es efímero y genera la necesidad de buscarlo continuamente para sentirse reconocido "
       "(Save the Children, 2024). Cada notificación o «like» produce una pequeña descarga de dopamina, lo que "
       "explica en parte el uso compulsivo del móvil (Desmurget, 2020).")
vineta("**Enganche, lectura y lenguaje:** ", "muchos no son conscientes del tiempo que pasan en plataformas como "
       "TikTok, que encadenan vídeos sin fin, y el 19,2 % reconoce estar conectado más de lo que le gustaría. "
       "El 27,6 % lee menos y el 31 % estudia menos por estar en Internet (Save the Children, 2024). Para "
       "Desmurget (2020), por encima de un nivel básico el lenguaje solo se enriquece a través de la lectura, "
       "por lo que esta pérdida empobrece el vocabulario y el pensamiento.")

doc.add_heading("2.3. En la dimensión socio-moral", 2)
vineta("**Amistades conectadas:** ", "el entorno digital también tiene aspectos positivos: permite a los "
       "adolescentes crear y mantener amistades y participar en comunidades afines (Save the Children, 2024).")
vineta("**Menos relación cara a cara y en familia:** ", "el 17,3 % pasa menos tiempo con su familia por estar "
       "conectado (Save the Children, 2024), cuando las relaciones familiares siguen siendo cruciales durante "
       "toda la adolescencia para el éxito escolar, la estabilidad emocional y la prevención de conductas de "
       "riesgo (Desmurget, 2020). Además, se conectan sobre todo a solas, lo que dificulta pedir ayuda ante "
       "una situación de riesgo.")
vineta("**Deshumanización:** ", "a través de una pantalla se dicen cosas que nunca se dirían cara a cara, lo que "
       "favorece el ciberacoso y los mensajes de odio: en torno al 20 % ha vivido o presenciado situaciones "
       "que podrían ser acoso. Las redes también se usan para controlar a la pareja: el 8,2 % cree que está "
       "bien mirarle el móvil y el 37,3 % que depende de la situación (Save the Children, 2024).")
vineta("**Pornografía y modelos sexistas:** ", "el 58 % se ha encontrado pornografía sin buscarla. Sin una "
       "educación afectivo-sexual, se convierte en el modelo de relación. En redes abundan además los "
       "estereotipos de género, la sexualización de las chicas y actitudes cada vez más machistas en los "
       "chicos (Save the Children, 2024).")

# ---------------------------------------------------------------- 3. por qué
doc.add_heading("3. ¿Por qué la adolescencia es tan sensible a lo digital?", 1)
p("Relacionando las dos partes del mapa se entiende por qué el impacto es tan fuerte en esta etapa:")
vineta("**Diseño persuasivo:** ", "las plataformas están pensadas para adultos y buscan que pasemos en ellas el "
       "mayor tiempo posible (Save the Children, 2024). Un expresidente de Facebook llegó a reconocer que se "
       "diseñaron para consumir «el máximo de vuestro tiempo y de vuestra capacidad de atención» (Desmurget, "
       "2020). El adolescente, que percibe poco el riesgo, necesita la aceptación del grupo y está "
       "construyendo su autoestima, es el usuario perfecto para este diseño.")
vineta("**Desplazamiento:** ", "cada hora frente a la pantalla es una hora menos de sueño, lectura, estudio, "
       "deporte o conversación. El daño no viene solo de lo que ven, sino de lo que dejan de hacer.")
vineta("**Huérfanos digitales:** ", "se les llama «nativos digitales», pero haber nacido rodeados de tecnología "
       "no significa saber usarla bien ni protegerse. Al dar por hecho que ya saben, nadie les ha educado en "
       "este entorno. Las familias, además, suelen controlar más que acompañar, y el 37 % de los adolescentes "
       "sabe saltarse los controles parentales (Save the Children, 2024).")

# ---------------------------------------------------------------- 4. posición
doc.add_heading("4. Nuestra posición como futuros profesores", 1)
p("Creemos que la escuela no puede ni ignorar las tecnologías digitales ni introducirlas sin criterio. "
  "Defendemos un uso pedagógico, crítico y limitado, basado en estas ideas:")
vineta("**Primacía de lo humano:** ", "se aprende mejor de una persona presente que de una pantalla, y el "
       "lenguaje y el pensamiento se desarrollan hablando, leyendo y debatiendo. La relación con el profesor y "
       "con los compañeros debe ser el centro del aula.")
vineta("**Tecnología con propósito:** ", "usarla solo cuando aporte algo que no se consiga de otra forma, con "
       "objetivos claros y tiempos acotados, evitando la multitarea.")
vineta("**Normas claras sobre el móvil:** ", "acordadas con el alumnado y explicadas, para proteger la atención "
       "y la convivencia en el centro.")
vineta("**Educación digital:** ", "precisamente porque no son «nativos digitales», hay que enseñarles a usar la "
       "tecnología de forma crítica y segura: privacidad, prevención del ciberacoso, respeto en las redes y "
       "educación afectivo-sexual e igualdad frente a la pornografía y los estereotipos.")
vineta("**Acompañar, no solo prohibir:** ", "coordinarnos con las familias, dar ejemplo como adultos y estar "
       "atentos a señales de malestar como la frustración, el aislamiento o el aburrimiento.")
p("Conocer cómo se desarrolla el adolescente nos permite entender por qué las tecnologías le afectan tanto y nos "
  "obliga a ofrecerle lo que la pantalla no puede darle: retos reales que le hagan sentirse capaz, relaciones "
  "humanas de calidad y criterio para moverse en el mundo digital con libertad y seguridad.")

# ---------------------------------------------------------------- referencias
doc.add_heading("Referencias", 1)
for ref in (
    "Casas Rivero, J. J. y Ceñal González-Fierro, M. J. (2005). Desarrollo del adolescente. Aspectos físicos, "
    "psicológicos y sociales. Pediatría Integral, 9(1), 20-24.",
    "Desmurget, M. (2020). Desarrollo: la inteligencia es la primera víctima. En La fábrica de cretinos "
    "digitales (pp. 256-297). Península.",
    "Save the Children España (2024). Un análisis sobre derechos de la infancia y la adolescencia y su "
    "protección en el entorno digital. Save the Children España.",
):
    par = doc.add_paragraph(ref)
    par.paragraph_format.left_indent = Cm(1)
    par.paragraph_format.first_line_indent = Cm(-1)

salida = AQUI / "trabajo_final.docx"
doc.save(salida)
print(salida)
