# Guiones de reels pendientes

Guiones listos para narrar con vidIQ (voz "Francisco", voiceId EK54is7sa3aPFLD9BwCC, una línea por escena) en cuanto haya créditos.
Se escribieron el 19 nov 2026: el saldo era de 22 créditos y un reel necesita unos 38-45 (28 de narración + ~10 de composición). Los créditos se renuevan el 16 dic 2026.

---

## Reel 04 · jueves 26 nov 2026 (víspera de Black Friday)
**Tema:** 30 % + 20 % de descuento no es 50 %
**Cálculos (propios):** 0,70 × 0,80 = 0,56 → descuento real 44 %. Sobre $200.000 pagas $112.000, no $100.000. Si antes subieron el precio 25 %, 1,25 × 0,80 = 1,00 → el "20 % off" te deja en el precio original.
**Nota en pantalla:** "Valores de ejemplo."

Guion (8 líneas):
1. ¿30 % más 20 % de descuento es 50 %? No.
2. Los descuentos encadenados no se suman, se multiplican.
3. Primero quitas el 30 %: pagas el 70 % del precio.
4. Luego el 20 % se aplica sobre ese 70 %, no sobre el precio original.
5. Resultado: pagas el 56 %. El descuento real es del 44 %.
6. En un producto de 200 mil pesos pagas 112 mil, no 100 mil.
7. Y ojo: si subieron el precio 25 % antes, un 20 % de descuento te deja igual.
8. Guárdalo para este Black Friday y compártelo con quien va a comprar.

Escenas sugeridas (tools/lib.py): S_lines gancho "30 % + 20 %" / "≠ 50 %" → S_stat "Pagas el" "70 %" → S_stat "70 % × 80 %" "56 %" → S_stat "Descuento real" "44 %" → barras $200.000 / $112.000 / $100.000 esperado → S_lines "Precio inflado +25 %" "× 0,80 = mismo precio" → S_tips (1 Revisa el precio días antes, 2 Multiplica, no sumes) → S_cta.

Texto para redes:
> 30 % + 20 % de descuento NO es 50 %. Es 44 %.
> Los descuentos encadenados se multiplican: 0,70 × 0,80 = 0,56. En $200.000 pagas $112.000. (Valores de ejemplo.)
> Antes de comprar este Black Friday, revisa el precio de los días anteriores. Guárdalo y compártelo.
> #blackfriday #descuentos #finanzaspersonales #compras #datos #colombia #atajodigital

Short de YouTube: "30 % + 20 % de descuento NO es 50 % #shorts" · categoría EDUCATION.

---

## Reel 05 · sábado 28 nov 2026
**Tema:** La regla del 72: cuánto tarda en duplicarse tu plata
**Cálculos (propios):** años ≈ 72 ÷ tasa anual. Exacto ln2/ln(1+r): 12 % → 6,1 años (regla: 6); 10 % → 7,3 (regla: 7,2); 5 % → 14,2 (regla: 14,4). Con inflación de 5 % anual, los precios se duplican en ~14 años (tu plata guardada pierde la mitad de su poder de compra).
**Nota en pantalla:** "Tasas de ejemplo. Rentabilidad no garantizada."

Guion (7 líneas):
1. ¿Cuánto tarda tu plata en duplicarse? Hay un truco de 5 segundos.
2. Se llama la regla del 72: divide 72 entre la tasa anual.
3. Al 12 % anual, tu plata se duplica en unos 6 años.
4. Al 6 %, en unos 12 años. La tasa lo cambia todo.
5. Y funciona al revés: con inflación del 5 %, los precios se duplican en unos 14 años.
6. Plata quieta debajo del colchón pierde la mitad de su valor en ese tiempo.
7. Guárdalo y úsalo antes de comparar cualquier inversión o CDT.

Escenas sugeridas: S_lines gancho "¿Cuánto tarda tu plata en duplicarse?" → S_stat "La regla del" "72" "÷ tasa anual" → barras 12 % → 6 años, 6 % → 12 años → S_stat "Inflación 5 %" "≈14 años" "para que los precios se dupliquen" → S_lines "Plata quieta" "pierde la mitad" → S_cta.

