# -*- coding: utf-8 -*-
"""Mesure la HAUTEUR NATURELLE du contenu de chaque page (transform off, height auto),
   via scrollHeight (insensible aux transforms / taille fenêtre, en px CSS @96dpi).
   Puis calcule un --page-scale déterministe qui fait tenir le contenu AU-DESSUS du
   qr-footer (18mm) -> plus d'overlap. Sortie: _scales.json
"""
import io, os, re, glob, json, subprocess, sys

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
LIVE   = "Cahier-V3-Cartoon-pages-A5"
SRC    = os.path.join(LIVE, "_A4_source_backup")

PXMM      = 96.0 / 25.4          # 3.7795 px CSS par mm @96dpi
BASE      = 148.0 / 210.0        # 0.70476 (cap : largeur A4->A5)
A5_H      = 210.0                # mm
FOOTER_MM = 18.0                 # hauteur qr-footer externe
GAP_MM    = 5.0                  # respiration contenu/footer
SAFETY    = 0.985
AVAIL_MM  = A5_H - FOOTER_MM - GAP_MM   # 187mm dispo pour le contenu scalé

PROBE = """
<script>
(function(){
  function emit(){
    var inn=document.querySelector(".page > .print-scale-inner");
    if(!inn){document.title="CH=ERR";return;}
    inn.style.setProperty("transform","none","important");
    inn.style.setProperty("height","auto","important");
    inn.style.setProperty("min-height","0","important");
    inn.style.setProperty("padding-bottom","0","important");
    void inn.offsetHeight;            // force reflow
    document.title="CH="+inn.scrollHeight;
  }
  if(document.fonts&&document.fonts.ready){document.fonts.ready.then(function(){setTimeout(emit,500);});}
  window.addEventListener("load",function(){setTimeout(emit,1000);});
  setTimeout(emit,3500);
})();
</script>
"""

def content_px(src_page):
    html = io.open(src_page, encoding="utf-8").read()
    html = html.replace("</body>", PROBE + "</body>", 1)
    tmp = os.path.join(LIVE, "_m_tmp.html")
    io.open(tmp, "w", encoding="utf-8").write(html)
    url = "file:///" + os.path.abspath(tmp).replace("\\", "/")
    try:
        out = subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
             "--virtual-time-budget=9000", "--dump-dom", url],
            capture_output=True, text=True, timeout=60, encoding="utf-8", errors="ignore"
        ).stdout or ""
    finally:
        try: os.remove(tmp)
        except OSError: pass
    m = re.search(r"CH=(\d+)", out)
    return int(m.group(1)) if m else None

def scale_for(px):
    content_mm = px / PXMM
    s = min(BASE, AVAIL_MM / content_mm) * SAFETY
    return round(max(0.30, s), 4), round(content_mm, 1)

def main():
    pages = sorted(glob.glob(os.path.join(SRC, "page-*.html")))
    assert len(pages) == 25, len(pages)
    only = sys.argv[1] if len(sys.argv) > 1 else None
    res = {}
    for p in pages:
        name = os.path.basename(p)
        if only and only not in name:
            continue
        px = content_px(p)
        if px is None:
            print(f"{name}: MESURE ECHOUEE"); continue
        s, cmm = scale_for(px)
        res[name] = s
        flag = "  <-- shrink" if s < BASE * SAFETY - 1e-4 else ""
        print(f"{name}: contenu={cmm}mm  px={px}  scale={s}{flag}")
        sys.stdout.flush()
    if not only:
        json.dump(res, io.open(os.path.join(LIVE, "_scales.json"), "w"), indent=0)
        print("--- ecrit:", os.path.join(LIVE, "_scales.json"))

if __name__ == "__main__":
    main()
