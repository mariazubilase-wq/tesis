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

## 7. Qué acaba en el minicírculo, y por qué pregunto por attB/attP

Sí: **attB y attP son exactamente la frontera entre lo que se queda y lo que se
destruye.**

Al añadir arabinosa, la cepa ZYCY10P3S2T induce dos enzimas a la vez:

1. **Integrasa ΦC31** — recombina `attB × attP`. Eso **parte el plásmido parental
   en dos círculos**: el que llevaba todo lo que estaba *entre* attB y attP (el
   **minicírculo**, cerrado por un sitio híbrido `attR`), y el que llevaba el resto
   (el **esqueleto bacteriano**).
2. **Endonucleasa I-SceI** — corta el esqueleto por los **32 sitios I-SceI en
   tándem** que lleva, lo hace trizas, y las exonucleasas de la cepa lo degradan.

```
   parental                               inducción
   ┌──attB──[ lo tuyo ]──attP──┐          ───────────→   ○ minicírculo (attR)
   │                           │           ΦC31              lo tuyo
   └──[ KanR · ori · 32×I-SceI ]┘          I-SceI       ✂ esqueleto → degradado
```

**Regla única: lo que no esté entre attB y attP, no existe en el producto final.**

Medido sobre tus dos parentales:

| | total | **va al minicírculo** (attB→attP) | se destruye |
|---|---|---|---|
| MN502A-1 | 5985 pb | **1908 pb** | 4003 pb |
| MNSI500A-1 | 6877 pb | **2840 pb** | 3963 pb |

Y comprobado rasgo a rasgo: EF1α, WPRE, SV40 polyA y el sitio de clonaje del
constructo 1 caen dentro; H1, el sitio de clonaje y el polyA del constructo 2
también. Ninguno se pierde.

**Por eso hay que mirar el mapa de MN100A-1.** No es burocracia: si el MCS1
cayera fuera de su ventana attB–attP, los dos casetes se irían al esqueleto y el
minicírculo saldría vacío. Por diseño está dentro —es un vector de clonaje de
minicírculos— pero es el supuesto del que depende todo lo demás y no lo he visto.

> **La otra cara de lo mismo, y ésta ya está comprobada:** los cuatro cortes con
> los que saco los casetes (SpeI 829, NcoI 2599, BglII 2639, BglII 2988) caen
> todos **dentro** de la ventana de su donante. Así que **ningún fragmento
> arrastra un attB ni un attP de más**. Si lo hiciera, el combinado tendría tres
> sitios ΦC31 y la recombinación daría productos que no quieres.

---

## 8. ¿Está todo para que se expresen los dos?

**Sí. Los dos casetes son unidades de transcripción completas y no falta ningún
elemento.** Repasado pieza por pieza:

| Casete A — pol II | ¿está? |
|---|---|
| Promotor EF1α (546 pb) | ✔ el corte SpeI(829) cae 6 pb por delante de su inicio (835) |
| Kozak | ✔ `GCC**ATG**T`, purina en −3 |
| CDS de KRT10, sin etiqueta | ✔ |
| Dos codones de parada en tándem | ✔ `TGA TAA` |
| WPRE (estabiliza el mRNA) | ✔ 1429–1964, dentro del fragmento |
| SV40 polyA | ✔ 2397–2528, y NcoI(2599) corta 71 pb por detrás |

| Casete B — pol III | ¿está? |
|---|---|
| Promotor H1 completo | ✔ anotado 2712–2928; BglII(2639) deja 73 pb de margen |
| Horquilla sh13 | ✔ |
| Terminador pol III `TTTTT` | ✔ va en el propio oligo TOP |
| polyA / caperuza | **no hacen falta** — la pol III no los usa |

**Que MN100A-1 no tenga promotor ni polyA propios no es una carencia: es el
motivo de elegirlo.** Cada casete trae el suyo, y así no hay un promotor huérfano
del vector compitiendo ni leyendo hacia donde no debe.

### 8.1 Lo que sí conviene tener en la cabeza

Ninguna de estas tres cosas es un elemento que falte; son consecuencias de meter
dos unidades de transcripción en un círculo pequeño.

- **Interferencia transcripcional.** En un círculo de ~4 kb los dos casetes están
  cerca. Si la pol II lee más allá del SV40 polyA, da la vuelta y atraviesa el
  promotor H1 en sentido directo, lo que puede ocluirlo y bajar algo el shRNA. La
  disposición en tándem con el casete pol III **por delante** es la que menos
  expone a esto; la convergente sería la peor con diferencia. Es un efecto que se
  mide, no que se predice: sale en la capa 3 de la validación (§4).
- **No hay marcador ni reportero.** El minicírculo no lleva nada seleccionable —
  que es justamente la gracia del formato. Para los experimentos de validación,
  si necesitas saber qué células han recibido el constructo, la vía es
  **cotransfectar** un reportero aparte, no meterlo dentro.
- **El EF1α de este vector son 546 pb**, o sea la versión corta, sin el intrón 1.
  Funciona perfectamente y el WPRE compensa; sólo conviene saberlo si algún día
  comparas niveles con un EF1α de longitud completa.

---

## 9. Tamaño del minicírculo combinado

| | pb |
|---|---|
| Casete A (EF1α→KRT10→WPRE→SV40pA) | 3530 |
| Casete B (H1→sh13→TTTTT) | 406 |
| MCS1 que se pierde entre los cortes XbaI y NcoI | −12 |
| **Aporte neto de los insertos** | **3924** |
| Ventana attB–attP del MN100A-1 vacío | *pendiente del mapa* |

```
minicírculo = 3924 pb + (ventana attB–attP de MN100A-1 vacío, incluido el attR)
```

Como MN100A-1 no lleva promotor, ni WPRE, ni polyA —sólo los espaciadores de los
att y los 50 pb del MCS1—, esa ventana debería andar por los **150–500 pb**. Para
comparar: en MN502A-1 la ventana son 1908 pb, de los cuales 1262 son elementos
(EF1α, MCS, WPRE, polyA) y **646 pb son relleno**.

> ### Estimación: **~4,1–4,4 kb**
>
> Frente a los ~8–9 kb que mediría el plásmido parental combinado. El dato exacto
> sale en diez segundos en cuanto tenga el mapa.

Para hacerse una idea de lo que eso significa en transfección: el minicírculo de
sh13 solo (constructo 2) sería de ~2,9 kb y el de reemplazo solo (constructo 1)
de ~3,7 kb. El combinado, con **~4,2 kb**, sigue estando en el rango bueno —
bastante por debajo del umbral a partir del cual la eficiencia de transfección
empieza a caer de verdad.

---

## 10. Lo que NO hay que hacer

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
