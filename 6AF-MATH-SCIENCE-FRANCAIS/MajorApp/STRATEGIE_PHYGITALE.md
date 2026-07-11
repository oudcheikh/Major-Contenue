# Strategie Phygitale: Cahier Intelligent + Mentor IA

## Flux implemente (MVP)
1. Scan QR dans `QRScannerScreen`.
2. Redirection vers `MentorFlowScreen`.
3. Accroche audio via TTS (`expo-speech`) avec ton familier.
4. Resume visuel (3 points max).
5. Micro-defi (QCM rapide) avec gain de credits.
6. Mise a jour du profil local (offline first): credits, niveau de savoir, suivi chapitre.
7. Suggestion de prof a domicile si echec repetitif (>=5 echecs consecutifs sur un chapitre).
8. Apercu de rapport parent hebdo (style WhatsApp) dans le profil.

## Contraintes terrain
- Offline first: stockage AsyncStorage.
- Low data: texte + TTS, pas de video.
- Multi-langues: Francais, Arabe, Hassanya (mode simplifie).

## Fichiers cle
- `src/screens/MentorFlowScreen.js`
- `src/utils/mentorEngine.js`
- `src/utils/phygitalStorage.js`
- `src/screens/QRScannerScreen.js`
- `src/screens/HomeScreen.js`
- `src/screens/ProfileScreen.js`
- `App.js`
