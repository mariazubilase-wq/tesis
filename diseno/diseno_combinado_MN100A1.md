# Diseño de clonaje — constructo combinado en `pMC.BESPX-MCS1` (MN100A-1)

**Constructo 3: reemplazo + silenciamiento en un solo minicírculo.**

Ruta por restricción pura, **usando los constructos 1 y 2 tal como están**. Sin
PCR, sin mutagénesis, sin síntesis. Dos pasos de clonaje.

---

## 1. Sobre los cambios sinónimos: ya no hacen falta

La especificidad de alelo de sh13 **está demostrada en el banco**. Eso cierra la
cuestión: el transgén silvestre no se toca y **el cDNA del constructo 1 entra en
el combinado sin modificar**.

Los cambios *wobble* quedan archivados como opción, no como requisito. Si alguna
vez quisieras hacerlos —por el margen extra o por tener una firma
transgén-específica para la ddPCR— la vía sería **mutagénesis dirigida, no
síntesis**: L157 `CTG`→`CTC` y A158 `GCT`→`GCC` están a 3 pb una de otra, así que
**una sola pareja de cebadores las introduce las dos a la vez** (Q5 SDM de NEB o
QuikChange: PCR sobre el plásmido entero, DpnI para destruir el molde metilado,
transformar). Un día de trabajo sobre el constructo 1 ya validado. Pero
insisto: **con tu dato de banco, esto no está en el camino crítico.**

---

## 2. El vector de destino y su MCS1

`pMC.BESPX-MCS1` (MN100A-1) es el parental **sin promotor**, que es justo lo que
hace falta: cada casete entra completo con el suyo.

```
         3      9      15     21     27     33     39     45
    CGACTAGTGAATTCAGATCTGATATCTCTAGAGTCGACCCATGGGGGCCC
      └SpeI─┘└EcoRI┘└BglII┘└EcoRV┘└XbaI─┘└SalI─┘└NcoI─┘└ApaI─┘
        CTAG   AATT   GATC   romo   CTAG   TCGA   CATG   GGCC
```

Dos cosas que la ficha del fabricante no dice:

- **Hay una NcoI (39–44) sin etiquetar.** Es la pieza clave del paso 2.
- **SpeI y XbaI dejan el mismo saliente `CTAG`** → son compatibles entre sí. Es
  lo que permite mover el casete A sin tocarlo.

### 2.1 Qué enzima sirve para qué

Comprobado contra los dos casetes reales (⚠ = corta dentro, inservible):

| Enzima del MCS1 | Casete A (EF1α→K10→polyA) | Casete B (H1→sh13) |
|---|---|---|
| SpeI | limpia | limpia |
| EcoRI | ⚠ 1× | ⚠ 1× |
| **BglII** | ⚠ **3×** | limpia |
| EcoRV | limpia | limpia |
| **XbaI** | ⚠ 1× | **limpia** |
| SalI | ⚠ 1× | limpia |
| **NcoI** | **limpia** | **limpia** |
| **ApaI** | limpia | ⚠ **1×** |

**De ahí sale el orden de los dos pasos, y no es negociable:**

> El casete A lleva **3 dianas BglII dentro**. Así que **B tiene que entrar
> primero**: en cuanto A esté dentro, BglII deja de servir para nada.
>
> Y el casete B lleva **una ApaI dentro**. Así que ApaI queda descartada para el
> paso 2, y el extremo 3' del casete A tiene que apoyarse en **NcoI**.

---

## 3. La ruta, en dos pasos

```
 MN100A-1        SpeI  EcoRI  BglII  EcoRV  XbaI  SalI  NcoI  ApaI
                               ↓(1)                ↓(2)  ↓(2)

 PASO 1  ── casete B (BglII/BglII, ~406 pb) ──→ BglII
 PASO 2  ── casete A (SpeI/NcoI,  ~3530 pb) ──→ XbaI + NcoI

 resultado:  [H1→sh13]  [EF1α→KRT10→WPRE→SV40pA]      en tándem
```

### 3.1 Paso 1 — el casete H1→sh13

**Del constructo 2, por digestión BglII.** Las dos dianas (2639 y 2988) lo
flanquean justo por fuera del H1 y del terminador.

| Fragmento | Tamaño | |
|---|---|---|
| 2639 → 2988 | **~406 pb** | ← **el casete**, H1 completo + horquilla + `TTTTT` |
| 2988 → 3579 | 591 pb | |
| 3579 → 2639 | ~5937 pb | |

