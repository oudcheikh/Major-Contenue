# -*- coding: utf-8 -*-
"""Base du générateur : CSS + gabarits de page (style pptx Major + méthode Singapour)."""
import json

ASSETS = json.load(open('assets.json'))

CSS = """
:root{
  --cream:#fbf6ea;
  --frame:#fffdf6;
  --ink:#26303c;
  --muted:#6b7280;
  --orange:#e08b2d;
  --orange-deep:#c9711a;
  --yellow:#fcd77f;
  --yellow-text:#8a4a12;
  --red:#e2504c;
  --blue:#2f6ea5;
  --p-blue:#cfe3e6;
  --p-green:#dcead3;
  --p-rose:#f6d9d0;
  --p-yell:#f8e3c8;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  font-family:'Cairo','Tahoma','Arial',sans-serif;
  background:linear-gradient(180deg,#e9e0cf 0%,#e0d4bd 100%);
  color:var(--ink);font-size:14px;direction:rtl;
}
/* ═══ PAGE ═══ */
.sheet{
  width:210mm;min-height:297mm;margin:18px auto;background:var(--cream);
  position:relative;overflow:hidden;border-radius:14px;
  box-shadow:0 18px 42px rgba(15,23,42,.18);
  display:flex;flex-direction:column;
}
.sheet-inner{flex:1;padding:8mm 9mm 26mm;display:flex;flex-direction:column}
/* header */
.head{display:flex;flex-direction:row-reverse;justify-content:space-between;align-items:flex-start;margin-bottom:2mm}
.head img.logo{width:15mm;height:15mm;object-fit:contain;border-radius:3mm}
.head .doc-id{font-size:9px;color:var(--muted);font-weight:700;text-align:right}
.lesson-title{
  text-align:center;color:var(--orange);font-weight:900;font-size:23px;
  font-family:'Cairo',sans-serif;margin:0 0 4mm;line-height:1.2;text-wrap:balance;
}
/* vague bleue bas de page */
.wave{position:absolute;left:0;right:0;bottom:0;height:20mm;pointer-events:none}
.wave svg{position:absolute;inset:0;width:100%;height:100%}
.pageno{
  position:absolute;left:50%;transform:translateX(-50%);bottom:4mm;
  font-size:17px;font-weight:900;color:#fff;z-index:2;
  font-variant-numeric:tabular-nums;font-family:'Cairo',sans-serif;
}
/* ═══ BADGES DE SECTION (carton jaune + mascotte) ═══ */
.badge-row{display:flex;flex-direction:row-reverse;align-items:flex-end;gap:4mm;margin:4mm 0 2.5mm}
.badge-row img.mascot{width:17mm;height:auto}
.badge{
  background:linear-gradient(180deg,#fde28f,#fbcf6b);
  color:var(--yellow-text);font-weight:900;font-size:14px;
  padding:6px 26px;border-radius:999px;font-family:'Cairo',sans-serif;
  box-shadow:0 3px 8px rgba(138,74,18,.18);
}
.badge small{display:block;font-size:9px;font-weight:700;color:#a3662b}
/* ═══ CADRE BLANC (carton de contenu) ═══ */
.frame{
  background:var(--frame);border:1.5px solid #e7dfcc;border-radius:14px;
  padding:5mm 6mm;position:relative;
  box-shadow:0 4px 12px rgba(120,100,60,.07);
}
.frame ul{margin:0;padding-right:5mm;padding-left:0;line-height:1.9;font-size:12.5px;font-weight:600}
.frame ul li::marker{color:var(--orange)}
.frame .hl{color:#c0392b;font-weight:900}
/* nuage vidéo + QR */
.video-box{
  position:absolute;left:5mm;bottom:4mm;width:34mm;text-align:center;direction:ltr;
}
.video-box .nuage{position:relative;width:100%}
.video-box .nuage img{width:100%;display:block}
.video-box .nuage span{
  position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  font-size:9.5px;font-weight:900;color:#b3541e;transform:rotate(-6deg);font-family:'Cairo',sans-serif;
}
.video-box img.qr{width:17mm;height:17mm;margin-top:1mm;image-rendering:pixelated}
.frame.has-video{padding-left:42mm;min-height:34mm}
/* ═══ SINGAPOUR : bandeau CPA ═══ */
.cpa{
  display:flex;flex-direction:row-reverse;gap:2mm;align-items:center;
  font-size:8.5px;font-weight:900;color:#8a4a12;margin:1.5mm 0 0;
}
.cpa span{background:#fdf1d7;border:1px dashed #e0b25f;border-radius:999px;padding:2px 9px}
.cpa b{color:#c9711a}
/* ═══ MODÈLE EN BARRES (نموذج الشريط) ═══ */
.barmodel{direction:ltr;margin:2.5mm auto;max-width:120mm}
.bm-row{display:flex;height:9mm}
.bm-seg{
  border:1.7px solid #33475e;display:flex;align-items:center;justify-content:center;
  font-weight:900;font-size:12px;font-variant-numeric:tabular-nums;background:#fff;
}
.bm-seg+.bm-seg{border-left:none}
.bm-seg.c1{background:#bcd9f5}
.bm-seg.c2{background:#f7c8c5}
.bm-seg.c3{background:#cde8cd}
.bm-seg.c4{background:#fbe3ad}
.bm-seg.empty{background:repeating-linear-gradient(45deg,#fff,#fff 5px,#f2ecdd 5px,#f2ecdd 9px)}
.bm-brace{
  display:flex;justify-content:center;font-size:10.5px;font-weight:800;color:#33475e;
  border-left:1.6px solid #33475e;border-right:1.6px solid #33475e;
  border-bottom:1.6px solid #33475e;height:3mm;margin-top:1mm;position:relative;
}
.bm-brace span{position:absolute;top:2.6mm;background:transparent;padding:0 6px}
.bm-lab{display:flex;font-size:10px;font-weight:800;color:#4b5b70}
.bm-lab div{display:flex;align-items:flex-start;justify-content:center;padding-top:.6mm}
/* ═══ LIEN NUMÉRIQUE (رابط العدد) ═══ */
.numbond{display:flex;justify-content:center;margin:2mm 0}
.numbond svg text{font-family:'Cairo',sans-serif;font-weight:900}
/* ═══ DISQUES DE VALEUR (أقراص المراتب) ═══ */
.pv-disc{
  display:inline-flex;align-items:center;justify-content:center;
  width:9.5mm;height:9.5mm;border-radius:50%;font-size:9px;font-weight:900;color:#fff;
  margin:.4mm;font-variant-numeric:tabular-nums;box-shadow:inset 0 -2px 0 rgba(0,0,0,.18);
}
.pv-1{background:#e2a23c}.pv-10{background:#5f9e62}.pv-100{background:#c65b53}
.pv-1000{background:#4a7fb5}.pv-p10{background:#9b7fc0}.pv-p100{background:#5aa7a0}
/* ═══ TABLEAU DES FAMILLES (pastel pptx) ═══ */
.fam-table{width:100%;border-collapse:collapse;direction:rtl;font-variant-numeric:tabular-nums;margin:2mm 0}
.fam-table th{font-size:10.5px;font-weight:900;padding:2.2mm 1mm;border:1.4px solid #c9bfa8}
.fam-table td{border:1.4px solid #c9bfa8;padding:1.6mm;text-align:center}
.fam-u  th{background:var(--p-yell);color:#7c4a12}
.fam-k  th{background:var(--p-rose);color:#8a3d2a}
.fam-m  th{background:var(--p-green);color:#33591f}
.fam-g  th{background:var(--p-blue);color:#1f5566}
.mini-cells{display:flex;flex-direction:row-reverse;justify-content:center;gap:1mm}
.mini-cell{
  width:7mm;height:7mm;border:1.7px solid #d78d33;border-radius:2px;background:#fff;
  display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:900;
}
.mini-cell.g{border-color:#2e5e4e}
.mini-lab{font-size:8px;color:#8a7a5c;font-weight:800}
.pink-strip{
  background:#f6dee4;border:1.4px solid #d9a9b6;border-radius:2mm;height:7mm;
  display:flex;align-items:center;justify-content:center;font-weight:900;font-size:11px;
}
/* ═══ EXERCICES (jetons rouges + colonnes pptx) ═══ */
.cols{display:grid;grid-template-columns:1fr 1fr;gap:4mm 8mm;position:relative;margin-top:2mm}
.cols:before{content:"";position:absolute;top:1mm;bottom:1mm;left:50%;width:1.8px;background:#2b2b2b;opacity:.75}
.exo{padding:1mm 0 2mm;break-inside:avoid}
.exo-head{display:flex;flex-direction:row-reverse;align-items:center;gap:2.5mm;margin-bottom:1.5mm}
.tok{
  position:relative;width:8.2mm;height:8.2mm;background:var(--red);border-radius:50%;
  display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;
  color:#fff;font-weight:900;font-size:13px;
  box-shadow:0 2px 4px rgba(197,48,48,.35);
}
.tok:after{
  content:"";position:absolute;left:-2.6mm;top:50%;transform:translateY(-50%);
  border:2.2mm solid transparent;border-right:3.2mm solid var(--red);border-left:none;
}
.tok i{
  position:absolute;inset:1.2mm;border-radius:50%;background:#fdeee0;font-style:normal;
  display:flex;align-items:center;justify-content:center;color:#c0392b;
}
.lvl{font-size:8.5px;font-weight:900;color:#7a6a45;background:#fdf1d7;border-radius:999px;padding:2px 8px}
.exo-q{font-size:12px;font-weight:700;line-height:1.75}
/* cartons de réponse */
.oval{
  display:inline-block;min-width:26mm;height:7mm;vertical-align:middle;
  border:1.7px solid #2b2b2b;border-radius:999px;background:#fff;margin:.6mm 1mm;
}
.oval.s{min-width:14mm}.oval.l{min-width:44mm}
.dashcard{
  border:1.9px dashed var(--red);border-radius:4mm;background:#fff;
  min-height:12mm;margin-top:1.6mm;position:relative;
}
.dashcard.tall{min-height:20mm}
.dotl{border-bottom:2px dotted #a8b0bd;height:6.5mm}
.dots{margin-top:1mm}
/* fractions : camemberts + bandes */
.pies{display:flex;flex-direction:row-reverse;flex-wrap:wrap;gap:3mm;align-items:center;justify-content:center;margin:2mm 0}
.pie{width:17mm;height:17mm;border-radius:50%;border:2px solid #2b2b2b;position:relative}
.pie-lab{text-align:center;font-weight:900;font-size:11px;margin-top:1mm}
.fstrip{display:flex;height:7mm;border:1.8px solid #2b2b2b;border-radius:2mm;overflow:hidden;direction:ltr;margin:1.6mm 0}
.fcell{flex:1;border-left:1.8px solid #2b2b2b}
.fcell:first-child{border-left:none}
.fill-b{background:#8fd4e8}.fill-o{background:#f5b34c}.fill-v{background:#b79ddb}.fill-g{background:#a9d3a0}
/* grille de 100 (pourcentage) */
.grid100{
  width:34mm;height:34mm;border:2px solid #2b2b2b;direction:ltr;position:relative;margin:0 auto;
  background:
    repeating-linear-gradient(0deg,transparent 0,transparent calc(10% - .5px),#8a8a8a calc(10% - .5px),#8a8a8a 10%),
    repeating-linear-gradient(90deg,transparent 0,transparent calc(10% - .5px),#8a8a8a calc(10% - .5px),#8a8a8a 10%),#fff;
}
.grid100 .gfill{position:absolute;left:0;top:0;bottom:0;background:rgba(143,212,232,.75)}
/* opérations verticales */
.vop{
  direction:ltr;display:inline-block;background:#fff;border:1.5px solid #ddd2b8;
  border-radius:3mm;padding:2mm 5mm;font-size:14px;font-weight:800;text-align:right;
  line-height:1.55;font-variant-numeric:tabular-nums;
}
.vop .vline{display:block;border-top:2.2px solid #33475e;margin-top:1mm;padding-top:1mm}
/* fraction empilée */
.mfrac{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;margin:0 1.2mm;font-weight:900;line-height:1.12;font-variant-numeric:tabular-nums}
.mfrac span:first-child{border-bottom:1.9px solid currentColor;padding:0 1.6mm}
.mfrac span:last-child{padding:0 1.6mm}
.mexp{direction:ltr;unicode-bidi:isolate;font-weight:800;font-variant-numeric:tabular-nums}
/* bulle crantée (lecture) */
.scallop{
  background:#fff;border:2px dotted #d98a95;border-radius:5mm;padding:3mm 5mm;
  font-size:11.5px;font-weight:700;line-height:1.7;position:relative;margin:2mm 0;
}
.scallop:before,.scallop:after{
  content:"";position:absolute;top:-2mm;width:4mm;height:4mm;border-radius:50%;
  background:#e8a9b4;border:1.4px solid #c37a88;
}
.scallop:before{right:6mm}.scallop:after{left:6mm}
/* étiquette guidée أتدرّب */
.step{display:flex;flex-direction:row-reverse;gap:2.5mm;align-items:flex-start;margin-bottom:1.6mm;font-size:11.5px;font-weight:700;line-height:1.6}
.step b.n{
  background:var(--blue);color:#fff;border-radius:50%;width:5.5mm;height:5.5mm;flex-shrink:0;
  display:inline-flex;align-items:center;justify-content:center;font-size:9.5px;margin-top:.5mm;
}
/* auto-évaluation */
.self-eval{
  display:flex;flex-direction:row-reverse;align-items:center;justify-content:space-between;gap:4mm;
  margin-top:auto;padding:2mm 5mm;border-radius:3mm;background:#fffdf6;
  border:1.6px dashed #cdbf9d;font-size:10px;font-weight:800;color:#5c5238;position:relative;z-index:2;
}
.se-item{display:flex;flex-direction:row-reverse;align-items:center;gap:2mm}
.se-box{width:4.5mm;height:4.5mm;border:1.8px solid #8a7a5c;border-radius:1mm;background:#fff}
/* couverture */
.cover .sheet-inner{justify-content:center;align-items:center;text-align:center}
.cover-logo{width:34mm;height:34mm;object-fit:contain;border-radius:6mm;box-shadow:0 8px 22px rgba(120,90,40,.25)}
.cover h1{font-size:52px;color:var(--orange);font-weight:900;margin:6mm 0 2mm;font-family:'Cairo',sans-serif}
.cover .sub{font-size:16px;font-weight:700;color:#6b5d3f;margin:0 0 8mm}
.cover-cards{display:grid;grid-template-columns:1fr 1fr;gap:4mm;width:150mm;margin:4mm 0 6mm}
.cover-card{border-radius:5mm;padding:5mm;text-align:right;border:1.6px solid rgba(0,0,0,.08)}
.cover-card b{font-size:14px;display:block;margin-bottom:1mm}
.cover-card span{font-size:10.5px;line-height:1.6;color:#4b5563}
.cover-band{display:flex;flex-direction:row-reverse;gap:3mm;flex-wrap:wrap;justify-content:center;margin-bottom:5mm}
.cover-band span{background:#fff;border:1.6px solid #e0d3b3;border-radius:999px;padding:2mm 5mm;font-size:10.5px;font-weight:900;color:#7c4a12}
.cover-mascots{display:flex;gap:8mm;align-items:flex-end;justify-content:center;margin-top:2mm}
.cover-mascots img{width:26mm}
/* toolbar */
.toolbar{position:fixed;top:14px;left:18px;z-index:9999}
.action-btn{
  border:none;border-radius:999px;padding:10px 16px;font-family:'Cairo',sans-serif;
  font-size:13px;font-weight:800;cursor:pointer;background:var(--blue);color:#fff;
  box-shadow:0 10px 24px rgba(15,23,42,.16);
}
.action-btn:focus-visible{outline:3px solid #9cc3e8;outline-offset:2px}
/* ═══ PRINT ═══ */
@media print{
  @page{size:A4 portrait;margin:0}
  .toolbar{display:none!important}
  html,body{background:#fff!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .sheet{
    width:210mm!important;height:297mm!important;min-height:297mm!important;
    margin:0 auto!important;border-radius:0!important;box-shadow:none!important;
    break-after:page;page-break-after:always;overflow:hidden!important;
  }
  .sheet:last-of-type{break-after:auto!important}
  .sheet-inner{padding:4.5mm 8mm 16mm!important}
  .wave{height:13mm!important}
  .pageno{bottom:2.2mm!important;font-size:13px!important}
  .head{margin-bottom:1mm!important}
  .head .logo{width:11mm!important;height:11mm!important}
  .head .doc-id{font-size:7.5px!important}
  .lesson-title{font-size:16.5px!important;margin-bottom:1.8mm!important}
  .badge-row{margin:1.8mm 0 1.3mm!important;gap:3mm!important}
  .badge-row .mascot{width:11.5mm!important;height:10mm!important}
  .badge{font-size:11px!important;padding:3px 16px!important}
  .badge small{font-size:7.5px!important}
  .frame{padding:2.6mm 3.8mm!important}
  .frame ul{font-size:9.6px!important;line-height:1.58!important}
  .frame.has-video{padding-left:31mm!important;min-height:25mm!important}
  .video-box{width:26mm!important;bottom:2.5mm!important;left:3mm!important}
  .video-box .nuage-bg{height:10mm!important}
  .video-box .nuage-bg span{font-size:7.5px!important}
  .video-box .qr{width:13mm!important;height:13mm!important}
  .cpa{font-size:7.2px!important;margin:1mm 0 0!important}
  .cpa span{padding:1px 6px!important}
  .fam-table th{font-size:8.2px!important;padding:1.2mm .6mm!important}
  .fam-table td{padding:.9mm!important}
  .mini-cell{width:5.4mm!important;height:5.4mm!important;font-size:9px!important}
  .pink-strip{height:5.4mm!important;font-size:9px!important}
  .pv-disc{width:7mm!important;height:7mm!important;font-size:7px!important;margin:.25mm!important}
  .scallop{font-size:9px!important;padding:1.8mm 3.5mm!important;margin:1.5mm 0 0!important;line-height:1.5!important}
  .barmodel{margin:1.5mm auto!important}
  .bm-row{height:6.6mm!important}
  .bm-seg{font-size:9.5px!important}
  .bm-brace{font-size:8.5px!important}
  .numbond svg{width:118px!important;height:68px!important}
  .cols{gap:2.2mm 6mm!important;margin-top:1.5mm!important}
  .exo{padding:.6mm 0 1.2mm!important}
  .exo-head{margin-bottom:1mm!important;gap:2mm!important}
  .exo-q{font-size:9.3px!important;line-height:1.5!important}
  .tok{width:6.4mm!important;height:6.4mm!important;font-size:10px!important}
  .tok:after{left:-2mm!important;border-width:1.7mm!important;border-right-width:2.5mm!important}
  .lvl{font-size:7px!important;padding:1px 6px!important}
  .oval{min-width:19mm!important;height:5.4mm!important}
  .oval.s{min-width:11mm!important}.oval.l{min-width:32mm!important}
  .dashcard{min-height:8mm!important;margin-top:1.2mm!important}
  .dashcard.tall{min-height:13mm!important}
  .dotl{height:4.8mm!important}
  .grid100{width:25mm!important;height:25mm!important}
  .pie{width:12.5mm!important;height:12.5mm!important}
  .pie-lab{font-size:9px!important}
  .fstrip{height:5.2mm!important;margin:1.2mm 0!important}
  .step{font-size:9px!important}
  .self-eval{font-size:7.8px!important;padding:1.1mm 3mm!important;border-radius:2mm!important}
  .se-box{width:3.6mm!important;height:3.6mm!important}
  .vop{font-size:10.5px!important;padding:1.5mm 3.5mm!important}
  .cover h1{font-size:44px!important}
  .cover-cards{gap:3mm!important}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""

WAVE_SVG = """<svg viewBox="0 0 210 20" preserveAspectRatio="none" aria-hidden="true">
<path d="M0,20 L0,10 Q35,0 75,8 Q130,17 210,5 L210,20 Z" fill="#2f6ea5"/>
<path d="M0,20 L0,14 Q45,5 95,12 Q150,19 210,10 L210,20 Z" fill="#4d89bd" opacity=".85"/>
</svg>"""

# Images embarquées UNE seule fois (classes CSS) pour garder un fichier léger
CSS_ASSETS = f"""
.im{{display:inline-block;background-repeat:no-repeat;background-position:center;background-size:contain}}
.im-fille{{background-image:url("{ASSETS['fille']}")}}
.im-garcon{{background-image:url("{ASSETS['garcon']}")}}
.im-nuage{{background-image:url("{ASSETS['nuage']}")}}
.im-qr{{background-image:url("{ASSETS['qr']}");image-rendering:pixelated}}
.im-logo{{background-image:url("{ASSETS['logo']}")}}
.badge-row .mascot{{width:17mm;height:15mm}}
.head .logo{{width:15mm;height:15mm;border-radius:3mm}}
.video-box .nuage-bg{{width:100%;height:15mm;position:relative}}
.video-box .nuage-bg span{{
  position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  font-size:9.5px;font-weight:900;color:#b3541e;transform:rotate(-6deg);font-family:'Cairo',sans-serif;
}}
.video-box .qr{{width:17mm;height:17mm;margin-top:1mm}}
.cover-logo{{width:34mm;height:34mm;border-radius:6mm;box-shadow:0 8px 22px rgba(120,90,40,.25)}}
.cover-mascots .im{{width:26mm;height:22mm}}
"""


def badge_row(label, sub, mascot_key):
    return f'''<div class="badge-row">
      <span class="im im-{mascot_key} mascot" role="img" aria-label=""></span>
      <div class="badge">{label}<small>{sub}</small></div>
    </div>'''


def video_box():
    return f'''<div class="video-box">
      <div class="nuage-bg im im-nuage"><span>شاهد الفيديو</span></div>
      <span class="im im-qr qr" role="img" aria-label="QR فيديو الدرس"></span>
    </div>'''


def tok(n):
    return f'<span class="tok"><i>{n}</i></span>'


def exo(n, lvl, body):
    return f'''<div class="exo">
      <div class="exo-head">{tok(n)}<span class="lvl">{lvl}</span></div>
      <div class="exo-q">{body}</div>
    </div>'''


def dots(n):
    return '<div class="dots">' + '<div class="dotl"></div>' * n + '</div>'


def pie(frac_deg, n_parts, fill='#8fd4e8'):
    """Camembert : secteur rempli via conic-gradient + traits de découpe."""
    step = 360 / n_parts
    lines = f'repeating-conic-gradient(from 0deg, transparent 0deg, transparent {step - 2.2}deg, #2b2b2b {step - 2.2}deg, #2b2b2b {step}deg)'
    sector = f'conic-gradient({fill} 0deg {frac_deg}deg, rgba(0,0,0,0) {frac_deg}deg 360deg)'
    return f'<div class="pie" style="background:{lines},{sector},#fff"></div>'


def numbond(whole, p1, p2):
    return f'''<div class="numbond"><svg width="150" height="86" viewBox="0 0 150 86">
      <line x1="75" y1="24" x2="34" y2="62" stroke="#33475e" stroke-width="2.2"/>
      <line x1="75" y1="24" x2="116" y2="62" stroke="#33475e" stroke-width="2.2"/>
      <circle cx="75" cy="20" r="17" fill="#fbe3ad" stroke="#33475e" stroke-width="2.2"/>
      <circle cx="32" cy="66" r="16" fill="#fff" stroke="#33475e" stroke-width="2.2"/>
      <circle cx="118" cy="66" r="16" fill="#fff" stroke="#33475e" stroke-width="2.2"/>
      <text x="75" y="26" text-anchor="middle" font-size="14">{whole}</text>
      <text x="32" y="72" text-anchor="middle" font-size="14">{p1}</text>
      <text x="118" y="72" text-anchor="middle" font-size="14">{p2}</text>
    </svg></div>'''


def page(num, title, body, footer_note=''):
    return f'''<div class="sheet">
  <div class="sheet-inner">
    <div class="head">
      <div class="doc-id">دفتر ماجور · الرياضيات<br>السنة السادسة الأساسية 6AF</div>
      <span class="im im-logo logo" role="img" aria-label="Major"></span>
    </div>
    <h2 class="lesson-title">{title}</h2>
    {body}
    <div class="self-eval">
      <span>📊 قيّم نفسك:</span>
      <span class="se-item"><span class="se-box"></span> فهمتُ جيدًا 😀</span>
      <span class="se-item"><span class="se-box"></span> أحتاج مراجعة 🤔</span>
      <span class="se-item"><span class="se-box"></span> أحتاج مساعدة 🙋</span>
      <span style="font-size:8px;color:#8a7a5c">{footer_note}</span>
    </div>
  </div>
  <div class="wave">{WAVE_SVG}</div>
  <div class="pageno">{num}</div>
</div>'''
