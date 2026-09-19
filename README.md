# Tesis — terapia génica para ictiosis epidermolítica

Parte 1: silenciamiento alelo-específico del alelo mutante + reemplazo con copia
silvestre, entregado como **minicírculos**.

## Contenido

| Ruta | Qué es |
|---|---|
| `diseno/diseno_tres_constructos.md` | **Diseño cerrado de los tres constructos.** Mutación, blindaje, cebadores, horquillas, orden de trabajo |
| `herramientas/disena_tres_constructos.py` | Lo calcula y lo verifica todo desde el GenBank real |
| `diseno/diseno_clonaje_KRT10_minicirculo.md` | Diseño previo (sólo constructo 1, por restricción). Superado por el anterior |
| `herramientas/disena_clonaje.py` | Herramienta previa, genérica |
| `secuencias/pCMV6-KRT10.gb` | Donante real: RC204500 TrueORF, Myc-DDK, 6633 pb |
| `secuencias/constructos/` | Secuencias literales generadas: inserto, CDS endurecida, horquillas, cebadores |

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

**Estrategia vigente: corte único con BamHI-HF + In-Fusion.** Los dos brazos de
15 nt caen dentro del MCS conocido, así que el constructo 1 está cerrado sin
necesitar el GenBank del vector. Ver §3.1 de `diseno/diseno_tres_constructos.md`.

Python 3.9+. Sin dependencias externas. No accede a internet.

## Los tres constructos previstos

1. **Minicírculo de reemplazo** — ORF de KRT10 silvestre, **endurecida** con 5
   mutaciones silenciosas para que el shRNA no la toque. Proteína idéntica.
2. **Minicírculo con shRNA** contra p.Arg156Cys — `sh466-A` (siRNA 13) + `shSCR`
3. **Minicírculo combinado** — In-Fusion de 3 piezas, mismas piezas que 1 y 2

Cada componente se valida por separado antes de construir el combinado.

## La diana

`KRT10 c.466C>T` = **p.Arg156Cys**, en el motivo de iniciación de la hélice 1A.
El punto caliente de la ictiosis epidermolítica. Dominante negativo.

El siRNA 13 (`13F`/`13R`) tiene el nucleótido discriminante en la **posición 13
de la guía**. **Su especificidad de alelo está verificada experimentalmente y el
siRNA no se modifica.**
