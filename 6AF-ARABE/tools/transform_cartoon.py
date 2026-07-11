# -*- coding: utf-8 -*-
"""
Transform Cahier V2 → V3-Cartoon
Stratégie : garder le format A4 (mise en page intacte),
appliquer uniquement le style cartoon (couleurs, police, bordures, spirale décorative).
"""

import re

SRC = "Cahier-Major-LangueArabe-Islamique-6AF-V2.html"
DST = "Cahier-Major-LangueArabe-Islamique-6AF-V3-Cartoon.html"

with open(SRC, encoding="utf-8") as f:
    html = f.read()

# ── 1. Police : Noto Naskh → Cairo ──────────────────────────────────────────
html = html.replace(
    "https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;500;600;700&display=swap",
    "https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&display=swap"
)
html = html.replace("'Noto Naskh Arabic','Traditional Arabic','Tahoma',serif", "'Cairo',sans-serif")
html = html.replace("font-family:'Noto Naskh Arabic'", "font-family:'Cairo'")

# ── 2. Fond body (gris neutre) ───────────────────────────────────────────────
html = html.replace("background:#d8cce8;", "background:#E8EBF0;")

# ── 3. Fond page : crème chaud ───────────────────────────────────────────────
html = html.replace("background:#fdf8f0;", "background:#FAF6EE;")

# ── 4. Couleur principale : violet → bleu royal ──────────────────────────────
html = html.replace("#7c3aed", "#2563eb")
html = html.replace("#4c1d95", "#1e3a5f")
html = html.replace("#c4b5fd", "#93C5FD")
html = html.replace("#f5f3ff", "#EEF2FF")
html = html.replace("#ddd6fe", "#DBEAFE")
html = html.replace("#a78bfa", "#60a5fa")
html = html.replace("#5b21b6", "#1e40af")
html = html.replace("#ede9fe", "#DBEAFE")

# ── 5. Couverture : gradient violet → bleu navy ──────────────────────────────
html = html.replace(
    "background:linear-gradient(160deg,#1e0a4a 0%,#4c1d95 40%,#7c3aed 70%,#a78bfa 100%)",
    "background:linear-gradient(160deg,#0f172a 0%,#1e3a5f 40%,#2563eb 70%,#38bdf8 100%)"
)

