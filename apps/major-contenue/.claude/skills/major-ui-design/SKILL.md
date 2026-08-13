---
name: major-ui-design
description: "Design UI/UX pour l'application mobile Major (React Native / Expo). Utilise ce skill chaque fois que l'utilisateur veut : cr\u00e9er ou modifier un \u00e9cran de l'appli, concevoir un composant React Native, cr\u00e9er une maquette ou un prototype UI, am\u00e9liorer l'exp\u00e9rience utilisateur, travailler sur les animations, le th\u00e8me, les couleurs, les ic\u00f4nes, ou tout ce qui touche \u00e0 l'interface de MajorApp. D\u00e9clenche aussi pour : \"ajouter un \u00e9cran\", \"modifier le home\", \"am\u00e9liorer le design de l'appli\", \"cr\u00e9er un composant\", \"maquette\", \"wireframe\", \"UI\", \"UX\", \"mockup\"."
---

# Major UI/UX Design — Application Mobile

Ce skill guide la conception et le d\u00e9veloppement de l'interface utilisateur de **MajorApp**, l'application mobile React Native / Expo du projet Major.

## Contexte

MajorApp est une application \u00e9ducative pour les \u00e9l\u00e8ves mauritaniens de CM2, pr\u00e9parant le concours 6AF. Elle doit \u00eatre :
- **Simple et engageante** (inspir\u00e9e de Duolingo)
- **Bilingue** (fran\u00e7ais + arabe RTL)
- **Offline first** (pas de d\u00e9pendance r\u00e9seau)
- **Performante** sur appareils bas de gamme

## Design System de r\u00e9f\u00e9rence

Avant tout travail UI, lire le fichier `DESIGN.md` \u00e0 la racine de MajorApp :
```
Major-Contenue/6AF-MATH-SCIENCE-FRANCAIS/MajorApp/DESIGN.md
```

Ce fichier contient la palette compl\u00e8te, la typographie, les composants, et les r\u00e8gles d'animation.

## Palette principale

| R\u00f4le | Hex | Usage |
|------|-----|-------|
| Navy | `#182b66` | Gradient d\u00e9part, fond hero |
| Royal | `#2563eb` | Couleur primaire, boutons, CTA |
| Sky | `#38bdf8` | Gradient fin, fran\u00e7ais |
| Or | `#fde68a` | Streak, progress |
| Orange | `#fb923c` | Math\u00e9matiques |
| Vert | `#34d399` | Sciences |
| Background | `#f0f4ff` | Fond global |
| Ink | `#0f172a` | Texte principal |
| Success | `#10b981` | Correct |
| Error | `#ef4444` | Incorrect |

## R\u00e8gles de design UI

### Structure d'\u00e9cran
1. Chaque \u00e9cran a UNE action principale visible imm\u00e9diatement
2. Padding horizontal de 16px syst\u00e9matique
3. Les gradients (expo-linear-gradient) habillent les zones hero et les headers
4. Fond g\u00e9n\u00e9ral : `#f0f4ff`

### Composants
- **Cards** : borderRadius 20-28px, shadow `#182b66` (jamais noir pur), fond blanc
- **Boutons** : borderRadius 16-18px, gradient ou couleur solide
- **Chips/Tags** : borderRadius 999px (pill), texte 10px uppercase, letterspacing 1.5
- **Barre de progression** : fill anim\u00e9 en `#fde68a`

### Texte bilingue
- Le texte fran\u00e7ais est affich\u00e9 normalement (LTR)
- Le texte arabe utilise `textAlign: 'right'` et `fontWeight: '800'`
- Les deux langues apparaissent ensemble dans la mascotte et les \u00e9tiquettes cl\u00e9s
- Couleur arabe : or (`#F0B429`) ou vert (`#06803C`) selon le contexte

### Animations
Toutes les animations utilisent React Native Animated API :
- `useNativeDriver: true` partout (sauf pour width/height)
- Entr\u00e9es : Spring (tension 65-70, friction 9-10) + fade
- Boucles : timing pour streak pulse (scale 1 \u2192 1.08)
- Press : Sequence spring scale (0.93 \u2192 retour)
- Mascotte : bounce loop vertical (-10px / 700ms)

