# -*- coding: utf-8 -*-
"""Base du cahier A5 : CSS + gabarits + composants (style pptx Major, format A5 148×210)."""
import json, math, os, re

_HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = json.load(open(os.path.join(_HERE, '..', 'math-html', 'assets.json')))

# ─── palette vive des unités (couleurs joyeuses, lisibles à l'impression) ───
UNIT_COLORS = ['#ffd98c', '#ffc7ba', '#c6e9a4', '#aae4f0', '#e6c7f2']

CSS = """
:root{
  --cream:#fffaef; --frame:#fffdf6; --ink:#26303c; --muted:#6b7280;
  --orange:#f28a15; --orange-deep:#d97706;
  --yellow:#ffd35c; --yellow-text:#8a4a12;
  --red:#ef4b45; --blue:#1d7fc4;
  --p-blue:#aae4f0; --p-green:#c6e9a4; --p-rose:#ffc7ba; --p-yell:#ffd98c; --p-lila:#e6c7f2;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  font-family:'Lateef','Cairo','Tahoma','Arial',sans-serif;
  background:var(--cream);
  color:var(--ink);font-size:13.5px;direction:rtl;
}
/* ═══ FEUILLE A5 ═══ */
.sheet{
  width:148mm;height:210mm;margin:16px auto;background:var(--cream);
  position:relative;overflow:hidden;border-radius:10px;
  box-shadow:none;
  display:flex;flex-direction:column;
}
.sheet-inner{flex:1;padding:5mm 5.5mm 18mm;display:flex;flex-direction:column;min-height:0}
.sheet-inner>*{flex-shrink:0}
/* Zone réservée QR : padding bas réduit + spacer .qr-reserve incompressible */
.sheet:has(.qr-corr) .sheet-inner{padding-bottom:12mm}
.qr-reserve{
  height:26mm;width:100%;flex:0 0 26mm;margin-top:auto;
  pointer-events:none;visibility:hidden;padding:0;border:0;
}
.sheet:has(.qr-corr) .self-eval{margin-inline-end:24mm;margin-bottom:.15mm;padding-left:2.2mm}
/* entête */
.head{display:flex;justify-content:flex-start;align-items:center;gap:2mm;margin-bottom:.8mm}
.head .brand{display:flex;align-items:center;gap:2mm;min-width:0}
.head .brand-text{display:flex;flex-direction:column;justify-content:center;gap:.2mm;line-height:1.1}
.head .brand-title{font-size:9px;font-weight:900;color:var(--ink);line-height:1.1;margin:0}
.head .brand-sub{font-size:7px;color:var(--muted);font-weight:700;line-height:1.2;margin:0}
.head .doc-id{font-size:7px;color:var(--muted);font-weight:700;text-align:right;line-height:1.45}
.head img.logo{width:8mm;height:8mm;border-radius:1.8mm;object-fit:contain;flex-shrink:0;display:block}
.lesson-title{
  text-align:center;color:var(--orange);font-weight:900;font-size:13.8px;
  margin:0 0 1.2mm;line-height:1.22;text-wrap:balance;
}
.unit-chip{
  display:inline-block;font-size:7.5px;font-weight:900;color:#6b5327;
  background:#fdf1d7;border:1px solid #e6cc93;border-radius:999px;padding:1px 7px;margin-bottom:.5mm;
}
/* bande de tranche — inset ≥1.5mm du trim, teintes allégées */
.edge{position:absolute;left:1.6mm;top:4mm;bottom:4mm;width:3mm;z-index:3;border-radius:0 1.2mm 1.2mm 0}
.edge-math{background:linear-gradient(180deg,#fb923c 0%,#fbbf24 100%)}
.edge-sci{background:linear-gradient(180deg,#34d399 0%,#6ee7b7 100%)}
.edge span{
  position:absolute;top:50%;left:50%;transform:translate(-50%, -50%);
  writing-mode:vertical-rl;font-size:7px;font-weight:900;color:#fff;letter-spacing:1px;
  max-height:70%;
}
/* carte QR correction — ≥15mm scannable, safe du trim */
.qr-corr{
  position:absolute;left:5mm;bottom:3mm;z-index:6;width:18.5mm;
  background:#fff;border:.45mm solid;border-radius:2mm;padding:1mm .7mm .55mm;
  text-align:center;box-shadow:none;overflow:hidden;box-sizing:border-box;
}
.qr-corr img{width:15mm;height:15mm;display:block;margin:0 auto}
.qr-corr span{display:block;font-size:7px;font-weight:900;line-height:1.2;margin-top:.45mm}
/* vague bleue */
.wave{position:absolute;left:0;right:0;bottom:0;height:10mm;pointer-events:none}
.wave svg{position:absolute;inset:0;width:100%;height:100%}
/* numéro de page */
.pageno{
  position:absolute;left:50%;transform:translateX(-50%);bottom:2.8mm;
  min-width:7mm;height:7mm;border-radius:999px;background:#fff;
  border:.5mm solid #f28a15;display:flex;align-items:center;justify-content:center;
  font-size:8.5px;font-weight:900;color:#26303c;z-index:5;
  font-variant-numeric:tabular-nums;padding:0 1mm;
}
.pageno.sci{border-color:#1e9e57}
.page-footer{
  position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;
  align-items:flex-end;padding:0 5mm 3.2mm 28mm;font-size:7px;color:var(--muted);font-weight:700;
}
.sheet:has(.qr-corr) .page-footer{padding-left:28mm}
/* ═══ BADGES (carton jaune + mascotte) ═══ */
.badge-row{display:flex;align-items:flex-end;gap:2.2mm;margin:1.2mm 0 1mm;background:transparent!important;box-shadow:none!important}
.badge{
  background:linear-gradient(180deg,#ffe27a,#ffc84d);
  color:var(--yellow-text);font-weight:900;font-size:10.5px;
  padding:1mm 4.5mm;border-radius:3.2mm;max-width:78mm;
  box-shadow:none;
}
.badge small{display:block;font-size:7px;font-weight:700;color:#a3662b}
.badge-row .mascot{width:10.5mm;height:9.6mm;background-color:transparent!important;box-shadow:none!important;filter:none!important}
/* ═══ CADRE BLANC ═══ */
.frame{
  background:var(--frame);border:1.2px solid #e7dfcc;border-radius:3mm;
  padding:1.8mm 2.6mm;position:relative;
  box-shadow:none;
}
.frame ul{margin:0;padding-right:3.4mm;padding-left:0;line-height:1.55;font-size:11.6px;font-weight:600}
.frame ul li::marker{color:var(--orange)}
.frame .hl{color:#c0392b;font-weight:900}
.frame.has-video{padding-left:32mm;min-height:26mm;overflow:visible}
.video-box{position:absolute;left:2.2mm;bottom:2mm;width:26mm;text-align:center;direction:ltr}
.video-box .nuage-bg{width:100%;height:8.8mm;position:relative}
.video-box .nuage-bg span{
  position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  font-size:7px;font-weight:900;color:#b3541e;transform:rotate(-6deg);
}
.video-box .qr{width:15.5mm;height:15.5mm;margin-top:.6mm}
/* bulle crantée */
.scallop{
  background:#fff;border:1.8px dotted #d98a95;border-radius:3.2mm;padding:1.4mm 2.8mm;
  font-size:11px;font-weight:700;line-height:1.55;position:relative;margin:1.1mm 0 0;
}
.scallop:before,.scallop:after{
  content:"";position:absolute;top:-1.5mm;width:3mm;height:3mm;border-radius:50%;
  background:#e8a9b4;border:1px solid #c37a88;
}
.scallop:before{right:5mm}.scallop:after{left:5mm}
/* exemple encadré vert */
.exemple{
  background:#f2f8ee;border:1.4px dashed #8fb87a;border-radius:2.8mm;
  padding:1.4mm 2.6mm;font-size:11.2px;font-weight:700;line-height:1.55;margin:1.1mm 0 0;
}
.exemple b.tag{color:#33591f}
/* ═══ EXERCICES : jetons rouges (anneau circulaire — pas de fond carré à l'impression) ═══ */
.exo{padding:.35mm 0 .75mm;break-inside:avoid}
.exo-head{display:flex;align-items:center;gap:1.8mm;margin-bottom:.55mm}
.tok{
  position:relative;width:6.2mm;height:6.2mm;background:transparent;border-radius:50%;
  display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;
  box-shadow:none;overflow:visible;
}
.tok:after{
  content:"";position:absolute;left:-1.9mm;top:50%;transform:translateY(-50%);
  border:1.6mm solid transparent;border-right:2.4mm solid var(--red);border-left:none;
  z-index:0;
}
.tok i{
  position:absolute;inset:0;border-radius:50%;box-sizing:border-box;
  background:#fdeee0;border:1.5mm solid var(--red);font-style:normal;
  display:flex;align-items:center;justify-content:center;color:#c0392b;
  font-weight:900;font-size:9.5px;z-index:1;
}
.lvl{font-size:7px;font-weight:900;color:#7a6a45;background:#fdf1d7;border-radius:999px;padding:1px 6px}
.exo-q{font-size:11.7px;font-weight:700;line-height:1.55}
.consigne{
  display:flex;align-items:center;gap:2mm;
  font-size:11.6px;font-weight:900;color:#8a4a12;margin:1.1mm 0 .7mm;
}
.consigne .tok{width:5.6mm;height:5.6mm}
.consigne .tok i{font-size:8.5px;border-width:1.35mm}
/* cartons de réponse */
.oval{
  display:inline-block;min-width:26mm;height:6.8mm;vertical-align:middle;
  border:1.4px solid #2b2b2b;border-radius:999px;background:#fff;margin:.5mm .8mm;
}
.oval.s{min-width:12mm;height:6mm}.oval.l{min-width:42mm}
.sq{
  display:inline-flex;align-items:center;justify-content:center;width:6.4mm;height:6.4mm;
  border:1.5px solid #d78d33;border-radius:1.2mm;background:#fff;vertical-align:middle;
  margin:0 .6mm;font-weight:900;font-size:10px;
}
.dashcard{
  border:1.6px dashed var(--red);border-radius:2.6mm;background:#fff;
  min-height:9mm;margin-top:.7mm;position:relative;
}
.dashcard.tall{min-height:15mm}
.dotl{border-bottom:1.8px dotted #a8b0bd;height:6.1mm}
.dots{margin-top:.4mm}
/* colonnes d'exercices (séparateur pptx) */
.cols{display:grid;grid-template-columns:1fr 1fr;gap:2.4mm 5mm;position:relative;margin-top:1.4mm}
.cols:before{content:"";position:absolute;top:1mm;bottom:1mm;left:50%;width:1.4px;background:#2b2b2b;opacity:.65}
.cols.nosep:before{display:none}
/* ═══ opérations posées ═══ */
.vgrid{display:grid;gap:1.3mm;margin-top:1.2mm;width:100%}
.vop{
  direction:ltr;background:#fff;border:1.3px solid #ddd2b8;border-radius:2.4mm;
  padding:1.2mm 2.4mm 3.8mm;font-size:11px;font-weight:800;text-align:right;
  line-height:1.45;font-variant-numeric:tabular-nums;
}
.vop .vline{display:block;border-top:1.8px solid #33475e;margin-top:.55mm;height:4.4mm}
.vop .sign{float:left;color:#c0392b}
.mexp,.vop,.fam-table,.conv-table,.fx,.cellbox,.sq,.tok,.prop-table{font-family:'Cairo','Arial',sans-serif}
/* ═══ tableau des familles آ ع م ═══ */
.fam-table{border-collapse:collapse;direction:rtl;font-variant-numeric:tabular-nums;margin:0 auto}
.fam-table th{font-size:7.6px;font-weight:900;padding:1mm .6mm;border:1.1px solid #c9bfa8;text-align:center}
.fam-table td{border:1.1px solid #c9bfa8;padding:.8mm;text-align:center}
.fam-table .sub th{font-size:7px;padding:.5mm;background:#fffdf6!important;color:#8a7a5c}
.fam-u th{background:var(--p-yell);color:#7c4a12}
.fam-k th{background:var(--p-rose);color:#8a3d2a}
.fam-m th{background:var(--p-green);color:#33591f}
.fam-g th{background:var(--p-blue);color:#1f5566}
.cellbox{width:6mm;height:6mm;border:1.3px solid #d78d33;border-radius:1mm;background:#fff;display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:9.5px}
.pink-strip{
  background:#f6dee4;border:1.1px solid #d9a9b6;border-radius:1.6mm;height:5.2mm;
  display:flex;align-items:center;justify-content:center;font-weight:900;font-size:8.5px;
}
/* ═══ fractions ═══ */
.mfrac{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;margin:0 1mm;font-weight:900;line-height:1.1;font-variant-numeric:tabular-nums}
.mfrac span:first-child{border-bottom:1.5px solid currentColor;padding:0 1.3mm}
.mfrac span:last-child{padding:0 1.3mm}
.mexp{direction:ltr;unicode-bidi:isolate;font-weight:800;font-variant-numeric:tabular-nums;white-space:nowrap;margin-inline:.5mm}
.pies{display:flex;flex-wrap:wrap;gap:2.4mm;align-items:flex-start;justify-content:center;margin:1.4mm 0}
.pie{width:13mm;height:13mm;display:block;margin:0 auto}
.pie-lab{text-align:center;font-weight:900;font-size:11px;margin-top:.7mm}
.fstrip{display:flex;height:5.6mm;border:1.5px solid #2b2b2b;border-radius:1.6mm;overflow:hidden;direction:ltr;margin:1.2mm 0}
.fcell{flex:1;border-left:1.5px solid #2b2b2b}
.fcell:first-child{border-left:none}
.fill-b{background:#8fd4e8}.fill-o{background:#f5b34c}.fill-v{background:#b79ddb}.fill-g{background:#a9d3a0}
.fracline{display:flex;align-items:center;gap:1.4mm;font-size:10px;font-weight:800;flex-wrap:wrap}
/* grille exercices fractions (a/b × c/d = ovale) */
.fx{
  display:flex;align-items:center;gap:.65mm;justify-content:center;
  background:#fff;border:1.2px solid #e2d8c0;border-radius:2mm;
  padding:1mm .4mm;font-size:9px;min-width:0;overflow:hidden;
}
.fx .mfrac{font-size:9.2px;margin:0 .2mm}
.fx .oval.s{min-width:5.8mm;height:4.4mm;margin:0 .2mm}
.fx-cmp{flex-direction:column;gap:.5mm;padding:1.1mm .7mm}
.fx-cmp .fx-cmp-row{display:flex;align-items:center;gap:1.1mm;justify-content:center}
.vgrid>*{min-width:0}
/* ═══ droite numérique ═══ */
.numline{direction:ltr;margin:1mm auto}
/* ═══ auto-évaluation ═══ */
.self-eval{
  display:flex;align-items:center;justify-content:space-between;gap:2mm;
  margin-top:auto;margin-bottom:1mm;padding:1mm 2.6mm;border-radius:2mm;background:#fffdf6;
  border:1.2px dashed #cdbf9d;font-size:6.9px;font-weight:800;color:#5c5238;position:relative;z-index:2;
}
.se-item{display:flex;align-items:center;gap:1.4mm}
.se-box{width:3.2mm;height:3.2mm;border:1.3px solid #8a7a5c;border-radius:.8mm;background:#fff}
/* ═══ KIT PÉDAGOGIQUE : objectifs · méthode · astuce · piège · défi · bulle ═══ */
.objectifs{
  background:linear-gradient(135deg,#eaf4fb,#eef8ee);border:1.4px solid #b5d5e8;
  border-radius:2.8mm;padding:1.6mm 2.8mm;margin:0 0 1.2mm;
}
.objectifs .obj-t{font-weight:900;font-size:11.5px;color:#1f5e8d;margin-bottom:.5mm}
.objectifs ul{margin:0;padding:0;list-style:none;font-size:10.6px;font-weight:700;line-height:1.55;color:#2c3e50}
.objectifs li:before{content:"☐";color:#2f6ea5;margin-left:1.8mm}
.methode{background:#fff;border:1.4px solid #cfe0ee;border-radius:2.8mm;padding:1.4mm 2.6mm;margin:1mm 0}
.methode .m-t{font-weight:900;font-size:11px;color:#1f5e8d;margin-bottom:.45mm}
.methode .step{display:flex;gap:1.8mm;align-items:flex-start;padding:.35mm 0;font-size:11px;font-weight:700;line-height:1.45}
.methode .sn{
  width:4.5mm;height:4.5mm;border-radius:50%;background:var(--blue);color:#fff;flex-shrink:0;
  display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:7.5px;margin-top:.2mm;
}
.astuce{
  display:flex;gap:2mm;align-items:flex-start;background:#fdf8e3;border:1.4px solid #e6cc93;
  border-radius:2.8mm;padding:1.4mm 2.4mm;margin:1mm 0;font-size:10.6px;font-weight:700;line-height:1.5;
}
.astuce .ico{font-size:11px;line-height:1;flex-shrink:0;margin-top:.3mm}
.astuce b{color:#8a4a12}
.attention{
  display:flex;gap:2mm;align-items:flex-start;background:#fdeeee;border:1.4px solid #e3a6a6;
  border-radius:2.8mm;padding:1.4mm 2.4mm;margin:1mm 0;font-size:10.6px;font-weight:700;line-height:1.5;
}
.attention .ico{font-size:11px;line-height:1;flex-shrink:0;margin-top:.3mm}
.attention b{color:#b03434}
.defi{
  background:linear-gradient(135deg,#fff3d6,#ffe8c2);border:1.6px solid #e8b45a;border-radius:2.6mm;
  padding:1.3mm 2.4mm;margin:.9mm 0;position:relative;
}
.defi .d-t{font-weight:900;font-size:11.2px;color:#a05e10;margin-bottom:.35mm}
.defi .d-q{font-size:10.8px;font-weight:700;line-height:1.55;overflow-wrap:anywhere}
.defi .d-ans{margin-top:1.4mm;display:flex;flex-wrap:wrap;gap:1.6mm;align-items:center}
.bulle-row{display:flex;gap:2mm;align-items:flex-end;margin:1mm 0}
.bulle-row .im{width:12mm;height:11mm;flex-shrink:0}
.bulle{
  position:relative;background:#fff;border:1.5px solid #a8cfe0;border-radius:2.8mm;
  padding:1.4mm 2.6mm;font-size:11px;font-weight:700;line-height:1.5;flex:1;
}
.bulle:after{
  content:"";position:absolute;bottom:2.2mm;right:-2.5mm;border:1.4mm solid transparent;
  border-left:2.6mm solid #a8cfe0;
}
/* ═══ méthode de Singapour : modèle en barres & co ═══ */
.sg-box{
  background:#f2fbf4;border:1.5px solid #9ed3ab;border-radius:3mm;
  padding:1.6mm 2.6mm 1mm;margin:1.4mm 0;
}
.sg-pill{
  display:inline-block;background:#2f8f5b;color:#fff;border-radius:999px;
  padding:.5mm 3mm;font-size:7.6px;font-weight:900;margin-bottom:.8mm;
}
.sg-note{font-size:8.8px;font-weight:800;color:#2f6e46;text-align:center;margin-top:.4mm}
.sg-draw{
  position:relative;border:1.6px dashed #2f8f5b;border-radius:2.6mm;background:#fbfefc;
  margin:1.2mm 0;
}
.sg-draw .sg-draw-h{
  position:absolute;top:.8mm;right:2mm;font-size:8.4px;font-weight:900;color:#2f8f5b;
}
.og-row{display:flex;gap:2.6mm;justify-content:center;flex-wrap:wrap;margin:1mm 0}
.og{
  display:flex;flex-wrap:wrap;gap:.6mm;align-items:center;justify-content:center;
  border:1.5px solid #d78d33;border-radius:45%/55%;background:#fffdf6;
  padding:1.6mm 2.4mm;min-width:13mm;min-height:9mm;font-size:9.5px;line-height:1;
}
.disc{
  width:5.8mm;height:5.8mm;border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-size:4.9px;font-weight:900;border:1.2px solid rgba(0,0,0,.35);color:#26303c;
  box-shadow:inset 0 -1.4px 0 rgba(0,0,0,.14);flex-shrink:0;
}
.disc.empty{border-style:dashed;background:#fff!important;box-shadow:none}
/* mini-جدول المنازل en disques : une colonne par position, chiffre en bas */
.pd-row{display:flex;direction:ltr;gap:1.8mm;justify-content:center;align-items:stretch;margin:1mm 0}
.pd-col{
  background:#fff;border:1.2px solid #e3d8ba;border-radius:2.6mm;padding:1mm 1.2mm .6mm;
  min-width:16mm;display:flex;flex-direction:column;align-items:center;
}
.pd-head{
  font-size:6.9px;font-weight:900;color:#5c4a1e;border-radius:999px;
  padding:.3mm 2.2mm;margin-bottom:.8mm;white-space:nowrap;
}
.pd-discs{
  display:flex;flex-wrap:wrap;gap:.6mm;justify-content:center;align-content:flex-start;
  max-width:16mm;flex:1;min-height:5mm;
}
.pd-discs .disc{width:4.8mm;height:4.8mm;font-size:4.1px}
.pd-digit{
  font-weight:900;font-size:12px;color:#1d7fc4;font-family:'Cairo';
  border-top:1.3px dotted #d8c9a4;width:100%;text-align:center;margin-top:.8mm;
}
/* ═══ bandeau d'unité ═══ */
.unit-banner{
  border-radius:3.5mm;padding:2.4mm 4mm;margin-bottom:2mm;
  display:flex;align-items:center;gap:3mm;
  border:1.4px solid rgba(0,0,0,.09);
}
.unit-banner .unum{
  width:9mm;height:9mm;border-radius:50%;background:#fff;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;font-weight:900;font-size:12px;color:#7c4a12;
  box-shadow:inset 0 -2px 0 rgba(0,0,0,.1);
}
.unit-banner b{font-size:12.5px;font-weight:900;color:#4a3a1c}
.unit-banner small{display:block;font-size:7.6px;font-weight:700;color:#6b5d3f}
/* ═══ couverture pédagogique (rayon / parents) ═══ */
.cover{background:#fff8ee;padding:0!important}
.cover .sheet-inner{
  padding:0!important;gap:0;min-height:0;text-align:center;
  display:flex;flex-direction:column;align-items:stretch;
}
.cover-head{
  position:relative;z-index:3;flex-shrink:0;
  background:linear-gradient(180deg,#ffffff 0%,#fff7ea 100%);
  padding:4.5mm 5.5mm 4.5mm;overflow:hidden;
}
.cover-head:after{
  content:"";position:absolute;left:0;right:0;bottom:-1px;height:7mm;
  background:linear-gradient(180deg,transparent,#ef7d14);
  clip-path:ellipse(75% 100% at 50% 100%);
}
.cover-brand-row{
  display:flex;align-items:center;justify-content:center;gap:2.4mm;margin-bottom:3mm;
}
.cover-brand-row .cover-brand-name{
  font-family:'Cairo',sans-serif;font-weight:900;font-size:13.5px;
  letter-spacing:.2em;color:#d35400;line-height:1;
}
/* ruban de coin 6AF (haut droit) */
.corner-ribbon{
  position:absolute;top:0;right:0;width:44mm;height:44mm;overflow:hidden;
  z-index:7;pointer-events:none;
}
.corner-ribbon span{
  position:absolute;display:block;width:62mm;padding:1.7mm 0;
  background:linear-gradient(145deg,#1d7fc4,#14639e);color:#fff;
  text-align:center;font-family:'Cairo',sans-serif;font-weight:900;font-size:9.4px;
  letter-spacing:.04em;transform:rotate(45deg);right:-16mm;top:10mm;
}
.cover-titles{position:relative;z-index:1}
.cover-titles .eyebrow{
  font-size:7.8px;font-weight:800;color:#8a6a3a;margin:0 0 1.2mm;
  letter-spacing:.06em;
}
.cover-titles h1{
  margin:0;padding:0;font-weight:900;line-height:1.05;color:#1f2a36;
}
.cover-titles h1 .t1{display:block;font-size:35px;color:#e85d04;text-shadow:0 1px 0 rgba(180,70,0,.12)}
.cover-titles h1 .t2{display:block;font-size:35px;color:#1f2a36;margin-top:.3mm}
/* ruban rouge Concours (bouts crantés) */
.ribbon-concours{
  display:block;margin:3.5mm auto 0;width:104mm;position:relative;z-index:2;
  background:linear-gradient(180deg,#e8402f,#c1121f);color:#fff;
  font-family:'Cairo',sans-serif;font-weight:900;font-size:12.5px;line-height:1.2;
  padding:2.4mm 8mm;text-align:center;
  clip-path:polygon(0 0,100% 0,calc(100% - 4mm) 50%,100% 100%,0 100%,4mm 50%);
}
.ribbon-concours small{
  display:block;font-size:7px;font-weight:800;opacity:.92;margin-top:.4mm;letter-spacing:.03em;
}
/* tampon rond « programme officiel » */
.cover-rosette{
  position:absolute;top:5mm;right:5.5mm;z-index:6;
  width:29mm;height:29mm;border-radius:50%;
  background:radial-gradient(circle at 35% 28%,#17a05d,#0a6b3c);
  color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;transform:rotate(7deg);
  font-family:'Cairo',sans-serif;line-height:1.3;padding:2.4mm;
}
.cover-rosette:before{
  content:"";position:absolute;inset:1.7mm;border-radius:50%;
  border:1.5px dashed rgba(255,255,255,.8);
}
.cover-rosette b{font-size:10.5px;font-weight:900}
.cover-rosette span{font-size:7px;font-weight:800;opacity:.95;margin-top:.5mm;line-height:1.45}
.cover-stage{
  position:relative;flex:1;min-height:0;overflow:hidden;
  background:
    radial-gradient(ellipse 90% 55% at 50% 0%, rgba(255,230,160,.55) 0%, transparent 55%),
    linear-gradient(175deg,#f6a01f 0%,#ef7a12 55%,#dc5608 100%);
  display:flex;flex-direction:column;align-items:center;justify-content:flex-end;
  padding:0 0 13mm;
}
.cover-chips{
  position:absolute;inset:0;pointer-events:none;z-index:4;
}
.cover-chip{
  position:absolute;background:#fff;border-radius:5mm;
  padding:1.5mm 3mm;font-size:8.5px;font-weight:900;color:#e0670c;
  font-family:'Cairo',sans-serif;line-height:1;
}
.cover-chip.math{top:9mm;left:8mm;transform:rotate(-6deg)}
.cover-chip.win{
  top:38mm;right:7mm;transform:rotate(2deg);
  color:#0f7a4a;font-size:8px;
}
.cover-stage .cover-mascots{
  position:relative;z-index:2;display:flex;gap:3mm;align-items:flex-end;justify-content:center;
  width:100%;height:84mm;padding:0;
}
.cover-stage .cover-mascots .im{
  width:58mm;height:84mm;
  background-size:140% auto;background-position:center 10%;
}
/* badge « cahier intelligent » : appli + vidéos */
.cover-app{
  position:absolute;z-index:4;left:7mm;top:22mm;width:56mm;
  background:#fff;border-radius:3mm;padding:2.4mm 2.8mm;
  display:flex;align-items:center;gap:2.2mm;text-align:right;
  font-family:'Cairo',sans-serif;
}
.cover-app .app-ic{
  width:8mm;height:8mm;border-radius:50%;flex-shrink:0;
  background:linear-gradient(145deg,#1d7fc4,#14639e);color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:9px;
}
.cover-app .app-txt{flex:1;min-width:0}
.cover-app .app-txt b{display:block;font-size:10px;font-weight:900;color:#1f2a36;line-height:1.2}
.cover-app .app-txt span{
  display:block;font-size:6.8px;font-weight:800;color:#6b5330;line-height:1.5;margin-top:.5mm;
}
.cover-stage .owner-line{
  position:absolute;left:50%;transform:translateX(-50%);bottom:8mm;z-index:5;
  width:124mm;background:#fff;border:none;border-radius:2.4mm;
  padding:1.9mm 4mm;font-size:8.2px;font-weight:800;color:#4a3a1c;
  display:flex;gap:2mm;align-items:center;justify-content:center;
}
.cover-stage .owner-line i{
  flex:1;border-bottom:1.5px dotted #c4a46a;height:3.4mm;font-style:normal;min-width:26mm;
}
.cover .wave{height:6.5mm;z-index:4}
/* cover-logo sizing is in CSS_ASSETS */
/* ═══ pages d'ouverture de partie ═══ */
.part-hero{
  position:relative;flex:1;min-height:0;border-radius:6mm;overflow:hidden;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;padding:9mm 8mm 0;
}
.part-orb{position:absolute;border-radius:50%;background:rgba(255,255,255,.4)}
.part-orb.o1{width:46mm;height:46mm;top:-14mm;left:-14mm}
.part-orb.o2{width:26mm;height:26mm;top:30mm;right:-9mm}
.part-orb.o3{width:16mm;height:16mm;bottom:52mm;left:8mm;background:rgba(255,255,255,.28)}
.part-emoji{
  width:22mm;height:22mm;border-radius:50%;background:#fff;
  display:flex;align-items:center;justify-content:center;font-size:26px;
  margin:auto auto 4.5mm;position:relative;z-index:1;
}
.part-kicker{
  color:#fff;border-radius:999px;padding:1.7mm 5.5mm;font-size:9.5px;font-weight:900;
  letter-spacing:.03em;position:relative;z-index:1;
}
.part-title{font-size:34px;font-weight:900;margin:3.5mm 0 2mm;position:relative;z-index:1;line-height:1.1}
.part-sub{
  font-size:9.8px;font-weight:800;line-height:1.8;max-width:104mm;
  margin:0 0 4.5mm;opacity:.85;position:relative;z-index:1;
}
.part-chips{
  display:flex;gap:2.6mm;flex-wrap:wrap;justify-content:center;
  max-width:116mm;position:relative;z-index:1;
}
.part-mascots{
  margin-top:auto;position:relative;z-index:1;
  display:flex;justify-content:center;align-items:flex-end;padding-top:4mm;
}
.part-mascots .im{
  width:58mm;height:52mm;
  background-size:contain;background-position:center bottom;
}
.toc{width:100%;border-collapse:collapse;margin-top:2mm}
.toc td{padding:1.5mm 2mm;border-bottom:1.4px dotted #d8c9a4;font-size:12px;font-weight:800}
.toc .tno{color:#fff;background:var(--orange);border-radius:50%;width:5.6mm;height:5.6mm;display:inline-flex;align-items:center;justify-content:center;font-size:8.5px;font-weight:900}
.toc .tp{text-align:left;color:var(--blue);font-weight:900;font-variant-numeric:tabular-nums}
/* toolbar */
.toolbar{position:fixed;top:12px;left:16px;z-index:9999}
.action-btn{
  border:none;border-radius:999px;padding:9px 15px;font-family:'Cairo',sans-serif;
  font-size:13px;font-weight:800;cursor:pointer;background:var(--blue);color:#fff;
  box-shadow:0 8px 20px rgba(15,23,42,.16);
}
.action-btn:focus-visible{outline:3px solid #9cc3e8;outline-offset:2px}
.figv{margin:1.6mm auto;background:#fff;border:1px solid #e4d9bd;border-radius:2.6mm;
  padding:1.6mm 1.6mm 1mm;box-shadow:0 1px 0 rgba(0,0,0,.04)}
.figv svg{width:100%;height:auto;display:block}
.figcap{text-align:center;font-size:7.5px;font-weight:700;color:#8a6d3b;margin-top:.8mm}
/* ═══ PRINT A5 ═══ */
@media print{
  @page{size:148mm 210mm;margin:0}
  .toolbar{display:none!important}
  html,body{background:#fff!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .sheet{
    width:148mm!important;height:210mm!important;margin:0 auto!important;
    border-radius:0!important;box-shadow:none!important;
    break-after:page;page-break-after:always;overflow:hidden!important;
  }
  .sheet:last-of-type{break-after:auto!important}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""

# vague aplatie (16/07) : le bleu ne monte plus qu'à ~5,5 mm sous le bord de sa boîte
# (avant : 2,5 mm) — dégage ~3 mm pour le contenu des pages pleines, même style.
WAVE_SVG = """<svg viewBox="0 0 148 12" preserveAspectRatio="none" aria-hidden="true">
<path d="M0,12 L0,7.5 Q25,5 53,7 Q92,9.5 148,6 L148,12 Z" fill="#1d7fc4"/>
<path d="M0,12 L0,9.5 Q32,6.5 67,8.5 Q106,10.5 148,8 L148,12 Z" fill="#45a4e0" opacity=".85"/>
</svg>"""

CSS_ASSETS = f"""
.im{{display:inline-block;background-repeat:no-repeat;background-position:center;background-size:contain;background-color:transparent!important;box-shadow:none!important;filter:none!important}}
.im-fille{{background-image:url("{ASSETS['fille']}")}}
.im-garcon{{background-image:url("{ASSETS['garcon']}")}}
.im-nuage{{background-image:url("{ASSETS['nuage']}")}}
.im-qr{{background-image:url("{ASSETS['qr']}");image-rendering:pixelated}}
.im-logo{{background-image:url("{ASSETS['logo']}")}}
img.logo{{width:8.5mm;height:8.5mm;border-radius:2mm;object-fit:contain;object-position:center;display:block;flex-shrink:0}}
img.cover-logo{{width:11mm;height:11mm;object-fit:contain;object-position:center;display:block;border-radius:2mm}}
"""


def logo_img(css_class='logo'):
    """Logo Major en <img> (fichier relatif livrables/logo-major.png — fiable à l'impression)."""
    return f'<img class="{css_class}" src="logo-major.png" alt="Major" draggable="false"/>'

# ─────────────────────────── helpers texte ───────────────────────────
FR = lambda a, b: f'<span class="mfrac"><span>{a}</span><span>{b}</span></span>'
MX = lambda s: f'<span class="mexp">{s}</span>'
OVAL = '<span class="oval"></span>'
OVS = '<span class="oval s"></span>'
OVM = '<span class="oval" style="min-width:20mm"></span>'  # réponse numérique inline (3-5 chiffres)
SQ = '<span class="sq"></span>'


def badge_row(label, sub, mascot_key):
    return f'''<div class="badge-row">
      <span class="im im-{mascot_key} mascot" role="img" aria-label=""></span>
      <div class="badge">{label}<small>{sub}</small></div>
    </div>'''


def video_box():
    return '''<div class="video-box">
      <div class="nuage-bg im im-nuage"><span>امسح: فيديو + ملخّص + أنشطة</span></div>
      <span class="im im-qr qr" role="img" aria-label="QR فيديو الدرس"></span>
    </div>'''


def figure_img(src, w_mm, caption=''):
    """Vignette illustrée (image du pptx d'origine) : centrée, cadre doux, légende."""
    cap = f'<div class="figcap">{caption}</div>' if caption else ''
    return (f'<div class="figv" style="width:{w_mm}mm">'
            f'<img src="{src}" alt="{caption}" style="width:100%;display:block"/>{cap}</div>')


def figure_svg(svg, w_mm, caption=''):
    """Vignette vectorielle (SVG inline du pptx) : nette à l'impression."""
    cap = f'<div class="figcap">{caption}</div>' if caption else ''
    return f'<div class="figv" style="width:{w_mm}mm">{svg}{cap}</div>'


def tok(n):
    return f'<span class="tok"><i>{n}</i></span>'


def _print_lvl(lvl):
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
        ('🎯', ''), ('🧩', ''), ('🔢', ''), ('🌿', ''), ('👀', ''),
        ('📚', ''), ('🛒', ''), ('🫖', ''), ('🥖', ''), ('🐟', ''),
        ('😀', ''), ('🤔', ''), ('🙋', ''), ('📊', ''),
        ('🖨', ''), ('🖨️', ''), ('☆', '○'), ('🇲🇷', ''),
        ('⚠️', ''), ('⚠', ''), ('⬆️', ''), ('⬆', ''), ('⏱️', ''), ('⏰', ''),
        ('✈️', ''), ('🗺️', ''), ('🗺', ''), ('🧭', ''), ('💡', ''),
    ]
    for a, b in repl:
        html = html.replace(a, b)
    html = re.sub(r'[ \t]{2,}', ' ', html)
    return html


