# Semana 2 (30 nov - 5 dic 2026). Reutiliza estilos y componentes de gen.py.
import os, sys
_src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"gen.py")).read().split("C=[]")[0]
exec(_src)
ROOT=sys.argv[1] if len(sys.argv)>1 else "/home/claude/gen/s2"
os.makedirs(ROOT,exist_ok=True)
C=[]
# 6 Tienda falsa (Cyber Monday)
C.append(("c6","Señales de una tienda falsa",[
 cover("CIBERSEGURIDAD","6 señales de una ","tienda falsa"," en internet","Revísalas antes de pagar este Cyber Monday."),
 item("Señal 1",'',"Precio demasiado bueno","Un celular nuevo a mitad de precio no es una ganga: es el anzuelo.")+item("Señal 2",code("ofertas-tecno-oficial.xyz"),"Dirección web rara","Lee la URL letra por letra. Las copias cambian una letra o usan terminaciones como .xyz, .shop u .online."),
 item("Señal 3",'',"Solo aceptan transferencia","Te piden consignar a la cuenta de una persona. Sin tarjeta ni pasarela de pago reconocida.")+item("Señal 4",'',"No hay NIT ni dirección","Una empresa real muestra razón social, NIT y contacto. Puedes verificarla en rues.org.co."),
 item("Señal 5",'',"Reseñas imposibles de comprobar","Solo opiniones perfectas en su propia web, o comentarios desactivados en sus redes.")+item("Señal 6",'',"Te apuran","\"Solo quedan 2\", contadores de minutos... La prisa es para que no revises nada."),
 note("Si ya pagaste y fue fraude","Pide la reversión del pago si compraste por internet con tarjeta o un medio de pago electrónico.","Tienes 5 días hábiles desde que te das cuenta: reclama a la tienda y avisa al banco o entidad de tu medio de pago. Lo dice el artículo 51 del Estatuto del Consumidor (Ley 1480 de 2011). Por transferencia a una persona es mucho más difícil recuperar la plata.",32),
 cta()]))
# 7 Prima de diciembre
C.append(("c7","Tu prima de diciembre",[
 cover("FINANZAS PERSONALES","Tu ","prima de diciembre",": cuánto te toca y qué hacer con ella","Si tienes contrato laboral, la fecha límite de pago es el 20 de diciembre."),
 item("Cálculo",code("Prima = salario × días trabajados ÷ 360"),"Calcúlala tú mismo","Si recibes auxilio de transporte, súmalo al salario para el cálculo.")+item("Ejemplo",code("4.000.000 × 180 ÷ 360 = 2.000.000"),"Semestre completo = medio salario","Si entraste en octubre (90 días), te toca la mitad: $1.000.000. Valores de ejemplo."),
 big("1","Paga lo más caro primero","Si tienes deuda en tarjeta de crédito o créditos de consumo, abona a capital. Es la plata que más intereses te cobra."),
 big("2","Separa para enero","Matrículas, útiles, impuestos y seguros llegan juntos. Guarda esa parte antes de gastar."),
 big("3","Date un gusto con tope","Define el reparto antes de recibirla. Por ejemplo: 50 % deudas, 30 % ahorro y 20 % gustos."),
 cta()]))
# 8 Celular robado
C.append(("c8","Si te roban el celular",[
 cover("SEGURIDAD MÓVIL","¿Te robaron el celular? ","5 pasos"," para la primera hora","Y lo que debes hacer hoy para estar preparado."),
 item("Paso 1",code("android.com/find · icloud.com/find",30),"Bloquéalo a distancia","Entra con tu cuenta de Google o Apple desde otro equipo. Bloquéalo y, si no lo vas a recuperar, borra los datos.")+item("Paso 2",'',"Llama a tu operador","Pide bloquear la SIM y reportar el IMEI. Así nadie usa tu número para recibir códigos."),
 item("Paso 3",'',"Llama a tu banco","Bloquea las tarjetas y las apps de pago que tenías en el celular, incluidas las billeteras digitales.")+item("Paso 4",'',"Cambia la clave de tu correo","Con tu correo se recuperan todas tus cuentas. Cierra las sesiones abiertas en el teléfono robado."),
 item("Paso 5",'',"Avisa a tus contactos","Los ladrones escriben desde tu WhatsApp pidiendo plata prestada. Que nadie transfiera nada.")+item("Y después",code("adenunciar.policia.gov.co",30),"Pon la denuncia","Te sirve para el reporte ante el operador, el seguro y el banco."),
 note("Hazlo hoy, antes de que pase","Marca *#06# y guarda tu IMEI. Activa la búsqueda del dispositivo y ponle un PIN a tu SIM.","iPhone: Ajustes > tu nombre > Buscar > Buscar mi iPhone. Android: busca \"Encontrar mi dispositivo\" en Ajustes y verifica que esté activado."),
 cta()]))
for cid,ctitle,slides in C:
    total=len(slides)
    for si,body in enumerate(slides):
        open(os.path.join(ROOT,f"{cid}-{si+1}.dc.html"),"w").write(page(f"{ctitle} – {si+1}/{total}",si+1,total,body,si==total-1))
print("ok")
