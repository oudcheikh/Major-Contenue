---
name: major-voice-tutor
description: "Tuteur vocal arabe pour enfants — syst\u00e8me de tutorat vocal temps r\u00e9el via OpenAI Realtime API. Utilise ce skill chaque fois que l'utilisateur veut : travailler sur le tuteur vocal, int\u00e9grer la voix dans MajorApp, configurer l'API Realtime OpenAI, modifier le comportement p\u00e9dagogique du tuteur arabe, am\u00e9liorer l'interaction vocale, tester le flux voix, cr\u00e9er des prompts pour le tuteur. D\u00e9clenche aussi pour : \"voice tutor\", \"tuteur vocal\", \"\u0645\u0639\u0644\u0645\", \"realtime API\", \"voix arabe\", \"interaction vocale\", \"TTS arabe\", \"assistant vocal\"."
---

# Major Voice Tutor \u2014 Tuteur Vocal Arabe

Ce skill guide le d\u00e9veloppement du **tuteur vocal arabe** de MajorApp, un assistant p\u00e9dagogique temps r\u00e9el bas\u00e9 sur l'API OpenAI Realtime Voice.

## Vue d'ensemble

Le tuteur vocal est un compagnon d'apprentissage vocal en arabe pour les enfants mauritaniens. Il compl\u00e8te le mentor texte existant (Major, le grand fr\u00e8re en fran\u00e7ais) avec une exp\u00e9rience vocale en arabe.

### Deux mentors, deux modes

| Mentor | Langue | Mode | API | Fichier |
|--------|--------|------|-----|---------|
| **Major** (existant) | Fran\u00e7ais | Texte/chat | OpenAI Chat Completions (gpt-4o-mini) | `src/prompts/grandFrerePrompt.js` |
| **Tuteur Vocal** (nouveau) | Arabe | Voix temps r\u00e9el | OpenAI Realtime API | `src/prompts/voiceTutorPrompt.js` |

## Architecture technique

### API OpenAI Realtime Voice

L'API Realtime utilise WebSocket, pas HTTP REST :

```
wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview
```

Le flux :
1. L'app ouvre une connexion WebSocket avec le token
2. Le system prompt (tuteur arabe) est envoy\u00e9 en `session.update`
3. L'audio du micro de l'enfant est stream\u00e9 en chunks
4. L'API r\u00e9pond en audio stream\u00e9 + transcription
5. L'app joue la r\u00e9ponse audio en temps r\u00e9el

### Int\u00e9gration dans MajorApp

Fichiers concern\u00e9s et \u00e0 cr\u00e9er :

```
MajorApp/src/
\u251c\u2500\u2500 prompts/
\u2502   \u251c\u2500\u2500 grandFrerePrompt.js        \u2190 Existant (Major, fran\u00e7ais, texte)
\u2502   \u2514\u2500\u2500 voiceTutorPrompt.js        \u2190 NOUVEAU (tuteur arabe, voix)
\u251c\u2500\u2500 utils/
\u2502   \u251c\u2500\u2500 mentorLLM.js               \u2190 Existant (Chat Completions)
\u2502   \u2514\u2500\u2500 voiceRealtimeClient.js     \u2190 NOUVEAU (WebSocket Realtime API)
\u2514\u2500\u2500 screens/
    \u2514\u2500\u2500 VoiceTutorScreen.js        \u2190 NOUVEAU (\u00e9cran de session vocale)
```

### Cl\u00e9 API

M\u00eame cl\u00e9 que le mentor existant :
```
EXPO_PUBLIC_OPENAI_API_KEY
```

Stockage : fichier `.env` \u00e0 la racine de MajorApp.

## Prompt syst\u00e8me du tuteur vocal

Le prompt complet est dans `src/prompts/voiceTutorPrompt.js`. Voici les principes cl\u00e9s \u00e0 respecter lors de toute modification :

### Identit\u00e9
- Tuteur arabe bienveillant, patient, chaleureux
- Parle en arabe standard moderne simplifi\u00e9 (accessible aux enfants)
- Ton : grand fr\u00e8re / grande s\u0153ur
- Sp\u00e9cialis\u00e9 dans le contenu p\u00e9dagogique Major

