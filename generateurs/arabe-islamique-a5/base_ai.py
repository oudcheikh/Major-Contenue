# -*- coding: utf-8 -*-
"""Socle du cahier A5 عربية/إسلامية — style « dfatir Major » repris du cahier A4
original (archives/Cahier-Major-LangueArabe-Islamique-6AF.SOURCE.html) :
dos relié bleu nuit + onglets de section, pages papier crème, cartes d'exercices
blanches à liseré coloré avec lignes d'écriture, tableaux à en-tête bleu nuit
avec cellules à remplir. Violet = اللغة العربية · vert = التربية الإسلامية.
Les composants gardent la même signature que le kit maths : les fichiers de
contenu (unites_ar_1..3.py, unites_isl.py) n'ont pas besoin de changer."""
import os
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

/* ── dos relié (bord droit) ── */
.spine{
  width:7mm;flex-shrink:0;position:relative;
  background:linear-gradient(180deg,#111827,#1f2937);
  display:flex;flex-direction:column;justify-content:space-between;align-items:center;
  padding:4mm 0;border-radius:0 5mm 5mm 0;
}
.spine:before{
  content:"";position:absolute;left:0;top:0;bottom:0;width:.8mm;
  background:linear-gradient(180deg,rgba(255,255,255,.18),rgba(255,255,255,0),rgba(255,255,255,.18));
}
.holes{display:flex;flex-direction:column;gap:3.2mm}
.hole{width:2mm;height:2mm;border-radius:50%;background:rgba(255,255,255,.13);border:.3mm solid rgba(255,255,255,.09)}
.spine-title{
  writing-mode:vertical-rl;transform:rotate(180deg);
  color:rgba(255,255,255,.4);font-size:5.4px;font-weight:800;letter-spacing:1.2px;
}
/* ── onglets de section (bord gauche) ── */
.tabs{width:4.6mm;flex-shrink:0;display:flex;flex-direction:column}
.tab{
  flex:1;color:#fff;font-size:5.6px;font-weight:900;letter-spacing:.8px;opacity:.32;
  display:flex;align-items:center;justify-content:center;writing-mode:vertical-rl;
}
.tab-active{flex:1.6;opacity:1}

/* ── colonne principale ── */
.page-main{flex:1;display:flex;flex-direction:column;min-width:0;position:relative}
.page-header{
  display:flex;justify-content:space-between;align-items:center;gap:2mm;
  padding:1.8mm 3.6mm;border-bottom:.35mm solid rgba(17,24,39,.08);flex-shrink:0;
}
.brand{display:flex;align-items:center;gap:1.6mm}
.brand .logo{width:6.5mm;height:6.5mm;border-radius:1.6mm}
.brand-title{font-size:8.5px;font-weight:900;line-height:1.1}
.brand-sub{font-size:5.6px;color:var(--muted);line-height:1.15}
.subject-tag{
  background:var(--part);color:#fff;padding:1mm 3.4mm;border-radius:999px;
  font-size:6.6px;font-weight:900;letter-spacing:.2px;max-width:72mm;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
}
.page-body{flex:1;overflow:hidden;padding:2.2mm 3.6mm 14.5mm;position:relative;min-width:0}
.page-footer{
  position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;
  align-items:flex-end;padding:0 3.6mm 1.4mm 20mm;font-size:5.6px;color:var(--muted);font-weight:700;
}
.bottom-number{
  position:absolute;left:50%;transform:translateX(-50%);bottom:1.2mm;
  min-width:6.5mm;height:6.5mm;border-radius:999px;background:#fff;
  border:.5mm solid var(--part);display:flex;align-items:center;justify-content:center;
  font-size:8.5px;font-weight:900;color:var(--ink);z-index:3;
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
  box-shadow:0 1px 3px rgba(15,23,42,.25);
}
.unit-banner b{font-size:11px;font-weight:900;display:block;line-height:1.25}
.unit-banner small{font-size:6.8px;font-weight:700;color:rgba(255,255,255,.92);display:block}

/* ── rangée de section (أتعلّم / تمارين …) ── */
.badge-row{display:flex;align-items:center;gap:1.8mm;margin:1.6mm 0 1.2mm}
.badge-row .num-badge{
  width:6mm;height:6mm;border-radius:50%;background:var(--part);color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:8px;flex-shrink:0;
  box-shadow:0 1px 2.5px rgba(15,23,42,.22);
}
.badge-row .bl{font-size:10.5px;font-weight:900;color:var(--ink)}
.badge-row .bs{
  font-size:6.4px;font-weight:800;color:var(--part);background:var(--part-soft);
  border:.35mm solid var(--part-border);border-radius:999px;padding:.5mm 2.6mm;
}
.badge-row .mascot{width:8.5mm;height:8mm;margin-inline-start:auto}

/* ── objectifs (في هذه الوحدة سأتعلّم) ── */
.objectifs{
  background:linear-gradient(135deg,rgba(124,58,237,.05),var(--part-soft));
  border:.5mm dashed var(--part-border);border-radius:3mm;
  padding:1.6mm 2.8mm;margin-bottom:1.6mm;
}
.part-isl .objectifs{background:linear-gradient(135deg,rgba(5,150,105,.05),var(--part-soft))}
.objectifs b{font-size:8px;font-weight:900;color:var(--part);display:block;margin-bottom:.5mm}
.objectifs ul{margin:0;padding:0;list-style:none}
.objectifs li{font-size:7.6px;font-weight:700;line-height:1.65;padding-right:5mm;position:relative}
.objectifs li:before{
  content:"";position:absolute;right:.6mm;top:1.1mm;width:2.6mm;height:2.6mm;
  border:.45mm solid var(--part);border-radius:.7mm;background:#fff;
}

/* ── cadre de leçon ── */
.frame{
  background:#fff;border:.4mm solid rgba(17,24,39,.1);border-radius:3.5mm;
  padding:2.2mm 3mm;margin:1.2mm 0;position:relative;
  box-shadow:0 1.5px 5px rgba(17,24,39,.05);
  border-top:1.2mm solid var(--part);
}
.frame ul{margin:.6mm 0 0;padding-right:4.5mm}
.frame li{font-size:8.2px;font-weight:700;line-height:1.7}
.frame.has-video{padding-left:23mm;min-height:25mm}
.video-box{
  position:absolute;left:2mm;top:2mm;width:19mm;text-align:center;
  background:#fff;border:.5mm dashed var(--part-border);border-radius:2.6mm;
  padding:1mm .8mm .8mm;
}
.video-box .vb-cap{font-size:5.2px;font-weight:900;color:var(--part);line-height:1.25;display:block;margin-top:.5mm}
.video-box .qr{width:15mm;height:15mm;border-radius:1.5mm}

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
  padding:1.6mm 2.8mm;margin:1.2mm 0;font-size:7.8px;line-height:1.6;font-weight:700;color:#713f12;
}
.tip-card b{color:#b45309;font-weight:900}
.warn-card{
  background:#fef2f2;border-right:1.4mm solid #dc2626;border-radius:3mm;
  padding:1.6mm 2.8mm;margin:1.2mm 0;font-size:7.8px;line-height:1.6;font-weight:700;color:#7f1d1d;
}
.warn-card b{color:#dc2626;font-weight:900}
.defi-card{
  background:linear-gradient(135deg,#fffbeb,#fef3c7);border:.55mm dashed #f59e0b;border-radius:3mm;
  padding:1.6mm 2.8mm;margin:1.2mm 0;font-size:7.8px;line-height:1.6;font-weight:800;color:#92400e;
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
  box-shadow:0 1.5px 5px rgba(17,24,39,.05);
}
.exo-top{display:flex;justify-content:space-between;align-items:center;gap:2mm;margin-bottom:.9mm}
.exo-num{display:flex;align-items:center;gap:1.4mm;font-size:8.4px;font-weight:900;color:var(--ink)}
.exo-num i{
  font-style:normal;width:4.8mm;height:4.8mm;border-radius:50%;background:var(--part);color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:7.5px;font-weight:900;flex-shrink:0;
}
.exo-level,.lvl{
  font-size:6.4px;font-weight:900;padding:.5mm 2.2mm;border-radius:999px;
  background:#fef3c7;color:#92400e;border:.3mm solid #fcd34d;letter-spacing:.3px;
}
.exo-text{font-size:8.2px;line-height:1.85;font-weight:700}
.consigne{font-size:8.4px;font-weight:900;margin:1mm 0 .6mm}

/* ── lignes d'écriture / cases à remplir ── */
.dots,.lines{margin-top:.9mm}
.dotl,.line,.wline{height:5.8mm;border-bottom:.5mm dashed #c9c2ea;margin-bottom:.3mm}
.part-isl .dotl,.part-isl .line,.part-isl .wline{border-bottom-color:#a8dcc8}
.oval{
  display:inline-block;min-width:28mm;height:6mm;vertical-align:-1.6mm;margin:.2mm 1mm;
  border-bottom:.55mm dashed var(--part-lite);
  background:linear-gradient(180deg,transparent 55%,var(--part-soft) 100%);
  border-radius:.8mm .8mm 0 0;
}
.oval.s{min-width:20mm;height:5.6mm}

/* ── tableaux ── */
.ai-table{width:100%;border-collapse:collapse;direction:rtl;margin:1.2mm 0}
.ai-table th{
  font-size:7.6px;font-weight:900;padding:1.2mm 1.6mm;text-align:center;
  background:var(--navy);color:#fff;border:.3mm solid var(--navy);
}
.ai-table th:first-child{border-radius:0 1.6mm 0 0}
.ai-table th:last-child{border-radius:1.6mm 0 0 0}
.ai-table td{
  border:.3mm solid #e2e8f0;padding:1mm 1.6mm;text-align:center;
  font-size:8px;font-weight:700;line-height:1.5;background:#fff;
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
  padding:1.4mm 2.6mm;font-size:7.6px;font-weight:800;line-height:1.6;color:#3b3557;
  position:relative;box-shadow:0 1px 4px rgba(17,24,39,.07);
}
.part-isl .bulle-row .bulle{color:#134e3a}
.bulle-row .bulle:before{
  content:"";position:absolute;right:-1.7mm;top:50%;transform:translateY(-50%) rotate(45deg);
  width:2.6mm;height:2.6mm;background:#fff;
  border-right:.5mm solid var(--part-border);border-top:.5mm solid var(--part-border);
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
.hl{background:rgba(253,230,138,.55);border-radius:1mm;padding:0 .5mm;font-weight:900}
.uw{text-decoration:underline;text-decoration-style:wavy;text-decoration-color:#c0392b;font-weight:900}
.unit-chip{display:none}
.scallop{
  background:var(--part-soft);border:.45mm dashed var(--part-border);border-radius:3mm;
  padding:1.6mm 2.8mm;font-size:7.4px;font-weight:800;line-height:1.7;color:#3b2b63;
}
.qr-corr{
  position:absolute;left:4mm;bottom:1mm;z-index:4;width:11.5mm;
  background:#fff;border:.4mm solid;border-radius:2mm;padding:.7mm .6mm .5mm;
  text-align:center;box-shadow:0 1px 3.5px rgba(15,23,42,.2);
}
.qr-corr img{width:9.8mm;height:9.8mm;display:block;margin:0 auto}
.qr-corr span{display:block;font-size:4.4px;font-weight:900;line-height:1.2;margin-top:.3mm}

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
    break-after:page;page-break-after:always;
  }
  .sheet:last-of-type{break-after:auto !important;page-break-after:auto !important}
}
"""


# ─────────────────────────── composants ───────────────────────────
OVAL = '<span class="oval"></span>'
OVS = '<span class="oval s"></span>'

_BADGE_ICONS = {'أتعلّم': '📖', 'تمارين': '✏️', 'أقرأ': '📖', 'أجيب': '✏️',
                'أقرأ وأجيب': '📖', 'أتحدّى': '🏆', 'أراجع': '🔄', 'أكتب': '✍️'}


def badge_row(label, sub, mascot_key):
    icon = _BADGE_ICONS.get(label, '⭐')
    return f'''<div class="badge-row">
      <span class="num-badge">{icon}</span>
      <span class="bl">{label}</span>
      <span class="bs">{sub}</span>
      <span class="im im-{mascot_key} mascot" role="img" aria-label=""></span>
    </div>'''


def video_box():
    return '''<div class="video-box">
      <span class="im im-qr qr" role="img" aria-label="QR فيديو الدرس"></span>
      <span class="vb-cap">📱 امسح وشاهد<br>فيديو الدرس</span>
    </div>'''


def tok(n):
    return f'<span class="exo-num"><i>{n}</i></span>'


def exo(n, lvl, body):
    lv = f'<span class="exo-level">{lvl}</span>' if lvl else ''
    return f'''<div class="exo-card">
      <div class="exo-top"><span class="exo-num"><i>{n}</i> التمرين {n}</span>{lv}</div>
      <div class="exo-text">{body}</div>
    </div>'''


def consigne(*args):
    """consigne(txt) ou consigne(n, txt) — même API que le kit maths."""
    if len(args) == 2:
        n, txt = args
        return f'<div class="consigne"><span class="exo-num"><i>{n}</i></span> {txt}</div>'
    return f'<div class="consigne">✏️ {args[0]}</div>'


def dots(n):
    return '<div class="lines">' + '<div class="line"></div>' * n + '</div>'


def wlines(n):
    return dots(n)


def objectifs(items):
    lis = ''.join(f'<li>{i}</li>' for i in items)
    return f'<div class="objectifs"><b>🎯 في هذه الوحدة سأتعلّم:</b><ul>{lis}</ul></div>'


def methode(title, steps):
    lis = ''.join(f'<li>{s}</li>' for s in steps)
    return f'<div class="rule-box"><b class="rb-title">🧭 {title}</b><ol>{lis}</ol></div>'


def astuce(txt):
    return f'<div class="tip-card"><b>💡 أستاذ ماجور ينصح:</b> {txt}</div>'


def attention(txt):
    return f'<div class="warn-card"><b>⚠️ انتبه!</b> {txt}</div>'


def defi(txt, lines=2):
    """Défi avec lignes d'écriture intégrées (c'est un cahier : l'élève répond dedans)."""
    ls = '<div class="lines">' + '<div class="line" style="height:5.2mm"></div>' * lines + '</div>' if lines else ''
    return f'<div class="defi-card"><b>🏆 تحدّي ماجور:</b> {txt}{ls}</div>'


def bulle(mascot_key, txt):
    return f'''<div class="bulle-row">
      <span class="im im-{mascot_key}" role="img" aria-label=""></span>
      <div class="bulle">{txt}</div>
    </div>'''


def self_eval():
    return '''<div class="self-eval">
      <span class="im im-fille" role="img" aria-label=""></span>
      <span class="se-txt">أحسنت! أنهيتَ هذه الوحدة 🎉<br>لوّن النجوم حسب أدائك:</span>
      <span class="se-stars">☆ ☆ ☆ ☆ ☆</span>
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
  {tabs(part)}
</div>'''