def exo(n, lvl, body):
    label = _print_lvl(lvl) if lvl else ''
    lv = f'<span class="lvl">{label}</span>' if label else ''
    return f'''<div class="exo">
      <div class="exo-head">{tok(n)}{lv}</div>
      <div class="exo-q">{body}</div>
    </div>'''


def consigne(n, txt):
    return f'<div class="consigne">{tok(n)}<span>{txt}</span></div>'


def dots(n):
    return '<div class="dots">' + '<div class="dotl"></div>' * n + '</div>'


def pie(frac_deg, n_parts, fill='#8fd4e8'):
    """Tarte de fractions en SVG vectoriel (net à l'impression) : secteur coloré de frac_deg
    degrés (depuis le haut, sens horaire), n_parts rayons de découpe, contour franc."""
    R, C = 18, 20  # rayon, centre — viewBox 40×40 affiché en 13mm (.pie)
    pt = lambda deg: f'{C + R * math.sin(math.radians(deg)):.2f},{C - R * math.cos(math.radians(deg)):.2f}'
    if frac_deg >= 360:
        sector = f'<circle cx="{C}" cy="{C}" r="{R}" fill="{fill}"/>'
    elif frac_deg > 0:
        large = 1 if frac_deg > 180 else 0
        sector = f'<path d="M{C},{C} L{pt(0)} A{R},{R} 0 {large} 1 {pt(frac_deg)} Z" fill="{fill}"/>'
    else:
        sector = ''
    xy = lambda deg: (C + R * math.sin(math.radians(deg)), C - R * math.cos(math.radians(deg)))
    spokes = ''.join(f'<line x1="{C}" y1="{C}" x2="{xy(i * 360 / n_parts)[0]:.2f}" y2="{xy(i * 360 / n_parts)[1]:.2f}" stroke="#2b2b2b" stroke-width="1.1"/>'
                     for i in range(n_parts)) if n_parts > 1 else ''
    return (f'<svg class="pie" viewBox="0 0 40 40" style="overflow:visible">'
            f'<circle cx="{C}" cy="{C}" r="{R}" fill="#fff"/>{sector}{spokes}'
            f'<circle cx="{C}" cy="{C}" r="{R}" fill="none" stroke="#2b2b2b" stroke-width="1.6"/></svg>')


