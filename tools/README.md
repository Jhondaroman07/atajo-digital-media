# Cómo se generan los carruseles

- `gen.py`: define el estilo de marca (fondo #0E1116, acento #C6F432, Space Grotesk / Inter / JetBrains Mono, 1080x1350) y el contenido de cada carrusel en la lista `C`. Escribe un archivo `.dc.html` por diapositiva.
- `render.py`: convierte cada diapositiva en PNG con Chrome (Playwright). Las fuentes se descargan con `npm pack @fontsource/space-grotesk @fontsource/jetbrains-mono` y se extraen en `fonts/`.
- Las rutas al inicio de cada script apuntan a carpetas de trabajo; ajústalas antes de ejecutar.
- Las imágenes finales se guardan en `carruseles/semana-NN/` y se usan desde raw.githubusercontent.com para programarlas en Metricool.
