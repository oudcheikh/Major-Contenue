# -*- coding: utf-8 -*-
"""
assets_hgc.py — bibliothèque d'illustrations SVG vectorielles pour le
Cahier Major « تاريخ وجغرافيا وتربية مدنية » (6AF Mauritanie, format A5 imprimé).

Usage :
    from assets_hgc import CARTE_MAURITANIE, DRAPEAU_MR, FRISE_SIRA
    html += f'<div class="figure">{CARTE_MAURITANIE}</div>'

Chaque constante est un SVG complet et autonome (aucun lien externe,
aucun bitmap), pensé pour une largeur d'impression de 90 à 120 mm.
Couleurs douces adaptées à l'impression ; textes arabes en Cairo/sans-serif.

Assets disponibles :
    CARTE_MAURITANIE    carte de référence complète (villes, voisins, route de l'Espoir)
    CARTE_VIERGE        fond de carte à compléter par l'élève
    CARTE_RESSOURCES    ressources économiques localisées
    CARTE_EMPIRES       empire du Ghana et Almoravides (Afrique de l'Ouest)
    CARTE_EMARAT        les 4 émirats historiques
    FRISE_SIRA          frise chronologique de la Sîra (570-632)
    FRISE_MAURITANIE    frise de l'histoire de la Mauritanie
    FRISE_KHILAFA       frise des 4 califes bien guidés
    DRAPEAU_MR          drapeau mauritanien (version 2017, 2 bandes rouges)
    SCHEMA_INSTITUTIONS organigramme des institutions de la République
    ROSE_VENTS          rose des vents décorative
    CLIMAT_ZONES        zones climatiques de la Mauritanie
"""

# ---------------------------------------------------------------------------
# Palette commune (impression douce)
# ---------------------------------------------------------------------------
SABLE = "#f5e6c8"
OCEAN = "#aad4e8"
VERT = "#2f9e5f"
AMBRE = "#d97706"
BLEU = "#1d7fc4"
ROUGE = "#c0392b"
TRAIT = "#334155"
FONT = "Cairo, sans-serif"

# ---------------------------------------------------------------------------
# Géométrie partagée : contour simplifié mais fidèle de la Mauritanie.
# Projection équirectangulaire réelle : x = 60 + (lon + 17.5) * 23,
# y = 26 + (27.5 - lat) * 23  (viewBox 0 0 420 360).
# Contour AUTHENTIQUE : frontières réelles issues de données cartographiques
# publiques (GeoJSON world.geo.json, domaine public), projetées telles
# quelles avec les formules ci-dessus — ne pas retoucher à la main.
# Le fleuve (_RIVER) et l'océan (_OCEAN_POLY) reprennent les mêmes points
# du tracé (segment fleuve Sénégal / segment côte), donc tout coïncide.
# ---------------------------------------------------------------------------
_MR = ("M 182.6,322.3 L 167.4,306.5 L 153.5,289.6 L 138.2,283.5 L 127.2,276.7 "
       "L 114.4,277.0 L 103.2,282.0 L 91.7,280.0 L 83.8,287.4 L 81.9,275.0 "
       "L 88.3,263.7 L 91.1,242.0 L 88.6,219.3 L 85.8,207.8 L 88.1,196.4 "
       "L 82.2,185.4 L 70.0,175.5 L 75.1,167.8 L 165.1,168.0 L 160.8,134.8 "
       "L 166.4,122.9 L 187.9,120.9 L 187.2,62.0 L 262.7,63.2 L 262.8,28.4 "
       "L 349.3,84.1 L 314.1,84.5 L 325.2,183.8 L 336.3,283.0 L 340.2,285.9 "
       "L 335.1,302.0 L 242.8,302.3 L 239.4,307.4 L 230.5,305.9 L 217.5,310.4 "
       "L 201.5,304.0 L 194.2,304.6 L 190.3,318.1 Z")

_OCEAN_POLY = ("M 12,150 L 75.1,167.8 L 70.0,175.5 L 82.2,185.4 L 88.1,196.4 "
               "L 85.8,207.8 L 88.6,219.3 L 91.1,242.0 L 88.3,263.7 L 81.9,275.0 "
               "L 83.8,287.4 L 68,338 L 14,344 Z")

_RIVER = ("M 83.8,287.4 L 91.7,280.0 L 103.2,282.0 L 114.4,277.0 L 127.2,276.7 "
          "L 138.2,283.5 L 153.5,289.6 L 167.4,306.5 L 182.6,322.3")


