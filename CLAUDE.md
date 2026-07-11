# MAJOR — Projet Éducatif Mauritanie 🇲🇷

> Plateforme phygitale (physique + digital) de préparation au concours 6AF (Sixième Année Fondamentale) pour les élèves mauritaniens de CM2.

## Vue d'ensemble

Major est un écosystème éducatif complet comprenant :
1. **Les Cahiers Major** — cahiers d'exercices physiques (PDF/HTML) avec QR codes intégrés
2. **MajorApp** — application mobile React Native / Expo (quiz, scanner QR, mentor IA, progression)
3. **Vidéos pédagogiques** — animations mathématiques pour CM2
4. **Scraper Rimbac** — outil de collecte de ressources éducatives publiques
5. **QCM Reviewer** — outil web/backend de révision par QCM

## Architecture des dossiers

```
Documents/
├── Major-Contenue/                    ← DOSSIER PRINCIPAL DU PROJET
│   ├── CLAUDE.md                      ← CE FICHIER
│   ├── .claude/skills/                ← Skills personnalisés pour Claude
│   │   ├── major-ui-design/           ← Skill design UI/UX de l'appli
│   │   ├── major-cahier-design/       ← Skill design des cahiers PDF/HTML
│   │   └── major-branding/            ← Skill identité visuelle Major
│   ├── 6AF-ARABE/                     ← Cahier arabe (contenu + HTML/PDF)
│   │   ├── Arabe/                     ← Sources par chapitre
│   │   ├── Histoire_Geographie/
│   │   ├── Islamique/
│   │   └── Cahier-Major-Arabe-6AF.*   ← PDF + HTML générés
│   ├── 6AF-MATH-SCIENCE-FRANCAIS/     ← Cahier français + maths + sciences
│   │   ├── Francais/
│   │   ├── Mathematiques/
│   │   ├── Sciences_naturelles/
│   │   ├── MajorApp/                  ← 📱 APPLICATION MOBILE (React Native / Expo)
│   │   └── *.html / *.pdf            ← Cahiers générés
│   ├── Cahier-Arabe.pdf               ← Version complète du cahier arabe
│   ├── cahier-français.pdf            ← Version complète du cahier français
│   ├── generate_qrcodes.py            ← Générateur de QR codes
│   └── Major-Presentation-Professeurs.html ← Présentation pour enseignants
├── cahier_malin/                      ← Prototype Flutter (ancien)
├── qcm-reviewer/                      ← Backend Django + frontend JS pour QCM
├── manuel-cm2/                        ← Notebooks Jupyter, API, data
├── videoMathCM2_LOT1/                 ← Vidéos MP4 de maths (13 vidéos)
├── rimbac_downloads/                  ← Ressources scrappées de rimbac.com
└── download_rimbac.py                 ← Script Python de scraping
```

## Skills personnalisés

Trois skills sont disponibles dans `.claude/skills/` pour guider Claude :

| Skill | Rôle | Déclencheur |
|-------|------|-------------|
| `major-ui-design` | Design UI/UX de l'appli React Native | Écrans, composants, maquettes, animations |
| `major-cahier-design` | Création des cahiers PDF/HTML | Cahiers, exercices, mise en page, QR codes |
| `major-branding` | Identité visuelle et communication | Branding, logo, présentations, marketing |
| `major-voice-tutor` | Tuteur vocal arabe (OpenAI Realtime API) | Voix, tuteur arabe, interaction vocale, TTS |

## Stack technique

### MajorApp (Application mobile)
- **Framework** : React Native 0.81.5 + Expo SDK 54
- **Navigation** : @react-navigation (native-stack + bottom-tabs)
- **Animations** : React Native Animated API (spring, timing, stagger, loop)
- **Persistance** : AsyncStorage (offline first)
- **Caméra/QR** : expo-camera (CameraView)
- **Audio/TTS** : expo-speech, expo-audio
- **Gradients** : expo-linear-gradient
- **Deep links** : major://lesson/{id}

