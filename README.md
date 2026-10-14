# Tesis — terapia génica para ictiosis epidermolítica

Parte 1: silenciamiento alelo-específico del alelo mutante + reemplazo con copia
silvestre, entregado como **minicírculos**.

## Contenido

| Ruta | Qué es |
|---|---|
| `diseno/diseno_clonaje_KRT10_minicirculo.md` | **Constructo 1 — KRT10 en `pMC.EF1α-MCS-SV40polyA`** (MN502A-1). Decisiones, protocolo, controles. **Ver el §14**: los cebadores reales son de ensamblaje, no de restricción |
| `diseno/diseno_sh13_pSI_H1.md` | **Constructo 2 — sh13 en `pMC.SI-H1-MCS`** (MNSI500A-1). Oligos desmontados, protocolo, aviso sobre la posición del desapareamiento |
| `diseno/diseno_combinado_MN100A1.md` | **Constructo 3 — los dos casetes en `pMC.BESPX-MCS1`** (MN100A-1). Estrategia + los cambios *wobble* que hacen falta |
| `herramientas/disena_clonaje.py` | Calcula cebadores y tamaños a partir de los GenBank reales |
| `herramientas/lee_snapgene.py` | Lee ficheros `.dna` de SnapGene: secuencia, rasgos y mapa de dianas |
| `secuencias/` | Aquí van los ficheros de secuencia (ver `secuencias/LEEME.md`) |

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

**El clonaje de KRT10 se resolvió por ensamblaje por homología (In-Fusion /
NEBuilder), no por restricción**: los cebadores `ClonK10MC_F/R` llevan colas de
16 y 15 nt idénticas al vector y piden linearización con **BamHI sola**. Esto
sustituye a la pareja NheI-HF + BamHI-HF del §3.6 — ver **§14** del diseño.

Python 3.9+. Sin dependencias externas. No accede a internet.

## Los tres constructos previstos

| # | Constructo | Parental | Estado |
|---|---|---|---|
| 1 | **Reemplazo** — cDNA de KRT10 silvestre, bajo EF1α | MN502A-1 | Diseño cerrado; cebadores verificados |
| 2 | **Silenciamiento** — sh13 alelo-específico, bajo H1 | MNSI500A-1 | Diseño cerrado; oligos verificados |
| 3 | **Combinado** — los dos casetes, cada uno con su promotor | MN100A-1 | Estrategia; falta el mapa completo del parental |

Cada componente se valida por separado antes de construir el combinado.

> ⚠️ **El constructo 3 no puede llevar el cDNA silvestre nativo del constructo 1.**
> sh13 es alelo-específico pero su desapareamiento frente al silvestre está mal
> colocado, así que silenciaría también la copia de reemplazo. Hacen falta dos
> cambios *wobble* (L157 `CTG`→`CTC`, A158 `GCT`→`GCC`) que no alteran la
> proteína. El razonamiento completo está en `diseno_combinado_MN100A1.md` §1.
