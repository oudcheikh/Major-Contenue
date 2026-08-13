---
name: major-cahier-design
description: "Création et mise en page des cahiers Major (HTML/PDF print-ready) pour les élèves mauritaniens de 6AF. Utilise ce skill pour : créer ou modifier un cahier, appliquer le design cartoon B5, générer des pages de leçons, d'exercices, de couverture, ou convertir en PDF. Déclenche aussi pour : 'cahier', 'page de leçon', 'exercices', 'mise en page', 'QR code', 'B5', 'PDF', 'RTL', 'arabe', 'cartoon'."
---

# Major Cahier Design — Cahiers PDF/HTML

Ce skill guide la création des cahiers Major : fichiers HTML print-ready convertis en PDF B5, style cartoon coloré pour enfants mauritaniens.

---

## Contexte pédagogique

Les cahiers Major sont des supports physiques (imprimés) liés à l'app via QR codes :
- **Public** : élèves CM2 (6ème Année Fondamentale), 10–12 ans, Mauritanie
- **Format** : B5 (176mm × 250mm), impression recto, reliure spirale à DROITE (RTL)
- **Langues** : Arabe (principal, RTL) + Français (secondaire)
- **Matières** : Arabe · Islamique · Histoire-Géo · Français · Maths · Sciences

---

## Design System — Style Cartoon Enfant

### Philosophie visuelle

Inspiré de "MAJOR by YASSIR" (Maroc) : style cartoon vivant, épais, coloré.
- Fond crème chaud (`#F8F3E8`) — doux pour les yeux, rappelle le papier
- Bordures épaisses `3px solid #111` + ombres décalées `4px 4px 0 #111` (néo-brutal)
- Illustrations SVG inline (laptop, trophée, téléphone, étoiles)
- Reliure spirale simulée à DROITE (RTL)
- Ruban adhésif (`tape`) sur les coins des encadrés

### Palette principale

| Rôle | Hex | Usage |
|------|-----|-------|
| Fond page | `#F8F3E8` | Arrière-plan crème chaud |
| Navy | `#182b66` | Header hero, footer |
| Royal | `#2563eb` | Primaire, boutons, règles |
| Sky | `#38bdf8` | Accent, Français |
| Crème | `#FFF9ED` | Cards exercices |
| Or | `#FDE68A` | Badges, progress |
| Vert | `#059669` | Scanner QR, Sciences |
| Orange | `#fb923c` | Maths |

### Couleurs par matière

| Matière | Header bg | Accent | Pill |
|---------|-----------|--------|------|
| Arabe | `#1e3a5f` → `#2563eb` | `#38bdf8` | `#DBEAFE` |
| Islamique | `#064e3b` → `#059669` | `#34d399` | `#D1FAE5` |
| Histoire-Géo | `#3b0764` → `#7c3aed` | `#a78bfa` | `#EDE9FE` |
| Français | `#0c4a6e` → `#0284c7` | `#38bdf8` | `#E0F2FE` |
| Maths | `#7c2d12` → `#ea580c` | `#fb923c` | `#FEF3C7` |
| Sciences | `#064e3b` → `#059669` | `#34d399` | `#D1FAE5` |

---

## Structure HTML d'une page B5

