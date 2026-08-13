# Graph Report - .  (2026-04-17)

## Corpus Check
- 72 files · ~894,308 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 452 nodes · 592 edges · 91 communities detected
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 111 edges (avg confidence: 0.72)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 65|Community 65]]
- [[_COMMUNITY_Community 66|Community 66]]
- [[_COMMUNITY_Community 67|Community 67]]
- [[_COMMUNITY_Community 68|Community 68]]
- [[_COMMUNITY_Community 69|Community 69]]
- [[_COMMUNITY_Community 70|Community 70]]
- [[_COMMUNITY_Community 71|Community 71]]
- [[_COMMUNITY_Community 72|Community 72]]
- [[_COMMUNITY_Community 73|Community 73]]
- [[_COMMUNITY_Community 74|Community 74]]
- [[_COMMUNITY_Community 75|Community 75]]
- [[_COMMUNITY_Community 76|Community 76]]
- [[_COMMUNITY_Community 77|Community 77]]
- [[_COMMUNITY_Community 78|Community 78]]
- [[_COMMUNITY_Community 79|Community 79]]
- [[_COMMUNITY_Community 80|Community 80]]
- [[_COMMUNITY_Community 81|Community 81]]
- [[_COMMUNITY_Community 82|Community 82]]
- [[_COMMUNITY_Community 83|Community 83]]
- [[_COMMUNITY_Community 84|Community 84]]
- [[_COMMUNITY_Community 85|Community 85]]
- [[_COMMUNITY_Community 86|Community 86]]
- [[_COMMUNITY_Community 87|Community 87]]
- [[_COMMUNITY_Community 88|Community 88]]
- [[_COMMUNITY_Community 89|Community 89]]
- [[_COMMUNITY_Community 90|Community 90]]

