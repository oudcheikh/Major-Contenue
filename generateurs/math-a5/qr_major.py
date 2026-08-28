# -*- coding: utf-8 -*-
"""QR codes réels du cahier → webapp Major (major-eval.vercel.app).

Chaque unité a deux QR :
  - leçon      /#/lesson/{id}      (carton أتعلّم : résumé, activités, vidéo)
  - correction /#/correction/{id}  (pages تمارين/مسائل : correction IA + QCM)

IDs : math6-u01..u31 (orange Major) · sci6-u1..u6 (vert Major) · fr6-u01..u29 (bleu français).
La webapp doit contenir ces leçons AVANT impression (content-pack-6af-arabe).
"""
import base64
import io

import qrcode
from qrcode.constants import ERROR_CORRECT_Q

BASE_URL = 'https://major-eval.vercel.app'
COLORS = {'math': '#ea580c', 'sci': '#059669', 'ar': '#7c3aed', 'isl': '#0d9488',
          'hg': '#b45309', 'civ': '#0f7b3a', 'fr': '#0284c7'}

_cache = {}


def unit_id(part, num):
    return {'math': f'math6-u{num:02d}', 'sci': f'sci6-u{num}',
            'ar': f'ar6-u{num:02d}', 'isl': f'isl6-u{num}',
            'hg': f'hg6-u{num:02d}', 'civ': f'civ6-u{num}',
            'fr': f'fr6-u{num:02d}'}[part]


def _qr_b64(url, color):
    key = (url, color, 'Q')
    if key not in _cache:
        qr = qrcode.QRCode(error_correction=ERROR_CORRECT_Q, box_size=10, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color=color, back_color='white')
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        _cache[key] = base64.b64encode(buf.getvalue()).decode('ascii')
    return _cache[key]


def lesson_qr_img(part, num):
    """<img> du QR leçon (gabarit video_box ~15.5mm)."""
    uid = unit_id(part, num)
    url = f'{BASE_URL}/#/lesson/{uid}'
    b64 = _qr_b64(url, COLORS[part])
    alt = f'QR leçon {uid}' if part == 'fr' else f'QR درس {uid}'
    return (f'<img class="qr" src="data:image/png;base64,{b64}" '
            f'style="width:15.5mm;height:15.5mm;margin-top:.4mm" '
            f'alt="{alt}"/>')


def correction_qr_card(part, num):
    """Carte QR « correction » posée dans le coin inférieur gauche (zone du pied de page,
    sous le padding-bottom de 14mm de .sheet-inner → aucun chevauchement possible)."""
    uid = unit_id(part, num)
    url = f'{BASE_URL}/#/correction/{uid}'
    b64 = _qr_b64(url, COLORS[part])
    color = COLORS[part]
    cap = 'Scanne pour la correction' if part == 'fr' else 'امسح للتصحيح والتدريب'
    alt = f'QR correction {uid}' if part == 'fr' else f'QR تصحيح {uid}'
    return (f'<div class="qr-corr" style="border-color:{color}66">'
            f'<img src="data:image/png;base64,{b64}" alt="{alt}"/>'
            f'<span style="color:{color}">{cap}</span>'
            f'</div>')


def lesson_qr_card(part, num):
    """Carte QR « leçon » dans le coin inférieur gauche (même gabarit que
    correction_qr_card) — pour les pages أتعلّم dont le cadre est trop dense
    pour accueillir le video_box sans chevauchement."""
    uid = unit_id(part, num)
    url = f'{BASE_URL}/#/lesson/{uid}'
    b64 = _qr_b64(url, COLORS[part])
    color = COLORS[part]
    cap = 'Scanne pour le cours' if part == 'fr' else 'امسح لفيديو الشرح'
    alt = f'QR leçon {uid}' if part == 'fr' else f'QR درس {uid}'
    return (f'<div class="qr-corr" style="border-color:{color}66">'
            f'<img src="data:image/png;base64,{b64}" alt="{alt}"/>'
            f'<span style="color:{color}">{cap}</span>'
            f'</div>')
