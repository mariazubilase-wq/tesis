# Ejemplo ejecutable (secuencias **inventadas**)

Estos cuatro ficheros los ha generado `herramientas/simula_clonaje.py --demo`.
Sirven para dos cosas: comprobar que el `.dna` abre bien en tu SnapGene Viewer, y
ver qué forma tiene la salida antes de gastar los ficheros de verdad.

| Fichero | Qué es |
|---|---|
| `pMC.EF1a-GEN_DEMO-SV40polyA.dna` | plásmido resultante, formato SnapGene |
| `pMC.EF1a-GEN_DEMO-SV40polyA.gb` | el mismo, en GenBank |
| `pMC.EF1a-GEN_DEMO-SV40polyA_amplicon.gb` | el amplicón de PCR **antes** de digerir |
| `pMC.EF1a-GEN_DEMO-SV40polyA_informe.md` | uniones, Tm, ORF, digestiones |

> ⚠️ **El vector y el gen son sintéticos.** El vector lleva un MCS real y attB/attP
> de ΦC31 de referencia, pero el resto es relleno aleatorio: no es
> `pMC.EF1α-MCS-SV40polyA` ni KRT10. No se usa para nada del banco. Para el
> constructo de verdad hacen falta los dos GenBank en `secuencias/`
> (ver `secuencias/LEEME.md`).

Para regenerarlos:

```bash
cd herramientas
python3 simula_clonaje.py --demo --salida ../ejemplo
```