# ─────────────────── kit pédagogique v2 ───────────────────
def objectifs(items):
    """Encadré « في هذه الوحدة سأتعلّم » avec cases à cocher (3-4 items max)."""
    lis = ''.join(f'<li>{i}</li>' for i in items)
    return f'<div class="objectifs"><div class="obj-t">في هذه الوحدة سأتعلّم:</div><ul>{lis}</ul></div>'


def methode(title, steps):
    """Méthode pas-à-pas numérotée (2-4 étapes courtes)."""
    rows = ''.join(f'<div class="step"><span class="sn">{i + 1}</span><span>{s}</span></div>'
                   for i, s in enumerate(steps))
    return f'<div class="methode"><div class="m-t">{title}</div>{rows}</div>'


def astuce(txt):
    """Conseil malin du prof (1-2 lignes)."""
    return f'<div class="astuce"><span class="ico">!</span><span><b>أستاذ ماجور ينصح:</b> {txt}</span></div>'


def attention(txt):
    """Erreur fréquente à éviter (1-2 lignes)."""
    return f'<div class="attention"><span class="ico">!</span><span><b>انتبه للخطأ الشائع:</b> {txt}</span></div>'


def defi(txt):
    """Défi des champions en fin d'unité.
    Les ovales/blanks en fin de phrase passent sur une ligne dédiée
    pour éviter le chevauchement avec le texte qui revient à la ligne."""
    m = re.search(r'((?:\s*<span class="oval[^"]*"[^>]*>.*?</span>)+\s*)$', txt)
    if m:
        q = txt[:m.start()].rstrip()
        blanks = m.group(1).strip()
        return (f'<div class="defi"><div class="d-t">تحدّي الأبطال</div>'
                f'<div class="d-q">{q}</div><div class="d-ans">{blanks}</div></div>')
    return f'<div class="defi"><div class="d-t">تحدّي الأبطال</div><div class="d-q">{txt}</div></div>'