Se separan de sobra en un gel al 1,5 %. Corta la banda de ~400 pb.

**El vector:** MN100A-1 digerido con **BglII** (corte único en el MCS1) y
**desfosforilado** (rSAP o CIP, 30 min a 37 °C, inactivar).

> **Aquí sí hay que desfosforilar, al revés que en el constructo 2.** Allí los
> oligos no llevaban fosfato y desfosforilar el vector habría matado la
> ligación. Aquí el inserto es un fragmento de restricción **con sus fosfatos**,
> y el vector tiene los dos extremos `GATC` compatibles entre sí: sin
> desfosforilar, se recirculariza solo y te llena la placa.

**Cribado:** la ligación no es direccional (mismo saliente a los dos lados), así
que hay que **mirar la orientación**. PCR con un cebador del vector + un cebador
del H1: sale banda en una orientación y no en la otra. Elige la que deja el
H1 transcribiendo **hacia la EcoRV/XbaI**, o sea en tándem con lo que vendrá
después (§3.3).

Al ligar `GATC` con `GATC` **se regeneran las dos BglII**. No importa: a partir
de aquí BglII ya no se usa.

### 3.2 Paso 2 — el casete EF1α→KRT10→WPRE→SV40polyA

**Del constructo 1, por digestión SpeI + NcoI.** Mirado sobre el mapa real:

| | Posición en MN502A-1 | Qué deja fuera |
|---|---|---|
| **SpeI** | 829 | corta 6 pb antes del EF1α (835). **Por detrás de attB (acaba en 816)** ✔ |
| **NcoI** | 2599 | corta 71 pb después del SV40 polyA (2528). **Por delante de attP (empieza en 2725)** ✔ |

> **Esta es la comprobación que no se puede saltar, y sale bien:** los dos cortes
> caen **dentro** de la ventana attB–attP del constructo 1. O sea que el
> fragmento **no arrastra ni attB ni attP**. Si arrastrara uno, el combinado
> tendría sitios ΦC31 de más y la recombinación daría productos que no quieres.
> (Lo mismo vale para el casete B: BglII 2639 y 2988 están dentro de
> attB 741–775 / attP 3616–3654 ✔.)

**El problema del gel, y cómo se resuelve.** SpeI corta 2× (815 y 829, los dos
pegados a attB) y NcoI 3× (2599, 2712, 3079). Los fragmentos que salen:

| Fragmento | Tamaño | |
|---|---|---|
| 829 → 2599 | **~3530 pb** | ← **el casete** |
| 3079 → 815 | ~3721 pb | ⚠ **sólo 191 pb de diferencia — no se separan** |
| 2712 → 3079 | 367 pb | |
| 2599 → 2712 | 113 pb | |
| 815 → 829 | 14 pb | |

**Añade una tercera enzima que parta el competidor sin tocar el casete.**
Comprobadas las cuatro candidatas; la mejor es **PciI** (`ACATGT`, única en
5161):

| Tercera enzima | Fragmentos >100 pb | Margen más estrecho |
|---|---|---|
| ninguna | 3721, 367, 113 | **191 pb** ❌ |
| FspI | 3389, 367, 332, 113 | **141 pb** ❌ *(peor: no la uses)* |
| **PciI** | 2082, 1639, 367, 113 | **1448 pb** ✅ |
| BspHI | 2359, 1362, 288, 113 | 1171 pb ✅ |
| BstZ17I | 2311, 1410, 367, 113 | 1219 pb ✅ |

Con PciI, la banda de ~3,5 kb queda sola y limpia. **Digestión triple
SpeI + NcoI + PciI**, corta la banda de ~3530 pb.

**El vector:** el intermedio del paso 1, digerido con **XbaI + NcoI**.

- `SpeI` (CTAG) del inserto liga con `XbaI` (CTAG) del vector ✔
- `NcoI` (CATG) con `NcoI` (CATG) ✔
- **Salientes distintos entre sí → clonaje direccional.** No hay que
  desfosforilar y el inserto no puede entrar invertido.
- La unión SpeI×XbaI genera un híbrido (`TCTAGT` = la `T` de `T^CTAGA` + `CTAG`
  + la `T` de `A^CTAGT`) **que no es ni SpeI ni XbaI**:
  las dos desaparecen. Es una ventaja, no un problema — no hay riesgo de
  re-corte, y además te da un diagnóstico (§4).

