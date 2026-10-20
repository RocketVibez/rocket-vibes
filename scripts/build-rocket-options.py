import numpy as np, math
from PIL import Image, ImageDraw, ImageFilter, ImageFont
ROOT='/workspace/rocket-vibes'
orig=np.asarray(Image.open(f'{ROOT}/logo-banner.png').convert('RGB')).astype(np.float32)/255
H,W,_=orig.shape

def blur(a,s):
    # 3x box blur ~ gaussian, a: HxW or HxWxC float
    if s<=0: return a
    r=max(1,int(round(s*0.87)))
    out=a.copy()
    for _ in range(3):
        for ax in (0,1):
            p=[(0,0)]*out.ndim; p[ax]=(r+1,r)
            c=np.cumsum(np.pad(out,p,mode='edge'),axis=ax)
            sl1=[slice(None)]*out.ndim; sl0=[slice(None)]*out.ndim
            sl1[ax]=slice(2*r+1,None); sl0[ax]=slice(0,-(2*r+1))
            out=(c[tuple(sl1)]-c[tuple(sl0)])/(2*r+1)
    return out

# ---------- region polygon (keeps clear of 't', 'V' and the shoe) ----------
P=[(418,268),(447,268),(447,300),(436,306),(435,350),(428,372),(414,380),(404,402),(352,402),
   (355,385),(363,370),(366,350),(372,336),(388,330),(400,325),(406,312),(411,298),(414,282)]
pm=Image.new('L',(W,H),0); ImageDraw.Draw(pm).polygon(P,fill=255)
poly=np.asarray(pm)>0
R,G,B=orig[...,0],orig[...,1],orig[...,2]
shoe=(R>0.25)&(B<R*0.4)&(G<R*0.9)          # orange/red/yellow figure pixels
fill=poly&~shoe                            # pixels to reconstruct
# ---------- clean plate: diffusion inpaint from boundary, shoe not used as source ----------
plate=orig.copy()
src=(~poly)&(~shoe)
valid=(~fill)&src | fill
cur=orig.copy(); cur[fill]=0.02
wv=valid.astype(np.float32)
for it in range(1500):
    acc=np.zeros_like(cur); cnt=np.zeros((H,W),np.float32)
    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
        acc+=np.roll(np.roll(cur*wv[...,None],dy,0),dx,1)
        cnt+=np.roll(np.roll(wv,dy,0),dx,1)
    new=acc/np.maximum(cnt,1e-6)[...,None]
    cur[fill]=new[fill]
plate[fill]=cur[fill]
# subtle background grain so the fill isn't plastic-smooth
rng=np.random.default_rng(7)
plate[fill]+=(rng.normal(0,0.004,(H,W,1))*np.ones(3))[fill]
plate=np.clip(plate,0,1)

# ---------- composite alpha: 1 inside polygon, feathered inward, exactly 0 outside ----------
er=pm.filter(ImageFilter.MinFilter(7))
alpha=np.asarray(er.filter(ImageFilter.GaussianBlur(2.5))).astype(np.float32)/255
alpha=np.where(poly,np.maximum(alpha,fill*0),0)  # zero outside polygon
alpha[fill & (alpha<1)] = alpha[fill & (alpha<1)]  # (feather band lies in background/glow)

# ---------- rocket rendering in local coords ----------
SS=4
NOZ=(397.0,351.0); ANG=math.radians(28.0)   # tilt up-right like the original
ca,sa=math.cos(ANG),math.sin(ANG)
def L2G(u,v):  # local (u right, v down; nozzle at 0, nose at negative v) -> hi-res pixel
    u=u*SX
    x=NOZ[0]+u*ca - v*sa; y=NOZ[1]+u*sa + v*ca
    return (x*SS,y*SS)
HW,HH=W*SS,H*SS
ys,xs=np.mgrid[0:HH,0:HW].astype(np.float32)
gx=(xs+0.5)/SS-NOZ[0]; gy=(ys+0.5)/SS-NOZ[1]
U0=gx*ca+gy*sa; V=-gx*sa+gy*ca; SX=1.0; U=U0
def pmask(pts):
    im=Image.new('L',(HW,HH),0); ImageDraw.Draw(im).polygon([L2G(*p) for p in pts],fill=255)
    return np.asarray(im).astype(np.float32)/255
def lmask(pts,w,closed=True):
    im=Image.new('L',(HW,HH),0); d=ImageDraw.Draw(im)
    q=[L2G(*p) for p in pts]+([L2G(*pts[0])] if closed else [])
    d.line(q,fill=255,width=max(1,int(w*SS)),joint='curve')
    return np.asarray(im).astype(np.float32)/255
def emask(cu,cv,ru,rv):
    return (((U-cu)/ru)**2+((V-cv)/rv)**2<=1).astype(np.float32)