def bulle(mascot_key, txt):
    """Bulle de dialogue d'une mascotte (fille/garcon)."""
    return f'''<div class="bulle-row">
      <span class="im im-{mascot_key}" role="img" aria-label=""></span>
      <div class="bulle">{txt}</div>
    </div>'''


def vop(a, b, sign):
    """Opération posée (a en haut, b en bas, ligne, espace résultat)."""
    return f'''<div class="vop">{a}<br><span class="sign">{sign}</span>{b}<span class="vline"></span></div>'''


def vop_grid(pairs, sign, cols=4):
    cells = ''.join(vop(a, b, sign) for a, b in pairs)
    return f'<div class="vgrid" style="grid-template-columns:repeat({cols},1fr)">{cells}</div>'


def fam_table_empty(families=3, reading_line=True):
    """Tableau آ ع م vide. Direction LTR : milliards à gauche, unités à droite
    (comme s'écrivent les chiffres), م ع آ = centaines/dizaines/unités dans chaque famille."""
    names = [('الوحدات', 'fam-u'), ('الآلاف', 'fam-k'), ('الملايين', 'fam-m'), ('المليارات', 'fam-g')]
    use = list(reversed(names[:families]))  # LTR : la plus grande famille en premier = à gauche
    top = ''.join(f'<th class="{c}" colspan="3" style="background:var(--p-{ {"fam-u":"yell","fam-k":"rose","fam-m":"green","fam-g":"blue"}[c] })">{n}</th>' for n, c in [(n, c) for n, c in use])
    sub = ''.join('<th style="font-size:7px">مئات</th><th style="font-size:7px">عشرات</th><th style="font-size:7px">آحاد</th>' for _ in use)
    cells = ''.join('<td><span class="cellbox">&nbsp;</span></td>' * 3 for _ in use)
    read = f'<tr><td colspan="{3*families}" style="border:none;padding-top:1mm"><div class="dotl" style="height:7mm"></div></td></tr>' if reading_line else ''
    return f'''<table class="fam-table" style="direction:ltr">
      <tr>{top}</tr><tr class="sub">{sub}</tr><tr>{cells}</tr>{read}
    </table>'''