### Accessibilit\u00e9
- Taille min tap : 44x44px
- Contraste blanc sur Royal (#2563eb) = 4.8:1
- activeOpacity entre 0.85 et 0.92

## Structure des fichiers

```
MajorApp/src/
\u251c\u2500\u2500 screens/          \u2190 Un fichier par \u00e9cran
\u2502   \u251c\u2500\u2500 HomeScreen.js
\u2502   \u251c\u2500\u2500 QuizScreen.js
\u2502   \u251c\u2500\u2500 ResultScreen.js
\u2502   \u251c\u2500\u2500 QRScannerScreen.js
\u2502   \u251c\u2500\u2500 LessonScreen.js
\u2502   \u251c\u2500\u2500 MentorFlowScreen.js
\u2502   \u251c\u2500\u2500 OnboardingScreen.js
\u2502   \u251c\u2500\u2500 ProfileScreen.js
\u2502   \u2514\u2500\u2500 SplashScreen.js
\u251c\u2500\u2500 components/       \u2190 Composants r\u00e9utilisables
\u2502   \u251c\u2500\u2500 Mascot.js
\u2502   \u251c\u2500\u2500 ProgressBar.js
\u2502   \u251c\u2500\u2500 LevelBadge.js
\u2502   \u251c\u2500\u2500 EncouragementModal.js
\u2502   \u251c\u2500\u2500 CourseVisualizer.js
\u2502   \u2514\u2500\u2500 MentorScene.js
\u251c\u2500\u2500 theme/
\u2502   \u2514\u2500\u2500 index.js          \u2190 COLORS, GRADIENTS, SHADOWS, LEVELS
\u251c\u2500\u2500 data/
\u2502   \u251c\u2500\u2500 exercises.js      \u2190 Questions et mati\u00e8res
\u2502   \u2514\u2500\u2500 courses.json      \u2190 28 mini-cours
\u2514\u2500\u2500 utils/
    \u251c\u2500\u2500 storage.js        \u2190 AsyncStorage
    \u251c\u2500\u2500 dailyChallenge.js \u2190 D\u00e9fi du jour
    \u2514\u2500\u2500 levelDetection.js \u2190 Calcul des niveaux
```

## Flux de navigation

```
Splash (2.6s)
  \u251c\u2500\u2500 [nouveau] \u2192 Onboarding \u2192 Main
  \u2514\u2500\u2500 [existant] \u2192 Main

Main (Tabs)
  \u251c\u2500\u2500 Home \u2192 Quiz \u2192 Result
  \u251c\u2500\u2500 ScannerTab \u2192 QRScanner \u2192 MentorFlow / Lesson \u2192 Quiz
  \u2514\u2500\u2500 Profile
```

## Cr\u00e9er un nouvel \u00e9cran

Quand on te demande de cr\u00e9er un nouvel \u00e9cran :
1. Cr\u00e9er le fichier dans `src/screens/NomScreen.js`
2. Importer les couleurs et gradients depuis `src/theme/index.js`
3. Utiliser `expo-linear-gradient` pour le header/hero
4. Ajouter les animations d'entr\u00e9e (Spring fade + translateY)
5. Supporter le bilingue (fr + ar) pour tout texte visible
6. Ajouter la navigation dans `App.js`
7. Respecter la structure : SafeAreaView \u2192 ScrollView \u2192 contenu

## Cr\u00e9er un nouveau composant

1. Cr\u00e9er dans `src/components/NomComposant.js`
2. Functional component avec hooks
3. Props bien d\u00e9finies avec valeurs par d\u00e9faut
4. Animations native driver quand applicable
5. Pas de styles inline — utiliser StyleSheet.create

## G\u00e9n\u00e9rer une maquette

Si l'utilisateur veut voir une maquette ou un wireframe :
1. Cr\u00e9er un fichier React (.jsx) avec la maquette interactive
2. Utiliser les vraies couleurs Major (pas de gris placeholder)
3. Simuler les donn\u00e9es avec des contenus r\u00e9alistes en fran\u00e7ais + arabe
4. Inclure la mascotte chameau dans les \u00e9tats encourageants

## Syst\u00e8me de niveaux (r\u00e9f\u00e9rence)

| Niveau | Score | Couleur | Ic\u00f4ne |
|--------|-------|---------|------|
| D\u00e9butant \u00b7 \u0645\u0628\u062a\u062f\u0626 | 0\u201339% | Gris | \ud83c\udf31 |
| Interm\u00e9diaire \u00b7 \u0645\u062a\u0648\u0633\u0637 | 40\u201369% | Orange | \u2b50 |
| Avanc\u00e9 \u00b7 \u0645\u062a\u0642\u062f\u0645 | 70\u201384% | Bleu | \ud83d\ude80 |
| Expert \u00b7 \u062e\u0628\u064a\u0631 | 85\u2013100% | Or | \ud83c\udfc6 |
