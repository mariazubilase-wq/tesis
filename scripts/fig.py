import sys; sys.path.insert(0,'s')
import numpy as np, openpyxl, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from PIL import Image
from strips import straighten
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8,'axes.linewidth':0.6,
  'xtick.major.width':0.6,'ytick.major.width':0.6,'axes.spines.top':False,'axes.spines.right':False})
src=openpyxl.load_workbook('in.xlsx')['Hoja3']
sig={r[2]:float(str(r[3]).replace(',','.')) for r in src.iter_rows(min_row=2,values_only=True)}
def vals(t0,g0,extra=None):
    t=[sig.get(t0+i,extra) for i in range(9)]; g=[sig[g0+i] for i in range(9)]
    return np.array(t,float),np.array(g,float)
TCOL={'Ctrl':'#b4b2a9','CQ':'#2a78d6','MG132':'#eb6834','CQ+MG132':'#1baf7a'}
T1=['Ctrl','CQ+MG132','MG132']; T2=['Ctrl','CQ','CQ+MG132']
GEN=['KerCT','K1 WT','K1 M']
def strip_img(name):
    o,_=straighten(name,half=15)
    lo,hi=np.percentile(o,20),np.percentile(o,99.7)
    v=np.clip((o-lo)/(hi-lo),0,1)
    im=Image.fromarray((255*(1-v)).astype('uint8')).resize((560,o.shape[0]),Image.LANCZOS)
    return np.asarray(im)
fig=plt.figure(figsize=(7.2,8.6))
gs=GridSpec(3,2,figure=fig,height_ratios=[1.35,1,1],hspace=0.32,wspace=0.30,left=0.10,right=0.98,top=0.96,bottom=0.08)
def blot_panel(ss,treats,rows,letter):
    sub=ss.subgridspec(len(rows)+1,1,height_ratios=[1.3]+[1]*len(rows),hspace=0.12)
    ax=fig.add_subplot(sub[0]); ax.set_xlim(0,9); ax.set_ylim(0,3); ax.axis('off')
    cq=['+' if 'CQ' in t else '−' for t in treats]*3; mg=['+' if 'MG132' in t else '−' for t in treats]*3
    for i in range(9):
        ax.text(i+0.5,1.25,cq[i],ha='center',va='center',fontsize=9); ax.text(i+0.5,0.35,mg[i],ha='center',va='center',fontsize=9)
    ax.text(-0.1,1.25,'CQ',ha='right',va='center'); ax.text(-0.1,0.35,'MG132',ha='right',va='center')
    for k,gname in enumerate(GEN):
        ax.plot([k*3+0.15,k*3+2.85],[2.05,2.05],color='k',lw=0.7); ax.text(k*3+1.5,2.3,gname,ha='center',va='bottom',fontweight='bold')
    ax.text(-1.55,2.6,letter,fontsize=12,fontweight='bold',va='bottom')
    for j,(lab,name) in enumerate(rows):
        a=fig.add_subplot(sub[j+1]); a.imshow(strip_img(name),cmap='gray',vmin=0,vmax=255,aspect='auto',extent=(0,9,0,1))
        a.set_xticks([]); a.set_yticks([]); [s.set_visible(True) for s in a.spines.values()]
        a.set_ylabel(lab,rotation=0,ha='right',va='center',fontsize=8,labelpad=4)
def bars(ss,t,g,treats,title,lowflag,est=None,letter=''):
    ax=fig.add_subplot(ss)
    ax.text(-0.22,1.04,letter,transform=ax.transAxes,fontsize=12,fontweight='bold')
    rel=(t/g)/(t[0]/g[0]); x=np.array([i+ (i//3)*0.6 for i in range(9)])
    for i in range(9):
        tr=treats[i%3]
        ax.bar(x[i],rel[i],width=0.82,color=TCOL[tr],edgecolor='white',linewidth=1,zorder=2)
        mark='†' if lowflag[i] else ''
        if est is not None and i==est: mark+='*'
        if mark: ax.text(x[i],rel[i]+0.04*np.nanmax(rel),mark,ha='center',va='bottom',fontsize=9)
    ax.set_xticks([x[1],x[4],x[7]]); ax.set_xticklabels(GEN); ax.tick_params(axis='x',length=0)
    ax.set_ylabel(f'{title} / GAPDH\n(rel. a KerCT ctrl)'); ax.set_ylim(0,np.nanmax(rel)*1.2)
    ax.axhline(1,color='#888',lw=0.6,ls=(0,(3,3)),zorder=1)
    ax.grid(axis='y',color='#e6e5e0',lw=0.5,zorder=0); ax.set_axisbelow(True)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=TCOL[k],label=k) for k in treats],frameon=False,fontsize=7,loc='upper left',ncol=3,handlelength=1,columnspacing=1)
blot_panel(gs[0,0],T1,[('K1','M1_K1'),('GAPDH','M1_GAPDH'),('β-catenina','M2_bcat'),('GAPDH','M2_GAPDH')],'A')
blot_panel(gs[0,1],T2,[('K1','M3_K1'),('GAPDH','M3_GAPDH'),('p62','M4_p62'),('GAPDH','M4_GAPDH')],'B')
def low(g): return g/g.mean()<0.5
t,g=vals(1,10);  bars(gs[1,0],t,g,T1,'K1',low(g),letter='C')
t,g=vals(19,28); bars(gs[2,0],t,g,T1,'β-catenina',low(g),letter='E')
t,g=vals(37,46); bars(gs[1,1],t,g,T2,'K1',low(g),letter='D')
t,g=vals(55,63,None); t[8]=630; bars(gs[2,1],t,g,T2,'p62',low(g),est=8,letter='F')
fig.text(0.10,0.012,'n = 1. Señal (Image Studio, fondo restado) normalizada a GAPDH de la misma membrana y relativa a KerCT sin tratar.\n'
 '† GAPDH < 50 % de la media de la membrana (carga baja).   * Valor estimado desde la imagen (sin cuantificar en Image Studio).',fontsize=6.5,color='#444')
for ext in ('png','pdf','svg'):
    fig.savefig(f'/home/user/tesis/2026-11-18_figura_western.{ext}',dpi=300 if ext=='png' else None)