def wheel(center, nums, r=15.5):
    """Roue de multiplication : centre 'Nx', anneau de nombres, anneau extérieur vide."""
    cx = cy = r + 1.2
    n = len(nums)
    spokes, innums = [], []
    for i, v in enumerate(nums):
        a0 = (i / n) * 2 * math.pi - math.pi / 2
        x1, y1 = cx + math.cos(a0) * (r * .34), cy + math.sin(a0) * (r * .34)
        x2, y2 = cx + math.cos(a0) * r, cy + math.sin(a0) * r
        spokes.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#8a4a12" stroke-width=".45"/>')
        am = ((i + .5) / n) * 2 * math.pi - math.pi / 2
        xm, ym = cx + math.cos(am) * (r * .52), cy + math.sin(am) * (r * .52)
        innums.append(f'<text x="{xm:.1f}" y="{ym + 1.1:.1f}" text-anchor="middle" font-size="3.1" font-weight="900" fill="#26303c">{v}</text>')
    return f'''<svg width="{2*cx}mm" height="{2*cy}mm" viewBox="0 0 {2*cx} {2*cy}" style="overflow:visible;display:block">
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="#fffdf6" stroke="#d78d33" stroke-width=".9"/>
      <circle cx="{cx}" cy="{cy}" r="{r*.68}" fill="#fdf1d7" stroke="#d78d33" stroke-width=".7"/>
      {''.join(spokes)}
      <circle cx="{cx}" cy="{cy}" r="{r*.34}" fill="#e2504c" stroke="#b13c38" stroke-width=".7"/>
      <text x="{cx}" y="{cy + 1.6}" text-anchor="middle" font-size="4.6" font-weight="900" fill="#fff">{center}</text>
      {''.join(innums)}
    </svg>'''


def angle_svg(deg, label='', w=24, h=18, color='#2f6ea5'):
    """Angle : deux rayons depuis un sommet + arc."""
    ox, oy = 3, h - 3
    L = min(w, h) - 5
    a = math.radians(deg)
    x2, y2 = ox + L, oy
    x3, y3 = ox + L * math.cos(a), oy - L * math.sin(a)
    ra = L * .38
    ax, ay = ox + ra, oy
    bx, by = ox + ra * math.cos(a), oy - ra * math.sin(a)
    large = 1 if deg > 180 else 0
    lab = (f'<text x="{w/2}" y="{h-.6}" text-anchor="middle" font-size="3.2" font-weight="900" fill="#8a4a12" '
           f'stroke="#fff" stroke-width="1.1" paint-order="stroke">{label}</text>') if label else ''
    return f'''<svg width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}" style="overflow:visible;display:block;margin:0 auto">
      <path d="M{ax:.1f},{ay:.1f} A{ra:.1f},{ra:.1f} 0 {large} 0 {bx:.1f},{by:.1f}" fill="none" stroke="#e2504c" stroke-width=".7"/>
      <line x1="{ox}" y1="{oy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="1.1" stroke-linecap="round"/>
      <line x1="{ox}" y1="{oy}" x2="{x3:.1f}" y2="{y3:.1f}" stroke="{color}" stroke-width="1.1" stroke-linecap="round"/>
      <circle cx="{ox}" cy="{oy}" r="1" fill="{color}"/>
      {lab}
    </svg>'''


def lines_svg(kind, w=27, h=16):
    """Paires de droites : parallel / perp / cross."""
    if kind == 'parallel':
        body = f'''<line x1="2" y1="5" x2="{w-2}" y2="3.4" stroke="#2f6ea5" stroke-width="1.1"/>
                   <line x1="2" y1="{h-4}" x2="{w-2}" y2="{h-5.6}" stroke="#e2504c" stroke-width="1.1"/>'''
    elif kind == 'perp':
        body = f'''<line x1="3" y1="{h-3}" x2="{w-3}" y2="{h-3}" stroke="#2f6ea5" stroke-width="1.1"/>
                   <line x1="{w/2}" y1="1.5" x2="{w/2}" y2="{h-1.5}" stroke="#e2504c" stroke-width="1.1"/>
                   <rect x="{w/2}" y="{h-6}" width="3" height="3" fill="none" stroke="#33591f" stroke-width=".55"/>'''
    else:
        body = f'''<line x1="2" y1="{h-2.5}" x2="{w-2}" y2="3" stroke="#2f6ea5" stroke-width="1.1"/>
                   <line x1="3" y1="4.5" x2="{w-3}" y2="{h-3.5}" stroke="#e2504c" stroke-width="1.1"/>'''
    return f'<svg width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}" style="overflow:visible;display:block;margin:0 auto">{body}</svg>'


def numline(w=118, ticks=None, labels=None, y=9):
    """Droite numérique. ticks = positions 0..1 ; labels = dict pos→txt ('?' → ovale à compléter).
    L'ovale s'adapte à l'écart entre graduations pour ne pas recouvrir les étiquettes voisines."""
    ticks = ticks or []
    labels = labels or {}
    st = sorted(ticks)
    gap = min((b - a for a, b in zip(st, st[1:])), default=1) * (w - 12)
    rx = min(4.6, max(2.4, gap * .40))
    parts = [f'<line x1="4" y1="{y}" x2="{w-4}" y2="{y}" stroke="#33475e" stroke-width="1"/>',
             f'<path d="M{w-4},{y} l-3,-1.8 l0,3.6 Z" fill="#33475e"/>']
    for t in ticks:
        x = 4 + t * (w - 12)
        parts.append(f'<line x1="{x:.1f}" y1="{y-2.4}" x2="{x:.1f}" y2="{y+2.4}" stroke="#33475e" stroke-width=".9"/>')
        lab = labels.get(t)
        if lab == '?':
            parts.append(f'<ellipse cx="{x:.1f}" cy="{y+6.2}" rx="{rx:.1f}" ry="{min(2.9, rx*.72):.1f}" fill="#fff" stroke="#2b2b2b" stroke-width=".65"/>')
        elif lab:
            parts.append(f'<text x="{x:.1f}" y="{y+7.6}" text-anchor="middle" font-size="4" font-weight="900" fill="#26303c">{lab}</text>')
    return f'<div class="numline"><svg width="{w}mm" height="{y+10}mm" viewBox="0 0 {w} {y+10}">{"".join(parts)}</svg></div>'


def fx_row(items, cols=5):
    """Grille de petites cartes d'opérations sur fractions."""
    return f'<div class="vgrid" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(items) + '</div>'


def fx(a, b, c, d, op='×'):
    """Carte : a/b op c/d = [ovale]."""
    return f'''<div class="fx">{FR(a,b)}<b>{op}</b>{FR(c,d)}<b>=</b><span class="oval s"></span></div>'''


def conv_table(units, subcols=1, rows=3, filled=None, title=''):
    """Tableau de conversion (longueurs, masses, aires…). units = liste RTL-safe affichée LTR.
    subcols=2 pour les aires (d/u), 3 pour les volumes (c/d/u). filled = dict {(row,col): digit}."""
    filled = filled or {}
    head = ''.join(f'<th colspan="{subcols}">{u}</th>' for u in units)
    sub = ''
    if subcols > 1:
        letters = ['م', 'ع', 'آ'][-subcols:]  # مئات عشرات آحاد
        sub = '<tr class="sub">' + ''.join(f'<th>{l}</th>' for _ in units for l in letters) + '</tr>'
    body = ''
    for r in range(rows):
        tds = ''
        for c in range(len(units) * subcols):
            v = filled.get((r, c), '')
            tds += f'<td><span class="cellbox">{v or "&nbsp;"}</span></td>'
        body += f'<tr>{tds}</tr>'
    t = f'<div style="text-align:center;font-weight:900;font-size:8.6px;color:#8a4a12;margin-bottom:.8mm">{title}</div>' if title else ''
    return f'''{t}<table class="fam-table" style="direction:ltr;width:100%">
      <tr>{head}</tr>{sub}{body}
    </table>'''


def tri_svg(kind='any', w=24, h=17, label=''):
    """Triangle : any / right / iso / equi / iso-right."""
    pts = {'any': '2,15 22,15 15,3', 'right': '3,15 21,15 3,3',
           'iso': '4,15 20,15 12,2', 'equi': '4.5,15 19.5,15 12,2.4',
           'iso-right': '3,15 17,15 3,1'}[kind]
    extra = ''
    if kind in ('right', 'iso-right'):
        extra = '<rect x="3" y="12" width="3" height="3" fill="none" stroke="#33591f" stroke-width=".5"/>'
    if kind == 'iso':
        extra = '<line x1="7" y1="8" x2="9" y2="9" stroke="#c0392b" stroke-width=".6"/><line x1="17" y1="8" x2="15" y2="9" stroke="#c0392b" stroke-width=".6"/>'
    lab = f'<text x="{w/2}" y="{h-.2}" text-anchor="middle" font-size="2.8" font-weight="900" fill="#8a4a12">{label}</text>' if label else ''
    return f'''<svg width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}" style="overflow:visible;display:block;margin:0 auto">
      <polygon points="{pts}" fill="#eaf3fa" stroke="#2f6ea5" stroke-width=".9" stroke-linejoin="round"/>{extra}{lab}</svg>'''


def quad_svg(kind, w=26, h=17):
    """Quadrilatère : square / rect / losange / para / trapeze."""
    if kind == 'square':
        body = '<rect x="6.5" y="2.5" width="12" height="12" fill="#fdf1d7" stroke="#c9711a" stroke-width=".9"/>'
    elif kind == 'rect':
        body = '<rect x="3" y="4" width="20" height="10" fill="#eaf3fa" stroke="#2f6ea5" stroke-width=".9"/>'
    elif kind == 'losange':
        body = ('<polygon points="13,1.5 21,8.5 13,15.5 5,8.5" fill="#f6d9d0" stroke="#c0392b" stroke-width=".9"/>'
                '<line x1="5" y1="8.5" x2="21" y2="8.5" stroke="#8a4a12" stroke-width=".5" stroke-dasharray="1.4,1"/>'
                '<line x1="13" y1="1.5" x2="13" y2="15.5" stroke="#8a4a12" stroke-width=".5" stroke-dasharray="1.4,1"/>')
    elif kind == 'para':
        body = '<polygon points="6,3 24,3 20,14 2,14" fill="#dcead3" stroke="#33591f" stroke-width=".9"/>'
    else:  # trapeze
        body = '<polygon points="8,3 18,3 23,14 3,14" fill="#ead9ee" stroke="#7a4f8a" stroke-width=".9"/>'
    return f'<svg width="{w}mm" height="{h}mm" viewBox="0 0 26 17" style="overflow:visible;display:block;margin:0 auto">{body}</svg>'


