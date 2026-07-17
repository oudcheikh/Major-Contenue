# -*- coding: utf-8 -*-
"""Base du cahier A5 : CSS + gabarits + composants (style pptx Major, format A5 148×210)."""
import json, math, os

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
  background:linear-gradient(180deg,#e9e0cf 0%,#e0d4bd 100%);
  color:var(--ink);font-size:13.5px;direction:rtl;
}
/* ═══ FEUILLE A5 ═══ */
.sheet{
  width:148mm;height:210mm;margin:16px auto;background:var(--cream);
  position:relative;overflow:hidden;border-radius:10px;
  box-shadow:0 14px 34px rgba(15,23,42,.18);
  display:flex;flex-direction:column;
}
.sheet-inner{flex:1;padding:3.8mm 6mm 14mm;display:flex;flex-direction:column;min-height:0}
/* entête */
.head{display:flex;justify-content:space-between;align-items:center;margin-bottom:1.2mm}
.head .doc-id{font-size:6.8px;color:var(--muted);font-weight:700;text-align:right;line-height:1.45}
.lesson-title{
  text-align:center;color:var(--orange);font-weight:900;font-size:14.5px;
  margin:0 0 2mm;line-height:1.25;text-wrap:balance;
}
.unit-chip{
  display:inline-block;font-size:7.5px;font-weight:900;color:#6b5327;
  background:#fdf1d7;border:1px solid #e6cc93;border-radius:999px;padding:1px 8px;margin-bottom:1mm;
}
/* bande de tranche : distingue partie رياضيات / partie علوم (bord extérieur = gauche en RTL) */
.edge{position:absolute;left:0;top:0;bottom:0;width:3.4mm;z-index:3}
.edge-math{background:linear-gradient(180deg,#f28a15 0%,#ffc84d 100%)}
.edge-sci{background:linear-gradient(180deg,#1e9e57 0%,#7fd490 100%)}
.edge span{
  position:absolute;top:7mm;left:50%;transform:translateX(-50%) rotate(0deg);
  writing-mode:vertical-rl;font-size:6.5px;font-weight:900;color:#fff;letter-spacing:1px;
}
/* carte QR correction (coin bas-gauche, dans la zone du pied de page) */
.qr-corr{
  position:absolute;left:5.5mm;bottom:1.2mm;z-index:4;width:11.6mm;
  background:#fff;border:1.2px solid;border-radius:1.8mm;padding:.6mm .6mm .5mm;
  text-align:center;box-shadow:0 1.5px 4px rgba(15,23,42,.22);
}
.qr-corr img{width:9.8mm;height:9.8mm;display:block;margin:0 auto}
.qr-corr span{display:block;font-size:4.4px;font-weight:900;line-height:1.25;margin-top:.3mm}
/* vague bleue */
.wave{position:absolute;left:0;right:0;bottom:0;height:11mm;pointer-events:none}
.wave svg{position:absolute;inset:0;width:100%;height:100%}
/* numéro de page façon cahier arabe : cercle blanc cerclé couleur matière, centré */
.pageno{
  position:absolute;left:50%;transform:translateX(-50%);bottom:1.2mm;
  min-width:6.5mm;height:6.5mm;border-radius:999px;background:#fff;
  border:.5mm solid #f28a15;display:flex;align-items:center;justify-content:center;
  font-size:8.5px;font-weight:900;color:#26303c;z-index:4;
  font-variant-numeric:tabular-nums;padding:0 1mm;
}
.pageno.sci{border-color:#1e9e57}
.page-footer{
  position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;
  align-items:flex-end;padding:0 4mm 1.6mm 20mm;font-size:5.6px;color:var(--muted);font-weight:700;
}
/* ═══ BADGES (carton jaune + mascotte) ═══ */
.badge-row{display:flex;align-items:flex-end;gap:2.6mm;margin:2mm 0 1.4mm}
.badge{
  background:linear-gradient(180deg,#ffe27a,#ffc84d);
  color:var(--yellow-text);font-weight:900;font-size:11px;
  padding:3px 16px;border-radius:999px;
  box-shadow:0 2px 6px rgba(138,74,18,.18);
}
.badge small{display:block;font-size:7px;font-weight:700;color:#a3662b}
.badge-row .mascot{width:11.5mm;height:10.5mm}
/* ═══ CADRE BLANC ═══ */
.frame{
  background:var(--frame);border:1.2px solid #e7dfcc;border-radius:3.5mm;
  padding:2.8mm 3.6mm;position:relative;
  box-shadow:0 3px 8px rgba(120,100,60,.07);
}
.frame ul{margin:0;padding-right:4mm;padding-left:0;line-height:1.72;font-size:12.5px;font-weight:600}
.frame ul li::marker{color:var(--orange)}
.frame .hl{color:#c0392b;font-weight:900}
.frame.has-video{padding-left:29mm;min-height:24mm}
.video-box{position:absolute;left:2.6mm;bottom:2.4mm;width:24mm;text-align:center;direction:ltr}
.video-box .nuage-bg{width:100%;height:9.5mm;position:relative}
.video-box .nuage-bg span{
  position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  font-size:6.8px;font-weight:900;color:#b3541e;transform:rotate(-6deg);
}
.video-box .qr{width:12.5mm;height:12.5mm;margin-top:.8mm}
/* bulle crantée */
.scallop{
  background:#fff;border:1.8px dotted #d98a95;border-radius:3.5mm;padding:1.8mm 3.4mm;
  font-size:11.3px;font-weight:700;line-height:1.6;position:relative;margin:1.6mm 0 0;
}
.scallop:before,.scallop:after{
  content:"";position:absolute;top:-1.5mm;width:3mm;height:3mm;border-radius:50%;
  background:#e8a9b4;border:1px solid #c37a88;
}
.scallop:before{right:5mm}.scallop:after{left:5mm}
/* exemple encadré vert */
.exemple{
  background:#f2f8ee;border:1.4px dashed #8fb87a;border-radius:3mm;
  padding:1.8mm 3.2mm;font-size:11.5px;font-weight:700;line-height:1.65;margin:1.6mm 0 0;
}
.exemple b.tag{color:#33591f}
/* ═══ EXERCICES : jetons rouges ═══ */
.exo{padding:.7mm 0 1.2mm;break-inside:avoid}
.exo-head{display:flex;align-items:center;gap:2mm;margin-bottom:.9mm}
.tok{
  position:relative;width:6.2mm;height:6.2mm;background:var(--red);border-radius:50%;
  display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;
  color:#fff;font-weight:900;font-size:9.5px;
  box-shadow:0 1.6px 3px rgba(197,48,48,.35);
}
.tok:after{
  content:"";position:absolute;left:-1.9mm;top:50%;transform:translateY(-50%);
  border:1.6mm solid transparent;border-right:2.4mm solid var(--red);border-left:none;
}
.tok i{
  position:absolute;inset:.9mm;border-radius:50%;background:#fdeee0;font-style:normal;
  display:flex;align-items:center;justify-content:center;color:#c0392b;
}
.lvl{font-size:6.8px;font-weight:900;color:#7a6a45;background:#fdf1d7;border-radius:999px;padding:1px 6px}
.exo-q{font-size:12px;font-weight:700;line-height:1.62}
.consigne{
  display:flex;align-items:center;gap:2mm;
  font-size:12.0px;font-weight:900;color:#8a4a12;margin:1.6mm 0 1mm;
}
.consigne .tok{width:5.6mm;height:5.6mm;font-size:8.5px}
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
  border:1.6px dashed var(--red);border-radius:3mm;background:#fff;
  min-height:12mm;margin-top:1.2mm;position:relative;
}
.dashcard.tall{min-height:20mm}
.dotl{border-bottom:1.8px dotted #a8b0bd;height:7.4mm}
.dots{margin-top:.8mm}
/* colonnes d'exercices (séparateur pptx) */
.cols{display:grid;grid-template-columns:1fr 1fr;gap:2.4mm 5mm;position:relative;margin-top:1.4mm}
.cols:before{content:"";position:absolute;top:1mm;bottom:1mm;left:50%;width:1.4px;background:#2b2b2b;opacity:.65}
.cols.nosep:before{display:none}
/* ═══ opérations posées ═══ */
.vgrid{display:grid;gap:1.8mm;margin-top:1.4mm}
.vop{
  direction:ltr;background:#fff;border:1.3px solid #ddd2b8;border-radius:2.4mm;
  padding:1.4mm 2.6mm 4.5mm;font-size:11px;font-weight:800;text-align:right;
  line-height:1.5;font-variant-numeric:tabular-nums;
}
.vop .vline{display:block;border-top:1.8px solid #33475e;margin-top:.7mm;height:5mm}
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
.fx{display:flex;align-items:center;gap:1.6mm;justify-content:center;background:#fff;border:1.2px solid #e2d8c0;border-radius:2.2mm;padding:1.6mm 1mm;font-size:10.5px;min-width:0}
.vgrid>*{min-width:0}
/* ═══ droite numérique ═══ */
.numline{direction:ltr;margin:1mm auto}
/* ═══ auto-évaluation ═══ */
.self-eval{
  display:flex;align-items:center;justify-content:space-between;gap:2mm;
  margin-top:auto;margin-bottom:1.6mm;padding:1.2mm 3mm;border-radius:2mm;background:#fffdf6;
  border:1.2px dashed #cdbf9d;font-size:7.2px;font-weight:800;color:#5c5238;position:relative;z-index:2;
}
.se-item{display:flex;align-items:center;gap:1.4mm}
.se-box{width:3.4mm;height:3.4mm;border:1.4px solid #8a7a5c;border-radius:.8mm;background:#fff}
/* ═══ KIT PÉDAGOGIQUE : objectifs · méthode · astuce · piège · défi · bulle ═══ */
.objectifs{
  background:linear-gradient(135deg,#eaf4fb,#eef8ee);border:1.4px solid #b5d5e8;
  border-radius:3mm;padding:2mm 3.2mm;margin:0 0 1.8mm;
}
.objectifs .obj-t{font-weight:900;font-size:12px;color:#1f5e8d;margin-bottom:.8mm}
.objectifs ul{margin:0;padding:0;list-style:none;font-size:11px;font-weight:700;line-height:1.68;color:#2c3e50}
.objectifs li:before{content:"☐";color:#2f6ea5;margin-left:1.8mm}
.methode{background:#fff;border:1.4px solid #cfe0ee;border-radius:3mm;padding:1.8mm 3mm;margin:1.4mm 0}
.methode .m-t{font-weight:900;font-size:11.5px;color:#1f5e8d;margin-bottom:.6mm}
.methode .step{display:flex;gap:2mm;align-items:flex-start;padding:.55mm 0;font-size:11.5px;font-weight:700;line-height:1.55}
.methode .sn{
  width:4.8mm;height:4.8mm;border-radius:50%;background:var(--blue);color:#fff;flex-shrink:0;
  display:inline-flex;align-items:center;justify-content:center;font-weight:900;font-size:8px;margin-top:.2mm;
}
.astuce{
  display:flex;gap:2.2mm;align-items:flex-start;background:#fdf8e3;border:1.4px solid #e6cc93;
  border-radius:3mm;padding:1.8mm 2.8mm;margin:1.4mm 0;font-size:11px;font-weight:700;line-height:1.6;
}
.astuce .ico{font-size:12px;line-height:1;flex-shrink:0;margin-top:.4mm}
.astuce b{color:#8a4a12}
.attention{
  display:flex;gap:2.2mm;align-items:flex-start;background:#fdeeee;border:1.4px solid #e3a6a6;
  border-radius:3mm;padding:1.8mm 2.8mm;margin:1.4mm 0;font-size:11px;font-weight:700;line-height:1.6;
}
.attention .ico{font-size:12px;line-height:1;flex-shrink:0;margin-top:.4mm}
.attention b{color:#b03434}
.defi{
  background:linear-gradient(135deg,#fff3d6,#ffe8c2);border:1.6px solid #e8b45a;border-radius:3mm;
  padding:2mm 3mm;margin:1.6mm 0;position:relative;
}
.defi .d-t{font-weight:900;font-size:12px;color:#a05e10;margin-bottom:.6mm}
.defi .d-q{font-size:11.5px;font-weight:700;line-height:1.6}
.bulle-row{display:flex;gap:2mm;align-items:flex-end;margin:1.4mm 0}
.bulle-row .im{width:12mm;height:11mm;flex-shrink:0}
.bulle{
  position:relative;background:#fff;border:1.5px solid #a8cfe0;border-radius:3mm;
  padding:1.8mm 3mm;font-size:11.3px;font-weight:700;line-height:1.6;flex:1;
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
/* ═══ couverture & sommaire ═══ */
.cover .sheet-inner{justify-content:center;align-items:center;text-align:center}
.cover h1{font-size:34px;color:var(--orange);font-weight:900;margin:3mm 0 1mm}
.cover .sub{font-size:11px;font-weight:800;color:#6b5d3f;margin:0 0 4mm}
.cover-band{display:flex;gap:2mm;flex-wrap:wrap;justify-content:center;margin-bottom:3.5mm}
.cover-band span{background:#fff;border:1.2px solid #e0d3b3;border-radius:999px;padding:1.2mm 3.4mm;font-size:7.6px;font-weight:900;color:#7c4a12}
.cover-cards{display:grid;grid-template-columns:1fr 1fr;gap:2.4mm;width:120mm;margin:1mm 0 3mm}
.cover-card{border-radius:3.5mm;padding:2.8mm 3.4mm;text-align:right;border:1.2px solid rgba(0,0,0,.08)}
.cover-card b{font-size:9.8px;display:block;margin-bottom:.6mm}
.cover-card span{font-size:7.4px;line-height:1.55;color:#4b5563;display:block}
.cover-mascots{display:flex;gap:6mm;align-items:flex-end;justify-content:center;margin-top:1.5mm}
.cover-mascots .im{width:19mm;height:16.5mm}
.cover-logo{width:23mm;height:23mm;border-radius:4.5mm;box-shadow:0 6px 16px rgba(120,90,40,.25)}
.owner-line{
  width:110mm;background:#fff;border:1.4px solid #e0d3b3;border-radius:999px;
  padding:1.8mm 5mm;font-size:9px;font-weight:800;color:#6b5327;margin-top:3mm;
  display:flex;gap:2mm;align-items:center;
}
.owner-line i{flex:1;border-bottom:1.6px dotted #b9a06a;height:4mm;font-style:normal}
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
.figcap{text-align:center;font-size:8.8px;font-weight:700;color:#8a6d3b;margin-top:.8mm}
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
.im{{display:inline-block;background-repeat:no-repeat;background-position:center;background-size:contain}}
.im-fille{{background-image:url("{ASSETS['fille']}")}}
.im-garcon{{background-image:url("{ASSETS['garcon']}")}}
.im-nuage{{background-image:url("{ASSETS['nuage']}")}}
.im-qr{{background-image:url("{ASSETS['qr']}");image-rendering:pixelated}}
.im-logo{{background-image:url("{ASSETS['logo']}")}}
.head .logo{{width:10mm;height:10mm;border-radius:2mm}}
"""

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


def exo(n, lvl, body):
    lv = f'<span class="lvl">{lvl}</span>' if lvl else ''
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
    return f'<div class="objectifs"><div class="obj-t">🎯 في هذه الوحدة سأتعلّم:</div><ul>{lis}</ul></div>'


def methode(title, steps):
    """Méthode pas-à-pas numérotée (2-4 étapes courtes)."""
    rows = ''.join(f'<div class="step"><span class="sn">{i + 1}</span><span>{s}</span></div>'
                   for i, s in enumerate(steps))
    return f'<div class="methode"><div class="m-t">🧭 {title}</div>{rows}</div>'


def astuce(txt):
    """Conseil malin du prof (1-2 lignes)."""
    return f'<div class="astuce"><span class="ico">💡</span><span><b>أستاذ ماجور ينصح:</b> {txt}</span></div>'


def attention(txt):
    """Erreur fréquente à éviter (1-2 lignes)."""
    return f'<div class="attention"><span class="ico">⚠️</span><span><b>انتبه للخطأ الشائع:</b> {txt}</span></div>'


def defi(txt):
    """Défi des champions en fin d'unité."""
    return f'<div class="defi"><div class="d-t">🏆 تحدّي الأبطال</div><div class="d-q">{txt}</div></div>'


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
    sub = ''.join('<th style="font-size:5.6px">مئات</th><th style="font-size:5.6px">عشرات</th><th style="font-size:5.6px">آحاد</th>' for _ in use)
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
    return f'''<div class="fx">{FR(a,b)}<b>{op}</b>{FR(c,d)}<b>=</b><span class="oval s" style="min-width:8mm;height:5mm"></span></div>'''


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
    lab = ('<line x1="13" y1="10" x2="22" y2="10" stroke="#c0392b" stroke-width=".7"/>'
           '<text x="17.5" y="8.8" text-anchor="middle" font-size="2.6" font-weight="900" fill="#c0392b">نق</text>'
           '<line x1="4" y1="14" x2="22" y2="14" stroke="#2f6ea5" stroke-width=".7"/>'
           '<text x="13" y="17.5" text-anchor="middle" font-size="2.6" font-weight="900" fill="#2f6ea5">القطر</text>') if labels else ''
    return f'''<svg width="{w}mm" height="{h}mm" viewBox="0 0 26 22" style="overflow:visible;display:block;margin:0 auto">
      <circle cx="13" cy="10" r="9" fill="#fffdf6" stroke="#2b2b2b" stroke-width=".9"/>
      <circle cx="13" cy="10" r=".8" fill="#2b2b2b"/>{lab}</svg>'''


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
    y0 = 7.6 if stagger else 5.0
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
        yn = 3.0 if rows[i] == 0 else 6.2
        segs.append(f'<rect x="{x:.1f}" y="{y0}" width="{sw:.1f}" height="{bh}" fill="{col}" stroke="#2b2b2b" stroke-width=".7"{" stroke-dasharray=\"1.6 1\"" if unknown else ""}/>')
        segs.append(f'<text x="{xc:.1f}" y="{y0 + bh / 2 + 1.3:.1f}" text-anchor="middle" font-size="{4.2 if unknown else 3.4}" font-weight="900" fill="{"#c0392b" if unknown else "#26303c"}">{shown}</text>')
        segs.append(f'<text x="{xc:.1f}" y="{yn:.1f}" text-anchor="middle" direction="rtl" font-size="3.0" font-weight="900" fill="#5c5238">{lab}</text>')
        segs.append(f'<line x1="{xc:.1f}" y1="{yn + .7:.1f}" x2="{xc:.1f}" y2="{y0 - .3:.1f}" stroke="#a8b0bd" stroke-width=".35"/>')
        x += sw
    yb, d, mid = y0 + bh + 1.1, 1.7, (x0 + x1) / 2
    brace = (f'<path d="M{x0},{yb} Q{x0},{yb + d} {x0 + d},{yb + d} L{mid - d:.1f},{yb + d} '
             f'Q{mid:.1f},{yb + d} {mid:.1f},{yb + 2 * d} Q{mid:.1f},{yb + d} {mid + d:.1f},{yb + d} '
             f'L{x1 - d},{yb + d} Q{x1},{yb + d} {x1},{yb}" fill="none" stroke="#8a4a12" stroke-width=".55"/>')
    tot = f'<text x="{mid:.1f}" y="{yb + 2 * d + 3.6:.1f}" text-anchor="middle" direction="rtl" font-size="3.5" font-weight="900" fill="#8a4a12">{total_label}</text>'
    H = yb + 2 * d + 4.9
    return (f'<div style="width:{w * scale:.1f}mm;margin:.6mm auto"><svg width="{w * scale:.1f}mm" height="{H * scale:.1f}mm" '
            f'viewBox="0 0 {w} {H:.1f}" style="overflow:visible;display:block">{"".join(segs)}{brace}{tot}</svg></div>')


def sg_pill():
    return '<span class="sg-pill">🧩 نموذج الشريط — أرسم لأفهم</span>'


def sg_box(content, note=''):
    """Encadré « modèle de Singapour » : visuel (bar model, number bond…) + pastille méthode."""
    n = f'<div class="sg-note">{note}</div>' if note else ''
    return f'<div class="sg-box">{sg_pill()}{content}{n}</div>'


def draw_model(h=16, hint='أرسم نموذج الشريط بنفسي ثم أحسب:'):
    """Zone où l'élève dessine SON modèle en barres (étape « je dessine » de Singapour).
    Minimum 12 mm imposé (règle « un vrai cahier pour écrire ») — un modèle a besoin de place."""
    return f'<div class="sg-draw" style="height:{max(h, 12)}mm"><div class="sg-draw-h">✏️ {hint}</div></div>'


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
    return f'<div style="background:{color};border-radius:2.6mm;padding:1.3mm 3.4mm;font-weight:900;font-size:9.4px;margin:.6mm 0;text-align:center">{txt}</div>'


def self_eval(note=''):
    return f'''<div class="self-eval">
      <span>📊 قيّم نفسك:</span>
      <span class="se-item"><span class="se-box"></span> فهمتُ جيدًا 😀</span>
      <span class="se-item"><span class="se-box"></span> أحتاج مراجعة 🤔</span>
      <span class="se-item"><span class="se-box"></span> أحتاج مساعدة 🙋</span>
      <span style="font-size:6.5px;color:#8a7a5c">{note}</span>
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
    return f'''<div class="sheet">
  <div class="sheet-inner">
    <div class="head">
      <div class="doc-id">دفتر ماجور · الرياضيات والعلوم<br>السنة السادسة الأساسية 6AF</div>
      <span class="im im-logo logo" role="img" aria-label="Major"></span>
    </div>
    {chip}
    <h2 class="lesson-title">{title}</h2>
    {body}
    {ev}
  </div>
  {edge_band(part)}
  <div class="page-footer"><span>دفتر ماجور · الرياضيات والعلوم</span><span>🇲🇷 السنة السادسة الأساسية 6AF</span></div>
  <div class="pageno {part}">{num}</div>
</div>'''


def unit_banner(num, title, sub, color):
    return f'''<div class="unit-banner" style="background:{color}">
      <span class="unum">{num}</span>
      <div><b>{title}</b><small>{sub}</small></div>
    </div>'''
