#!/usr/bin/env python3
"""
Diseno completo de los tres constructos de minicirculo para KRT10 c.466C>T.

  Constructo 1  pMC.EF1a-[KRT10 endurecido]-SV40pA      (reemplazo)
  Constructo 2  pMC.BESPX-[H1-shRNA]                    (silenciador)
  Constructo 3  los dos en un solo minicirculo

Sin dependencias externas. Verifica todo contra el GenBank real del donante.
"""
import re, sys, os, textwrap

AQUI = os.path.dirname(os.path.abspath(__file__))
GB   = os.path.join(AQUI, "..", "secuencias", "pCMV6-KRT10.gb")

# ---------------------------------------------------------------- utilidades
COMP = str.maketrans("ACGTUacgtuNn", "TGCAAtgcaaNn")
def rc(s):  return s.translate(COMP)[::-1]
def dna(s): return s.upper().replace("U", "T")

CODONES = {}
for i, aa in enumerate("KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF"):
    b = "ACGT"
    CODONES[b[i>>4] + b[(i>>2)&3] + b[i&3]] = aa

def traduce(s):
    return "".join(CODONES.get(s[i:i+3], "?") for i in range(0, len(s) - 2, 3))

def lee_genbank(ruta):
    txt = open(ruta).read()
    seq = "".join(re.findall(r"^\s*\d+\s+([acgtnACGTN\s]+)$", txt.split("ORIGIN")[1], re.M))
    return re.sub(r"\s", "", seq).upper()

def sitios(seq, patron, circular=True):
    d = seq + seq[:len(patron)-1] if circular else seq
    return [m.start() + 1 for m in re.finditer("(?=" + patron + ")", d)]

def linea(c="-", n=78): return c * n

# ---------------------------------------------------------------- 1. donante
P = lee_genbank(GB)
print(linea("="));  print("1. DONANTE  pCMV6-KRT10"); print(linea("="))
print(f"Longitud                  : {len(P)} pb")

ATG = 1029                       # anotado "ATG iniciador" 1029..1031
# la ORF de KRT10 (RC204500 TrueORF) NO lleva stop: continua hasta Myc-DDK
CDS_INI, CDS_LEN = ATG, 1752
CDS_FIN = CDS_INI + CDS_LEN - 1
cds = P[CDS_INI-1:CDS_FIN]
prot = traduce(cds)

print(f"ATG iniciador             : {CDS_INI}..{CDS_INI+2}  = {P[CDS_INI-1:CDS_INI+2]}")
print(f"ORF sin stop              : {CDS_INI}..{CDS_FIN}  ({CDS_LEN} nt = {CDS_LEN//3} codones)")
print(f"Proteina                  : {len(prot)} aa,  inicio {prot[:6]}...  final ...{prot[-6:]}")
print(f"Stops internos            : {prot.count('*')}   (debe ser 0)")
print(f"SgfI/AsiSI GCGATCGC       : {sitios(P,'GCGATCGC')}  (justo antes del ATG)")
print(f"MluI ACGCGT               : {sitios(P,'ACGCGT')}  (justo despues del ultimo codon)")
print(f"Base inmediatamente tras la ORF: {P[CDS_FIN:CDS_FIN+6]}  -> etiqueta Myc-DDK en fase")
assert prot.count("*") == 0 and prot.endswith("GPRY") and len(prot) == 584

# ---------------------------------------------------------------- 2. mutacion
print(); print(linea("=")); print("2. LA MUTACION  c.466C>T"); print(linea("="))
c466 = CDS_INI + 466 - 1
cod156_ini = CDS_INI + (156-1)*3
cod156 = P[cod156_ini-1:cod156_ini+2]
print(f"c.466 en el plasmido      : posicion {c466}, base '{P[c466-1]}'")
print(f"Codon 156 ({cod156_ini}..{cod156_ini+2}) : {cod156} = {CODONES[cod156]}")
print(f"Tras c.466C>T             : {'T'+cod156[1:]} = {CODONES['T'+cod156[1:]]}")
print(f"=> p.Arg156Cys (R156C).  Contexto proteico: ...{prot[148:166]}...")
print("   (motivo de iniciacion de la helice 1A: el punto caliente de la ictiosis epidermolitica)")
assert c466 == 1494 and cod156 == "CGC"

MUT = P[:c466-1] + "T" + P[c466:]          # plasmido con el alelo mutante