Texto para redes:
> ¿Cuánto tarda tu plata en duplicarse? Divide 72 entre la tasa anual.
> Al 12 % anual, unos 6 años. Al 6 %, unos 12. Y con inflación del 5 %, los precios se duplican en ~14 años. (Tasas de ejemplo.)
> Úsalo antes de comparar un CDT o una inversión. Guárdalo.
> #finanzaspersonales #inversion #educacionfinanciera #ahorro #cdt #colombia #atajodigital

Short de YouTube: "La regla del 72: cuánto tarda en duplicarse tu plata #shorts" · categoría EDUCATION.

---

# Semana 2 (30 nov – 5 dic 2026)
Escritos el 26 nov 2026. Saldo de vidIQ: 22 créditos (no alcanza para ningún reel; renovación el 16 dic 2026). No hay nada programado en Metricool para estas fechas.

## Reel 06 · martes 1 dic 2026
**Tema:** Tus 15 GB gratis de Google se llenan con 37 minutos de video
**Cálculos (propios, con tamaños aproximados):** video 4K a 60 cps ≈ 400 MB/min (referencia de tamaños de la cámara del iPhone, HEVC ≈ 440 MB/min) → 15.000 MB ÷ 400 ≈ 37 min. Foto ≈ 3 MB → 15.000 ÷ 3 = 5.000 fotos. iCloud gratis 5 GB → 5.000 ÷ 400 ≈ 12 min. 1080p a 30 cps ≈ 60 MB/min (unas 7 veces menos que 4K60).
**Nota en pantalla:** "Tamaños aproximados. Varían según el celular."

Guion (8 líneas):
1. Tus 15 GB gratis de Google se llenan con solo 37 minutos de video.
2. Un minuto de video en 4K a 60 cuadros puede pesar unos 400 megas.
3. 15 GB entre 400 megas: unos 37 minutos. Eso es todo.
4. En fotos rinde más: a unos 3 megas por foto, caben unas 5.000.
5. Y ojo: esos 15 GB se comparten entre Gmail, Drive y Google Fotos.
6. En iCloud gratis tienes 5 GB: unos 12 minutos de video 4K.
7. Truco: graba en 1080p cuando no necesites 4K. Pesa varias veces menos.
8. Guárdalo y revisa hoy cuánto espacio te queda.

Escenas sugeridas (tools/lib.py): S_lines gancho "15 GB gratis" / "= 37 min de video" → S_stat "1 min en 4K60" "≈400 MB" → S_stat "15.000 ÷ 400" "≈37 min" → S_stat "Fotos de ~3 MB" "≈5.000" → S_lines "Gmail + Drive + Fotos" "comparten los 15 GB" → S_stat "iCloud gratis 5 GB" "≈12 min" → barras 4K60 400 MB / 1080p 60 MB → S_cta.

Texto para redes:
> Tus 15 GB gratis de Google se llenan con unos 37 minutos de video en 4K.
> Un minuto en 4K a 60 cuadros pesa cerca de 400 MB, y esos 15 GB se comparten entre Gmail, Drive y Fotos. (Tamaños aproximados.)
> Graba en 1080p cuando no necesites 4K. Guárdalo y revisa tu espacio hoy.
> #googlefotos #almacenamiento #celular #tecnologia #trucos #colombia #atajodigital

Short de YouTube: "15 GB gratis = solo 37 minutos de video 4K #shorts" · categoría SCIENCE_TECHNOLOGY.

---

## Reel 07 · jueves 3 dic 2026
**Tema:** Lo que te cuesta el 4x1000 y cómo no pagarlo
**Cálculos (propios):** GMF 0,4 %: $1.000.000 → $4.000. Sueldo de $4.000.000 retirado completo cada mes → $16.000/mes → $192.000/año. Cuenta exenta: una sola, hasta 350 UVT al mes; UVT 2026 = $52.374 (DIAN, Resolución 238 de 2025) → 350 × 52.374 = $18.330.900.
**Nota en pantalla:** "Valores de ejemplo. UVT 2026: $52.374."

