import sys
from lib import *
NOTE="Velocidad de ejemplo: 100.000 millones de intentos por segundo."
def bars(t,D,k):
    im,d=frame_base(); ctext(d,300,"Tiempo para probar todas",F(IB,60),TXT); ctext(d,380,"las combinaciones",F(IB,60),TXT)
    rows=[("8 minúsculas","abcdefgh","2 segundos",0.08),("8 de todo tipo","aB3$kP9!","17 horas",0.35),("12 de todo tipo","aB3$kP9!xQ2#","150.000 años",1.0)]
    for i,(lab,ex,val,frac) in enumerate(rows[:k]):
        a=ease(t/0.8) if i==k-1 else 1
        y=600+i*320
        d.text((110,y),lab,font=F(IS,46),fill=TXT); w=d.textlength(ex,font=F(MONO,40)); d.text((W-110-w,y+4),ex,font=F(MONO,40),fill=MUT)
        bw=(W-220)*frac*a
        d.rounded_rectangle([110,y+75,110+max(bw,24),y+150],radius=18,fill=ACC if i==2 else GRAY)
        d.text((110,y+170),val,font=F(IB,60),fill=ACC if i==2 else TXT)
    ctext(d,H-260,NOTE,F(IR,30),MUT)
    return im
SC=[S_lines([("¿Cuánto tarda",96,TXT,0),("una computadora",96,TXT,0.3),("en adivinar",96,TXT,0.6),("tu contraseña?",96,ACC,0.9)],("Depende del largo y de los caracteres",3.6)),
    S_stat("Un equipo que prueba","100.000 millones","de combinaciones por segundo"),
    lambda t,D: bars(t,D,1), lambda t,D: bars(t,D,2), lambda t,D: bars(t,D,3),
    S_lines([("Cada carácter extra",80,TXT,0),("multiplica el trabajo.",80,TXT,0.3),("El largo pesa más",80,ACC,2.4),("que los trucos.",80,ACC,2.7)]),
    S_tips("Protégete así",[("1","Usa frases largas,","una por cada cuenta."),("2","Guárdalas en un","gestor de contraseñas.")],gap=2.6),
    S_cta("Compártelo con quien","usa la misma clave",s2="para más datos que te protegen")]
starts=[0,7.079184,11.363265,16.352653,22.883265,27.794286,33.593469,39.314286,46.0]
if sys.argv[1:]==["still"]: stills(SC,starts,"r2")
else: render(SC,starts,"r2")