```html
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;900&display=swap" rel="stylesheet">
  <style>
    @page { size: 176mm 250mm; margin: 0; }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: #E5E7EB; font-family: 'Cairo', sans-serif; }
    
    .page {
      width: 176mm; min-height: 250mm;
      background: #F8F3E8;
      position: relative;
      overflow: hidden;
      print-color-adjust: exact;
      -webkit-print-color-adjust: exact;
    }
    
    /* SPIRALE DROITE */
    .spiral-strip {
      position: absolute; top: 0; right: 0;
      width: 22mm; height: 100%;
      background: linear-gradient(180deg, #2a2a2a 0%, #3a3a3a 100%);
      z-index: 10;
    }
    .ring {
      position: absolute; right: -5px;
      width: 20px; height: 20px;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%, #6B6560, #3A3530);
      border: 2px solid #1a1a1a;
      box-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* CONTENU (marge droite pour spirale) */
    .content { 
      padding: 6mm 8mm 6mm 28mm; /* droite=28mm pour spirale */
    }
    
    /* HEADER HERO */
    .lesson-header {
      background: linear-gradient(135deg, #1e3a5f, #2563eb, #38bdf8);
      padding: 10mm 12mm 8mm;
      border-bottom: 4px solid #111;
      position: relative;
    }
    
    /* BADGE NIVEAU */
    .level-badge {
      display: inline-flex; align-items: center; gap: 6px;
      background: white; border: 3px solid #111;
      border-radius: 20px; padding: 3px 10px;
      box-shadow: 3px 3px 0 #111;
      font-weight: 900; font-size: 13px; color: #1e3a5f;
    }
    
    /* ENCADRÉ RÈGLE */
    .rule-box {
      background: #EEF2FF;
      border: 3px solid #111;
      border-radius: 12px;
      box-shadow: 4px 4px 0 #111;
      padding: 10px 14px;
      position: relative;
      margin: 8px 0;
    }
    .tape {
      position: absolute; top: -10px; right: 20px;
      width: 40px; height: 18px;
      background: rgba(253, 230, 138, 0.7);
      border: 1px solid rgba(0,0,0,0.1);
      border-radius: 3px;
      transform: rotate(-3deg);
    }
    
    /* GRILLE EXERCICES */
    .exercise-grid {
      display: grid; grid-template-columns: 1fr 1fr;
      gap: 8px; margin: 8px 0;
    }
    .ex-card {
      border: 3px solid #111; border-radius: 12px;
      box-shadow: 3px 3px 0 #111;
      padding: 8px 10px;
    }
    .ex-card.blue { background: #DBEAFE; }
    .ex-card.yellow { background: #FEF9C3; }
    
    /* SECTION QR */
    .qr-section {
      background: linear-gradient(135deg, #064e3b, #059669);
      border: 3px solid #111; border-radius: 14px;
      box-shadow: 4px 4px 0 #111;
      padding: 10px 14px;
      margin: 8px 0;
    }
    .scan-btn {
      background: white; color: #059669;
      border: 3px solid #111; border-radius: 20px;
      box-shadow: 3px 3px 0 #111;
      padding: 6px 14px;
      font-weight: 900; font-size: 13px;
      display: inline-block;
    }
    
    /* FOOTER */
    .page-footer {
      background: #1e3a5f;
      border-top: 3px solid #111;
      padding: 5mm 8mm 5mm 28mm;
      display: flex; justify-content: space-between; align-items: center;
    }
  </style>
</head>
<body>
  <div class="page">
    <!-- Spirale droite -->
    <div class="spiral-strip">
      <!-- Anneaux positionnés à intervalles réguliers -->
      <div class="ring" style="top:15mm"></div>
      <div class="ring" style="top:35mm"></div>
      <!-- ... répéter jusqu'à 230mm -->
    </div>
    
    <!-- Header -->
    <div class="lesson-header">
      <div class="level-badge">📌 6AF · ماجور</div>
      <h1 style="color:white; font-size:28px; font-weight:900; margin-top:6px">
        عنوان الدرس هنا
      </h1>
      <span style="background:#DBEAFE; border:2px solid #93C5FD; 
                   border-radius:20px; padding:3px 12px; color:#1e3a5f;
                   font-size:12px; font-weight:700; display:inline-block; margin-top:4px">
        💡 اللغة العربية
      </span>
    </div>
    
    <!-- Contenu -->
    <div class="content">
      
      <!-- Encadré règle -->
      <div class="rule-box">
        <div class="tape"></div>
        <div style="color:#2563eb; font-weight:900; font-size:13px; margin-bottom:4px">
          📖 القاعدة الأساسية
        </div>
        <p style="color:#1e293b; font-size:14px; line-height:1.6">
          نص القاعدة هنا...
        </p>
      </div>
      
      <!-- Exercices -->
      <div style="color:#7c3aed; font-weight:900; font-size:14px; margin:8px 0 4px">
        ✏️ تدريبات
      </div>
      <div class="exercise-grid">
        <div class="ex-card blue">
          <div style="font-weight:700; font-size:12px; color:#1e40af">١ — السؤال هنا</div>
          <div style="border-bottom:1.5px solid #93C5FD; margin:18px 0 4px"></div>
        </div>
        <div class="ex-card yellow">
          <div style="font-weight:700; font-size:12px; color:#92400e">٢ — السؤال هنا</div>
          <div style="border-bottom:1.5px solid #FCD34D; margin:18px 0 4px"></div>
        </div>
      </div>
      
      <!-- QR Section -->
      <div class="qr-section">
        <div style="display:flex; align-items:center; justify-content:space-between">
          <div>
            <div style="color:#A7F3D0; font-size:11px; font-weight:700">🎯 تحدي اليوم</div>
            <div style="color:white; font-size:13px; font-weight:900">
              امسح الرمز وحل التحدي!
            </div>
          </div>
          <div style="text-align:center">
            <!-- QR code image ici -->
            <img src="qr_p1.png" width="55" height="55" 
                 style="border:3px solid white; border-radius:8px; display:block; margin-bottom:4px">
            <div class="scan-btn">امسحني ✨</div>
          </div>
        </div>
      </div>
      
    </div>
    
    <!-- Footer -->
    <div class="page-footer">
      <div style="color:#93C5FD; font-size:10px; font-weight:700">ماجور · 6AF</div>
      <div style="color:white; font-size:11px; font-weight:900">MAJOR</div>
      <div style="color:#93C5FD; font-size:10px">الصفحة ١</div>
    </div>
    
  </div>
</body>
</html>
```