C=lambda *c: np.array(c,np.float32)/255
PINK=C(255,48,214); MAG=C(225,25,170); PURP=C(150,45,225); DPURP=C(70,18,120); VIOL=C(110,40,200)
CYAN=C(25,211,255); BLUE=C(30,120,255); WHITE=C(235,250,255); ICE=C(170,245,255)

class Layer:
    def __init__(s): s.col=np.zeros((HH,HW,3),np.float32); s.A=np.zeros((HH,HW),np.float32); s.glow=np.zeros((HH,HW,3),np.float32)
    def paint(s,m,color):  # opaque fill (color may be HxWx3)
        m=m[...,None]; s.col=s.col*(1-m)+color*m; s.A=np.maximum(s.A,m[...,0])
    def emit(s,m,color,k=1.0): s.glow+=m[...,None]*color*k
    def halo(s,m,color,sig,k): s.glow+=blur(m,sig*SS)[...,None]*color*k
def shade(base,hi,lo,u0,u1):
    t=np.clip((U-u0)/(u1-u0+1e-6),0,1)[...,None]
    return np.where(t<0.35, hi*(1-t/0.35)+base*(t/0.35), base*(1-(t-0.35)/0.65)+lo*((t-0.35)/0.65))
def mirror(pts): return [(-u,v) for u,v in reversed(pts)]

def flame_plume(Ly,length,w0,core=True,k=1.0):
    t=np.clip(V/length,0,1)
    width=w0*(1-t)**0.8+0.3
    m=((V>=-1)&(V<=length)&(np.abs(U)<=width)).astype(np.float32)
    fade=np.clip(1-V/length,0,1)**1.3
    Ly.emit(m*fade,CYAN,1.0*k); Ly.halo(m*fade,BLUE,2.5,1.2*k); Ly.halo(m*fade,CYAN,6,0.6*k)
    if core:
        cm=((V>=-1)&(V<=length*0.45)&(np.abs(U)<=width*0.4)).astype(np.float32)*np.clip(1-V/(length*0.45),0,1)
        Ly.emit(blur(cm,1*SS),WHITE,1.1*k)

def rocket_a():   # retro 1950s finned
    Ly=Layer()
    prof=[(0,-80),(2.5,-72),(4.6,-60),(6.2,-46),(6.8,-34),(6.4,-20),(5.4,-10),(4.6,-6)]
    body=prof+mirror(prof)
    lf=[(-5.8,-30),(-11,-22),(-15.5,-10),(-17,2),(-14.5,-1),(-10.5,-6),(-5,-9)]
    rf=[(-u,v) for u,v in lf]
    for f in (lf,rf):
        Ly.paint(pmask(f),shade(PURP,PINK,DPURP,-17,17)); Ly.emit(lmask(f,0.9),PINK,1.0); Ly.halo(lmask(f,1.2),PINK,2.5,0.9)
    Ly.paint(pmask(body),shade(VIOL,PINK,DPURP,-7,7))
    # chrome bands
    for v in (-9,-7):
        Ly.emit(((np.abs(V-v)<0.5)&(np.abs(U)<5.6)).astype(np.float32),C(255,190,250),0.8)
    nozzle=[(-4.2,-6),(4.2,-6),(3.2,-1),(-3.2,-1)]
    Ly.paint(pmask(nozzle),C(120,60,170)); Ly.emit(lmask(nozzle,0.6),PINK,0.7)
    # center fin (edge-on)
    cf=[(-1.1,-24),(1.1,-24),(1.4,1),(-1.4,1)]
    Ly.paint(pmask(cf),shade(PURP,PINK,DPURP,-1.5,1.5)); Ly.emit(lmask(cf,0.6),PINK,0.9)
    # specular streak
    Ly.emit(blur(((np.abs(U+3)<0.7)&(V>-62)&(V<-22)).astype(np.float32),0.8*SS),C(255,200,250),0.6)
    Ly.emit(lmask(body,0.9),PINK,1.0); Ly.halo(lmask(body,1.5),PINK,3,1.0); Ly.halo(pmask(body),MAG,7,0.35)
    flame_plume(Ly,62,4.0)
    return Ly