### 3.3 La disposición final

```
attB ─ SpeI ─ EcoRI ─[ H1 → sh13 → TTTTT ]─ EcoRV ─[ EF1α → KRT10 → WPRE → SV40pA ]─ ApaI ─ attP
                      └──── ~406 pb ────┘          └──────────── ~3530 pb ─────────┘
```

**Tándem, con el casete pol III por delante.** Es la disposición clásica de los
vectores duales: el terminador `TTTTT` corta la pol III en seco y la pol II
arranca limpia por detrás. Lo que **nunca** hay que montar es convergente (cola
con cola): las dos polimerasas chocarían de frente.

Inserto total ~3,95 kb. El minicírculo final será eso más lo que haya entre attB
y el MCS1 en MN100A-1 (§6).

---

## 4. Diagnóstico de los clones

| Qué | Cómo | Qué tiene que salir |
|---|---|---|
| Paso 1, orientación | PCR vector + H1 | banda sólo en la orientación buena |
| Paso 2, inserción | **XbaI** | **no corta** — la unión dejó `TCTAGT`, que no es diana |
| Paso 2, inserción | **BglII** | 3 bandas (las 3 dianas internas del casete A) |
| Estructura completa | **NcoI** | linealiza por el sitio del MCS1 + los internos del casete A |
| Lo definitivo | Secuenciación de las dos uniones y del casete B | — |

> **Secuencia el casete B entero cada vez.** El tallo de 21 pb es el punto donde
> *E. coli* delecciona, y una deleción parcial no se ve en ningún gel.

---

## 5. Antes de pedir nada: dos comprobaciones

Las dos son instantáneas y las dos pueden tumbar el plan:

**1. ¿El cDNA de KRT10 lleva SpeI o NcoI?** ✅ **Comprobado: no.** Ni `ACTAGT` ni
`CCATGG` en el CDS, así que la ruta SpeI + NcoI del paso 2 es válida. Si algún día
se cambia el cDNA (otro clon, KRT1), hay que volver a mirarlo:

```bash
python3 herramientas/lee_snapgene.py secuencias/pCMV6-KRT10.dna --dianas
```

Si en ese caso NcoI cortara dentro: la alternativa para el extremo 3' es **StuI** (única en
2689, romo) contra la **EcoRV** del MCS1 — pero eso obliga a invertir el orden de
los pasos, porque EcoRV queda por delante de XbaI. Si cortara SpeI: queda **ApaI
(2718)** para el 3' y hay que replantear el extremo 5'.

**2. ¿BglII, XbaI y NcoI son únicas en MN100A-1?** Ahora mismo sólo sé que lo son
*dentro del MCS1*, que son 50 pb. Hace falta el mapa completo (§6).

---

## 6. Lo único que me falta

> **El GenBank / SnapGene completo de `pMC.BESPX-MCS1` (MN100A-1).**

| Qué comprobaría | Para qué |
|---|---|
| Unicidad de **BglII, XbaI y NcoI** en todo el plásmido | Es el supuesto sobre el que descansan los dos pasos |
| Posición de **attB y attP** respecto al MCS1 | Confirmar que los dos casetes caen dentro del minicírculo |
| Tamaño total | Calcular el minicírculo final |

```bash
python3 herramientas/lee_snapgene.py secuencias/pMC.BESPX-MCS1.dna --dianas
```

---

## 7. Lo que NO hay que hacer

- ❌ **Meter el casete A antes que el B.** A lleva 3 BglII dentro; después de
  meterlo, B ya no tiene por dónde entrar.
- ❌ **Usar ApaI para el casete A.** Parece la pareja natural de SpeI, pero
  el casete B lleva una ApaI dentro.
- ❌ **Usar FspI como tercera enzima** (deja el competidor a 141 pb del casete).
- ❌ **Digerir sólo con SpeI + NcoI** sin la tercera: 3530 y 3721 pb no se
  separan, y te llevas el esqueleto del parental al gel.
- ❌ **Desfosforilar en el paso 2.** Es direccional; desfosforilar sólo resta.
- ❌ **Olvidar desfosforilar en el paso 1.** Ahí sí hace falta.
- ❌ Montar los casetes en convergente.
- ❌ Dar por hecho que BglII/XbaI/NcoI son únicas en MN100A-1 sin el mapa.
- ❌ Construir en ZYCY10P3S2T.
