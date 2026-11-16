import re, os, glob, asyncio
from playwright.async_api import async_playwright
SRC="/home/claude/atajo-carruseles/project"; OUT="/home/claude/gen/png"; os.makedirs(OUT,exist_ok=True)
F="/home/claude/gen/fonts"
ff=f"""@font-face{{font-family:'Space Grotesk';font-weight:500;src:url(file://{F}/fontsource-space-grotesk-5.3.0/package/files/space-grotesk-latin-500-normal.woff2)}}
@font-face{{font-family:'Space Grotesk';font-weight:700;src:url(file://{F}/fontsource-space-grotesk-5.3.0/package/files/space-grotesk-latin-700-normal.woff2)}}
@font-face{{font-family:'JetBrains Mono';font-weight:500;src:url(file://{F}/fontsource-jetbrains-mono-5.3.0/package/files/jetbrains-mono-latin-500-normal.woff2)}}"""
names={"Main.dc.html":"c1-1"}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg=await b.new_page(viewport={"width":1080,"height":1350})
        for path in sorted(glob.glob(SRC+"/*.dc.html")):
            s=open(path).read()
            body=re.search(r"</helmet>(.*)</x-dc>",s,re.S).group(1).replace("{{accent}}","#C6F432")
            doc=f"<!doctype html><html lang='es'><head><meta charset='utf-8'><style>{ff} body{{margin:0}}</style></head><body>{body}</body></html>"
            tmp=OUT+"/_t.html"; open(tmp,"w").write(doc)
            await pg.goto("file://"+tmp); await pg.evaluate("document.fonts.ready")
            n=names.get(os.path.basename(path),os.path.basename(path).replace(".dc.html",""))
            await pg.screenshot(path=f"{OUT}/{n}.png",clip={"x":0,"y":0,"width":1080,"height":1350})
        await b.close()
asyncio.run(main())
