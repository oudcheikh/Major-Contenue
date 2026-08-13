#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Correction v3 pour les pages A5 :
  - Mesure de contentBottom avec buffer de marge (marges non incluses dans bbox)
  - el.closest() pour exclure correctement les descendants des elements decoratifs
  - GAP proportionnel a la hauteur de la page (5mm)
  - html overflow:hidden pour eliminer le scroll en mode ecran
"""
import os, re

PAGES_DIR = r"c:\Users\PC\Documents\Major-Contenue\6AF-ARABE\Cahier-V3-Cartoon-pages-A5"

NEW_JS_BLOCK = """<script>
(() => {
  const BASE_SCALE = 148 / 210;
  const DECO = ['wave-footer','page-num','qr-strip','blob-wrap','spiral-strip'];

  const resetPageTransform = () => {
    const p = document.querySelector('.page');
    if (p) { p.style.transform = 'none'; p.style.marginBottom = '0'; p.style.marginTop = '4px'; }
  };

  const fitPage = () => {
    const page   = document.querySelector('.page');
    const inner  = document.querySelector('.page > .print-scale-inner');
    const footer = document.querySelector('.page > .qr-footer');
    if (!page || !inner) return;

    inner.style.transform = 'none';
    const pageBox  = page.getBoundingClientRect();
    const innerBox = inner.getBoundingClientRect();
    const footerH  = footer ? footer.getBoundingClientRect().height : 0;

    let contentBottom = 0;
    let contentRight  = innerBox.width;

    inner.querySelectorAll('*').forEach((el) => {
      const st = getComputedStyle(el);
      if (st.display === 'none' || st.visibility === 'hidden') return;
      // Exclure les elements decoratifs ET tous leurs descendants
      if (DECO.some(c => el.closest('.' + c))) return;
      const box = el.getBoundingClientRect();
      contentBottom = Math.max(contentBottom, box.bottom - innerBox.top);
      contentRight  = Math.max(contentRight,  box.right  - innerBox.left);
    });

    if (contentBottom < 10) contentBottom = innerBox.height;

    // Buffer : les marges (margin-bottom) ne sont pas incluses dans getBoundingClientRect
    // On ajoute 28px (~7mm) pour couvrir les marges entre blocs
    contentBottom += 28;

    // GAP = 5mm proportionnel a la hauteur reelle de la page
    const GAP = pageBox.height * (5 / 210);
    const availH         = pageBox.height - footerH - GAP;
    const maxScaleFooter = availH / contentBottom;
    const scaleByWidth   = pageBox.width / Math.max(contentRight, innerBox.width);
    const scaleByHeight  = pageBox.height / contentBottom;
    const scale = Math.min(BASE_SCALE, scaleByWidth, scaleByHeight, maxScaleFooter) * 0.995;

    inner.style.setProperty('--page-scale', String(scale));
    inner.style.transform = '';
  };

  const fitViewport = () => {
    const page = document.querySelector('.page');
    if (!page) return;
    const s = Math.min(1,
      (window.innerWidth  - 8) / page.offsetWidth,
      (window.innerHeight - 8) / page.offsetHeight
    );
    page.style.transform       = 'scale(' + s.toFixed(3) + ')';
    page.style.transformOrigin = 'top center';
    page.style.marginTop       = '4px';
    page.style.marginBottom    = ((s - 1) * page.offsetHeight) + 'px';
    // Empecher le scroll : ajuster la hauteur de html a la taille visuelle de la page
    document.documentElement.style.height   = (8 + Math.round(page.offsetHeight * s)) + 'px';
    document.documentElement.style.overflow = 'hidden';
  };

  const run      = () => { resetPageTransform(); fitPage(); fitViewport(); };
  const runPrint = () => { resetPageTransform(); fitPage(); };

  window.addEventListener('load',        run);
  window.addEventListener('resize',      run);
  window.addEventListener('beforeprint', runPrint);
  document.fonts && document.fonts.ready.then(run);
})();
</script>"""

EXTRA_CSS = """
/* Masquer wave-footer et page-num (redondants avec le qr-footer externe) */
.wave-footer { display:none !important; }
.page-num    { display:none !important; }
"""


def process_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()
    content = raw.replace('\r\n', '\n')

    changed = False

    # Remplacer le bloc <script>...</script>
    new_content, n = re.subn(
        r'<script>\s*\(\(\) => \{.*?\}\)\(\);\s*</script>',
        NEW_JS_BLOCK,
        content,
        count=1,
        flags=re.DOTALL
    )
    if n:
        content = new_content
        changed = True
    else:
        print(f'  WARN: script non trouve dans {os.path.basename(filepath)}')

    # Ajouter CSS si absent
    if '.wave-footer { display:none' not in content:
        idx = content.rfind('</style>\n</head>')
        if idx != -1:
            content = content[:idx] + EXTRA_CSS + '</style>\n</head>' + content[idx + len('</style>\n</head>'):]
            changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    return changed


def main():
    fixed = 0
    for i in range(1, 26):
        fn = f'page-{i:02d}.html'
        fp = os.path.join(PAGES_DIR, fn)
        if not os.path.exists(fp):
            continue
        ok = process_page(fp)
        print(f'{"OK" if ok else "SKIP"} {fn}')
        if ok:
            fixed += 1
    print(f'\nTermine: {fixed} pages.')


if __name__ == '__main__':
    main()