### Comportement p\u00e9dagogique (ordre strict)
1. Encourager d'abord
2. Expliquer simplement la t\u00e2che
3. Donner un indice AVANT la r\u00e9ponse
4. Laisser l'enfant r\u00e9fl\u00e9chir
5. Expliquer \u00e9tape par \u00e9tape si n\u00e9cessaire
6. Donner la r\u00e9ponse seulement en dernier recours
7. Proposer un mini exercice similaire
8. Finir par de la motivation

### Anti-triche / Anti-apprentissage passif
M\u00eame si l'enfant a la bonne r\u00e9ponse, v\u00e9rifier la compr\u00e9hension :
- Poser une mini-question similaire
- Demander d'expliquer bri\u00e8vement
- Demander de r\u00e9p\u00e9ter la r\u00e8gle en mots simples
- Proposer un choix entre options

### Optimisation vocale
Le prompt est con\u00e7u pour la voix, donc :
- R\u00e9ponses courtes et naturelles
- Phras\u00e9 oral (pas \u00e9crit/litt\u00e9raire)
- Pas de markdown, pas de listes
- Pas de r\u00e9p\u00e9tition
- Une id\u00e9e \u00e0 la fois
- Rythme de tutorat naturel

### Langue
- Arabe standard moderne simplifi\u00e9
- Pas d'arabe litt\u00e9raire compliqu\u00e9
- Si l'enfant est confus, reformuler en arabe plus simple
- Phrases courtes, naturelles pour la parole orale

## Donn\u00e9es d'entr\u00e9e

Le tuteur peut recevoir via le contexte :
- Transcription de la voix de l'enfant
- OCR de pages du cahier Major
- Texte d'exercice
- Contexte de le\u00e7on (de `courses.json`)
- M\u00e9tadonn\u00e9es : classe, mati\u00e8re, le\u00e7on, difficult\u00e9

## Guide d'impl\u00e9mentation

### \u00c9tape 1 : Cr\u00e9er le prompt
Fichier `voiceTutorPrompt.js` exportant le system prompt en constante.

### \u00c9tape 2 : Client WebSocket Realtime
Fichier `voiceRealtimeClient.js` qui :
- Ouvre la connexion WebSocket
- Envoie `session.update` avec le prompt
- G\u00e8re l'envoi d'audio (PCM 16bit, 24kHz)
- Re\u00e7oit et joue l'audio de r\u00e9ponse
- G\u00e8re la d\u00e9connexion / reconnexion

### \u00c9tape 3 : \u00c9cran VoiceTutorScreen
- Bouton micro (push-to-talk ou d\u00e9tection automatique)
- Affichage de la transcription en temps r\u00e9el
- Mascotte chameau avec animation pendant que le tuteur parle
- Contexte de la le\u00e7on affich\u00e9 en haut

### \u00c9tape 4 : Navigation
- Accessible depuis le scan QR (option "Tuteur vocal" en plus du cours texte)
- Accessible depuis le profil (mode r\u00e9vision vocale)

## Contraintes sp\u00e9cifiques

- **Offline** : le tuteur vocal N\u00c9CESSITE internet (contrairement au reste de l'app). Afficher un message clair si pas de connexion.
- **Co\u00fbt** : l'API Realtime est co\u00fbteuse. Impl\u00e9menter un syst\u00e8me de cr\u00e9dits/limites.
- **Bruit** : les enfants utilisent l'app dans des environnements bruyants. Pr\u00e9f\u00e9rer push-to-talk.
- **Latence** : afficher la mascotte en animation de "r\u00e9flexion" pendant l'attente.

## Coh\u00e9rence avec le projet

Le tuteur vocal compl\u00e8te le syst\u00e8me existant :
- **Major** (texte, fran\u00e7ais) = mentor pour les sessions de quiz et les cours
- **Tuteur vocal** (voix, arabe) = compagnon pour la r\u00e9vision orale et la compr\u00e9hension
- Les deux utilisent le m\u00eame contenu (`courses.json`, `exercises.js`)
- Les deux partagent la m\u00eame philosophie : ne jamais donner la r\u00e9ponse, guider l'enfant