def circle_svg(w=26, h=22, labels=True):
    """Cercle : diamètre horizontal + rayon vertical (libellés hors des traits)."""
    cx, cy, r = 13, 10, 9
    body = (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fffdf6" stroke="#2b2b2b" stroke-width=".9"/>'
        f'<line x1="{cx - r}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="#2f6ea5" '
        f'stroke-width=".85" stroke-linecap="round"/>'
        f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - r}" stroke="#c0392b" '
        f'stroke-width=".85" stroke-linecap="round"/>'
        f'<circle cx="{cx}" cy="{cy}" r=".85" fill="#2b2b2b"/>'
    )
    if labels:
        body += (
            f'<text x="{cx}" y="{cy + 4.4}" text-anchor="middle" font-size="2.6" font-weight="900" '
            f'fill="#2f6ea5" stroke="#fffdf6" stroke-width="1.1" paint-order="stroke fill">القطر</text>'
            f'<text x="{cx + 3.4}" y="{cy - r / 2 + .7:.1f}" text-anchor="start" font-size="2.8" font-weight="900" '
            f'fill="#c0392b" stroke="#fffdf6" stroke-width="1.3" paint-order="stroke fill">نق</text>'
        )
    return (f'<svg width="{w}mm" height="{h}mm" viewBox="0 0 26 22" '
            f'style="overflow:visible;display:block;margin:0 auto">{body}</svg>')


def solid_svg(kind, w=24, h=20):
    """Solide : cube / pave / cyl / sphere."""
    if kind == 'cube':
        body = ('<polygon points="4,7 14,7 14,17 4,17" fill="#eaf3fa" stroke="#2f6ea5" stroke-width=".8"/>'
                '<polygon points="4,7 8,3 18,3 14,7" fill="#d5e6f4" stroke="#2f6ea5" stroke-width=".8"/>'
                '<polygon points="14,7 18,3 18,13 14,17" fill="#c2d9ee" stroke="#2f6ea5" stroke-width=".8"/>')
    elif kind == 'pave':
        body = ('<polygon points="2,9 16,9 16,17 2,17" fill="#fdf1d7" stroke="#c9711a" stroke-width=".8"/>'
                '<polygon points="2,9 7,4 21,4 16,9" fill="#fbe3ad" stroke="#c9711a" stroke-width=".8"/>'
                '<polygon points="16,9 21,4 21,12 16,17" fill="#f5d68a" stroke="#c9711a" stroke-width=".8"/>')
    elif kind == 'cyl':
        body = ('<rect x="6" y="5" width="12" height="11" fill="#dcead3" stroke="#33591f" stroke-width=".8"/>'
                '<ellipse cx="12" cy="16" rx="6" ry="2.2" fill="#cfe0c4" stroke="#33591f" stroke-width=".8"/>'
                '<ellipse cx="12" cy="5" rx="6" ry="2.2" fill="#e8f2e0" stroke="#33591f" stroke-width=".8"/>'
                '<line x1="6" y1="5" x2="6" y2="16" stroke="#33591f" stroke-width=".8"/>'
                '<line x1="18" y1="5" x2="18" y2="16" stroke="#33591f" stroke-width=".8"/>')
    else:  # sphere
        body = ('<circle cx="12" cy="10.5" r="8" fill="#f6d9d0" stroke="#c0392b" stroke-width=".8"/>'
                '<ellipse cx="12" cy="10.5" rx="8" ry="2.6" fill="none" stroke="#c0392b" stroke-width=".55" stroke-dasharray="1.4,1"/>')
    return f'<svg width="{w}mm" height="{h}mm" viewBox="0 0 24 20" style="overflow:visible;display:block;margin:0 auto">{body}</svg>'


def prop_table(top_label, bottom_label, tops, bottoms):
    """Tableau de proportionnalité : '?' → case à remplir."""
    def cell(v):
        inner = '<span class="cellbox">&nbsp;</span>' if v == '?' else f'<b>{v}</b>'
        return f'<td>{inner}</td>'
    return f'''<table class="fam-table" style="width:100%">
      <tr><th style="background:var(--p-yell);color:#7c4a12">{top_label}</th>{''.join(cell(v) for v in tops)}</tr>
      <tr><th style="background:var(--p-blue);color:#1f5566">{bottom_label}</th>{''.join(cell(v) for v in bottoms)}</tr>
    </table>'''


# ─────────────────── schémas pédagogiques v3 ───────────────────
def clock_svg(h, m, w=22, label=''):
    """Cadran d'horloge : cercle, 12 graduations, chiffres 12/3/6/9, aiguilles selon h:m."""
    cx = cy = w / 2
    r = w / 2 - 1.1
    parts = [f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="#fffdf6" stroke="#2b2b2b" stroke-width=".9"/>']
    for i in range(12):
        a = math.radians(i * 30 - 90)
        r2 = r - (1.9 if i % 3 == 0 else 1.2)
        parts.append(f'<line x1="{cx + math.cos(a) * r2:.1f}" y1="{cy + math.sin(a) * r2:.1f}" '
                     f'x2="{cx + math.cos(a) * (r - .4):.1f}" y2="{cy + math.sin(a) * (r - .4):.1f}" '
                     f'stroke="#33475e" stroke-width="{".8" if i % 3 == 0 else ".45"}"/>')
    for v, ang in ((12, -90), (3, 0), (6, 90), (9, 180)):
        a = math.radians(ang)
        parts.append(f'<text x="{cx + math.cos(a) * (r - 3.8):.1f}" y="{cy + math.sin(a) * (r - 3.8) + 1.15:.1f}" '
                     f'text-anchor="middle" font-size="3.1" font-weight="900" fill="#26303c">{v}</text>')
    ah = math.radians((h % 12) * 30 + m * .5 - 90)
    am = math.radians(m * 6 - 90)
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + math.cos(ah) * r * .45:.1f}" y2="{cy + math.sin(ah) * r * .45:.1f}" stroke="#1d7fc4" stroke-width="1.4" stroke-linecap="round"/>')
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + math.cos(am) * r * .72:.1f}" y2="{cy + math.sin(am) * r * .72:.1f}" stroke="#e2504c" stroke-width=".9" stroke-linecap="round"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r=".9" fill="#26303c"/>')
    svg = f'<svg width="{w}mm" height="{w}mm" viewBox="0 0 {w} {w}" style="overflow:visible;display:block;margin:0 auto">{"".join(parts)}</svg>'
    if label:
        return f'<div style="text-align:center">{svg}<div style="font-size:8.4px;font-weight:900;color:#8a4a12;margin-top:.4mm">{label}</div></div>'
    return svg


def bar_model(total_label, parts, w=100, stagger=None, scale=1):
    """Barre segmentée (bar model de Singapour) : segments proportionnels + accolade du total.
    parts = liste (label, valeur relative, couleur[, affiché]) — noms au-dessus, valeurs dans
    les segments ; le 4ᵉ élément optionnel remplace la valeur affichée (p.ex. '؟' pour l'inconnue).
    stagger : noms sur deux rangées alternées (auto si un segment est étroit).
    scale < 1 : réduit le rendu (même dessin, moins de place) pour les pages chargées."""
    if stagger is None:
        stagger = len(parts) > 2
    bh = 8
    y0 = 8.4 if stagger else 6.4
    total = sum(p[1] for p in parts) or 1
    x0, x1 = 2, w - 2
    rows = [i % 2 for i in range(len(parts))] if stagger else [0] * len(parts)
    segs, x = [], x0
    for i, p in enumerate(parts):
        lab, v, col = p[0], p[1], p[2]
        shown = p[3] if len(p) > 3 else f'{v:g}'
        unknown = shown == '؟'
        sw = (x1 - x0) * v / total
        xc = x + sw / 2
        yn = 3.6 if rows[i] == 0 else 6.6
        segs.append(f'<rect x="{x:.1f}" y="{y0}" width="{sw:.1f}" height="{bh}" fill="{col}" stroke="#2b2b2b" stroke-width=".7"{" stroke-dasharray=\"1.6 1\"" if unknown else ""}/>')
        # LTR + espaces insécables : « 1 000 » ne devient jamais « 000 1 » en contexte RTL
        shown_txt = shown.replace(' ', '\u00a0')
        segs.append(
            f'<text x="{xc:.1f}" y="{y0 + bh / 2 + 1.3:.1f}" text-anchor="middle" direction="ltr" '
            f'unicode-bidi="isolate" font-size="{4.2 if unknown else 3.4}" font-weight="900" '
            f'fill="{"#c0392b" if unknown else "#26303c"}">{shown_txt}</text>')
        if lab:
            segs.append(f'<text x="{xc:.1f}" y="{yn:.1f}" text-anchor="middle" direction="rtl" font-size="3.0" font-weight="900" fill="#5c5238">{lab}</text>')
            segs.append(f'<line x1="{xc:.1f}" y1="{yn + .7:.1f}" x2="{xc:.1f}" y2="{y0 - .3:.1f}" stroke="#a8b0bd" stroke-width=".35"/>')
        x += sw
    yb, d, mid = y0 + bh + 1.1, 1.7, (x0 + x1) / 2
    brace = (f'<path d="M{x0},{yb} Q{x0},{yb + d} {x0 + d},{yb + d} L{mid - d:.1f},{yb + d} '
             f'Q{mid:.1f},{yb + d} {mid:.1f},{yb + 2 * d} Q{mid:.1f},{yb + d} {mid + d:.1f},{yb + d} '
             f'L{x1 - d},{yb + d} Q{x1},{yb + d} {x1},{yb}" fill="none" stroke="#8a4a12" stroke-width=".55"/>')
    # total : RTL pour l'arabe, chiffres isolés LTR
    tot_safe = re.sub(
        r'(\d[\d\u00a0 ]*[,\d]*)',
        lambda m: f'<tspan direction="ltr" unicode-bidi="isolate">{m.group(1).replace(" ", "\u00a0")}</tspan>',
        total_label,
    )
    tot = (f'<text x="{mid:.1f}" y="{yb + 2 * d + 3.6:.1f}" text-anchor="middle" direction="rtl" '
           f'font-size="3.5" font-weight="900" fill="#8a4a12">{tot_safe}</text>')
    H = yb + 2 * d + 4.9
    return (f'<div style="width:{w * scale:.1f}mm;margin:.6mm auto"><svg width="{w * scale:.1f}mm" height="{H * scale:.1f}mm" '
            f'viewBox="0 0 {w} {H:.1f}" style="overflow:visible;display:block">{"".join(segs)}{brace}{tot}</svg></div>')


