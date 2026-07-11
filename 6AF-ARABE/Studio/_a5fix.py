# -*- coding: utf-8 -*-
"""Correctif déterministe A4->A5 pour les pages du Cahier V3 Cartoon.
   - supprime le moteur de scaling JS (fragile, casse en export PDF)
   - injecte un bloc CSS final qui scale le bloc A4 entier par 0.70476
   - affiche le QR interne (.qr-strip) en bas du contenu scalé
   - masque le footer externe dupliqué (.qr-footer) et déco écran
"""
import io, re, sys

OVERRIDE = """
<style id="major-a5-fix">
/* ===== MAJOR A5 PRINT FIX — déterministe, sans JS ===== */
@media screen {
  html, body { width:auto !important; height:auto !important; overflow:auto !important;
    background:#e5e7eb !important; margin:0 !important; padding:16px 0 !important; }
  .page { position:relative !important; width:148mm !important; height:210mm !important;
    min-height:210mm !important; margin:0 auto !important; padding:0 !important;
    overflow:hidden !important; transform:none !important; inset:auto !important;
    box-shadow:0 6px 36px rgba(0,0,0,.18) !important; }
}
@media print {
  @page { size:A5 portrait; margin:0; }
  html, body { width:148mm !important; height:210mm !important; margin:0 !important;
    padding:0 !important; background:#fff !important; overflow:hidden !important; }
  .page { position:relative !important; width:148mm !important; height:210mm !important;
    min-height:210mm !important; margin:0 !important; padding:0 !important;
    overflow:hidden !important; transform:none !important; inset:auto !important;
    box-shadow:none !important; page-break-after:always !important; break-after:page !important; }
  .page:last-child { page-break-after:auto !important; break-after:auto !important; }
}
/* le calque A4 scalé en A5 (écran + impression, valeur FIXE) */
.page > .print-scale-inner {
  position:absolute !important; top:0 !important; right:0 !important; left:auto !important; bottom:auto !important;
  width:210mm !important; height:297mm !important;
  padding:6mm 20mm 30mm 9mm !important; box-sizing:border-box !important;
  transform:scale(.70476) !important; transform-origin:top right !important;
  overflow:hidden !important; background:inherit !important; }
/* QR visible en bas du contenu scalé ; on tue le footer externe dupliqué */
.qr-strip { display:flex !important; position:absolute !important;
  bottom:7mm !important; left:9mm !important; right:20mm !important; margin:0 !important; }
.qr-footer, .wave-footer, .page-num, .cartoon-illus, .page-sticker { display:none !important; }
.spiral-strip { display:block !important; }
* { -webkit-print-color-adjust:exact !important; print-color-adjust:exact !important; }
</style>
</head>"""

def cover_rule(html):
    """Si .page a un fond dégradé inline (couverture/4e de couv), le forcer en !important
       car la règle existante .page{background:#FAF6EE!important} l'écrase sinon."""
    m = re.search(r'class="page"[^>]*?style="([^"]*)"', html)
    if not m:
        return ""
    decls = [d.strip() for d in m.group(1).split(';') if d.strip()]
    bg = next((d for d in decls if d.lower().startswith('background') and 'gradient' in d.lower()), None)
    if not bg:
        return ""
    return ("\n/* page spéciale : fond dégradé pleine page + hero centré vertical */\n"
            ".page{%s !important}\n"
            ".page > .print-scale-inner{background:transparent !important;padding:0 !important;"
            "display:flex !important;flex-direction:column !important;justify-content:center !important}\n" % bg)

def fix_html(html):
    # 1) retirer le moteur JS (IIFE contenant BASE_SCALE) + sa balise script
    html = re.sub(r"<script>\s*\(\(\)\s*=>\s*\{.*?BASE_SCALE.*?\}\)\(\);\s*</script>",
                  "", html, flags=re.DOTALL)
    # 2) construire l'override (+ règle couverture éventuelle) et l'injecter avant </head>
    if "major-a5-fix" not in html:
        override = OVERRIDE.replace("</style>\n</head>", cover_rule(html) + "</style>\n</head>")
        html = html.replace("</head>", override, 1)
    return html

if __name__ == "__main__":
    path = sys.argv[1]
    out  = sys.argv[2] if len(sys.argv) > 2 else path
    with io.open(path, encoding="utf-8") as f:
        html = f.read()
    new = fix_html(html)
    with io.open(out, "w", encoding="utf-8") as f:
        f.write(new)
    print("OK ->", out, "| script retiré:", "BASE_SCALE" not in new)
