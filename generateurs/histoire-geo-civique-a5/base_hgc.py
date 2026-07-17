# -*- coding: utf-8 -*-
"""Socle du cahier A5 التاريخ والجغرافيا · التربية المدنية — même style « carnet
relié » que le cahier arabe-islamique (base_ai), avec 3 onglets de partie :
تاريخ (ambre) · جغرافيا (bleu) · تربية مدنية (vert), et des composants visuels
(fig SVG, carte à compléter). Les cartes/frises viennent d'assets_hgc.py."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, '..', 'arabe-islamique-a5')))

# tout le kit de composants du cahier arabe-islamique (mêmes signatures)
from base_ai import (CSS, CSS_ASSETS, OVAL, OVS,  # noqa: F401
                     badge_row, video_box, tok, exo, consigne, dots, wlines,
                     objectifs, methode, astuce, attention, defi, bulle,
                     self_eval, unit_banner, ai_table, ayah, spine)

DOC_ID = 'دفتر ماجور · التاريخ والجغرافيا والتربية المدنية<br>السنة السادسة الأساسية 6AF'

# ── 3 parties : تاريخ ambre · جغرافيا bleu · مدنية vert ──
CSS_HGC = """
.part-hist{--part:#b45309;--part-lite:#f59e0b;--part-soft:#fdf3e3;--part-border:#f3c98a}
.part-geo{--part:#1d4ed8;--part-lite:#60a5fa;--part-soft:#eaf1fe;--part-border:#a8c6f5}
.part-civ{--part:#0f7b3a;--part-lite:#34d399;--part-soft:#e9f7ee;--part-border:#93dcb4}
/* figure : illustration SVG + légende */
.fig{
  background:#fff;border:.4mm solid rgba(17,24,39,.1);border-radius:3.5mm;
  border-top:1.2mm solid var(--part);padding:1.8mm 2mm 1.2mm;margin:1.4mm 0;
  text-align:center;box-shadow:0 1.5px 5px rgba(17,24,39,.05);
}
.fig svg{width:100%;height:auto;display:block}
.fig .fig-cap{
  font-size:7.2px;font-weight:900;color:var(--part);margin-top:.8mm;
  display:flex;align-items:center;justify-content:center;gap:1.5mm;
}
.fig.exercice{border-style:dashed;border-width:.55mm;border-top-width:1.2mm}
.fig.exercice .fig-cap{color:#c0392b}
/* deux figures côte à côte */
.fig-row{display:grid;grid-template-columns:1fr 1fr;gap:2.4mm}
"""


def fig(svg, caption, exercice=False, width=''):
    """Illustration SVG encadrée avec légende. exercice=True → cadre pointillé
    (l'élève complète le fond de carte). width ex. '78mm' pour réduire."""
    cls = 'fig exercice' if exercice else 'fig'
    st = f' style="width:{width};margin-inline:auto"' if width else ''
    ic = '✏️' if exercice else '🗺️'
    return (f'<div class="{cls}"{st}>{svg}'
            f'<div class="fig-cap">{ic} {caption}</div></div>')


def tabs3(part):
    h = ' tab-active' if part == 'hist' else ''
    g = ' tab-active' if part == 'geo' else ''
    c = ' tab-active' if part == 'civ' else ''
    return (f'<div class="tabs">'
            f'<div class="tab{h}" style="background:#b45309">التاريخ</div>'
            f'<div class="tab{g}" style="background:#1d4ed8">الجغرافيا</div>'
            f'<div class="tab{c}" style="background:#0f7b3a">التربية المدنية</div>'
            f'</div>')


def page(num, title, body, unit_label='', with_eval=False, part=''):
    ev = self_eval() if with_eval else ''
    part_cls = f' part-{part}' if part else ''
    tag = f'<span class="subject-tag">{unit_label}</span>' if unit_label else ''
    foot_r = 'دفتر ماجور · التاريخ والجغرافيا والتربية المدنية'
    foot_l = '🇲🇷 السنة السادسة الأساسية 6AF'
    return f'''<div class="sheet{part_cls}">
  {spine()}
  <div class="page-main">
    <div class="page-header">
      <div class="brand">
        <span class="im im-logo logo" role="img" aria-label="Major"></span>
        <span><span class="brand-title">دفتر ماجور</span><br><span class="brand-sub">السنة السادسة الأساسية 6AF</span></span>
      </div>
      {tag}
    </div>
    <div class="page-body">
      <h2 class="lesson-title">{title}</h2>
      {body}
      {ev}
    </div>
    <div class="page-footer"><span>{foot_r}</span><span>{foot_l}</span></div>
    <div class="bottom-number">{num}</div>
  </div>
  {tabs3(part)}
</div>'''