### Cahiers (Génération PDF)
- **Source** : HTML structuré avec CSS print-ready
- **Conversion** : html_to_pdf.py (Python)
- **QR codes** : generate_qrcodes.py (major://lesson/{id})
- **Langues** : Français, Arabe (RTL), bilingue

### Backend / Outils
- **QCM Reviewer** : Django + SQLite (Python 3.13)
- **Scraper** : Python (requests, BeautifulSoup)
- **Data** : Jupyter Notebooks (market_risk, data-quality)

## Identité visuelle Major

### Palette de couleurs
| Nom         | Hex       | Usage                           |
|-------------|-----------|----------------------------------|
| Navy        | `#182b66` | Gradient départ, fond hero       |
| Royal       | `#2563eb` | Couleur primaire, boutons, CTA   |
| Sky         | `#38bdf8` | Gradient fin, accents, français  |
| Or          | `#fde68a` | Streak, progress fill            |
| Or foncé    | `#F0B429` | Textes en or, labels             |
| Orange      | `#fb923c` | Mathématiques                    |
| Vert        | `#34d399` | Sciences                         |
| Background  | `#f0f4ff` | Fond global                      |

### Matières et couleurs
| Matière         | Couleur   | Emoji |
|-----------------|-----------|-------|
| Français        | `#38bdf8` | 📖    |
| Mathématiques   | `#fb923c` | 📐    |
| Sciences        | `#34d399` | 🔬    |
| Arabe           | `#06803C` | 🕌    |
| Histoire-Géo    | `#8b5cf6` | 🌍    |
| Islamique       | `#059669` | ☪️    |

### Mascotte
- **Animal** : Chameau 🐪 (symbole mauritanien)
- **Comportement** : bounce animation, messages bilingues contextuels
- **Ton** : encourageant, comme un grand frère / grande sœur

### Dégradés (gradients)
```js
hero:      ['#182b66', '#2563eb', '#38bdf8']   // Écrans principaux
challenge: ['#1e1b4b', '#4338ca', '#6366f1']   // Défi du jour
gold:      ['#F0B429', '#fb923c']               // Boutons secondaires
success:   ['#059669', '#10b981']               // Réussite
french:    ['#0284c7', '#38bdf8']               // Français
math:      ['#ea580c', '#fb923c']               // Maths
science:   ['#059669', '#34d399']               // Sciences
```

## Conventions de code

### React Native / MajorApp
- **Langue du code** : anglais (noms de variables, fonctions, commentaires techniques)
- **Langue du contenu** : français + arabe (textes affichés, UI)
- **Style** : functional components + hooks, pas de classes
- **Animations** : `useNativeDriver: true` partout (sauf width/height)
- **Fichiers** : PascalCase pour les composants, camelCase pour les utils
- **Structure** : src/screens/, src/components/, src/data/, src/utils/, src/theme/

### Cahiers HTML/PDF
- **Direction texte arabe** : `dir="rtl"`, `text-align: right`
- **Noms de fichiers** : Cahier-Major-{Matière}-6AF.{html,pdf}
- **QR codes** : format `major://lesson/{lessonId}` (ex: math-001, fr-001, sci-001)

### Python
- **Style** : PEP 8, docstrings en français
- **Encoding** : UTF-8 systématique (contenu arabe)

## Contraintes terrain (Mauritanie)

Ces contraintes sont CRITIQUES et doivent guider chaque décision :
1. **Offline first** — beaucoup d'élèves n'ont pas de connexion internet stable. Tout doit fonctionner hors ligne via AsyncStorage
2. **Low data** — privilégier texte + TTS, minimiser les images/vidéos dans l'app
3. **Bilingue** — tout texte visible doit être en français ET en arabe
4. **Appareils bas de gamme** — optimiser les performances, animations légères
5. **Contexte culturel** — respecter les valeurs mauritaniennes, utiliser le chameau comme mascotte, couleurs du drapeau

## Stratégie phygitale (Cahier ↔ App)

Le pont entre le cahier physique et l'app se fait par QR codes :
1. L'élève scanne un QR code dans le cahier physique
2. L'app ouvre `MentorFlowScreen` avec le cours correspondant
3. Accroche audio via TTS (ton familier, "grand frère")
4. Résumé visuel (3 points max)
5. Micro-défi (QCM rapide) avec gain de crédits
6. Mise à jour du profil local
7. Si ≥5 échecs consécutifs → suggestion de prof à domicile

## Système de mentors IA

L'app embarque deux mentors complémentaires :

| Mentor | Langue | Mode | API | Prompt |
|--------|--------|------|-----|--------|
| **Major** (grand frère) | Français | Texte/chat | OpenAI Chat Completions (gpt-4o-mini) | `src/prompts/grandFrerePrompt.js` |
| **Tuteur vocal** | Arabe | Voix temps réel | OpenAI Realtime API (WebSocket) | `src/prompts/voiceTutorPrompt.js` |

Les deux partagent la même philosophie pédagogique : ne jamais donner la réponse directement, guider l'enfant par des indices et des questions, vérifier la compréhension même après une bonne réponse. Major utilise des analogies locales mauritaniennes en français, le tuteur vocal travaille en arabe standard simplifié pour l'oral.

## Fichiers clés à connaître

### MajorApp
| Fichier | Rôle |
|---------|------|
| `App.js` | Navigation principale (Stack + Tabs) |
| `src/screens/HomeScreen.js` | Accueil — hero, défi du jour, matières |
| `src/screens/QuizScreen.js` | Session de quiz |
| `src/screens/MentorFlowScreen.js` | Flux mentor IA après scan QR |
| `src/screens/QRScannerScreen.js` | Scanner caméra |
| `src/data/exercises.js` | Base d'exercices (EXERCISES + SUBJECTS) |
| `src/data/courses.json` | 28 mini-cours |
| `src/utils/mentorEngine.js` | Moteur du mentor IA |
| `src/utils/storage.js` | Persistance AsyncStorage |
| `src/prompts/voiceTutorPrompt.js` | Prompt du tuteur vocal arabe (Realtime API) |
| `src/theme/index.js` | COLORS, GRADIENTS, SHADOWS, LEVELS |
| `DESIGN.md` | Design system complet |

### Cahiers
| Fichier | Rôle |
|---------|------|
| `6AF-ARABE/Cahier-Major-Arabe-6AF.html` | Cahier arabe (source) |
| `6AF-MATH-SCIENCE-FRANCAIS/Cahier major 6AF PREPA-COUNCOURS.html` | Cahier maths/français/sciences |
| `generate_qrcodes.py` | Générateur de QR codes |
| `6AF-MATH-SCIENCE-FRANCAIS/html_to_pdf.py` | Convertisseur HTML→PDF |

## Système de niveaux

| Niveau | Score | Couleur | Icône |
|--------|-------|---------|-------|
| Débutant · مبتدئ | 0–39% | Gris | 🌱 |
| Intermédiaire · متوسط | 40–69% | Orange | ⭐ |
| Avancé · متقدم | 70–84% | Bleu | 🚀 |
| Expert · خبير | 85–100% | Or | 🏆 |

## Prochaines étapes / Roadmap

- [x] Organiser l'arborescence et nettoyer les doublons
- [x] Créer CLAUDE.md et skills personnalisés
- [ ] Ajouter plus de contenu arabe (Histoire-Géo, Islamique)
- [ ] Intégrer les vidéos Math CM2 dans l'app
- [ ] Mode parent (rapport hebdomadaire WhatsApp-like)
- [ ] Publication sur Play Store / APK
- [ ] Tests unitaires pour mentorEngine et quiz logic

## graphify

This project has a graphify knowledge graph at graphify-out/.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- After modifying code files in this session, run `graphify update .` to keep the graph current (AST-only, no API cost)
