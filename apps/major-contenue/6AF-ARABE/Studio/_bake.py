# -*- coding: utf-8 -*-
"""Reconstruit les 25 pages live À PARTIR DES ORIGINAUX (design d'origine correct) :
   - retire le moteur JS (qui plante en print headless -> fallback 0.7047 -> overlap)
   - FIGE le --page-scale mesuré par page (contenu scalé pour tenir AU-DESSUS du qr-footer)
   - garde le qr-footer slim d'origine en bas (QR taille constante, scannable)
   - couvertures : dégradé plein cadre + hero centré
"""
import io, os, re, glob, json

LIVE = "Cahier-V3-Cartoon-pages-A5"
SRC  = os.path.join(LIVE, "_A4_source_backup")
SCALES = json.load(io.open(os.path.join(LIVE, "_scales.json")))

JS_RE = re.compile(r"<script>\s*\(\(\)\s*=>\s*\{.*?BASE_SCALE.*?\}\)\(\);\s*</script>", re.DOTALL)

def cover_gradient(html):
    m = re.search(r'<div class="page"[^>]*?style="([^"]*)"', html)
    if not m:
        return None
    decls = [d.strip() for d in m.group(1).split(';') if d.strip()]
    return next((d for d in decls if d.lower().startswith('background') and 'gradient' in d.lower()), None)

def bake(name):
    html = io.open(os.path.join(SRC, name), encoding="utf-8").read()
    html = JS_RE.sub("", html)                       # retirer le JS
    s = SCALES.get(name, round(148/210*0.985, 4))
    grad = cover_gradient(html)
    rules = [".page > .print-scale-inner{--page-scale:%s !important}" % s]
    if grad:
        rules.append(".page{%s !important;display:flex !important;flex-direction:column !important;"
                     "align-items:center !important;justify-content:center !important}" % grad)
        rules.append(".page > .print-scale-inner{background:transparent !important;padding:0 !important;"
                     "display:flex !important;flex-direction:column !important;justify-content:center !important}")
    style = '<style id="major-a5-bake">\n/* echelle figee A5 (sans JS) */\n' + "\n".join(rules) + "\n</style>\n</head>"
    if "major-a5-bake" not in html:
        html = html.replace("</head>", style, 1)
    io.open(os.path.join(LIVE, name), "w", encoding="utf-8").write(html)
    return s, ("COUVERTURE" if grad else "contenu")

if __name__ == "__main__":
    for name in sorted(os.path.basename(p) for p in glob.glob(os.path.join(SRC, "page-*.html"))):
        s, kind = bake(name)
        print(f"{name}: scale={s}  ({kind})")
    print("OK -> 25 pages live reconstruites depuis les originaux + scale figé")