# ── 6. Injecter CSS cartoon ──────────────────────────────────────────────────
CARTOON_CSS = """
/* ════════════════════════════════════════
   CARTOON STYLE OVERRIDE — Major 6AF V3
   ════════════════════════════════════════ */

/* Police globale */
body { font-family: 'Cairo', sans-serif !important; }

/* ── Fond page crème ── */
.page { background: #FAF6EE !important; }

/* ── Header néo-brutal ── */
.page-header {
  background: linear-gradient(135deg, #1e3a5f 0%, #2563eb 60%, #38bdf8 100%) !important;
  border-radius: 16px 16px 0 0 !important;
  border-bottom: 3px solid #111 !important;
  padding: 9px 14px 8px !important;
  margin: -2px -2px 8px -2px !important;
  box-shadow: 0 4px 0 #111 !important;
}
.brand-name { color: #fff !important; font-weight: 900 !important; text-shadow: 1px 1px 0 rgba(0,0,0,.3) !important; }
.brand-sub  { color: #BFDBFE !important; }

/* ── Barre étudiant ── */
.info-field { border-bottom: 2px solid #2563eb !important; border-radius: 0 !important; }
.fl { color: #1e3a5f !important; font-weight: 900 !important; }

/* ── Pill de section néo-brutal ── */
.sec-pill {
  border: 2.5px solid #111 !important;
  box-shadow: 3px 3px 0 #111 !important;
  font-weight: 900 !important;
  letter-spacing: 0.3px !important;
}

/* ── Encadré qaida ── */
.qaaida-box {
  background: #EEF2FF !important;
  border: 2.5px solid #111 !important;
  border-radius: 14px !important;
  box-shadow: 4px 4px 0 #111 !important;
}
.qaaida-title { color: #2563eb !important; font-weight: 900 !important; font-size: 13px !important; }
.qaaida-text .hl { background: #DBEAFE !important; color: #1e40af !important; border-radius: 4px !important; padding: 0 3px !important; }

/* ── Cards exercice néo-brutal ── */
.exo-card {
  background: #fff !important;
  border: 2.5px solid #111 !important;
  border-radius: 14px !important;
  box-shadow: 3px 3px 0 #111 !important;
}

/* ── Cercle numéro exo ── */
.exo-circle {
  border: 2px solid #111 !important;
  box-shadow: 2px 2px 0 #111 !important;
  font-weight: 900 !important;
}

/* ── Zone exemple ── */
.exo-example {
  border-radius: 10px !important;
  border: 2px solid #93C5FD !important;
  background: #EEF2FF !important;
}

/* ── Encadré fill-item ── */
.fill-item {
  border: 2px solid #93C5FD !important;
  border-radius: 10px !important;
  background: #F0F7FF !important;
}
.fill-item.two-lines { border-color: #93C5FD !important; }
.fill-index { background: #DBEAFE !important; color: #1e40af !important; border-radius: 6px !important; font-weight: 900 !important; }

/* ── Bank de mots ── */
.word-bank {
  border: 2px solid #2563eb !important;
  border-radius: 10px !important;
  background: #EEF2FF !important;
}
.bank-word { border-color: #2563eb !important; color: #1e3a5f !important; font-weight: 900 !important; }

/* ── Tables ── */
.ex-table th { border: 1.5px solid #111 !important; font-weight: 900 !important; }
.ex-table td { border: 1.5px solid #93C5FD !important; }

/* ── QR strip ── */
.qr-strip {
  background: linear-gradient(135deg, #064e3b, #059669) !important;
  border: 2.5px solid #111 !important;
  border-radius: 14px !important;
  box-shadow: 3px 3px 0 #111 !important;
}
.qr-text { color: #D1FAE5 !important; }
.qr-text strong { color: #fff !important; font-weight: 900 !important; }

/* ── Hint / tip box ── */
.hint-box {
  border: 2px solid #FCD34D !important;
  background: #FFFBEB !important;
  border-radius: 10px !important;
}

/* ── Spirale décorative droite ── */
.spiral-strip {
  position: absolute;
  top: 0; right: 0;
  width: 14mm;
  height: 100%;
  background: linear-gradient(90deg, #3a3a3a 0%, #2a2a2a 100%);
  z-index: 20;
  pointer-events: none;
}
.ring {
  position: absolute;
  right: 0px;
  width: 16px; height: 16px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #8a8580, #3A3530);
  border: 2px solid #1a1a1a;
  box-shadow: 1px 1px 3px rgba(0,0,0,.6);
}

/* ── Circle-grid ── */
.circle-item {
  border: 2px solid #93C5FD !important;
  background: #F0F7FF !important;
  border-radius: 10px !important;
}
.circle-choice {
  border: 2px solid #2563eb !important;
  color: #2563eb !important;
  font-weight: 900 !important;
}

/* ── Writing area ── */
.answer-line { border-bottom-color: #93C5FD !important; }

/* ── Harf / damir items ── */
.harf-item, .damir-item {
  border: 2px solid #93C5FD !important;
  background: #EEF2FF !important;
  border-radius: 8px !important;
  font-weight: 900 !important;
}

/* ── Reading box ── */
.reading-box {
  border: 2px solid #93C5FD !important;
  background: #F0F7FF !important;
  border-radius: 12px !important;
}

/* ── Print : cacher spirale, garder couleurs ── */
@media print {
  .spiral-strip { display: none !important; }
  * { print-color-adjust: exact !important; -webkit-print-color-adjust: exact !important; }
}
"""

html = html.replace("</style>", CARTOON_CSS + "\n</style>", 1)

# ── 7. Injecter spirale dans chaque page normale ─────────────────────────────
rings = "".join(
    f'  <div class="ring" style="top:{10 + i*15}mm"></div>\n'
    for i in range(19)
)
SPIRAL_HTML = f'<div class="spiral-strip" aria-hidden="true">\n{rings}</div>'

def add_spiral(match):
    return match.group(0) + "\n" + SPIRAL_HTML

# Seulement les <div class="page"> sans style inline (pas la couverture)
html = re.sub(r'<div class="page"(?!\s+style)', add_spiral, html)

# ── 8. Sauvegarder ──────────────────────────────────────────────────────────
with open(DST, "w", encoding="utf-8") as f:
    f.write(html)

orig_size = len(open(SRC, encoding='utf-8').read())
print(f"✅ {DST}")
print(f"   Original : {orig_size:,} chars")
print(f"   V3       : {len(html):,} chars")
print(f"   Pages    : {html.count('class=\"page\"')} pages")
