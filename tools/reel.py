import subprocess, math, sys
from PIL import Image, ImageDraw, ImageFont
W,H,FPS=1080,1920,30
BG=(14,17,22); TXT=(245,247,250); MUT=(174,182,194); ACC=(198,244,50); CARD=(22,27,34); LINE=(44,52,64); GRAY=(70,78,92)
IB="/usr/share/fonts/opentype/inter/Inter-Bold.otf"; IS="/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"; IR="/usr/share/fonts/opentype/inter/Inter-Regular.otf"
MONO="/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
_fc={}
def F(p,s):
    k=(p,s)
    if k not in _fc: _fc[k]=ImageFont.truetype(p,s)
    return _fc[k]
def ease(x): x=max(0,min(1,x)); return 1-(1-x)**3
def pesos(n): return "$"+f"{int(round(n)):,}".replace(",",".")
def ctext(d,y,s,font,fill,alpha=1.0,dy=0):
    w=d.textlength(s,font=font); 
    col=tuple(int(BG[i]+(fill[i]-BG[i])*alpha) for i in range(3))
    d.text(((W-w)/2,y+dy),s,font=font,fill=col)
def logo(d,x,y,s=64):
    d.rounded_rectangle([x,y,x+s,y+s],radius=s*0.25,fill=ACC)
    k=s/56
    for ox in (15,29):
        d.line([(x+ox*k,y+18*k),(x+(ox+10)*k,y+28*k),(x+ox*k,y+38*k)],fill=BG,width=int(5*k),joint="curve")
def frame_base():
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    logo(d,80,110,64); d.text((166,124),"ATAJO DIGITAL",font=F(IS,32),fill=TXT)
    d.text((80,H-150),"@atajo.digital.media",font=F(IR,32),fill=MUT)
    return im,d
def note(d,a=1):
    ctext(d,H-260,"Ejemplo ilustrativo. Tu tasa puede ser distinta.",F(IR,30),MUT,a)

P=1_000_000; r=0.02
def tot(n): return P*r/(1-(1+r)**-n)*n
def cuota(n): return P*r/(1-(1+r)**-n)
ROWS=[(12,tot(12)),(24,tot(24)),(36,tot(36))]
def bars(d,shown,t_new,highlight=None):
    x0=110; maxw=W-220; top=620
    for i,(n,T) in enumerate(ROWS[:shown]):
        a = ease(t_new/0.8) if i==shown-1 else 1
        y=top+i*300
        d.text((x0,y),f"{n} cuotas",font=F(IS,44),fill=TXT if a>0.05 else BG)
        bw=maxw*(T/ROWS[-1][1])*a; pw=maxw*(P/ROWS[-1][1])*min(1,a*1.4)
        d.rounded_rectangle([x0,y+70,x0+max(pw,1),y+150],radius=18,fill=GRAY)
        if bw>pw: d.rounded_rectangle([x0+pw-18,y+70,x0+bw,y+150],radius=18,fill=ACC); d.rectangle([x0+pw-18,y+70,x0+pw,y+150],fill=GRAY)
        val=pesos(P+(T-P)*a)
        d.text((x0,y+168),val,font=F(IB,54),fill=TXT)
        pct=f"+{(T-P)/P*100:.0f} %"
        w=d.textlength(pct,font=F(IB,54)); d.text((x0+maxw-w,y+168),pct,font=F(IB,54),fill=ACC if (highlight==i or highlight is None) else MUT)
    # legend
    d.rounded_rectangle([110,500,146,536],radius=8,fill=GRAY); d.text((160,500),"Precio",font=F(IR,32),fill=MUT)
    d.rounded_rectangle([340,500,376,536],radius=8,fill=ACC); d.text((390,500),"Intereses",font=F(IR,32),fill=MUT)

def s1(t,D):
    im,d=frame_base()
    a=ease(t/0.6); ctext(d,560,"Compraste un celular de",F(IB,64),TXT,a,(1-a)*40)
    a2=ease((t-0.5)/0.8); v=P*a2
    ctext(d,680,pesos(v),F(IB,150),ACC,min(1,a2*2))
    a3=ease((t-2.4)/0.6); ctext(d,940,"con tu tarjeta de crédito.",F(IR,54),MUT,a3)
    a4=ease((t-3.2)/0.5); 
    if a4>0:
        s=0.8+0.2*a4; fs=int(110*s)
        ctext(d,1180,"¿A cuántas",F(IB,fs),TXT,a4); ctext(d,1180+fs*1.1,"cuotas?",F(IB,fs),ACC,a4)
    return im
def s2(t,D):
    im,d=frame_base()
    a=ease(t/0.6); ctext(d,640,"Hagamos las cuentas",F(IB,80),TXT,a,(1-a)*40)
    a2=ease((t-0.8)/0.6)
    if a2>0:
        bw,bh=760,220; x=(W-bw)/2; y=900+(1-a2)*30
        d.rounded_rectangle([x,y,x+bw,y+bh],radius=36,fill=CARD,outline=LINE,width=3)
        ctext(d,y+30,"Tasa de ejemplo",F(IS,44),MUT,a2); ctext(d,y+95,"2 % mensual",F(IB,90),ACC,a2)
    note(d,a2)
    return im
