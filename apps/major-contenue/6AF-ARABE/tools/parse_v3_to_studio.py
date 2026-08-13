#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convertit Cahier-Major-LangueArabe-Islamique-6AF-V3-Cartoon.html
→ project JSON pour Cahier Studio V2 (blocs avec HTML réel).
"""
import os, json, random, string, re
from bs4 import BeautifulSoup, NavigableString

SRC  = r"c:\Users\PC\Documents\Major-Contenue\6AF-ARABE\Cahier-Major-LangueArabe-Islamique-6AF-V3-Cartoon.html"
OUT  = r"c:\Users\PC\Documents\Major-Contenue\6AF-ARABE\cahier-studio-v2\dist\v3cartoon.json"

def uid():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

def clean(t):
    return ' '.join((t or '').split()).strip()

# ─── Estimateur de positions (layout A4 → positions absolues) ───────────────
# Zone utile: left=7mm right=17mm top=29mm bottom=22mm
# Largeur utile = 210-7-17 = 186mm (A4). Hauteur utile = 297-29-22 = 246mm

X0 = 7    # marge gauche mm
W  = 182  # largeur totale utile mm (A4)
Y0 = 29   # départ sous header mm

BLOCK_HEIGHTS = {
    'section':  11,
    'rule':     20,
    'exercise': 52,
    'wide':     52,
    'table':    52,
    'writing':  34,
}
GAP = 5   # espace entre blocs mm

def assign_positions(raw_blocks):
    """Attribue x/y/w/h en mm (espace A4) à chaque bloc."""
    result = []
    y = Y0

    i = 0
    while i < len(raw_blocks):
        b = raw_blocks[i]
        btype = b['type']
        h = BLOCK_HEIGHTS.get(btype, 50)

        # Si c'est un exercice en grille 2, prendre le suivant aussi
        if btype == 'exercise' and i + 1 < len(raw_blocks) and raw_blocks[i+1]['type'] == 'exercise':
            b2 = raw_blocks[i+1]
            half = (W - 4) // 2
            b.update( {'id':uid(),'x':X0,        'y':y, 'w':half, 'h':h})
            b2.update({'id':uid(),'x':X0+half+4, 'y':y, 'w':half, 'h':h})
            result.append(b)
            result.append(b2)
            y += h + GAP
            i += 2
        else:
            b.update({'id': uid(), 'x': X0, 'y': y, 'w': W, 'h': h})
            result.append(b)
            y += h + GAP
            i += 1

    return result


def extract_blocks(page_div):
    """Extrait les blocs d'un .page div, retourne liste de dicts."""
    skip_classes = {
        'spiral-strip','ring','blob-wrap','page-header',
        'qr-strip','wave-footer','page-num','cartoon-illus','page-sticker',
    }
    raw = []

    for child in page_div.children:
        if isinstance(child, NavigableString):
            continue
        classes = set(child.get('class') or [])

        if classes & skip_classes:
            continue

        # Section pill
        if 'sec-pill-wrap' in classes:
            pill = child.find(class_='sec-pill')
            raw.append({
                'type': 'section',
                'html': str(child),
                'title': clean(pill.get_text()) if pill else '✎ عنوان',
            })

        # Règle (qaaida)
        elif 'qaaida-box' in classes:
            title_el = child.find(class_='qaaida-title')
            raw.append({
                'type': 'rule',
                'html': str(child),
                'title': clean(title_el.get_text()) if title_el else 'القاعدة',
            })

        # Grille 2 colonnes d'exercices
        elif 'grid2' in classes:
            cards = child.find_all(class_='exo-card', recursive=False)
            for card in cards:
                instr = card.find(class_='exo-instr')
                raw.append({
                    'type': 'exercise',
                    'html': str(card),
                    'title': clean(instr.get_text()) if instr else 'تمرين',
                })

        # Exercice pleine largeur (hors grid2)
        elif 'exo-card' in classes:
            instr = child.find(class_='exo-instr')
            raw.append({
                'type': 'wide',
                'html': str(child),
                'title': clean(instr.get_text()) if instr else 'تمرين',
            })

    return raw


def parse_v3(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Extraire le CSS V3-Cartoon (tous les <style>)
    css_parts = []
    for s in soup.find_all('style'):
        css_parts.append(s.string or '')
    css = '\n'.join(css_parts)

    # Corriger les chemins assets pour le serveur Studio
    css = css.replace("url('assets/", "url('/assets/")
    css = css.replace('url("assets/', 'url("/assets/')
    css = css.replace("url(assets/", "url(/assets/")

    # Supprimer les règles qui entrent en conflit avec le Studio
    # (tailles de .page, body, html)
    import re as _re
    css = _re.sub(r'body\s*\{[^}]*\}', '', css)
    css = _re.sub(r'html\s*,\s*body[^{]*\{[^}]*\}', '', css)
    css = _re.sub(r'@media\s+print\s*\{[^}]*(?:\{[^}]*\}[^}]*)*\}', '', css, flags=_re.DOTALL)

    pages = []
    for page_num, page_div in enumerate(soup.find_all(class_='page')):
        # En-tête
        header = page_div.find(class_='page-header')
        brand_name = header.find(class_='brand-name') if header else None
        brand_sub  = header.find(class_='brand-sub')  if header else None
        lesson = clean(brand_sub.get_text()) if brand_sub else 'Major 6AF'

        # Thème
        header_classes = header.get('class', []) if header else []
        theme = 'green' if 'islamic' in header_classes else 'blue'
        if 'التربية الإسلامية' in lesson or 'إسلام' in lesson:
            theme = 'green'

        # QR footer
        qr_strip = page_div.find(class_='qr-strip')
        qr_text_el = qr_strip.find(class_='qr-text') if qr_strip else None
        if qr_text_el:
            lines = clean(qr_text_el.get_text(separator='\n')).split('\n')
            footer_txt = lines[0] if lines else lesson
        else:
            footer_txt = lesson

        # Page-num
        pn_el = page_div.find(class_='page-num')
        pg_label = clean(pn_el.get_text()) if pn_el else str(page_num)

        # Extraire les blocs
        raw_blocks = extract_blocks(page_div)
        blocks = assign_positions(raw_blocks)

        pages.append({
            'id':     uid(),
            'title':  f'Page {page_num:02d}' if page_num > 0 else 'Couverture',
            'theme':  theme,
            'lesson': lesson[:90],
            'footer': footer_txt[:90],
            'pageLabel': pg_label,
            'blocks': blocks,
        })

        nb = len(blocks)
        print(f'  page {page_num:02d}: {nb:2d} blocs - {theme:5s}')

    return {'pages': pages, 'css': css}


def main():
    print(f'Parsing {os.path.basename(SRC)} ...')
    project = parse_v3(SRC)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(project, f, ensure_ascii=False, indent=2)

    total_blocks = sum(len(p['blocks']) for p in project['pages'])
    size_kb = os.path.getsize(OUT) // 1024
    print(f'\nOK -> {OUT}')
    print(f'     {len(project["pages"])} pages · {total_blocks} blocs · {size_kb} KB')


if __name__ == '__main__':
    main()
