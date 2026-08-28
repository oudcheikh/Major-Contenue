# -*- coding: utf-8 -*-
"""Grammaire 6AF — 15 leçons riches (cours + exemples corrigés + 6 exercices)."""
from base_fr import make_unit, OVS, dots, q_lignes


UNITS_GRAM = [

make_unit(dict(
    num=1, title='Les types de phrases',
    sub='Déclarative · interrogative · exclamative · impérative',
    learn_badge='Quatre types, quatre intentions',
    t1='Les quatre types de phrases',
    t2='Je reconnais et je transforme — corrigé',
    t3='Exercices — nommer le type',
    t4='Exercices — transformer et inventer',
    objectifs=[
        'Reconnaître les 4 types de phrases et l’intention de celui qui parle.',
        'Utiliser la ponctuation et le mode du verbe comme indices.',
        'Transformer une phrase d’un type à un autre sans changer le sens essentiel.',
    ],
    rules=[
        'Une <span class="hl">phrase déclarative</span> informe. Elle se termine par un <b>point</b>. <i>Fatimata va au marché de Nouakchott.</i>',
        'Une <span class="hl">phrase interrogative</span> pose une question. Elle se termine par <b>?</b>. On utilise <i>est-ce que</i>, un mot interrogatif (<i>qui, où, quand…</i>) ou l’inversion : <i>Fatimata va-t-elle au marché ?</i>',
        'Une <span class="hl">phrase exclamative</span> exprime un sentiment (joie, surprise, colère). Elle se termine par <b>!</b>. <i>Quel beau marché !</i>',
        'Une <span class="hl">phrase impérative</span> donne un <b>ordre</b>, un conseil ou une interdiction. Le verbe est à l’<b>impératif</b> (souvent sans sujet). <i>Va au marché. N’oublie pas tes ouguiyas.</i>',
    ],
    table=(['Type', 'On veut…', 'Fin', 'Exemple (Mauritanie)'], [
        ['Déclarative', 'informer', '.', 'Les pêcheurs partent de Nouadhibou.'],
        ['Interrogative', 'demander', '?', 'Partent-ils de Nouadhibou ?'],
        ['Exclamative', 'un sentiment', '!', 'Quelle mer magnifique !'],
        ['Impérative', 'un ordre / un conseil', '. ou !', 'Rentrez avant la chaleur.'],
    ]),
    methode=('Comment trouver le type ?', [
        'Je lis jusqu’au bout et je note la <b>ponctuation finale</b> (. ? !).',
        'Je cherche un <b>ordre</b> (verbe à l’impératif, souvent sans <i>je / tu / il</i>) ou une <b>question</b> (<i>est-ce que</i>, inversion, mot en <i>qu-</i>).',
        'Je nomme le type : déclarative, interrogative, exclamative ou impérative.',
    ]),
    astuce='Une phrase qui commence par « Quel / Quelle / Que » et qui finit par ! est presque toujours exclamative : <i>Quelle chaleur à Atar !</i>',
    worked=[
        ('Exemple 1 — Je reconnais',
         '''<i>Ahmed rentre-t-il de l’école à Tevragh Zeina ?</i>
         <ol>
           <li>Ponctuation : <b>?</b> → ce n’est pas une déclarative.</li>
           <li>Inversion du sujet (<i>rentre-t-il</i>) → on pose une question.</li>
           <li><b>Réponse : phrase interrogative.</b></li>
         </ol>'''),
        ('Exemple 2 — Je transforme les 4 types',
         '''Phrase de départ : <i>Mariem prépare le couscous.</i> (déclarative)
         <ol>
           <li>Interrogative : <i>Mariem prépare-t-elle le couscous ?</i> / <i>Est-ce que Mariem prépare le couscous ?</i></li>
           <li>Exclamative : <i>Comme Mariem prépare bien le couscous !</i></li>
           <li>Impérative (on s’adresse à Mariem) : <i>Prépare le couscous, Mariem.</i></li>
         </ol>'''),
        ('Exemple 3 — Piège fréquent',
         '''<i>Tu ranges tes dattes.</i> = déclarative (sujet <b>tu</b> + point).<br>
         <i>Range tes dattes.</i> = impérative (pas de sujet, verbe à l’impératif).<br>
         Ce n’est <b>pas</b> le même type, même si le sens est proche.'''),
    ],
    bulle=('fille', 'Lis à voix haute : si ta voix monte, c’est souvent une question. Si tu donnes un ordre, cherche l’impératif.'),
    attention='« Quel vent ! » n’est pas une question. Le point d’exclamation l’emporte : c’est une exclamative.',
    mini='''Consigne : indique le type de <i>Est-ce que tu bois l’ataya ?</i><br>
    On voit <b>est-ce que</b> + <b>?</b> → phrase <b>interrogative</b>.''',
    exos_a='Je nomme le type',
    exos=[
        ('⭐', 'Indique le type de chaque phrase (déclarative, interrogative, exclamative, impérative).<br>'
         + q_lignes([
             'Les pêcheurs partent de Nouadhibou.',
             'Ferme le cahier.',
             'Quelle chaleur à Atar !',
             'Le concours 6AF a lieu en juin.',
             'Où habites-tu, à Dar-Naim ou à Sebkha ?',
         ])),
        ('⭐', 'Même consigne.<br>'
         + q_lignes([
             'Écoute le maître.',
             'Est-ce que tu bois l’ataya ?',
             'Les dunes d’Akjoujt sont dorées.',
             'Ne cours pas dans la cour !',
             'Que cette mosquée est belle !',
         ])),
        ('⭐⭐', 'Transforme chaque phrase <b>en interrogative</b> (deux façons si tu peux : <i>est-ce que</i> et inversion).'
         + dots(1) +
         '<i>a) Mariem prépare le couscous.</i>' + dots(2) +
         '<i>b) Les élèves de Kaédi révisent.</i>' + dots(2)),
        ('⭐⭐', 'Transforme en <b>impérative</b>. Attention : on enlève souvent le sujet <i>tu / vous</i>.'
         + dots(1) +
         '<i>a) Tu ranges tes dattes dans le sac.</i>' + dots(1) +
         '<i>b) Vous fermez la porte de la classe.</i>' + dots(1) +
         '<i>c) Tu n’oublies pas tes ouguiyas.</i>' + dots(1)),
        ('⭐⭐⭐', '''Réécris ce petit texte en changeant le type de <b>chaque</b> phrase
        (décl. → interr. · interr. → décl. · excl. → décl.).<br>
        <i>Le fleuve Sénégal est large à Rosso. Fait-il trop chaud ? Quelle foule au marché !</i>''' + dots(2)),
        ('⭐⭐⭐', 'Écris <b>une phrase de chaque type</b> sur l’école de ton quartier. Souligne la ponctuation finale.'
         + dots(2)),
    ],
    defi='Écris un mini-dialogue (4 répliques) entre deux élèves avant le concours : tu dois utiliser les 4 types.',
    defi_lines=1,
)),

make_unit(dict(
    num=2, title='Phrase simple et phrase complexe',
    sub='Compter les verbes conjugués',
    learn_badge='Un verbe ou plusieurs ?',
    t1='Phrase simple et phrase complexe',
    t2='Je compte les verbes — corrigé',
    t3='Exercices — classer les phrases',
    t4='Exercices — construire une phrase complexe',
    objectifs=[
        'Distinguer phrase simple et phrase complexe.',
        'Repérer tous les verbes conjugués (pas l’infinitif ni le participe seul).',
        'Construire une phrase complexe à partir d’une phrase simple.',
    ],
    rules=[
        'Une <span class="hl">phrase simple</span> contient <b>un seul verbe conjugué</b>. <i>Sidi achète du poisson.</i> → 1 verbe → simple.',
        'Une <span class="hl">phrase complexe</span> contient <b>plusieurs verbes conjugués</b>. <i>Sidi achète du poisson et sa sœur prépare le riz.</i> → 2 verbes → complexe.',
        'Chaque verbe conjugué forme une <span class="hl">proposition</span>. Donc : 1 verbe = 1 proposition ; 2 verbes = 2 propositions.',
        'Ne compte pas l’<b>infinitif</b> (<i>acheter, partir</i>) ni un participe employé comme adjectif. Compte : <i>achète, part, est, a, va…</i>',
    ],
    table=(['Phrase', 'Verbes conjugués', 'Type'], [
        ['Les chameaux traversent le désert.', 'traversent', 'simple'],
        ['Les chameaux traversent le désert quand le soleil se lève.', 'traversent, se lève', 'complexe'],
        ['Khadijetou veut réussir le concours.', 'veut', 'simple (réussir = infinitif)'],
        ['Quand le vent souffle, les dunes bougent.', 'souffle, bougent', 'complexe'],
    ]),
    methode=('La méthode en 3 temps', [
        'Je souligne <b>tous les verbes conjugués</b> (je les « cherche » : qui fait quoi ?).',
        'Je compte : 1 → phrase simple ; 2 ou plus → phrase complexe.',
        'Je vérifie que je n’ai pas compté un infinitif (<i>pour partir, il faut…</i>).',
    ]),
    astuce='Astuce concours : si tu vois <i>et / mais / parce que / quand / qui</i> entre deux verbes, tu as presque sûrement une phrase complexe.',
    worked=[
        ('Exemple 1',
         '''<i>Le maître entre dans la classe.</i>
         <ol><li>Verbe conjugué : <b>entre</b> (1 seul).</li>
         <li><b>Phrase simple.</b></li></ol>'''),
        ('Exemple 2',
         '''<i>Khadijetou lit et Mohamed écrit.</i>
         <ol><li>Verbes : <b>lit</b>, <b>écrit</b> (2).</li>
         <li><b>Phrase complexe</b> (2 propositions coordonnées par <i>et</i>).</li></ol>'''),
        ('Exemple 3 — piège de l’infinitif',
         '''<i>Oumar aime boire de l’eau fraîche.</i><br>
         <b>aime</b> est conjugué ; <b>boire</b> est un infinitif. → 1 verbe conjugué → <b>phrase simple</b>.'''),
    ],
    bulle=('garcon', 'Pour passer de simple à complexe, ajoute une raison, un moment ou une deuxième action : <i>parce que…, quand…, et…</i>'),
    attention='« Les élèves de 6AF révisent le français. » → un seul verbe (<i>révisent</i>). « de 6AF » n’est pas un verbe !',
    mini='''<i>Quand le vent souffle, les dunes bougent.</i><br>
    Verbes soulignés : <b>souffle</b>, <b>bougent</b> → 2 verbes → <b>phrase complexe</b>.''',
    exos_a='Je classe',
    exos=[
        ('⭐', 'Simple ou complexe ? Souligne le(s) verbe(s) dans ta tête, puis écris S ou C.<br>'
         + q_lignes([
             'Le maître entre dans la classe.',
             'Khadijetou lit et Mohamed écrit.',
             'Les dattes sèchent au soleil.',
             'Sidi achète du poisson puis il rentre.',
             'Nous voulons réussir.',
         ])),
        ('⭐', 'Même consigne.<br>'
         + q_lignes([
             'Les élèves de 6AF révisent le français.',
             'Quand le vent souffle, les dunes bougent.',
             'Fatimata prépare l’ataya pour les invités.',
             'Il fait chaud mais les enfants jouent.',
             'Le taxi s’arrête devant l’école.',
         ])),
        ('⭐⭐', 'Pour chaque phrase : 1) copie-la 2) souligne les verbes conjugués 3) écris simple ou complexe.'
         + dots(1) +
         '<i>a) Les chameaux traversent le désert.</i>' + dots(2) +
         '<i>b) Les chameaux traversent le désert quand le soleil se lève.</i>' + dots(2)),
        ('⭐⭐', 'Réécris chaque phrase <b>simple</b> en phrase <b>complexe</b> en ajoutant <i>parce que</i>.'
         + dots(1) +
         '<i>a) Oumar boit de l’eau.</i>' + dots(2) +
         '<i>b) Les pêcheurs rentrent tard.</i>' + dots(2)),
        ('⭐⭐⭐', '''Transforme cette phrase complexe en <b>deux phrases simples</b>.<br>
        <i>Le marché de Nouakchott s’ouvre tôt et les vendeuses installent les dattes.</i>''' + dots(2)),
        ('⭐⭐⭐', 'Écris : une phrase simple, puis une phrase complexe de <b>deux verbes</b>, puis une de <b>trois verbes</b>, toutes sur le marché de Nouakchott.'
         + dots(2)),
    ],
    defi='Dans un texte de 4 lignes sur ta journée d’école, mets au moins 3 phrases complexes. Souligne tous les verbes.',
    defi_lines=1,
)),

make_unit(dict(
    num=3, title='Propositions',
    sub='Juxtaposition · coordination · subordination',
    learn_badge='Comment les propositions se lient',
    t1='Lier les propositions',
    t2='Je nomme le lien — corrigé',
    t3='Exercices — reconnaître le lien',
    t4='Exercices — réécrire avec un autre lien',
    objectifs=[
        'Reconnaître juxtaposition, coordination et subordination.',
        'Mémoriser les mots outils : mais, ou, et, donc, or, ni, car / que, quand, parce que, si, qui…',
        'Réécrire une phrase en changeant le type de lien.',
    ],
    rules=[
        '<span class="hl">Juxtaposition</span> : les propositions sont collées par une <b>virgule</b>, un point-virgule ou un deux-points. <i>Il fait chaud, les enfants jouent dehors.</i>',
        '<span class="hl">Coordination</span> : un petit mot relie deux propositions de même niveau : <b>mais, ou, et, donc, or, ni, car</b> (tu peux retenir <b>Mais où est donc Ornicar ?</b>). <i>Il fait chaud <u>mais</u> les enfants jouent dehors.</i>',
        '<span class="hl">Subordination</span> : une proposition <b>dépend</b> de l’autre. Mots outils : <b>que, quand, parce que, si, qui, dont, où, comme, lorsque…</b> <i>Les enfants jouent <u>parce qu’</u>il fait chaud.</i>',
        'La proposition qui dépend s’appelle <span class="hl">subordonnée</span>. L’autre est la <span class="hl">principale</span>.',
    ],
    table=(['Lien', 'Outil typique', 'Au port de Nouadhibou'], [
        ['Juxtaposition', ',  ;  :', 'Les bateaux rentrent, les vendeurs crient.'],
        ['Coordination', 'et, mais, car…', 'Les bateaux rentrent et les vendeurs crient.'],
        ['Subordination', 'quand, parce que…', 'Les vendeurs crient quand les bateaux rentrent.'],
    ]),
    methode=('Pour nommer le lien', [
        'Je coupe la phrase aux verbes : combien de propositions ?',
        'S’il n’y a qu’une virgule (pas de mot de liaison) → juxtaposition.',
        'Si je vois <i>et, mais, car, donc…</i> → coordination. Si je vois <i>que, quand, parce que, si, qui…</i> → subordination.',
    ]),
    astuce='« car » = coordination (on peut souvent remplacer par « parce que », mais « car » n’introduit pas une subordonnée : les deux propositions restent « égales »).',
    worked=[
        ('Exemple 1',
         '''<i>Les bateaux rentrent, les vendeurs crient.</i><br>
         Deux propositions, séparées par une virgule, <b>aucun mot de liaison</b> → <b>juxtaposition</b>.'''),
        ('Exemple 2',
         '''<i>Les bateaux rentrent <b>et</b> les vendeurs crient.</i><br>
         Mot outil <b>et</b> (Mais où est donc Ornicar ?) → <b>coordination</b>.'''),
        ('Exemple 3',
         '''<i>Les vendeurs crient <b>quand</b> les bateaux rentrent.</i><br>
         <i>quand</i> = subordonnant. « quand les bateaux rentrent » dépend de « les vendeurs crient » → <b>subordination</b>.'''),
    ],
    bulle=('fille', 'Pour passer de la juxtaposition à la coordination, remplace la virgule par <i>et</i> ou <i>mais</i>.'),
    attention='« qui » et « que » introduisent souvent une subordonnée relative : <i>Le pêcheur qui rentre est fatigué.</i>',
    mini='''<i>Nous restons chez nous car il pleut à Rosso.</i><br>
    Mot outil <b>car</b> → <b>coordination</b>.''',
    exos_a='Je reconnais',
    exos=[
        ('⭐', 'Juxtaposition (J), coordination (C) ou subordination (S) ?<br>'
         + q_lignes([
             'Il fait chaud, les enfants jouent dehors.',
             'Il fait chaud mais les enfants jouent dehors.',
             'Les enfants jouent parce qu’il fait chaud.',
             'Le maître parle et les élèves écoutent.',
             'Quand le vent souffle, on ferme les fenêtres.',
         ])),
        ('⭐', 'Souligne le mot de liaison (s’il y en a un) et nomme le lien.<br>'
         + q_lignes([
             'Sidi vend du poisson ou il répare le filet.',
             'Le taxi klaxonne, les piétons traversent.',
             'Nous partons si le maître nous autorise.',
             'Les dunes sont belles car le soleil se couche.',
             'L’élève qui révise réussit.',
         ])),
        ('⭐⭐', 'Réécris chaque juxtaposition en <b>coordination</b> (choisis et / mais / car).'
         + dots(1) +
         '<i>a) Le vent souffle, le sable vole.</i>' + dots(2) +
         '<i>b) Le marché est plein, on trouve des dattes.</i>' + dots(2)),
        ('⭐⭐', 'Réécris en <b>subordination</b> avec <i>quand</i> ou <i>parce que</i>.'
         + dots(1) +
         '<i>a) Les vendeurs crient. Les bateaux rentrent.</i>' + dots(2) +
         '<i>b) Oumar boit. Il a soif.</i>' + dots(2)),
        ('⭐⭐⭐', '''Même idée, trois liens différents. Recopie et complète.<br>
        Idée : la chaleur à Atar / rester à l’ombre.<br>
        Juxtaposition : … &nbsp; Coordination : … &nbsp; Subordination : …''' + dots(2)),
        ('⭐⭐⭐', 'Écris un petit paragraphe (4 phrases) sur le port de Nouadhibou : 1 juxtaposition, 1 coordination, 1 subordination, 1 phrase simple.'
         + dots(2)),
    ],
    defi='Retiens « Mais où est donc Ornicar ? » et écris 7 mini-phrases, une pour chaque coordinateur.',
    defi_lines=1,
)),

make_unit(dict(
    num=4, title='Nature et fonction',
    sub='Classe du mot · rôle dans la phrase',
    learn_badge='Deux questions différentes',
    t1='Nature et fonction des mots',
    t2='Je ne mélange plus — corrigé',
    t3='Exercices — donner la nature',
    t4='Exercices — donner la fonction',
    objectifs=[
        'Distinguer la nature (classe du mot) et la fonction (rôle dans la phrase).',
        'Donner la nature des mots courants : nom, déterminant, adjectif, verbe, pronom, adverbe.',
        'Donner la fonction : sujet, COD, COI, attribut, complément du nom, CC.',
    ],
    rules=[
        'La <span class="hl">nature</span> répond à : « C’est <b>quoi</b> comme mot ? » Elle ne change pas si on déplace le mot. Ex. : <i>dattes</i> = <b>nom commun</b>.',
        'La <span class="hl">fonction</span> répond à : « À <b>quoi sert</b> ce mot dans <b>cette</b> phrase ? » Elle change selon la phrase. Ex. : dans <i>Fatimata vend des dattes</i>, <i>dattes</i> = <b>COD</b>.',
        'Natures utiles au 6AF : <b>nom, déterminant, adjectif qualificatif, verbe, pronom, adverbe, préposition, conjonction</b>.',
        'Fonctions utiles : <b>sujet, COD, COI, attribut du sujet, complément du nom, complément circonstanciel</b>.',
    ],
    table=(['Mot dans la phrase', 'Nature', 'Fonction'], [
        ['Fatimata vend des dattes.', 'Fatimata = nom propre', 'sujet de vend'],
        ['Fatimata vend des dattes.', 'vend = verbe', 'noyau du groupe verbal'],
        ['Fatimata vend des dattes.', 'dattes = nom commun', 'COD de vend'],
        ['Les dattes sont sucrées.', 'sucrées = adjectif', 'attribut du sujet'],
    ]),
    methode=('Deux colonnes dans la tête', [
        'Je pose d’abord la question <b>nature</b> : nom ? verbe ? adjectif ?…',
        'Ensuite seulement la question <b>fonction</b> : qui fait l’action ? qui / quoi ? à qui ?',
        'Je n’écris jamais « sujet » dans la colonne nature, ni « nom » dans la colonne fonction.',
    ]),
    astuce='Le même mot change de fonction, pas de nature : <i>Le maître explique.</i> (maître = sujet) / <i>Nous écoutons le maître.</i> (maître = COD). Nature = nom dans les deux cas.',
    worked=[
        ('Exemple 1 — nature',
         '''Phrase : <i>Le petit chameau avance lentement.</i>
         <ol>
           <li><i>Le</i> = déterminant &nbsp; <i>petit</i> = adjectif &nbsp; <i>chameau</i> = nom</li>
           <li><i>avance</i> = verbe &nbsp; <i>lentement</i> = adverbe</li>
         </ol>'''),
        ('Exemple 2 — fonction',
         '''Même phrase.
         <ol>
           <li><i>Le petit chameau</i> = <b>sujet</b> de <i>avance</i> (qui est-ce qui avance ?).</li>
           <li><i>lentement</i> = <b>CC de manière</b> (comment ?).</li>
         </ol>'''),
        ('Exemple 3 — le piège',
         '''On te dit : « Donne la fonction de <i>sucrées</i> dans <i>Les dattes sont sucrées.</i> »<br>
         Ce n’est pas « adjectif » (ça, c’est la nature). Fonction = <b>attribut du sujet</b>.'''),
    ],
    bulle=('garcon', 'Nature = la carte d’identité du mot. Fonction = son métier dans la phrase du jour.'),
    attention='Un infinitif peut avoir une fonction (COD) : <i>Il aime jouer.</i> Nature de <i>jouer</i> = verbe à l’infinitif ; fonction = COD de <i>aime</i>.',
    mini='''<i>Aïcha lit un livre.</i> Nature de <i>livre</i> = nom commun. Fonction = COD de <i>lit</i> (elle lit quoi ?).''',
    exos_a='La nature d’abord',
    exos=[
        ('⭐', 'Donne la <b>nature</b> de chaque mot souligné (dans ta copie, recopie le mot).<br>'
         + q_lignes([
             '<u>Fatimata</u> vend des dattes.',
             'Fatimata <u>vend</u> des dattes.',
             'Fatimata vend des <u>dattes</u>.',
             'Le <u>petit</u> chameau avance.',
             'Le chameau avance <u>lentement</u>.',
         ])),
        ('⭐', 'Donne la <b>fonction</b> du groupe en gras.<br>'
         + q_lignes([
             '<b>Fatimata</b> vend des dattes.',
             'Fatimata vend <b>des dattes</b>.',
             '<b>Le petit chameau</b> avance.',
             'Les dattes sont <b>sucrées</b>.',
             'Nous partons <b>à l’aube</b>.',
         ])),
        ('⭐⭐', 'Pour chaque mot, remplis : nature / fonction.'
         + dots(1) +
         '<i>a) Dans « Mohamed écrit une lettre », lettre = … / …</i>' + dots(2) +
         '<i>b) Dans « La lettre arrive », lettre = … / …</i>' + dots(2)),
        ('⭐⭐', 'Classe ces mots selon la nature : <i>Nouakchott, très, cahier, rouge, ils, dans, mais, réussir</i>.'
         + ' Tableau libre : nom · déterminant/pronom · adjectif · verbe · adverbe · prép./conj.'
         + dots(2)),
        ('⭐⭐⭐', '''Même mot, deux fonctions. Écris deux phrases avec le nom <b>maître</b> :
        1) sujet  2) COD. Indique la fonction sous le mot.''' + dots(2)),
        ('⭐⭐⭐', 'Analyse complète de : <i>Hier, la grande sœur de Mariem a préparé l’ataya.</i><br>'
         'Pour <i>Hier / grande / sœur / Mariem / a préparé / ataya</i> : nature et fonction.'
         + dots(2)),
    ],
    defi='Prends une phrase de ton cahier de leçons et fais le tableau Nature | Fonction pour 5 mots.',
    defi_lines=1,
)),

make_unit(dict(
    num=5, title='L’adjectif qualificatif',
    sub='Épithète · attribut · accord',
    learn_badge='Il précise le nom',
    t1='L’adjectif qualificatif',
    t2='Épithète ou attribut ? — corrigé',
    t3='Exercices — trouver et accorder',
    t4='Exercices — épithète et attribut',
    objectifs=[
        'Repérer l’adjectif qualificatif et le nom qu’il qualifie.',
        'Distinguer épithète (collé au nom) et attribut (après un verbe d’état).',
        'Accorder l’adjectif en genre et en nombre avec le nom.',
    ],
    rules=[
        'L’<span class="hl">adjectif qualificatif</span> donne une qualité du nom : couleur, taille, caractère… <i>une <b>grande</b> mosquée, des dunes <b>dorées</b></i>.',
        '<span class="hl">Épithète</span> : l’adjectif est collé au nom, dans le groupe nominal. <i>la <b>vieille</b> porte</i>. On peut souvent l’enlever : <i>la porte</i>.',
        '<span class="hl">Attribut du sujet</span> : l’adjectif est séparé du nom par un <b>verbe d’état</b> (être, sembler, devenir, rester, paraître…). <i>La porte est <b>vieille</b>.</i>',
        'Il s’<span class="hl">accorde</span> avec le nom : <i>un petit garçon / une petite fille / de petits chameaux / de petites dunes</i>.',
    ],
    table=(['Phrase', 'Adjectif', 'Rôle', 'Accord avec'], [
        ['la grande mosquée', 'grande', 'épithète', 'mosquée (f. s.)'],
        ['Les dunes sont dorées.', 'dorées', 'attribut', 'dunes (f. pl.)'],
        ['un beau port', 'beau', 'épithète', 'port (m. s.)'],
        ['Les filles deviennent sages.', 'sages', 'attribut', 'filles (f. pl.)'],
    ]),
    methode=('Épithète ou attribut ?', [
        'Je trouve l’adjectif, puis le nom dont il parle.',
        'S’il est <b>collé</b> au nom (éventuellement après) sans verbe d’état entre les deux → épithète.',
        'S’il y a <i>est, sont, semble, devient…</i> entre le nom et l’adjectif → attribut.',
    ]),
    astuce='Féminins irréguliers à retenir : beau → belle · nouveau → nouvelle · vieux → vieille · blanc → blanche · long → longue · gros → grosse.',
    worked=[
        ('Exemple 1',
         '''<i>La grande mosquée de Nouakchott est belle.</i>
         <ol>
           <li><i>grande</i> : collée à <i>mosquée</i> → <b>épithète</b>.</li>
           <li><i>belle</i> : après <i>est</i> → <b>attribut du sujet</b> (sujet = la grande mosquée).</li>
         </ol>'''),
        ('Exemple 2 — accord',
         '''On part de <i>un petit chameau blanc</i>.<br>
         Au féminin pluriel : <i>de petit<b>es</b> dunes blanc<b>hes</b></i>. On accorde <b>tous</b> les adjectifs.'''),
        ('Exemple 3',
         '''<i>Les pêcheurs semblent fatigués.</i> — <i>semblent</i> = verbe d’état. <i>fatigués</i> = attribut, accordé avec <i>pêcheurs</i> (m. pl.).'''),
    ],
    bulle=('fille', 'Si tu peux coller l’adjectif juste à côté du nom et enlever le verbe <i>être</i>, c’était un attribut : <i>Les dunes sont dorées</i> → <i>les dunes dorées</i>.'),
    attention='Après <i>avoir l’air, rester, demeurer, paraître</i>, l’adjectif est souvent attribut. Ne dis pas « épithète » trop vite.',
    mini='''<i>Une belle dune dorée borde Atar.</i> — <i>belle</i> et <i>dorée</i> sont deux <b>épithètes</b> de <i>dune</i> (f. s.) → <i>belle, dorée</i>.''',
    exos_a='Je repère et j’accorde',
    exos=[
        ('⭐', 'Souligne l’adjectif et indique le nom avec lequel il s’accorde.<br>'
         + q_lignes([
             'la grande mosquée',
             'des dunes dorées',
             'un vieux filet',
             'une petite fille sage',
             'les sacs lourds',
         ])),
        ('⭐', 'Accorde l’adjectif entre parenthèses.<br>'
         + q_lignes([
             'une (joli) ville',
             'une (blanc) robe',
             'la (nouveau) école',
             'une (vieux) maison',
             'des (beau) dunes',
         ])),
        ('⭐⭐', 'Épithète ou attribut ? Recopie la phrase et entoure le verbe d’état s’il y en a un.'
         + dots(1) +
         '<i>a) La mer est calme à Nouadhibou.</i>' + dots(1) +
         '<i>b) La mer calme brille.</i>' + dots(1) +
         '<i>c) Les élèves restent silencieux.</i>' + dots(1) +
         '<i>d) Les élèves silencieux écrivent.</i>' + dots(1)),
        ('⭐⭐', 'Réécris au féminin pluriel : <i>un grand marché animé · un beau chameau blanc · un nouveau cahier propre</i>.'
         + dots(2)),
        ('⭐⭐⭐', 'Corrige les accords : <i>une petit fille heureux ; la nouveau rue large ; des vieux portes belles.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Décris une vendeuse du marché de Nouakchott : 3 adjectifs épithètes et 2 adjectifs attributs, tous bien accordés.'
         + dots(2)),
    ],
    defi='Trouve 6 adjectifs autour de toi (classe, cour, rue) et fais une phrase épithète + une phrase attribut pour chacun.',
    defi_lines=1,
)),

make_unit(dict(
    num=6, title='Le nom complément du nom',
    sub='Préciser un nom avec de / à',
    learn_badge='Un nom qui précise un autre nom',
    t1='Le nom complément du nom',
    t2='Je trouve le complément — corrigé',
    t3='Exercices — repérer de / à',
    t4='Exercices — construire des GN',
    objectifs=[
        'Repérer le nom complément du nom (souvent introduit par de, du, des, d’, à).',
        'Le distinguer de l’adjectif et du COD.',
        'Enrichir un groupe nominal avec un complément du nom.',
    ],
    rules=[
        'Le <span class="hl">complément du nom</span> est un nom (ou un groupe nominal) qui précise un autre nom. <i>le sac <b>de dattes</b>, le maître <b>de français</b>, l’école <b>de Dar-Naim</b></i>.',
        'Il est souvent introduit par <b>de, d’, du, de la, des, à</b>. On pose la question : <b>de quoi ? de qui ? à quoi ?</b>',
        'Ce n’est pas un adjectif : on ne l’accorde pas avec le premier nom. <i>les sacs de datte<b>s</b></i> (dattes au pluriel si on parle de plusieurs fruits).',
        'Ce n’est pas un COD : le complément du nom dépend d’un <b>nom</b>, pas d’un verbe. Dans <i>il vend des dattes</i>, <i>des dattes</i> = COD de <i>vend</i>.',
    ],
    table=(['Groupe nominal', 'Nom principal', 'Complément du nom'], [
        ['le port de Nouadhibou', 'port', 'de Nouadhibou'],
        ['un verre d’ataya', 'verre', 'd’ataya'],
        ['la feuille de cahier', 'feuille', 'de cahier'],
        ['un maître à lunettes', 'maître', 'à lunettes'],
    ]),
    methode=('Pour le trouver', [
        'Je trouve un nom, puis je lis ce qui vient juste après avec <i>de / à</i>.',
        'Je pose : « un sac de quoi ? » Si la réponse est un nom → complément du nom.',
        'Je vérifie que ce groupe dépend du nom, pas du verbe.',
    ]),
    astuce='On peut souvent remplacer le complément du nom par un adjectif : <i>un maître de français</i> ≈ <i>un maître français</i> (le sens bouge un peu, mais le test aide).',
    worked=[
        ('Exemple 1',
         '''<i>Le sac de riz pèse lourd.</i>
         <ol>
           <li>Nom principal : <b>sac</b>.</li>
           <li><i>de riz</i> précise le sac → <b>complément du nom</b>.</li>
           <li>Sujet du verbe <i>pèse</i> = tout le GN <i>le sac de riz</i>.</li>
         </ol>'''),
        ('Exemple 2 — ne pas confondre avec le COD',
         '''<i>Fatimata vend des dattes du marché.</i><br>
         <i>des dattes</i> = COD de <i>vend</i> (elle vend quoi ?).<br>
         <i>du marché</i> = complément du nom <i>dattes</i> (des dattes de où / de quoi ?).'''),
        ('Exemple 3',
         '''<i>L’école des filles de Rosso</i> peut contenir <b>deux</b> compléments du nom à la suite : <i>des filles</i> complète <i>école</i> ; <i>de Rosso</i> complète <i>filles</i>.'''),
    ],
    bulle=('garcon', 'Si tu enlèves le complément du nom, la phrase reste correcte : <i>Le sac pèse lourd.</i> Tu as juste perdu une précision.'),
    attention='« beaucoup de dattes » : <i>de dattes</i> n’est pas complément d’un nom <i>beaucoup</i> (beaucoup est un indéfini). Au 6AF, on s’entraîne surtout sur nom + de + nom.',
    mini='''<i>Le maître de français explique la leçon.</i> — <i>de français</i> complète <b>maître</b> (pas le verbe).''',
    exos_a='Je repère',
    exos=[
        ('⭐', 'Souligne le complément du nom.<br>'
         + q_lignes([
             'le port de Nouadhibou',
             'un verre d’ataya',
             'la cour de l’école',
             'un sac de riz',
             'le concours de 6AF',
         ])),
        ('⭐', 'Complète avec un complément du nom qui a du sens.'
         + q_lignes([
             'le marché de …',
             'une tasse de …',
             'le maître de …',
             'la rive du …',
             'un chameau de …',
         ])),
        ('⭐⭐', 'Dans chaque phrase, dis si le groupe en gras est COD ou complément du nom.'
         + dots(1) +
         '<i>a) Il apporte <b>un sac de dattes</b>.</i>' + dots(1) +
         '<i>b) Le <b>sac de dattes</b> est lourd.</i>' + dots(1) +
         '<i>c) Elle vend <b>des dattes du jardin</b>.</i>' + dots(2)),
        ('⭐⭐', 'Enrichis ces noms avec un complément du nom, puis mets le GN dans une phrase.'
         + dots(1) +
         'école / filet / dune / fleuve' + dots(2)),
        ('⭐⭐⭐', 'Réécris en remplaçant l’adjectif par un complément du nom (ou l’inverse).<br>'
         '<i>une porte en bois · la chaleur atarienne · un pêcheur de Nouadhibou · une robe bleue</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Décris le marché de ton quartier avec 5 GN contenant chacun un complément du nom. Souligne-les.'
         + dots(2)),
    ],
    defi='Construis une « chaîne » de 4 noms : le cahier de l’élève de la classe de 6AF…',
    defi_lines=1,
)),

make_unit(dict(
    num=7, title='La proposition relative',
    sub='qui · que · où · dont',
    learn_badge='Une subordonnée qui complète un nom',
    t1='La proposition relative',
    t2='Qui, que, où, dont — corrigé',
    t3='Exercices — choisir le pronom',
    t4='Exercices — relier deux phrases',
    objectifs=[
        'Repérer une proposition relative et son antécédent.',
        'Choisir le pronom relatif : qui, que, où, dont.',
        'Relier deux phrases simples par une relative.',
    ],
    rules=[
        'La <span class="hl">proposition relative</span> complète un nom (l’<span class="hl">antécédent</span>). <i>L’élève <b>qui révise</b> réussit.</i> Antécédent = <i>élève</i>.',
        '<b>qui</b> = sujet du verbe de la relative. <i>le pêcheur <u>qui</u> rentre</i> (qui rentre ? le pêcheur).',
        '<b>que / qu’</b> = COD. <i>le poisson <u>que</u> Sidi vend</i> (Sidi vend quoi ? le poisson).',
        '<b>où</b> = lieu ou parfois temps. <i>la ville <u>où</u> j’habite</i>. &nbsp; <b>dont</b> = de qui / de quoi. <i>le cahier <u>dont</u> j’ai besoin</i> (j’ai besoin <b>de</b> ce cahier).',
    ],
    table=(['Pronom', 'Fonction dans la relative', 'Exemple'], [
        ['qui', 'sujet', 'l’enfant qui court'],
        ['que', 'COD', 'les dattes que Fatimata vend'],
        ['où', 'CC de lieu (souvent)', 'l’école où nous apprenons'],
        ['dont', 'complément introduit par de', 'le maître dont on parle'],
    ]),
    methode=('Quel pronom relatif ?', [
        'Je trouve l’antécédent (le nom juste avant).',
        'Je refais la phrase avec ce nom à la place du pronom : <i>le pêcheur rentre</i> → sujet → <b>qui</b>.',
        'Si j’ai besoin de <i>de</i> (<i>parler de, avoir besoin de, être fier de</i>) → <b>dont</b>.',
    ]),
    astuce='Test de <i>que</i> : on peut souvent le remplacer par <i>le / la / les / l’</i> dans une phrase simple : <i>Sidi vend le poisson</i> → <i>le poisson que Sidi vend</i>.',
    worked=[
        ('Exemple 1 — qui',
         '''<i>Le pêcheur rentre. Le pêcheur est fatigué.</i><br>
         On remplace le 2<sup>e</sup> « pêcheur » sujet par <b>qui</b> :<br>
         <i>Le pêcheur <b>qui rentre</b> est fatigué.</i>'''),
        ('Exemple 2 — que',
         '''<i>Fatimata vend des dattes. J’aime ces dattes.</i><br>
         J’aime quoi ? les dattes → COD → <b>que</b> :<br>
         <i>J’aime les dattes <b>que</b> Fatimata vend.</i>'''),
        ('Exemple 3 — dont / où',
         '''<i>Voici le cahier. J’ai besoin de ce cahier.</i> → <i>Voici le cahier <b>dont</b> j’ai besoin.</i><br>
         <i>Rosso est une ville. Le fleuve passe à Rosso.</i> → <i>Rosso est une ville <b>où</b> le fleuve passe.</i>'''),
    ],
    bulle=('fille', 'N’écris jamais *le pêcheur que rentre* : si le nom fait l’action, c’est <b>qui</b>.'),
    attention='<i>que</i> s’élide : <i>le livre qu’Ahmed lit</i>. <i>qui</i> ne s’élide pas.',
    mini='''<i>L’école où nous apprenons se trouve à Tevragh Zeina.</i> — antécédent = <b>école</b> ; pronom = <b>où</b> (lieu).''',
    exos_a='Je choisis qui / que / où / dont',
    exos=[
        ('⭐', 'Complète par qui ou que.<br>'
         + q_lignes([
             'L’élève … révise réussit.',
             'Les dattes … Fatimata vend sont sucrées.',
             'Le maître … explique est patient.',
             'Le texte … nous lisons est court.',
             'Les enfants … jouent habitent à Sebkha.',
         ])),
        ('⭐', 'Complète par où ou dont.<br>'
         + q_lignes([
             'Nouadhibou est le port … les bateaux rentrent.',
             'Voici le sac … j’ai besoin.',
             'Kaédi est la ville … coule le fleuve.',
             'Le chameau … on parle appartient à Sidi.',
             'L’année … tu auras le concours arrive vite.',
         ])),
        ('⭐⭐', 'Relie les deux phrases par une relative (qui ou que).'
         + dots(1) +
         '<i>a) Le taxi s’arrête. Le taxi est jaune.</i>' + dots(2) +
         '<i>b) J’ai acheté un cahier. Le cahier est neuf.</i>' + dots(2)),
        ('⭐⭐', 'Même consigne avec où ou dont.'
         + dots(1) +
         '<i>a) Atar est une ville. Il fait très chaud à Atar.</i>' + dots(2) +
         '<i>b) C’est un récit. Nous sommes fiers de ce récit.</i>' + dots(2)),
        ('⭐⭐⭐', 'Corrige : <i>Le pêcheur que rentre est fatigué. La dune qui nous voyons est haute. La classe dont nous travaillons est calme.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Écris 4 phrases sur ton quartier, une pour chaque pronom : qui, que, où, dont. Souligne l’antécédent.'
         + dots(2)),
    ],
    defi='Fais une phrase avec deux relatives : <i>L’élève qui… et que…</i>',
    defi_lines=1,
)),

make_unit(dict(
    num=8, title='Les pronoms',
    sub='Remplacer le nom sans le répéter',
    learn_badge='Éviter les répétitions',
    t1='Les pronoms personnels',
    t2='Je remplace le nom — corrigé',
    t3='Exercices — choisir le pronom',
    t4='Exercices — réécrire sans répétition',
    objectifs=[
        'Utiliser les pronoms personnels sujets et compléments.',
        'Remplacer un nom ou un GN par le bon pronom (le, la, les, lui, leur, en, y…).',
        'Éviter les répétitions dans un court texte.',
    ],
    rules=[
        'Un <span class="hl">pronom</span> remplace un nom déjà connu. <i>Fatimata vend des dattes. <b>Elle</b> les range.</i>',
        'Pronoms <b>sujets</b> : je, tu, il, elle, on, nous, vous, ils, elles.',
        'Pronoms <b>COD</b> : me, te, le, la, l’, nous, vous, les. <i>Je vois Sidi. → Je <b>le</b> vois.</i>',
        'Pronoms <b>COI</b> : me, te, lui, nous, vous, leur. <i>Je parle à Mariem. → Je <b>lui</b> parle.</i> &nbsp; <b>en</b> remplace de + nom. <b>y</b> remplace à / un lieu.',
    ],
    table=(['On remplace…', 'Pronom', 'Phrase'], [
        ['Fatimata (sujet)', 'elle', 'Elle prépare l’ataya.'],
        ['les dattes (COD)', 'les', 'Fatimata les vend.'],
        ['à Sidi (COI)', 'lui', 'Nous lui donnons le sac.'],
        ['au marché (lieu)', 'y', 'Nous y allons demain.'],
        ['des dattes (de + nom)', 'en', 'Elle en vend beaucoup.'],
    ]),
    methode=('Quel pronom ?', [
        'Je trouve le groupe à remplacer et sa fonction (sujet, COD, COI, lieu…).',
        'Je choisis la série : sujet / le-la-les / lui-leur / y / en.',
        'Je place le pronom <b>devant le verbe</b> (sauf à l’impératif affirmatif : <i>prends-les</i>).',
    ]),
    astuce='<i>leur</i> COI est invariable : <i>Je leur parle</i> (pas *leurs). <i>leurs</i> avec s = déterminant possessif : <i>leurs cahiers</i>.',
    worked=[
        ('Exemple 1 — COD',
         '''<i>Les élèves lisent le texte. Les élèves lisent le texte avec attention.</i> trop de répétitions !<br>
         → <i>Les élèves lisent le texte. Ils <b>le</b> lisent avec attention.</i><br>
         <i>le texte</i> = COD masculin singulier → <b>le</b>.'''),
        ('Exemple 2 — COI',
         '''<i>Le maître explique la leçon aux filles.</i><br>
         Je parle <b>à qui</b> ? aux filles → COI pluriel → <b>leur</b> :<br>
         <i>Le maître <b>leur</b> explique la leçon.</i>'''),
        ('Exemple 3 — y et en',
         '''<i>Nous allons à Rosso. Nous allons à Rosso en taxi.</i><br>
         → <i>Nous <b>y</b> allons en taxi.</i><br>
         <i>Tu veux des dattes ? J’ai des dattes.</i> → <i>J’<b>en</b> ai.</i>'''),
    ],
    bulle=('garcon', 'Le pronom COD se place avant le verbe : <i>Je les vois</i>, pas *Je vois les (sauf phrase incomplète).'),
    attention='Devant un verbe à l’infinitif : <i>Je vais le voir</i>. Devant un verbe pronominal, ne confonds pas <i>se</i> et <i>le</i>.',
    mini='''<i>Fatimata range ses livres. Elle les range dans le sac.</i> — <i>ses livres</i> (COD pluriel) → <b>les</b>.''',
    exos_a='Je remplace',
    exos=[
        ('⭐', 'Remplace le groupe souligné par un pronom sujet ou COD.<br>'
         + q_lignes([
             '<u>Fatimata</u> prépare l’ataya.',
             'Nous voyons <u>le maître</u>.',
             'Sidi vend <u>les poissons</u>.',
             '<u>Les dunes</u> brillent.',
             'J’écoute <u>Mariem</u>.',
         ])),
        ('⭐', 'Complète par le, la, les, lui ou leur.<br>'
         + q_lignes([
             'Les dattes ? Fatimata … vend au marché.',
             'À Mohamed ? Je … parle.',
             'La leçon ? Le maître … explique.',
             'Aux élèves ? Le maître … explique la leçon.',
             'Le fleuve ? On … voit depuis Rosso.',
         ])),
        ('⭐⭐', 'Réécris en remplaçant les répétitions par des pronoms.'
         + dots(1) +
         '<i>Aïcha va au marché. Aïcha achète des dattes. Aïcha donne des dattes à sa mère.</i>'
         + dots(2)),
        ('⭐⭐', 'Utilise y ou en.'
         + dots(1) +
         '<i>a) Tu vas à Nouadhibou ? Oui, je … vais.</i>' + dots(1) +
         '<i>b) Il reste des ouguiyas ? Oui, il … reste.</i>' + dots(1) +
         '<i>c) Vous parlez du concours ? Oui, nous … parlons.</i>' + dots(1)),
        ('⭐⭐⭐', 'Corrige : <i>Je vois les. Je parle à elle. Je leurs donne le cahier. Nous allons à y.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Raconte en 5 phrases ta matinée sans répéter les noms : utilise au moins elle, le, les, lui, y, en.'
         + dots(2)),
    ],
    defi='Transforme un dialogue du quotidien (acheter de l’ataya) en remplaçant tous les GN répétés par des pronoms.',
    defi_lines=1,
)),

make_unit(dict(
    num=9, title='Les adverbes',
    sub='Invariables · -ment · sens du verbe',
    learn_badge='Ils précisent le verbe',
    t1='Les adverbes',
    t2='Je repère et je forme — corrigé',
    t3='Exercices — trouver l’adverbe',
    t4='Exercices — former et employer',
    objectifs=[
        'Reconnaître un adverbe (souvent invariable, souvent en -ment).',
        'Dire ce qu’il précise : manière, temps, lieu, intensité, affirmation…',
        'Former un adverbe en -ment à partir d’un adjectif.',
    ],
    rules=[
        'L’<span class="hl">adverbe</span> précise un verbe, un adjectif ou un autre adverbe. <i>Il court <b>vite</b>. Elle est <b>très</b> sage. Il parle <b>trop vite</b>.</i>',
        'Il est presque toujours <span class="hl">invariable</span> : on n’ajoute pas de -s. On n’écrit pas *vites, *doucements.',
        'Beaucoup se terminent par <b>-ment</b> : <i>lentement, facilement, vraiment</i>. Formation : adjectif féminin + ment (<i>lent → lente → lentement</i> ; <i>heureux → heureuse → heureusement</i>).',
        'Autres adverbes fréquents : <b>hier, aujourd’hui, demain, ici, là, très, trop, bien, mal, beaucoup, peu, souvent, jamais, déjà</b>.',
    ],
    table=(['Adverbe', 'Il précise…', 'Exemple'], [
        ['vite, bien, lentement', 'la manière (comment ?)', 'Les ânes avancent lentement.'],
        ['hier, demain, déjà', 'le temps (quand ?)', 'Hier, nous avons révisé.'],
        ['ici, là, dehors', 'le lieu (où ?)', 'Reste ici, près du puits.'],
        ['très, trop, peu', 'l’intensité', 'Il fait trop chaud à Atar.'],
    ]),
    methode=('Est-ce un adverbe ?', [
        'Je peux souvent le déplacer ou le supprimer : <i>Il (vite) rentre.</i>',
        'Il ne s’accorde pas avec le nom. S’il s’accorde, c’est un adjectif : <i>une fille rapide</i> / <i>elle court rapidement</i>.',
        'Question : comment ? quand ? où ? combien ?',
    ]),
    astuce='Adjectif en -ant / -ent : prudent → prudemment (avec -emment). Courant → couramment.',
    worked=[
        ('Exemple 1',
         '''<i>Aujourd’hui, les élèves écoutent très attentivement.</i>
         <ol>
           <li><i>Aujourd’hui</i> = adverbe de temps.</li>
           <li><i>attentivement</i> = manière (comment ils écoutent).</li>
           <li><i>très</i> = intensité, il précise <i>attentivement</i>.</li>
         </ol>'''),
        ('Exemple 2 — formation',
         '''<i>calme → calme (déjà f.) → calmement</i><br>
         <i>heureux → heureuse → heureusement</i><br>
         <i>rapide → rapide → rapidement</i>'''),
        ('Exemple 3 — piège',
         '''<i>Les filles sont calmes.</i> → <i>calmes</i> = adjectif (accordé).<br>
         <i>Les filles parlent calmement.</i> → <i>calmement</i> = adverbe (invariable).'''),
    ],
    bulle=('fille', 'Si tu hésites entre adjectif et adverbe : l’adjectif se colle au nom et s’accorde ; l’adverbe se colle plutôt au verbe et ne bouge pas.'),
    attention='<i>tout</i> parfois s’accorde (<i>toute la classe, toutes les filles</i>). <i>très, trop, bien, vite</i> jamais.',
    mini='''<i>Le vent souffle fortement sur Kiffa.</i> — <i>fortement</i> = adverbe de manière, formé sur <i>forte</i>.''',
    exos_a='Je repère',
    exos=[
        ('⭐', 'Souligne les adverbes.<br>'
         + q_lignes([
             'Aujourd’hui, nous allons très vite à l’école.',
             'Hier, trop de vent soufflait ici.',
             'Elle écrit bien et lentement.',
             'Les chameaux avancent déjà loin.',
             'Ne parle jamais trop fort en classe.',
         ])),
        ('⭐', 'Adjectif ou adverbe ?<br>'
         + q_lignes([
             'une réponse juste',
             'il répond juste',
             'des élèves calmes',
             'ils écoutent calmement',
             'une fille rapide / elle court rapidement',
         ])),
        ('⭐⭐', 'Forme l’adverbe en -ment : calme, heureux, lent, vrai, prudent, facile.'
         + dots(2)),
        ('⭐⭐', 'Réécris en ajoutant un adverbe de manière, un de temps et un d’intensité.'
         + dots(1) +
         '<i>Les pêcheurs rentrent.</i>' + dots(2)),
        ('⭐⭐⭐', 'Corrige : <i>Ils parlent doucements. Elle court vites. Les élèves écoutent attentifsment.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Décris une tempête de sable à Atar avec au moins 6 adverbes différents. Souligne-les et indique leur sens (temps, lieu, manière, intensité).'
         + dots(2)),
    ],
    defi='Fais une liste de 10 adverbes de ta vie quotidienne (maison, école, marché) classés par sens.',
    defi_lines=1,
)),

make_unit(dict(
    num=10, title='Le sujet du verbe',
    sub='Qui est-ce qui ? · accord',
    learn_badge='Qui fait l’action ?',
    t1='Le sujet du verbe',
    t2='Je trouve le sujet — corrigé',
    t3='Exercices — qui est-ce qui ?',
    t4='Exercices — sujets pièges',
    objectifs=[
        'Trouver le sujet en posant « qui est-ce qui ? / qu’est-ce qui ? ».',
        'Accorder le verbe avec le sujet (personne et nombre).',
        'Gérer sujet inversé, sujet éloigné, on et qui.',
    ],
    rules=[
        'Le <span class="hl">sujet</span> fait ou subit l’action. Question : <b>qui est-ce qui ?</b> / <b>qu’est-ce qui ?</b> + verbe. <i>Les pêcheurs partent.</i> Qui est-ce qui part ? → <b>les pêcheurs</b>.',
        'Le verbe s’accorde avec le sujet, pas avec le mot le plus proche. <i>Le tas de dattes <b>est</b> prêt.</i> (sujet = le tas).',
        '<b>on</b> → 3<sup>e</sup> personne du singulier. <i>On <b>révise</b>.</i> &nbsp; <b>qui</b> s’accorde avec l’antécédent : <i>les filles qui <b>chantent</b></i>.',
        'Sujet inversé : le sujet est après le verbe. <i>Là <b>passent</b> des taxis.</i> Dans la cour jouent les enfants.',
    ],
    table=(['Phrase', 'Sujet', 'Verbe accordé'], [
        ['Le maître explique.', 'Le maître', 'explique (3e s.)'],
        ['Les sacs de riz arrivent.', 'Les sacs', 'arrivent (3e pl.)'],
        ['On écoute le maître.', 'On', 'écoute (3e s.)'],
        ['Dans la cour jouent les enfants.', 'les enfants', 'jouent (3e pl.)'],
    ]),
    methode=('La chasse au sujet', [
        'Je trouve le verbe conjugué.',
        'Je pose « qui est-ce qui ? » / « qu’est-ce qui ? ».',
        'Je conjugue le verbe pour qu’il « ressemble » à ce sujet (je/tu/il… singulier/pluriel).',
    ]),
    astuce='Encadre le sujet : <i>c’est … qui</i>. <i>C’est le maître qui explique.</i> Si la phrase reste juste, tu as le bon sujet.',
    worked=[
        ('Exemple 1',
         '''<i>Les sacs de riz arrivent au port.</i>
         <ol>
           <li>Verbe : <i>arrivent</i>.</li>
           <li>Qu’est-ce qui arrive ? <b>les sacs</b> (pas le riz).</li>
           <li>Sujet pluriel → verbe au pluriel. On n’écrit pas *arrive.</li>
         </ol>'''),
        ('Exemple 2 — sujet éloigné',
         '''<i>Le maître des élèves de 6AF explique la leçon.</i><br>
         Sujet = <b>le maître</b> (singulier), même s’il y a « élèves » juste avant le verbe. → <i>explique</i>.'''),
        ('Exemple 3 — inversion',
         '''<i>Dans la cour de Tevragh Zeina jouent les enfants.</i><br>
         Qui est-ce qui joue ? <b>les enfants</b> → <i>jouent</i>. Le lieu n’est pas sujet.'''),
    ],
    bulle=('garcon', 'Le sujet peut être un pronom, un nom, un GN long, ou même un infinitif : <i>Réviser est utile.</i>'),
    attention='Dans une interrogative, le sujet peut être séparé : <i>Les pêcheurs partent-ils ?</i> Sujet = les pêcheurs (repris par ils).',
    mini='''<i>Là passent des taxis jaunes.</i> — qui est-ce qui passe ? <b>des taxis jaunes</b> → verbe pluriel <i>passent</i>.''',
    exos_a='Je trouve le sujet',
    exos=[
        ('⭐', 'Souligne le sujet, puis accorde le verbe entre parenthèses.<br>'
         + q_lignes([
             'Les dunes (être) dorées.',
             'Le maître (parler) doucement.',
             'On (revoir) la leçon.',
             'Fatimata et Aïcha (préparer) l’ataya.',
             'Le tas de dattes (être) prêt.',
         ])),
        ('⭐', 'Qui est-ce qui ? Écris le sujet complet.<br>'
         + q_lignes([
             'Dans la cour jouent les enfants.',
             'Là passent des taxis.',
             'Les sacs de farine pèsent lourd.',
             'Les filles qui chantent sont prêtes.',
             'Réussir demande du travail.',
         ])),
        ('⭐⭐', 'Choisis la bonne forme et justifie par le sujet.'
         + dots(1) +
         '<i>a) Le tas de dattes (est / sont) …</i>' + dots(1) +
         '<i>b) Les sacs de farine (pèse / pèsent) …</i>' + dots(1) +
         '<i>c) Le maître des élèves (explique / expliquent) …</i>' + dots(1)),
        ('⭐⭐', 'Réécris en mettant le sujet avant le verbe (tu « déboulonnes » l’inversion).'
         + dots(1) +
         '<i>a) Dans le port s’agitent les pêcheurs.</i>' + dots(2) +
         '<i>b) Ici commencent les dunes.</i>' + dots(2)),
        ('⭐⭐⭐', 'Corrige : <i>Les élèves de 6AF réussit. Les filles qui chante sont prêtes. On vont au marché. Là passe des chameaux.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Écris 4 phrases : 1 sujet GN long, 1 on, 1 qui + pluriel, 1 sujet inversé. Souligne chaque sujet.'
         + dots(2)),
    ],
    defi='Dictée express : invente 3 phrases où le mot juste avant le verbe n’est PAS le sujet. Accorde quand même juste.',
    defi_lines=1,
)),

make_unit(dict(
    num=11, title='L’attribut du sujet',
    sub='Verbes d’état · accord',
    learn_badge='Il dit ce qu’est le sujet',
    t1='L’attribut du sujet',
    t2='Je le distingue du COD — corrigé',
    t3='Exercices — verbes d’état',
    t4='Exercices — accorder l’attribut',
    objectifs=[
        'Reconnaître les verbes d’état : être, sembler, devenir, rester, paraître, avoir l’air…',
        'Trouver l’attribut du sujet (nom ou adjectif).',
        'Ne pas le confondre avec le COD, et l’accorder.',
    ],
    rules=[
        'L’<span class="hl">attribut du sujet</span> dit <b>ce qu’est</b> (ou devient, semble) le sujet. Il passe par un <span class="hl">verbe d’état</span>. <i>Sidi <b>est pêcheur</b>. Les dunes <b>sont dorées</b>.</i>',
        'Verbes d’état à retenir : <b>être, devenir, sembler, paraître, rester, demeurer, avoir l’air</b>.',
        'L’attribut peut être un <b>adjectif</b> (<i>dorées</i>) ou un <b>nom</b> (<i>pêcheur</i>). L’adjectif s’accorde avec le sujet.',
        'Test COD vs attribut : on ne peut pas transformer l’attribut en passif. <i>Sidi est pêcheur</i> → on ne dit pas *un pêcheur est été par Sidi. En revanche <i>Sidi vend du poisson</i> → passif possible.',
    ],
    table=(['Phrase', 'Verbe d’état', 'Attribut', 'Nature'], [
        ['Mariem est sage.', 'est', 'sage', 'adjectif'],
        ['Ahmed devient maître.', 'devient', 'maître', 'nom'],
        ['Les filles semblent prêtes.', 'semblent', 'prêtes', 'adjectif'],
        ['Le thé reste chaud.', 'reste', 'chaud', 'adjectif'],
    ]),
    methode=('Trouver l’attribut', [
        'Je vérifie que le verbe est un verbe d’état (pas un verbe d’action comme vendre, manger, voir).',
        'Je pose : le sujet est / semble / devient <b>quoi</b> ?',
        'J’accorde l’adjectif avec le sujet.',
    ]),
    astuce='On peut souvent coller l’attribut-adjectif au nom : <i>Les dunes sont dorées</i> → <i>les dunes dorées</i>. Avec un COD, ça ne marche pas : <i>Il mange une datte</i> → *il une datte ?',
    worked=[
        ('Exemple 1',
         '''<i>Les dunes d’Atar sont dorées.</i>
         <ol>
           <li>Verbe <i>sont</i> = être → verbe d’état.</li>
           <li>Les dunes sont <b>quoi</b> ? dorées → attribut.</li>
           <li>Accord avec <i>dunes</i> (f. pl.) → <i>dorées</i>.</li>
         </ol>'''),
        ('Exemple 2 — pas un COD',
         '''<i>Fatimata vend des dattes.</i> — <i>vend</i> = action. <i>des dattes</i> = COD (elle vend quoi ?).<br>
         <i>Fatimata est vendeuse.</i> — <i>est</i> = état. <i>vendeuse</i> = attribut.'''),
        ('Exemple 3',
         '''<i>Les élèves restent silencieux.</i> — <i>restent</i> verbe d’état. Attribut = <i>silencieux</i>, accordé avec <i>élèves</i> (m. pl.). Si on parle de filles : <i>silencieuses</i>.'''),
    ],
    bulle=('fille', 'Question magique : après <i>être / sembler / devenir</i>, ce qui vient est souvent l’attribut, pas le COD.'),
    attention='<i>avoir</i> n’est pas un verbe d’état : <i>Elle a une datte</i> → COD, pas attribut.',
    mini='''<i>Le poisson semble frais.</i> — verbe d’état <i>semble</i> ; attribut <i>frais</i> (accordé avec <i>poisson</i>, m. s.).''',
    exos_a='Je reconnais',
    exos=[
        ('⭐', 'Souligne l’attribut du sujet.<br>'
         + q_lignes([
             'Mariem est sage.',
             'Les dunes sont dorées.',
             'Ahmed devient maître.',
             'Le thé reste chaud.',
             'Les filles semblent prêtes.',
         ])),
        ('⭐', 'COD ou attribut ?<br>'
         + q_lignes([
             'Fatimata vend des dattes.',
             'Fatimata est vendeuse.',
             'Sidi a un filet.',
             'Sidi paraît fatigué.',
             'Nous écoutons le maître. / Nous sommes attentifs.',
         ])),
        ('⭐⭐', 'Accorde l’attribut.'
         + dots(1) +
         '<i>a) Les rues sont (calme) …</i>' + dots(1) +
         '<i>b) La mer devient (fort) …</i>' + dots(1) +
         '<i>c) Mes sœurs restent (silencieux) …</i>' + dots(1) +
         '<i>d) Cette dune paraît (haut) …</i>' + dots(1)),
        ('⭐⭐', 'Réécris en remplaçant le COD par un attribut (change le verbe si besoin).'
         + dots(1) +
         '<i>a) Oumar porte une djellaba blanche.</i> → Oumar est …' + dots(2) +
         '<i>b) Les pêcheurs ont l’air fatigué.</i> (déjà attribut : accorde et recopie)' + dots(1)),
        ('⭐⭐⭐', 'Corrige : <i>Les filles est prêtes. Sidi sont pêcheur. La mer semblent calme. Nous devenons sages.</i> (une est déjà juste : trouve-la)'
         + dots(2)),
        ('⭐⭐⭐', 'Écris 5 phrases sur tes camarades avec 5 verbes d’état différents. Souligne chaque attribut.'
         + dots(2)),
    ],
    defi='Même idée, deux phrases : une avec attribut adjectif, une avec attribut nom. Ex. : <i>Mon père est … / Mon père est …</i>',
    defi_lines=1,
)),

make_unit(dict(
    num=12, title='Le COD',
    sub='Qui ? Quoi ? · le / la / les',
    learn_badge='Le complément d’objet direct',
    t1='Le COD du verbe',
    t2='Je le trouve et je le pronominalise — corrigé',
    t3='Exercices — qui ? quoi ?',
    t4='Exercices — le, la, les',
    objectifs=[
        'Trouver le COD avec les questions qui ? / quoi ? (sans préposition).',
        'Le distinguer du sujet, du COI et du CC.',
        'Le remplacer par le, la, l’, les.',
    ],
    rules=[
        'Le <span class="hl">COD</span> (complément d’objet direct) complète un verbe d’action <b>sans préposition</b> (sans à, de, dans…). Questions : <b>qui ?</b> ou <b>quoi ?</b> <i>Fatimata vend <b>des dattes</b>.</i> Elle vend quoi ?',
        'Le COD peut être un nom, un GN, un pronom, un infinitif. <i>Il aime <b>jouer</b>.</i>',
        'On peut souvent le remplacer par <b>le / la / l’ / les</b> : <i>Fatimata <b>les</b> vend.</i>',
        'Au passif, le COD de l’active devient sujet : <i>Les dattes sont vendues par Fatimata.</i>',
    ],
    table=(['Phrase', 'Verbe', 'COD', 'Question'], [
        ['Sidi répare le filet.', 'répare', 'le filet', 'répare quoi ?'],
        ['Nous écoutons le maître.', 'écoutons', 'le maître', 'écoutons qui ?'],
        ['Aïcha prépare l’ataya.', 'prépare', 'l’ataya', 'prépare quoi ?'],
        ['Ils veulent réussir.', 'veulent', 'réussir', 'veulent quoi ?'],
    ]),
    methode=('Trois tests', [
        'Question <b>qui / quoi</b> collée au verbe, sans à / de.',
        'Remplacement par le / la / les.',
        'Si je peux mettre au passif, c’était un COD.',
    ]),
    astuce='Les verbes d’état n’ont pas de COD : après <i>être</i>, cherche un attribut. <i>Il est pêcheur</i> ≠ COD.',
    worked=[
        ('Exemple 1',
         '''<i>Les élèves lisent le texte.</i>
         <ol>
           <li>Verbe d’action : lisent.</li>
           <li>Ils lisent <b>quoi</b> ? le texte → COD.</li>
           <li>Pronom : <i>Ils <b>le</b> lisent.</i></li>
         </ol>'''),
        ('Exemple 2 — pas un CC',
         '''<i>Les élèves lisent le texte dans la cour.</i><br>
         <i>le texte</i> = COD (quoi ?).<br>
         <i>dans la cour</i> = CC de lieu (où ?), introduit par <i>dans</i>.'''),
        ('Exemple 3',
         '''<i>Le maître explique la leçon aux élèves.</i><br>
         <i>la leçon</i> = COD (explique quoi ?).<br>
         <i>aux élèves</i> = COI (à qui ?). Deux compléments différents.'''),
    ],
    bulle=('garcon', 'Si tu vois à ou de devant le complément, ce n’est pas un COD. COD = collé au verbe, sans petit mot.'),
    attention='Certains verbes n’ont pas de COD : <i>Il dort. Les dunes brillent. Nous partons.</i> (verbes intransitifs).',
    mini='''<i>Nous voyons la mer à Nouadhibou.</i> — voyons <b>quoi</b> ? <i>la mer</i> = COD. <i>à Nouadhibou</i> = CC de lieu.''',
    exos_a='Je pose la question',
    exos=[
        ('⭐', 'Souligne le COD. S’il n’y en a pas, écris « pas de COD ».<br>'
         + q_lignes([
             'Sidi répare le filet.',
             'Les dunes brillent.',
             'Nous écoutons le maître.',
             'Aïcha prépare l’ataya.',
             'Le taxi s’arrête.',
         ])),
        ('⭐', 'Remplace le COD par le, la, l’ ou les.<br>'
         + q_lignes([
             'Fatimata vend les dattes. → Fatimata … vend.',
             'Je vois Mohamed. → Je … vois.',
             'Nous lisons la leçon. → Nous … lisons.',
             'Tu fermes les fenêtres. → Tu … fermes.',
             'Elle aime l’école. → Elle … aime.',
         ])),
        ('⭐⭐', 'Dans chaque phrase, entoure le COD et le CC (s’il y en a). Nomme-les.'
         + dots(1) +
         '<i>a) Les pêcheurs salent le poisson sur le quai.</i>' + dots(2) +
         '<i>b) Mariem range ses cahiers dans le sac.</i>' + dots(2)),
        ('⭐⭐', 'Mets au passif (le COD devient sujet).'
         + dots(1) +
         '<i>a) Le maître corrige les cahiers.</i>' + dots(1) +
         '<i>b) Fatimata vend les dattes.</i>' + dots(1) +
         '<i>c) Les élèves lisent le texte.</i>' + dots(1)),
        ('⭐⭐⭐', 'COD, COI ou attribut ? Justifie.'
         + dots(1) +
         '<i>a) Sidi est pêcheur.</i>' + dots(1) +
         '<i>b) Sidi parle aux pêcheurs.</i>' + dots(1) +
         '<i>c) Sidi voit les pêcheurs.</i>' + dots(2)),
        ('⭐⭐⭐', 'Écris 6 phrases : 2 avec COD nom, 2 avec COD pronom, 2 sans COD. Souligne les COD.'
         + dots(2)),
    ],
    defi='Prends un verbe du marché (acheter, vendre, peser, compter) et construis une phrase COD + CC lieu + CC temps.',
    defi_lines=1,
)),

make_unit(dict(
    num=13, title='Le COI',
    sub='À qui ? De qui ? · lui / leur',
    learn_badge='Le complément d’objet indirect',
    t1='Le COI du verbe',
    t2='Lui ou leur ? — corrigé',
    t3='Exercices — à qui ? de qui ?',
    t4='Exercices — COD et COI ensemble',
    objectifs=[
        'Trouver le COI avec à qui ? / de qui ? / à quoi ? / de quoi ?',
        'Le distinguer du COD et du CC.',
        'Le remplacer par lui, leur, en, y.',
    ],
    rules=[
        'Le <span class="hl">COI</span> complète le verbe <b>avec une préposition</b>, souvent <b>à</b> ou <b>de</b>. Questions : <b>à qui ? de qui ? à quoi ? de quoi ?</b> <i>Je parle <b>à Mariem</b>.</i>',
        'Pronoms : <b>lui</b> (à lui / à elle, singulier), <b>leur</b> (à eux / à elles, pluriel). <i>Je <b>lui</b> parle. Je <b>leur</b> parle.</i>',
        '<b>en</b> remplace souvent <i>de + nom</i> : <i>Je parle du concours. → J’<b>en</b> parle.</i> &nbsp; <b>y</b> remplace souvent <i>à + chose / lieu</i> : <i>Je pense à Rosso. → J’<b>y</b> pense.</i>',
        'Beaucoup de verbes ont COD + COI : <i>Le maître explique <b>la leçon</b> (COD) <b>aux élèves</b> (COI).</i>',
    ],
    table=(['Phrase', 'Question', 'COI', 'Pronom'], [
        ['Je parle à Sidi.', 'à qui ?', 'à Sidi', 'lui'],
        ['Nous obéissons aux maîtres.', 'à qui ?', 'aux maîtres', 'leur'],
        ['Elle se souvient de Kaédi.', 'de quoi ?', 'de Kaédi', 'en'],
        ['Il pense à l’école.', 'à quoi ?', 'à l’école', 'y'],
    ]),
    methode=('COD ou COI ?', [
        'Je cherche une préposition <i>à / de</i> devant le complément de personne ou de chose.',
        'S’il n’y en a pas et que qui/quoi marche → COD.',
        'Je pronominalise : le/la/les = COD ; lui/leur = COI personne.',
    ]),
    astuce='<i>leur</i> COI ne prend jamais de s : <i>Je leur donne un cahier.</i> Le s de <i>leurs</i> n’apparaît que dans <i>leurs cahiers</i> (possessif).',
    worked=[
        ('Exemple 1',
         '''<i>Le maître explique la leçon aux filles de 6AF.</i>
         <ol>
           <li>explique <b>quoi</b> ? la leçon → COD.</li>
           <li>explique <b>à qui</b> ? aux filles → COI.</li>
           <li>Pronoms : <i>Il <b>la leur</b> explique.</i> (COD puis COI devant le verbe.)</li>
         </ol>'''),
        ('Exemple 2 — lui / leur',
         '''<i>Je donne un stylo à Mohamed.</i> → <i>Je <b>lui</b> donne un stylo.</i><br>
         <i>Je donne un stylo à Mohamed et à Sidi.</i> → <i>Je <b>leur</b> donne un stylo.</i>'''),
        ('Exemple 3 — pas un CC',
         '''<i>Je vais à Nouakchott.</i> — <i>à Nouakchott</i> = lieu (où ?) → <b>CC de lieu</b>, pas COI.<br>
         Le COI répond plutôt à <b>à qui / de qui</b> (une personne, parfois une chose liée au verbe : parler de, penser à).'''),
    ],
    bulle=('fille', 'Ordre des pronoms : me/te/nous/vous puis le/la/les puis lui/leur. Au 6AF, retiens surtout : <i>Je le lui donne. Je la leur explique.</i>'),
    attention='<i>téléphoner à, obéir à, plaire à, succéder à</i> se construisent avec un COI, jamais un COD.',
    mini='''<i>Aïcha offre des dattes à sa tante.</i> — COD = des dattes ; COI = à sa tante → <i>Elle <b>lui</b> offre des dattes</i> ou <i>Elle <b>les lui</b> offre</i>.''',
    exos_a='Je pose à qui / de qui',
    exos=[
        ('⭐', 'Souligne le COI.<br>'
         + q_lignes([
             'Je parle à Mariem.',
             'Nous obéissons au maître.',
             'Sidi téléphone à son frère.',
             'Elle se souvient de Rosso.',
             'Le maître explique la leçon aux élèves.',
         ])),
        ('⭐', 'Complète par lui ou leur.<br>'
         + q_lignes([
             'À Fatimata ? Je … donne le sac.',
             'Aux pêcheurs ? On … vend le sel.',
             'À ta sœur ? Tu … racontes l’histoire.',
             'Aux filles ? Le maître … parle.',
             'À Ahmed ? Nous … écrivons une lettre.',
         ])),
        ('⭐⭐', 'Réécris en remplaçant COD et/ou COI par des pronoms.'
         + dots(1) +
         '<i>a) Le maître explique la leçon aux élèves.</i>' + dots(2) +
         '<i>b) Fatimata donne les dattes à sa mère.</i>' + dots(2)),
        ('⭐⭐', 'COD, COI ou CC de lieu ?'
         + dots(1) +
         '<i>a) Nous allons à Kaédi.</i>' + dots(1) +
         '<i>b) Nous pensons à Kaédi.</i>' + dots(1) +
         '<i>c) Nous visitons Kaédi.</i>' + dots(2)),
        ('⭐⭐⭐', 'Corrige : <i>Je parle elle. Je leurs donne le livre. Je le donne à leur. J’y parle à Sidi.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Écris 4 phrases du type « quelqu’un donne / dit / explique quelque chose à quelqu’un », puis réécris-les avec des pronoms.'
         + dots(2)),
    ],
    defi='Fais la différence en deux phrases : <i>Je lui parle</i> / <i>Je le parle</i> — laquelle est juste, pourquoi ?',
    defi_lines=1,
)),

make_unit(dict(
    num=14, title='CC lieu, temps, manière',
    sub='Où ? Quand ? Comment ?',
    learn_badge='Les circonstances de l’action',
    t1='Compléments circonstanciels : lieu, temps, manière',
    t2='Je pose les bonnes questions — corrigé',
    t3='Exercices — où, quand, comment',
    t4='Exercices — déplacer et inventer',
    objectifs=[
        'Identifier un CC de lieu, de temps ou de manière.',
        'Savoir qu’on peut souvent le déplacer ou le supprimer.',
        'Enrichir une phrase avec les trois types.',
    ],
    rules=[
        'Un <span class="hl">complément circonstanciel</span> (CC) indique une circonstance de l’action. On peut souvent le <b>déplacer</b> ou l’<b>enlever</b> : la phrase reste correcte.',
        '<span class="hl">CC de lieu</span> : <b>où ?</b> <i>à Nouakchott, dans la cour, sur le quai, ici, près du puits</i>.',
        '<span class="hl">CC de temps</span> : <b>quand ?</b> <i>hier, à l’aube, en juin, pendant le ramadan, chaque matin</i>.',
        '<span class="hl">CC de manière</span> : <b>comment ?</b> <i>vite, avec soin, en silence, à pied, lentement</i>.',
    ],
    table=(['Question', 'Type', 'Exemples mauritaniens'], [
        ['Où ?', 'lieu', 'à Rosso, dans le désert, au port'],
        ['Quand ?', 'temps', 'hier, à 8 h, pendant la récréation'],
        ['Comment ?', 'manière', 'rapidement, à voix basse, avec joie'],
    ]),
    methode=('Pour classer un CC', [
        'Je pose où / quand / comment sur le verbe.',
        'Je vérifie que je peux déplacer le groupe : <i>Hier, Sidi est parti. / Sidi est parti hier.</i>',
        'Je ne le confonds pas avec un COD (qui/quoi sans préposition).',
    ]),
    astuce='Un adverbe peut être un CC à lui tout seul : <i>vite, hier, ici</i>. Un GN aussi : <i>le matin, la veille du concours</i>.',
    worked=[
        ('Exemple 1',
         '''<i>Hier, les pêcheurs sont rentrés lentement au port de Nouadhibou.</i>
         <ol>
           <li><i>Hier</i> = <b>temps</b> (quand ?).</li>
           <li><i>lentement</i> = <b>manière</b> (comment ?).</li>
           <li><i>au port de Nouadhibou</i> = <b>lieu</b> (où ?).</li>
         </ol>'''),
        ('Exemple 2 — déplacement',
         '''On peut écrire : <i>Les pêcheurs sont rentrés au port de Nouadhibou lentement, hier.</i><br>
         Les trois CC bougent ; le sujet et le verbe restent le cœur de la phrase.'''),
        ('Exemple 3 — pas un COD',
         '''<i>Nous visitons Nouakchott demain.</i><br>
         <i>Nouakchott</i> = COD (visitons quoi / qui ? une ville, sans préposition).<br>
         <i>demain</i> = CC de temps. Attention au piège « ville = forcément lieu ».'''),
    ],
    bulle=('garcon', 'Si tu peux enlever le groupe et que la phrase reste entière, c’est souvent un CC. Si tu l’enlèves et qu’il manque l’objet du verbe, c’était un COD.'),
    attention='<i>dans, sur, sous, chez, vers, en, à</i> introduisent souvent un CC de lieu, mais <i>à + personne</i> peut être un COI : <i>Je parle à Sidi</i>.',
    mini='''<i>À l’aube, les ânes avancent lentement vers Atar.</i> — temps : à l’aube ; manière : lentement ; lieu : vers Atar.''',
    exos_a='Je classe',
    exos=[
        ('⭐', 'Lieu, temps ou manière ?<br>'
         + q_lignes([
             'à Rosso',
             'hier soir',
             'lentement',
             'dans la cour',
             'avec soin',
             'en juin',
         ])),
        ('⭐', 'Souligne les CC et nomme-les.<br>'
         + q_lignes([
             'Les enfants jouent dans la cour.',
             'Nous révisons chaque soir.',
             'Sidi parle à voix basse.',
             'À midi, le marché se vide.',
             'Ils reviennent à pied.',
         ])),
        ('⭐⭐', 'Déplace le CC en tête de phrase (virgule derrière).'
         + dots(1) +
         '<i>a) Les dunes brillent le matin.</i>' + dots(1) +
         '<i>b) Les élèves écrivent avec application.</i>' + dots(1) +
         '<i>c) Le taxi s’arrête devant l’école.</i>' + dots(1)),
        ('⭐⭐', 'Enrichis : ajoute un CC de lieu, un de temps et un de manière.'
         + dots(1) +
         '<i>Les élèves révisent.</i>' + dots(2)),
        ('⭐⭐⭐', 'Dans chaque phrase, sépare COD et CC.'
         + dots(1) +
         '<i>a) Nous visitons Kaédi demain.</i>' + dots(1) +
         '<i>b) Elle range les cahiers rapidement dans le sac.</i>' + dots(2)),
        ('⭐⭐⭐', 'Raconte un trajet (maison → école) en 5 phrases. Chaque phrase doit avoir au moins 2 CC différents. Souligne-les et nomme-les.'
         + dots(2)),
    ],
    defi='Même action, 3 phrases : tu changes seulement les CC (lieu / temps / manière) pour raconter 3 moments de la journée.',
    defi_lines=1,
)),

make_unit(dict(
    num=15, title='CC but, cause, conséquence',
    sub='Pour · parce que · donc',
    learn_badge='Pourquoi ? Dans quel but ? Quel résultat ?',
    t1='But, cause, conséquence',
    t2='Je ne les mélange plus — corrigé',
    t3='Exercices — nommer le rapport',
    t4='Exercices — relier les phrases',
    objectifs=[
        'Distinguer but (objectif), cause (raison) et conséquence (résultat).',
        'Utiliser pour / afin de, parce que / car, donc / alors / si bien que.',
        'Transformer une cause en conséquence et inversement.',
    ],
    rules=[
        '<span class="hl">But</span> : dans quel objectif ? On n’a pas encore le résultat, on le vise. Outils : <b>pour, afin de, pour que</b>. <i>Il part tôt <b>pour</b> arriver à l’heure.</i>',
        '<span class="hl">Cause</span> : pour quelle raison ? Le fait est déjà là, il explique. Outils : <b>parce que, car, comme, puisque</b>. <i>Il boit <b>parce que</b> la chaleur est forte.</i>',
        '<span class="hl">Conséquence</span> : quel résultat ? Outils : <b>donc, alors, si bien que, c’est pourquoi</b>. <i>Il fait chaud, <b>donc</b> il reste à l’ombre.</i>',
        'Cause et conséquence sont les deux faces d’une même idée : <i>La mer est forte, donc le port est fermé</i> ⇔ <i>Le port est fermé parce que la mer est forte</i>.',
    ],
    table=(['Rapport', 'Question', 'Outils', 'Exemple'], [
        ['But', 'dans quel but ?', 'pour, afin de', 'Mariam révise pour réussir.'],
        ['Cause', 'pourquoi ?', 'parce que, car', 'Elle révise parce que le concours approche.'],
        ['Conséquence', 'et alors ?', 'donc, si bien que', 'Elle a révisé, donc elle est prête.'],
    ]),
    methode=('Trois questions', [
        'Est-ce un <b>objectif</b> (pas encore réalisé) → but.',
        'Est-ce une <b>raison</b> qui explique → cause.',
        'Est-ce un <b>résultat</b> qui suit → conséquence.',
    ]),
    astuce='<i>pour</i> + infinitif = souvent le but. <i>parce que</i> + verbe conjugué = cause. <i>donc</i> entre deux propositions = conséquence.',
    worked=[
        ('Exemple 1 — les trois sur le même thème',
         '''Thème : la chaleur à Atar.
         <ol>
           <li><b>But</b> : <i>Mariam boit beaucoup d’eau <u>pour</u> ne pas avoir soif.</i></li>
           <li><b>Cause</b> : <i>Elle boit <u>parce que</u> la chaleur est forte.</i></li>
           <li><b>Conséquence</b> : <i>La chaleur est forte, <u>donc</u> elle reste à l’ombre.</i></li>
         </ol>'''),
        ('Exemple 2 — transformation',
         '''Cause → conséquence :<br>
         <i>Le port est fermé parce que la mer est forte.</i><br>
         → <i>La mer est forte, donc le port est fermé.</i>'''),
        ('Exemple 3 — piège',
         '''<i>Il part tôt pour arriver à l’heure.</i> n’est <b>pas</b> une cause. Arriver à l’heure est l’objectif (but), pas la raison déjà vraie.<br>
         La cause serait : <i>Il part tôt parce que le taxi est rare.</i>'''),
    ],
    bulle=('fille', 'Pour le concours : si tu peux inverser avec « donc » / « parce que », tu es entre cause et conséquence. Le but, lui, se dit avec « pour ». '),
    attention='<i>car</i> = cause (comme parce que) mais c’est une <b>coordination</b>. <i>parce que</i> = subordination.',
    mini='''<i>Il part tôt pour arriver à l’heure.</i> — question : dans quel but ? → <b>but</b> (outil : pour + infinitif).''',
    exos_a='Je nomme le rapport',
    exos=[
        ('⭐', 'But, cause ou conséquence ?<br>'
         + q_lignes([
             'Il part tôt pour arriver à l’heure.',
             'Le vent souffle, donc le sable vole.',
             'Nous restons chez nous car il pleut à Rosso.',
             'Elle révise afin de réussir le 6AF.',
             'Comme il fait nuit, on rentre.',
         ])),
        ('⭐', 'Souligne l’outil et nomme le rapport.<br>'
         + q_lignes([
             'Les élèves sont fatigués parce qu’ils ont révisé tard.',
             'Ils ont révisé tard, si bien qu’ils sont fatigués.',
             'Oumar ouvre le robinet pour boire.',
             'Le maître parle plus fort, alors tout le monde entend.',
             'Puisque tu as fini, range ton cahier.',
         ])),
        ('⭐⭐', 'Relie par <b>parce que</b> (une seule phrase).'
         + dots(1) +
         '<i>a) Les élèves sont fatigués. Ils ont révisé tard.</i>' + dots(2) +
         '<i>b) Les vendeuses rentrent. Le marché ferme.</i>' + dots(2)),
        ('⭐⭐', 'Transforme la cause en conséquence (donc) et la conséquence en cause (parce que).'
         + dots(1) +
         '<i>a) Le port est fermé parce que la mer est forte.</i>' + dots(2) +
         '<i>b) Il fait trop chaud, donc on reste à l’ombre.</i>' + dots(2)),
        ('⭐⭐⭐', 'Même situation, trois phrases : but, cause, conséquence. Sujet : le concours 6AF / réviser le français.'
         + dots(2)),
        ('⭐⭐⭐', 'Rédige un paragraphe de 6 lignes sur une journée à Rosso en utilisant au moins une fois pour, parce que, car, donc, afin de. Souligne et nomme chaque rapport.'
         + dots(2)),
    ],
    defi='Explique à un camarade, en 4 lignes, la différence but / cause avec tes propres exemples (ataya, école, chameau…).',
    defi_lines=1,
)),

]
