# -*- coding: utf-8 -*-
"""Orthographe 6AF — 6 leçons riches (règles, tests, dictées)."""
from base_fr import make_unit, OVS, dots, q_lignes


UNITS_ORTH = [

make_unit(dict(
    num=22, title='La ponctuation',
    sub='Point · virgule · ? ! · deux-points · dialogue',
    learn_badge='Les signes qui font respirer le texte',
    t1='La ponctuation',
    t2='Je ponctue un texte — corrigé',
    t3='Exercices — . ? ! et virgules',
    t4='Exercices — dialogue et texte',
    objectifs=[
        'Utiliser le point, le point d’interrogation, le point d’exclamation et la virgule.',
        'Ponctuer une énumération et un dialogue (deux-points, guillemets).',
        'Relire un texte sans majuscules ni points et le rétablir.',
    ],
    rules=[
        'Le <span class="hl">point</span> termine une phrase déclarative. Après le point, on met une <b>majuscule</b>.',
        '<b>?</b> termine une question. <b>!</b> une exclamation ou un ordre vif. On ne met pas de majuscule après ? ou ! s’il s’agit de la même réplique… mais une <b>nouvelle phrase</b> reprend la majuscule.',
        'La <span class="hl">virgule</span> sépare des mots, des groupes ou des propositions juxtaposées. Elle marque une petite pause. On ne met <b>pas</b> de virgule entre le sujet et le verbe.',
        'Les <span class="hl">deux-points</span> annoncent une explication, une énumération ou des paroles. Les <span class="hl">guillemets</span> encadrent les paroles : <i>Le maître dit : « Sortez vos cahiers. »</i>',
    ],
    table=(['Signe', 'Rôle', 'Exemple'], [
        ['.', 'fin d’une information', 'Les pêcheurs partent de Nouadhibou.'],
        ['?', 'question', 'Tu as tes dattes ?'],
        ['!', 'sentiment ou ordre', 'Quelle chaleur à Atar ! Ferme la porte !'],
        [',', 'pause / liste', 'Mohamed, Aïcha et Sidi révisent.'],
        [': « »', 'paroles / liste', 'Il a pris trois choses : un cahier, un stylo, une règle.'],
    ]),
    methode=('Pour ponctuer', [
        'Je lis à voix haute : pause longue → point ; pause courte → virgule ; voix qui monte → ? ; émotion → !.',
        'Je vérifie les majuscules après chaque point.',
        'Pour un dialogue : deux-points, guillemets, majuscule au début des paroles.',
    ]),
    astuce='Dans une liste de 3 éléments : A, B et C. Virgule entre A et B, <i>et</i> avant le dernier (sans virgule avant <i>et</i> en général).',
    worked=[
        ('Exemple 1 — . ? !',
         '''<i>Quel vent à Atar_  Tu as tes dattes_  Ferme la porte_</i><br>
         → <i>Quel vent à Atar<b> !</b> Tu as tes dattes<b> ?</b> Ferme la porte<b>.</b></i><br>
         (ordre calme = point ; on peut aussi mettre ! si l’ordre est vif).'''),
        ('Exemple 2 — virgules',
         '''<i>Mohamed Aïcha et Sidi révisent le français les maths et les sciences.</i><br>
         → <i>Mohamed, Aïcha et Sidi révisent le français, les maths et les sciences.</i>'''),
        ('Exemple 3 — dialogue',
         '''<i>Le maître dit Sortez le cahier</i><br>
         → <i>Le maître dit : « Sortez le cahier. »</i>'''),
    ],
    bulle=('garcon', 'Si tu enchaînes trois phrases sans point, le correcteur ne peut plus respirer — et toi non plus à l’oral.'),
    attention='Pas de virgule entre sujet et verbe : *Les élèves, révisent est faux. On écrit : Les élèves révisent.',
    mini='''<i>Fatimata demande : « Tu viens au marché ? » Quelle foule !</i> — deux-points + guillemets + ? puis phrase exclamative.''',
    exos_a='Je replace les signes',
    exos=[
        ('⭐', 'Ajoute . ? ou ! et la majuscule s’il manque.<br>'
         + q_lignes([
             'quel vent à Atar_',
             'tu as tes dattes_',
             'ferme la porte_',
             'le concours a lieu en juin_',
             'est-ce que tu viens à Rosso_',
         ])),
        ('⭐', 'Place les virgules.'
         + dots(1) +
         '<i>a) Mohamed Aïcha et Sidi révisent le français les maths et les sciences.</i>' + dots(2) +
         '<i>b) À Nouakchott on trouve du poisson des dattes du thé et du tissu.</i>' + dots(2)),
        ('⭐⭐', 'Ponctue le dialogue ( : « » ).'
         + dots(1) +
         '<i>a) Le maître dit Sortez le cahier</i>' + dots(2) +
         '<i>b) Aïcha demande Tu as tes ouguiyas</i>' + dots(2)),
        ('⭐⭐', 'Réécris avec deux-points et virgules.<br>'
         '<i>Il a pris trois choses un cahier un stylo une règle.</i>' + dots(2) +
         '<i>Le pêcheur a répondu la mer est forte aujourd’hui.</i>' + dots(2)),
        ('⭐⭐⭐', 'Ponctue tout le texte (majuscules comprises).<br>'
         '<i>est-ce que tu viens à rosso quelle joie partons vite le taxi attend déjà</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Écris un mini-dialogue de 6 répliques entre deux élèves avant le concours. Ponctue parfaitement ( ? ! : « » ).'
         + dots(2)),
    ],
    defi='Dictée à recopier sans faute de ponctuation : Le maître dit : « Qui a fini ? » Quelle joie ! Ahmed, Mariem et Sidi lèvent le doigt.',
    defi_lines=1,
)),

make_unit(dict(
    num=23, title='Homophones ce/se · ces/ses',
    sub='Tests de remplacement',
    learn_badge='Quatre petits mots, quatre tests',
    t1='ce / se · ces / ses',
    t2='Je teste et je choisis — corrigé',
    t3='Exercices — ce ou se',
    t4='Exercices — ces ou ses · dictée',
    objectifs=[
        'Choisir ce ou se grâce à un test de remplacement.',
        'Choisir ces ou ses (démonstratif / possessif).',
        'Relire une phrase mixte sans se tromper.',
    ],
    rules=[
        '<span class="hl">se</span> (s’) = <b>pronom</b>, toujours devant un verbe (ou entre auxiliaire et participe). Test : on sent l’action « sur soi ». <i>Elle <b>se</b> lève. Il <b>s’</b>habille. Ils se sont lavés.</i>',
        '<span class="hl">ce</span> = démonstratif. Devant un nom : <i><b>Ce</b> cahier</i>. Devant <i>être / sont</i> : <i><b>c’</b>est, <b>ce</b> sont</i>. Test : on peut souvent dire <i>cela / cet / cette</i>.',
        '<span class="hl">ses</span> = possessif (à lui / à elle). Test : on remplace par <b>les siens / les siennes</b>. <i>Fatimata range <b>ses</b> livres</i> (les siens).',
        '<span class="hl">ces</span> = démonstratif (ceux-ci / ceux-là). Test : on remplace par <b>les</b> ou on ajoute <i>-ci</i>. <i><b>Ces</b> livres sont neufs</i> (les livres-ci).',
    ],
    table=(['Forme', 'Nature', 'Test', 'Exemple'], [
        ['se / s’', 'pronom', 'devant un verbe', 'Aïcha se prépare.'],
        ['ce / c’', 'démonstratif', 'ce cahier / c’est', 'Ce matin, c’est l’ataya.'],
        ['ses', 'possessif', '→ les siens', 'Elle met ses sandales.'],
        ['ces', 'démonstratif', '→ les / ceux-ci', 'Ces sandales viennent du marché.'],
    ]),
    methode=('Les 4 tests', [
        'Devant un verbe conjugué sans nom entre les deux → souvent <b>se</b>.',
        'Devant un nom (matin, cahier, maître…) → <b>ce / cet / cette / ces</b>.',
        'On peut dire « les siens » → <b>ses</b>. On peut dire « ceux-ci » → <b>ces</b>.',
        'Je relis la phrase à voix haute.',
    ]),
    astuce='<i>c’est</i> s’écrit avec une apostrophe (ce + est). <i>s’est</i> = se + est (pronom + auxiliaire) : <i>Elle s’est levée.</i>',
    worked=[
        ('Exemple 1 — ce / se',
         '''<i>___ maître ___ lève tôt.</i><br>
         1) devant <i>maître</i> (nom) → <b>Ce</b> maître.<br>
         2) devant <i>lève</i> (verbe) → <b>se</b> lève.<br>
         <i>Ce maître se lève tôt.</i>'''),
        ('Exemple 2 — ces / ses',
         '''<i>Fatimata range ___ cahiers. ___ cahiers sont propres.</i><br>
         1) les siens → <b>ses</b> cahiers.<br>
         2) ceux-ci, les cahiers dont on parle → <b>Ces</b> cahiers sont propres.'''),
        ('Exemple 3 — phrase complète',
         '''<i>Ce matin, Aïcha se prépare. Elle met ses sandales. Ces sandales viennent du marché.</i><br>
         Les quatre formes, chacune à sa place.'''),
    ],
    bulle=('fille', 'Si tu hésites entre ces et ses, dis la phrase avec « les siens ». Si ça marche, c’est ses.'),
    attention='<i>Se soir</i> est toujours faux : soir est un nom → <b>Ce</b> soir. <i>L’enfant ce lave</i> est faux : lave est un verbe → <b>se</b> lave.',
    mini='''<i>Ce sont des pêcheurs. Le filet se déchire.</i> — <i>ce sont</i> (démonstratif + être) ; <i>se déchire</i> (pronom + verbe).''',
    exos_a='ce ou se',
    exos=[
        ('⭐', 'Complète par ce / c’ / se / s’.<br>'
         + q_lignes([
             '___ maître ___ lève tôt.',
             '___ matin, elle ___ prépare.',
             '___ est un chameau.',
             'L’enfant ___ lave.',
             '___ sont des dunes.',
         ])),
        ('⭐', 'Complète par ces ou ses.<br>'
         + q_lignes([
             'Fatimata range ___ cahiers.',
             '___ cahiers sont propres.',
             'Le pêcheur répare ___ filets.',
             'Regarde ___ bateaux au port !',
             'Mariem cherche ___ sandales. ___ sandales sont sous le lit.',
         ])),
        ('⭐⭐', 'Réécris sans faute.<br>'
         '<i>Se soir, ses dunes sont dorées. L’enfant ce lave. C’est ses dattes-ci que je veux. Elle s’est trompée : ce sont ces siennes.</i>'
         + dots(2)),
        ('⭐⭐', 'Dictée guidée : recopie en choisissant bien.<br>'
         '<i>Ces élèves se concentrent ; ce devoir est long ; ses parents attendent ; c’est bientôt le concours.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Inventé 8 phrases (2 ce, 2 se, 2 ces, 2 ses) sur l’ataya. Souligne les homophones.'
         + dots(2)),
        ('⭐⭐⭐', 'Explique pour chaque mot le test utilisé : <i>Ce soir, Sidi se souvient de ces jours où ses oncles arrivaient.</i>'
         + dots(2)),
    ],
    defi='Fais une carte mentale des 4 tests et colle un exemple mauritanien sous chaque mot.',
    defi_lines=1,
)),

make_unit(dict(
    num=24, title='L’accord en genre dans le GN',
    sub='Déterminant + nom + adjectif',
    learn_badge='Tout le groupe suit le nom',
    t1='L’accord en genre dans le groupe nominal',
    t2='Je forme le féminin — corrigé',
    t3='Exercices — accorder',
    t4='Exercices — réécrire au féminin',
    objectifs=[
        'Accorder déterminant et adjectif avec le nom en genre (et en nombre).',
        'Former le féminin des adjectifs courants, y compris les irréguliers.',
        'Repérer le nom noyau du GN pour accorder juste.',
    ],
    rules=[
        'Dans le <span class="hl">groupe nominal</span>, tout s’accorde avec le <b>nom</b> : déterminant + adjectif(s). <i>un petit chameau / une petite fille / de petits sacs / de petites dunes</i>.',
        'Féminin régulier : souvent <b>+ e</b>. <i>grand → grande, joli → jolie, lourd → lourde</i>. Si l’adjectif se termine déjà par e : <i>calme, jeune, rouge</i> → invariable au féminin.',
        'Irréguliers à retenir : <b>beau → belle</b>, <b>nouveau → nouvelle</b>, <b>vieux → vieille</b>, <b>blanc → blanche</b>, <b>long → longue</b>, <b>gros → grosse</b>, <b>doux → douce</b>, <b>faux → fausse</b>, <b>sec → sèche</b>.',
        'Le déterminant change : <i>le / la / les</i> · <i>un / une / des</i> · <i>ce / cette / ces</i> · <i>mon / ma / mes</i> (mais <i>mon école</i> devant une voyelle).',
    ],
    table=(['Masculin', 'Féminin', 'Masculin pluriel', 'Féminin pluriel'], [
        ['un petit cahier', 'une petite fille', 'de petits cahiers', 'de petites filles'],
        ['un beau port', 'une belle dune', 'de beaux ports', 'de belles dunes'],
        ['un nouveau maître', 'une nouvelle école', 'de nouveaux maîtres', 'de nouvelles écoles'],
        ['un vieux filet', 'une vieille porte', 'de vieux filets', 'de vieilles portes'],
    ]),
    methode=('Pour accorder', [
        'Je trouve le nom : masculin ou féminin ? singulier ou pluriel ?',
        'Je fais suivre le déterminant, puis chaque adjectif.',
        'Je vérifie les formes irrégulières (beau / nouveau / vieux / blanc…).',
    ]),
    astuce='Pour le genre d’un nom, remplace par il / elle : <i>la mosquée → elle</i> (féminin). <i>le marché → il</i> (masculin).',
    worked=[
        ('Exemple 1',
         '''<i>une (joli) ville · une (blanc) robe</i> → <b>une jolie ville</b> (déjà un e, + e quand même pour -i : jolie) · <b>une blanche robe</b> ou <i>une robe blanche</i>.'''),
        ('Exemple 2 — irréguliers',
         '''<i>la (nouveau) école · une (vieux) maison</i> → <b>la nouvelle école</b>, <b>une vieille maison</b>.'''),
        ('Exemple 3 — tout le GN',
         '''<i>un grand marché animé</i> au féminin : <i>une grand<b>e</b> place animé<b>e</b></i> (on change aussi le nom si besoin : marché est masculin, place est féminin). Ou : <i>une grande foire animée</i>.'''),
    ],
    bulle=('garcon', 'Accorde tous les adjectifs, pas seulement le premier : <i>une petite fille heureuse</i>, pas *heureuse sans e.'),
    attention='<i>des vieux portes</i> est doublement faux : portes = féminin pluriel → <b>de vieilles portes</b> (et <i>de</i> souvent devant adjectif pluriel).',
    mini='''<i>La grande mosquée, la vieille porte, une belle dune près d’Atar.</i> — trois féminins, trois adjectifs accordés.''',
    exos_a='J’accorde',
    exos=[
        ('⭐', 'Accorde l’adjectif.<br>'
         + q_lignes([
             'une (joli) ville',
             'une (blanc) robe',
             'la (nouveau) école',
             'une (vieux) maison',
             'une (gros) datte · une (doux) voix',
         ])),
        ('⭐', 'Choisis le déterminant (le / la / un / une / les / des).<br>'
         + q_lignes([
             '___ belle dune',
             '___ beau port',
             '___ vieilles portes',
             '___ nouveau cahier',
             '___ nouvelle rue',
         ])),
        ('⭐⭐', 'Réécris au féminin (change le nom si c’est un métier / un animal).'
         + dots(1) +
         '<i>a) un grand marché animé</i>' + dots(1) +
         '<i>b) un beau chameau blanc</i>' + dots(1) +
         '<i>c) un petit vendeur heureux</i>' + dots(1)),
        ('⭐⭐', 'Réécris au pluriel : <i>une belle dune dorée · un vieux filet troué · la nouvelle école propre</i>.'
         + dots(2)),
        ('⭐⭐⭐', 'Corrige : <i>une petit fille heureux ; la nouveau rue large ; des vieux portes belles ; un belle port calme.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Décris une vendeuse du marché (5 GN féminins, chacun avec au moins un adjectif accordé). Souligne déterminant, nom, adjectif.'
         + dots(2)),
    ],
    defi='Fiche des 8 adjectifs irréguliers : masculin / féminin / un exemple du quotidien.',
    defi_lines=1,
)),

make_unit(dict(
    num=25, title='Les mots invariables',
    sub='Adverbes · prépositions · conjonctions',
    learn_badge='Ceux qui ne prennent jamais de -s',
    t1='Les mots invariables',
    t2='Je ne leur ajoute rien — corrigé',
    t3='Exercices — repérer',
    t4='Exercices — corriger et employer',
    objectifs=[
        'Reconnaître les mots invariables (adverbes, prépositions, conjonctions).',
        'Ne jamais leur ajouter de marque de genre ou de nombre.',
        'Les employer dans des phrases justes (dictée).',
    ],
    rules=[
        'Un mot <span class="hl">invariable</span> ne change jamais de forme : pas de -e, pas de -s, pas de -nt d’accord.',
        'Ce sont surtout : les <b>adverbes</b> (<i>hier, très, bien, trop, ici, lentement</i>), les <b>prépositions</b> (<i>avec, dans, sur, pour, sans, sous, chez, vers</i>), les <b>conjonctions</b> (<i>mais, et, donc, or, ni, car, que, quand, si</i>).',
        'On n’écrit pas *biens, *trèses, *avecs, *pourses, *doucements (sauf si -ment fait déjà partie de l’adverbe : <i>doucement</i> est la bonne forme, invariable).',
        'Certains mots ressemblent à des adjectifs : <i>juste, fort, bas</i> peuvent être adjectifs (variables) <b>ou</b> adverbes (invariables). <i>une voix juste</i> / <i>il chante juste</i>.',
    ],
    table=(['Classe', 'Exemples à retenir', 'On n’écrit jamais'], [
        ['Adverbes', 'hier, aujourd’hui, très, trop, bien, mal, ici, là, déjà, souvent', '*biens *trèses *vites'],
        ['Prépositions', 'avec, dans, sur, sous, chez, pour, sans, entre, vers', '*avecs *danss *pours'],
        ['Conjonctions', 'mais, et, donc, car, ou, ni, que, quand, si', '(invariables)'],
    ]),
    methode=('Est-il invariable ?', [
        'Est-ce un nom, un adjectif, un verbe, un déterminant ? → souvent variable.',
        'Est-ce un petit mot de liaison ou un -ment / hier / très / dans ? → invariable.',
        'Je refuse d’ajouter un -s « pour faire joli » à la fin de la phrase.',
    ]),
    astuce='<i>tout</i> parfois s’accorde (<i>toute la classe, toutes les filles</i>). <i>trop / très / bien / vite</i> jamais.',
    worked=[
        ('Exemple 1',
         '''<i>Aujourd’hui, nous allons très vite à l’école.</i><br>
         Invariables : <b>Aujourd’hui, très, vite, à</b>. <i>allons</i> = verbe (conjugué, donc « variable » selon la personne).'''),
        ('Exemple 2 — fautes',
         '''<i>Ils sont venus avecs leurs sacs. Elles jouent bienses.</i><br>
         → <i>Ils sont venus <b>avec</b> leurs sacs. Elles jouent <b>bien</b>.</i>'''),
        ('Exemple 3',
         '''<i>Hier, trop de vent soufflait ici, mais nous avons bien travaillé.</i><br>
         Toute une dictée d’invariables : hier, trop, ici, mais, bien.'''),
    ],
    bulle=('fille', 'Le -s de la 2e personne (<i>tu chantes</i>) n’a rien à voir : c’est une terminaison de verbe, pas un mot invariable qu’on « accorde ».'),
    attention='<i>leurs</i> s’accorde parce que c’est un déterminant possessif (<i>leurs sacs</i>). <i>leur</i> pronom COI reste sans s : <i>Je leur parle</i>.',
    mini='''<i>Ils parlent doucement.</i> — <i>doucement</i> est déjà un adverbe en -ment : on n’ajoute pas de -s (*doucements).''',
    exos_a='Je repère',
    exos=[
        ('⭐', 'Souligne les mots invariables.<br>'
         + q_lignes([
             'Aujourd’hui, nous allons très vite à l’école.',
             'Hier, trop de vent soufflait ici.',
             'Elle écrit bien et lentement.',
             'Sans bruit, les élèves entrent dans la classe.',
             'Mais nous avons déjà fini.',
         ])),
        ('⭐', 'Vrai ou faux ? Si faux, corrige.<br>'
         + q_lignes([
             'On écrit « ils parlent doucements ».',
             'On écrit « avecs leurs sacs ».',
             '« lentement » est invariable.',
             '« grande » est invariable.',
             '« dans » prend un s au pluriel.',
         ])),
        ('⭐⭐', 'Corrige : <i>Ils sont venus avecs leurs sacs. Elles jouent bienses. Nous partons vites verss Atar. Tropes d’élèves parlent forts.</i>'
         + dots(2)),
        ('⭐⭐', 'Classe : lentement / grande / dans / élèves / hier / cahiers / mais / blancs / trop / dunes — invariable ou variable ?'
         + dots(2)),
        ('⭐⭐⭐', 'Écris une phrase sur le fleuve Sénégal qui contient au moins 6 invariables différents. Souligne-les et donne leur classe (adv. / prép. / conj.).'
         + dots(2)),
        ('⭐⭐⭐', 'Dictée express (recopie sans faute) :<br>'
         '<i>Hier, trop de vent soufflait ici, mais nous avons bien travaillé, sans bruit, puis nous sommes rentrés chez nous très vite.</i>'
         + dots(2)),
    ],
    defi='Liste 20 invariables classés en 3 colonnes (adv. / prép. / conj.) et apprends-les pour la prochaine dictée.',
    defi_lines=1,
)),

make_unit(dict(
    num=26, title='L’accord sujet / verbe',
    sub='Sujet éloigné · on · qui · inversion',
    learn_badge='Le verbe « copie » son sujet',
    t1='L’accord du verbe avec le sujet',
    t2='Je trouve d’abord le sujet — corrigé',
    t3='Exercices — accorder',
    t4='Exercices — pièges du concours',
    objectifs=[
        'Accorder le verbe avec son sujet (personne et nombre).',
        'Ne pas se laisser tromper par un nom placé juste avant le verbe.',
        'Gérer on, qui, et le sujet inversé.',
    ],
    rules=[
        'Le verbe s’accorde avec le <span class="hl">sujet</span>, pas avec le mot le plus proche. <i>Le maître des élèves <b>explique</b>.</i> (sujet = le maître).',
        '<b>on</b> → toujours 3<sup>e</sup> personne du singulier. <i>On <b>revoit</b> la leçon.</i> (même si on = plusieurs personnes).',
        '<b>qui</b> → le verbe s’accorde avec l’<b>antécédent</b>. <i>l’élève qui <b>chante</b> / les filles qui <b>chantent</b></i>.',
        'Sujet inversé : <i>Là <b>passent</b> des taxis. Dans la cour <b>jouent</b> les enfants.</i> Le verbe s’accorde avec le nom placé <b>après</b>.',
    ],
    table=(['Phrase', 'Sujet réel', 'Verbe'], [
        ['Les sacs de riz arrivent.', 'les sacs', 'arrivent'],
        ['Le tas de dattes est prêt.', 'le tas', 'est'],
        ['On écoute.', 'on', 'écoute'],
        ['Les filles qui chantent sont prêtes.', 'filles / qui=filles', 'chantent / sont'],
        ['Là passent des chameaux.', 'des chameaux', 'passent'],
    ]),
    methode=('Toujours dans cet ordre', [
        'Je trouve le verbe.',
        'Je pose qui est-ce qui / qu’est-ce qui ? (sujet complet).',
        'Je conjugue pour ce sujet seulement.',
    ]),
    astuce='Encadre : c’est … qui. <i>C’est le tas de dattes qui est prêt.</i> Tu vois tout de suite le singulier.',
    worked=[
        ('Exemple 1',
         '''<i>Les sacs de riz arrivent au port.</i> — qu’est-ce qui arrive ? <b>les sacs</b> → pluriel → <i>arrivent</i>. Pas *arrive à cause de riz.'''),
        ('Exemple 2',
         '''<i>Les élèves de 6AF (réussir).</i> Sujet = les élèves → <b>réussissent</b>. « 6AF » n’est pas le sujet.'''),
        ('Exemple 3',
         '''<i>Les filles qui (chanter) sont prêtes. On (aller) au marché. Là (passer) des chameaux.</i><br>
         → <i>chantent</i> (antécédent filles) · <i>va</i> (on = 3e s.) · <i>passent</i> (chameaux).'''),
    ],
    bulle=('garcon', 'Si tu accords avec le dernier nom lu, tu tombes dans le piège préféré du concours. Recule jusqu’au vrai sujet.'),
    attention='Sujet double : <i>Fatimata et Aïcha préparent l’ataya</i> → pluriel. <i>Fatimata, avec Aïcha, prépare</i> → le noyau est Fatimata (singulier). Au 6AF, on s’entraîne surtout sur le GN long et l’inversion.',
    mini='''<i>Le tas de dattes est prêt. Les sacs de farine pèsent lourd.</i> — tas = singulier ; sacs = pluriel.''',
    exos_a='J’accorde',
    exos=[
        ('⭐', 'Accorde le verbe.<br>'
         + q_lignes([
             'Les dunes (être) dorées.',
             'Le maître (parler) doucement.',
             'On (revoir) la leçon.',
             'Fatimata et Aïcha (préparer) l’ataya.',
             'Le tas de dattes (être) prêt.',
         ])),
        ('⭐', 'Choisis et écris le verbe.'
         + q_lignes([
             'Les sacs de farine (pèse / pèsent).',
             'Le maître des élèves (explique / expliquent).',
             'Les filles qui (chante / chantent) sont prêtes.',
             'On (va / vont) au marché.',
             'Là (passe / passent) des chameaux.',
         ])),
        ('⭐⭐', 'Sujet inversé : mets le verbe au bon nombre.'
         + dots(1) +
         '<i>a) Dans la cour (jouer) … les enfants.</i>' + dots(1) +
         '<i>b) Ici (commencer) … les dunes.</i>' + dots(1) +
         '<i>c) Dans le port (s’agiter) … les pêcheurs.</i>' + dots(1)),
        ('⭐⭐', 'Réécris en accordant : <i>Les élèves de 6AF réussit. Les filles qui chante sont prêtes. On vont au marché. Là passe des taxis jaunes.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Justifie l’accord (sujet + personne + nombre) pour : <i>Le groupe d’élèves de Dar-Naim arrive. Les sacs de riz du quai pèsent lourd. Qui vient ? Des cousins.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Écris 5 phrases pièges : sujet GN long, on, qui + pluriel, inversion, sujet double. Souligne le sujet et le verbe.'
         + dots(2)),
    ],
    defi='Inventé une phrase où trois noms apparaissent avant le verbe, mais un seul est sujet. Fais accorder un camarade.',
    defi_lines=1,
)),

make_unit(dict(
    num=27, title='L’accord du participe passé',
    sub='Être · avoir · pronominal',
    learn_badge='Le -e et le -s du participe',
    t1='L’accord du participe passé',
    t2='Être ou avoir ? — corrigé',
    t3='Exercices — avec être',
    t4='Exercices — avec avoir et pronominal',
    objectifs=[
        'Accorder le participe passé avec être (sujet).',
        'Retenir la règle de base avec avoir : pas d’accord avec le sujet.',
        'Accorder les pronominaux courants du type se lever, se laver (sans COD après).',
    ],
    rules=[
        'Avec <span class="hl">être</span> : le participe s’accorde avec le <b>sujet</b>. <i>Elle est <b>partie</b>. Ils sont <b>arrivés</b>. Elles sont <b>rentrées</b>.</i>',
        'Avec <span class="hl">avoir</span> : en 6AF, on retient d’abord : <b>pas d’accord avec le sujet</b>. <i>Elle a <b>mangé</b>. Ils ont <b>fini</b>. Les filles ont <b>préparé</b> l’ataya.</i>',
        'Verbes pronominaux (se lever, se laver, s’asseoir…) : on accorde souvent comme avec être. <i>Elles se sont <b>levées</b>.</i>',
        'Si un COD est placé <b>après</b> un pronominal comme <i>se laver</i> : <i>Nous nous sommes lavé <b>les mains</b></i> (on n’accorde pas : COD après). Règle à connaître pour le concours, avec un exemple.',
    ],
    table=(['Auxiliaire', 'Règle 6AF', 'Exemple'], [
        ['être', 'accord avec le sujet', 'Mariam est arrivée. Ils sont sortis.'],
        ['avoir', 'pas d’accord avec le sujet', 'Mariam a préparé l’ataya.'],
        ['pronominal (être)', 'souvent accord sujet', 'Elles se sont levées tôt.'],
        ['se laver + COD après', 'pas d’accord', 'Nous nous sommes lavé les mains.'],
    ]),
    methode=('Trois questions', [
        'Quel est l’auxiliaire ? être ou avoir ?',
        'Si être : je copie le genre et le nombre du sujet sur le participe.',
        'Si avoir : je laisse le participe au masculin singulier (mangé, fini, vu) — au 6AF c’est la règle de base.',
    ]),
    astuce='N’ajoute jamais -e / -s « parce que le sujet est féminin » si tu vois <i>a / as / ont / avons</i> (avoir).',
    worked=[
        ('Exemple 1 — être',
         '''<i>Elle est (allé). Ils sont (sorti).</i> → <b>allée</b>, <b>sortis</b>.'''),
        ('Exemple 2 — avoir',
         '''<i>Elle a (fini). Nous avons (mangé).</i> → <b>fini</b>, <b>mangé</b> (invariables ici).'''),
        ('Exemple 3 — mélange',
         '''<i>Les pêcheuses sont rentrées tard. Elles ont vendu le poisson. Elles se sont lavé les mains.</i><br>
         être → rentrées ; avoir → vendu ; se laver + les mains après → lavé.'''),
    ],
    bulle=('fille', 'Deux colonnes mentales : colonne ÊTRE (j’accorde) / colonne AVOIR (je n’accorde pas avec le sujet).'),
    attention='<i>Aïcha est parti</i> est faux (être + sujet féminin → <b>partie</b>). <i>Aïcha a partie</i> est faux (avoir + partir n’existe pas : partir va avec être).',
    mini='''<i>Mariam est arrivée. Elle a préparé l’ataya. Ses tantes sont restées.</i> — arrivée / restées (être) ; préparé (avoir).''',
    exos_a='Avec être',
    exos=[
        ('⭐', 'Accorde si besoin.<br>'
         + q_lignes([
             'Elle est (allé).',
             'Ils sont (sorti).',
             'Elle a (fini).',
             'Nous avons (mangé).',
             'Aïcha est (revenu).',
         ])),
        ('⭐', 'Choisis la bonne forme.<br>'
         + q_lignes([
             'Les filles sont (entré / entrées).',
             'Les filles ont (entré / entré) le banc. (entrer qqch. = avoir)',
             'Mariam est (arrivé / arrivée).',
             'Ils ont (vu / vus) la mer. (COD après)',
             'Elles se sont (levé / levées).',
         ])),
        ('⭐⭐', 'Réécris : <i>Aïcha est parti au marché. Ses sœurs ont rangé. Elles sont revenu tard. Nous avons fini.</i>'
         + dots(2)),
        ('⭐⭐', 'Accorde : <i>Elles se sont (levé) tôt. Nous nous sommes (lavé) les mains. Ils se sont (assis) par terre. Elles se sont (habillé).</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Dictée : recopie en soignant les participes.<br>'
         '<i>Mariam est arrivée. Elle a préparé l’ataya. Ses tantes sont restées. Elles se sont assises. Nous avons bu trois verres.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Pour chaque verbe, écris 2 phrases : une avec être (accord) et une avec avoir (pas d’accord avec le sujet) si les deux existent (monter, descendre, sortir, rentrer). Sinon explique.'
         + dots(2)),
    ],
    defi='Explique à un camarade, avec tes exemples, pourquoi <i>Elle est partie</i> prend un e et <i>Elle a mangé</i> n’en prend pas.',
    defi_lines=1,
)),

]
