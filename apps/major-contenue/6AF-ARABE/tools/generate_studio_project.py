#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convertit les pages Cahier-V3-Cartoon-pages-A5/*.html
en un projet JSON importable dans Cahier Studio V2.
"""
import os, json, random, string, re
from bs4 import BeautifulSoup

PAGES_DIR = r"c:\Users\PC\Documents\Major-Contenue\6AF-ARABE\Cahier-V3-Cartoon-pages-A5"
OUT_FILE  = r"c:\Users\PC\Documents\Major-Contenue\6AF-ARABE\cahier-studio-v2\public\cahier_arabe_6af.json"

def uid():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

def clean(text):
    """Nettoie le texte extrait du HTML."""
    if not text: return ''
    return ' '.join(text.split()).strip()

# ── Positions automatiques ──────────────────────────────────────
# On dispose les blocs en colonne, avec un espacement vertical.

def layout_blocks(blocks):
    """Assigne x/y/w/h automatiquement selon le type de bloc."""
    y = 28  # on commence sous le header
    result = []
    for b in blocks:
        btype = b.get('type','exercise')
        bvar  = b.get('variant','cartoon')

        if btype == 'section':
            b.update({'x': 6, 'y': y, 'w': 118, 'h': 11, 'variant': 'section'})
            y += 14

        elif btype == 'rule':
            b.update({'x': 6, 'y': y, 'w': 124, 'h': 18, 'variant': 'rule'})
            y += 22

        elif btype == 'table':
            b.update({'x': 6, 'y': y, 'w': 124, 'h': 44, 'variant': 'soft'})
            y += 48

        elif btype == 'writing':
            b.update({'x': 6, 'y': y, 'w': 124, 'h': 28, 'variant': 'minimal'})
            y += 32

        elif bvar == 'wide':
            b.update({'x': 6, 'y': y, 'w': 124, 'h': 48, 'variant': 'cartoon'})
            y += 52

        else:  # exercice 2 colonnes
            b.update({'x': 6, 'y': y, 'w': 124, 'h': 46, 'variant': 'cartoon'})
            y += 50

        b['id'] = uid()
        result.append(b)

    return result


def parse_page(filepath, idx):
    """Extrait les blocs d'une page HTML."""
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Thème (bleu Arabe ou vert Islamique)
    brand = soup.find(class_='brand-sub')
    lesson = clean(brand.get_text()) if brand else 'Major 6AF'
    theme = 'green' if 'الإسلامية' in lesson or 'إسلام' in lesson else 'blue'

    # Numéro de page
    pg_num_el = soup.find(class_='page-num')
    pg_num = clean(pg_num_el.get_text()) if pg_num_el else str(idx)

    # Footer QR
    qr_text_el = soup.find(class_='qr-text')
    if qr_text_el:
        footer_txt = clean(qr_text_el.get_text(separator=' ', strip=True))
        # Prendre le chapitre (2e ligne)
        lines = [l for l in footer_txt.split() if l]
        footer = ' '.join(lines[:6]) if lines else lesson
    else:
        footer = lesson

    blocks_raw = []

    # ── Section pills (titres de section) ──
    for pill in soup.find_all(class_='sec-pill-wrap'):
        pill_el = pill.find(class_='sec-pill')
        if pill_el:
            title = clean(pill_el.get_text())
            blocks_raw.append({
                'type': 'section',
                'title': title or '✎ عنوان القسم',
                'text': '',
            })

    # ── Règles (قاعدة) ──
    for box in soup.find_all(class_='qaaida-box'):
        title_el = box.find(class_='qaaida-title')
        text_el  = box.find(class_='qaaida-text')
        title = clean(title_el.get_text()) if title_el else 'القاعدة'
        text  = clean(text_el.get_text(separator=' ')) if text_el else ''
        # Insérer AVANT les exercices — on les collecte d'abord, puis on trie
        blocks_raw.append({
            'type': 'rule',
            'title': title,
            'text': text[:180],   # limite pour ne pas déborder
        })

    # ── Exercices (exo-card) ──
    for card in soup.find_all(class_='exo-card'):
        instr_el = card.find(class_='exo-instr')
        ex_el    = card.find(class_='exo-example')
        table_el = card.find('table')
        write_el = card.find(class_='writing-area')

        instr = clean(instr_el.get_text()) if instr_el else ''
        example = clean(ex_el.get_text(separator=' ')) if ex_el else ''

        # Niveau
        lvl_el = card.find(class_=re.compile(r'exo-level|level-'))
        level  = clean(lvl_el.get_text()) if lvl_el else ''

        # Pts
        pts_el = card.find(class_='exo-pts')
        pts    = clean(pts_el.get_text()) if pts_el else '4 نقاط'

        if table_el:
            btype = 'table'
        elif write_el:
            btype = 'writing'
        else:
            btype = 'exercise'

        # Exercice large = pleine largeur (pas de grid2)
        is_wide = card.parent and 'grid2' not in (card.parent.get('class') or [])
        bvar = 'wide' if (is_wide and btype == 'exercise') else btype

        blocks_raw.append({
            'type': btype,
            'title': instr or 'أكمل ما يلي :',
            'text':  example[:120] if example else '',
            'level': level,
            'pts':   pts,
            'variant': bvar if bvar != btype else 'cartoon',
        })

    # ── Tri : sections > règles > exercices ──
    sections  = [b for b in blocks_raw if b['type'] == 'section']
    rules     = [b for b in blocks_raw if b['type'] == 'rule']
    exercises = [b for b in blocks_raw if b['type'] not in ('section','rule')]

    # Intercaler règle après chaque section
    ordered = []
    rule_idx = 0
    for s in sections:
        ordered.append(s)
        if rule_idx < len(rules):
            ordered.append(rules[rule_idx])
            rule_idx += 1
        # Prendre les exercices correspondants (2 par section max pour tenir en A5)
        batch = exercises[:2]
        exercises = exercises[2:]
        ordered.extend(batch)
    # Restes
    ordered.extend(exercises)

    blocks = layout_blocks(ordered)

    return {
        'id':     uid(),
        'title':  f'Page {idx:02d}',
        'theme':  theme,
        'lesson': lesson[:80],
        'footer': footer[:80],
        'blocks': blocks,
    }


def main():
    pages = []
    # Page 01 = couverture : on la garde vide stylisée
    cover = {
        'id':     uid(),
        'title':  'Couverture',
        'theme':  'blue',
        'lesson': 'اللغة العربية والتربية الإسلامية — 6AF',
        'footer': 'Major 6AF · دفتر التمارين',
        'blocks': [],
    }
    pages.append(cover)

    for i in range(2, 26):
        fn = f'page-{i:02d}.html'
        fp = os.path.join(PAGES_DIR, fn)
        if not os.path.exists(fp):
            print(f'  Skip {fn}')
            continue
        try:
            page = parse_page(fp, i)
            pages.append(page)
            nb = len(page['blocks'])
            print(f'  OK page-{i:02d} — {nb} blocs — thème {page["theme"]}')
        except Exception as e:
            print(f'  ERR page-{i:02d} : {e}')

    project = {'pages': pages}
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(project, f, ensure_ascii=False, indent=2)

    print(f'\nProjet généré : {OUT_FILE}')
    print(f'Total pages   : {len(pages)}')
    total_blocs = sum(len(p["blocks"]) for p in pages)
    print(f'Total blocs   : {total_blocs}')


if __name__ == '__main__':
    main()
