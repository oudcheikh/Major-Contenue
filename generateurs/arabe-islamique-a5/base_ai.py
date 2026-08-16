# -*- coding: utf-8 -*-
"""Socle du cahier A5 عربية/إسلامية — style « dfatir Major » repris du cahier A4
original (archives/Cahier-Major-LangueArabe-Islamique-6AF.SOURCE.html) :
dos relié bleu nuit + onglets de section, pages papier crème, cartes d'exercices
blanches à liseré coloré avec lignes d'écriture, tableaux à en-tête bleu nuit
avec cellules à remplir. Violet = اللغة العربية · vert = التربية الإسلامية.
Les composants gardent la même signature que le kit maths : les fichiers de
contenu (unites_ar_1..3.py, unites_isl.py) n'ont pas besoin de changer."""
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, '..', 'math-a5')))

from base_a5 import CSS_ASSETS  # noqa: F401  (mascottes, logo, QR déco en base64)

DOC_ID = 'دفتر ماجور · اللغة العربية والتربية الإسلامية<br>السنة السادسة الأساسية 6AF'

# ─────────────────────────── CSS ───────────────────────────
CSS = """
:root{
  --paper:#fffdf8; --ink:#182230; --muted:#5c6776;
  --ar:#7c3aed; --is:#059669; --navy:#1e293b;
  --part:#7c3aed; --part-lite:#a78bfa; --part-soft:#f3f0ff; --part-border:#c4b5fd;
  --p-yell:#ffd98c; --p-rose:#ffc7ba; --p-green:#c6e9a4; --p-blue:#1d7fc4; --p-lila:#e6c7f2;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  font-family:'Cairo','Tahoma','Arial',sans-serif;
  background:linear-gradient(180deg,#efe6d8 0%,#e8dbc8 100%);
  color:var(--ink);direction:rtl;
}
.sheet{
  width:148mm;height:210mm;margin:6mm auto;background:var(--paper);
  display:flex;flex-direction:row;overflow:hidden;position:relative;
  box-shadow:0 10px 26px rgba(15,23,42,.16);border-radius:5mm 0 0 5mm;
}
.part-ar{--part:#7c3aed;--part-lite:#a78bfa;--part-soft:#f3f0ff;--part-border:#c4b5fd}
.part-isl{--part:#059669;--part-lite:#34d399;--part-soft:#e6f7f1;--part-border:#8ee0c3}

/* ── dos relié (bord droit) — gris ardoise (économie d'encre) ── */
.spine{
  width:5.5mm;flex-shrink:0;position:relative;
  background:linear-gradient(180deg,#94a3b8,#64748b);
  display:flex;flex-direction:column;justify-content:space-between;align-items:center;
  padding:5mm 0;border-radius:0 5mm 5mm 0;
}
.spine:before{
  content:"";position:absolute;left:0;top:0;bottom:0;width:.6mm;
  background:linear-gradient(180deg,rgba(255,255,255,.25),rgba(255,255,255,0),rgba(255,255,255,.25));
}
.holes{display:flex;flex-direction:column;gap:3.2mm}
.hole{width:1.6mm;height:1.6mm;border-radius:50%;background:rgba(255,255,255,.22);border:.25mm solid rgba(255,255,255,.15)}
.spine-title{
  writing-mode:vertical-rl;transform:rotate(180deg);
  color:rgba(255,255,255,.92);font-size:6.5px;font-weight:800;letter-spacing:1px;
}
/* ── onglets (bord gauche) — inset ≥1.5mm du trim ── */
.tabs{width:4mm;flex-shrink:0;display:flex;flex-direction:column;margin:4mm 0 4mm 1.6mm}
.tab{
  flex:1;color:#fff;font-size:6.5px;font-weight:900;letter-spacing:.5px;opacity:.38;
  display:flex;align-items:center;justify-content:center;writing-mode:vertical-rl;
  border-radius:1.2mm 0 0 1.2mm;
}
.tab-active{flex:1.6;opacity:1}

/* ── colonne principale — marges safe ≥5mm ── */
.page-main{flex:1;display:flex;flex-direction:column;min-width:0;position:relative}
.page-header{
  display:flex;justify-content:space-between;align-items:center;gap:2mm;
  padding:4mm 5mm 1.8mm;border-bottom:.35mm solid rgba(17,24,39,.08);flex-shrink:0;
}
.brand{display:flex;align-items:center;gap:2mm;min-width:0}
.brand .logo,.brand .im-logo{
  width:8.5mm;height:8.5mm;border-radius:2mm;flex-shrink:0;
  background-size:contain;background-repeat:no-repeat;background-position:center;
}
.brand-text{display:flex;flex-direction:column;justify-content:center;gap:.35mm;min-width:0;line-height:1.15}
.brand-title{font-size:9px;font-weight:900;color:var(--ink);line-height:1.15;margin:0}
.brand-sub{font-size:7px;color:var(--muted);font-weight:700;line-height:1.2;margin:0}
.subject-tag{
  background:var(--part);color:#fff;padding:1mm 3.2mm;border-radius:999px;
  font-size:7px;font-weight:900;letter-spacing:.15px;max-width:68mm;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
}
.page-body{
  flex:1;overflow:hidden;padding:2.4mm 5mm 18mm;position:relative;min-width:0;
  display:flex;flex-direction:column;
}
.page-body>*{flex-shrink:0}
/* QR hors flux : réserve basse incompressible + padding footer */
.page-main:has(.qr-corr) .page-body{padding-bottom:12mm}
.qr-reserve{
  height:26mm;width:100%;flex:0 0 26mm;margin-top:auto;
  pointer-events:none;visibility:hidden;margin-bottom:0;padding:0;border:0;
}
.page-main:has(.qr-corr) .self-eval{margin-left:24mm}
.page-footer{
  position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;
  align-items:flex-end;padding:0 5mm 3.2mm 24mm;font-size:6.5px;color:var(--muted);font-weight:700;
}
.page-main:has(.qr-corr) .page-footer{padding-left:28mm}
.bottom-number{
  position:absolute;left:50%;transform:translateX(-50%);bottom:2.8mm;
  min-width:7mm;height:7mm;border-radius:999px;background:#fff;
  border:.5mm solid var(--part);display:flex;align-items:center;justify-content:center;
  font-size:8.5px;font-weight:900;color:var(--ink);z-index:5;
  font-variant-numeric:tabular-nums;
}

/* ── titre de leçon ── */
.lesson-title{
  font-size:12.5px;font-weight:900;margin:.4mm 0 1.6mm;color:var(--ink);
  display:flex;align-items:center;gap:1.8mm;
}
.lesson-title:after{content:"";flex:1;height:1.1mm;border-radius:999px;
  background:linear-gradient(90deg,var(--part),transparent)}

/* ── bandeau d'unité ── */
.unit-banner{
  position:relative;overflow:hidden;border-radius:3.5mm;color:#fff;
  background:linear-gradient(120deg,var(--part) 0%,var(--part-lite) 100%);
  padding:2.2mm 3.2mm;margin-bottom:1.8mm;display:flex;align-items:center;gap:2.4mm;
}
.unit-banner:before{content:"";position:absolute;width:26mm;height:26mm;border-radius:50%;
  background:rgba(255,255,255,.13);top:-14mm;left:8mm}
.unit-banner:after{content:"";position:absolute;width:16mm;height:16mm;border-radius:50%;
  background:rgba(255,255,255,.1);bottom:-9mm;left:34mm}
.unit-banner .ub-num{
  width:7.5mm;height:7.5mm;border-radius:50%;background:#fff;color:var(--part);
  display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:900;flex-shrink:0;
  box-shadow:none;
}
.unit-banner b{font-size:11px;font-weight:900;display:block;line-height:1.25}
.unit-banner small{font-size:6.8px;font-weight:700;color:rgba(255,255,255,.92);display:block}

/* ── rangée de section (أتعلّم / تمارين …) ── */
.badge-row{display:flex;align-items:center;gap:1.8mm;margin:1.6mm 0 1.2mm}
.badge-row .num-badge{
  width:6mm;height:6mm;border-radius:50%;background:var(--part);color:#fff;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
  box-shadow:none;overflow:hidden;line-height:0;
}
.badge-row .num-badge svg{width:3.3mm;height:3.3mm;display:block}
.badge-row .bl{font-size:10.5px;font-weight:900;color:var(--ink)}
.badge-row .bs{
  font-size:6.4px;font-weight:800;color:var(--part);background:var(--part-soft);
  border:.35mm solid var(--part-border);border-radius:999px;padding:.5mm 2.6mm;
}
.badge-row .mascot{width:8.5mm;height:8mm;margin-inline-start:auto;background:transparent!important;box-shadow:none!important;filter:none!important}

/* ── objectifs (في هذه الوحدة سأتعلّم) ── */
.objectifs{
  background:#fff;border:.4mm solid var(--part-border);border-radius:3mm;
  padding:1.6mm 2.8mm;margin-bottom:1.6mm;box-shadow:none;
}
.part-isl .objectifs{background:#fff;border-color:#a8dcc8}
.objectifs b{
  font-size:8px;font-weight:900;color:var(--part);
  display:block;margin-bottom:.7mm;line-height:1.45;
}
.objectifs b .ico-svg{
  width:1.15em;height:1.15em;vertical-align:-0.2em;margin-left:.35em;
  display:inline-block;
}
.objectifs ul{margin:0;padding:0;list-style:none}
.objectifs li{
  font-size:7.6px;font-weight:700;line-height:1.7;padding-right:5.2mm;position:relative;
  min-height:3.2mm;display:flex;align-items:center;
}
.objectifs li:before{
  content:"";position:absolute;right:.4mm;top:50%;transform:translateY(-50%);
  width:2.4mm;height:2.4mm;border:.4mm solid var(--part);border-radius:.5mm;
  background:#fff;box-shadow:none;
}

/* ── cadre de leçon ── */
.frame{
  background:#fff;border:.4mm solid rgba(17,24,39,.1);border-radius:3.5mm;
  padding:2.2mm 3mm;margin:1.2mm 0;position:relative;
  box-shadow:none;
  border-top:1.2mm solid var(--part);
}
.frame ul{margin:.6mm 0 0;padding-right:4.5mm}
.frame li{font-size:8.2px;font-weight:700;line-height:1.7}
.frame.has-video{padding-left:26mm;min-height:32mm;overflow:hidden}
.video-box{
  position:absolute;left:2mm;top:2.8mm;width:21.5mm;max-width:calc(100% - 4mm);
  text-align:center;box-sizing:border-box;
  background:#fff;border:.35mm dashed var(--part-border);border-radius:2mm;
  padding:.7mm .55mm .55mm;box-shadow:none;
}
.video-box .vb-cap{
  font-size:6.5px;font-weight:900;color:var(--part);line-height:1.25;
  display:block;margin-top:.45mm;
}
.video-box .qr,.video-box img.qr{
  width:15.5mm;height:15.5mm;display:block;margin:0 auto;
  border-radius:0;background:transparent!important;box-shadow:none!important;
  object-fit:contain;
}

/* ── règles / méthode / boîtes ── */
.rule-box{
  border-radius:3mm;padding:1.8mm 3mm;margin:1.2mm 0;font-size:8.2px;line-height:1.65;
  font-weight:700;border-right:1.4mm solid var(--part);background:var(--part-soft);color:#3b2b63;
}
.part-isl .rule-box{color:#0c4a36}
.rule-box b.rb-title{display:block;font-size:8.6px;font-weight:900;color:var(--part);margin-bottom:.5mm}
.rule-box ol{margin:.4mm 0 0;padding-right:5mm}
.rule-box ol li{margin-bottom:.5mm}
.tip-card{
  background:#fffbeb;border:.45mm solid #fcd34d;border-radius:3mm;
  padding:1.6mm 2.8mm;margin:1.2mm 0;font-size:7.8px;line-height:1.65;font-weight:700;color:#713f12;
}
.tip-card b{color:#b45309;font-weight:900}
.warn-card{
  background:#fef2f2;border-right:1.4mm solid #dc2626;border-radius:3mm;
  padding:1.6mm 2.8mm;margin:1.2mm 0;font-size:7.8px;line-height:1.65;font-weight:700;color:#7f1d1d;
}
.warn-card b{color:#dc2626;font-weight:900}
.defi-card{
  background:linear-gradient(135deg,#fffbeb,#fef3c7);border:.55mm dashed #f59e0b;border-radius:3mm;
  padding:1.6mm 2.8mm;margin:1.2mm 0;font-size:7.8px;line-height:1.65;font-weight:800;color:#92400e;
}
.defi-card b{color:#d97706;font-weight:900}

/* ── exemple résolu ── */
.exemple{
  background:#f8f9fb;border-right:1.1mm solid #cbd5e1;border-radius:2.6mm;
  padding:1.5mm 2.8mm;margin:1.2mm 0;font-size:7.9px;line-height:1.6;font-weight:700;color:#334155;
}
.exemple .tag{color:var(--part);font-weight:900;font-size:7.8px}

/* ── cartes d'exercices ── */
.exo-card{
  background:#fff;border:.4mm solid rgba(17,24,39,.09);border-radius:3.2mm;
  border-top:1.2mm solid var(--part);
  padding:1.8mm 2.8mm 1.6mm;margin:1.4mm 0;
  box-shadow:none;
}
.exo-top{display:flex;justify-content:space-between;align-items:center;gap:2mm;margin-bottom:.9mm}
.exo-num{display:flex;align-items:center;gap:1.4mm;font-size:8.4px;font-weight:900;color:var(--ink)}
.exo-num i{
  font-style:normal;width:4.8mm;height:4.8mm;border-radius:50%;background:var(--part);color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:7.5px;font-weight:900;flex-shrink:0;
}
.exo-level,.lvl{
  font-size:6.8px;font-weight:900;padding:.45mm 2mm;border-radius:999px;
  background:#fef3c7;color:#92400e;border:.3mm solid #fcd34d;letter-spacing:0;
  box-shadow:none;
}
.exo-text{font-size:8.2px;line-height:1.85;font-weight:700}
.consigne{font-size:8.4px;font-weight:900;margin:1mm 0 .6mm}

/* ── lignes d'écriture / cases à remplir ── */
.dots,.lines{margin-top:.9mm}
.dotl,.line,.wline{height:5.8mm;border-bottom:.5mm dashed #c9c2ea;margin-bottom:.3mm}
.composer-fill{margin:1.6mm 0 1mm}
.composer-fill .consigne{font-size:7.8px;margin-bottom:.4mm;color:#5b5478}
.part-isl .dotl,.part-isl .line,.part-isl .wline{border-bottom-color:#a8dcc8}
.oval{
  display:inline-block;min-width:28mm;height:6mm;vertical-align:-1.6mm;margin:.2mm 1mm;
  border-bottom:.55mm dashed var(--part-lite);
  background:transparent;border-radius:0;box-shadow:none;
}
.oval.s{min-width:20mm;height:5.6mm}

/* ── tableaux ── */
.ai-table{
  width:100%;border-collapse:separate;border-spacing:0;direction:rtl;margin:1.2mm 0;
  border-radius:0;overflow:hidden;
}
.ai-table th{
  font-size:7.6px;font-weight:900;padding:1.2mm 1.6mm;text-align:center;
  background:var(--navy);color:#fff;border:.3mm solid var(--navy);border-radius:0;
}
.ai-table th:first-child,.ai-table th:last-child{border-radius:0}
.ai-table td{
  border:.3mm solid #e2e8f0;padding:1mm 1.6mm;text-align:center;
  font-size:8px;font-weight:700;line-height:1.5;background:#fff;border-radius:0;
}
.ai-table tr:nth-child(odd) td{background:#f8fafc}
.ai-table td.r{text-align:right}
.ai-table .fill{background:#fff !important}
.ai-table .fill .dotl{height:5.6mm;margin:0;border-bottom-color:#d3ccef}

/* ── verset / hadith ── */
.ayah{
  background:linear-gradient(135deg,#eef8f4,#f4f8ee);border:.45mm solid #9dc9ae;border-radius:3mm;
  padding:1.8mm 3.2mm;margin:1.4mm 0;font-size:9px;font-weight:800;line-height:1.9;
  text-align:center;color:#1d5c40;
}
.ayah small{display:block;font-size:6.6px;font-weight:900;color:#4a7a5c;margin-top:.5mm}

/* ── bulle mascotte ── */
.bulle-row{display:flex;align-items:center;gap:2mm;margin:1.2mm 0}
.bulle-row .im{width:10.5mm;height:9.5mm;flex-shrink:0}
.bulle-row .bulle{
  flex:1;background:#fff;border:.5mm solid var(--part-border);border-radius:3mm;
  padding:1.4mm 2.6mm;font-size:7.6px;font-weight:800;line-height:1.65;color:#3b3557;
  position:relative;box-shadow:none;
}
.part-isl .bulle-row .bulle{color:#134e3a}
.bulle-row .bulle:before{
  content:"";position:absolute;right:-1.35mm;top:50%;margin-top:-1.35mm;
  width:2.7mm;height:2.7mm;background:#fff;box-sizing:border-box;
  border-right:.5mm solid var(--part-border);border-top:.5mm solid var(--part-border);
  transform:rotate(45deg);
}

/* ── auto-évaluation ── */
.self-eval{
  display:flex;align-items:center;gap:2.4mm;margin-top:1.6mm;margin-left:14mm;
  background:linear-gradient(135deg,#ecfdf5,#d1fae5);border:.5mm solid #10b981;border-radius:3mm;
  padding:1.6mm 2.8mm;
}
.self-eval .im{width:11mm;height:10mm;flex-shrink:0}
.self-eval .se-txt{font-size:7.6px;font-weight:900;color:#065f46;line-height:1.5}
.self-eval .se-stars{margin-inline-start:auto;display:flex;gap:1.2mm;font-size:13px;color:#10b981;letter-spacing:1px}

/* ── divers ── */
.hl{background:rgba(253,230,138,.45);border-radius:.6mm;padding:0 .4mm;font-weight:900;box-shadow:none;text-shadow:none}
.uw{text-decoration:underline;text-decoration-style:wavy;text-decoration-color:#c0392b;font-weight:900;text-shadow:none}
.unit-chip{display:none}
.scallop{
  background:var(--part-soft);border:.45mm solid var(--part-border);border-radius:3mm;
  padding:1.6mm 2.8mm;font-size:7.4px;font-weight:800;line-height:1.7;color:#3b2b63;
  box-shadow:none;
}
.ico-svg{
  width:1.1em;height:1.1em;display:inline-block;
  vertical-align:-0.18em;margin-left:.3em;flex-shrink:0;
}
.ico-inline{display:inline;color:var(--part)}
.ico-inline .ico-svg{width:1.05em;height:1.05em;vertical-align:-0.16em;margin-left:.25em}
.tip-card b,.warn-card b,.defi-card b{display:inline;font-weight:900}
.tip-card .ico-svg,.warn-card .ico-svg,.defi-card .ico-svg,.objectifs .ico-svg{
  vertical-align:-0.18em;
}
.bulle-row .im,.badge-row .mascot,.self-eval .im{
  background-color:transparent!important;box-shadow:none!important;filter:none!important;
}
.qr-corr{
  position:absolute;left:5mm;bottom:3.2mm;z-index:6;width:18.5mm;
  background:#fff;border:.45mm solid;border-radius:2mm;padding:1mm .7mm .55mm;
  text-align:center;box-shadow:none!important;overflow:hidden;box-sizing:border-box;
  filter:none!important;
}
.qr-corr img{
  width:15mm;height:15mm;display:block;margin:0 auto;
  background:transparent!important;box-shadow:none!important;object-fit:contain;
}
.qr-corr span{display:block;font-size:6.5px;font-weight:900;line-height:1.2;margin-top:.45mm}

.toolbar{position:fixed;top:10px;left:14px;z-index:9999}
.action-btn{
  border:none;border-radius:999px;padding:9px 15px;font-family:'Cairo',sans-serif;
  font-size:13px;font-weight:800;cursor:pointer;background:#2563eb;color:#fff;
  box-shadow:0 8px 20px rgba(15,23,42,.18);
}

@media print{
  @page{size:A5 portrait;margin:0}
  .toolbar{display:none !important}
  html,body{background:#fff !important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .sheet{
    width:148mm !important;height:210mm !important;margin:0 !important;
    box-shadow:none !important;border-radius:0 !important;
    break-after:page;page-break-after:always;overflow:hidden !important;
  }
  .sheet:last-of-type{break-after:auto !important;page-break-after:auto !important}
  .spine{border-radius:0 !important}
  .tabs{margin:4mm 0 !important}
}
"""