def sg_pill():
    return '<span class="sg-pill">نموذج الشريط — أرسم لأفهم</span>'


def sg_box(content, note=''):
    """Encadré « modèle de Singapour » : visuel (bar model, number bond…) + pastille méthode."""
    n = f'<div class="sg-note">{note}</div>' if note else ''
    return f'<div class="sg-box">{sg_pill()}{content}{n}</div>'


def draw_model(h=16, hint='أرسم نموذج الشريط بنفسي ثم أحسب:'):
    """Zone où l'élève dessine SON modèle en barres (étape « je dessine » de Singapour).
    Minimum 12 mm imposé (règle « un vrai cahier pour écrire ») — un modèle a besoin de place."""
    return f'<div class="sg-draw" style="height:{max(h, 12)}mm"><div class="sg-draw-h">{hint}</div></div>'


def number_bond(whole, parts, w=32):
    """Schéma partie-tout (number bond) : cercle du tout en haut, branches vers les parties.
    whole/parts = textes ; '؟' s'affiche en rouge (l'inconnue à trouver)."""
    n = len(parts)
    VW, VH = 40, 26
    cxw, cyw, rw = VW / 2, 6.2, 5.6
    rp, cyp = 4.8, VH - 5.2
    els = []
    for i, p in enumerate(parts):
        cx = (i + 1) * VW / (n + 1)
        els.append(f'<line x1="{cxw}" y1="{cyw}" x2="{cx:.1f}" y2="{cyp}" stroke="#8a4a12" stroke-width=".55"/>')
    def circ(cx, cy, r, txt, fill):
        unk = txt == '؟'
        return (f'<circle cx="{cx:.1f}" cy="{cy}" r="{r}" fill="{fill}" stroke="#2b2b2b" stroke-width=".7"'
                f'{" stroke-dasharray=\"1.6 1\"" if unk else ""}/>'
                f'<text x="{cx:.1f}" y="{cy + 1.5}" text-anchor="middle" font-size="{4.6 if unk else 3.6}" '
                f'font-weight="900" fill="{"#c0392b" if unk else "#26303c"}">{txt}</text>')
    for i, p in enumerate(parts):
        els.append(circ((i + 1) * VW / (n + 1), cyp, rp, p, '#aae4f0'))
    els.append(circ(cxw, cyw, rw, whole, '#ffd98c'))
    return (f'<svg width="{w}mm" height="{w * VH / VW:.1f}mm" viewBox="0 0 {VW} {VH}" '
            f'style="overflow:visible;display:block;margin:0 auto">{"".join(els)}</svg>')


DISC_COLORS = {'1': '#ffd98c', '10': '#ffc7ba', '100': '#c6e9a4', '1000': '#aae4f0', '10000': '#e6c7f2'}


PLACE_NAMES = {'1': 'الآحاد', '10': 'العشرات', '100': 'المئات',
               '1000': 'الآلاف', '10000': 'عشرات الآلاف'}


def place_discs(groups, caption=''):
    """Mini-جدول المنازل en disques : une colonne par position (en-tête coloré, grands→petits
    de gauche à droite comme l'écriture du nombre), disques empilés, et LE CHIFFRE à écrire
    en bas de la colonne. count=0 → disque vide pointillé + chiffre 0 (le zéro se voit)."""
    cols = []
    for val, cnt in groups:
        col = DISC_COLORS.get(val, '#fff')
        if cnt:
            discs = ''.join(f'<span class="disc" style="background:{col}">{val}</span>' for _ in range(cnt))
        else:
            discs = f'<span class="disc empty">{val}</span>'
        cols.append(f'''<div class="pd-col">
          <div class="pd-head" style="background:{col}">{PLACE_NAMES.get(val, val)}</div>
          <div class="pd-discs">{discs}</div>
          <div class="pd-digit">{cnt}</div>
        </div>''')
    cap = f'<div class="sg-note">{caption}</div>' if caption else ''
    return f'<div class="pd-row">{"".join(cols)}</div>{cap}'


def obj_groups(n_groups, per_group, emoji='🌴'):
    """Groupes concrets (assiettes d'objets) : le « محسوس » de Singapour — n groupes égaux."""
    g = f'<div class="og">{("<span>" + emoji + "</span>") * per_group}</div>'
    return f'<div class="og-row">{g * n_groups}</div>'


def bar_compare(a_label, a_val, b_label, b_val, w=100, diff_label='؟', unit=''):
    """Modèle de comparaison : deux barres alignées, l'écart marqué d'une accolade « ؟ »."""
    big, small = max(a_val, b_val), min(a_val, b_val)
    x0 = 24
    x1 = w - 3
    scale = (x1 - x0) / big
    bh, y_a, y_b = 6.5, 2, 10.5
    wa, wb = a_val * scale, b_val * scale
    els = [
        # direction="ltr" EXPLICITE sur les étiquettes : le svg hérite du direction:rtl du
        # document, ce qui inverse l'ancrage et fait filer le texte sous la barre (bug u8_p1).
        # Avec ltr + text-anchor="end", le bord droit du texte s'arrête à 1,5 mm de la barre.
        f'<text x="{x0 - 1.5}" y="{y_a + bh / 2 + 1.3}" text-anchor="end" direction="ltr" style="direction:ltr" font-size="3.2" font-weight="900" fill="#5c5238">{a_label}</text>',
        f'<rect x="{x0}" y="{y_a}" width="{wa:.1f}" height="{bh}" fill="#8fd4e8" stroke="#2b2b2b" stroke-width=".7"/>',
        f'<text x="{x0 + wa / 2:.1f}" y="{y_a + bh / 2 + 1.3}" text-anchor="middle" font-size="3.4" font-weight="900" fill="#26303c">{a_val:g}{(" " + unit) if unit else ""}</text>',
        f'<text x="{x0 - 1.5}" y="{y_b + bh / 2 + 1.3}" text-anchor="end" direction="ltr" style="direction:ltr" font-size="3.2" font-weight="900" fill="#5c5238">{b_label}</text>',
        f'<rect x="{x0}" y="{y_b}" width="{wb:.1f}" height="{bh}" fill="#f5b34c" stroke="#2b2b2b" stroke-width=".7"/>',
        f'<text x="{x0 + wb / 2:.1f}" y="{y_b + bh / 2 + 1.3}" text-anchor="middle" font-size="3.4" font-weight="900" fill="#26303c">{b_val:g}{(" " + unit) if unit else ""}</text>',
        f'<line x1="{x0 + small * scale:.1f}" y1="1" x2="{x0 + small * scale:.1f}" y2="{y_b + bh + 1}" stroke="#8a4a12" stroke-width=".4" stroke-dasharray="1.2 .9"/>',
    ]
    ya = y_a if a_val < b_val else y_b  # barre la plus courte → accolade de l'écart à sa hauteur
    els.append(f'<path d="M{x0 + small * scale:.1f},{ya - .8} L{x0 + big * scale:.1f},{ya - .8}" fill="none" stroke="#c0392b" stroke-width=".6"/>' if ya == y_b else
               f'<path d="M{x0 + small * scale:.1f},{y_b + bh + 1.8} L{x0 + big * scale:.1f},{y_b + bh + 1.8}" fill="none" stroke="#c0392b" stroke-width=".6"/>')
    mid_diff = x0 + (small + big) / 2 * scale
    y_txt = (ya - 2 if ya == y_b else y_b + bh + 5.4)
    els.append(f'<text x="{mid_diff:.1f}" y="{y_txt}" text-anchor="middle" font-size="4.2" font-weight="900" fill="#c0392b">{diff_label}</text>')
    H = y_b + bh + 7
    return (f'<div style="width:{w}mm;margin:.6mm auto"><svg width="{w}mm" height="{H}mm" '
            f'viewBox="0 0 {w} {H}" style="overflow:visible;display:block">{"".join(els)}</svg></div>')


def mult_area(tens, units, mult, w=52):
    """Modèle en aire de la multiplication posée : (dizaines + unités) × mult,
    produits partiels dans les cases — le « pourquoi » du calcul en colonnes."""
    VW, VH = 60, 22
    x0, y0, bh = 8, 5, 12
    wt = (VW - x0 - 2) * .68
    wu = (VW - x0 - 2) * .32
    pt, pu = tens * mult, units * mult
    els = [
        f'<text x="{x0 + wt / 2:.1f}" y="3.6" text-anchor="middle" font-size="3.6" font-weight="900" fill="#1f5566">{tens}</text>',
        f'<text x="{x0 + wt + wu / 2:.1f}" y="3.6" text-anchor="middle" font-size="3.6" font-weight="900" fill="#8a3d2a">{units}</text>',
        f'<text x="{x0 - 2.5}" y="{y0 + bh / 2 + 1.4}" text-anchor="middle" font-size="3.6" font-weight="900" fill="#33591f">×{mult}</text>',
        f'<rect x="{x0}" y="{y0}" width="{wt:.1f}" height="{bh}" fill="#aae4f0" stroke="#2b2b2b" stroke-width=".7"/>',
        f'<rect x="{x0 + wt:.1f}" y="{y0}" width="{wu:.1f}" height="{bh}" fill="#ffc7ba" stroke="#2b2b2b" stroke-width=".7"/>',
        f'<text x="{x0 + wt / 2:.1f}" y="{y0 + bh / 2 + 1.5}" text-anchor="middle" font-size="4" font-weight="900" fill="#26303c">{tens} × {mult} = {pt}</text>',
        f'<text x="{x0 + wt + wu / 2:.1f}" y="{y0 + bh / 2 + 1.5}" text-anchor="middle" font-size="4" font-weight="900" fill="#26303c">{pu}</text>',
        f'<text x="{VW / 2}" y="{y0 + bh + 4.2}" text-anchor="middle" font-size="3.8" font-weight="900" fill="#2f8f5b">{pt} + {pu} = {pt + pu}</text>',
    ]
    return (f'<svg width="{w}mm" height="{w * VH / VW:.1f}mm" viewBox="0 0 {VW} {VH}" '
            f'style="overflow:visible;display:block;margin:0 auto;direction:ltr">{"".join(els)}</svg>')


