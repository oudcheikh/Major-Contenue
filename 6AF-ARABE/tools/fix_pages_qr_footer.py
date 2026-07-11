#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Cahier-V3-Cartoon-pages-A5 pages:
  • Ajoute un footer QR external (dans l'espace A5, hors du contenu scalé)
  • Le footer montre : QR code + chapitre + numéro de page
  • Met à jour le JS fitPage pour scaler le contenu au-dessus du footer
"""
import os, re

PAGES_DIR = r"c:\Users\PC\Documents\Major-Contenue\6AF-ARABE\Cahier-V3-Cartoon-pages-A5"

QR_FOOTER_CSS = """
/* ═══ QR Footer fixe dans l'espace A5 ═══ */
.qr-footer{position:absolute;bottom:0;left:0;right:0;height:18mm;display:flex;align-items:center;padding:0 5mm;gap:7px;direction:rtl;z-index:15;border-radius:10px 10px 0 0;overflow:hidden;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.qr-footer::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,#1e3a5f 0%,#2563eb 60%,#38bdf8 100%);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.qr-footer.islamic::before{background:linear-gradient(135deg,#064e3b 0%,#059669 60%,#34d399 100%)!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.qr-footer>*{position:relative;z-index:1}
.qr-footer-img{width:42px;height:42px;border-radius:5px;flex-shrink:0;background:#fff;padding:2px;display:block;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.qr-footer-text{flex:1;color:#fff;direction:rtl;text-align:right;line-height:1.35;font-family:'Cairo',sans-serif}
.qr-footer-text strong{display:block;font-size:9.5px;font-weight:900}
.qr-footer-text span{display:block;font-size:8px;opacity:.85;margin-top:2px}
.qr-footer-pgnum{font-size:11px;font-weight:900;color:rgba(255,255,255,.8);flex-shrink:0;direction:ltr;border:1.5px solid rgba(255,255,255,.35);border-radius:6px;padding:2px 8px;background:rgba(255,255,255,.12);white-space:nowrap;font-family:'Cairo',sans-serif}
@media print{.qr-footer{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}.qr-footer::before{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}.qr-footer-img{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}}
"""

# Ancien JS scaleByHeight (même dans toutes les pages)
JS_BEFORE = (
    '    const scaleByWidth = pageBox.width / Math.max(contentRight, innerBox.width);\n'
    '    const scaleByHeight = pageBox.height / contentBottom;'
)
# Nouveau JS avec soustraction de la hauteur du footer
JS_AFTER = (
    '    const qrFoot = document.querySelector(\'.page > .qr-footer\');\n'
    '    const footerH = qrFoot ? qrFoot.getBoundingClientRect().height : 0;\n'
    '    const scaleByWidth = pageBox.width / Math.max(contentRight, innerBox.width);\n'
    '    const scaleByHeight = (pageBox.height - footerH) / contentBottom;'
)

ANCHOR = '</div></div>\n<script>'  # fin print-scale-inner + fin page + début script


def extract_qr_src(content):
    """Extrait le src base64 du QR dans le qr-img-wrap."""
    m = re.search(r'class="qr-img-wrap"><img src="([^"]+)"', content)
    return m.group(1) if m else None


def process_page(filepath, page_idx):
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()

    content = raw.replace('\r\n', '\n')

    # Déjà traité ?
    if 'qr-footer' in content:
        print(f'  SKIP (déjà traité): {os.path.basename(filepath)}')
        return False

    # ── Métadonnées ──────────────────────────────────
    brand_m = re.search(r'class="brand-sub">([^<]+)<', content)
    brand_sub = brand_m.group(1).strip() if brand_m else ''

    pg_m = re.search(r'class="page-num">([^<]+)<', content)
    pg_num = pg_m.group(1).strip() if pg_m else f'{page_idx} / 25'

    qr_src = extract_qr_src(content)

    # Détection couleur (islamique = vert, arabe = bleu)
    is_islamic = ('التربية الإسلامية' in brand_sub
                  or 'border-color:#059669' in content
                  or (not brand_sub and page_idx >= 17))
    footer_class = 'qr-footer islamic' if is_islamic else 'qr-footer'

    # Affichage court du chapitre (après le tiret)
    if '&mdash;' in brand_sub:
        display_sub = brand_sub.split('&mdash;', 1)[1].strip()
    elif '—' in brand_sub:
        display_sub = brand_sub.split('—', 1)[1].strip()
    elif brand_sub:
        display_sub = brand_sub
    else:
        display_sub = 'Major 6AF · دفتر التمارين'

    # ── Construire le HTML du footer ─────────────────
    qr_img_html = (
        f'<img class="qr-footer-img" src="{qr_src}" alt="QR"/>'
        if qr_src else ''
    )
    footer_html = (
        f'<div class="{footer_class}">'
        + qr_img_html
        + '<div class="qr-footer-text">'
        + '<strong>&#128247; امسح الرمز بهاتفك</strong>'
        + f'<span>{display_sub}</span>'
        + '</div>'
        + f'<div class="qr-footer-pgnum">&#128209; {pg_num}</div>'
        + '</div>'
    )

    # ── 1. Injecter le CSS ───────────────────────────
    content = content.replace(
        '</style>\n</head>',
        QR_FOOTER_CSS + '</style>\n</head>',
        1
    )

    # ── 2. Injecter le footer HTML ───────────────────
    if ANCHOR not in content:
        print(f'  AVERTISSEMENT: ancre introuvable dans {os.path.basename(filepath)}')
        return False

    idx = content.rfind(ANCHOR)
    content = (
        content[:idx]
        + '</div>\n'
        + footer_html
        + '\n</div>\n<script>'
        + content[idx + len(ANCHOR):]
    )

    # ── 3. Mettre à jour le JS fitPage ───────────────
    if JS_BEFORE in content:
        content = content.replace(JS_BEFORE, JS_AFTER, 1)
    else:
        print(f'  AVERTISSEMENT: pattern JS introuvable dans {os.path.basename(filepath)}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True


def main():
    fixed = 0
    for i in range(2, 26):
        fn = f'page-{i:02d}.html'
        fp = os.path.join(PAGES_DIR, fn)
        if not os.path.exists(fp):
            print(f'Skip {fn} (introuvable)')
            continue
        ok = process_page(fp, i)
        if ok:
            print(f'OK {fn}')
            fixed += 1

    print(f'\nTermine! {fixed} pages corrigees.')


if __name__ == '__main__':
    main()
