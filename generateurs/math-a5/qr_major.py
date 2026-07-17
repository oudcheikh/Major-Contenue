# -*- coding: utf-8 -*-
"""QR codes réels du cahier → webapp Major (major-eval.vercel.app).

Chaque unité a deux QR :
  - leçon      /#/lesson/{id}      (carton أتعلّم : résumé, activités, vidéo)
  - correction /#/correction/{id}  (pages تمارين/مسائل : correction IA + QCM)

IDs : math6-u01..u31 (orange Major) · sci6-u1..u6 (vert Major).
La webapp doit contenir ces leçons AVANT impression (content-pack-6af-arabe).
"""
import base64
import io

import qrcode
from qrcode.constants import ERROR_CORRECT_M

BASE_URL = 'https://major-eval.vercel.app'
COLORS = {'math': '#ea580c', 'sci': '#059669', 'ar': '#7c3aed', 'isl': '#0d9488',
          'hg': '#b45309', 'civ': '#0f7b3a'}

_cache = {}


def unit_id(part, num):
    return {'math': f'math6-u{num:02d}', 'sci': f'sci6-u{num}',
            'ar': f'ar6-u{num:02d}', 'isl': f'isl6-u{num}',
            'hg': f'hg6-u{num:02d}', 'civ': f'civ6-u{num}'}[part]


def _qr_b64(url, color):
    key = (url, color)
    if key not in _cache:
        qr = qrcode.QRCode(error_correction=ERROR_CORRECT_M, box_size=8, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color=color, back_color='white')
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        _cache[key] = base64.b64encode(buf.getvalue()).decode('ascii')
    return _cache[key]


def lesson_qr_img(part, num):
    """<img> du QR leçon, même gabarit que le QR décoratif du video_box (.qr 12.5mm)."""
    url = f'{BASE_URL}/#/lesson/{unit_id(part, num)}'
    b64 = _qr_b64(url, COLORS[part])
    return (f'<img class="qr" src="data:image/png;base64,{b64}" '
            f'style="width:12.5mm;height:12.5mm;margin-top:.8mm;border-radius:1mm" '
            f'alt="QR درس {unit_id(part, num)}"/>')


def correction_qr_card(part, num):
    """Carte QR « correction » posée dans le coin inférieur gauche (zone du pied de page,
    sous le padding-bottom de 14mm de .sheet-inner → aucun chevauchement possible)."""
    url = f'{BASE_URL}/#/correction/{unit_id(part, num)}'
    b64 = _qr_b64(url, COLORS[part])
    color = COLORS[part]
    return (f'<div class="qr-corr" style="border-color:{color}66">'
            f'<img src="data:image/png;base64,{b64}" alt="QR تصحيح {unit_id(part, num)}"/>'
            f'<span style="color:{color}">📱 امسح للتصحيح والتدريب</span>'
            f'</div>')


def lesson_qr_card(part, num):
    """Carte QR « leçon » dans le coin inférieur gauche (même gabarit que
    correction_qr_card) — pour les pages أتعلّم dont le cadre est trop dense
    pour accueillir le video_box sans chevauchement."""
    url = f'{BASE_URL}/#/lesson/{unit_id(part, num)}'
    b64 = _qr_b64(url, COLORS[part])
    color = COLORS[part]
    return (f'<div class="qr-corr" style="border-color:{color}66">'
            f'<img src="data:image/png;base64,{b64}" alt="QR درس {unit_id(part, num)}"/>'
            f'<span style="color:{color}">📱 امسح لفيديو الشرح</span>'
            f'</div>')
