# -*- coding: utf-8 -*-
"""Assemble les 25 pages corrigées en UN seul HTML (police embarquée 1x).
   - <head> partagé pris sur une page de contenu (CSS générique, sans règle couverture)
   - chaque .page reçoit un id pgN ; les pages à dégradé sont scopées par id (pas de bleed)
"""
import io, re, glob, os, json

SRC = "Cahier-V3-Cartoon-pages-A5"
files = sorted(glob.glob(os.path.join(SRC, "page-*.html")))
assert len(files) == 25
SCALES = json.load(io.open(os.path.join(SRC, "_scales.json")))  # echelle figee par page

def read(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()

# head partagé = celui d'une page de CONTENU (pas de règle .page{gradient})
head = re.search(r"<head>(.*?)</head>", read(os.path.join(SRC,"page-02.html")), re.DOTALL).group(1)

bodies, cover_rules, scale_rules = [], [], []
for i, p in enumerate(files, 1):
    html = read(p)
    body = re.search(r"<body[^>]*>(.*?)</body>", html, re.DOTALL).group(1).strip()
    # injecter id="pgN" dans le 1er <div class="page"
    body = re.sub(r'<div class="page"', f'<div id="pg{i}" class="page"', body, count=1)
    bodies.append(body)
    # echelle figee PAR PAGE (le <head> partagé ne porte qu'une seule valeur -> on scope par id)
    s = SCALES.get(os.path.basename(p), round(148/210*0.985, 4))
    scale_rules.append(f"#pg{i} > .print-scale-inner{{--page-scale:{s} !important}}")
    # dégradé inline éventuel -> règle scopée par id
    m = re.search(r'<div id="pg%d" class="page"[^>]*style="([^"]*)"' % i, body)
    if m:
        decls = [d.strip() for d in m.group(1).split(';') if d.strip()]
        bg = next((d for d in decls if d.lower().startswith('background') and 'gradient' in d.lower()), None)
        if bg:
            cover_rules.append(
                f"#pg{i}{{{bg} !important}}"
                f"#pg{i} > .print-scale-inner{{background:transparent !important;padding:0 !important;"
                f"display:flex !important;flex-direction:column !important;justify-content:center !important}}")

multipage = ("<style>\n/* multipage : laisser les 25 pages se paginer (sinon body height:210mm + overflow:hidden ne montre qu'1 page) */\n"
             "@media screen{html,body{height:auto !important;min-height:auto !important;overflow:auto !important}}\n"
             "@media print{html,body{height:auto !important;min-height:auto !important;overflow:visible !important}}\n"
             "/* inner en FLUX (pas position:absolute) : Chrome clippe les éléments absolus aux\n"
             "   frontières de page lors de la pagination multi-pages. En RTL un bloc plus large\n"
             "   que son parent s'ancre à DROITE (déborde à gauche) -> transform-origin:top right\n"
             "   remappe 210mm->148mm sans décalage. .page{height:210mm;overflow:hidden} clippe le reste. */\n"
             ".page > .print-scale-inner{position:static !important;transform-origin:top right !important;"
             "top:auto !important;right:auto !important;left:auto !important;bottom:auto !important;margin:0 !important}\n"
             ".page{overflow:hidden !important}\n</style>")

scoped = ("<style>\n/* echelle figee par page (id > .class bat le head partagé) */\n" + "\n".join(scale_rules) + "\n</style>"
          + "<style>\n/* dégradés couverture scopés (anti-bleed) */\n" + "\n".join(cover_rules) + "\n</style>"
          + multipage)

doc = ("<!DOCTYPE html>\n<html lang=\"ar\" dir=\"rtl\">\n<head>"
       + head + scoped + "</head>\n<body>\n"
       + "\n".join(bodies) + "\n</body>\n</html>\n")

# Le combiné est dans Studio/ (un niveau au-dessus des pages individuelles).
# Les overlays (spirale, textures) sont en 6AF-ARABE/assets/ -> depuis Studio/ c'est ../assets/
# alors que les pages individuelles utilisent ../../assets/. On corrige la profondeur.
doc = doc.replace("../../assets/", "../assets/")

out = "Cahier-Major-LangueArabe-Islamique-6AF-A5.html"
with io.open(out, "w", encoding="utf-8") as f:
    f.write(doc)
print("OK ->", out, "| pages combinées:", len(bodies), "| dégradés scopés:", len(cover_rules))