def rocket_b():   # chunky cartoon with porthole
    Ly=Layer()
    prof=[(0,-70),(4.5,-67),(8.5,-59),(11,-48),(12,-36),(11.8,-24),(10.8,-14),(9.5,-8)]
    body=prof+mirror(prof)
    lf=[(-10.5,-30),(-16,-24),(-20,-14),(-20.5,-3),(-17.5,-5),(-14,-8),(-9.5,-10)]
    rf=[(-u,v) for u,v in lf]
    for f in (lf,rf):
        Ly.paint(pmask(f),shade(PURP,C(210,90,255),DPURP,-20,20)); Ly.emit(lmask(f,1.0),PINK,1.0); Ly.halo(lmask(f,1.4),PINK,2.5,0.9)
    bm=pmask(body)
    Ly.paint(bm,shade(MAG,C(255,120,230),C(150,20,120),-12,12))
    nose=pmask([(0,-70),(4.5,-67),(8.5,-59),(10.2,-52),(-10.2,-52),(-8.5,-59),(-4.5,-67)])
    Ly.paint(nose*bm,shade(PURP,C(200,110,255),DPURP,-10,10))
    base=((V>-14)&(V<-8))*bm
    Ly.paint(base.astype(np.float32),shade(PURP,C(200,110,255),DPURP,-11,11))
    nozzle=[(-6,-8),(6,-8),(4.8,-3),(-4.8,-3)]
    Ly.paint(pmask(nozzle),C(110,40,170)); Ly.emit(lmask(nozzle,0.7),PINK,0.7)
    # porthole
    Ly.paint(emask(0,-34,6.8,6.8),C(120,35,190)); Ly.emit(((((U)**2+(V+34)**2)**0.5>5.9)&(((U)**2+(V+34)**2)**0.5<6.8)).astype(np.float32),PINK,0.8)
    glass=emask(0,-34,4.7,4.7)
    Ly.paint(glass,shade(CYAN,C(200,255,255),C(0,120,200),-4.7,4.7)); Ly.halo(glass,CYAN,2,0.7)
    Ly.emit(blur(emask(-1.8,-36,1.3,1.0),0.5*SS),WHITE,1.0)
    Ly.emit(blur(((np.abs(U+7)<0.9)&(V>-52)&(V<-18)).astype(np.float32),0.8*SS),C(255,200,245),0.5)
    Ly.emit(lmask(body,1.0),PINK,1.0); Ly.halo(lmask(body,1.6),PINK,3,1.0); Ly.halo(bm,MAG,7,0.35)
    # chunky teardrop flame
    t=np.clip(V/46,0,1); width=np.where(V<12,4.8+V*0.15,(6.6)*np.clip(1-(V-12)/34,0,1)**0.9)
    m=((V>=-3)&(V<=46)&(np.abs(U)<=np.maximum(width,0))).astype(np.float32)
    Ly.emit(m*np.clip(1.1-t,0,1),CYAN,1.0); Ly.halo(m,BLUE,2.5,1.0); Ly.halo(m,CYAN,6,0.5)
    cm=((V>=-3)&(V<=20)&(np.abs(U)<=2.6*(1-np.clip(V/20,0,1)))).astype(np.float32)
    Ly.emit(blur(cm,1*SS),WHITE,1.2)
    return Ly

def rocket_c():   # lightning-bolt rocket, zigzag exhaust
    Ly=Layer()
    body=[(0,-80),(5.5,-62),(6.5,-50),(6.5,-22),(4.8,-8),(-4.8,-8),(-6.5,-22),(-6.5,-50),(-5.5,-62)]
    lf=[(-6.5,-32),(-15,-14),(-15.5,-2),(-9,-9),(-5.5,-10)]
    rf=[(-u,v) for u,v in lf]
    for f in (lf,rf):
        Ly.paint(pmask(f),shade(DPURP,PURP,C(40,10,80),-16,16)); Ly.emit(lmask(f,1.0),PINK,1.0); Ly.halo(lmask(f,1.4),PINK,2.5,1.0)
    bm=pmask(body)
    Ly.paint(bm,shade(C(90,25,150),C(160,60,230),C(45,12,85),-7,7))
    inner=[(0,-72),(3.6,-58),(3.6,-24),(2.4,-14),(-2.4,-14),(-3.6,-24),(-3.6,-58)]
    Ly.emit(lmask(inner,0.5),C(200,70,255),0.55)
    bolt=[(1.6,-52),(-2.6,-38),(0.4,-38),(-1.6,-26),(2.8,-41),(-0.2,-41)]
    Ly.paint(pmask(bolt),C(255,120,240)); Ly.emit(pmask(bolt),PINK,0.4); Ly.halo(pmask(bolt),PINK,1.5,0.8)
    nozzle=[(-3.8,-8),(3.8,-8),(3,-4),(-3,-4)]
    Ly.paint(pmask(nozzle),C(100,40,160)); Ly.emit(lmask(nozzle,0.6),PINK,0.7)
    Ly.emit(lmask(body,1.0),PINK,1.0); Ly.halo(lmask(body,1.6),PINK,3,1.0); Ly.halo(bm,MAG,7,0.35)
    # zigzag bolt exhaust
    zz=[(0,-4),(-3.5,9),(3.0,19),(-4.5,32),(2.5,42),(-3.5,55),(0.5,68)]
    br1=[(3.0,19),(7.5,26),(6.0,31)]; br2=[(-4.5,32),(-8.5,40)]; br3=[(2.5,42),(6.0,50)]
    for pts,w,k in ((zz,2.0,1.15),(br1,1.0,0.8),(br2,1.0,0.8),(br3,0.9,0.7)):
        m=lmask(pts,w,closed=False)
        fade=np.clip(1.15-V/75,0.2,1)
        Ly.emit(m*fade,CYAN,1.0*k); Ly.halo(m*fade,BLUE,2.2,1.4*k); Ly.halo(m*fade,CYAN,5,0.7*k)
        Ly.emit(lmask(pts,w*0.45,closed=False)*fade,WHITE,0.9*k)
    Ly.halo(((V>-5)&(V<4)&(np.abs(U)<3)).astype(np.float32),WHITE,1.5,1.0)
    return Ly

