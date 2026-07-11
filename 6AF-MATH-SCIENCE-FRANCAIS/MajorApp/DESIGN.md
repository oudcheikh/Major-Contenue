# MAJOR — Design System

> Document de référence pour le design de l'application Major 6AF.

---

## Identité visuelle

### Inspiration

Le design de Major combine deux références :
- **La marque Major** — le cahier physique avec son identité bleu marine / bleu royal / or
- **La Mauritanie** — le chameau 🐪, le bilingue français/arabe, le drapeau 🇲🇷

### Ton visuel

Moderne, chaleureux, encourageant. Inspiré de Duolingo pour l'engagement, mais ancré dans la réalité mauritanienne. Les animations sont vives et récompensantes sans être distrayantes.

---

## Palette de couleurs

### Brand Major

| Nom | Hex | Usage |
|---|---|---|
| Navy | `#182b66` | Gradient départ, fond hero |
| Royal | `#2563eb` | Couleur primaire, boutons, CTA |
| Sky | `#38bdf8` | Gradient fin, accents, français |
| Or | `#fde68a` | Streak, progress fill, highlights |
| Or foncé | `#F0B429` | Textes en or, labels |

### Matières

| Matière | Couleur | Hex |
|---|---|---|
| 📖 Français | Bleu ciel | `#38bdf8` |
| 📐 Mathématiques | Orange | `#fb923c` |
| 🔬 Sciences | Vert émeraude | `#34d399` |

### UI

| Rôle | Hex | Description |
|---|---|---|
| Background | `#f0f4ff` | Bleu très pâle — fond global |
| Surface | `#ffffff` | Cartes, modals |
| Ink | `#0f172a` | Texte principal |
| Muted | `#64748b` | Sous-titres, labels secondaires |
| Success | `#10b981` | Correct, validé |
| Error | `#ef4444` | Incorrect, erreur |

### Dégradés

```js
hero:      ['#182b66', '#2563eb', '#38bdf8']   // Écrans principaux
challenge: ['#1e1b4b', '#4338ca', '#6366f1']   // Défi du jour
gold:      ['#F0B429', '#fb923c']               // Boutons secondaires
success:   ['#059669', '#10b981']               // Défi complété
french:    ['#0284c7', '#38bdf8']               // Quiz Français
math:      ['#ea580c', '#fb923c']               // Quiz Maths
science:   ['#059669', '#34d399']               // Quiz Sciences
```

---

## Typographie

Police système (Verdana / San Francisco / Roboto selon plateforme).

| Style | Taille | Poids | Usage |
|---|---|---|---|
| Display | 40px | 900 | Nom app sur Splash |
| H1 | 26–28px | 900 | Titre principal écran |
| H2 | 20–22px | 900 | Titre carte, défi |
| Body Large | 16px | 700 | Boutons, inputs |
| Body | 14px | 600 | Texte courant |
| Caption | 12px | 700 | Labels, tags |
| Micro | 10px | 900 | Tags en majuscules, letterspacing 1.5 |

**Arabe** : aligné à droite, `textAlign: 'right'`, poids 800.

---

## Composants clés

### Hero (HomeScreen)

```
LinearGradient [#182b66 → #2563eb → #38bdf8]
├── Cercles décoratifs (position: absolute, rgba blanc)
├── Prénom + salutation bilingue
├── Streak pulse (🔥 + nombre en or)
├── Mascot compact (chameau inline)
└── Barre de progression globale (fill animée #fde68a)
```

**Animations d'entrée** :
- Slide from top (translateY -30 → 0) + fade in
- Barre de progression : 0% → valeur réelle en 900ms (délai 600ms)
- Streak : pulse loop (scale 1 → 1.08)

### Carte Défi du jour

```
LinearGradient [#1e1b4b → #4338ca → #6366f1]
├── Tag "DÉFI DU JOUR · تحدي اليوم" (10px, letterspacing 1.5)
├── Titre + emoji 🎯 (44px)
├── Chips matières (3 icônes + "Mix de matières")
├── Barre de progression si déjà commencé (fill #fde68a)
└── Bouton "▶ Commencer le défi" (rgba blanc, bordure)
```

**Animation entrée** : Spring depuis 90% scale → 100%, fade in.

### Cartes matières (SubjectCard)

```
Card blanc (borderRadius 20, shadow navy 8%)
├── Accent gradient en haut (hauteur 4px, couleur matière)
├── Icône ronde (couleur matière 18% opacity)
├── Nom matière (12px, 800)
├── Pourcentage (20px, 900, couleur matière)
└── Barre de progression (couleur matière)
```

**Animation presse** : Scale 1 → 0.93 → spring retour.

### Mascotte (Mascot)

**Mode compact** (dans le hero) :
```
Row: 🐪 (28px, bounce -5px loop) + texte bilingue (13px blanc)
```

**Mode full** (standalone) :
```
🐪 (50px, bounce) + bulle blanche
  ├── Texte arabe (14px, vert #06803C, right-aligned)
  └── Texte français (13px, ink)
```

### Bouton scanner (Tab center)

```
Cercle 62×62px, bleu #2563eb
Bordure blanche 3px
Shadow navy, offset 8px, opacity 45%
Position : top: -22 (flottant au-dessus de la tab bar)
```

---

## Animations — référence

| Élément | Type | Paramètres |
|---|---|---|
| Entrée hero | Spring translateY | tension 70, friction 10 |
| Entrée challenge | Spring scale | tension 65, friction 9 |
| Entrée matières | Spring translateY | tension 70, friction 10 |
| Streak | Loop timing scale | 1 → 1.08, 800ms |
| Progress bar | Timing width | 900ms, délai 600ms |
| Press card | Sequence spring scale | 80ms → 0.93, spring retour |
| Chameau bounce | Loop sequence | -10px / 700ms |
| Confettis résultat | Parallel spring/timing | 22 particules, stagger |
| Loading dots | Loop sequence | 3 dots, délai 200ms chacun |
| Splash loader | Loop interpolate | 30% → 90% width |

---

## Écrans — flux de navigation

```
Splash (2.6s)
  ├── [nouveau] → Onboarding → Main
  └── [existant] → Main

Main (Tabs)
  ├── Home → Quiz → Result
  ├── ScannerTab [bouton] → QRScanner (stack) → Lesson → Quiz
  └── Profile

Stack standalone :
  Quiz → Result → Home (ou retour)
```

---

## Règles de design

1. **Padding horizontal** : 16px systématique sur toutes les sections
2. **Gap cards** : 10px entre cartes en row, 16px entre sections
3. **Border radius** : Cards 20–28px, Boutons 16–18px, Chips 999px (pill)
4. **Shadows** : Toujours `shadowColor: '#182b66'`, jamais noir pur
5. **Texte arabe** : Toujours `textAlign: 'right'`, couleur or ou bleu primaire
6. **Icônes emoji** : Préférer emoji natifs pour les icônes de matières et mascotte
7. **Animations** : `useNativeDriver: true` partout sauf pour `width`/`height` (layout)
8. **États vides** : Toujours afficher la mascotte + texte encourageant

---

## Accessibilité

- Contrastes : blanc sur `#2563eb` → ratio 4.8:1 ✓
- Tailles minimales tap : 44×44px sur tous les boutons
- `activeOpacity` entre 0.85 et 0.92 (feedback visuel systématique)

---

*Major Design System v1.0 — Avril 2026*