## God Nodes (most connected - your core abstractions)
1. `QRCodeGenerator` - 34 edges
2. `QRInjector` - 14 edges
3. `LayoutFixer` - 14 edges
4. `ContentBuilder` - 9 edges
5. `CahierConverter` - 9 edges
6. `generate_session()` - 9 edges
7. `find_lesson()` - 8 edges
8. `build_lesson_context()` - 8 edges
9. `OllamaClient` - 8 edges
10. `callChatCompletion()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `MentorFlowScreen()` --calls--> `isMentorLLMConfigured()`  [INFERRED]
  6AF-MATH-SCIENCE-FRANCAIS\MajorApp\src\screens\MentorFlowScreen.js → 6AF-MATH-SCIENCE-FRANCAIS\MajorApp\src\utils\mentorLLM.js
- `buildWeeklyParentSummary()` --calls--> `getStats()`  [INFERRED]
  6AF-MATH-SCIENCE-FRANCAIS\MajorApp\src\utils\phygitalStorage.js → 6AF-MATH-SCIENCE-FRANCAIS\MajorApp\src\utils\storage.js
- `major_tools.cli — Interface en ligne de commande ===============================` --uses--> `CahierConverter`  [INFERRED]
  major_tools\cli.py → major_tools\pdf.py
- `major_tools.cli — Interface en ligne de commande ===============================` --uses--> `QRCodeGenerator`  [INFERRED]
  major_tools\cli.py → major_tools\qr.py
- `major_tools.cli — Interface en ligne de commande ===============================` --uses--> `QRInjector`  [INFERRED]
  major_tools\cli.py → major_tools\injector.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (36): cmd_qr_export(), cmd_qr_inject(), ContentBuilder, major_tools.content — Ajout de contenu aux cahiers HTML ========================, Insère des pages de concours blanc dans le cahier.          Paramètres :, Sépare un cahier multi-matières en sous-cahiers indépendants.          Chaque en, Construit et enrichit les cahiers HTML Major avec de nouvelles pages.      Gère, Insère un bloc d'exercices HTML dans une page spécifique.          Paramètres : (+28 more)

### Community 1 - "Community 1"
Cohesion: 0.08
Nodes (21): clamp(), correctExercise(), safeArray(), CorrectionPage(), getConfidenceCopy(), getMasteryCopy(), getPracticeCopy(), buildQuizSet() (+13 more)

### Community 2 - "Community 2"
Cohesion: 0.1
Nodes (33): BaseModel, chat(), chat_stream(), GenericChatMessage, GenericChatRequest, Generic chat endpoint (free-form, not tied to a specific lesson)., Generic chat with Server-Sent Events streaming., ChatMessage (+25 more)

### Community 3 - "Community 3"
Cohesion: 0.09
Nodes (31): get_all_courses(), get_lesson(), get_subject_lessons(), list_subjects(), List all subjects with their lesson count., Return the full courses.json content., Get all lessons for a subject., Get a single lesson by ID with full details. (+23 more)

### Community 4 - "Community 4"
Cohesion: 0.1
Nodes (15): Speech-to-Text using faster-whisper (CTranslate2 Whisper)., Transcribe audio bytes to text.         Accepts any format ffmpeg supports (mp3, STTService, Text-to-Speech using edge-tts (free Microsoft Edge voices)., TTSService, list_voices(), List available TTS voices., Convert text to speech audio (MP3, base64-encoded). (+7 more)

### Community 5 - "Community 5"
Cohesion: 0.11
Nodes (15): cmd_fix_print(), cmd_rep(), cmd_repaginate(), cmd_trim(), major_tools.cli — Interface en ligne de commande ===============================, _build_sub_pages(), LayoutFixer, major_tools.layout — Correction de mise en page des cahiers HTML =============== (+7 more)

### Community 6 - "Community 6"
Cohesion: 0.19
Nodes (15): MentorFlowScreen(), awardMicroWin(), awardScanPoints(), buildWeeklyParentSummary(), computeKnowledgeLevel(), computeKnowledgePct(), getChapterInsight(), getChapterProgressMap() (+7 more)

### Community 7 - "Community 7"
Cohesion: 0.23
Nodes (13): cleanupSubscription(), fetchTTSBase64(), speakWithOpenAITTS(), stopMentorRecordingAndTranscribe(), stopMentorVoice(), transcribeWithModel(), buildToneWavBase64(), bytesToBase64() (+5 more)

### Community 8 - "Community 8"
Cohesion: 0.18
Nodes (7): OllamaClient, Returns (ollama_connected, model_loaded)., Client for Ollama LLM API., health(), lifespan(), get_tutor_prompt(), Backward-compatible: used by the generic /chat endpoint.

### Community 9 - "Community 9"
Cohesion: 0.41
Nodes (10): answerCourseQuestion(), callChatCompletion(), chatWithMentorSimple(), cleanJsonString(), generateMentorNudge(), generateMentorSession(), getApiKey(), isMentorLLMConfigured() (+2 more)

### Community 10 - "Community 10"
Cohesion: 0.2
Nodes (4): generateChallenge(), getDailyChallenge(), getMascotMessage(), HomeScreen()

### Community 11 - "Community 11"
Cohesion: 0.29
Nodes (6): cmd_pdf(), CahierConverter, Convertit tous les fichiers HTML correspondant au pattern dans un dossier., Convertit un fichier HTML de cahier Major en PDF imprimable.      Utilise Chrome, Cherche chrome.exe dans les emplacements standards Windows., Convertit un fichier HTML en PDF.          Paramètres :             html_path (s

### Community 12 - "Community 12"
Cohesion: 0.22
Nodes (2): computeSubjectLevel(), ResultScreen()

### Community 13 - "Community 13"
Cohesion: 0.29
Nodes (2): DraggableToken(), useDraggableToken()

### Community 14 - "Community 14"
Cohesion: 0.32
Nodes (4): getStats(), getStreak(), updateStats(), updateStreak()

### Community 15 - "Community 15"
Cohesion: 0.29
Nodes (0): 

### Community 16 - "Community 16"
Cohesion: 0.33
Nodes (1): App()

### Community 17 - "Community 17"
Cohesion: 0.6
Nodes (5): exportCahierPdf(), listCahiers(), readCahier(), request(), saveCahier()

### Community 18 - "Community 18"
Cohesion: 0.5
Nodes (2): buildMentorHook(), getLocalExample()

### Community 19 - "Community 19"
Cohesion: 0.5
Nodes (0): 

### Community 20 - "Community 20"
Cohesion: 0.5
Nodes (3): BaseSettings, Config, Settings

### Community 21 - "Community 21"
Cohesion: 1.0
Nodes (0): 

### Community 22 - "Community 22"
Cohesion: 1.0
Nodes (0): 

### Community 23 - "Community 23"
Cohesion: 1.0
Nodes (0): 

### Community 24 - "Community 24"
Cohesion: 1.0
Nodes (0): 

### Community 25 - "Community 25"
Cohesion: 1.0
Nodes (0): 

### Community 26 - "Community 26"
Cohesion: 1.0
Nodes (0): 

### Community 27 - "Community 27"
Cohesion: 1.0
Nodes (0): 

### Community 28 - "Community 28"
Cohesion: 1.0
Nodes (0): 

### Community 29 - "Community 29"
Cohesion: 1.0
Nodes (0): 

### Community 30 - "Community 30"
Cohesion: 1.0
Nodes (0): 

### Community 31 - "Community 31"
Cohesion: 1.0
Nodes (0): 

### Community 32 - "Community 32"
Cohesion: 1.0
Nodes (0): 

### Community 33 - "Community 33"
Cohesion: 1.0
Nodes (0): 

### Community 34 - "Community 34"
Cohesion: 1.0
Nodes (0): 

### Community 35 - "Community 35"
Cohesion: 1.0
Nodes (0): 

### Community 36 - "Community 36"
Cohesion: 1.0
Nodes (0): 

### Community 37 - "Community 37"
Cohesion: 1.0
Nodes (0): 

### Community 38 - "Community 38"
Cohesion: 1.0
Nodes (0): 

### Community 39 - "Community 39"
Cohesion: 1.0
Nodes (0): 

### Community 40 - "Community 40"
Cohesion: 1.0
Nodes (0): 

### Community 41 - "Community 41"
Cohesion: 1.0
Nodes (0): 

### Community 42 - "Community 42"
Cohesion: 1.0
Nodes (0): 

### Community 43 - "Community 43"
Cohesion: 1.0
Nodes (0): 

### Community 44 - "Community 44"
Cohesion: 1.0
Nodes (0): 

### Community 45 - "Community 45"
Cohesion: 1.0
Nodes (1): Reconstruit plusieurs pages HTML à partir des groupes d'exercices.          Cons

### Community 46 - "Community 46"
Cohesion: 1.0
Nodes (1): add_exos_arabe_islamique.py =========================== Ajoute dans le cahier ar

### Community 47 - "Community 47"
Cohesion: 1.0
Nodes (1): add_exos_plus_paginate.py ========================= 1. Ajoute 10 nouveaux exerci

### Community 48 - "Community 48"
Cohesion: 1.0
Nodes (1): fix_print_layout.py =================== 1. Corrige le CSS print : overflow:visib

### Community 49 - "Community 49"
Cohesion: 1.0
Nodes (1): fix_print_v2.py =============== 1. Corrige CSS print (overflow:visible, height:a

### Community 50 - "Community 50"
Cohesion: 1.0
Nodes (1): Génère une démo de cahier avec QR codes pointant vers la page CORRECTION IA. Sca

### Community 51 - "Community 51"
Cohesion: 1.0
Nodes (1): Script de génération des QR codes pour le Cahier Major 6AF — Mauritanie Remplace

### Community 52 - "Community 52"
Cohesion: 1.0
Nodes (1): Génère un QR code PNG en base64.

### Community 53 - "Community 53"
Cohesion: 1.0
Nodes (1): Génère le HTML de remplacement.

### Community 54 - "Community 54"
Cohesion: 1.0
Nodes (1): Génération des QR codes pour le Cahier Major Arabe 6AF — Mauritanie Produit :

### Community 55 - "Community 55"
Cohesion: 1.0
Nodes (1): Enregistre le QR code en PNG et retourne le chemin.

### Community 56 - "Community 56"
Cohesion: 1.0
Nodes (1): Génère une page de démo : extrait de cahier avec vrais QR codes web Scan QR → ou

### Community 57 - "Community 57"
Cohesion: 1.0
Nodes (1): Génère une page de démo : extrait de cahier avec vrais QR codes web Scan QR → o

### Community 58 - "Community 58"
Cohesion: 1.0
Nodes (1): Generate and inject QR codes for the new Concours Blanc pages in the French pape

### Community 59 - "Community 59"
Cohesion: 1.0
Nodes (1): inject_qr_arabe_clean.py ======================== Repart du backup propre du cah

### Community 60 - "Community 60"
Cohesion: 1.0
Nodes (1): inject_qr_banner_arabe.py  (v3 — placement correct) ============================

### Community 61 - "Community 61"
Cohesion: 1.0
Nodes (1): Met a jour les QR/URLs HTML du projet vers la version Vercel.  Le script traite

### Community 62 - "Community 62"
Cohesion: 1.0
Nodes (1): Met a jour les grands QR du cahier arabe vers la version Vercel.  Ce script remp

### Community 63 - "Community 63"
Cohesion: 1.0
Nodes (1): Regenerate every QR code in the French paper cahier so it points to Vercel.

### Community 64 - "Community 64"
Cohesion: 1.0
Nodes (1): inject_web_qr_arabe.py ====================== 1. Remplace les 21 QR codes "hero"

### Community 65 - "Community 65"
Cohesion: 1.0
Nodes (1): Bloc QR hero (remplace les real-qr dans les scan-card).

### Community 66 - "Community 66"
Cohesion: 1.0
Nodes (1): Mini-QR ajouté dans chaque exo-top (coin droit).

### Community 67 - "Community 67"
Cohesion: 1.0
Nodes (1): inject_web_qr_francais.py ========================= 1. Remplace les 16 QR codes

### Community 68 - "Community 68"
Cohesion: 1.0
Nodes (1): Retourne la position après le </div> correspondant au <div[start].

### Community 69 - "Community 69"
Cohesion: 1.0
Nodes (1): Retourne la liste (start, end) des enfants directs de page-body.

### Community 70 - "Community 70"
Cohesion: 1.0
Nodes (1): Poids visuel (en 'rangées') d'un élément enfant direct de page-body.      Règles

### Community 71 - "Community 71"
Cohesion: 1.0
Nodes (1): Regroupe les enfants en chunks de poids ≤ max_w.     • Les éléments hero restent

### Community 72 - "Community 72"
Cohesion: 1.0
Nodes (1): Retourne (opening_shell, closing_shell, pb_open_end, pb_content_end).     openin

### Community 73 - "Community 73"
Cohesion: 1.0
Nodes (1): Insère le snippet QR juste avant <div class="page-number".

### Community 74 - "Community 74"
Cohesion: 1.0
Nodes (1): Ajoute le CSS fix dans le bloc @media print existant.

### Community 75 - "Community 75"
Cohesion: 1.0
Nodes (1): restore_and_fix_print.py ======================== 1. Fusionne les pages découpée

### Community 76 - "Community 76"
Cohesion: 1.0
Nodes (1): Fusionne les pages tابع avec la page précédente.

### Community 77 - "Community 77"
Cohesion: 1.0
Nodes (1): Remplace le bloc @media print existant par le nouveau.

### Community 78 - "Community 78"
Cohesion: 1.0
Nodes (1): split_cahier_arabe.py ===================== Lit le BACKUP original (mise en page

### Community 79 - "Community 79"
Cohesion: 1.0
Nodes (1): Remplace le numéro de page hardcodé par new_num.

### Community 80 - "Community 80"
Cohesion: 1.0
Nodes (1): Remplace le bloc .tabs par les onglets du cahier (seulement les matières concern

### Community 81 - "Community 81"
Cohesion: 1.0
Nodes (1): Ajoute un QR code compact en bas de chaque page d'exercices.     Détecte la mati

### Community 82 - "Community 82"
Cohesion: 1.0
Nodes (1): Génère une couverture personnalisée à partir de l'original en remplaçant :     -

### Community 83 - "Community 83"
Cohesion: 1.0
Nodes (1): Page HG supplémentaire : Colonisation française + résistance + Mauritanie modern

### Community 84 - "Community 84"
Cohesion: 1.0
Nodes (1): Page HG supplémentaire : Géographie de l'Afrique — pays, frontières, organisatio

### Community 85 - "Community 85"
Cohesion: 1.0
Nodes (1): Page Civique supplémentaire : Élections, démocratie, justice.

### Community 86 - "Community 86"
Cohesion: 1.0
Nodes (1): split_long_pages.py =================== Pour chaque page avec >4 exercices : cou

### Community 87 - "Community 87"
Cohesion: 1.0
Nodes (1): Extract header, body content, and footer from a page segment.

### Community 88 - "Community 88"
Cohesion: 1.0
Nodes (1): Split body_content after the split_at-th exercise (0-indexed).

### Community 89 - "Community 89"
Cohesion: 1.0
Nodes (1): Reconstruct a page from parts.

### Community 90 - "Community 90"
Cohesion: 1.0
Nodes (1): trim_overflows.py ================= Pour les pages avec trop d'exercices, coupe

## Knowledge Gaps
- **95 isolated node(s):** `Trouve la position de fermeture d'un <div> imbriqué.`, `Extrait le code de leçon (ex: 'AR-01') d'un bloc HTML.`, `Extrait l'URL encodée dans un bloc QR HTML.`, `Génère un bloc HTML real-qr complet.`, `major_tools.layout — Correction de mise en page des cahiers HTML ===============` (+90 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 21`** (2 nodes): `EncouragementModal.js`, `EncouragementModal()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (2 nodes): `LevelBadge.js`, `LevelBadge()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (2 nodes): `Mascot.js`, `Mascot()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (2 nodes): `MentorScene.js`, `MentorScene()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (2 nodes): `ProgressBar.js`, `ProgressBar()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (2 nodes): `voiceTutorPrompt.js`, `buildVoiceTutorContext()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (2 nodes): `OnboardingScreen.js`, `OnboardingScreen()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (2 nodes): `ProfileScreen.js`, `ProfileScreen()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (2 nodes): `QRScannerScreen.js`, `QRScannerScreen()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (2 nodes): `QuizScreen.js`, `QuizScreen()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (2 nodes): `SplashScreen.js`, `SplashScreen()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (2 nodes): `CahierStudioPage()`, `CahierStudioPage.jsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (2 nodes): `LessonPage()`, `LessonPage.jsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (2 nodes): `SubjectPage.jsx`, `SubjectPage()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (2 nodes): `health()`, `studio_server.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (1 nodes): `babel.config.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (1 nodes): `metro.config.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (1 nodes): `exercises.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `grandFrerePrompt.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (1 nodes): `index.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (1 nodes): `eslint.config.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (1 nodes): `vite.config.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (1 nodes): `data.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (1 nodes): `main.jsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (1 nodes): `Reconstruit plusieurs pages HTML à partir des groupes d'exercices.          Cons`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (1 nodes): `add_exos_arabe_islamique.py =========================== Ajoute dans le cahier ar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 47`** (1 nodes): `add_exos_plus_paginate.py ========================= 1. Ajoute 10 nouveaux exerci`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (1 nodes): `fix_print_layout.py =================== 1. Corrige le CSS print : overflow:visib`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 49`** (1 nodes): `fix_print_v2.py =============== 1. Corrige CSS print (overflow:visible, height:a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (1 nodes): `Génère une démo de cahier avec QR codes pointant vers la page CORRECTION IA. Sca`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (1 nodes): `Script de génération des QR codes pour le Cahier Major 6AF — Mauritanie Remplace`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 52`** (1 nodes): `Génère un QR code PNG en base64.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 53`** (1 nodes): `Génère le HTML de remplacement.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (1 nodes): `Génération des QR codes pour le Cahier Major Arabe 6AF — Mauritanie Produit :`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 55`** (1 nodes): `Enregistre le QR code en PNG et retourne le chemin.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 56`** (1 nodes): `Génère une page de démo : extrait de cahier avec vrais QR codes web Scan QR → ou`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (1 nodes): `Génère une page de démo : extrait de cahier avec vrais QR codes web Scan QR → o`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (1 nodes): `Generate and inject QR codes for the new Concours Blanc pages in the French pape`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 59`** (1 nodes): `inject_qr_arabe_clean.py ======================== Repart du backup propre du cah`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 60`** (1 nodes): `inject_qr_banner_arabe.py  (v3 — placement correct) ============================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (1 nodes): `Met a jour les QR/URLs HTML du projet vers la version Vercel.  Le script traite`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 62`** (1 nodes): `Met a jour les grands QR du cahier arabe vers la version Vercel.  Ce script remp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (1 nodes): `Regenerate every QR code in the French paper cahier so it points to Vercel.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 64`** (1 nodes): `inject_web_qr_arabe.py ====================== 1. Remplace les 21 QR codes "hero"`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 65`** (1 nodes): `Bloc QR hero (remplace les real-qr dans les scan-card).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 66`** (1 nodes): `Mini-QR ajouté dans chaque exo-top (coin droit).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 67`** (1 nodes): `inject_web_qr_francais.py ========================= 1. Remplace les 16 QR codes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 68`** (1 nodes): `Retourne la position après le </div> correspondant au <div[start].`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 69`** (1 nodes): `Retourne la liste (start, end) des enfants directs de page-body.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 70`** (1 nodes): `Poids visuel (en 'rangées') d'un élément enfant direct de page-body.      Règles`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 71`** (1 nodes): `Regroupe les enfants en chunks de poids ≤ max_w.     • Les éléments hero restent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 72`** (1 nodes): `Retourne (opening_shell, closing_shell, pb_open_end, pb_content_end).     openin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 73`** (1 nodes): `Insère le snippet QR juste avant <div class="page-number".`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 74`** (1 nodes): `Ajoute le CSS fix dans le bloc @media print existant.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 75`** (1 nodes): `restore_and_fix_print.py ======================== 1. Fusionne les pages découpée`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 76`** (1 nodes): `Fusionne les pages tابع avec la page précédente.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 77`** (1 nodes): `Remplace le bloc @media print existant par le nouveau.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 78`** (1 nodes): `split_cahier_arabe.py ===================== Lit le BACKUP original (mise en page`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 79`** (1 nodes): `Remplace le numéro de page hardcodé par new_num.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 80`** (1 nodes): `Remplace le bloc .tabs par les onglets du cahier (seulement les matières concern`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 81`** (1 nodes): `Ajoute un QR code compact en bas de chaque page d'exercices.     Détecte la mati`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 82`** (1 nodes): `Génère une couverture personnalisée à partir de l'original en remplaçant :     -`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 83`** (1 nodes): `Page HG supplémentaire : Colonisation française + résistance + Mauritanie modern`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 84`** (1 nodes): `Page HG supplémentaire : Géographie de l'Afrique — pays, frontières, organisatio`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 85`** (1 nodes): `Page Civique supplémentaire : Élections, démocratie, justice.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 86`** (1 nodes): `split_long_pages.py =================== Pour chaque page avec >4 exercices : cou`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 87`** (1 nodes): `Extract header, body content, and footer from a page segment.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 88`** (1 nodes): `Split body_content after the split_at-th exercise (0-indexed).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 89`** (1 nodes): `Reconstruct a page from parts.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 90`** (1 nodes): `trim_overflows.py ================= Pour les pages avec trop d'exercices, coupe`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `QRCodeGenerator` connect `Community 0` to `Community 5`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **Why does `voice_chat()` connect `Community 4` to `Community 8`, `Community 2`, `Community 3`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._
- **Why does `LayoutFixer` connect `Community 5` to `Community 0`?**
  _High betweenness centrality (0.012) - this node is a cross-community bridge._
- **Are the 26 inferred relationships involving `QRCodeGenerator` (e.g. with `major_tools.cli — Interface en ligne de commande ===============================` and `ContentBuilder`) actually correct?**
  _`QRCodeGenerator` has 26 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `QRInjector` (e.g. with `major_tools.cli — Interface en ligne de commande ===============================` and `QRCodeGenerator`) actually correct?**
  _`QRInjector` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 6 inferred relationships involving `LayoutFixer` (e.g. with `major_tools.cli — Interface en ligne de commande ===============================` and `major_tools — Boîte à outils du projet Major 6AF ===============================`) actually correct?**
  _`LayoutFixer` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `ContentBuilder` (e.g. with `QRCodeGenerator` and `major_tools — Boîte à outils du projet Major 6AF ===============================`) actually correct?**
  _`ContentBuilder` has 2 INFERRED edges - model-reasoned connections that need verification._