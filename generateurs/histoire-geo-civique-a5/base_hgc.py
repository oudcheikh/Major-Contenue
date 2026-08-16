# -*- coding: utf-8 -*-
"""Socle du cahier A5 التاريخ والجغرافيا · التربية المدنية — même style « carnet
relié » que le cahier arabe-islamique (base_ai), avec 3 onglets de partie :
تاريخ (ambre) · جغرافيا (bleu) · تربية مدنية (vert), et des composants visuels
(fig SVG, carte à compléter). Les cartes/frises viennent d'assets_hgc.py."""
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, '..', 'arabe-islamique-a5')))

# tout le kit de composants du cahier arabe-islamique (mêmes signatures)
from base_ai import (CSS, CSS_ASSETS, OVAL, OVS,  # noqa: F401
                     badge_row, video_box, tok, exo, consigne, dots, wlines,
                     objectifs, methode, astuce, attention, defi, bulle,
                     self_eval, unit_banner, ai_table, ayah, spine, exemple,
                     print_sanitize)

DOC_ID = 'دفتر ماجور · التاريخ والجغرافيا والتربية المدنية<br>السنة السادسة الأساسية 6AF'

# ── 3 parties : تاريخ ambre · جغرافيا bleu · مدنية vert ──
# TYPO VERROUILLÉE : Cairo + tailles de contenu (8.2 / 12.5). Ne pas modifier
# font-family / font-size ici sans demande explicite de l'utilisateur.
CSS_HGC = """
.part-hist{--part:#b45309;--part-lite:#f59e0b;--part-soft:#fdf3e3;--part-border:#f3c98a}
.part-geo{--part:#1d4ed8;--part-lite:#60a5fa;--part-soft:#eaf1fe;--part-border:#a8c6f5}
.part-civ{--part:#0f7b3a;--part-lite:#34d399;--part-soft:#e9f7ee;--part-border:#93dcb4}
/* Empêche l'héritage 16px du navigateur sur texte hors <li> (examens, etc.) */
.page-body{font-size:8.2px}
.part-hist .frame,.part-geo .frame,.part-civ .frame{
  font-size:8.2px;line-height:1.7;font-weight:700;
}
/* figure : illustration SVG + légende */
.fig{
  background:#fff;border:.4mm solid rgba(17,24,39,.1);border-radius:3.5mm;
  border-top:1.2mm solid var(--part);padding:1.8mm 2mm 1.2mm;margin:1.4mm 0;
  text-align:center;box-shadow:0 1.5px 5px rgba(17,24,39,.05);overflow:hidden;
}
.fig svg{width:100%;height:auto;display:block;overflow:visible}
.fig .fig-cap{
  font-size:6.8px;font-weight:900;color:var(--part);margin-top:.8mm;
  display:flex;align-items:center;justify-content:center;gap:1.5mm;
}
/* exercice = bordure pleine (pas de pointillés) pour ne pas polluer les cartes */
.fig.exercice{border-style:solid;border-width:.55mm;border-color:#c0392b;border-top-width:1.2mm}
.fig.exercice .fig-cap{color:#c0392b}
/* deux figures côte à côte */
.fig-row{display:grid;grid-template-columns:1fr 1fr;gap:2.4mm}
/* QR vidéo : réserve gauche nette, pas de chevauchement */
.part-hist .frame.has-video,.part-geo .frame.has-video,.part-civ .frame.has-video{
  padding-left:28mm!important;min-height:34mm;
}
.part-hist .video-box,.part-geo .video-box,.part-civ .video-box{z-index:3;background:#fff}
/* Évite le collage défi / auto-éval en bas de page */
.defi-card + .self-eval,.tip-card + .self-eval,.warn-card + .self-eval,
.exo-card + .self-eval{margin-top:2.4mm!important}
@media print{
  .fig{box-shadow:none!important;margin:1.6mm 0!important;padding:1.8mm 2mm 1.2mm!important;overflow:visible!important}
  .fig svg{overflow:visible!important}
  .fig-row{gap:1.8mm}
}
"""


def fig(svg, caption, exercice=False, width='', label=''):
    """Illustration SVG encadrée avec légende. exercice=True → cadre à compléter.
    label: préfixe légende (خريطة / خط زمني / رسم…). Défaut خريطة."""
    cls = 'fig exercice' if exercice else 'fig'
    st = f' style="width:{width};margin-inline:auto"' if width else ''
    ic = 'أكمل' if exercice else (label or 'خريطة')
    return (f'<div class="{cls}"{st}>{svg}'
            f'<div class="fig-cap"><b>{ic}</b> · {caption}</div></div>')


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
    """Même gabarit print que base_ai.page : sanitize + QR hors flux + qr-reserve."""
    ev = self_eval() if with_eval else ''
    part_cls = f' part-{part}' if part else ''
    tag = f'<span class="subject-tag">{unit_label}</span>' if unit_label else ''
    foot_r = 'دفتر ماجور · التاريخ والجغرافيا والتربية المدنية'
    foot_l = 'السنة السادسة الأساسية 6AF'
    qr = ''
    m = re.search(r'(<div class="qr-corr"[^>]*>.*?</div>)', body, flags=re.S)
    if m:
        qr = m.group(1)
        body = body[:m.start()] + body[m.end():]
    body = print_sanitize(body)
    title = print_sanitize(title)
    unit_label = print_sanitize(unit_label)
    tag = f'<span class="subject-tag">{unit_label}</span>' if unit_label else ''
    qr_reserve = '<div class="qr-reserve" aria-hidden="true"></div>' if qr else ''
    return f'''<div class="sheet{part_cls}">
  {spine()}
  <div class="page-main">
    <div class="page-header">
      <div class="brand">
        <span class="im im-logo logo" role="img" aria-label="Major"></span>
        <div class="brand-text">
          <div class="brand-title">دفتر ماجور</div>
          <div class="brand-sub">السنة السادسة الأساسية 6AF</div>
        </div>
      </div>
      {tag}
    </div>
    <div class="page-body">
      <h2 class="lesson-title">{title}</h2>
      {body}
      {ev}
      {qr_reserve}
    </div>
    {qr}
    <div class="page-footer"><span>{foot_r}</span><span>{foot_l}</span></div>
    <div class="bottom-number">{num}</div>
  </div>
  {tabs3(part)}
</div>'''
