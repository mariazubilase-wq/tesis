import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, Reference
from openpyxl.comments import Comment
src=openpyxl.load_workbook('in.xlsx')['Hoja3']
rows=[[c.value for c in r] for r in src.iter_rows(min_row=2)]
def num(x): return float(str(x).replace(',','.')) if isinstance(x,str) else x
wb=openpyxl.Workbook(); d=wb.active; d.title='Datos'
F=Font(name='Arial'); B=Font(name='Arial',bold=True)
hdr=['ROI','Canal','Señal (bkg restado)','Total','Área','Bkgnd','Asignación']
groups=[(1,9,'M4 · p62'),(10,18,'M4 · GAPDH'),(19,27,'M3 · K1'),(28,36,'M3 · GAPDH'),
        (37,45,'M2 · β-catenina'),(46,54,'M2 · GAPDH'),(55,62,'M1 · K1 (carril 9 sin cuantificar)'),(63,71,'M1 · GAPDH')]
def asg(n):
    for a,b,l in groups:
        if a<=n<=b: return f'{l} · carril {n-a+1}'
d.append(hdr)
for r in rows:
    n=r[2]; d.append([n,r[1],num(r[3]),num(r[4]),num(r[5]),num(r[6]),asg(n)])
for row in d.iter_rows():
    for c in row: c.font=F
for c in d[1]: c.font=B
for col,w in zip('ABCDEFG',[6,14,18,10,8,9,34]): d.column_dimensions[col].width=w
d['I1']='Señal exportada del Image Studio (Total − Bkgnd×Área). Asignación ROI→membrana según el número escrito en cada membrana en la imagen: arriba izq. = 4, arriba dcha. = 3, abajo izq. = 2, abajo dcha. = 1.'
d['I1'].font=Font(name='Arial',italic=True)

L12=['KerCT','KerCT CQ+MG132','KerCT MG132','K1 WT','K1 WT CQ+MG132','K1 WT MG132','K1 M','K1 M CQ+MG132','K1 M MG132']
L34=['KerCT','KerCT CQ','KerCT CQ+MG132','K1 WT','K1 WT CQ','K1 WT CQ+MG132','K1 M','K1 M CQ','K1 M CQ+MG132']
mem=[('Membrana 1 · K1 / GAPDH','K1',55,63,L12),('Membrana 2 · β-catenina / GAPDH','β-catenina',37,46,L12),
     ('Membrana 3 · K1 / GAPDH','K1',19,28,L34),('Membrana 4 · p62 / GAPDH','p62',1,10,L34)]
a=wb.create_sheet('Análisis')
head=PatternFill('solid',fgColor='DDEBF7'); warn=PatternFill('solid',fgColor='FCE4D6')
thin=Side(style='thin',color='999999')
r0=1
a.cell(r0,1,'Cuantificación western 2026-11-18 · normalizado a GAPDH').font=Font(name='Arial',bold=True,size=13)
a.cell(r0+1,1,'n = 1 por condición (sin estadística). "Rel. a su control" = ratio / ratio del no tratado del mismo genotipo. Naranja: GAPDH < 50 % de la media de la membrana (carga baja, ratio poco fiable).').font=Font(name='Arial',italic=True,size=9)
r=r0+3
for title,tgt,t0,g0,labels in mem:
    a.cell(r,1,title).font=Font(name='Arial',bold=True,size=11); r+=1
    H=['Carril','Muestra',f'{tgt} (señal)','GAPDH (señal)','GAPDH / media','Ratio diana/GAPDH','Rel. a KerCT','Rel. a su control']
    for j,h in enumerate(H,1):
        c=a.cell(r,j,h); c.font=B; c.fill=head; c.alignment=Alignment(wrap_text=True,horizontal='center'); c.border=Border(bottom=thin)
    first=r+1; last=r+9
    for i in range(9):
        rr=first+i; ctrl=first+(i//3)*3
        tref=630 if (t0==55 and i==8) else f'=Datos!C{t0+i+1}'
        vals=[i+1,labels[i],tref,f'=Datos!C{g0+i+1}',
              f'=D{rr}/AVERAGE($D${first}:$D${last})',f'=IF(C{rr}="","",C{rr}/D{rr})',f'=IF(C{rr}="","",F{rr}/$F${first})',f'=IF(C{rr}="","",F{rr}/$F${ctrl})']
        for j,v in enumerate(vals,1):
            c=a.cell(rr,j,v); c.font=F
            if tref==630 and j==3:
                c.fill=PatternFill('solid',fgColor='FFFF00'); c.font=Font(name='Arial',color='0000FF')
                c.comment=Comment('ESTIMADO, no medido en Image Studio. Banda medida sobre la imagen PNG incrustada (canal verde) y calibrada con los carriles 1-8 de Image Studio (r = 0,93; rango 620-650). Sustituir por el valor de Image Studio cuando se cuantifique.','Análisis')
            c.number_format={3:'#,##0',4:'#,##0',5:'0%',6:'0.000',7:'0.00',8:'0.00'}.get(j,'General')
    from openpyxl.formatting.rule import FormulaRule
    a.conditional_formatting.add(f'A{first}:H{last}',FormulaRule(formula=[f'$E{first}<0.5'],fill=warn))
    ch=BarChart(); ch.type='col'; ch.title=f'{tgt} / GAPDH (rel. a KerCT)'; ch.roundedCorners=False
    ch.add_data(Reference(a,min_col=7,min_row=first-1,max_row=last),titles_from_data=True)
    ch.set_categories(Reference(a,min_col=2,min_row=first,max_row=last))
    ch.legend=None; ch.title.overlay=False if hasattr(ch.title,'overlay') else None
    ch.x_axis.delete=False; ch.y_axis.delete=False; ch.height=7; ch.width=16
    a.add_chart(ch,f'J{r-1}')
    r=last+6
a.cell(r,1,'Carril 9 de K1 en la membrana 1 (K1 M MG132): valor ESTIMADO (~630) a partir de la imagen, no de Image Studio. Celda amarilla: sustituir por el valor real.').font=Font(name='Arial',bold=True,color='C00000')
for col,w in zip('ABCDEFGH',[7,18,13,13,10,12,11,12]): a.column_dimensions[col].width=w
from openpyxl.drawing.image import Image as XI
im=wb.create_sheet('Imágenes')
im['A1']='Imágenes del Excel original (recuadros de Image Studio con número de ROI y señal).'; im['A1'].font=B
x1=XI('x/xl/media/image2.png'); x1.width,x1.height=1748*0.6,725*0.6; im.add_image(x1,'A3')
x2=XI('x/xl/media/image1.png'); x2.width,x2.height=1311*0.8,678*0.8; im.add_image(x2,'A28')
wb.move_sheet('Análisis',-2)
wb.save('/home/user/tesis/2026-11-18_cuantif_analisis.xlsx')
