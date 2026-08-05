# Kit de publication Play Store — Major 6AF

## Infos techniques
- **Package** : `mr.major.mobile`
- **Fichier à téléverser** : AAB de production (build EAS — lien dans la session)
- **Signature** : keystore gérée par EAS (compte Expo mmcheikh) — choisir « Google Play App Signing » à la première publication
- **Politique de confidentialité** : https://major-eval.vercel.app/confidentialite.html (⚠️ déployer major-web avant la soumission)

## Fiche (arabe — langue principale)
- **Titre (30 car. max)** : `ماجور — السادسة ابتدائي`
- **Description courte (80 car. max)** :
  `مراجعة السنة السادسة: دروس، تمارين، فيديوهات وألعاب — رفيق دفاتر ماجور`
- **Description complète** :

```
ماجور هو الرفيق الرقمي لدفاتر ماجور للسنة السادسة من التعليم الأساسي في موريتانيا.

📚 خمس مواد كاملة: الرياضيات، العلوم الطبيعية، اللغة العربية، التربية الإسلامية، التاريخ والجغرافيا والتربية المدنية.

✨ ماذا يقدّم التطبيق؟
• بطاقات مراجعة مختصرة لكل درس، بأسلوب معلّم يخاطب تلميذه
• تمارين وأسئلة اختيار من متعدد مع التصحيح الفوري
• ألعاب تعليمية ممتعة لكل وحدة في الرياضيات
• فيديوهات شرح متحركة بالعربية الفصحى
• مسح رمز QR من صفحات الدفتر للوصول مباشرة إلى الدرس
• رمز التلميذ MAJ ليتابع الأستاذ ووليّ الأمر تقدّم الطفل

🔒 بدون إعلانات، وبدون أي مشتريات داخل التطبيق.
📱 المحتوى مدمج في التطبيق ويعمل دون إنترنت (ما عدا الفيديوهات).

بالتوفيق لجميع تلاميذنا!
```

- **Langue secondaire (français)** :
  - Titre : `Major — 6AF Mauritanie`
  - Courte : `Révision 6ᵉ année fondamentale : leçons, quiz, vidéos et jeux éducatifs`

## Questionnaires Play Console
- **Audience cible** : 9-12 ans (+ cocher 6-8 si proposé) → appli « conçue pour les enfants » → programme Familles
- **Classification du contenu** : questionnaire IARC → Éducation, aucune violence, aucun contenu sensible → PEGI 3
- **Sécurité des données** :
  - Données collectées : « Progression dans l'app » (associée à un pseudo/code, pas à une identité)
  - Auth : anonyme (Firebase) — pas de données personnelles
  - Pas de partage avec des tiers, pas de collecte de localisation/contacts/photos
  - Données chiffrées en transit : oui (HTTPS) ; suppression sur demande : oui (e-mail)
- **Publicité** : aucune
- **Permission caméra** : justification = « lecture des QR codes imprimés dans les cahiers Major pour ouvrir la leçon correspondante »

## Visuels requis
- Icône 512×512 : `apps/major-mobile/assets/icon.png` (vérifier la taille)
- Bannière « feature graphic » 1024×500 : à générer (logo Major + slogan sur fond navy/or)
- Captures d'écran (min 2) : accueil, liste des leçons, une leçon avec vidéo, un jeu, un quiz — à prendre sur le téléphone ou l'émulateur

## Étapes dans la console (compte existant)
1. « Créer une application » → nom `ماجور — السادسة ابتدائي`, langue par défaut arabe, gratuit
2. Renseigner la fiche (textes ci-dessus + visuels)
3. Questionnaires : audience, contenu, sécurité des données
4. Production → « Créer une release » → téléverser l'AAB → laisser Google gérer la signature
5. Soumettre pour examen (appli enfants : examen parfois plus long, quelques jours)

## Après publication
- OTA : les mises à jour du canal `production` se publient avec
  `npx eas-cli update --branch production --message "..."` (indépendant du canal preview des testeurs)
