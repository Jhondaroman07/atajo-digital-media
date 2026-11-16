import json, html, os
ROOT="/home/claude/atajo-carruseles/project"
BG="#0E1116"; TXT="#F5F7FA"; MUT="#AEB6C2"; LINE="#2C3440"; CARD="#161B22"
W,H=1080,1350
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=JetBrains+Mono:wght@500&amp;family=Space+Grotesk:wght@500;700&amp;display=swap" rel="stylesheet">'
E=html.escape
LOGO=('<svg aria-hidden="true" width="56" height="56" viewBox="0 0 56 56"><rect width="56" height="56" rx="14" fill="{{accent}}"></rect>'
      '<path d="M15 18 L25 28 L15 38 M29 18 L39 28 L29 38" fill="none" stroke="'+BG+'" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"></path></svg>')
ARROW='<svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="{{accent}}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
H_FONT="font-family:'Space Grotesk',Inter,sans-serif"
M_FONT="font-family:'JetBrains Mono',monospace"

def page(title, n, total, body, last=False):
    foot_r = '' if last else f'<div style="display:flex;align-items:center;gap:14px;font-size:28px;font-weight:600;color:{TXT}">Desliza {ARROW}</div>'
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{E(title)}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0}}
a{{color:#C6F432}}a:hover{{color:#E2FF8A}}
</style>
</helmet>
<div style="width:{W}px;height:{H}px;box-sizing:border-box;padding:88px;background:{BG};color:{TXT};font-family:Inter,sans-serif;display:flex;flex-direction:column;justify-content:space-between;gap:48px">
<div style="display:flex;align-items:center;justify-content:space-between">
<div style="display:flex;align-items:center;gap:20px">{LOGO}<span style="font-size:26px;font-weight:600;letter-spacing:0.12em">ATAJO DIGITAL</span></div>
<span style="font-size:26px;font-weight:500;color:{MUT}">{n}/{total}</span>
</div>
<div style="flex-grow:1;display:flex;flex-direction:column;justify-content:center;gap:56px">
{body}
</div>
<div style="display:flex;align-items:center;justify-content:space-between">
<span style="font-size:28px;font-weight:500;color:{MUT}">@atajo.digital.media</span>
{foot_r}
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"accent":{{"editor":"color","default":"#C6F432","options":["#C6F432","#5EEAD4","#FDBA74"]}},"$preview":{{"width":{W},"height":{H}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{ accent: this.props.accent ?? '#C6F432' }};
}}
}}
</script>
</body>
</html>
'''

def cover(kicker, before, hl, after, sub):
    return (f'<div style="display:flex;flex-direction:column;gap:40px">'
      f'<span style="{M_FONT};font-size:30px;color:{{{{accent}}}};letter-spacing:0.08em">{E(kicker)}</span>'
      f'<h1 style="margin:0;{H_FONT};font-size:104px;font-weight:700;line-height:1.02;letter-spacing:-0.02em">{E(before)}<span style="color:{{{{accent}}}}">{E(hl)}</span>{E(after)}</h1>'
      f'<p style="margin:0;font-size:40px;line-height:1.35;color:{MUT}">{E(sub)}</p></div>')

def kbd(keys):
    caps=[]
    for i,k in enumerate(keys):
        if i: caps.append(f'<span style="font-size:36px;color:{MUT}">+</span>')
        caps.append(f'<span style="{M_FONT};font-size:38px;color:{TXT};background:#1B212B;border:2px solid {LINE};border-bottom-width:7px;border-radius:14px;padding:12px 24px">{E(k)}</span>')
    return '<div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap">'+''.join(caps)+'</div>'

def item(label, top, title, desc):
    return (f'<div style="display:flex;flex-direction:column;gap:22px">'
      f'<span style="{M_FONT};font-size:26px;color:{{{{accent}}}}">{E(label)}</span>{top}'
      f'<h2 style="margin:0;{H_FONT};font-size:56px;font-weight:700;line-height:1.08">{E(title)}</h2>'
      f'<p style="margin:0;font-size:34px;line-height:1.4;color:{MUT}">{E(desc)}</p></div>')

def code(t, size=32):
    return f'<div style="{M_FONT};font-size:{size}px;line-height:1.45;color:{{{{accent}}}};background:{CARD};border:2px solid {LINE};border-radius:20px;padding:26px 32px;overflow-wrap:anywhere">{E(t)}</div>'

def swap(old, new):
    return (f'<div style="display:flex;align-items:center;gap:22px;flex-wrap:wrap">'
      f'<span style="font-size:36px;color:{MUT};text-decoration:line-through">{E(old)}</span>'
      f'<svg aria-hidden="true" width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="{MUT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
      f'<span style="{H_FONT};font-size:56px;font-weight:700;color:{{{{accent}}}}">{E(new)}</span></div>')

def big(num, title, desc):
    return (f'<div style="display:flex;flex-direction:column;gap:28px">'
      f'<span style="{H_FONT};font-size:380px;font-weight:700;line-height:0.85;color:{{{{accent}}}}">{E(num)}</span>'
      f'<h2 style="margin:0;{H_FONT};font-size:72px;font-weight:700;line-height:1.05">{E(title)}</h2>'
      f'<p style="margin:0;font-size:38px;line-height:1.4;color:{MUT}">{E(desc)}</p></div>')

def note(title, desc, box=None, size=34):
    b = f'<div style="font-size:{size}px;line-height:1.5;color:{TXT};background:{CARD};border:2px solid {LINE};border-radius:20px;padding:32px 36px">{E(box)}</div>' if box else ''
    return (f'<div style="display:flex;flex-direction:column;gap:32px">'
      f'<h2 style="margin:0;{H_FONT};font-size:72px;font-weight:700;line-height:1.05">{E(title)}</h2>'
      f'<p style="margin:0;font-size:38px;line-height:1.4;color:{MUT}">{E(desc)}</p>{b}</div>')

ICONS={'save':'<path d="M6 3h12v18l-6-4-6 4z"></path>','share':'<path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"></path>','follow':'<path d="M12 5v14M5 12h14"></path>'}
def cta():
    rows=[('save','Guárdalo para tenerlo a mano'),('share','Compártelo con alguien que lo necesite'),('follow','Sígueme para más atajos cada semana')]
    lis=''.join(f'<div style="display:flex;align-items:center;gap:28px"><span style="display:flex;align-items:center;justify-content:center;width:84px;height:84px;border-radius:20px;background:{CARD};border:2px solid {LINE}"><svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="{{{{accent}}}}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[k]}</svg></span><span style="font-size:40px;font-weight:500">{E(t)}</span></div>' for k,t in rows)
    return (f'<h1 style="margin:0;{H_FONT};font-size:112px;font-weight:700;line-height:1">¿Te <span style="color:{{{{accent}}}}">sirvió</span>?</h1>'
      f'<div style="display:flex;flex-direction:column;gap:36px">{lis}</div>'
      f'<p style="margin:0;{H_FONT};font-size:52px;font-weight:700;color:{{{{accent}}}}">@atajo.digital.media</p>')

C=[]
# 1 Windows
C.append(("c1","7 atajos de Windows",[
 cover("WINDOWS","7 atajos que te ahorran ","1 hora"," a la semana","Úsalos todos los días y dejarás de perder tiempo con el mouse."),
 item("Atajo 1",kbd(["Win","V"]),"Historial del portapapeles","Pega cualquier cosa que copiaste antes, no solo la última.")+item("Atajo 2",kbd(["Win","Shift","S"]),"Captura de una parte","Recorta solo la zona de la pantalla que necesitas."),
 item("Atajo 3",kbd(["Win","D"]),"Ir al escritorio","Minimiza todo de un golpe. Repítelo para volver.")+item("Atajo 4",kbd(["Win","L"]),"Bloquear el PC","Antes de levantarte del puesto, en un segundo."),
 item("Atajo 5",kbd(["Win","E"]),"Abrir el Explorador","Llega a tus archivos sin buscar el ícono.")+item("Atajo 6",kbd(["Win","."]),"Emojis y símbolos","Inserta emojis y símbolos en cualquier programa."),
 item("Atajo 7",kbd(["Ctrl","Shift","T"]),"Reabrir pestaña cerrada","¿Cerraste una pestaña del navegador sin querer? Vuelve al instante. Funciona varias veces seguidas."),
 cta()]))
# 2 Software gratis
C.append(("c2","5 programas gratis",[
 cover("SOFTWARE","5 programas ","gratis"," que reemplazan software caro","Alternativas legales y potentes para editar, diseñar y trabajar."),
 item("Diseño",swap("Photoshop","Photopea"),"Edita imágenes en el navegador","Abre archivos PSD sin instalar nada.")+item("Video",swap("Premiere Pro","DaVinci Resolve"),"Edición de video profesional","Su versión gratuita es usada por creadores de todo el mundo."),
 item("Oficina",swap("Microsoft Office","LibreOffice"),"Documentos, hojas y presentaciones","Abre y guarda archivos de Word, Excel y PowerPoint.")+item("Grabación",swap("Grabadores de pago","OBS Studio"),"Graba tu pantalla sin límites","Sin marcas de agua y sin límite de tiempo."),
 item("Ilustración",swap("Illustrator","Inkscape"),"Gráficos vectoriales","Crea logos e ilustraciones que no pierden calidad al ampliarlos."),
 note("Un consejo importante","Descárgalos siempre desde su página oficial. Las versiones de otros sitios pueden traer virus."),
 cta()]))
# 3 Excel
C.append(("c3","5 fórmulas de Excel",[
 cover("EXCEL","5 fórmulas que todo ","profesional"," debe saber","Con estas resuelves la mayoría de tus reportes del día a día."),
 item("Fórmula 1",code("=BUSCARX(A2;Productos!A:A;Productos!C:C)"),"BUSCARX","Trae un dato de otra tabla, por ejemplo el precio de un producto.")+item("Fórmula 2",code('=SUMAR.SI.CONJUNTO(D:D;B:B;"Bogotá";C:C;"Enero")'),"SUMAR.SI.CONJUNTO","Suma solo lo que cumple varias condiciones a la vez."),
 item("Fórmula 3",code('=FILTRAR(A2:D100;C2:C100="Pendiente")'),"FILTRAR","Muestra solo las filas que cumplen una condición, y se actualiza sola.")+item("Fórmula 4",code("=UNICOS(B2:B100)"),"UNICOS","Saca una lista sin datos repetidos."),
 item("Fórmula 5",code('=SI.ERROR(BUSCARX(A2;Productos!A:A;Productos!C:C);"No encontrado")'),"SI.ERROR","Cambia los errores feos por un mensaje claro."),
 note("Antes de copiarlas","BUSCARX, FILTRAR y UNICOS funcionan en Excel 365 y Excel 2021 o posterior.","Si tu Excel usa coma decimal, los argumentos se separan con punto y coma (;). Si usa punto decimal, cámbialos por coma (,)."),
 cta()]))
# 4 IA + Excel
C.append(("c4","Pídele fórmulas a la IA",[
 cover("IA + EXCEL","Pídele a la IA ","cualquier fórmula"," en 4 pasos","Así obtienes una fórmula que funciona a la primera."),
 item("Paso 1",'',"Describe tus datos","Qué columnas tienes y en qué rango están. Ejemplo: A1:D200 con Fecha, Ciudad, Vendedor y Venta.")+item("Paso 2",'',"Di qué resultado quieres","Y en qué celda lo necesitas."),
 item("Paso 3",'',"Indica tu Excel","La versión y el idioma, porque las fórmulas cambian de nombre en español.")+item("Paso 4",'',"Pide la explicación","Que te la explique paso a paso. Así aprendes y puedes ajustarla tú."),
 note("Copia este ejemplo","Cambia los datos por los tuyos:","Tengo una tabla en A1:D200 con Fecha, Ciudad, Vendedor y Venta. Quiero en F2 el total de ventas de Bogotá en enero. Uso Excel 365 en español. Dame la fórmula y explícamela paso a paso.",36),
 cta()]))
# 5 Backup
C.append(("c5","Regla 3-2-1 de respaldo",[
 cover("RESPALDOS","Regla ","3-2-1",": nunca vuelvas a perder tus archivos","El método más simple para proteger fotos, documentos y trabajo."),
 big("3","copias de tus archivos","El original y dos respaldos. Si una falla, tienes otras dos."),
 big("2","tipos de almacenamiento","Por ejemplo, el disco de tu PC y un disco externo. Así un solo daño no se lleva todo."),
 big("1","copia fuera de casa","En la nube. Te protege de robos, incendios o daños en tu casa u oficina."),
 note("Ejemplo práctico","Tu PC + un disco externo + Google Drive.","Automatízalo: activa el Historial de archivos de Windows hacia el disco externo, e instala Google Drive para escritorio para que tus carpetas se copien solas en la nube."),
 cta()]))

boards={}; order=[]
y=300
for ci,(cid,ctitle,slides) in enumerate(C):
    total=len(slides)
    for si,body in enumerate(slides):
        fn=f"{cid}-{si+1}.dc.html" if not (ci==0 and si==0) else "Main.dc.html"
        last= si==total-1
        open(os.path.join(ROOT,fn),"w").write(page(f"{ctitle} – {si+1}/{total}",si+1,total,body,last))
        boards[fn]={"x":si*(W+80),"y":y,"w":W,"h":H,"title":f"{ctitle} · {si+1}"}
        order.append(fn)
    y+=H+120+260
notes={}
y=300
for ci,(cid,ctitle,slides) in enumerate(C):
    notes[f"t{ci+1}"]={"x":0,"y":y-260,"text":f"Carrusel {ci+1}: {ctitle}","kind":"title1","maxW":len(slides)*(W+80)-80}
    y+=H+120+260
canvas={"v":3,"createdOnFiles":{"v":1,"at":"2026-11-16T19:58:00Z"},"title":"Atajo Digital – Primeros 5 carruseles","launch":{"view":"canvas"},"pages":[],"boards":boards,"order":order,"notes":notes,"designSystems":[]}
json.dump(canvas,open(os.path.join(ROOT,"canvas.json"),"w"),ensure_ascii=False)
print(order)
