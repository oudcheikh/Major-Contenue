# MAJOR · ماجور

**Application mobile de préparation au concours 6AF (Sixième Année Fondamentale) — Mauritanie 🇲🇷**

> Transforme la révision en aventure. Chaque jour, un défi. Chaque leçon, un QR code.

---

## Présentation

**Major** est une application React Native / Expo conçue pour aider les élèves mauritaniens de CM2 à préparer le concours d'entrée en 6ème année fondamentale (6AF). Elle accompagne le *Cahier Major 6AF* — un cahier d'exercices physique dont chaque leçon contient un QR code scannable pour accéder à un mini-cours interactif.

### Pourquoi Major ?

Les applications qui ont connu une adoption massive (Duolingo, Khan Academy Kids) partagent trois principes :
1. **Simplicité radicale** — une action principale par écran
2. **Engagement quotidien** — streak, défi du jour, récompenses immédiates
3. **Feedback positif** — confettis, étoiles, mascotte encourageante

Major applique ces trois principes à la réalité mauritanienne : bilinguisme français/arabe, chameau mascotte, couleurs du livre Major.

---

## Fonctionnalités

| Fonctionnalité | Description |
|---|---|
| 🎯 **Défi du jour** | 6 questions mixtes (2 par matière), renouvelées chaque jour automatiquement |
| 📷 **Scanner QR** | Scan du cahier physique → accès immédiat au mini-cours correspondant |
| 📚 **Cours interactifs** | 28 leçons : résumé, points clés, règle, astuce, bouton "S'entraîner" |
| 🏆 **Quiz adaptatif** | Questions avec feedback immédiat, animation sur bonne/mauvaise réponse |
| 🔥 **Streak** | Compteur de jours consécutifs pour maintenir la motivation |
| ⭐ **Résultats** | Score en étoiles (1-3), confettis si ≥ 60 %, encouragements bilingues |
| 👤 **Profil** | Progression par matière avec niveau (Débutant → Expert) |
| 🐪 **Mascotte** | Chameau animé avec messages contextuels bilingues |

---

## Matières

| Matière | Couleur | Exercices |
|---|---|---|
| 📖 Français | `#38bdf8` | Grammaire, conjugaison, orthographe, lecture |
| 📐 Mathématiques | `#fb923c` | Numération, calcul, géométrie, problèmes |
| 🔬 Sciences | `#34d399` | Biologie, physique, environnement, hygiène |

---

## Stack technique

```
React Native 0.81 (Expo SDK 54)
├── Navigation      @react-navigation/native-stack + bottom-tabs
├── Animations      React Native Animated API (spring, timing, stagger, loop)
├── Gradients       expo-linear-gradient
├── Caméra / QR     expo-camera (CameraView + useCameraPermissions)
├── Persistance     @react-native-async-storage/async-storage
└── Deep links      major://lesson/{id}
```

---

## Architecture des fichiers

```
MajorApp/
├── App.js                        # Navigation (Stack + Tabs)
├── Logo.png                      # Icône de l'app
├── src/
│   ├── screens/
│   │   ├── SplashScreen.js       # Écran de chargement animé
│   │   ├── OnboardingScreen.js   # Inscription (prénom)
│   │   ├── HomeScreen.js         # Accueil — hero, défi, matières
│   │   ├── QuizScreen.js         # Session de quiz
│   │   ├── ResultScreen.js       # Résultats avec confettis
│   │   ├── QRScannerScreen.js    # Scanner caméra
│   │   ├── LessonScreen.js       # Mini-cours
│   │   └── ProfileScreen.js      # Profil et statistiques
│   ├── components/
│   │   ├── Mascot.js             # Chameau 🐪 animé (compact + full)
│   │   └── ProgressBar.js        # Barre de progression réutilisable
│   ├── data/
│   │   ├── exercises.js          # Base d'exercices (EXERCISES + SUBJECTS)
│   │   └── courses.json          # 28 mini-cours (math, français, sciences)
│   ├── utils/
│   │   ├── storage.js            # AsyncStorage (student, stats, streak)
│   │   ├── levelDetection.js     # Calcul du niveau global et par matière
│   │   └── dailyChallenge.js     # Défi du jour + mascot messages
│   └── theme/
│       └── index.js              # COLORS, GRADIENTS, SHADOWS, LEVELS
```

---

## Lancement

```bash
# Installer les dépendances
npm install

# Démarrer le serveur Expo
npx expo start

# Scanner le QR code avec l'app Expo Go (iOS/Android)
# Ou appuyer sur "i" pour iOS Simulator
```

**Prérequis** : Node 18+, Expo Go installé sur l'appareil, SDK 54.

---

## Système QR Code

Chaque leçon du cahier physique contient un QR code encodant :
```
major://lesson/{lessonId}
```

| ID Leçon | Matière | Titre |
|---|---|---|
| `math-001` | Maths | Numération — Les grands nombres |
| `math-002` | Maths | Addition et soustraction posées |
| `fr-001` | Français | Le nom et ses déterminants |
| `fr-002` | Français | Le groupe nominal |
| `sci-001` | Sciences | Les êtres vivants |
| ... | ... | 28 leçons au total |

Les QR codes sont générés avec `generate_qrcodes.py` (à la racine du dossier parent).

---

## Système de niveaux

| Niveau | Score | Couleur | Icône |
|---|---|---|---|
| Débutant · مبتدئ | 0–39% | Gris | 🌱 |
| Intermédiaire · متوسط | 40–69% | Orange | ⭐ |
| Avancé · متقدم | 70–84% | Bleu | 🚀 |
| Expert · خبير | 85–100% | Or | 🏆 |

---

## Défi du jour

Généré automatiquement à minuit :
- 2 questions de Français
- 2 questions de Mathématiques
- 2 questions de Sciences

Mélangées aléatoirement. Persisté dans AsyncStorage avec la date du jour comme clé — se réinitialise automatiquement le lendemain.

---

## Culture mauritanienne

L'app est conçue pour les élèves mauritaniens :
- 🇲🇷 Couleurs du drapeau en accent
- 🐪 Chameau comme mascotte nationale
- 🌐 Bilingue français / arabe tout au long de l'expérience
- 📚 Contenu aligné sur le programme 6AF mauritanien

---

*Cahier Major 6AF — Prépa Concours · موريتانيا*