# ─────────────────────────── composants ───────────────────────────
OVAL = '<span class="oval"></span>'
OVS = '<span class="oval s"></span>'

_BADGE_ICONS = {
    'أتعلّم': ('book',
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#fff" d="M6.5 3A2.5 2.5 0 0 0 4 5.5v13A2.5 2.5 0 0 0 6.5 21H20V3H6.5zm0 1.5H18.5v15H6.5a1 1 0 0 1-1-1v-13a1 1 0 0 1 1-1zm5.2 2.2v10.6l-2.4-1.3-2.4 1.3V6.7h4.8z"/></svg>'),
    'تمارين': ('pencil',
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#fff" d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 0 0 0-1.41l-2.34-2.34a1 1 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>'),
    'أقرأ': ('book',
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#fff" d="M6.5 3A2.5 2.5 0 0 0 4 5.5v13A2.5 2.5 0 0 0 6.5 21H20V3H6.5zm0 1.5H18.5v15H6.5a1 1 0 0 1-1-1v-13a1 1 0 0 1 1-1zm5.2 2.2v10.6l-2.4-1.3-2.4 1.3V6.7h4.8z"/></svg>'),
    'أجيب': ('pencil',
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#fff" d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 0 0 0-1.41l-2.34-2.34a1 1 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>'),
    'أقرأ وأجيب': ('book',
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#fff" d="M6.5 3A2.5 2.5 0 0 0 4 5.5v13A2.5 2.5 0 0 0 6.5 21H20V3H6.5zm0 1.5H18.5v15H6.5a1 1 0 0 1-1-1v-13a1 1 0 0 1 1-1zm5.2 2.2v10.6l-2.4-1.3-2.4 1.3V6.7h4.8z"/></svg>'),
    'أتحدّى': ('trophy',
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#fff" d="M6 3h12v2h2a2 2 0 0 1 2 2v1a5 5 0 0 1-4.1 4.9A5.01 5.01 0 0 1 13 16.9V18h3v2H8v-2h3v-1.1A5.01 5.01 0 0 1 6.1 12.9 5 5 0 0 1 2 8V7a2 2 0 0 1 2-2h2V3zm0 2H4v3a3 3 0 0 0 3 3V8H6V5zm12 0v3h-1v2.9a3 3 0 0 0 3-3V5h-2z"/></svg>'),
    'أراجع': ('refresh',
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#fff" d="M12 5V2L8 6l4 4V7a5 5 0 1 1-4.9 6.1l-1.96.4A7 7 0 1 0 12 5z"/></svg>'),
    'أكتب': ('write',
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#fff" d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 0 0 0-1.41l-2.34-2.34a1 1 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>'),
}
_BADGE_FALLBACK = (
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#fff" d="M12 2l2.4 7.2H22l-6 4.4 2.3 7.2L12 16.8 5.7 20.8 8 13.6 2 9.2h7.6z"/></svg>'
)


def badge_row(label, sub, mascot_key):
    icon = _BADGE_ICONS.get(label, (None, _BADGE_FALLBACK))[1]
    return f'''<div class="badge-row">
      <span class="num-badge">{icon}</span>
      <span class="bl">{label}</span>
      <span class="bs">{sub}</span>
      <span class="im im-{mascot_key} mascot" role="img" aria-label=""></span>
    </div>'''


def video_box():
    return '''<div class="video-box">
      <span class="im im-qr qr" role="img" aria-label="QR فيديو الدرس"></span>
      <span class="vb-cap">امسح وشاهد<br>فيديو الدرس</span>
    </div>'''


def exo(n, lvl, body):
    lv = f'<span class="exo-level">{_print_lvl(lvl)}</span>' if lvl else ''
    return f'''<div class="exo-card">
      <div class="exo-top"><span class="exo-num"><i>{n}</i> التمرين {n}</span>{lv}</div>
      <div class="exo-text">{body}</div>
    </div>'''


def _print_lvl(lvl):
    """Niveaux sans emoji couleur (impression fiable)."""
    if not lvl:
        return ''
    n = lvl.count('⭐') + lvl.count('★')
    if n >= 3:
        return 'صعب'
    if n == 2:
        return 'متوسط'
    if n == 1:
        return 'سهل'
    return lvl


def print_sanitize(html):
    """Remplace emojis / symboles colorés pour un rendu print stable."""
    if not html:
        return html
    repl = [
        ('⭐⭐⭐', 'صعب'), ('⭐⭐', 'متوسط'), ('⭐', 'سهل'),
        ('✓', 'صح'), ('✔', 'صح'), ('✗', 'خطأ'), ('✘', 'خطأ'),
        ('📱', ''), ('📲', ''), ('✏️', ''), ('✏', ''), ('📖', ''), ('📘', ''),
        ('✍️', ''), ('✍', ''), ('🌟', ''), ('🎉', ''), ('🏆', ''),
        ('🌊', ''), ('🏫', ''), ('☪️', ''), ('☪', ''), ('🔤', ''),
        ('🖨', ''), ('🖨️', ''), ('☆', '○'), ('🇲🇷', ''),
        ('🗺️', ''), ('🗺', ''), ('🏰', ''), ('🤝', ''), ('🌍', ''),
        ('⚔️', ''), ('⚔', ''), ('🕌', ''), ('🏜️', ''), ('🏜', ''),
        ('🌾', ''), ('⛏️', ''), ('⛏', ''), ('🐟', ''), ('💧', ''),
        ('⚠️', ''), ('⚠', ''), ('💡', ''), ('🧭', ''),
    ]
    for a, b in repl:
        html = html.replace(a, b)
    html = re.sub(r'[ \t]{2,}', ' ', html)
    return html


def tok(n):
    return f'<span class="exo-num"><i>{n}</i></span>'


_ICO_TARGET = '<svg class="ico-svg" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="1.8" fill="currentColor"/><path fill="#ef4444" d="M18.5 3.2l1.2 3.4-2.6 1.1 2.2 2.8-3.3-1.4-1.1 2.7-1.2-6.6z"/></svg>'
_ICO_TIP = '<svg class="ico-svg" viewBox="0 0 24 24" aria-hidden="true"><path fill="#f59e0b" d="M9 21h6v-1.5H9V21zm3-19a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2z"/></svg>'
_ICO_WARN = '<svg class="ico-svg" viewBox="0 0 24 24" aria-hidden="true"><path fill="#dc2626" d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/></svg>'
_ICO_TROPHY = '<svg class="ico-svg" viewBox="0 0 24 24" aria-hidden="true"><path fill="#d97706" d="M6 3h12v2h2a2 2 0 0 1 2 2v1a5 5 0 0 1-4.1 4.9A5.01 5.01 0 0 1 13 16.9V18h3v2H8v-2h3v-1.1A5.01 5.01 0 0 1 6.1 12.9 5 5 0 0 1 2 8V7a2 2 0 0 1 2-2h2V3z"/></svg>'
_ICO_PENCIL = '<svg class="ico-svg" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 0 0 0-1.41l-2.34-2.34a1 1 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>'


def consigne(*args):
    """consigne(txt) ou consigne(n, txt) — même API que le kit maths.
    Avec numéro : même libellé que exo() → « التمرين N » à côté du cercle."""
    if len(args) == 2:
        n, txt = args
        return (f'<div class="consigne">'
                f'<span class="exo-num"><i>{n}</i> التمرين {n}</span> {txt}</div>')
    return f'<div class="consigne"><span class="ico-inline">{_ICO_PENCIL}</span> {args[0]}</div>'


def dots(n):
    return '<div class="lines">' + '<div class="line"></div>' * n + '</div>'


def wlines(n):
    return dots(n)


def objectifs(items):
    lis = ''.join(f'<li>{i}</li>' for i in items)
    return f'<div class="objectifs"><b>{_ICO_TARGET} في هذه الوحدة سأتعلّم:</b><ul>{lis}</ul></div>'


def methode(title, steps):
    lis = ''.join(f'<li>{s}</li>' for s in steps)
    return f'<div class="rule-box"><b class="rb-title">{title}</b><ol>{lis}</ol></div>'


def astuce(txt):
    return f'<div class="tip-card"><b>{_ICO_TIP} أستاذ ماجور ينصح:</b> {txt}</div>'


def attention(txt):
    return f'<div class="warn-card"><b>{_ICO_WARN} انتبه!</b> {txt}</div>'


def exemple(txt, tag='مثال للتوضيح:'):
    """Bloc d'exemple pédagogique — à ajouter sans modifier le contenu existant."""
    return f'<div class="exemple"><b class="tag"><span class="ico-inline">{_ICO_PENCIL}</span> {tag}</b> {txt}</div>'


def defi(txt, lines=2):
    """Défi avec lignes d'écriture intégrées (c'est un cahier : l'élève répond dedans)."""
    ls = '<div class="lines">' + '<div class="line" style="height:5.2mm"></div>' * lines + '</div>' if lines else ''
    return f'<div class="defi-card"><b>{_ICO_TROPHY} تحدّي ماجور:</b> {txt}{ls}</div>'


def bulle(mascot_key, txt):
    return f'''<div class="bulle-row">
      <span class="im im-{mascot_key}" role="img" aria-label=""></span>
      <div class="bulle">{txt}</div>
    </div>'''


def self_eval():
    return '''<div class="self-eval">
      <span class="im im-fille" role="img" aria-label=""></span>
      <span class="se-txt">أحسنت! أنهيتَ هذه الوحدة.<br>لوّن الدوائر حسب أدائك:</span>
      <span class="se-stars">○ ○ ○ ○ ○</span>
    </div>'''


def unit_banner(num, title, sub, color=''):
    return f'''<div class="unit-banner">
      <span class="ub-num">{num}</span>
      <span><b>{title}</b><small>{sub}</small></span>
    </div>'''


def ai_table(headers, rows, header_bg='', header_color=''):
    """Tableau style original (en-tête bleu nuit, zébrage) : headers = liste,
    rows = liste de listes. Une cellule '…' devient une ligne à compléter."""
    st = f' style="background:{header_bg};color:{header_color};border-color:{header_bg}"' if header_bg else ''
    th = ''.join(f'<th{st}>{h}</th>' for h in headers)
    trs = ''
    for r in rows:
        tds = ''
        for c in r:
            if c == '…':
                tds += '<td class="fill"><div class="dotl"></div></td>'
            else:
                tds += f'<td>{c}</td>'
        trs += f'<tr>{tds}</tr>'
    return f'<table class="ai-table"><tr>{th}</tr>{trs}</table>'


def ayah(txt, source):
    """Verset coranique ou hadith avec sa référence."""
    return f'<div class="ayah">{txt}<small>{source}</small></div>'


# ─────────────────────────── gabarit de page ───────────────────────────
def spine():
    holes = '<div class="holes">' + '<div class="hole"></div>' * 6 + '</div>'
    return f'''<div class="spine">
      {holes}
      <div class="spine-title">دفتر ماجور · MAJOR · 6AF</div>
      {holes}
    </div>'''


def tabs(part):
    a = ' tab-active' if part == 'ar' else ''
    i = ' tab-active' if part == 'isl' else ''
    return (f'<div class="tabs">'
            f'<div class="tab{a}" style="background:var(--ar)">اللغة العربية</div>'
            f'<div class="tab{i}" style="background:var(--is)">التربية الإسلامية</div>'
            f'</div>')


def page(num, title, body, unit_label='', with_eval=False, part=''):
    ev = self_eval() if with_eval else ''
    part_cls = f' part-{part}' if part else ''
    tag = f'<span class="subject-tag">{unit_label}</span>' if unit_label else ''
    foot_r = 'دفتر ماجور · اللغة العربية والتربية الإسلامية'
    foot_l = 'السنة السادسة الأساسية 6AF'
    # QR hors du flux de .page-body (absolu coin bas-gauche)
    qr = ''
    m = re.search(r'(<div class="qr-corr"[^>]*>.*?</div>)', body, flags=re.S)
    if m:
        qr = m.group(1)
        body = body[:m.start()] + body[m.end():]
    body = print_sanitize(body)
    title = print_sanitize(title)
    unit_label = print_sanitize(unit_label)
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
  {tabs(part)}
</div>'''