def _svg_open(vb="0 0 420 360"):
    # direction=ltr : text-anchor et positions x fiables (sinon le RTL du HTML
    # inverse les ancres et coupe les légendes). L'arabe reste lisible.
    return (f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="{FONT}" direction="ltr">')


def _ar(txt):
    """Texte arabe isolé (bidi) pour dates / chiffres en LTR."""
    return f'<tspan unicode-bidi="isolate">{txt}</tspan>'


def _yrs(a, b):
    """Plage d'années toujours affichée a → b (jamais inversée par le RTL)."""
    return f'<tspan unicode-bidi="isolate" direction="ltr">{a} – {b}</tspan>'


def _yrs_rtl(a, b):
    """Plage pour frise RTL : début à droite, fin à gauche (ex. 634 – 632)."""
    return f'<tspan unicode-bidi="isolate" direction="ltr">{b} – {a}</tspan>'


# Cadre : marge intérieure pour que le trait ne soit JAMAIS rogné
# (anti-aliasing PDF mange les bords du viewBox → droite/bas plus fins sinon).
_CADRE_PAD = 5
_CADRE_SW = 2.0
_MR_SW = 2.0


def _cadre_fill(fill="#fdfaf2", w=420, h=360, pad=_CADRE_PAD):
    return (f'<rect x="{pad}" y="{pad}" width="{w - 2 * pad}" height="{h - 2 * pad}" '
            f'rx="10" fill="{fill}"/>')


def _cadre_stroke(w=420, h=360, pad=_CADRE_PAD, sw=_CADRE_SW, color=None):
    """Contour dessiné en dernier. Épaisseur IDENTIQUE haut/bas/gauche/droite,
    entièrement à l'intérieur du viewBox (pad ≥ sw)."""
    col = color or TRAIT
    c = pad + sw / 2
    return (f'<rect x="{c}" y="{c}" width="{w - 2 * c}" height="{h - 2 * c}" rx="9" '
            f'fill="none" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round"/>')


def _leg_row(x, y, ico_html, label):
    """Une entrée de légende : icône + libellé, ancrage fiable."""
    return (f'{ico_html}'
            f'<text x="{x + 12}" y="{y + 4}" font-size="10" font-weight="700" '
            f'fill="{TRAIT}" text-anchor="start" unicode-bidi="isolate">{label}</text>')


# ===========================================================================
# 1. CARTE_MAURITANIE — carte de référence complète
# ===========================================================================
_villes = [
    # (x, y, nom, dx, dy, anchor, capital?)
    (95, 242, "انواكشوط", 14, -14, "start", True),   # عاصمة = زر أحمر
    (73, 178, "انواذيبو", -12, -10, "end", False),   # label côté océan (pas sur côte)
    (176, 136, "ازويرات", 9, 4, "start", False),
    (162, 187, "أطار", -8, -4, "end", False),
    (178, 188, "شنقيط", 2, 15, "middle", False),
    (195, 177, "ودان", 8, -3, "start", False),
    (200, 232, "تجكجة", 9, 4, "start", False),
    (200, 276, "كيفة", -8, 16, "end", False),       # sous la route — évite عيون العتروس
    (242, 275, "عيون العتروس", 6, -16, "middle", False),  # au-dessus de la route
    (296, 276, "النعمة", -12, 10, "end", False),     # à l'intérieur, hors frontière E
    (99, 279, "روصو", -8, -14, "end", False),       # au-dessus du fleuve
    (182, 310, "سيلبابي", 14, 2, "start", False),    # à droite, hors du fleuve
    (301, 261, "ولاتة", -14, -10, "end", False),     # à l'intérieur, hors frontière E
]

_villes_svg = ""
for _x, _y, _nom, _dx, _dy, _anc, _cap in _villes:
    if _cap:
        _villes_svg += (
            f'<circle cx="{_x}" cy="{_y}" r="7" fill="#ffffff" stroke="{ROUGE}" stroke-width="2"/>'
            f'<circle cx="{_x}" cy="{_y}" r="3.2" fill="{ROUGE}"/>'
        )
    else:
        _villes_svg += (
            f'<circle cx="{_x}" cy="{_y}" r="3.6" fill="{TRAIT}" '
            f'stroke="#ffffff" stroke-width="1.5"/>'
        )
    _villes_svg += (
        f'<text x="{_x + _dx}" y="{_y + _dy + 4}" font-size="11" '
        f'font-weight="{"800" if _cap else "600"}" fill="{TRAIT}" text-anchor="{_anc}"'
        f' unicode-bidi="isolate">{_nom}</text>'
    )

CARTE_MAURITANIE = (
    _svg_open()
    + f'''
  <defs>
    <clipPath id="mrClip">
      <rect x="{_CADRE_PAD + 1}" y="{_CADRE_PAD + 1}"
            width="{420 - 2 * (_CADRE_PAD + 1)}" height="{360 - 2 * (_CADRE_PAD + 1)}" rx="8"/>
    </clipPath>
  </defs>
  {_cadre_fill("#fdfaf2")}
  <g clip-path="url(#mrClip)">
  <!-- محيط أطلسي ملوّن (مرجع) -->
  <path d="{_OCEAN_POLY}" fill="{OCEAN}" opacity="0.85"/>
  <path d="{_MR}" fill="{SABLE}" stroke="none"/>
  <path d="{_RIVER}" fill="none" stroke="{BLEU}" stroke-width="3" stroke-linecap="round"/>
  <path d="{_MR}" fill="none" stroke="{TRAIT}" stroke-width="{_MR_SW}"/>
  <!-- طريق الأمل -->
  <path d="M 95,242 L 125,255 L 143,266 L 200,276 L 242,275 L 296,276"
        fill="none" stroke="{AMBRE}" stroke-width="2.4" stroke-dasharray="7 4" stroke-linecap="round"/>
  <text x="168" y="248" font-size="11" font-weight="700" fill="{AMBRE}" text-anchor="middle"
        unicode-bidi="isolate">طريق الأمل</text>
  <!-- الجيران -->
  <text x="112" y="122" font-size="12" font-weight="700" fill="#8a6d3b" text-anchor="middle"
        unicode-bidi="isolate">الصحراء الغربية</text>
  <text x="352" y="48" font-size="13" font-weight="700" fill="#8a6d3b" unicode-bidi="isolate">الجزائر</text>
  <text x="382" y="200" font-size="13" font-weight="700" fill="#8a6d3b" text-anchor="middle"
        unicode-bidi="isolate">مالي</text>
  <text x="250" y="342" font-size="13" font-weight="700" fill="#8a6d3b" text-anchor="middle"
        unicode-bidi="isolate">مالي</text>
  <text x="118" y="330" font-size="13" font-weight="700" fill="#8a6d3b" text-anchor="middle"
        unicode-bidi="isolate">السنغال</text>
  <text x="36" y="250" font-size="12" font-weight="700" fill="{BLEU}"
        transform="rotate(-90 36 250)" text-anchor="middle" unicode-bidi="isolate">المحيط الأطلسي</text>
  <text x="95" y="298" font-size="11" font-weight="600" fill="{BLEU}" unicode-bidi="isolate">نهر السنغال</text>
  {_villes_svg}
  <!-- وردة اتجاهات مصغّرة (هامش كافٍ — غير مقصوصة) -->
  <g transform="translate(10,12) scale(0.96)">
    <line x1="42" y1="48" x2="42" y2="82" stroke="{TRAIT}" stroke-width="1.5"/>
    <line x1="25" y1="65" x2="59" y2="65" stroke="{TRAIT}" stroke-width="1.5"/>
    <path d="M 42,44 L 38,54 L 46,54 Z" fill="{ROUGE}"/>
    <text x="42" y="40" font-size="10" font-weight="800" fill="{ROUGE}" text-anchor="middle"
          unicode-bidi="isolate">شمال</text>
    <text x="42" y="95" font-size="10" font-weight="700" fill="{TRAIT}" text-anchor="middle"
          unicode-bidi="isolate">جنوب</text>
    <text x="64" y="69" font-size="10" font-weight="700" fill="{TRAIT}" text-anchor="start"
          unicode-bidi="isolate">شرق</text>
    <text x="20" y="69" font-size="10" font-weight="700" fill="{TRAIT}" text-anchor="end"
          unicode-bidi="isolate">غرب</text>
  </g>
  <!-- مقياس (loin du bord droit) -->
  <g stroke="{TRAIT}" stroke-width="1.6">
    <line x1="310" y1="338" x2="358" y2="338"/>
    <line x1="310" y1="333" x2="310" y2="343"/>
    <line x1="358" y1="333" x2="358" y2="343"/>
  </g>
  <text x="334" y="330" font-size="11" fill="{TRAIT}" text-anchor="middle" unicode-bidi="isolate">200 كم</text>
  </g>
  {_cadre_stroke()}
</svg>'''
)

# ===========================================================================
# 2. CARTE_VIERGE — fond de carte (bandeau haut = sujet exact de l'exercice)
# ===========================================================================
_vierge_spots = [
    (95, 242, 104, 246, 46),
    (73, 178, 82, 170, 46),
    (176, 136, 186, 140, 46),
    (162, 187, 145, 201, 46),
    (200, 232, 210, 236, 46),
    (200, 276, 210, 268, 46),
    (296, 276, 306, 280, 46),
    (99, 279, 58, 267, 40),
    (182, 310, 192, 317, 46),
]
# Points = emplacements des ressources uniquement (pas les villes)
_richesse_spots = [
    # (x, y, lx, ly, llen) — alignés sur CARTE_RESSOURCES
    (176, 136, 186, 140, 40),   # حديد ازويرات
    (112, 168, 124, 172, 40),   # ذهب تازيازت
    (128, 198, 140, 202, 40),   # نحاس أكجوجت
    (200, 112, 210, 116, 36),   # ملح
    (58, 210, 72, 214, 36),     # صيد (ساحل)
    (58, 262, 72, 266, 36),     # نفط (بحر)
    (130, 278, 142, 282, 40),   # زراعة
    (250, 220, 262, 224, 40),   # رعي
]


def _spots_svg(spots, capital_xy=None, with_lines=True):
    """capital_xy = (x,y) → cercle rouge pour العاصمة.
    with_lines=False → cercles seuls (ex. exercice symboles/richesses)."""
    out = ""
    for _x, _y, _lx, _ly, _ll in spots:
        is_cap = capital_xy and abs(_x - capital_xy[0]) < 0.5 and abs(_y - capital_xy[1]) < 0.5
        if is_cap:
            out += (
                f'<circle cx="{_x}" cy="{_y}" r="6" fill="#ffffff" stroke="{ROUGE}" stroke-width="2"/>'
                f'<circle cx="{_x}" cy="{_y}" r="2.4" fill="{ROUGE}"/>'
            )
        else:
            out += (
                f'<circle cx="{_x}" cy="{_y}" r="5" fill="#ffffff" stroke="{TRAIT}" stroke-width="1.5"/>'
            )
        if with_lines:
            out += (
                f'<line x1="{_lx}" y1="{_ly}" x2="{_lx + _ll}" y2="{_ly}" '
                f'stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>'
            )
    return out


_vierge_clip_n = 0


def carte_vierge(bandeau, spots=None, voisins=True, capital=False, colorier_ocean=False,
                 with_lines=True):
    """Fond de carte exercice.
    colorier_ocean=True → océan blanc sans label (élève colorie).
    with_lines=False → pas de tirets (ex. placer des symboles).
    Contenu clipé + scale pour rester DANS le cadre."""
    global _vierge_clip_n
    _vierge_clip_n += 1
    clip_id = f"vgClip{_vierge_clip_n}"

    use_spots = spots if spots is not None else _vierge_spots
    cap = (95, 242) if capital else None
    svg_spots = _spots_svg(use_spots, capital_xy=cap, with_lines=with_lines)
    voisin_lines = ''
    if voisins:
        voisin_lines = '''
  <line x1="100" y1="118" x2="148" y2="118" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
  <line x1="300" y1="58" x2="348" y2="58" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
  <line x1="348" y1="200" x2="378" y2="200" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
  <line x1="100" y1="328" x2="142" y2="328" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>'''
    if colorier_ocean:
        ocean = f'<path d="{_OCEAN_POLY}" fill="#ffffff" stroke="{BLEU}" stroke-width="1.2"/>'
    else:
        ocean = (
            f'<path d="{_OCEAN_POLY}" fill="{OCEAN}" opacity="0.7"/>'
            f'<text x="42" y="250" font-size="12" font-weight="700" fill="{BLEU}" '
            f'transform="rotate(-90 42 250)" text-anchor="middle" '
            f'unicode-bidi="isolate">المحيط الأطلسي</text>'
        )
    ix, iy = _CADRE_PAD + 1, 34
    iw, ih = 420 - 2 * (_CADRE_PAD + 1), 360 - iy - _CADRE_PAD - 1
    return (
        _svg_open()
        + f'''
  <defs>
    <clipPath id="{clip_id}">
      <rect x="{ix}" y="{iy}" width="{iw}" height="{ih}" rx="6"/>
    </clipPath>
  </defs>
  {_cadre_fill("#ffffff")}
  <g clip-path="url(#{clip_id})">
    <g transform="translate(8, 30) scale(0.96)">
      {ocean}
      <path d="{_MR}" fill="#fefcf6" stroke="none"/>
      <path d="{_RIVER}" fill="none" stroke="{BLEU}" stroke-width="2.4" stroke-linecap="round"/>
      <path d="{_MR}" fill="none" stroke="{TRAIT}" stroke-width="{_MR_SW}"/>
      {svg_spots}
      {voisin_lines}
    </g>
  </g>
  <rect x="{_CADRE_PAD}" y="{_CADRE_PAD}" width="{420 - 2 * _CADRE_PAD}" height="26" rx="10" fill="#e8f1fb"/>
  <rect x="{_CADRE_PAD}" y="{_CADRE_PAD + 16}" width="{420 - 2 * _CADRE_PAD}" height="12" fill="#e8f1fb"/>
  <text x="210" y="{_CADRE_PAD + 17}" font-size="11.5" font-weight="700" fill="{BLEU}" text-anchor="middle"
        unicode-bidi="isolate">{bandeau}</text>
  {_cadre_stroke()}
</svg>'''
    )


CARTE_VIERGE = carte_vierge('أكمل: أسماء المدن والجيران · لوّن المحيط', capital=True,
                            colorier_ocean=True)
CARTE_VIERGE_VILLES = carte_vierge('أكمل: ضع أسماء المدن أمام الدوائر · العاصمة بالدائرة الحمراء',
                                   voisins=False, capital=True)
CARTE_VIERGE_RICHESSES = carte_vierge(
    'أكمل: ضع رموز الثروات في أماكنها الصحيحة',
    spots=_richesse_spots,
    voisins=False,
    with_lines=False,
)
CARTE_VIERGE_ROUTES = carte_vierge('أكمل: ارسم الطرق وسمِّ المدن (كما في المسابقة)', capital=True)

# ===========================================================================
# 3. CARTE_RESSOURCES — ذهب تازيازت · نحاس أكجوجت · légende lisible
# ===========================================================================
def _ico_pick(cx, cy, fill="#64748b"):
    return (f'<g transform="translate({cx},{cy})">'
            f'<rect x="-2" y="-7" width="4" height="12" rx="1" fill="{fill}"/>'
            f'<path d="M-8,-8 L8,-8 L4,-2 L-4,-2 Z" fill="{fill}"/>'
            f'</g>')


def _ico_circle(cx, cy, fill, r=6):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{TRAIT}" stroke-width="0.9"/>'


def _ico_salt(cx, cy):
    return (f'<g transform="translate({cx},{cy})">'
            f'<rect x="-5" y="-3" width="10" height="8" rx="1.5" fill="#e2e8f0" stroke="{TRAIT}" stroke-width="0.8"/>'
            f'<circle cx="-2" cy="-5" r="2" fill="#fff" stroke="{TRAIT}" stroke-width="0.7"/>'
            f'<circle cx="2" cy="-5" r="2" fill="#fff" stroke="{TRAIT}" stroke-width="0.7"/>'
            f'</g>')


def _ico_oil(cx, cy):
    return (f'<g transform="translate({cx},{cy})">'
            f'<rect x="-5" y="-6" width="10" height="12" rx="1.5" fill="#c0392b" stroke="{TRAIT}" stroke-width="0.8"/>'
            f'<rect x="-5" y="-6" width="10" height="3" fill="#7f1d1d"/>'
            f'</g>')


def _ico_fish(cx, cy):
    return (f'<g transform="translate({cx},{cy})">'
            f'<ellipse cx="0" cy="0" rx="8" ry="4" fill="{BLEU}"/>'
            f'<path d="M8,0 L13,-4 L13,4 Z" fill="{BLEU}"/>'
            f'<circle cx="-3" cy="-1" r="1" fill="#fff"/>'
            f'</g>')


def _ico_grain(cx, cy):
    return (f'<g transform="translate({cx},{cy})">'
            f'<path d="M0,6 L0,-6" stroke="{VERT}" stroke-width="1.6"/>'
            f'<path d="M0,-2 Q-6,-6 -2,-10" fill="none" stroke="{VERT}" stroke-width="1.4"/>'
            f'<path d="M0,-2 Q6,-6 2,-10" fill="none" stroke="{VERT}" stroke-width="1.4"/>'
            f'</g>')


def _ico_camel(cx, cy):
    return (f'<g transform="translate({cx},{cy})">'
            f'<ellipse cx="0" cy="1" rx="9" ry="5" fill="{AMBRE}"/>'
            f'<circle cx="8" cy="-2" r="3.2" fill="{AMBRE}"/>'
            f'<rect x="-6" y="4" width="2.2" height="6" fill="{AMBRE}"/>'
            f'<rect x="3" y="4" width="2.2" height="6" fill="{AMBRE}"/>'
            f'</g>')


def _mark(cx, cy, ico, label, sub='', lab_dx=12, lab_dy=4):
    bits = [ico]
    bits.append(
        f'<text x="{cx + lab_dx}" y="{cy + lab_dy}" font-size="11" font-weight="700" '
        f'fill="{TRAIT}" text-anchor="start" unicode-bidi="isolate">{label}</text>'
    )
    if sub:
        bits.append(
            f'<text x="{cx + lab_dx}" y="{cy + lab_dy + 12}" font-size="8.5" font-weight="600" '
            f'fill="#64748b" text-anchor="start" unicode-bidi="isolate">{sub}</text>'
        )
    return ''.join(bits)


CARTE_RESSOURCES = (
    _svg_open()
    + f'''
  <defs><clipPath id="resClip"><rect x="{_CADRE_PAD + 1}" y="{_CADRE_PAD + 1}"
        width="{420 - 2 * (_CADRE_PAD + 1)}" height="{360 - 2 * (_CADRE_PAD + 1)}" rx="8"/></clipPath></defs>
  {_cadre_fill("#fdfaf2")}
  <g clip-path="url(#resClip)">
  <path d="{_OCEAN_POLY}" fill="{OCEAN}" opacity="0.8"/>
  <path d="{_MR}" fill="{SABLE}" stroke="none"/>
  <path d="{_RIVER}" fill="none" stroke="{BLEU}" stroke-width="2.4" stroke-linecap="round"/>
  <path d="{_MR}" fill="none" stroke="{TRAIT}" stroke-width="{_MR_SW}"/>
  <text x="210" y="22" font-size="13" font-weight="700" fill="{TRAIT}" text-anchor="middle"
        unicode-bidi="isolate">ثروات بلادي</text>

  {_mark(176, 138, _ico_pick(176, 138), 'حديد', 'ازويرات')}
  {_mark(112, 168, _ico_circle(112, 168, '#eab308'), 'ذهب', 'تازيازت', lab_dx=14)}
  {_mark(128, 198, _ico_circle(128, 198, '#a16207'), 'نحاس', 'أكجوجت', lab_dx=14)}
  {_mark(200, 112, _ico_salt(200, 112), 'ملح')}
  {_ico_fish(52, 210)}
  <text x="52" y="228" font-size="11" font-weight="700" fill="{BLEU}" text-anchor="middle"
        unicode-bidi="isolate">صيد</text>
  {_ico_oil(52, 262)}
  <text x="52" y="280" font-size="11" font-weight="700" fill="{TRAIT}" text-anchor="middle"
        unicode-bidi="isolate">نفط</text>
  {_mark(130, 278, _ico_grain(130, 278), 'زراعة')}
  {_mark(250, 220, _ico_camel(250, 220), 'رعي', lab_dx=14)}

  <rect x="10" y="298" width="236" height="54" rx="7" fill="#ffffff" stroke="{TRAIT}" stroke-width="1.3"/>
  <text x="128" y="312" font-size="10" font-weight="700" fill="{TRAIT}" text-anchor="middle"
        unicode-bidi="isolate">مفتاح الرموز</text>
  {_ico_pick(28, 326)}
  <text x="40" y="330" font-size="9.5" font-weight="700" fill="{TRAIT}" text-anchor="start" unicode-bidi="isolate">حديد</text>
  {_ico_circle(78, 326, '#eab308', 5)}
  <text x="88" y="330" font-size="9.5" font-weight="700" fill="{TRAIT}" text-anchor="start" unicode-bidi="isolate">ذهب</text>
  {_ico_circle(128, 326, '#a16207', 5)}
  <text x="138" y="330" font-size="9.5" font-weight="700" fill="{TRAIT}" text-anchor="start" unicode-bidi="isolate">نحاس</text>
  {_ico_salt(182, 326)}
  <text x="194" y="330" font-size="9.5" font-weight="700" fill="{TRAIT}" text-anchor="start" unicode-bidi="isolate">ملح</text>
  {_ico_oil(28, 344)}
  <text x="40" y="348" font-size="9.5" font-weight="700" fill="{TRAIT}" text-anchor="start" unicode-bidi="isolate">نفط</text>
  {_ico_fish(78, 344)}
  <text x="94" y="348" font-size="9.5" font-weight="700" fill="{TRAIT}" text-anchor="start" unicode-bidi="isolate">صيد</text>
  {_ico_grain(138, 344)}
  <text x="150" y="348" font-size="9.5" font-weight="700" fill="{VERT}" text-anchor="start" unicode-bidi="isolate">زراعة</text>
  {_ico_camel(194, 344)}
  <text x="210" y="348" font-size="9.5" font-weight="700" fill="{AMBRE}" text-anchor="start" unicode-bidi="isolate">رعي</text>
  </g>
  {_cadre_stroke()}
</svg>'''
)

# ===========================================================================
# 4. CARTE_EMPIRES — Maghreb / Andalus / Ghana (projection lon/lat réelle)
# Projection : x = 40+(lon+18)*14.5 · y = 28+(44-lat)*9.2  (viewBox 420×360)
# Zones : المرابطون = المغرب + الصحراء الغربية + موريتانيا حتى السنغال + الأندلس
#         غانا = جنوب شرق نهر السنغال (كومبي صالح ≈ 15.4°N, 7.8°W)
# ===========================================================================
_IBERIA = (
    "M 163.2,37.2 L 185.0,32.6 L 199.5,30.8 L 214.0,32.6 L 228.5,35.4 L 250.2,41.8 "
    "L 272.0,51.0 L 286.5,60.2 L 293.8,72.2 L 289.4,85.0 L 279.2,92.4 L 257.5,95.2 "
    "L 235.8,96.1 L 222.7,101.1 L 219.8,101.6 L 211.1,100.2 L 199.5,97.0 L 185.0,92.4 "
    "L 173.4,85.0 L 166.1,74.0 L 163.2,60.2 L 163.2,46.4 L 163.2,37.2 Z"
)
_AFRIQUE_NW = (
    "M 224.1,102.5 L 216.9,103.9 L 209.6,107.1 L 202.4,115.4 L 196.6,121.8 L 187.9,129.2 "
    "L 177.8,136.6 L 167.6,143.9 L 160.4,152.2 L 159.6,161.4 L 161.8,167.8 L 156.0,173.4 "
    "L 141.5,178.9 L 127.0,185.3 L 115.4,193.6 L 105.2,201.0 L 93.6,208.3 L 83.5,216.6 "
    "L 74.8,224.9 L 69.0,235.0 L 61.8,241.4 L 56.0,248.8 L 60.3,258.0 L 66.1,265.4 "
    "L 69.0,274.6 L 63.2,281.9 L 57.4,286.5 L 56.0,293.0 L 61.8,298.5 L 71.9,303.1 "
    "L 86.4,306.8 L 105.2,310.4 L 124.1,314.1 L 144.4,317.8 L 167.6,320.6 L 192.2,322.4 "
    "L 214.0,319.6 L 235.8,315.0 L 257.5,308.6 L 279.2,299.4 L 301.0,287.4 L 322.8,271.8 "
    "L 344.5,253.4 L 361.9,230.4 L 373.5,207.4 L 380.8,179.8 L 385.1,156.8 L 376.4,133.8 "
    "L 359.0,118.2 L 337.2,109.0 L 315.5,101.6 L 293.8,97.9 L 272.0,96.5 L 250.2,97.0 "
    "L 231.4,99.8 L 224.1,102.5 Z"
)
_ZONE_ALM = (
    "M 177.8,90.6 L 199.5,97.0 L 216.9,101.6 L 221.2,106.2 L 206.8,120.0 L 192.2,133.8 "
    "L 177.8,147.6 L 170.5,161.4 L 156.0,175.2 L 134.2,189.0 L 112.5,202.8 L 90.8,216.6 "
    "L 76.2,235.0 L 69.0,253.4 L 71.9,271.8 L 83.5,281.0 L 105.2,283.8 L 127.0,281.0 "
    "L 148.8,271.8 L 170.5,258.0 L 185.0,239.6 L 199.5,216.6 L 206.8,193.6 L 214.0,170.6 "
    "L 221.2,147.6 L 225.6,124.6 L 221.2,109.0 L 206.8,101.6 L 192.2,97.0 L 177.8,90.6 Z"
)
_ZONE_GHANA = (
    "M 134.2,281.0 L 163.2,276.4 L 192.2,278.2 L 214.0,287.4 L 221.2,299.4 L 206.8,311.4 "
    "L 177.8,315.0 L 148.8,311.4 L 127.0,302.2 L 119.8,290.2 L 134.2,281.0 Z"
)
_SENEGAL_EMP = "M 61.8,285.6 L 80.6,289.3 L 100.9,292.0 L 119.8,294.8 L 138.6,297.6 L 156.0,299.4"

CARTE_EMPIRES = (
    _svg_open("0 0 420 360")
    + f'''
  {_cadre_fill("#dbeefe", w=420, h=360)}
  <!-- اليابسة: شبه الجزيرة الإيبيرية + شمال غرب إفريقيا -->
  <path d="{_IBERIA}" fill="{SABLE}" stroke="{TRAIT}" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="{_AFRIQUE_NW}" fill="{SABLE}" stroke="{TRAIT}" stroke-width="1.5" stroke-linejoin="round"/>
  <!-- مضيق جبل طارق -->
  <path d="M 218,101 L 224,103" fill="none" stroke="{OCEAN}" stroke-width="3.2" stroke-linecap="round"/>
  <!-- دولة المرابطين (المغرب · الصحراء · موريتانيا · الأندلس) -->
  <path d="{_ZONE_ALM}" fill="{VERT}" opacity="0.28" stroke="{VERT}" stroke-width="1.8" stroke-linejoin="round"/>
  <text x="130" y="200" font-size="13" font-weight="700" fill="#1c6b40" text-anchor="middle"
        unicode-bidi="isolate">دولة المرابطين</text>
  <!-- إمبراطورية غانا جنوب شرق نهر السنغال -->
  <path d="{_ZONE_GHANA}" fill="{AMBRE}" opacity="0.32" stroke="{AMBRE}" stroke-width="1.8" stroke-linejoin="round"/>
  <text x="175" y="298" font-size="12" font-weight="700" fill="#9a5b06" text-anchor="middle"
        unicode-bidi="isolate">إمبراطورية غانا</text>
  <!-- نهر السنغال -->
  <path d="{_SENEGAL_EMP}" fill="none" stroke="{BLEU}" stroke-width="2.8" stroke-linecap="round"/>
  <text x="95" y="318" font-size="10" font-weight="700" fill="{BLEU}" text-anchor="middle"
        unicode-bidi="isolate">نهر السنغال</text>
  <!-- مدن -->
  <circle cx="185" cy="142" r="3.8" fill="{TRAIT}"/>
  <text x="194" y="140" font-size="11" font-weight="700" fill="{TRAIT}" text-anchor="start"
        unicode-bidi="isolate">مراكش</text>
  <circle cx="188" cy="291" r="3.8" fill="{ROUGE}"/>
  <text x="198" y="295" font-size="10" font-weight="700" fill="{ROUGE}" text-anchor="start"
        unicode-bidi="isolate">كومبي صالح</text>
  <!-- سهم التوسّع نحو الأندلس -->
  <defs>
    <marker id="arrE" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="{VERT}"/>
    </marker>
  </defs>
  <path d="M 84,250 L 110,210 L 145,160 L 175,120" fill="none" stroke="{VERT}"
        stroke-width="2.4" stroke-linecap="round" marker-end="url(#arrE)"/>
  <path d="M 185,112 L 198,92" fill="none" stroke="{VERT}" stroke-width="2.4"
        stroke-linecap="round" marker-end="url(#arrE)"/>
  <!-- تسميات جغرافية -->
  <text x="215" y="62" font-size="13" font-weight="700" fill="{TRAIT}" text-anchor="middle"
        unicode-bidi="isolate">الأندلس</text>
  <text x="155" y="155" font-size="11" font-weight="700" fill="#8a6d3b" text-anchor="middle"
        unicode-bidi="isolate">المغرب</text>
  <text x="315" y="195" font-size="12" font-weight="700" fill="#8a6d3b" text-anchor="middle"
        unicode-bidi="isolate">الصحراء الكبرى</text>
  <text x="28" y="210" font-size="11" font-weight="700" fill="{BLEU}"
        transform="rotate(-90 28 210)" text-anchor="middle" unicode-bidi="isolate">المحيط الأطلسي</text>
  {_cadre_stroke(w=420, h=360)}
</svg>'''
)

# ===========================================================================
# 5. CARTE_EMARAT — les 4 émirats historiques
# ===========================================================================
CARTE_EMARAT = (
    _svg_open()
    + f'''
  {_cadre_fill("#fdfaf2")}
  <path d="{_OCEAN_POLY}" fill="{OCEAN}" opacity="0.6"/>
  <path d="{_MR}" fill="{SABLE}" stroke="none"/>
  <path d="{_RIVER}" fill="none" stroke="{BLEU}" stroke-width="2.4" stroke-linecap="round"/>
  <path d="{_MR}" fill="none" stroke="{TRAIT}" stroke-width="{_MR_SW}"/>
  <text x="210" y="26" font-size="14" font-weight="700" fill="{TRAIT}" text-anchor="middle">الإمارات التاريخية الأربع</text>
  <!-- آدرار (شمال : أطار وشنقيط) -->
  <ellipse cx="178" cy="188" rx="36" ry="22" fill="{AMBRE}" opacity="0.3" stroke="{AMBRE}" stroke-width="1.4"/>
  <text x="178" y="193" font-size="13" font-weight="700" fill="#9a5b06" text-anchor="middle">آدرار</text>
  <!-- تكانت (وسط : تجكجة) -->
  <ellipse cx="204" cy="238" rx="38" ry="22" fill="{BLEU}" opacity="0.22" stroke="{BLEU}" stroke-width="1.4"/>
  <text x="204" y="243" font-size="13" font-weight="700" fill="{BLEU}" text-anchor="middle">تكانت</text>
  <!-- الترارزة (جنوب غرب بين الساحل والنهر) -->
  <ellipse cx="112" cy="256" rx="21" ry="18" fill="{VERT}" opacity="0.26" stroke="{VERT}" stroke-width="1.4"/>
  <text x="112" y="261" font-size="12" font-weight="700" fill="#1c6b40" text-anchor="middle">الترارزة</text>
  <!-- البراكنة (جنوب : حوض النهر الأوسط) -->
  <ellipse cx="156" cy="262" rx="22" ry="15" fill="{ROUGE}" opacity="0.2" stroke="{ROUGE}" stroke-width="1.4"/>
  <text x="156" y="267" font-size="12" font-weight="700" fill="{ROUGE}" text-anchor="middle">البراكنة</text>
  <text x="30" y="250" font-size="12" font-weight="700" fill="{BLEU}"
        transform="rotate(-90 30 250)" text-anchor="middle">المحيط الأطلسي</text>
  {_cadre_stroke()}
</svg>'''
)

# ===========================================================================
# 6-7-12. Frises chronologiques (générateur commun)
# ===========================================================================
def _frise(events, title, marker_id, vb_w=470):
    """events = list of (x, year, label1, label2 or None) ; alternance haut/bas."""
    line_y = 92
    parts = [
        _svg_open(f"0 0 {vb_w} 168"),
        f'<defs><marker id="{marker_id}" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">'
        f'<path d="M0,0 L8,3 L0,6 Z" fill="{TRAIT}"/></marker></defs>',
        f'<rect x="{_CADRE_PAD}" y="{_CADRE_PAD}" width="{vb_w - 2 * _CADRE_PAD}" height="{168 - 2 * _CADRE_PAD}" '
        f'rx="10" fill="#fdfaf2"/>',
        f'<text x="{vb_w // 2}" y="22" font-size="14" font-weight="700" fill="{TRAIT}" text-anchor="middle">{title}</text>',
        f'<line x1="{vb_w - 18}" y1="{line_y}" x2="16" y2="{line_y}" stroke="{TRAIT}" stroke-width="2.4" marker-end="url(#{marker_id})"/>',
    ]
    for i, (x, year, l1, l2) in enumerate(events):
        color = [VERT, AMBRE, BLEU, ROUGE][i % 4]
        parts.append(f'<circle cx="{x}" cy="{line_y}" r="5.5" fill="{color}" stroke="#ffffff" stroke-width="1.6"/>')
        if i % 2 == 0:  # au-dessus
            parts.append(f'<line x1="{x}" y1="{line_y - 6}" x2="{x}" y2="{line_y - 18}" stroke="{color}" stroke-width="1.4"/>')
            if l2:
                parts.append(f'<text x="{x}" y="{line_y - 52}" font-size="12" font-weight="700" fill="{TRAIT}" text-anchor="middle">{l1}</text>')
                parts.append(f'<text x="{x}" y="{line_y - 38}" font-size="12" font-weight="700" fill="{TRAIT}" text-anchor="middle">{l2}</text>')
            else:
                parts.append(f'<text x="{x}" y="{line_y - 38}" font-size="12" font-weight="700" fill="{TRAIT}" text-anchor="middle">{l1}</text>')
            parts.append(f'<text x="{x}" y="{line_y - 23}" font-size="11" font-weight="600" fill="{color}" text-anchor="middle">{year}</text>')
        else:  # en dessous
            parts.append(f'<line x1="{x}" y1="{line_y + 6}" x2="{x}" y2="{line_y + 18}" stroke="{color}" stroke-width="1.4"/>')
            parts.append(f'<text x="{x}" y="{line_y + 32}" font-size="11" font-weight="600" fill="{color}" text-anchor="middle">{year}</text>')
            parts.append(f'<text x="{x}" y="{line_y + 48}" font-size="12" font-weight="700" fill="{TRAIT}" text-anchor="middle">{l1}</text>')
            if l2:
                parts.append(f'<text x="{x}" y="{line_y + 62}" font-size="12" font-weight="700" fill="{TRAIT}" text-anchor="middle">{l2}</text>')
    parts.append(_cadre_stroke(w=vb_w, h=168))
    parts.append("</svg>")
    return "".join(parts)


# NB : frise arabe → le temps s'écoule de droite à gauche
FRISE_SIRA = _frise(
    [
        (430, "570م", "الميلاد", None),
        (368, "610م", "البعثة", None),
        (305, "622م", "الهجرة", None),
        (243, "2هـ", "غزوة بدر", None),
        (181, "3هـ", "غزوة أحد", None),
        (118, "8هـ", "فتح مكة", None),
        (44, "632م", "الوفاة", None),
    ],
    "الخط الزمني للسيرة النبوية ﷺ",
    "arrS",
)

FRISE_MAURITANIE = _frise(
    [
        (415, "1076م", "المرابطون", "وغانا"),
        (325, "القرن 17", "قيام", "الإمارات"),
        (232, "1903-1934", "الاستعمار", "والمقاومة"),
        (140, "28/11/1960", "الاستقلال", None),
        (48, "1961", "عضوية الأمم", "المتحدة"),
    ],
    "محطات من تاريخ موريتانيا",
    "arrM",
)

# ===========================================================================
# 12. FRISE_KHILAFA — les 4 califes bien guidés
# ===========================================================================
_khoulafa = [
    ("أبو بكر الصديق", "632", "634"),
    ("عمر بن الخطاب", "634", "644"),
    ("عثمان بن عفان", "644", "656"),
    ("علي بن أبي طالب", "656", "661"),
]
_kh_parts = [
    _svg_open("0 0 470 150"),
    f'<defs><marker id="arrK" markerWidth="10" markerHeight="10" refX="8" refY="3.5" orient="auto">'
    f'<path d="M0,0 L9,3.5 L0,7 Z" fill="{TRAIT}"/></marker></defs>',
    _cadre_fill("#fdfaf2", w=470, h=150),
    f'<text x="235" y="26" font-size="14" font-weight="700" fill="{TRAIT}" text-anchor="middle"'
    f' unicode-bidi="isolate">الخلفاء الراشدون رضي الله عنهم</text>',
]
_kh_colors = [VERT, AMBRE, BLEU, ROUGE]
# RTL arabe : أبو بكر (1) à droite → علي (4) à gauche · flèches vers la gauche
for _i, (_nom, _a, _b) in enumerate(_khoulafa):
    _bx = 362 - _i * 118
    _c = _kh_colors[_i]
    _kh_parts.append(
        f'<rect x="{_bx}" y="48" width="90" height="62" rx="10" fill="#ffffff" '
        f'stroke="{_c}" stroke-width="2"/>'
        f'<text x="{_bx + 45}" y="74" font-size="11" font-weight="700" fill="{TRAIT}" '
        f'text-anchor="middle" unicode-bidi="isolate">{_nom}</text>'
        f'<text x="{_bx + 45}" y="96" font-size="12" font-weight="600" fill="{_c}" '
        f'text-anchor="middle">{_yrs_rtl(_a, _b)}</text>'
        f'<circle cx="{_bx + 45}" cy="128" r="10" fill="{_c}" opacity="0.9"/>'
        f'<text x="{_bx + 45}" y="132.5" font-size="11" font-weight="700" fill="#ffffff" '
        f'text-anchor="middle" unicode-bidi="isolate">{_i + 1}</text>'
    )
    if _i < 3:
        # flèche RTL : de la boîte courante (droite) vers la suivante (gauche)
        _x1 = _bx - 4
        _x2 = _bx - 24
        _kh_parts.append(
            f'<line x1="{_x1}" y1="79" x2="{_x2}" y2="79" '
            f'stroke="{TRAIT}" stroke-width="2.6" marker-end="url(#arrK)"/>'
        )
_kh_parts.append(_cadre_stroke(w=470, h=150))
_kh_parts.append("</svg>")
FRISE_KHILAFA = "".join(_kh_parts)

# ===========================================================================
# 8. DRAPEAU_MR — drapeau mauritanien (depuis 2017)
# ===========================================================================
_GOLD = "#f2c437"
DRAPEAU_MR = (
    _svg_open("0 0 400 267")
    + f'''
  <rect x="0" y="0" width="400" height="267" rx="6" fill="#1f8a4c"/>
  <rect x="0" y="0" width="400" height="53" fill="{ROUGE}"/>
  <rect x="0" y="214" width="400" height="53" fill="{ROUGE}"/>
  <rect x="0.8" y="0.8" width="398.4" height="265.4" rx="6" fill="none" stroke="{TRAIT}" stroke-width="1.6"/>
  <!-- الهلال (motif centré dans la bande verte : 53-214) -->
  <path d="M 118,118 A 82,82 0 0 0 282,118 A 104,104 0 0 1 118,118 Z" fill="{_GOLD}"/>
  <!-- النجمة -->
  <g transform="translate(0,-12)">
    <polygon fill="{_GOLD}" points="200,78 206.1,95.6 224.7,96 209.9,107.2 215.3,125
             200,114.4 184.7,125 190.1,107.2 175.3,96 193.9,95.6"/>
  </g>
</svg>'''
)

# ===========================================================================
# 9. SCHEMA_INSTITUTIONS — organigramme de la République
# ===========================================================================
SCHEMA_INSTITUTIONS = (
    _svg_open("0 0 420 330")
    + f'''
  <defs><marker id="arrI" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">
    <path d="M0,0 L8,3 L0,6 Z" fill="{TRAIT}"/></marker></defs>
  {_cadre_fill("#fdfaf2", w=420, h=330)}
  <text x="210" y="24" font-size="14" font-weight="700" fill="{TRAIT}" text-anchor="middle">مؤسسات الجمهورية الإسلامية الموريتانية</text>

  <!-- رئيس الجمهورية -->
  <rect x="228" y="44" width="160" height="46" rx="10" fill="{VERT}" opacity="0.18" stroke="{VERT}" stroke-width="2"/>
  <text x="308" y="72" font-size="13" font-weight="700" fill="#1c6b40" text-anchor="middle">رئيس الجمهورية</text>

  <!-- البرلمان -->
  <rect x="32" y="44" width="160" height="46" rx="10" fill="{BLEU}" opacity="0.15" stroke="{BLEU}" stroke-width="2"/>
  <text x="112" y="63" font-size="13" font-weight="700" fill="{BLEU}" text-anchor="middle">البرلمان</text>
  <text x="112" y="81" font-size="11" font-weight="600" fill="{BLEU}" text-anchor="middle">(الجمعية الوطنية)</text>

  <!-- الحكومة -->
  <rect x="256" y="150" width="152" height="52" rx="10" fill="{AMBRE}" opacity="0.16" stroke="{AMBRE}" stroke-width="2"/>
  <text x="332" y="172" font-size="13" font-weight="700" fill="#9a5b06" text-anchor="middle">الحكومة</text>
  <text x="332" y="192" font-size="11" font-weight="600" fill="#9a5b06" text-anchor="middle">(الوزير الأول والوزراء)</text>

  <!-- القضاء (سلطة مستقلة، في الأسفل يمينًا) -->
  <rect x="288" y="262" width="120" height="46" rx="10" fill="#ffffff" stroke="{ROUGE}" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="348" y="281" font-size="13" font-weight="700" fill="{ROUGE}" text-anchor="middle">القضاء ⚖️</text>
  <text x="348" y="300" font-size="11" font-weight="600" fill="{ROUGE}" text-anchor="middle">سلطة مستقلة</text>

  <!-- الشعب -->
  <rect x="130" y="262" width="120" height="46" rx="23" fill="{TRAIT}" opacity="0.9"/>
  <text x="190" y="290" font-size="14" font-weight="700" fill="#ffffff" text-anchor="middle">الشعب 🗳️</text>

  <!-- الأسهم -->
  <path d="M 215,262 L 250,96" fill="none" stroke="{TRAIT}" stroke-width="2" marker-end="url(#arrI)"/>
  <path d="M 160,262 L 116,96" fill="none" stroke="{TRAIT}" stroke-width="2" marker-end="url(#arrI)"/>
  <text x="150" y="192" font-size="11" font-weight="700" fill="{TRAIT}" text-anchor="start">يَنتخبُ</text>
  <text x="212" y="192" font-size="11" font-weight="700" fill="{TRAIT}" text-anchor="end">يَنتخبُ</text>
  <path d="M 332,96 L 332,144" fill="none" stroke="{TRAIT}" stroke-width="2" marker-end="url(#arrI)"/>
  <text x="340" y="124" font-size="11" font-weight="700" fill="{TRAIT}" text-anchor="start">يُعيّنُ</text>
  <!-- البرلمان يراقب الحكومة -->
  <path d="M 112,96 L 112,126 L 300,126 L 300,144" fill="none" stroke="{BLEU}"
        stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#arrI)"/>
  <text x="200" y="120" font-size="11" font-weight="600" fill="{BLEU}" text-anchor="middle">يُراقبُ</text>
  {_cadre_stroke(w=420, h=330)}
</svg>'''
)

# ===========================================================================
# 10. ROSE_VENTS — rose des vents décorative
# ===========================================================================
import math as _math


def _rose_point(cx, cy, angle_deg, tip_r, base_r):
    """Losange d'une pointe de rose des vents (tip, base gauche, centre, base droite)."""
    a = _math.radians(angle_deg)
    a1 = _math.radians(angle_deg - 45)
    a2 = _math.radians(angle_deg + 45)
    pts = [
        (cx + tip_r * _math.cos(a), cy + tip_r * _math.sin(a)),
        (cx + base_r * _math.cos(a1), cy + base_r * _math.sin(a1)),
        (cx, cy),
        (cx + base_r * _math.cos(a2), cy + base_r * _math.sin(a2)),
    ]
    return " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)


_rose_parts = [
    _svg_open("0 0 360 360"),
    _cadre_fill("#ffffff", w=360, h=360),
    # marge intérieure légère (évite le rognage sans rapetisser la rose)
    f'<g transform="translate(18,18) scale(0.95)">'
    f'<circle cx="160" cy="160" r="118" fill="#ffffff" stroke="{TRAIT}" stroke-width="1.6"/>',
    f'<circle cx="160" cy="160" r="94" fill="none" stroke="{TRAIT}" stroke-width="1.2" stroke-dasharray="4 4"/>',
]
# pointes intermédiaires
for _ang in (-45, 45, 135, 225):
    _rose_parts.append(
        f'<polygon points="{_rose_point(160, 160, _ang, 62, 15)}" '
        f'fill="{AMBRE}" opacity="0.45" stroke="{TRAIT}" stroke-width="1.2"/>'
    )
for _ang, _col in ((-90, ROUGE), (0, SABLE), (90, SABLE), (180, SABLE)):
    _rose_parts.append(
        f'<polygon points="{_rose_point(160, 160, _ang, 100, 20)}" '
        f'fill="{_col}" stroke="{TRAIT}" stroke-width="1.3"/>'
    )
_rose_parts.append(
    f'<circle cx="160" cy="160" r="7" fill="{BLEU}" stroke="#ffffff" stroke-width="1.6"/>'
    f'<text x="160" y="36" font-size="16" font-weight="900" fill="{ROUGE}" text-anchor="middle"'
    f' unicode-bidi="isolate">شمال</text>'
    f'<text x="160" y="300" font-size="15" font-weight="900" fill="{TRAIT}" text-anchor="middle"'
    f' unicode-bidi="isolate">جنوب</text>'
    f'<text x="278" y="166" font-size="15" font-weight="900" fill="{TRAIT}" text-anchor="middle"'
    f' unicode-bidi="isolate">شرق</text>'
    f'<text x="42" y="166" font-size="15" font-weight="900" fill="{TRAIT}" text-anchor="middle"'
    f' unicode-bidi="isolate">غرب</text>'
    f'<rect x="208" y="58" width="72" height="18" rx="5" fill="#ffffff" stroke="{TRAIT}" stroke-width="0.8"/>'
    f'<text x="244" y="71" font-size="11" font-weight="800" fill="{TRAIT}" text-anchor="middle"'
    f' unicode-bidi="isolate">شمال شرقي</text>'
    f'<rect x="40" y="58" width="72" height="18" rx="5" fill="#ffffff" stroke="{TRAIT}" stroke-width="0.8"/>'
    f'<text x="76" y="71" font-size="11" font-weight="800" fill="{TRAIT}" text-anchor="middle"'
    f' unicode-bidi="isolate">شمال غربي</text>'
    f'<rect x="208" y="248" width="72" height="18" rx="5" fill="#ffffff" stroke="{TRAIT}" stroke-width="0.8"/>'
    f'<text x="244" y="261" font-size="11" font-weight="800" fill="{TRAIT}" text-anchor="middle"'
    f' unicode-bidi="isolate">جنوب شرقي</text>'
    f'<rect x="40" y="248" width="72" height="18" rx="5" fill="#ffffff" stroke="{TRAIT}" stroke-width="0.8"/>'
    f'<text x="76" y="261" font-size="11" font-weight="800" fill="{TRAIT}" text-anchor="middle"'
    f' unicode-bidi="isolate">جنوب غربي</text>'
    f'</g>'
)
_rose_parts.append(_cadre_stroke(w=360, h=360))
_rose_parts.append('</svg>')
ROSE_VENTS = "".join(_rose_parts)

# ===========================================================================
# 11. CLIMAT_ZONES — zones climatiques
# ===========================================================================
CLIMAT_ZONES = (
    _svg_open()
    + f'''
  <defs><clipPath id="climClip"><path d="{_MR}"/></clipPath></defs>
  {_cadre_fill("#fdfaf2")}
  <path d="{_OCEAN_POLY}" fill="{OCEAN}" opacity="0.6"/>
  <g clip-path="url(#climClip)">
    <rect x="0" y="0" width="420" height="212" fill="{SABLE}"/>
    <rect x="0" y="212" width="420" height="148" fill="{VERT}" opacity="0.3"/>
    <polygon points="62,172 98,172 106,292 62,292" fill="{OCEAN}" opacity="0.75"/>
  </g>
  <path d="{_RIVER}" fill="none" stroke="{BLEU}" stroke-width="2.4" stroke-linecap="round"/>
  <path d="{_MR}" fill="none" stroke="{TRAIT}" stroke-width="{_MR_SW}"/>
  <text x="210" y="26" font-size="14" font-weight="700" fill="{TRAIT}" text-anchor="middle"
        unicode-bidi="isolate">المناطق المناخية في موريتانيا</text>
  <text x="264" y="120" font-size="12" font-weight="700" fill="#8a6d3b" text-anchor="middle"
        unicode-bidi="isolate">المنطقة الصحراوية</text>
  <text x="97" y="232" font-size="11" font-weight="700" fill="{BLEU}" text-anchor="middle"
        transform="rotate(-75 97 232)" unicode-bidi="isolate">المنطقة الساحلية</text>
  <text x="250" y="270" font-size="12" font-weight="700" fill="#1c6b40" text-anchor="middle"
        unicode-bidi="isolate">منطقة الساحل</text>
  <!-- légende (LTR + ancres start fiables) -->
  <rect x="232" y="296" width="178" height="56" rx="8" fill="#ffffff" stroke="{TRAIT}" stroke-width="1.3"/>
  <rect x="244" y="308" width="12" height="10" fill="{SABLE}" stroke="{TRAIT}" stroke-width="0.8"/>
  <text x="262" y="317" font-size="10" fill="{TRAIT}" text-anchor="start" unicode-bidi="isolate">صحراوي: حار وجاف</text>
  <rect x="244" y="324" width="12" height="10" fill="{OCEAN}" stroke="{TRAIT}" stroke-width="0.8"/>
  <text x="262" y="333" font-size="10" fill="{TRAIT}" text-anchor="start" unicode-bidi="isolate">ساحلي: معتدل</text>
  <rect x="244" y="340" width="12" height="10" fill="{VERT}" opacity="0.4" stroke="{TRAIT}" stroke-width="0.8"/>
  <text x="262" y="349" font-size="10" fill="{TRAIT}" text-anchor="start" unicode-bidi="isolate">ساحل: أمطار الخريف</text>
  {_cadre_stroke()}
</svg>'''
)

# ===========================================================================
# 13. HIERARCHIE_LOIS — pyramide الدستور fوق القانون
# ===========================================================================
HIERARCHIE_LOIS = (
    _svg_open("0 0 420 240")
    + f'''
  {_cadre_fill("#fdfaf2", w=420, h=240)}
  <text x="210" y="26" font-size="14" font-weight="700" fill="{TRAIT}" text-anchor="middle">الدستور فوق الجميع 📜</text>
  <!-- pyramide -->
  <polygon points="210,42 290,108 130,108" fill="{VERT}" opacity="0.25" stroke="{VERT}" stroke-width="2"/>
  <text x="210" y="88" font-size="13" font-weight="700" fill="#1c6b40" text-anchor="middle">الدستور</text>
  <text x="210" y="102" font-size="9.5" font-weight="600" fill="#1c6b40" text-anchor="middle">القانون الأعلى للدولة</text>
  <polygon points="122,116 298,116 336,170 84,170" fill="{BLEU}" opacity="0.18" stroke="{BLEU}" stroke-width="2"/>
  <text x="210" y="140" font-size="13" font-weight="700" fill="{BLEU}" text-anchor="middle">القوانين</text>
  <text x="210" y="157" font-size="9.5" font-weight="600" fill="{BLEU}" text-anchor="middle">يضعها البرلمان — لا تخالف الدستور</text>
  <polygon points="76,178 344,178 372,226 48,226" fill="{AMBRE}" opacity="0.18" stroke="{AMBRE}" stroke-width="2"/>
  <text x="210" y="200" font-size="13" font-weight="700" fill="#9a5b06" text-anchor="middle">القرارات والأنظمة</text>
  <text x="210" y="217" font-size="9.5" font-weight="600" fill="#9a5b06" text-anchor="middle">تصدرها الحكومة والإدارة — لا تخالف القانون</text>
  {_cadre_stroke(w=420, h=240)}
</svg>'''
)

# ===========================================================================
# 14. CARTE_HOQOQ — بطاقة حقوق الطفل
# ===========================================================================
_HOQOQ = [("🪪", "الاسم والجنسية"), ("📚", "التعليم"), ("🏥", "الصحة والغذاء"),
          ("👨‍👩‍👧", "العيش مع الأسرة"), ("⚽", "اللعب والراحة"), ("🛡️", "الحماية من الأذى")]
_hq_parts = [
    _svg_open("0 0 420 200"),
    _cadre_fill("#fdfaf2", w=420, h=200),
    f'<rect x="{_CADRE_PAD}" y="{_CADRE_PAD}" width="{420 - 2 * _CADRE_PAD}" height="30" rx="10" fill="{VERT}" opacity="0.85"/>',
    f'<text x="210" y="24" font-size="14" font-weight="700" fill="#ffffff" text-anchor="middle">من حقوق الطفل (اتفاقية 1989)</text>',
]
for _i, (_ic, _lbl) in enumerate(_HOQOQ):
    _cx = 350 - (_i % 3) * 140
    _cy = 66 + (_i // 3) * 74
    _hq_parts.append(
        f'<rect x="{_cx - 62}" y="{_cy - 20}" width="124" height="58" rx="10" fill="#ffffff" stroke="{TRAIT}" stroke-width="1.2"/>'
        f'<text x="{_cx}" y="{_cy + 2}" font-size="17" text-anchor="middle">{_ic}</text>'
        f'<text x="{_cx}" y="{_cy + 26}" font-size="11.5" font-weight="700" fill="{TRAIT}" text-anchor="middle">{_lbl}</text>'
    )
_hq_parts.append(_cadre_stroke(w=420, h=200, color=VERT))
_hq_parts.append("</svg>")
CARTE_HOQOQ = "".join(_hq_parts)

# ===========================================================================
# 15. MIZAN_ADL — ميزان العدل والمساواة
# ===========================================================================
MIZAN_ADL = (
    _svg_open("0 0 420 210")
    + f'''
  {_cadre_fill("#fdfaf2", w=420, h=210)}
  <text x="210" y="26" font-size="14" font-weight="700" fill="{TRAIT}" text-anchor="middle">العدل: الناس سواسية أمام القانون ⚖️</text>
  <!-- socle et mât -->
  <rect x="186" y="176" width="48" height="10" rx="4" fill="{TRAIT}"/>
  <rect x="207" y="52" width="6" height="126" rx="3" fill="{TRAIT}"/>
  <line x1="110" y1="62" x2="310" y2="62" stroke="{TRAIT}" stroke-width="5" stroke-linecap="round"/>
  <circle cx="210" cy="52" r="7" fill="{AMBRE}" stroke="{TRAIT}" stroke-width="1.6"/>
  <!-- plateaux équilibrés -->
  <line x1="110" y1="62" x2="88" y2="112" stroke="{TRAIT}" stroke-width="1.8"/>
  <line x1="110" y1="62" x2="132" y2="112" stroke="{TRAIT}" stroke-width="1.8"/>
  <path d="M 76,112 A 34,30 0 0 0 144,112 Z" fill="{VERT}" opacity="0.3" stroke="{TRAIT}" stroke-width="1.8"/>
  <text x="110" y="132" font-size="11.5" font-weight="700" fill="#1c6b40" text-anchor="middle">حقوقي</text>
  <line x1="310" y1="62" x2="288" y2="112" stroke="{TRAIT}" stroke-width="1.8"/>
  <line x1="310" y1="62" x2="332" y2="112" stroke="{TRAIT}" stroke-width="1.8"/>
  <path d="M 276,112 A 34,30 0 0 0 344,112 Z" fill="{BLEU}" opacity="0.25" stroke="{TRAIT}" stroke-width="1.8"/>
  <text x="310" y="132" font-size="11.5" font-weight="700" fill="{BLEU}" text-anchor="middle">واجباتي</text>
  <text x="210" y="200" font-size="11" font-weight="600" fill="{TRAIT}" text-anchor="middle">لا حقّ بلا واجب، ولا حرية بلا ضوابط يحددها القانون</text>
  {_cadre_stroke(w=420, h=210)}
</svg>'''
)

# ===========================================================================
# 16. SCHEMA_TAAWNIYA — تنظيم التعاونية المدرسية
# ===========================================================================
SCHEMA_TAAWNIYA = (
    _svg_open("0 0 420 250")
    + f'''
  <defs><marker id="arrT" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">
    <path d="M0,0 L8,3 L0,6 Z" fill="{TRAIT}"/></marker></defs>
  {_cadre_fill("#fdfaf2", w=420, h=250)}
  <text x="210" y="24" font-size="13" font-weight="700" fill="{TRAIT}" text-anchor="middle">تنظيم التعاونية المدرسية</text>
  <rect x="120" y="36" width="180" height="36" rx="10" fill="{VERT}" opacity="0.2" stroke="{VERT}" stroke-width="2"/>
  <text x="210" y="59" font-size="12" font-weight="700" fill="#1c6b40" text-anchor="middle">الجمعية العامة (كل التلاميذ)</text>
  <path d="M 210,74 L 210,92" fill="none" stroke="{TRAIT}" stroke-width="2" marker-end="url(#arrT)"/>
  <rect x="218" y="78" width="36" height="14" rx="3" fill="#ffffff"/>
  <text x="236" y="89" font-size="9.5" font-weight="700" fill="{TRAIT}" text-anchor="middle">تنتخب</text>
  <rect x="110" y="96" width="200" height="40" rx="10" fill="{BLEU}" opacity="0.15" stroke="{BLEU}" stroke-width="2"/>
  <text x="210" y="114" font-size="12" font-weight="700" fill="{BLEU}" text-anchor="middle">المكتب التنفيذي</text>
  <text x="210" y="128" font-size="9.5" font-weight="600" fill="{BLEU}" text-anchor="middle">الرئيس · الأمين العام · أمين المال</text>
  <path d="M 210,138 L 210,156" fill="none" stroke="{TRAIT}" stroke-width="2" marker-end="url(#arrT)"/>
  <rect x="218" y="142" width="36" height="14" rx="3" fill="#ffffff"/>
  <text x="236" y="153" font-size="9.5" font-weight="700" fill="{TRAIT}" text-anchor="middle">ينسّق</text>
  <!-- اللجان -->
  <rect x="12" y="162" width="92" height="54" rx="10" fill="#ffffff" stroke="{AMBRE}" stroke-width="1.8"/>
  <path d="M58,188 L58,176" stroke="{VERT}" stroke-width="1.6"/>
  <path d="M58,180 Q52,174 56,170" fill="none" stroke="{VERT}" stroke-width="1.4"/>
  <path d="M58,180 Q64,174 60,170" fill="none" stroke="{VERT}" stroke-width="1.4"/>
  <text x="58" y="206" font-size="10" font-weight="700" fill="#9a5b06" text-anchor="middle">لجنة البستنة</text>
  <rect x="114" y="162" width="92" height="54" rx="10" fill="#ffffff" stroke="{AMBRE}" stroke-width="1.8"/>
  <circle cx="160" cy="180" r="8" fill="#fff" stroke="{TRAIT}" stroke-width="1.3"/>
  <circle cx="160" cy="180" r="3.2" fill="{TRAIT}"/>
  <text x="160" y="206" font-size="10" font-weight="700" fill="#9a5b06" text-anchor="middle">لجنة الرياضة</text>
  <rect x="216" y="162" width="92" height="54" rx="10" fill="#ffffff" stroke="{AMBRE}" stroke-width="1.8"/>
  <rect x="248" y="172" width="28" height="18" rx="2" fill="#fff" stroke="{BLEU}" stroke-width="1.3"/>
  <path d="M252,178 h20 M252,183 h14" stroke="{BLEU}" stroke-width="1.3"/>
  <text x="262" y="206" font-size="10" font-weight="700" fill="#9a5b06" text-anchor="middle">لجنة الثقافة</text>
  <rect x="318" y="162" width="90" height="54" rx="10" fill="#ffffff" stroke="{AMBRE}" stroke-width="1.8"/>
  <path d="M355,172 L363,190 L347,190 Z" fill="#94a3b8" stroke="{TRAIT}" stroke-width="0.8"/>
  <rect x="348" y="188" width="20" height="3.5" rx="1" fill="#64748b"/>
  <text x="363" y="206" font-size="10" font-weight="700" fill="#9a5b06" text-anchor="middle">لجنة النظافة</text>
  <text x="210" y="238" font-size="9.5" font-weight="600" fill="{TRAIT}" text-anchor="middle">التعاونية هيئة غير حكومية تعلّمنا العمل الجماعي وتحمّل المسؤولية</text>
  {_cadre_stroke(w=420, h=250)}
</svg>'''
)

# ===========================================================================
# 17. SCHEMA_MONDE — موريتانيا في المنظمات الدولية والإقليمية
# ===========================================================================
_ORGS = [
    ("الأمم المتحدة", "عضو منذ 1961", BLEU, 210, 62),
    ("الجامعة العربية", "عضو منذ 1973", VERT, 340, 120),
    ("الاتحاد الإفريقي", "منذ 2002 (أ.و.إ 1963)", AMBRE, 296, 208),
    ("اتحاد المغرب العربي", "تأسس 1989", ROUGE, 124, 208),
    ("منظمة استثمار نهر السنغال", "مع السنغال ومالي وغينيا", "#0e7490", 80, 120),
]
_mn_parts = [
    _svg_open("0 0 420 260"),
    _cadre_fill("#fdfaf2", w=420, h=260),
    f'<text x="210" y="24" font-size="14" font-weight="700" fill="{TRAIT}" text-anchor="middle">موريتانيا عضو فاعل في العالم 🌍</text>',
]
for _nom, _sub, _col, _cx, _cy in _ORGS:
    _mn_parts.append(f'<line x1="210" y1="140" x2="{_cx}" y2="{_cy}" stroke="{_col}" stroke-width="1.6" stroke-dasharray="5 4"/>')
for _nom, _sub, _col, _cx, _cy in _ORGS:
    _w = 138 if len(_nom) > 14 else 108
    _mn_parts.append(
        f'<rect x="{_cx - _w // 2}" y="{_cy - 21}" width="{_w}" height="42" rx="12" fill="#ffffff" stroke="{_col}" stroke-width="2"/>'
        f'<text x="{_cx}" y="{_cy - 4}" font-size="10.5" font-weight="700" fill="{_col}" text-anchor="middle">{_nom}</text>'
        f'<text x="{_cx}" y="{_cy + 13}" font-size="9" font-weight="600" fill="{TRAIT}" text-anchor="middle">{_sub}</text>'
    )
_mn_parts.append(
    f'<circle cx="210" cy="140" r="34" fill="{VERT}" opacity="0.9"/>'
    f'<text x="210" y="136" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">موريتانيا</text>'
    f'<text x="210" y="152" font-size="13" text-anchor="middle">🇲🇷</text>'
)
_mn_parts.append(_cadre_stroke(w=420, h=260))
_mn_parts.append("</svg>")
SCHEMA_MONDE = "".join(_mn_parts)

# ===========================================================================
# 18. PLANISPHERE — carte du monde (Natural Earth 110m, domaine public)
# ===========================================================================
_WORLD_LAND = "M179,245 180,246 181,247 179,248 177,249 175,249 172,249 169,249 167,249 168,248 170,248 171,247 173,246 174,245 177,245 179,245Z M162,224 161,225 160,224 158,225 157,226 156,228 154,229 153,230 154,231 156,232 157,233 158,234 158,236 159,237 158,239 156,240 155,241 153,241 151,242 149,242 147,243 145,243 143,243 141,243 138,243 139,244 141,244 143,245 139,245 138,246 137,247 139,247 141,248 143,248 146,249 150,250 153,250 156,250 158,251 160,251 162,252 164,252 166,252 168,251 171,251 173,250 176,250 179,251 181,251 182,250 184,250 187,250 190,250 192,249 195,249 197,249 199,248 198,247 195,247 193,247 190,247 190,245 193,245 195,244 198,243 201,243 202,242 205,242 207,242 210,241 213,241 214,240 216,239 214,239 215,238 217,237 220,237 221,236 222,235 224,235 226,235 228,234 230,235 233,235 235,235 237,235 239,234 241,234 243,234 244,233 246,233 248,234 250,234 251,233 253,233 254,234 255,233 258,233 260,233 262,233 263,234 265,234 267,234 269,234 270,233 273,233 275,232 277,231 279,231 280,232 282,232 283,233 285,232 286,231 289,231 290,230 292,230 293,229 294,230 295,229 297,229 298,228 300,227 302,227 304,227 306,227 307,228 308,229 310,229 312,230 314,230 315,229 317,230 319,230 321,230 322,231 321,233 320,234 321,235 320,236 322,236 324,236 325,235 326,234 327,233 330,233 331,232 333,232 334,230 336,230 337,229 340,229 342,229 344,228 345,227 346,228 347,229 349,229 351,229 353,229 355,229 357,229 360,229 361,228 362,227 364,226 365,227 368,228 370,228 373,228 375,227 377,227 379,228 381,228 383,229 385,229 387,228 389,228 391,228 393,228 395,228 397,228 400,228 402,227 404,227 405,226 405,228 407,228 410,228 413,228 415,228 417,228 418,229 420,230 421,231 423,231 426,231 428,231 430,232 433,232 435,233 437,234 440,234 443,234 446,234 447,235 449,235 448,237 447,238 445,239 443,239 442,240 441,241 440,242 439,243 440,244 441,245 443,245 444,246 441,246 440,247 437,247 436,248 435,249 436,250 438,251 440,251 441,252 443,252 446,253 447,254 450,254 452,254 455,254 458,255 460,255 460,263 10,263 10,255 11,254 13,255 14,254 17,255 19,254 23,254 26,255 30,255 33,256 37,256 41,255 46,256 49,256 53,256 56,255 51,255 47,254 43,253 44,252 42,250 39,250 42,250 45,249 47,250 49,249 51,249 52,248 50,247 48,247 46,247 43,247 41,246 38,245 37,243 39,244 41,244 43,243 44,244 46,244 49,243 52,243 52,241 54,241 57,241 60,240 63,240 66,239 68,240 70,239 71,240 73,240 75,239 76,240 78,240 80,240 82,240 84,240 87,239 90,239 93,238 94,239 95,240 97,240 99,240 101,241 104,240 106,240 107,241 109,241 110,240 108,239 106,239 105,237 108,237 110,237 112,238 115,238 118,238 121,238 123,237 126,238 129,238 132,238 133,239 134,238 136,238 138,238 140,239 143,238 145,238 147,238 149,237 151,237 151,235 150,234 149,233 150,231 151,230 150,229 151,228 152,227 154,226 155,225 157,225 158,224 160,224 162,223 163,224Z M298,149 298,151 297,152 297,154 296,157 296,159 295,162 294,164 294,166 292,167 291,166 290,165 289,162 289,160 290,158 291,157 290,156 290,154 291,153 292,152 294,151 295,150 296,148 296,146 297,147 298,149Z M414,149 415,150 417,151 417,153 418,155 418,157 419,158 421,159 422,160 422,162 423,161 424,163 425,164 426,166 426,168 427,170 427,172 426,174 426,176 425,178 424,179 423,181 423,183 422,184 420,185 419,186 418,187 417,186 416,185 415,186 413,186 411,185 410,184 409,182 408,181 406,181 407,180 407,178 406,179 405,181 404,180 403,178 401,176 399,175 397,176 395,176 394,177 391,177 390,178 389,179 387,179 385,179 384,180 383,181 381,181 379,180 379,178 380,177 379,174 379,172 378,171 378,169 377,168 378,167 377,166 377,164 377,162 378,161 380,160 381,159 383,159 384,158 386,158 387,157 388,156 388,154 389,153 390,154 389,153 390,152 391,151 392,150 393,149 395,150 396,151 397,150 398,148 399,147 401,147 400,145 402,146 404,147 405,146 406,147 405,148 405,150 404,151 405,152 407,153 408,154 410,155 411,154 412,153 412,151 412,149 412,147 413,145 414,146 414,148Z M403,130 403,133 405,132 407,131 409,131 410,132 413,133 416,134 417,135 417,137 420,138 419,139 420,140 421,142 422,143 424,144 422,144 420,144 419,143 418,142 418,140 416,140 414,141 413,142 411,142 410,141 407,141 408,140 408,138 407,136 405,135 402,134 401,135 401,133 402,132 400,132 399,131 398,130 400,129 402,130Z M367,137 365,136 363,135 362,133 361,131 360,129 359,128 358,126 357,125 356,123 354,121 355,120 357,121 358,122 359,123 360,124 361,125 363,126 364,128 365,130 366,131 367,132 368,133 367,135 367,137Z M382,126 384,127 382,127 382,130 381,131 380,134 379,135 378,134 377,133 375,134 374,133 373,131 372,130 371,129 371,126 372,125 373,126 374,124 376,124 377,123 378,122 379,120 380,119 381,118 382,119 383,120 384,121 383,122 382,124 383,125 382,126Z M411,73 411,75 410,76 409,77 407,77 405,78 404,77 402,77 400,78 399,81 398,82 398,80 397,79 398,78 399,77 401,76 403,75 405,75 406,73 409,72 410,70 410,68 412,67 412,69 411,71 411,73Z M231,41 230,43 231,42 233,42 232,44 231,45 234,47 235,49 237,50 236,51 237,52 236,53 234,53 232,53 230,53 228,54 230,52 229,51 230,50 229,49 231,49 230,47 229,46 228,44 228,42 229,41 231,41Z M217,29 218,31 216,32 213,33 212,34 210,33 207,33 208,32 205,32 207,31 205,30 207,29 209,30 211,30 213,30 215,29 217,29Z M16,29 17,28 20,29 23,30 21,31 19,31 19,33 18,32 15,32 13,31 11,30 10,31 10,25 13,27 16,28Z M122,25 125,26 126,28 127,27 128,26 128,24 130,24 132,24 133,25 133,27 131,29 129,30 128,29 127,30 126,31 124,33 122,33 120,35 119,36 117,38 117,40 118,41 119,42 120,43 124,44 126,45 129,46 131,46 132,47 132,49 133,51 135,52 137,50 136,48 135,47 137,46 139,45 139,43 138,42 137,41 138,39 137,35 140,35 142,36 143,35 144,36 145,37 148,37 148,39 150,41 152,41 153,39 154,38 155,40 157,42 158,43 159,45 161,46 163,46 164,48 165,49 165,51 164,52 162,52 160,53 158,54 155,53 153,53 151,55 149,55 148,57 146,59 147,58 149,56 152,55 154,55 155,56 154,57 154,59 156,60 158,60 159,58 160,60 159,61 156,62 153,63 152,62 154,61 152,61 151,62 149,63 147,63 146,64 147,66 145,67 143,67 145,67 143,68 142,69 141,70 141,72 140,73 140,71 140,73 140,75 138,77 137,78 136,79 135,80 134,81 133,82 133,84 134,85 134,87 135,88 135,90 134,91 133,90 132,89 132,87 131,85 130,84 128,84 127,83 124,83 123,84 122,85 120,84 118,84 115,86 114,87 113,88 114,90 113,91 113,94 113,96 114,98 115,100 116,101 118,101 120,101 121,100 122,99 122,97 124,96 126,96 126,98 125,99 126,100 125,101 125,103 124,104 125,105 127,105 129,105 131,106 131,108 131,110 130,111 131,113 132,114 133,115 135,115 136,114 137,115 139,116 140,114 141,113 142,112 144,111 145,110 146,111 145,112 145,114 146,115 146,113 147,111 148,110 149,111 150,112 151,113 153,113 155,113 156,112 158,112 157,113 158,114 159,116 161,116 162,117 163,119 164,120 166,119 168,120 170,122 171,123 172,126 173,127 172,128 174,129 177,130 179,131 181,132 183,133 185,133 187,134 188,136 191,136 191,138 192,139 191,142 190,143 189,145 188,147 187,148 186,149 186,152 186,154 186,156 185,158 184,160 183,162 181,163 179,163 178,164 175,166 174,167 174,169 174,171 173,172 172,175 171,176 170,177 169,178 168,179 166,181 165,180 163,180 162,179 163,181 164,183 163,185 161,186 158,187 157,186 157,188 157,190 155,190 154,189 154,191 155,192 154,193 153,195 152,196 151,198 152,199 153,200 151,201 150,203 149,204 149,206 150,207 148,206 146,207 146,209 144,208 143,207 141,206 141,204 140,201 141,200 142,199 140,198 142,197 142,194 143,195 144,192 143,191 143,193 142,191 143,188 143,186 143,184 144,181 145,179 146,177 145,175 146,173 146,170 147,167 147,164 147,160 147,158 147,156 146,155 143,153 141,151 140,150 139,149 139,147 137,144 136,141 135,139 134,138 133,136 134,134 135,132 134,131 135,129 135,127 136,126 137,125 138,124 139,123 138,122 138,120 138,118 137,117 137,115 135,116 134,118 133,117 132,116 130,116 131,115 130,114 129,113 128,114 128,112 127,111 126,110 125,109 123,108 121,108 120,107 118,105 117,104 115,105 113,105 112,104 110,103 108,102 106,101 105,100 103,99 103,97 103,95 102,94 101,93 100,92 99,91 98,90 97,88 96,87 95,86 94,84 94,82 93,81 91,82 92,83 93,85 94,86 95,88 96,90 97,91 98,93 97,94 96,93 95,92 95,90 94,89 93,88 91,87 92,86 91,85 90,83 89,81 88,79 87,78 86,77 84,77 83,74 82,72 80,70 80,68 80,66 79,65 80,63 80,60 80,58 79,57 81,57 82,58 81,55 79,54 78,53 76,53 75,51 74,50 73,48 72,47 71,46 70,44 68,43 67,42 64,42 63,41 60,40 59,39 57,39 55,39 53,38 51,38 50,39 48,39 47,40 45,40 46,38 47,37 45,38 44,39 42,40 43,41 42,42 40,43 37,44 35,45 33,46 31,47 29,47 30,46 33,45 35,44 37,43 38,42 39,40 37,41 35,40 33,41 32,40 33,39 30,39 29,38 28,37 29,35 30,34 32,34 34,33 33,32 31,32 29,32 27,32 26,31 25,30 27,30 29,29 30,30 33,30 32,29 30,28 28,27 27,26 29,26 31,25 33,23 36,23 39,22 41,22 42,23 45,23 47,23 50,24 53,24 56,24 59,24 61,25 63,25 64,26 65,25 67,24 69,25 71,24 73,24 75,24 76,23 78,25 79,24 80,25 82,24 85,25 88,25 90,26 93,26 91,27 93,27 97,27 99,28 100,27 99,26 101,26 103,26 105,27 108,27 110,27 112,27 113,26 115,27 117,27 117,25 116,24 114,24 115,22 116,21 118,21 119,22 121,24 119,24 122,25Z M92,19 94,20 96,20 98,20 100,21 100,19 102,19 103,20 104,21 107,23 109,24 107,25 105,26 103,25 101,25 99,26 95,26 93,26 91,25 88,24 91,24 93,24 94,23 92,23 89,23 87,23 90,22 88,22 86,22 87,20 91,19Z M127,19 128,20 129,19 132,18 134,20 137,20 140,21 142,21 145,22 146,23 149,23 150,24 151,25 149,26 152,27 154,27 156,29 158,29 157,30 155,31 152,29 150,30 151,31 153,32 154,34 152,34 149,33 151,35 152,36 149,35 146,35 145,34 143,33 141,32 138,33 137,32 138,31 140,31 143,31 142,30 143,29 144,28 143,27 141,26 139,26 140,25 138,24 136,24 133,24 129,24 126,24 124,23 123,22 122,21 123,19 128,18 127,19Z M84,22 81,23 80,22 78,21 79,19 80,18 83,17 85,18 88,18 91,19 89,19 86,20 84,21Z M307,23 302,23 300,22 299,21 301,21 303,19 302,18 305,17 307,16 311,15 316,14 318,14 320,14 316,15 312,16 308,18 306,19 304,20 305,22 307,23Z M117,13 118,14 120,14 122,14 121,15 123,15 124,16 127,16 129,15 132,15 134,15 135,16 134,17 131,17 127,17 125,17 123,17 119,17 119,15 115,14 114,13 117,13Z M369,14 374,14 377,15 376,16 373,17 372,18 375,18 377,19 379,18 383,19 389,20 389,18 392,19 394,19 396,19 396,21 397,22 399,23 400,21 402,22 404,21 407,22 410,22 409,20 411,20 422,21 423,22 426,23 431,22 434,23 435,24 436,25 438,24 440,24 442,25 445,25 447,26 449,25 448,24 452,24 455,24 458,25 460,25 460,31 458,32 459,34 457,35 453,36 450,37 448,38 446,38 443,39 441,39 439,39 438,41 439,42 439,45 437,46 438,47 435,47 435,49 433,49 433,51 431,52 430,49 429,46 430,44 431,43 433,42 435,40 437,38 440,37 441,35 439,35 438,36 435,38 434,36 431,37 428,39 429,40 426,41 424,41 422,39 421,40 417,40 413,40 409,43 404,47 406,47 408,48 409,47 410,48 412,49 411,52 411,54 410,56 408,58 406,61 404,63 402,65 400,64 399,65 397,66 396,68 395,69 394,70 395,71 397,73 397,75 396,76 394,77 393,76 393,74 394,73 393,72 391,72 392,71 391,70 392,69 390,69 388,70 386,70 387,69 388,68 387,67 386,68 385,69 384,70 382,71 383,72 384,73 386,72 388,73 386,74 385,75 384,76 385,77 386,79 387,80 387,82 388,84 387,85 386,86 385,88 384,90 383,92 382,93 380,94 378,95 377,96 375,96 373,96 373,98 372,97 371,96 368,98 367,99 368,102 369,104 371,106 372,108 372,111 370,112 369,113 368,114 366,116 366,114 365,113 364,112 363,110 361,110 361,108 360,110 359,112 359,114 360,115 361,117 362,118 363,119 364,120 364,122 364,124 365,125 365,127 363,125 362,124 361,123 361,121 360,119 359,117 358,116 358,114 358,112 358,110 358,108 357,106 357,104 356,103 354,105 353,104 353,101 352,100 351,99 350,98 350,96 349,94 348,95 347,96 345,96 344,97 343,98 341,99 340,101 339,102 338,103 337,104 336,105 335,106 335,108 335,110 335,113 334,114 333,115 332,116 331,115 330,113 329,111 329,109 328,108 327,105 326,102 326,100 326,98 324,97 321,95 322,94 320,93 319,92 318,90 316,91 314,91 312,91 310,91 308,90 306,88 303,89 302,88 301,87 299,87 299,85 298,83 297,84 296,83 295,84 296,86 297,87 298,89 298,91 299,90 300,91 299,92 300,93 301,92 303,92 304,90 305,89 305,91 306,92 307,93 309,94 310,95 309,96 308,98 307,99 306,101 305,102 304,103 302,103 301,104 300,105 299,106 297,106 296,108 294,108 292,109 290,110 289,109 289,107 288,106 289,105 288,104 288,102 287,101 286,99 285,98 284,97 284,95 283,93 282,92 281,91 280,89 279,87 278,86 279,85 278,86 277,87 276,86 276,84 276,86 277,87 278,89 278,91 280,93 279,94 281,95 281,97 281,99 282,101 283,102 284,103 284,105 286,107 287,108 288,109 289,110 288,111 289,112 290,113 292,112 294,112 295,111 297,111 298,110 299,111 299,113 298,115 297,118 296,120 295,122 293,124 292,125 290,127 289,128 288,130 287,131 286,132 285,133 285,135 283,137 284,139 284,141 285,144 286,145 286,147 286,150 285,152 284,153 283,154 282,155 280,156 279,158 278,159 279,160 279,163 280,164 279,165 276,166 276,168 276,171 274,172 273,174 271,176 270,177 269,178 268,179 266,179 264,179 262,180 260,180 258,179 257,177 258,176 257,174 256,173 255,171 254,169 254,167 253,166 253,164 253,162 252,161 251,158 250,155 250,153 250,151 251,149 252,147 252,145 251,143 252,141 251,140 250,138 250,136 249,134 248,133 247,132 246,130 247,128 247,125 247,123 246,122 244,122 242,122 241,120 240,119 238,119 236,120 234,120 233,121 231,121 229,121 227,121 226,122 224,121 223,120 222,119 221,118 219,118 219,116 218,115 217,114 216,112 215,111 214,110 214,108 213,106 214,105 215,103 215,101 215,99 214,98 214,96 215,95 215,93 216,92 216,90 217,89 219,87 220,86 221,85 223,84 223,82 223,80 224,79 225,78 227,76 228,75 229,76 232,76 233,75 235,75 236,74 239,74 241,73 242,74 243,73 245,73 247,73 248,74 249,73 248,74 249,75 248,77 249,78 251,79 252,80 254,80 255,82 258,83 260,82 260,80 262,79 264,80 265,81 268,81 269,82 271,82 273,81 275,82 277,82 278,81 279,79 280,77 280,75 279,74 276,75 275,74 273,74 271,74 269,72 268,71 269,70 269,68 271,68 272,67 274,67 275,66 277,66 279,66 281,67 283,67 285,67 287,66 286,64 283,62 281,61 283,59 284,58 282,58 281,59 279,59 279,61 281,61 279,61 277,62 276,61 277,60 275,59 273,59 272,61 271,62 270,64 270,66 271,67 269,68 268,67 266,67 265,68 266,69 264,69 263,68 264,69 264,71 265,72 264,73 263,74 262,73 261,71 260,70 259,68 259,66 258,65 257,64 255,63 254,62 253,61 252,62 252,60 250,61 251,63 253,65 254,66 256,67 258,68 256,68 256,70 255,72 255,70 254,69 253,68 252,67 250,66 249,65 248,64 247,63 246,62 245,63 243,64 241,64 239,64 239,66 238,67 236,67 235,69 235,71 234,72 233,73 232,74 230,74 228,75 227,74 226,73 224,73 224,71 223,70 224,69 224,67 224,65 223,64 225,63 227,63 230,64 233,64 234,60 232,58 231,57 229,57 231,55 233,56 233,54 234,55 237,54 237,52 239,52 240,51 241,49 243,49 244,48 245,49 246,48 246,46 245,44 246,43 248,42 248,44 247,46 249,47 250,48 251,47 252,48 254,48 255,47 257,47 260,47 262,46 261,45 262,43 263,42 264,43 265,42 266,41 264,41 266,40 267,39 269,40 271,39 270,38 268,38 266,39 264,39 263,38 262,36 261,35 262,34 263,33 266,32 267,31 265,30 263,30 262,31 260,33 257,35 256,37 257,38 258,39 257,40 256,41 256,43 255,45 253,45 251,46 251,44 250,43 249,41 248,40 245,41 244,42 242,41 242,39 241,36 242,35 246,34 248,32 250,30 253,27 256,26 259,24 262,24 264,24 266,22 268,22 270,22 274,23 273,24 274,25 275,24 277,25 281,25 285,27 286,28 285,30 283,30 277,29 279,30 279,32 280,33 281,32 284,32 286,32 285,31 288,29 290,30 291,29 290,28 289,26 293,27 292,28 293,29 295,29 298,27 302,26 303,27 304,26 307,26 309,26 310,27 311,26 310,25 311,24 314,25 316,25 321,27 320,25 319,24 318,23 321,21 322,19 326,20 325,22 326,23 326,25 327,26 324,29 326,30 327,29 328,28 329,27 328,26 329,25 327,25 328,23 326,22 329,21 328,20 330,21 329,22 330,21 332,21 335,20 337,21 336,20 336,18 338,18 341,18 344,18 343,17 344,16 348,16 351,15 355,15 359,14 361,14 362,13 365,12 368,13 366,13 369,14Z M258,9 262,11 259,11 258,12 257,13 256,14 252,13 253,12 251,12 249,11 248,10 251,9 252,10 254,10 256,9 258,9Z M126,10 128,10 126,10 124,12 121,12 119,11 118,10 116,10 115,9 116,8 117,7 119,7 121,8 123,8 125,9 126,10Z M149,4 153,4 155,5 158,5 155,6 152,6 150,7 153,7 150,8 148,8 146,9 143,10 139,10 141,10 140,12 138,12 137,13 135,13 138,13 134,15 131,14 127,15 126,14 123,14 125,13 129,13 127,12 125,11 128,11 129,10 127,9 130,9 133,8 130,8 126,8 123,8 122,7 121,6 124,6 126,6 128,5 130,5 131,6 132,5 134,5 136,4 140,4 144,4 147,4 149,4Z M201,4 209,5 207,6 202,6 195,6 200,6 204,6 206,6 209,7 215,6 219,6 220,7 215,8 210,9 213,9 211,10 210,11 210,13 212,14 210,14 208,14 210,15 211,16 209,16 211,18 208,18 209,19 207,19 207,21 205,20 206,21 207,22 208,23 206,23 203,22 202,24 205,24 207,24 204,25 200,26 197,27 195,27 192,29 190,30 187,30 185,31 184,32 184,34 181,35 182,36 181,37 181,39 179,39 177,38 175,38 173,37 173,35 170,33 170,31 168,30 168,28 169,26 171,26 171,24 170,25 168,25 167,24 168,23 171,23 169,22 167,22 165,21 167,20 165,18 163,17 162,16 158,15 156,15 152,15 149,15 148,14 146,13 149,13 152,13 146,13 143,12 144,11 148,11 153,10 150,9 151,8 155,7 157,7 160,6 163,6 167,6 169,6 172,5 175,6 177,6 179,7 176,6 177,5 181,4 185,4 187,4 191,4 201,4Z"

def _plani_land_paths(land=_WORLD_LAND):
    """Reste du monde NE ; Antarctique redessiné en continent lisible
    (le polygone NE est un filet collé au bord — illisible en A5)."""
    import re
    polys = re.findall(r'M[^M]+', land)
    rest = ''.join(polys[2:])  # hors Antarctique NE
    # Continent gelé : côtes irrégulières (pas un ovale lisse), océan visible autour
    ant = (
        "M 88,232 L 105,224 L 128,220 L 152,218 L 178,214 L 205,212 L 232,210 "
        "L 258,212 L 285,216 L 312,218 L 338,222 L 362,226 L 388,230 L 410,236 "
        "L 428,244 L 438,252 L 432,258 L 415,262 L 392,266 L 365,268 L 335,270 "
        "L 300,271 L 265,272 L 230,271 L 195,270 L 160,268 L 128,264 L 102,258 "
        "L 82,250 L 74,242 L 78,236 L 88,232 Z"
    )
    return rest, ant


_WORLD_REST, _WORLD_ANT = _plani_land_paths()

_PLANI_LABELS = [
    (330, 82, "آسيا", "#7c4a03", 13),
    (250, 145, "إفريقيا", "#7c4a03", 13),
    (243, 52, "أوروبا", "#7c4a03", 11),
    (115, 120, "أمريكا", "#7c4a03", 13),
    (398, 172, "أستراليا", "#7c4a03", 11),
    (235, 248, "القارة القطبية الجنوبية", "#5b4a32", 10),
    (55, 140, "المحيط الهادي", "#1d5f8f", 10),
    (432, 108, "المحيط الهادي", "#1d5f8f", 9),
    (185, 120, "المحيط الأطلسي", "#1d5f8f", 10),
    (330, 160, "المحيط الهندي", "#1d5f8f", 10),
    (235, 18, "المحيط المتجمد الشمالي", "#1d5f8f", 9),
]
_PLANI_W, _PLANI_H = 470, 268
# Contour léger uniquement (pas de trait noir fort)
_LAND_STROKE = 'stroke="#d2c4a6" stroke-width="0.3" stroke-linejoin="round" stroke-linecap="round"'
_plani_parts = [
    _svg_open(f"0 0 {_PLANI_W} {_PLANI_H}"),
    f'<defs><clipPath id="planiClip">'
    f'<rect x="{_CADRE_PAD + 1}" y="{_CADRE_PAD + 1}" '
    f'width="{_PLANI_W - 2 * (_CADRE_PAD + 1)}" height="{_PLANI_H - 2 * (_CADRE_PAD + 1)}" rx="8"/>'
    f'</clipPath></defs>',
    _cadre_fill("#dbeefe", w=_PLANI_W, h=_PLANI_H),
    f'<g clip-path="url(#planiClip)" transform="translate(0,2) scale(1,0.96)">'
    f'<path d="{_WORLD_REST}" fill="#f0e2bd" {_LAND_STROKE}/>'
    f'<path d="{_WORLD_ANT}" fill="#f0e2bd" {_LAND_STROKE}/>',
    f'<circle cx="222" cy="99" r="5" fill="{VERT}" stroke="#ffffff" stroke-width="1.3"/>',
    f'<text x="214" y="92" font-size="9.5" font-weight="700" fill="#1c6b40" text-anchor="start"'
    f' unicode-bidi="isolate">موريتانيا</text>',
]
for _x, _y, _t, _c, _fs in _PLANI_LABELS:
    _plani_parts.append(
        f'<text x="{_x}" y="{_y}" font-size="{_fs}" font-weight="700" fill="{_c}" '
        f'text-anchor="middle" unicode-bidi="isolate">{_t}</text>'
    )
_plani_parts.append('</g>')
_plani_parts.append(_cadre_stroke(w=_PLANI_W, h=_PLANI_H))
_plani_parts.append("</svg>")
PLANISPHERE = "".join(_plani_parts)


# ---------------------------------------------------------------------------
ALL_ASSETS = {
    "CARTE_MAURITANIE": CARTE_MAURITANIE,
    "CARTE_VIERGE": CARTE_VIERGE,
    "CARTE_VIERGE_VILLES": CARTE_VIERGE_VILLES,
    "CARTE_VIERGE_RICHESSES": CARTE_VIERGE_RICHESSES,
    "CARTE_VIERGE_ROUTES": CARTE_VIERGE_ROUTES,
    "CARTE_RESSOURCES": CARTE_RESSOURCES,
    "CARTE_EMPIRES": CARTE_EMPIRES,
    "CARTE_EMARAT": CARTE_EMARAT,
    "FRISE_SIRA": FRISE_SIRA,
    "FRISE_MAURITANIE": FRISE_MAURITANIE,
    "FRISE_KHILAFA": FRISE_KHILAFA,
    "DRAPEAU_MR": DRAPEAU_MR,
    "SCHEMA_INSTITUTIONS": SCHEMA_INSTITUTIONS,
    "ROSE_VENTS": ROSE_VENTS,
    "CLIMAT_ZONES": CLIMAT_ZONES,
    "HIERARCHIE_LOIS": HIERARCHIE_LOIS,
    "CARTE_HOQOQ": CARTE_HOQOQ,
    "MIZAN_ADL": MIZAN_ADL,
    "SCHEMA_TAAWNIYA": SCHEMA_TAAWNIYA,
    "SCHEMA_MONDE": SCHEMA_MONDE,
    "PLANISPHERE": PLANISPHERE,
}

if __name__ == "__main__":
    for _name, _svg in ALL_ASSETS.items():
        print(f"{_name}: {len(_svg)} caractères")
