import numpy as np
from PIL import Image
from scipy.ndimage import uniform_filter1d, map_coordinates
A=np.asarray(Image.open('x/xl/media/image1.png').convert('RGB')).astype(float)
R,G=A[:,:,0],A[:,:,1]
# name: (channel, x0, x1, y0, y1)  rough search window
S={'M1_K1':(R,75,640,145,195),'M1_GAPDH':(R,60,612,250,290),
   'M2_bcat':(G,725,1285,128,165),'M2_GAPDH':(R,715,1285,225,262),
   'M3_K1':(R,70,635,410,475),'M3_GAPDH':(R,60,622,560,600),
   'M4_p62':(G,705,1265,425,470),'M4_GAPDH':(R,700,1262,530,560)}
def straighten(name,half=16):
    ch,x0,x1,y0,y1=S[name]
    xs=np.arange(x0,x1); ys=[]
    for x in xs:
        prof=uniform_filter1d(ch[y0:y1,x],5); ys.append(y0+prof.argmax()); 
    ys=np.array(ys); w=ch[y0:y1,x0:x1].max(0)
    m=w>=np.percentile(w,50)                       # fit only columns with band
    p=np.polyfit(xs[m],ys[m],1)
    yc=np.polyval(p,xs)
    rr=np.arange(-half,half+1)
    Y=yc[None,:]+rr[:,None]; X=np.broadcast_to(xs,Y.shape)
    out=map_coordinates(ch,[Y,X],order=1)
    return out,p
if __name__=='__main__':
    for n in S:
        o,p=straighten(n); print(n,o.shape,'slope %.3f'%p[0],'max',o.max())
        Image.fromarray((255-np.clip(o,0,255)).astype('uint8')).resize((o.shape[1],o.shape[0]*2)).save(f'dbg_{n}.png')
