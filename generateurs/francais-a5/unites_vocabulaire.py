# -*- coding: utf-8 -*-
"""Vocabulaire 6AF — 2 leçons riches (dictionnaire + polysémie)."""
from base_fr import make_unit, OVS, dots, q_lignes


UNITS_VOC = [

make_unit(dict(
    num=28, title='Utiliser le dictionnaire : définir un mot',
    sub='Nature · définition · exemple',
    learn_badge='Lire un article, en écrire un',
    t1='Définir un mot comme le dictionnaire',
    t2='Je rédige une définition — corrigé',
    t3='Exercices — lire un article',
    t4='Exercices — écrire des définitions',
    objectifs=[
        'Savoir ce qu’on trouve dans un article de dictionnaire (orthographe, nature, sens, exemple).',
        'Comprendre les abréviations : n. m., n. f., v., adj., adv., pl.',
        'Rédiger une définition claire : classe + caractéristique + exemple, sans répéter le mot.',
    ],
    rules=[
        'Un <span class="hl">article de dictionnaire</span> donne : l’<b>orthographe</b>, la <b>nature</b> (n. m., n. f., v., adj.), parfois le pluriel, le ou les <b>sens</b>, un <b>exemple</b>.',
        'Abréviations : <b>n. m.</b> nom masculin · <b>n. f.</b> nom féminin · <b>v.</b> verbe · <b>adj.</b> adjectif · <b>adv.</b> adverbe · <b>pl.</b> pluriel.',
        'Pour définir un nom : on dit d’abord la <b>classe</b> (c’est un / une …) puis la <b>caractéristique</b> qui le distingue. <i>Un chameau est un mammifère du désert, utilisé pour le transport.</i>',
        'On <b>n’emploie pas le mot</b> dans sa propre définition. *Un marché est un marché où on vend* ne sert à rien. On peut commencer par « C’est un lieu / un objet / une action qui… ».',
    ],
    table=(['Abréviation', 'Signification', 'Exemple'], [
        ['n. m. / n. f.', 'nom masculin / féminin', 'ouguiya n. f. · ataya n. m.'],
        ['v.', 'verbe', 'réviser v.'],
        ['adj.', 'adjectif', 'sablonneux adj.'],
        ['adv.', 'adverbe', 'hier adv.'],
    ]),
    methode=('Rédiger une définition', [
        'Je donne la nature (n. m., n. f., v., adj.).',
        'J’écris : c’est un / une … qui / que … (classe + trait distinctif).',
        'J’ajoute un exemple de ma vie (Mauritanie, école, maison).',
    ]),
    astuce='Si le mot a plusieurs sens, le dictionnaire les numérote 1. 2. 3. Tu choisis le sens qui correspond à ta phrase.',
    worked=[
        ('Exemple 1 — lire',
         '''<i>Ataya, n. m. : thé vert à la menthe, préparé en plusieurs verres, très courant en Mauritanie. Ex. : Le soir, on sert l’ataya aux invités.</i>
         <ol>
           <li>Nature : nom masculin.</li>
           <li>Définition : on dit ce que c’est (thé) + une précision (menthe, verres).</li>
           <li>Exemple : une phrase vraie du quotidien.</li>
         </ol>'''),
        ('Exemple 2 — mauvaise définition',
         '''<i>Un marché est un marché où on vend.</i> → on répète le mot, on n’apprend rien.<br>
         <b>Corrigé</b> : <i>Marché, n. m. : lieu public où l’on vend et achète des produits. Ex. : Au marché de Nouakchott, Fatimata vend des dattes.</i>'''),
        ('Exemple 3 — un verbe',
         '''<i>Réviser, v. : relire et s’entraîner pour mieux retenir une leçon. Ex. : Les élèves de 6AF révisent le français chaque soir.</i>'''),
    ],
    bulle=('garcon', 'Une bonne définition permet à quelqu’un qui ne connaît pas le mot de le comprendre. Si tu as besoin du mot pour l’expliquer, recommence.'),
    attention='Le genre se voit à l’article : <i>une ouguiya</i> (n. f.) même si on dit parfois « un » par erreur à l’oral. Au dictionnaire, respecte n. f.',
    mini='''Pour <b>dune</b> : <i>Dune, n. f. : colline de sable formée par le vent dans le désert. Ex. : Les dunes d’Atar sont dorées le soir.</i>''',
    exos_a='Je lis le dictionnaire',
    exos=[
        ('⭐', 'Que signifient ces abréviations ?<br>'
         + q_lignes(['n. f.', 'n. m.', 'v.', 'adj.', 'adv.', 'pl.'])),
        ('⭐', 'Classe (nom, verbe ou adjectif) puis propose le genre si c’est un nom.<br>'
         + q_lignes(['ouguiya', 'réviser', 'sablonneux', 'pirogue', 'réussir', 'calme'])),
        ('⭐⭐', 'Rédige une définition complète (nature + définition + exemple) pour : <b>dune</b> et <b>concours</b> (le concours 6AF).'
         + dots(2)),
        ('⭐⭐', 'Corrige ces mauvaises définitions, puis réécris-les bien.'
         + dots(1) +
         '<i>a) Un marché est un marché où on vend.</i>' + dots(2) +
         '<i>b) Réviser, c’est quand on révise.</i>' + dots(2)),
        ('⭐⭐⭐', 'Rédige l’article de dictionnaire de <b>pirogue</b> et de <b>ataya</b> (orthographe, nature, définition, exemple mauritanien).'
         + dots(2)),
        ('⭐⭐⭐', 'Choisis 3 mots de ta vie (école, maison, rue) et rédige 3 articles complets. N’utilise pas le mot dans la définition.'
         + dots(2)),
    ],
    defi='Ouvre un vrai dictionnaire (ou demande à un aîné). Recopie un article et souligne : nature, définition, exemple.',
    defi_lines=1,
)),

make_unit(dict(
    num=29, title='Les mots polysémiques',
    sub='Plusieurs sens · le contexte décide',
    learn_badge='Un mot, plusieurs vies',
    t1='Les mots polysémiques',
    t2='Je choisis le bon sens — corrigé',
    t3='Exercices — le sens selon la phrase',
    t4='Exercices — produire deux sens',
    objectifs=[
        'Comprendre qu’un mot polysémique a plusieurs significations.',
        'Choisir le bon sens grâce au contexte (les mots autour).',
        'Distinguer polysémie et homonymes (mer / mère / maire).',
        'Écrire deux phrases qui illustrent deux sens d’un même mot.',
    ],
    rules=[
        'Un mot <span class="hl">polysémique</span> a <b>plusieurs sens</b>, notés 1. 2. 3. dans le dictionnaire. <i>glace</i> = dessert / miroir / eau gelée.',
        'Le <span class="hl">contexte</span> (la phrase, la situation) indique le bon sens. On ne devine pas le sens tout seul, hors phrase.',
        'Ce n’est pas la même chose que les <span class="hl">homonymes</span> : des mots <b>différents</b> qui se prononcent pareil. <i>mer / mère / maire</i> · <i>ver / vers / vert / verre</i>. En polysémie, c’est <b>le même mot</b> (même orthographe).',
        'Au 6AF, on t’entraîne à : 1) dire le sens dans une phrase donnée 2) inventer une 2<sup>e</sup> phrase à l’autre sens.',
    ],
    table=(['Mot', 'Sens 1', 'Sens 2'], [
        ['banc', 'siège (banc de l’école)', 'groupe de poissons (banc près de Nouadhibou)'],
        ['feuille', 'd’un arbre', 'du cahier'],
        ['voler', 'dans les airs (oiseau)', 'dérober (voleur)'],
        ['glace', 'eau gelée / dessert froid', 'miroir'],
        ['opération', 'calcul en maths', 'acte à l’hôpital'],
        ['classe', 'salle / groupe d’élèves', 'catégorie (1re classe)'],
    ]),
    methode=('Trouver le bon sens', [
        'Je lis toute la phrase, pas seulement le mot.',
        'Je me demande : de quoi on parle ici (lieu, action, objet) ?',
        'Je reformule le mot par un synonyme qui irait dans cette phrase seulement.',
    ]),
    astuce='Si les deux sens ont un lien (la feuille de l’arbre et la feuille du cahier : une surface mince), c’est souvent de la polysémie. Les homonymes n’ont pas de lien de sens.',
    worked=[
        ('Exemple 1',
         '''<i>Il n’y a pas de glace dans le désert d’Atar.</i><br>
         Contexte : désert, chaleur → sens = <b>eau gelée</b> (pas le miroir, pas la crème glacée du congélateur… même si en ville on peut acheter une glace).'''),
        ('Exemple 2',
         '''<i>Écris sur une feuille.</i> → <b>feuille de papier</b> (cahier), pas la feuille du palmier.<br>
         Autre phrase : <i>Une feuille tombe du palmier.</i> → végétal.'''),
        ('Exemple 3 — homonyme ≠ polysémie',
         '''<i>mer / mère / maire</i> : trois mots, trois orthographes (ou presque), trois sens sans lien. Ce ne sont <b>pas</b> des sens d’un même mot polysémique.<br>
         <i>voler</i> (l’oiseau / le voleur) : un seul mot, deux sens → polysémie.'''),
    ],
    bulle=('fille', 'Quand tu ne comprends pas une phrase, ce n’est pas toujours que tu ne connais pas le mot : c’est parfois le mauvais sens que tu as mis.'),
    attention='Ne réponds jamais « ça veut dire voler » tout court. Dis : « ici, voler signifie … parce que … ».',
    mini='''<i>Le banc de l’école est en bois. / Un banc de poissons près de Nouadhibou.</i> — même mot <b>banc</b>, deux sens (siège / groupe).''',
    exos_a='Je lis le contexte',
    exos=[
        ('⭐', 'Quel est le sens du mot en gras dans cette phrase ?<br>'
         + q_lignes([
             'Il n’y a pas de <b>glace</b> dans le désert d’Atar.',
             'Écris sur une <b>feuille</b>.',
             'Le <b>banc</b> de l’école est cassé.',
             'L’oiseau <b>vole</b> au-dessus du port.',
             'La <b>classe</b> de 6AF révise.',
         ])),
        ('⭐', 'Même consigne, autre sens du même mot.'
         + q_lignes([
             'Je me regarde dans la <b>glace</b>.',
             'Une <b>feuille</b> tombe du palmier.',
             'Un <b>banc</b> de poissons passe près de Nouadhibou.',
             'On a <b>volé</b> le sac de Sidi.',
             'Ce ticket est de première <b>classe</b>.',
         ])),
        ('⭐⭐', 'Écris 2 phrases (2 sens) pour chaque mot : <b>voler</b> · <b>pierre</b> (rocher / prénom) · <b>thé</b> (boisson / plante) si tu peux, sinon un autre mot de ton choix.'
         + dots(2)),
        ('⭐⭐', 'Explique les 2 sens de <b>opération</b> (calcul / hôpital) et de <b>course</b> (courir / courses au marché). Une phrase chacun.'
         + dots(2)),
        ('⭐⭐⭐', 'Polysémie ou homonymes ? Justifie : <i>mer / mère</i> · <i>feuille</i> (arbre / papier) · <i>ver / verre</i> · <i>glace</i> (miroir / eau gelée).'
         + dots(2)),
        ('⭐⭐⭐', 'Trouve un mot polysémique de ta vie (thé, course, classe, maître, pièce, timbre…) et rédige un mini-article de dictionnaire avec 2 sens numérotés + 2 exemples mauritaniens.'
         + dots(2)),
    ],
    defi='En une semaine, note 5 mots polysémiques entendus à la maison ou en classe, avec la phrase et le sens.',
    defi_lines=1,
)),

]