def s3(t,D):
    im,d=frame_base(); ctext(d,300,"Lo que pagas en total",F(IB,64),TXT); bars(d,1,t); note(d); return im
def s4(t,D):
    im,d=frame_base(); ctext(d,300,"Lo que pagas en total",F(IB,64),TXT); bars(d,2,t); note(d); return im
def s5(t,D):
    im,d=frame_base(); ctext(d,300,"Lo que pagas en total",F(IB,64),TXT); bars(d,3,t,highlight=2)
    a=ease((t-2.6)/0.6)
    if a>0:
        y=1560-(a)*20; bw=900; x=(W-bw)/2
        d.rounded_rectangle([x,y,x+bw,y+150],radius=30,fill=ACC)
        ctext(d,y+38,f"{pesos(tot(36)-P)} solo en intereses",F(IB,56),BG)
    if a<=0: note(d)
    return im
def s6(t,D):
    im,d=frame_base()
    ctext(d,330,"La cuota baja…",F(IB,80),TXT,ease(t/0.5))
    rows=[(12,cuota(12),tot(12)-P),(24,cuota(24),tot(24)-P),(36,cuota(36),tot(36)-P)]
    hx=[110,420,720]
    d.text((110,560),"Cuotas",font=F(IS,36),fill=MUT); d.text((420,560),"Pagas al mes",font=F(IS,36),fill=MUT); d.text((720,560),"Intereses",font=F(IS,36),fill=MUT)
    for i,(n,c,it) in enumerate(rows):
        a=ease((t-0.5-i*0.5)/0.5)
        if a<=0: continue
        y=650+i*170
        d.rounded_rectangle([90,y-20,W-90,y+120],radius=24,fill=CARD)
        col=lambda c_: tuple(int(CARD[k]+(c_[k]-CARD[k])*a) for k in range(3))
        d.text((110,y+15),str(n),font=F(IB,64),fill=col(TXT))
        d.text((420,y+22),pesos(c),font=F(IB,52),fill=col(TXT))
        d.text((720,y+22),pesos(it),font=F(IB,52),fill=col(ACC))
    a=ease((t-2.6)/0.6)
    ctext(d,1260,"…pero los intereses",F(IB,80),TXT,a); ctext(d,1360,"se disparan.",F(IB,80),ACC,a)
    return im
def s7(t,D):
    im,d=frame_base()
    ctext(d,420,"Antes de comprar",F(IB,84),TXT,ease(t/0.5))
    items=[("1","Revisa la tasa de tu","tarjeta en el extracto."),("2","Elige el menor número de","cuotas que puedas pagar.")]
    for i,(n,l1,l2) in enumerate(items):
        a=ease((t-0.8-i*2.4)/0.6)
        if a<=0: continue
        y=700+i*360+(1-a)*30
        d.rounded_rectangle([90,y,W-90,y+290],radius=32,fill=CARD,outline=LINE,width=3)
        d.rounded_rectangle([130,y+50,250,y+170],radius=28,fill=ACC); 
        w=d.textlength(n,font=F(IB,80)); d.text((190-w/2,y+58),n,font=F(IB,80),fill=BG)
        d.text((290,y+60),l1,font=F(IS,50),fill=TXT); d.text((290,y+130),l2,font=F(IS,50),fill=TXT)
    return im
def s8(t,D):
    im,d=frame_base()
    a=ease(t/0.6); s=int(200*(0.8+0.2*a)); 
    logo(d,(W-s)/2,560,s)
    ctext(d,860,"Guárdalo para",F(IB,84),TXT,ease((t-0.4)/0.5)); ctext(d,965,"tu próxima compra",F(IB,84),ACC,ease((t-0.4)/0.5))
    a3=ease((t-1.8)/0.6)
    ctext(d,1200,"Sigue a Atajo Digital",F(IS,54),TXT,a3); ctext(d,1280,"para más datos que te ahorran plata",F(IR,42),MUT,a3)
    return im

starts=[0,5.564082,9.351837,13.792653,17.502041,24.737959,30.850612,38.243265,45.0]
SC=[s1,s2,s3,s4,s5,s6,s7,s8]
which=sys.argv[1:]  # 'all' or 'still'
if which and which[0]=="still":
    for i,f in enumerate(SC):
        D=starts[i+1]-starts[i]; f(D-0.01,D).save(f"still{i+1}.png")
    sys.exit()
import os
for i,f in enumerate(SC):
    D=starts[i+1]-starts[i]; n=round(starts[i+1]*FPS)-round(starts[i]*FPS)
    tmp=f"scene{i+1}.tmp.mp4"
    p=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-c:v","libx264","-crf","18","-preset","veryfast","-pix_fmt","yuv420p",tmp],stdin=subprocess.PIPE)
    for k in range(n):
        p.stdin.write(f(k/FPS,D).tobytes())
    p.stdin.close()
    if p.wait()==0: os.rename(tmp,f"scene{i+1}.mp4")
with open("list.txt","w") as fl:
    for i in range(len(SC)): fl.write(f"file 'scene{i+1}.mp4'\n")
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i","list.txt","-c","copy","reel_silent.mp4"],check=True)