def container_svg(brut, net, tare, w=64):
    """Caisse avec contenu : accolade كتلة قائمة (brut) = صافية (net) + فارغ (tare)."""
    VW, VH = 80, 34
    parts = [
        # contenu (المنتوج)
        f'<rect x="32" y="11" width="16" height="18" fill="#ffd98c"/>',
        f'<path d="M33.5,14 h4 M39,17 h5 M34,21 h6 M41,24 h4" stroke="#e0a53f" stroke-width=".7" stroke-linecap="round"/>',
        # parois de la caisse (الغلاف)
        f'<rect x="29.5" y="5" width="2.5" height="26" fill="#b97a33" stroke="#8a4a12" stroke-width=".4"/>',
        f'<rect x="48" y="5" width="2.5" height="26" fill="#b97a33" stroke="#8a4a12" stroke-width=".4"/>',
        f'<rect x="29.5" y="28.5" width="21" height="2.5" fill="#b97a33" stroke="#8a4a12" stroke-width=".4"/>',
        # accolade gauche = الكتلة القائمة (caisse + contenu)
        f'<path d="M28.3,5 Q26.8,5 26.8,6.7 L26.8,16.3 Q26.8,18 25.3,18 Q26.8,18 26.8,19.7 L26.8,29.3 Q26.8,31 28.3,31" fill="none" stroke="#8a4a12" stroke-width=".55"/>',
        f'<text x="13" y="14.5" text-anchor="middle" font-size="3.2" font-weight="900" fill="#8a4a12">الكتلة القائمة</text>',
        f'<text x="13" y="19.5" text-anchor="middle" font-size="3.6" font-weight="900" fill="#26303c">{brut}</text>',
        # étiquette الصافية → contenu
        f'<line x1="44" y1="12.5" x2="55" y2="8.5" stroke="#33591f" stroke-width=".45"/>',
        f'<text x="66" y="7.6" text-anchor="middle" font-size="3.2" font-weight="900" fill="#33591f">الكتلة الصافية</text>',
        f'<text x="66" y="12" text-anchor="middle" font-size="3.4" font-weight="900" fill="#26303c">{net}</text>',
        # étiquette الفارغ → paroi
        f'<line x1="46" y1="29.7" x2="55" y2="26.8" stroke="#b03434" stroke-width=".45"/>',
        f'<text x="66" y="25" text-anchor="middle" font-size="3.2" font-weight="900" fill="#b03434">الفارغ (الغلاف)</text>',
        f'<text x="66" y="29.4" text-anchor="middle" font-size="3.4" font-weight="900" fill="#26303c">{tare}</text>',
    ]
    return (f'<svg width="{w}mm" height="{w * VH / VW:.1f}mm" viewBox="0 0 {VW} {VH}" '
            f'style="overflow:visible;display:block;margin:0 auto">{"".join(parts)}</svg>')


def balance_svg(left_label, right_label, w=46):
    """Balance à deux plateaux équilibrée (ميزان) avec étiquettes sur les plateaux."""
    VW, VH = 52, 29
    def pan(cx, lab):
        return (f'<line x1="{cx}" y1="7" x2="{cx - 6}" y2="13.5" stroke="#33475e" stroke-width=".5"/>'
                f'<line x1="{cx}" y1="7" x2="{cx + 6}" y2="13.5" stroke="#33475e" stroke-width=".5"/>'
                f'<path d="M{cx - 7},13.5 L{cx + 7},13.5 L{cx + 5},18 L{cx - 5},18 Z" fill="#aae4f0" stroke="#1f5566" stroke-width=".6"/>'
                f'<text x="{cx}" y="16.7" text-anchor="middle" font-size="2.7" font-weight="900" fill="#26303c">{lab}</text>')
    parts = [
        f'<line x1="8" y1="7" x2="44" y2="7" stroke="#33475e" stroke-width="1.2" stroke-linecap="round"/>',
        f'<line x1="26" y1="7" x2="26" y2="24" stroke="#8a6d3b" stroke-width="1.4"/>',
        f'<rect x="19" y="24" width="14" height="2.4" rx="1.2" fill="#8a6d3b"/>',
        f'<circle cx="26" cy="7" r="1.3" fill="#e2504c"/>',
        pan(8, left_label), pan(44, right_label),
        f'<text x="26" y="17.5" text-anchor="middle" font-size="4.6" font-weight="900" fill="#c0392b">=</text>',
    ]
    return (f'<svg width="{w}mm" height="{w * VH / VW:.1f}mm" viewBox="0 0 {VW} {VH}" '
            f'style="overflow:visible;display:block;margin:0 auto">{"".join(parts)}</svg>')


def grid100_svg(shaded, w=24, fill='#f5b34c'):
    """Grille 10×10, `shaded` cases coloriées (pour les %) — remplies de droite à gauche (RTL)."""
    cell, k, parts = 3, 0, []
    for r in range(10):
        for c in range(10):
            x = 30 - (c + 1) * cell  # départ en haut à droite
            parts.append(f'<rect x="{x}" y="{r * cell}" width="{cell}" height="{cell}" '
                         f'fill="{fill if k < shaded else "#fff"}" stroke="#c9bfa8" stroke-width=".25"/>')
            k += 1
    parts.append('<rect x="0" y="0" width="30" height="30" fill="none" stroke="#2b2b2b" stroke-width=".8"/>')
    return (f'<svg width="{w}mm" height="{w}mm" viewBox="-.5 -.5 31 31" '
            f'style="overflow:visible;display:block;margin:0 auto">{"".join(parts)}</svg>')


def area_grid(rows_frac, cols_frac, w=32):
    """Rectangle quadrillé pour ضرب الكسور : rows_frac=(a,b) colore a/b des lignes,
    cols_frac=(c,d) colore c/d des colonnes (côté droit, sens RTL), intersection soutenue."""
    a, b = rows_frac
    c, d = cols_frac
    VW, VH = 36, 24
    ch, cw = VH / b, VW / d
    parts = []
    for r in range(b):
        for col in range(d):
            in_r, in_c = r < a, col >= d - c
            fill = '#f28a15' if (in_r and in_c) else ('#aae4f0' if in_r else ('#ffd98c' if in_c else '#fff'))
            parts.append(f'<rect x="{col * cw:.2f}" y="{r * ch:.2f}" width="{cw:.2f}" height="{ch:.2f}" '
                         f'fill="{fill}" stroke="#8a7a5c" stroke-width=".3"/>')
    parts.append(f'<rect x="0" y="0" width="{VW}" height="{VH}" fill="none" stroke="#2b2b2b" stroke-width=".8"/>')
    return (f'<svg width="{w}mm" height="{w * VH / VW:.1f}mm" viewBox="-.5 -.5 {VW + 1} {VH + 1}" '
            f'style="overflow:visible;display:block;margin:0 auto">{"".join(parts)}</svg>')


def flow_chips(steps, note=''):
    """Chaîne d'étapes RTL (schéma de leçon sciences) : bulles emoji+texte reliées de flèches."""
    chips = []
    for i, (emo, lab) in enumerate(steps):
        chips.append(f'''<div style="background:#fff;border:1.3px solid #d8c9a4;border-radius:2.6mm;padding:1.2mm 1.6mm;text-align:center;flex:1">
          <div style="font-size:12px;line-height:1.1">{emo}</div>
          <div style="font-size:8px;font-weight:900;color:#4a3a1c;line-height:1.45;margin-top:.4mm">{lab}</div>
        </div>''')
        if i < len(steps) - 1:
            chips.append('<div style="font-size:11px;font-weight:900;color:#f28a15;flex-shrink:0">⬅</div>')
    n = f'<div class="sg-note">{note}</div>' if note else ''
    return f'<div style="display:flex;gap:1.4mm;align-items:stretch;margin:1mm 0">{"".join(chips)}</div>{n}'


def ans_cells(items, cols=3):
    """Cases de cahier alignées : chaque item (question/équation) dans sa case blanche
    avec un GRAND ovale de réponse dessous — vrai espace pour écrire."""
    cells = ''.join(f'''<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.2mm 1mm;text-align:center;font-weight:800;font-size:9.5px">
      {it}<div style="margin-top:.7mm"><span class="oval" style="min-width:17mm;height:5.8mm"></span></div>
    </div>''' for it in items)
    return f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:1.8mm;margin-top:1mm">{cells}</div>'


def eq_cells(items, cols=3):
    """Cases de cahier alignées pour équations à trou (le carré de réponse est dans l'équation)."""
    cells = ''.join(f'''<div style="background:#fff;border:1.2px solid #ddd2b8;border-radius:2mm;padding:1.8mm 1mm;text-align:center;font-weight:800;font-size:9.5px;display:flex;align-items:center;justify-content:center;gap:1mm">
      {it}
    </div>''' for it in items)
    return f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:1.8mm;margin-top:1mm">{cells}</div>'


def formula(txt, color='var(--p-green)'):
    return f'<div style="background:{color};border-radius:2.4mm;padding:1.1mm 2.8mm;font-weight:900;font-size:9px;margin:.45mm 0;text-align:center;line-height:1.35">{txt}</div>'


def self_eval(note=''):
    return f'''<div class="self-eval">
      <span>قيّم نفسك:</span>
      <span class="se-item"><span class="se-box"></span> فهمتُ جيدًا</span>
      <span class="se-item"><span class="se-box"></span> أحتاج مراجعة</span>
      <span class="se-item"><span class="se-box"></span> أحتاج مساعدة</span>
      <span style="font-size:7px;color:#8a7a5c">{note}</span>
    </div>'''


def edge_band(part):
    """Bande de tranche colorée : 'math' (orange-doré) ou 'sci' (vert)."""
    if not part:
        return ''
    lab = 'الرياضيات' if part == 'math' else 'العلوم'
    return f'<div class="edge edge-{part}"><span>{lab}</span></div>'


def page(num, title, body, unit_label='', with_eval=False, part=''):
    ev = self_eval() if with_eval else ''
    chip = f'<div style="text-align:center"><span class="unit-chip">{unit_label}</span></div>' if unit_label else ''
    qr = ''
    m = re.search(r'(<div class="qr-corr"[^>]*>.*?</div>)', body, flags=re.S)
    if m:
        qr = m.group(1)
        body = body[:m.start()] + body[m.end():]
    body = print_sanitize(body)
    title = print_sanitize(title)
    unit_label = print_sanitize(unit_label)
    qr_reserve = '<div class="qr-reserve" aria-hidden="true"></div>' if qr else ''
    return f'''<div class="sheet">
  <div class="sheet-inner">
    <div class="head">
      {logo_img('logo')}
      <div class="brand-text">
        <div class="brand-title">دفتر ماجور</div>
        <div class="brand-sub">الرياضيات والعلوم · السنة السادسة الأساسية 6AF</div>
      </div>
    </div>
    {chip}
    <h2 class="lesson-title">{title}</h2>
    {body}
    {ev}
    {qr_reserve}
  </div>
  {qr}
  {edge_band(part)}
  <div class="page-footer"><span>دفتر ماجور · الرياضيات والعلوم</span><span>السنة السادسة الأساسية 6AF</span></div>
  <div class="pageno {part}">{num}</div>
</div>'''


def unit_banner(num, title, sub, color):
    return f'''<div class="unit-banner" style="background:{color}">
      <span class="unum">{num}</span>
      <div><b>{title}</b><small>{sub}</small></div>
    </div>'''
