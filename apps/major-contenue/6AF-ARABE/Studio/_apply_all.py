# -*- coding: utf-8 -*-
import io, os, glob, shutil
from _a5fix import fix_html

SRC = "Cahier-V3-Cartoon-pages-A5"
BAK = os.path.join(SRC, "_A4_source_backup")
os.makedirs(BAK, exist_ok=True)

pages = sorted(glob.glob(os.path.join(SRC, "page-*.html")))
for p in pages:
    name = os.path.basename(p)
    bak = os.path.join(BAK, name)
    # sauvegarde unique (ne pas écraser un backup déjà fait)
    if not os.path.exists(bak):
        shutil.copy2(p, bak)
    with io.open(p, encoding="utf-8") as f:
        html = f.read()
    new = fix_html(html)
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(new)
    flag = "déjà-corrigé" if new == html else "corrigé"
    print(f"{name}: {flag} (js retiré: {'BASE_SCALE' not in new})")

print(f"\n{len(pages)} pages traitées. Backups -> {BAK}")
