---
name: major-cahier-design
description: "Design et g\u00e9n\u00e9ration des Cahiers Major (PDF/HTML) pour la pr\u00e9paration au concours 6AF. Utilise ce skill d\u00e8s que l'utilisateur veut : cr\u00e9er, modifier, ou am\u00e9liorer un cahier d'exercices, g\u00e9n\u00e9rer un PDF \u00e9ducatif, travailler sur la mise en page d'un cahier, ajouter des exercices ou des le\u00e7ons, g\u00e9n\u00e9rer des QR codes, convertir HTML en PDF, cr\u00e9er du contenu imprimable pour les \u00e9l\u00e8ves. D\u00e9clenche aussi pour : \"cahier\", \"exercices\", \"PDF\", \"mise en page\", \"version papier\", \"imprimer\", \"QR code\", \"contenu 6AF\", \"concours\"."
---

# Major Cahier Design \u2014 Cr\u00e9ation de cahiers \u00e9ducatifs

Ce skill guide la cr\u00e9ation et la mise en page des **Cahiers Major 6AF**, les cahiers d'exercices physiques imprim\u00e9s pour la pr\u00e9paration au concours d'entr\u00e9e en 6\u00e8me ann\u00e9e fondamentale en Mauritanie.

## Contexte

Les cahiers Major sont le c\u0153ur physique du projet. Chaque cahier :
- Contient des le\u00e7ons, r\u00e8gles, exercices et QR codes li\u00e9s \u00e0 l'appli MajorApp
- Est g\u00e9n\u00e9r\u00e9 en HTML (source) puis converti en PDF (impression)
- Doit \u00eatre imprimable sur papier A4 avec mise en page optimis\u00e9e
- Existe en version fran\u00e7aise et arabe (RTL)

## Cahiers existants

| Cahier | Chemin | Mati\u00e8res |
|--------|--------|----------|
| Maths + Fran\u00e7ais + Sciences | `6AF-MATH-SCIENCE-FRANCAIS/` | Math\u00e9matiques, Fran\u00e7ais, Sciences naturelles |
| Arabe | `6AF-ARABE/` | Arabe, Histoire-G\u00e9ographie, Islamique |

## Architecture d'un cahier HTML

Chaque cahier est un fichier HTML autonome avec CSS int\u00e9gr\u00e9 et optimis\u00e9 pour l'impression. Voici la structure type :

### Variables CSS

```css
:root {
  --paper: #fffdf8;      /* Fond papier chaud */
  --ink: #182230;         /* Texte principal */
  --muted: #5c6776;       /* Texte secondaire */
  --shadow: 0 18px 42px rgba(15,23,42,.16);
}
```

Couleurs par mati\u00e8re :
| Mati\u00e8re | Variable | Hex |
|---------|----------|-----|
| Fran\u00e7ais | `--fr` | `#0ea5e9` |
| Math\u00e9matiques | `--ma` | `#f97316` |
| Sciences | `--sc` | `#10b981` |
| Arabe | `--ar` | `#7c3aed` |
| Histoire-G\u00e9o | `--hg` | `#b45309` |
| Islamique | `--is` | `#059669` |

### Structure de page

Chaque page du cahier est un div `.page` format\u00e9 pour A4 :

```html
<div class="page">
  <!-- Reliure lat\u00e9rale (spine) -->
  <div class="spine">
    <div class="holes">...</div>
    <span class="spine-title">MAJOR \u00b7 6AF</span>
  </div>
  
  <!-- Onglets mati\u00e8res (tabs) -->
  <div class="tabs">
    <div class="tab active" style="background: var(--fr)">FR</div>
    <div class="tab" style="background: var(--ma)">MA</div>
    <div class="tab" style="background: var(--sc)">SC</div>
  </div>
  
  <!-- Contenu principal -->
  <div class="page-main">
    <div class="page-header">
      <span class="lesson-tag">Le\u00e7on N\u00b0X</span>
      <h2>Titre de la le\u00e7on</h2>
    </div>
    <div class="page-body">
      <!-- Contenu: r\u00e8gles, exercices, QR codes -->
    </div>
    <div class="page-footer">
      <span>Cahier Major 6AF \u00b7 Mati\u00e8re</span>
    </div>
  </div>
</div>
```