# ---------------------------------------------------------------- 3. siRNA
print(); print(linea("=")); print("3. EL siRNA QUE ME HAS DADO"); print(linea("="))
F = dna("aaugacugccuggcuuccuuu")
R = dna("aaaggaagccaggcagucauu")
print(f"13F (21 nt) : 5'-{F}-3'")
print(f"13R (21 nt) : 5'-{R}-3'")
print(f"Son complementarias exactas (duplex romo 21/21) : {rc(R) == F}")

# donde cae F sobre el mRNA mutante
pos = MUT.find(F[:19])
print(f"\n13F casa con el mRNA MUTANTE en {pos+1}..{pos+19} (19/19); sus 2 ultimas T son voladizo")
print(f"   mRNA mutante {pos+1}..{pos+21} : {MUT[pos:pos+21]}")
print(f"   13F                            : {F}")
print(f"   mRNA silvestre {pos+1}..{pos+21}: {P[pos:pos+21]}")
print("=> 13F es la hebra SENTIDO (pasajera); 13R es la hebra GUIA (antisentido).")

DIANA_INI, DIANA_FIN = pos+1, pos+21       # 1488..1508 = c.460..c.480
# posicion de la mutacion dentro de la guia, registro romo: R[j] aparea con mRNA (DIANA_FIN+1-j)
gp = DIANA_FIN + 1 - c466
print(f"\nVentana diana en el mRNA  : {DIANA_INI}..{DIANA_FIN}  (c.460..c.480)")
print(f"La mutacion cae en la posicion {gp} de la guia 13R (registro romo 21/21)")
print(f"   En registro 19+2 clasico seria la posicion {gp-2}  <- de ahi el '13' del nombre")
print("   AVISO: ni 13 ni 15 son el centro. Ago2 corta entre las posiciones 10 y 11 de la guia;")
print("   la discriminacion de 1 nt es maxima con el desapareamiento en 10-11 y en la semilla (2-8).")

# ---------------------------------------------------------------- 4. blindaje
print(); print(linea("=")); print("4. BLINDAJE DE LA COPIA DE REEMPLAZO (wobble)"); print(linea("="))
wt21 = P[DIANA_INI-1:DIANA_FIN]
# c.460 es el primer nt del codon 154 -> la ventana esta en fase
assert (466 - 1) % 3 == 0 and (DIANA_INI - CDS_INI) % 3 == 0
CAMBIOS = {1496:"G", 1499:"C", 1502:"C", 1503:"A", 1504:"G"}   # todos sinonimos
hard = list(P)
for p, b in CAMBIOS.items(): hard[p-1] = b
hard = "".join(hard)
hd21 = hard[DIANA_INI-1:DIANA_FIN]

print(f"silvestre  {DIANA_INI}..{DIANA_FIN} : {' '.join(wt21[i:i+3] for i in range(0,21,3))}")
print(f"endurecida               : {' '.join(hd21[i:i+3] for i in range(0,21,3))}")
print(f"aminoacidos silvestre    : {'   '.join(traduce(wt21))}")
print(f"aminoacidos endurecida   : {'   '.join(traduce(hd21))}")
print(f"proteina identica        : {traduce(wt21) == traduce(hd21)}")
cds_hard = hard[CDS_INI-1:CDS_FIN]
print(f"proteina COMPLETA identica: {traduce(cds_hard) == prot}")
assert traduce(cds_hard) == prot

def desapareamientos(guia, mrna21, recorta_voladizo=True):
    """Desapareamientos de la guia frente a una ventana de mRNA.

    Las 2 primeras bases de una guia 21-mero de este diseno son el voladizo 3'
    (aparean con la cola UU no templada de la hebra pasajera, no con el mRNA).
    La guia FUNCIONAL son sus 19 nt restantes; se numera 1..19 desde su 5'.
    """
    diana_rc = rc(mrna21)
    bruto = [j+1 for j in range(len(guia)) if guia[j] != diana_rc[j]]
    if not recorta_voladizo:
        return bruto
    return [j-2 for j in bruto if j > 2]

print(f"\nDesapareamientos de la guia 13R frente a:")
for nom, s in [("mRNA MUTANTE  (diana)", MUT[DIANA_INI-1:DIANA_FIN]),
               ("mRNA silvestre endogeno", wt21),
               ("transgen ENDURECIDO", hd21)]:
    mm = desapareamientos(R, s)
    print(f"   {nom:24s}: {len(mm)} desapareamiento(s) en posicion(es) {mm}")
