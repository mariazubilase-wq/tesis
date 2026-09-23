# Tesis — terapia génica para ictiosis epidermolítica

Parte 1: silenciamiento alelo-específico del alelo mutante + reemplazo con copia
silvestre, entregado como **minicírculos**.

## Contenido

| Ruta | Qué es |
|---|---|
| `diseno/diseno_clonaje_KRT10_minicirculo.md` | **Diseño de clonaje de KRT10 en `pMC.EF1α-MCS-SV40polyA`.** Decisiones, protocolo, controles |
| `herramientas/disena_clonaje.py` | Calcula cebadores y tamaños a partir de los GenBank reales |
| `herramientas/verifica_oligos.py` | **Comprueba oligos ya escritos** contra el fichero real: brazos, apareo, Tm, pauta, Kozak, dianas |
| `diseno/verificacion_ClonK10MC.md` | Verificación de la pareja `ClonK10MC_F`/`_R` (BamHI + In-Fusion) |
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

### Comprobar unos oligos que ya tienes escritos

```bash
python3 herramientas/verifica_oligos.py --autotest      # 13 comprobaciones internas

python3 herramientas/verifica_oligos.py \
    --donante secuencias/pCMV6-KRT10.dna \
    --mcs tctagagctagcgaattcgaatttaaatcggatccgcggccgcgtcga \
    --enzima BamHI-HF \
    --f TTCGAATTTAAATCGGCCATGTCTGTTCGATACAGCTCAAGC \
    --r ACGCGGCCGCGGATCTTATCAGTATCTTGGTCCCTTAGATGAAGACTCGCC
```

Sale con código 0 si no hay fallos. Añade `--aceptor` cuando tengas el GenBank
del parental para comprobar que la enzima corta una sola vez en todo el vector.

Las dos herramientas leen **GenBank, FASTA y `.dna` de SnapGene** (con sus
rasgos anotados).

**Pareja elegida: NheI-HF (5') + BamHI-HF (3')**, las dos ya en el congelador.
Ver §3.6 del diseño.

Python 3.9+. Sin dependencias externas. No accede a internet.

## Los tres constructos previstos

1. **Minicírculo de reemplazo** — cDNA de KRT10 (o KRT1) silvestre ← *este repositorio*
2. **Minicírculo con shRNA** contra el alelo mutante
3. **Minicírculo combinado** — ambos en un vector

Cada componente se valida por separado antes de construir el combinado.
