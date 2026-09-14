# Ficheros de secuencia

Deja aquí los dos ficheros. La herramienta acepta **GenBank** (`.gb`, `.gbk`),
**FASTA** (`.fa`, `.fasta`) o texto plano con sólo la secuencia.

## 1. Donante — `pCMV6-KRT10`

Tu clon de OriGene. **GenBank mucho mejor que FASTA**: con las anotaciones la
herramienta localiza el CDS directamente en vez de tener que deducirlo.

Comprueba de cuál de los dos se trata, porque cambia el recorte (ver §2.1 del
diseño):

- `RC204500` — pCMV6-Entry, **Myc-DDK en C-terminal, sin codón stop**
- `SC122561` — TrueClone sin etiqueta, con UTR y stop nativo

## 2. Aceptor — `pMC.EF1α-MCS-SV40polyA`

GenBank del vector parental de System Biosciences (número de catálogo a
confirmar: **MN502A-1**). Viene con el vector; si no lo tienes, pídeselo a
soporte técnico.

**Para que el análisis sea completo, el GenBank debe traer anotados:**

| Rasgo | Etiqueta que la herramienta busca | Para qué |
|---|---|---|
| attB (ΦC31) | `attB` | Acotar la región que acaba en el minicírculo |
| attP (ΦC31) | `attP` | Ídem |
| Promotor EF1α | `promoter`, `EF1`, `EF-1` | Límite 5' de la ventana de clonaje |
| SV40 polyA | `polyA`, `SV40` | Límite 3' de la ventana |
| I-SceI | `I-SceI` | Informativo |

Si faltan attB/attP, la herramienta intenta localizarlos por motivo ΦC31 y avisa.
Si no los encuentra, **no puede comprobar que el casete caiga dentro del
minicírculo**, que es la restricción arquitectónica principal: anótalos a mano en
SnapGene y vuelve a ejecutarla.

## Nombres sugeridos

```
secuencias/pCMV6-KRT10.gb
secuencias/pMC.EF1a-MCS-SV40polyA.gb
```

(Los ficheros de secuencia no están versionados en este repositorio.)