### Composants de contenu

**Bo\u00eete de r\u00e8gle** :
```html
<div class="rule-box" style="border-color: var(--fr)">
  <strong>\ud83d\udccc R\u00e8gle</strong>
  <p>Texte de la r\u00e8gle...</p>
</div>
```

**Exercice** :
```html
<div class="exo-card">
  <div class="exo-header">
    <span class="exo-num">1</span>
    <span class="exo-text">Consigne de l'exercice</span>
  </div>
  <div class="lines">
    <div class="line"></div>
    <div class="line"></div>
  </div>
</div>
```

**QR Code** :
```html
<div class="scan-card">
  <div class="fake-qr"></div>
  <div class="scan-title">\ud83d\udcf1 Scanne pour le mini-cours</div>
</div>
```

Les vrais QR codes sont g\u00e9n\u00e9r\u00e9s par `generate_qrcodes.py` avec le format `major://lesson/{lessonId}`.

## R\u00e8gles de mise en page pour l'impression

### Format
- Taille : A4 portrait (210mm x 297mm)
- Marges print : 8mm
- Police arabe : Cairo (Google Fonts) ou Tahoma
- Police fran\u00e7aise : syst\u00e8me ou Calibri

### Print CSS
Le `@media print` est essentiel et doit :
- Supprimer les ombres et d\u00e9corations non imprimables
- Activer `print-color-adjust: exact` pour conserver les couleurs
- G\u00e9rer les sauts de page avec `break-after: page`
- Cacher la toolbar de navigation (`.toolbar { display: none }`)
- Optimiser les tailles de police pour le papier

### RTL pour l'arabe
Pour les cahiers arabes :
- `<html lang="ar" dir="rtl">`
- La reliure (spine) est \u00e0 DROITE
- Les onglets sont \u00e0 gauche
- Tout le texte est `text-align: right`
- Police : Cairo wght 400-900

## G\u00e9n\u00e9rer un nouveau cahier

Quand on te demande de cr\u00e9er ou modifier un cahier :

1. **D\u00e9terminer la mati\u00e8re et la langue** (FR ou AR)
2. **Lire le cahier existant le plus proche** comme r\u00e9f\u00e9rence de style
3. **Cr\u00e9er le HTML** avec toute la structure (spine, tabs, pages, header, body, footer)
4. **Int\u00e9grer le CSS print** pour une impression A4 propre
5. **Ajouter les QR codes** li\u00e9s aux le\u00e7ons de l'appli
6. **Tester** en ouvrant le HTML dans un navigateur et en v\u00e9rifiant l'aper\u00e7u print (Ctrl+P)

## Conversion HTML \u2192 PDF

Le script `html_to_pdf.py` se trouve dans `6AF-MATH-SCIENCE-FRANCAIS/`. Pour convertir :
```bash
python html_to_pdf.py
```

Alternative : ouvrir le HTML dans Chrome et imprimer en PDF (Ctrl+P \u2192 Enregistrer en PDF).

## Contenu par mati\u00e8re

### Fran\u00e7ais
Grammaire, conjugaison, orthographe, lecture/compr\u00e9hension. Exercices types : compl\u00e9ter, souligner, transformer, r\u00e9\u00e9crire.

### Math\u00e9matiques
Num\u00e9ration, calcul (4 op\u00e9rations), g\u00e9om\u00e9trie, probl\u00e8mes, fractions, pourcentages, proportionnalit\u00e9. Exercices types : calculer, r\u00e9soudre, tracer, mesurer.

### Sciences naturelles
Biologie, physique simple, environnement, hygi\u00e8ne. Exercices types : relier, compl\u00e9ter un sch\u00e9ma, vrai/faux, expliquer.

### Arabe (\u0639\u0631\u0628\u064a\u0629)
Grammaire arabe, expression \u00e9crite, lecture, po\u00e9sie. Tout en RTL.

### Histoire-G\u00e9ographie
Histoire de la Mauritanie, g\u00e9ographie africaine, \u00e9ducation civique.

### \u00c9ducation islamique
Programme religieux mauritanien standard.
