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


import os
def render(SC,starts,out):
    for i,f in enumerate(SC):
        D=starts[i+1]-starts[i]; n=round(starts[i+1]*FPS)-round(starts[i]*FPS)
        tmp=f"{out}_s{i+1}.tmp.mp4"
        p=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-c:v","libx264","-crf","18","-preset","veryfast","-pix_fmt","yuv420p",tmp],stdin=subprocess.PIPE)
        for k in range(n): p.stdin.write(f(k/FPS,D).tobytes())
        p.stdin.close()
        if p.wait()==0: os.rename(tmp,f"{out}_s{i+1}.mp4")
    with open(f"{out}_list.txt","w") as fl:
        for i in range(len(SC)): fl.write(f"file '{out}_s{i+1}.mp4'\n")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"{out}_list.txt","-c","copy",f"{out}.mp4"],check=True)
def stills(SC,starts,out):
    from PIL import Image
    ims=[]
    for i,f in enumerate(SC):
        D=starts[i+1]-starts[i]; ims.append(f(D-0.01,D).resize((270,480)))
    m=Image.new("RGB",(270*4,960))
    for i,im in enumerate(ims): m.paste(im,((i%4)*270,(i//4)*480))
    m.save(f"{out}_stills.png")
# generic scenes
def S_lines(lines,sub=None):
    # lines: list of (text,size,color,delay)
    def f(t,D):
        im,d=frame_base(); y0=700 if len(lines)<=3 else 560
        y=y0
        for txt,size,col,dl in lines:
            a=ease((t-dl)/0.5); ctext(d,y,txt,F(IB,size),col,a,(1-a)*30); y+=int(size*1.25)
        if sub: ctext(d,y+40,sub[0],F(IR,46),MUT,ease((t-sub[1])/0.5))
        return im
    return f
def S_stat(label,value,sub,note_txt=None,count=None):
    def f(t,D):
        im,d=frame_base()
        a=ease(t/0.5); ctext(d,640,label,F(IS,54),MUT,a,(1-a)*30)
        a2=ease((t-0.4)/0.8)
        v = count(a2) if count else value
        fs=150 if len(v)<10 else 120
        ctext(d,760,v,F(IB,fs),ACC,min(1,a2*2))
        a3=ease((t-1.2)/0.5); ctext(d,780+fs*1.3,sub,F(IS,56),TXT,a3)
        if note_txt: ctext(d,H-260,note_txt,F(IR,30),MUT,a)
        return im
    return f
def S_tips(title,items,gap=2.2):
    def f(t,D):
        im,d=frame_base()
        ctext(d,420,title,F(IB,84),TXT,ease(t/0.5))
        for i,(n,l1,l2) in enumerate(items):
            a=ease((t-0.6-i*gap)/0.6)
            if a<=0: continue
            y=700+i*360+(1-a)*30
            d.rounded_rectangle([90,y,W-90,y+290],radius=32,fill=CARD,outline=LINE,width=3)
            d.rounded_rectangle([130,y+50,250,y+170],radius=28,fill=ACC)
            w=d.textlength(n,font=F(IB,80)); d.text((190-w/2,y+58),n,font=F(IB,80),fill=BG)
            d.text((290,y+60),l1,font=F(IS,50),fill=TXT); d.text((290,y+130),l2,font=F(IS,50),fill=TXT)
        return im
    return f
def S_cta(l1="Guárdalo y",l2="compártelo",s1="Sigue a Atajo Digital",s2="para más datos que te sirven"):
    def f(t,D):
        im,d=frame_base()
        a=ease(t/0.6); s=int(200*(0.8+0.2*a)); logo(d,(W-s)/2,560,s)
        ctext(d,860,l1,F(IB,84),TXT,ease((t-0.4)/0.5)); ctext(d,965,l2,F(IB,84),ACC,ease((t-0.4)/0.5))
        a3=ease((t-1.6)/0.6); ctext(d,1200,s1,F(IS,54),TXT,a3); ctext(d,1280,s2,F(IR,42),MUT,a3)
        return im
    return f
