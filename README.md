# Tesis — terapia génica para ictiosis epidermolítica

Parte 1: silenciamiento alelo-específico del alelo mutante + reemplazo con copia
silvestre, entregado como **minicírculos**.

## Contenido

| Ruta | Qué es |
|---|---|
| `diseno/diseno_clonaje_KRT10_minicirculo.md` | **Diseño de clonaje de KRT10 en `pMC.EF1α-MCS-SV40polyA`.** Decisiones, protocolo, controles |
| `diseno/produccion_minicirculos.md` | **Producción del minicírculo en el laboratorio.** Cómo funciona la cepa ZYCY10P3S2T, protocolo, QC, costes y alternativas |
| `herramientas/disena_clonaje.py` | Calcula cebadores y tamaños a partir de los GenBank reales |
| `secuencias/` | Aquí van los dos ficheros de secuencia (ver `secuencias/LEEME.md`) |

## Uso rápido

```bash
cd herramientas
python3 disena_clonaje.py --autotest          # 29 comprobaciones internas

python3 disena_clonaje.py \
    --donante ../secuencias/pCMV6-KRT10.gb \
    --aceptor ../secuencias/pMC.EF1a-MCS-SV40polyA.gb \
    --salida  ../diseno/informe_KRT10.md
```

Python 3.9+. Sin dependencias externas. No accede a internet.

## Los tres constructos previstos

1. **Minicírculo de reemplazo** — cDNA de KRT10 (o KRT1) silvestre ← *este repositorio*
2. **Minicírculo con shRNA** contra el alelo mutante
3. **Minicírculo combinado** — ambos en un vector

Cada componente se valida por separado antes de construir el combinado.