print("   (semilla = posiciones 2-8; sitio de corte = 10-11)")

print("\nLos 5 cambios, uno a uno:")
for p in sorted(CAMBIOS):
    cod_i = CDS_INI + ((p - CDS_INI)//3)*3
    print(f"   {p}  {P[p-1]}>{CAMBIOS[p]}   codon {(cod_i-CDS_INI)//3+1:3d} "
          f"{P[cod_i-1:cod_i+2]}>{hard[cod_i-1:cod_i+2]} = {CODONES[P[cod_i-1:cod_i+2]]} "
          f"  guia pos {DIANA_FIN+1-p}")

# ---------------------------------------------------------------- 5. dianas
print(); print(linea("=")); print("5. DIANAS DE RESTRICCION DENTRO DE LA ORF ENDURECIDA"); print(linea("="))
ENZ = {"XbaI":"TCTAGA","NheI":"GCTAGC","EcoRI":"GAATTC","SwaI":"ATTTAAAT",
       "BamHI":"GGATCC","NotI":"GCGGCCGC","SalI":"GTCGAC","SpeI":"ACTAGT",
       "Bsp120I/PspOMI":"GGGCCC","AsiSI/SgfI":"GCGATCGC","MluI":"ACGCGT",
       "BbsI/BpiI":"GAAGAC","Esp3I/BsmBI":"CGTCTC","AgeI":"ACCGGT","HindIII":"AAGCTT"}
for nom, s in sorted(ENZ.items()):
    h = sitios(cds_hard, s, circular=False) + [-x for x in sitios(cds_hard, rc(s), circular=False)]
    h = sorted(set(abs(x) for x in h))
    print(f"   {nom:16s} {s:9s} : {'LIBRE' if not h else 'CORTA en ' + str(h)}")

print(); print(linea("=")); print("5b. DIFICULTAD DE SINTESIS / ESTABILIDAD EN E. coli"); print(linea("="))
for nom, i, j in [("cabeza rica en Gly  c.1-c.430", 1, 430),
                  ("dominio varilla     c.431-c.1290", 431, 1290),
                  ("cola rica en Gly    c.1291-c.1752", 1291, 1752)]:
    sub = cds_hard[i-1:j]
    g = 100*sum(sub.count(b) for b in "GC")/len(sub)
    rep = sum(1 for k in range(0, len(sub)-20) if sub.count(sub[k:k+20]) > 1)
    print(f"   {nom:32s} {len(sub):4d} nt  GC {g:4.1f}%  ventanas de 20 nt repetidas: {rep}")
print("   => la cola C-terminal es el problema: 71% GC y fuertemente repetitiva.")
print("      Es la region que un proveedor marcara como 'compleja' y la que recombina en E. coli.")

# ---------------------------------------------------------------- 6. MCS
print(); print(linea("=")); print("6. MCS DE pMC.EF1a-MCS-SV40polyA"); print(linea("="))
MCS = dna("tctagagctagcgaattcgaatttaaatcggatccgcggccgcgtcga")
print(f"MCS ({len(MCS)} nt) : {MCS}")
for nom, s in [("XbaI","TCTAGA"),("NheI","GCTAGC"),("EcoRI","GAATTC"),
               ("SwaI","ATTTAAAT"),("BamHI","GGATCC"),("NotI","GCGGCCGC")]:
    for p in sitios(MCS, s, circular=False):
        print(f"   {nom:6s} {s:9s} en {p}..{p+len(s)-1}")
print("   SalI GTCGAC : el MCS acaba en ...GTCGA; si la base 49 del vector es C, hay SalI")

BAM = MCS.find("GGATCC") + 1            # 1-based
corte = BAM                              # G^GATCC -> entre 30 y 31
ARM5 = MCS[corte-15:corte]               # 15 nt aguas arriba del corte
ARM3 = MCS[corte:corte+15]               # 15 nt aguas abajo del corte
print(f"\nCorte unico BamHI G^GATCC entre las posiciones {corte} y {corte+1} del MCS.")
print(f"   brazo In-Fusion 5' (15 nt, conocido) : {ARM5}")
print(f"   brazo In-Fusion 3' (15 nt, conocido) : {ARM3}")
print("   => LOS DOS BRAZOS CAEN DENTRO DEL MCS QUE ME HAS DADO: no hace falta el GenBank del vector.")

# ---------------------------------------------------------------- 7. constructo 1
print(); print(linea("=")); print("7. CONSTRUCTO 1 - inserto y cebadores"); print(linea("="))
KOZAK, STOPS = "GCCACC", "TGATAA"
inserto1 = KOZAK + cds_hard + STOPS
print(f"Inserto (Kozak + ORF endurecida + 2 stops) : {len(inserto1)} pb")
print(f"   empieza : {inserto1[:36]} ...")
print(f"   acaba   : ... {inserto1[-36:]}")
print(f"   traduccion desde el ATG : {traduce(inserto1[6:])[:5]}...{traduce(inserto1[6:])[-6:]}")

ANN_F, ANN_R = cds_hard[:24], rc(cds_hard[-21:])
cebF = ARM5 + KOZAK + ANN_F
cebR = rc(ARM3) + rc(STOPS) + ANN_R
def tm(s):
    g = sum(s.count(b) for b in "GC")
    return 64.9 + 41*(g - 16.4)/len(s)
print(f"\nKRT10-MC-F ({len(cebF)} nt)  Tm(zona de apareo) = {tm(ANN_F):.1f} C")
print(f"   5'-{ARM5} {KOZAK} {ANN_F}-3'")
print(f"KRT10-MC-R ({len(cebR)} nt)  Tm(zona de apareo) = {tm(ANN_R):.1f} C")
print(f"   5'-{rc(ARM3)} {rc(STOPS)} {ANN_R}-3'")
print(f"\nUnion final en el plasmido:")
print(f"   ...{MCS[:corte].lower()} | {KOZAK}ATG...TAC{STOPS} | {MCS[corte:].lower()}...")
print(f"   BamHI queda DESTRUIDO en el clon correcto -> digestion diagnostica gratis")

# ---------------------------------------------------------------- 8. mutagenesis
print(); print(linea("=")); print("8. MUTAGENESIS DIRIGIDA sobre pCMV6-KRT10 (plan B)"); print(linea("="))
SOL = hard[1494-1:1508]                  # bloque endurecido de 15 nt = solapamiento In-Fusion
annF = P[1509-1:1530]
annR = rc(P[1473-1:1493])
print(f"Solapamiento (bloque endurecido 1494..1508) : {SOL}")
print(f"   silvestre en esa ventana                 : {P[1493:1508]}")
print(f"KRT10-hard-F ({15+len(annF)} nt)  5'-{SOL} {annF}-3'   Tm={tm(annF):.1f} C")
print(f"KRT10-hard-R ({15+len(annR)} nt)  5'-{rc(SOL)} {annR}-3'   Tm={tm(annR):.1f} C")
print("PCR inversa sobre los 6633 pb del pCMV6 -> DpnI -> In-Fusion (recircula por el solapamiento).")
print("Un solo tubo instala los 5 cambios a la vez.")

# ---------------------------------------------------------------- 9. shRNA
print(); print(linea("=")); print("9. CONSTRUCTO 2 - horquillas"); print(linea("="))
LAZO, TERM = "CTCGAG", "TTTTT"

# diseno alternativo: mutacion en la posicion 10 de la guia
s10 = c466 - 10 + 1 - 0                  # ventana [s, s+20] con mut en guia pos 10 -> s = c466-(21-10)
S10_INI = c466 - (21 - 10)
S10_FIN = S10_INI + 20
sense10 = MUT[S10_INI-1:S10_FIN]
guia10  = rc(sense10)
assert desapareamientos(guia10, MUT[S10_INI-1:S10_FIN]) == []
mm10_wt = desapareamientos(guia10, P[S10_INI-1:S10_FIN])
mm10_hd = desapareamientos(guia10, hard[S10_INI-1:S10_FIN])

import random
PROHIBIDAS = ["GGATCC","GAATTC","ACCGGT","TCTAGA","GCTAGC","GCGGCCGC",
              "GTCGAC","ATTTAAAT","AAGCTT","ACTAGT","CGTCTC","GAAGAC"]
def limpia(h):
    d = h + rc(h)
    return not any(p in d for p in PROHIBIDAS) and "TTTT" not in h[:-5]
random.seed(0)
while True:
    lst = list(R[1:-2]); random.shuffle(lst)
    scr_guia = R[0] + "".join(lst) + R[-2:]
    cand = rc(scr_guia) + "CTCGAG" + scr_guia + "TTTTT"
    # sin coincidencia de semilla con KRT10 ni con la diana real
    semilla = scr_guia[2:9]
    if limpia(cand) and semilla not in P and rc(semilla) not in P:
        break

HORQUILLAS = [
 ("sh466-A  (estandar sentido-lazo-antisentido)", F,        R,        "tu siRNA exacto; formato pLKO/pSUPER"),
 ("sh466-B  (antisentido-lazo-sentido)",          R,        F,        "el 5' de la guia lo fija el +1 de Pol III"),
 ("sh466-P10 (mutacion en la posicion 10)",       sense10,  guia10,   f"ventana {S10_INI}..{S10_FIN}; desap. vs silvestre en {mm10_wt}"),
 ("shSCR    (control desordenado)",               rc(scr_guia), scr_guia, "mismo %GC, sin diana"),
]
for nom, a, b, nota in HORQUILLAS:
    h = a + LAZO + b + TERM
    print(f"\n{nom}")
    print(f"   {nota}")
    print(f"   horquilla ({len(h)} nt): 5'-{a} {LAZO} {b} {TERM}-3'")
    print(f"   tallo perfecto de 21 pb : {rc(a) == b}")
print(f"\nsh466-P10: desapareamientos de su guia frente al transgen endurecido : {mm10_hd}")
print(f"sh466-A/B: desapareamientos de 13R frente al transgen endurecido     : {desapareamientos(R, hd21)}")

print(); print(linea("-"))
print("OLIGOS PARA ANILLAR (formato pLKO.1: AgeI 5' / EcoRI 3')")
print("AgeI A^CCGGT y EcoRI G^AATTC estan LIBRES dentro de la ORF de KRT10;")
print("BbsI y Esp3I NO lo estan, asi que Golden Gate queda descartado para el constructo 3.")
print(linea("-"))
for nom, a, b, _ in HORQUILLAS:
    etiq = nom.split()[0]
    h = a + LAZO + b + TERM
    print(f"\n{etiq}")
    print(f"   superior 5'-CCGG {h} -3'")
    print(f"   inferior 5'-AATT {rc(h)} -3'")

# ---------------------------------------------------------------- 10. ficheros
salida = os.path.join(AQUI, "..", "secuencias", "constructos")
os.makedirs(salida, exist_ok=True)
with open(os.path.join(salida, "inserto_C1_KRT10_endurecido.fa"), "w") as fh:
    fh.write(">inserto_C1_Kozak-KRT10hard-TGATAA  %d pb\n" % len(inserto1))
    fh.write("\n".join(textwrap.wrap(inserto1, 60)) + "\n")
with open(os.path.join(salida, "inserto_C1_con_brazos_InFusion.fa"), "w") as fh:
    frag = ARM5 + inserto1 + ARM3
    fh.write(">fragmento_sintetico_C1_con_brazos_15nt  %d pb\n" % len(frag))
    fh.write("\n".join(textwrap.wrap(frag, 60)) + "\n")
with open(os.path.join(salida, "cds_KRT10_endurecido.fa"), "w") as fh:
    fh.write(">KRT10_CDS_endurecido_1752nt_584aa_proteina_identica_a_P13645\n")
    fh.write("\n".join(textwrap.wrap(cds_hard, 60)) + "\n")
with open(os.path.join(salida, "horquillas.fa"), "w") as fh:
    for nom, a, b, _ in HORQUILLAS:
        etiq = nom.split()[0]
        fh.write(">%s_horquilla\n%s\n" % (etiq, a + LAZO + b + TERM))
        fh.write(">%s_oligo_superior\n%s\n" % (etiq, a + LAZO + b + TERM))
        fh.write(">%s_oligo_inferior\n%s\n" % (etiq, rc(a + LAZO + b + TERM)))
with open(os.path.join(salida, "cebadores.txt"), "w") as fh:
    fh.write("KRT10-MC-F\t%s\n" % cebF)
    fh.write("KRT10-MC-R\t%s\n" % cebR)
    fh.write("KRT10-hard-F\t%s\n" % (SOL + annF))
    fh.write("KRT10-hard-R\t%s\n" % (rc(SOL) + annR))
print(); print(linea("=")); print("FICHEROS ESCRITOS en secuencias/constructos/"); print(linea("="))
for f in sorted(os.listdir(salida)): print("   " + f)