---

## Illustrations SVG inline

### Laptop avec logo Major
```html
<svg width="70" height="55" viewBox="0 0 70 55">
  <rect x="8" y="4" width="54" height="36" rx="4" fill="#1e3a5f" stroke="#111" stroke-width="2"/>
  <rect x="11" y="7" width="48" height="30" rx="2" fill="#2563eb"/>
  <!-- Logo 2×2 grille -->
  <rect x="19" y="13" width="13" height="13" rx="2" fill="#38bdf8"/>
  <rect x="35" y="13" width="13" height="13" rx="2" fill="#fb923c"/>
  <rect x="19" y="29" width="13" height="6" rx="2" fill="#34d399"/>
  <rect x="35" y="29" width="13" height="6" rx="2" fill="#fde68a"/>
  <!-- Base laptop -->
  <path d="M2 42 Q35 46 68 42 L70 50 Q35 54 0 50 Z" fill="#374151" stroke="#111" stroke-width="1.5"/>
</svg>
```

### Trophée
```html
<svg width="50" height="55" viewBox="0 0 50 55">
  <path d="M15 5 Q25 3 35 5 L33 28 Q25 33 17 28 Z" fill="#FDE68a" stroke="#111" stroke-width="2"/>
  <rect x="22" y="28" width="6" height="10" fill="#F59E0B" stroke="#111" stroke-width="1.5"/>
  <rect x="15" y="38" width="20" height="5" rx="2" fill="#92400E" stroke="#111" stroke-width="1.5"/>
  <path d="M35 8 Q45 8 44 18 Q43 25 35 22" fill="none" stroke="#F59E0B" stroke-width="3" stroke-linecap="round"/>
  <path d="M15 8 Q5 8 6 18 Q7 25 15 22" fill="none" stroke="#F59E0B" stroke-width="3" stroke-linecap="round"/>
  <text x="25" y="22" text-anchor="middle" font-size="12" font-weight="900">🏆</text>
</svg>
```

---

## Règles RTL

- `<html dir="rtl" lang="ar">` — TOUJOURS
- La spirale est à DROITE → padding-left (côté ouverture) réduit
- `padding: 6mm 8mm 6mm 28mm` = top right bottom **left** (le contenu s'ouvre à gauche)
- `text-align: right` pour tout contenu arabe
- Les grilles flex : `flex-direction: row` (pas besoin de reverse avec RTL)

---

## Fichiers de référence

| Fichier | Rôle |
|---------|------|
| `6AF-ARABE/template-cahier-cartoon-6AF.html` | Template de référence B5 cartoon |
| `6AF-ARABE/Cahier-Major-LangueArabe-Islamique-6AF-V2.html` | Cahier arabe (24 pages, contenu complet) |
| `6AF-MATH-SCIENCE-FRANCAIS/html_to_pdf.py` | Conversion HTML→PDF (Chrome headless) |
| `generate_qrcodes.py` | Génération QR codes `major://lesson/{id}` |

---

## Workflow de création d'un cahier

1. **Partir du template** `template-cahier-cartoon-6AF.html`
2. **Adapter la couleur** selon la matière (tableau palette ci-dessus)
3. **Remplir le contenu** : titre, règle, exemples, exercices, QR id
4. **Positions spirale** : anneaux de `top:10mm` à `top:235mm`, pas de `20mm`
5. **QR codes** : `<img src="qr_p{N}.png">` + lancer `generate_qrcodes.py`
6. **PDF** : lancer `html_to_pdf.py` avec taille B5

---

## Conventions typographiques

| Élément | Font | Weight | Size |
|---------|------|--------|------|
| Titre leçon | Cairo | 900 | 26–34px |
| Sous-titre | Cairo | 700 | 14–16px |
| Corps texte | Cairo | 700 | 13–14px |
| Badge/pill | Cairo | 700 | 10–12px |
| Numéros page | Cairo | 700 | 10px |

---

## CSS Print

```css
@media print {
  body { background: white; }
  .page { box-shadow: none; }
  * { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
}
```
