# Tesis — terapia génica para ictiosis epidermolítica

Parte 1: silenciamiento alelo-específico del alelo mutante + reemplazo con copia
silvestre, entregado como **minicírculos**.

## Contenido

| Ruta | Qué es |
|---|---|
| `diseno/diseno_clonaje_KRT10_minicirculo.md` | **Diseño de clonaje de KRT10 en `pMC.EF1α-MCS-SV40polyA`.** Decisiones, protocolo, controles |
| `herramientas/disena_clonaje.py` | **Diseña**: calcula cebadores y tamaños a partir de los GenBank reales |
| `herramientas/simula_clonaje.py` | **Simula**: PCR + digestión + ligación, y escribe el `.dna` del plásmido resultante |
| `herramientas/valida_dna.py` | Comprueba un `.dna` con un lector independiente |
| `ejemplo/` | Salida de ejemplo con secuencias inventadas, para ver la pinta que tiene |
| `secuencias/` | Aquí van los dos ficheros de secuencia (ver `secuencias/LEEME.md`) |

## Uso rápido

```bash
cd herramientas
python3 disena_clonaje.py --autotest          # 29 comprobaciones internas

# Sólo con el donante y el MCS (sin el GenBank del parental)
python3 disena_clonaje.py \
    --donante ../secuencias/pCMV6-KRT10.gb \
    --mcs tctagagctagcgaattcgaatttaaatcggatccgcggccgcgtcga \
    --salida  ../diseno/informe_KRT10.md

# Con el mapa completo del parental (obligatorio antes de digerir)
python3 disena_clonaje.py \
    --donante ../secuencias/pCMV6-KRT10.gb \
    --aceptor ../secuencias/pMC.EF1a-MCS-SV40polyA.gb \
    --mcs tctagagctagcgaattcgaatttaaatcggatccgcggccgcgtcga \
    --salida  ../diseno/informe_KRT10.md
```

**Pareja elegida: NheI-HF (5') + BamHI-HF (3')**, las dos ya en el congelador.
Ver §3.6 del diseño.

## Generar el `.dna` del plásmido resultante

Sin licencia de SnapGene: el **Viewer es gratis y abre `.dna`**; lo que cuesta es
crear y editar. Así que el fichero se construye aquí y el visor sólo lo muestra.

```bash
cd herramientas

# 1. Ver que funciona, con secuencias inventadas (no toca nada tuyo)
python3 simula_clonaje.py --demo --salida ../ejemplo

# 2. El constructo de verdad, con los cebadores que dio disena_clonaje.py
python3 simula_clonaje.py \
    --aceptor ../secuencias/pMC.EF1a-MCS-SV40polyA.gb \
    --donante ../secuencias/pCMV6-KRT10.gb \
    --directo CACCACGCTAGCGCCACC... \
    --reverso CACCACGGATCCTCATTA... \
    --enzimas NheI-HF,BamHI-HF \
    --nombre  pMC.EF1a-KRT10-SV40polyA \
    --salida  ../resultados
```

Sale el `.dna`, el `.gb`, el GenBank del amplicón sin digerir y un informe con las
uniones, el ORF traducido y las digestiones diagnósticas. Si no le pasas los
cebadores, con `--auto` los calcula del CDS del donante.

### Ensamblado por homología (In-Fusion de Takara, Gibson, HiFi)

Es la vía que se ha seguido para **K10MC en MN502A1**: el vector se linealiza con
**una** enzima y los brazos de homología los llevan las colas 5' de los cebadores,
sin digerir el inserto y sin cicatriz en las uniones.

```bash
python3 simula_clonaje.py \
    --aceptor  ../secuencias/MN502A1.dna \
    --donante  ../secuencias/pCMV6-KRT10.dna \
    --directo  TTCGAATTTAAATCGGCCATGTCTGTTCGATACAGCTCAAGC \
    --reverso  ACGCGGCCGCGGATCTTATCAGTATCTTGGTCCCTTAGATGAAGACTCGCC \
    --infusion BamHI-HF \
    --nombre-orf KRT10 \
    --nombre   MN502A1-K10MC \
    --salida   ../resultados
```

Resultado: **7.746 pb**, ORF de **584 aa** sin stops internos, la diana BamHI
**destruida** (el cribado del protocolo) y el resto del plásmido idéntico al
parental, repeticiones I-SceI incluidas. Comprueba además que los brazos midan lo
que pide el protocolo (≥15 nt), que no aparezcan dos veces en el vector y que las
uniones reconstruyan la secuencia del parental sin cicatriz; por debajo de 8 nt de
solape se para, porque eso ya no es un brazo de homología.

Acepta de entrada `.gb`, `.gbk`, `.fa`, `.fasta`, **`.dna`** y texto plano, así que
si SBI te manda el vector como `.dna` de SnapGene vale directamente.

Se para con un error explicado —no escribe nada— si alguna diana no es única en el
vector o en el amplicón, si las dos enzimas dejan el mismo extremo, si los
cebadores están intercambiados o si una diana no se regenera en la unión.

Para confirmar que el `.dna` está bien formado sin abrir SnapGene:

```bash
python3 valida_dna.py ../resultados/pMC.EF1a-KRT10-SV40polyA.dna
```

Python 3.9+. Sin dependencias externas (Biopython es opcional, y sólo para
`valida_dna.py`). No accede a internet.

**Lo que esto no es:** una predicción, no un resultado. El clon se verifica
secuenciando; el informe te dice exactamente qué secuencia tiene que salir.

## Los tres constructos previstos

1. **Minicírculo de reemplazo** — cDNA de KRT10 (o KRT1) silvestre ← *este repositorio*
2. **Minicírculo con shRNA** contra el alelo mutante
3. **Minicírculo combinado** — ambos en un vector

Cada componente se valida por separado antes de construir el combinado.
