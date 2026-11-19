import sys
from lib import *
def pes(n): return pesos(n)
def bars(t,D):
    im,d=frame_base(); ctext(d,300,"En un año",F(IB,72),TXT)
    rows=[("Café diario",2112000),("4 suscripciones",1200000)]
    for i,(lab,v) in enumerate(rows):
        a=ease((t-i*1.6)/0.8)
        if a<=0: continue
        y=600+i*360
        d.text((110,y),lab,font=F(IS,50),fill=TXT)
        d.rounded_rectangle([110,y+80,110+max((W-220)*v/2112000*a,24),y+170],radius=18,fill=ACC if i==0 else GRAY)
        d.text((110,y+190),pes(v*a),font=F(IB,64),fill=TXT)
    a=ease((t-3.8)/0.6)
    if a>0:
        y=1420; bw=900; x=(W-bw)/2
        d.rounded_rectangle([x,y,x+bw,y+150],radius=30,fill=ACC); ctext(d,y+38,"Total: "+pes(3312000)+" al año",F(IB,56),BG)
    ctext(d,H-260,"Valores de ejemplo.",F(IR,30),MUT)
    return im
SC=[S_lines([("Un café de",96,TXT,0),("$8.000",160,ACC,0.4),("no parece nada…",80,TXT,1.4)],("…hasta que haces la cuenta.",2.6)),
    S_stat("Un café cada día laboral","22 cafés","al mes"),
    S_stat("Eso es","$176.000","al mes",count=lambda a: pes(176000*a)),
    S_stat("Y al año","$2.112.000","solo en café",count=lambda a: pes(2112000*a)),
    bars,
    S_lines([("No se trata de",80,TXT,0),("dejar el café.",80,TXT,0.3),("Se trata de saber",80,ACC,2.4),("cuánto te cuesta.",80,ACC,2.7)]),
    S_tips("Este mes",[("1","Revisa el extracto","de tu tarjeta."),("2","Cancela lo que","no usas.")],gap=1.8),
    S_cta("Guárdalo para","revisar tus gastos",s2="para más datos que te ahorran plata")]
starts=[0,4.440816,8.071837,11.154286,15.516735,22.047347,27.454694,31.660408,37.0]
if sys.argv[1:]==["still"]: stills(SC,starts,"r3")
else: render(SC,starts,"r3")