Guion (8 líneas):
1. Cada vez que mueves un millón de pesos, el banco te quita 4.000.
2. Es el 4x1000: el impuesto a los movimientos financieros, el 0,4 %.
3. Si sacas todo tu sueldo de 4 millones cada mes, pagas 16.000.
4. En un año son 192.000 pesos. Sin darte cuenta.
5. Pero puedes marcar una cuenta como exenta, en un solo banco.
6. En 2026 quedan libres los retiros hasta unos 18,3 millones al mes: 350 UVT.
7. Pídelo en tu banco o en su app; muchas veces es un solo clic.
8. Guárdalo y compártelo con quien todavía paga el 4x1000 sin necesidad.

Escenas sugeridas: S_lines gancho "$1.000.000" / "−$4.000" → S_stat "4x1000" "0,4 %" → S_stat "Sueldo $4.000.000" "−$16.000/mes" → S_stat "En un año" "$192.000" → S_lines "1 cuenta exenta" "en un solo banco" → S_stat "350 UVT" "≈$18,3 M/mes" → S_tips (1 Marca la cuenta donde recibes el sueldo, 2 Pídelo en la app) → S_cta.

Texto para redes:
> ¿Sigues pagando el 4x1000 en la cuenta donde recibes el sueldo?
> Con un sueldo de $4.000.000 son $192.000 al año. Puedes marcar una cuenta como exenta y no pagar hasta 350 UVT al mes (≈$18,3 millones en 2026). (Valores de ejemplo.)
> Pídelo en tu banco. Guárdalo y compártelo.
> #4x1000 #finanzaspersonales #bancos #ahorro #impuestos #colombia #atajodigital

Short de YouTube: "Así dejas de pagar el 4x1000 #shorts" · categoría EDUCATION.

---

## Reel 08 · sábado 5 dic 2026
**Tema:** 1 de cada 10 PIN es 1234
**Datos (verificados):** análisis de DataGenetics (2012) sobre 3,4 millones de PIN de 4 dígitos filtrados: 1234 ≈ 10,7 %; 1111 ≈ 6 %; los 20 más comunes ≈ 26,8 %. Combinaciones: 10^4 = 10.000; 10^6 = 1.000.000 (100 veces más).
**Nota en pantalla:** "Fuente: análisis de DataGenetics sobre 3,4 millones de PIN filtrados."

Guion (8 líneas):
1. Uno de cada diez PIN de cuatro dígitos es 1234.
2. Un análisis de 3,4 millones de PIN filtrados lo encontró: casi el 11 %.
3. Y los 20 más comunes suman más de una cuarta parte de todos.
4. Hay 10.000 combinaciones posibles, pero casi nadie las usa.
5. Fechas, años y patrones como 1111 o 0000 son lo primero que se prueba.
6. Un PIN de 6 dígitos tiene un millón de combinaciones: 100 veces más.
7. Si tu PIN es una fecha o un patrón, cámbialo hoy.
8. Guárdalo y compártelo con quien todavía usa 1234.

Escenas sugeridas: S_lines gancho "1 de cada 10 PIN" / "es 1234" → S_stat "1234" "10,7 %" → S_stat "Top 20 PIN" "26,8 %" → S_stat "Combinaciones" "10.000" → S_lines "1111 · 0000 · 19XX" "se prueban primero" → barras 4 dígitos 10.000 / 6 dígitos 1.000.000 → S_tips (1 Nada de fechas, 2 Usa 6 dígitos) → S_cta.

Texto para redes:
> 1 de cada 10 PIN de 4 dígitos es 1234.
> En un análisis de 3,4 millones de PIN filtrados, los 20 más comunes sumaron más de la cuarta parte. Un PIN de 6 dígitos tiene 100 veces más combinaciones.
> Si el tuyo es una fecha o un patrón, cámbialo hoy. Compártelo.
> #ciberseguridad #contraseñas #seguridad #celular #tecnologia #colombia #atajodigital

Short de YouTube: "1 de cada 10 PIN es 1234 #shorts" · categoría SCIENCE_TECHNOLOGY.