def rocket_d():   # geometric triangle rocket
    Ly=Layer()
    N=(0,-80); a=(-5.5,-58); b=(5.5,-58); c=(0,-50)
    d=(-7.5,-34); e=(7.5,-34); f=(0,-28); g=(-5,-12); h=(5,-12); k=(0,-6)
    tris=[((N,a,c),PINK),((N,c,b),VIOL),((a,d,c),MAG),((c,d,f),C(200,40,200)),((c,f,e),PURP),((c,e,b),C(120,35,210)),
          ((d,g,f),C(235,60,200)),((f,g,k),MAG),((f,k,h),VIOL),((f,h,e),C(95,30,180))]
    lf=[(-6.8,-30),(-17,-6),(-11,-9)]; lf2=[(-6.8,-30),(-11,-9),(-5,-12)]
    rf=[(6.8,-30),(17,-6),(11,-9)]; rf2=[(6.8,-30),(11,-9),(5,-12)]
    for t_,col in ((lf,PINK),(lf2,MAG),(rf,PURP),(rf2,VIOL)):
        Ly.paint(pmask(t_),col); Ly.emit(lmask(t_,0.5),C(255,140,240),0.6)
    for t_,col in tris:
        Ly.paint(pmask(t_),col); Ly.emit(lmask(t_,0.45),C(255,150,245),0.45)
    outline=[N,b,e,h,k,g,d,a]
    for f_ in (lf,rf):
        Ly.halo(lmask(f_,1.0),PINK,2.5,0.8)
    Ly.emit(lmask(outline,0.8),C(255,90,230),0.9); Ly.halo(lmask(outline,1.4),PINK,3,1.0); Ly.halo(pmask(outline),MAG,7,0.35)
    # stacked triangle exhaust
    for (w,v0,v1,kk) in ((5.0,-5,14,1.0),(4.0,8,28,0.85),(3.0,22,42,0.7),(2.0,36,54,0.5)):
        t_=[(-w,v0),(w,v0),(0,v1)]
        m=pmask(t_)
        Ly.emit(m,CYAN,0.9*kk); Ly.halo(m,BLUE,2.2,1.0*kk); Ly.halo(m,CYAN,5,0.5*kk)
        Ly.emit(pmask([(-w*0.45,v0),(w*0.45,v0),(0,v0+(v1-v0)*0.55)]),ICE,0.7*kk)
    return Ly

def down(a):
    s=a.shape
    return a.reshape(s[0]//SS,SS,s[1]//SS,SS,*s[2:]).mean(axis=(1,3))

def composite(Ly):
    A=down(Ly.A)[...,None]; col=down(Ly.col); gl=down(Ly.glow)
    col=np.clip(col/np.maximum(A,1e-6),0,1)
    base=plate*(1-A)+col*A
    rk=1-(1-base)*(1-np.clip(gl,0,1))
    a=alpha[...,None]
    out=orig*(1-a)+rk*a
    return out

names={1:('a',rocket_a),2:('b',rocket_b),3:('c',rocket_c),4:('d',rocket_d)}
import sys
which=[int(x) for x in sys.argv[1:]] or [1,2,3,4]
origu8=(orig*255+0.5).astype(np.uint8)
SXS={1:1.3,2:1.05,3:1.3,4:1.3}
for i in which:
    SX=SXS[i]; U=U0/SX
    out=composite(names[i][1]())
    u8=(np.clip(out,0,1)*255+0.5).astype(np.uint8)
    u8[~poly]=origu8[~poly]   # guarantee exactness outside region
    Image.fromarray(u8).save(f'{ROOT}/logo-rocket-option-{i}.png')
    d=np.abs(u8.astype(int)-origu8.astype(int)).max(axis=2)
    print(i,'outside-mask maxdiff',int(d[~poly].max()),'changed px outside',int((d[~poly]>0).sum()),'inside changed',int((d[poly]>0).sum()))
Image.fromarray((np.clip(plate,0,1)*255+.5).astype(np.uint8)).save(f'{ROOT}/_scratch/rk/plate.png')
