# -*- coding: utf-8 -*-
"""Conjugaison 6AF — 6 leçons riches (cours + tableaux + exemples corrigés)."""
from base_fr import make_unit, OVS, dots, q_lignes


UNITS_CONJ = [

make_unit(dict(
    num=16, title='Les variations du verbe',
    sub='3 groupes · présent des verbes courants',
    learn_badge='Le verbe change selon la personne et le temps',
    t1='Les variations du verbe',
    t2='Je conjugue au présent — corrigé',
    t3='Exercices — groupes et présent',
    t4='Exercices — verbes fréquents',
    objectifs=[
        'Reconnaître les 3 groupes du verbe et les verbes irréguliers utiles au 6AF.',
        'Conjuguer au présent les verbes réguliers et être, avoir, aller, faire, venir, prendre.',
        'Accorder la terminaison avec la personne (je, tu, il, nous, vous, ils).',
    ],
    rules=[
        'Le verbe <span class="hl">varie</span> selon la <b>personne</b> (je, tu, il…), le <b>nombre</b> (singulier / pluriel) et le <b>temps</b> (présent, imparfait…).',
        '<b>1<sup>er</sup> groupe</b> : infinitif en <span class="hl">-er</span> (sauf <i>aller</i>) : <i>chanter, jouer, arriver, manger</i>. Présent : <i>je joue, tu joues, il joue, nous jouons, vous jouez, ils jouent</i>.',
        '<b>2<sup>e</sup> groupe</b> : infinitif en <span class="hl">-ir</span> avec <b>-issons</b> au présent : <i>finir, réussir, grandir</i>. <i>nous finissons</i>.',
        '<b>3<sup>e</sup> groupe</b> : tous les autres : <i>être, avoir, aller, faire, prendre, venir, voir, dire, partir…</i> À mémoriser.',
    ],
    table=(['Personne', 'jouer (1er)', 'finir (2e)', 'prendre (3e)'], [
        ['je / tu / il', 'joue / joues / joue', 'finis / finis / finit', 'prends / prends / prend'],
        ['nous / vous / ils', 'jouons / jouez / jouent', 'finissons / finissez / finissent', 'prenons / prenez / prennent'],
    ]),
    methode=('Pour classer un verbe', [
        'Je mets l’infinitif : <i>ils jouent → jouer</i>.',
        'Si -er (et pas aller) → 1er groupe. Si nous …-issons → 2e. Sinon → 3e.',
        'Je choisis la bonne terminaison pour la personne demandée.',
    ]),
    astuce='Mémorise en priorité : être, avoir, aller, faire. Ils reviennent à chaque dictée et au concours.',
    worked=[
        ('Exemple 1 — trouver le groupe',
         '''<i>Les enfants jouent dans la cour de Tevragh Zeina.</i>
         <ol>
           <li>Infinitif : <b>jouer</b> → -er, pas aller → <b>1<sup>er</sup> groupe</b>.</li>
           <li>Personne : ils → terminaison <b>-ent</b> : <i>jouent</i>.</li>
         </ol>'''),
        ('Exemple 2 — 2e groupe',
         '''<i>Nous (réussir) le concours.</i> → 2e groupe, personne nous → <b>réussissons</b> (on entend -issons).'''),
        ('Exemple 3 — irréguliers',
         '''<i>Je (aller) au marché. Tu (être) prêt. Elle (avoir) soif. Nous (faire) nos exercices.</i><br>
         → <i>Je <b>vais</b>. Tu <b>es</b> prêt. Elle <b>a</b> soif. Nous <b>faisons</b> nos exercices.</i>'''),
    ],
    bulle=('garcon', 'Au présent, 1er groupe : je/il = -e, tu = -es, nous = -ons, vous = -ez, ils = -ent. Les -e -es -ent ne s’entendent pas : il faut les voir.'),
    attention='<i>manger</i> : nous mangeons (on garde le e pour le son [ʒ]). <i>aller</i> n’est pas du 1er groupe malgré -er.',
    mini='''<i>nous (chanter)</i> → 1er groupe, personne nous → <b>chantons</b>.''',
    exos_a='Groupes et terminaisons',
    exos=[
        ('⭐', 'Indique le groupe (1, 2 ou 3).<br>'
         + q_lignes(['manger', 'finir', 'prendre', 'arriver', 'être', 'réussir', 'aller', 'venir'])),
        ('⭐', 'Conjugue au présent.<br>'
         + q_lignes([
             'nous (chanter)',
             'ils (finir)',
             'je (jouer)',
             'vous (réussir)',
             'tu (arriver)',
         ])),
        ('⭐⭐', 'Conjugue : je (aller), tu (être), elle (avoir), nous (faire), vous (aller), ils (être).'
         + dots(2)),
        ('⭐⭐', 'Réécris au pluriel (attention aux verbes).<br>'
         '<i>Je prends le taxi. Tu vas à l’école. Il finit son exercice. Elle est prête.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Conjugue <b>venir</b> et <b>prendre</b> aux 6 personnes du présent.'
         + dots(2)),
        ('⭐⭐⭐', 'Écris 6 phrases au présent sur Nouakchott : 2 du 1er groupe, 2 du 2e, 2 du 3e (dont être ou aller). Souligne les verbes.'
         + dots(2)),
    ],
    defi='Fais ta fiche « 10 verbes du 3e groupe » : infinitif + je + nous + ils au présent.',
    defi_lines=1,
)),

make_unit(dict(
    num=17, title='Le passé simple',
    sub='Récit · verbes fréquents',
    learn_badge='Le temps des histoires écrites',
    t1='Le passé simple de l’indicatif',
    t2='Je raconte au passé simple — corrigé',
    t3='Exercices — former le passé simple',
    t4='Exercices — un récit',
    objectifs=[
        'Former le passé simple des verbes du 1er groupe et des verbes fréquents.',
        'Comprendre qu’il raconte un fait achevé, souvent dans un récit écrit.',
        'L’employer dans un court récit (voyage, journée, tempête).',
    ],
    rules=[
        'Le <span class="hl">passé simple</span> raconte un fait <b>achevé</b>, qui fait avancer l’histoire. On le trouve surtout à l’écrit (contes, récits).',
        '1<sup>er</sup> groupe : <b>-ai, -as, -a, -âmes, -âtes, -èrent</b>. <i>je chantai, tu chantas, il chanta, nous chantâmes, vous chantâtes, ils chantèrent</i>.',
        '<b>être</b> : je fus, tu fus, il fut, nous fûmes, vous fûtes, ils furent. &nbsp; <b>avoir</b> : j’eus, tu eus, il eut, nous eûmes, vous eûtes, ils eurent.',
        'Autres fréquents : <i>aller → j’allai, ils allèrent</i> · <i>faire → je fis, il fit, nous fîmes, ils firent</i> · <i>voir → je vis, il vit, ils virent</i> · <i>prendre → je pris, il prit, ils prirent</i>.',
    ],
    table=(['Personne', 'jouer', 'être', 'faire'], [
        ['je / tu / il', 'jouai / jouas / joua', 'fus / fus / fut', 'fis / fis / fit'],
        ['nous / vous / ils', 'jouâmes / jouâtes / jouèrent', 'fûmes / fûtes / furent', 'fîmes / fîtes / firent'],
    ]),
    methode=('Pour former le 1er groupe', [
        'Je prends le radical de l’infinitif : <i>arriver → arriv-</i>.',
        'J’ajoute -ai -as -a -âmes -âtes -èrent selon la personne.',
        'À la 3e personne du pluriel, j’entends souvent « èr » : <i>ils arrivèrent</i>.',
    ]),
    astuce='Au 6AF, on te demande surtout de reconnaître le passé simple et de conjuguer les verbes courants, pas tous les irréguliers du dictionnaire.',
    worked=[
        ('Exemple 1',
         '''<i>Le vent se leva, le sable envahit la piste d’Atar, puis le calme revint.</i>
         <ol>
           <li>Trois actions achevées qui s’enchaînent → passé simple.</li>
           <li><i>se leva, envahit, revint</i> : 3e personne du singulier.</li>
         </ol>'''),
        ('Exemple 2 — 1er groupe',
         '''<i>il (jouer) · ils (arriver)</i> → <b>il joua</b>, <b>ils arrivèrent</b>.'''),
        ('Exemple 3 — être / avoir / faire',
         '''<i>Je (être) malade. Nous (avoir) peur. Ils (faire) un feu.</i><br>
         → <i>Je <b>fus</b> malade. Nous <b>eûmes</b> peur. Ils <b>firent</b> un feu.</i>'''),
    ],
    bulle=('fille', 'Le passé simple n’est pas le passé composé : on ne met pas d’auxiliaire. <i>il chanta</i> ≠ <i>il a chanté</i> (même idée, forme différente).'),
    attention='Accent circonflexe : nous chant<b>â</b>mes, vous chant<b>â</b>tes, nous f<b>û</b>mes, il f<b>î</b>t. Ne l’oublie pas à l’écrit.',
    mini='''<i>Le maître entra. Les élèves se levèrent.</i> — deux faits successifs au passé simple (1er groupe + pronominal).''',
    exos_a='Je conjugue',
    exos=[
        ('⭐', 'Conjugue au passé simple, 3e personne.<br>'
         + q_lignes(['il (jouer)', 'ils (arriver)', 'elle (chanter)', 'elles (regarder)', 'on (entrer)'])),
        ('⭐', 'Conjugue être et avoir.<br>'
         + q_lignes(['je (être)', 'il (être)', 'nous (être)', 'tu (avoir)', 'ils (avoir)'])),
        ('⭐⭐', 'Mets au passé simple.<br>'
         '<i>Le maître entre. Les élèves se lèvent. Le silence s’installe. Une fille tousse.</i>'
         + dots(2)),
        ('⭐⭐', 'Conjugue <b>faire</b> et <b>aller</b> : je, il, nous, ils.'
         + dots(2)),
        ('⭐⭐⭐', 'Réécris au passé simple : <i>Sidi va au port et voit les bateaux. Il prend un poisson et rentre chez lui.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Écris un récit de 8 verbes au passé simple : un voyage vers Nouadhibou (départ, route, mer, retour). Varie les personnes.'
         + dots(2)),
    ],
    defi='Recopie 4 verbes d’un conte (passé simple) et donne leur infinitif + leur personne.',
    defi_lines=1,
)),

make_unit(dict(
    num=18, title='Imparfait et passé simple',
    sub='Décor / habitude · fait unique',
    learn_badge='Deux temps pour raconter',
    t1='Imparfait et passé simple ensemble',
    t2='Je choisis le temps — corrigé',
    t3='Exercices — habitude ou fait',
    t4='Exercices — un récit mêlé',
    objectifs=[
        'Former l’imparfait (radical nous du présent + -ais -ais -ait -ions -iez -aient).',
        'Choisir imparfait (décor, habitude, durée) ou passé simple (fait ponctuel).',
        'Écrire un récit qui mélange les deux temps.',
    ],
    rules=[
        'L’<span class="hl">imparfait</span> décrit, montre une habitude ou une action qui dure. Terminaisons : <b>-ais, -ais, -ait, -ions, -iez, -aient</b>. Radical = <i>nous</i> du présent sans -ons : <i>nous jouons → je jouais</i>.',
        'Le <span class="hl">passé simple</span> fait <b>avancer</b> l’histoire : action unique, soudaine, achevée.',
        'Ensemble : <i>Le soleil <b>brillait</b> (décor). Soudain un chameau <b>apparut</b> (fait).</i>',
        'Indices imparfait : <i>chaque matin, pendant que, d’habitude, autrefois</i>. Indices passé simple : <i>soudain, un jour, tout à coup, alors</i>.',
    ],
    table=(['Situation', 'Temps', 'Exemple'], [
        ['décor, météo, paysage', 'imparfait', 'Le vent soufflait sur Atar.'],
        ['habitude répétée', 'imparfait', 'Chaque matin, les pêcheurs partaient.'],
        ['fait unique qui arrive', 'passé simple', 'Un jour, la mer se déchaîna.'],
        ['actions qui s’enchaînent', 'passé simple', 'Il entra, salua, s’assit.'],
    ]),
    methode=('Quel temps ?', [
        'Est-ce le décor ou une habitude ? → imparfait.',
        'Est-ce un événement unique qui fait bouger l’histoire ? → passé simple.',
        'Je conjugue avec les bonnes terminaisons (pas d’auxiliaire).',
    ]),
    astuce='Si tu peux dire « pendant ce temps-là / d’habitude » → imparfait. Si tu peux dire « et là, tout à coup » → passé simple.',
    worked=[
        ('Exemple 1',
         '''<i>Quand j’étais petit, je (jouer) dans la rue.</i><br>
         Habitude + « quand j’étais » déjà à l’imparfait → <b>je jouais</b>.'''),
        ('Exemple 2',
         '''<i>Soudain, le maître (entrer).</i> → indice « soudain » → <b>entra</b> (passé simple).'''),
        ('Exemple 3 — récit complet',
         '''<i>Il <b>faisait</b> beau. Les filles <b>chantaient</b>. Tout à coup un taxi <b>s’arrêta</b>.</i><br>
         Deux imparfaits (décor + action en cours) puis un passé simple (événement).'''),
    ],
    bulle=('garcon', 'L’imparfait « filme » le décor. Le passé simple « clique » sur la photo de l’événement.'),
    attention='Nous : imparfait <i>nous jou<b>i</b>ons</i> (on garde le i). Ne l’oublie pas : *nous jouons à l’imparfait est faux.',
    mini='''<i>Chaque matin, les pêcheurs partaient. Un jour, la mer se déchaîna.</i> — habitude = imparfait ; un jour = passé simple.''',
    exos_a='Je choisis',
    exos=[
        ('⭐', 'Imparfait ou passé simple ? Écris le verbe conjugué.<br>'
         + q_lignes([
             'Quand j’étais petit, je (jouer) dans la rue.',
             'Soudain, le maître (entrer).',
             'Autrefois, on (boire) l’ataya le soir.',
             'Un jour, Sidi (voir) un dauphin.',
             'Pendant que le vent (souffler), nous (rester) chez nous.',
         ])),
        ('⭐', 'Mets à l’imparfait (6 personnes de <i>finir</i> ou au moins je / nous / ils de <i>aller</i> et <i>faire</i>).'
         + dots(2)),
        ('⭐⭐', 'Conjugue le temps qui convient.<br>'
         '<i>Il (faire) beau. Les filles (chanter). Tout à coup un taxi (s’arrêter). Le chauffeur (descendre) et (appeler) Sidi.</i>'
         + dots(2)),
        ('⭐⭐', 'Réécris en mélangeant les deux temps.<br>'
         '<i>La mer est calme. Un bateau arrive. Les pêcheurs crient. La foule s’approche.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Complète : Pendant que le vent (souffler) …, une dune (s’écrouler) … . Les enfants (jouer) … encore quand le maître (apparaître) … .'
         + dots(2)),
        ('⭐⭐⭐', 'Récit de 8 à 10 lignes (imparfait + passé simple) : une journée à Rosso. Souligne en deux couleurs (ou marque I / PS).'
         + dots(2)),
    ],
    defi='Prends 5 indices (chaque matin, soudain, autrefois, un jour, pendant que) et écris 5 mini-phrases au bon temps.',
    defi_lines=1,
)),

make_unit(dict(
    num=19, title='Imparfait et passé composé',
    sub='Habitude · fait achevé (oral et concours)',
    learn_badge='Le passé qu’on utilise tous les jours',
    t1='Imparfait et passé composé',
    t2='Avoir ou être ? — corrigé',
    t3='Exercices — former le PC',
    t4='Exercices — choisir le temps',
    objectifs=[
        'Former le passé composé : auxiliaire au présent + participe passé.',
        'Choisir l’auxiliaire avoir ou être, et accorder avec être.',
        'Opposer imparfait (durée, habitude) et passé composé (fait terminé, résultat).',
    ],
    rules=[
        'Le <span class="hl">passé composé</span> = auxiliaire au <b>présent</b> + <b>participe passé</b>. <i>j’ai mangé, elle est partie, nous avons fini</i>. C’est le passé de la conversation et souvent du concours.',
        'Auxiliaire <b>avoir</b> : la plupart des verbes. Pas d’accord avec le sujet. <i>Elle a mangé. Ils ont fini.</i>',
        'Auxiliaire <b>être</b> : verbes de mouvement (aller, venir, partir, arriver, entrer, sortir, monter, descendre, naître, mourir, rester, tomber…) + verbes pronominaux. Accord avec le sujet : <i>elle est parti<b>e</b>, ils sont allé<b>s</b></i>.',
        '<span class="hl">Imparfait</span> = habitude / description. <span class="hl">PC</span> = action terminée, souvent datée (hier, ce matin, en 2024).',
    ],
    table=(['Infinitif', 'Participe', 'PC (il / elle / ils)'], [
        ['manger / finir', 'mangé / fini', 'il a mangé / elle a fini'],
        ['aller / partir', 'allé / parti', 'elle est allée / ils sont partis'],
        ['faire / prendre', 'fait / pris', 'nous avons fait / tu as pris'],
        ['se laver', 'lavé', 'elles se sont lavées'],
    ]),
    methode=('PC ou imparfait ?', [
        'Y a-t-il une date ponctuelle, un résultat fini ? → PC.',
        'Est-ce « tous les jours / quand j’étais petit / pendant que » ? → imparfait.',
        'Je choisis avoir ou être, puis j’accorde le participe si l’auxiliaire est être.',
    ]),
    astuce='Dr et Mrs Vandertramp (ou la maison d’être) : aller, venir, arriver, partir, entrer, sortir, monter, descendre, tomber, rester, naître, mourir, retourner…',
    worked=[
        ('Exemple 1 — formation',
         '''<i>tu (manger) · elle (partir)</i> → <b>tu as mangé</b> (avoir, invariable ici) · <b>elle est partie</b> (être + -e).'''),
        ('Exemple 2 — choix du temps',
         '''<i>Quand j’étais petit, je (boire) de l’ataya tous les soirs.</i> → habitude → <b>je buvais</b> (imparfait).<br>
         <i>Hier soir, j’(boire) de l’ataya.</i> → fait fini → <b>j’ai bu</b> (PC).'''),
        ('Exemple 3 — accord',
         '''<i>Elles sont (allé) au marché. Nous avons (fini).</i><br>
         → <i>Elles sont <b>allées</b>. Nous avons <b>fini</b>.</i> (avoir : pas d’accord avec nous).'''),
    ],
    bulle=('fille', 'Au PC, l’accord se voit à l’écrit : <i>partie / partis / parties</i>. À l’oral, on n’entend pas toujours le -e : d’où les pièges de dictée.'),
    attention='<i>Elle a parti</i> est faux. Partir se conjugue avec être : <i>elle est partie</i>.',
    mini='''<i>Hier, nous avons révisé le français. Avant, nous révisions chaque soir.</i> — fait fini = PC ; habitude = imparfait.''',
    exos_a='Je forme le PC',
    exos=[
        ('⭐', 'Conjugue au passé composé.<br>'
         + q_lignes(['tu (manger)', 'elle (partir)', 'nous (finir)', 'ils (aller)', 'je (faire)'])),
        ('⭐', 'PC ou imparfait ? Conjugue.<br>'
         + q_lignes([
             'Quand j’étais petit, je (boire) de l’ataya tous les soirs.',
             'Hier, nous (réviser) le français.',
             'Chaque matin, le maître (entrer) à 8 h.',
             'Ce matin, le maître (entrer) en retard.',
             'Autrefois, les caravanes (traverser) le désert.',
         ])),
        ('⭐⭐', 'Accorde le participe si besoin.'
         + dots(1) +
         '<i>a) Elles sont (allé) au marché.</i>' + dots(1) +
         '<i>b) Nous avons (fini) l’exercice.</i>' + dots(1) +
         '<i>c) Aïcha est (revenu) tard.</i>' + dots(1) +
         '<i>d) Ils sont (sorti) dans la cour.</i>' + dots(1)),
        ('⭐⭐', 'Réécris au PC : <i>Je vais à Nouadhibou. Je vois la mer. Nous rentrons le soir. Fatimata prépare l’ataya.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Choisis et conjugue : Hier il (pleuvoir) … pendant que nous (jouer) … . Soudain, un ami (arriver) … et nous (partir) … .'
         + dots(2)),
        ('⭐⭐⭐', 'Écris 6 phrases sur l’école : 3 imparfaits (habitude) et 3 PC (hier / ce matin). Souligne les auxiliaires.'
         + dots(2)),
    ],
    defi='Liste 8 verbes avec être au PC, au féminin singulier et au masculin pluriel (elle est… / ils sont…).',
    defi_lines=1,
)),

make_unit(dict(
    num=20, title='Voix active, passive et pronominale',
    sub='Le sujet fait, subit, ou agit sur soi',
    learn_badge='Trois façons de dire l’action',
    t1='Les trois voix du verbe',
    t2='Je transforme active ↔ passive — corrigé',
    t3='Exercices — reconnaître la voix',
    t4='Exercices — transformer',
    objectifs=[
        'Distinguer voix active, passive et pronominale.',
        'Transformer active ↔ passive au présent et au passé composé.',
        'Repérer le pronom réfléchi (se, s’, me, te, nous, vous).',
    ],
    rules=[
        '<span class="hl">Voix active</span> : le sujet <b>fait</b> l’action. <i>Le maître <b>explique</b> la leçon.</i>',
        '<span class="hl">Voix passive</span> : le sujet <b>subit</b> l’action. Forme : <b>être + participe passé</b> (+ <i>par …</i> éventuellement). <i>La leçon <b>est expliquée</b> par le maître.</i>',
        'Au passif, le <b>COD</b> de l’active devient <b>sujet</b>. Le sujet de l’active devient complément d’agent (<i>par …</i>).',
        '<span class="hl">Voix pronominale</span> : pronom réfléchi de la même personne que le sujet. <i>Les élèves <b>se lèvent</b>. Je <b>me</b> lave. Nous <b>nous</b> dépêchons.</i>',
    ],
    table=(['Voix', 'Le sujet…', 'Exemple (quai de Nouadhibou)'], [
        ['active', 'fait l’action', 'Les pêcheurs salent le poisson.'],
        ['passive', 'subit l’action', 'Le poisson est salé par les pêcheurs.'],
        ['pronominale', 'agit sur soi / l’un l’autre', 'Les pêcheurs se saluent.'],
    ]),
    methode=('Pour passer à l’actif au passif', [
        'Je trouve le COD de l’active : c’est lui le nouveau sujet.',
        'Je mets le verbe <i>être</i> au même temps, puis le participe (accordé avec le nouveau sujet).',
        'J’ajoute <i>par + ancien sujet</i> si on veut garder l’agent.',
    ]),
    astuce='On ne met au passif que les verbes qui ont un COD. <i>Les dunes brillent</i> n’a pas de passif utile.',
    worked=[
        ('Exemple 1 — présent',
         '''<i>Le maître corrige les cahiers.</i>
         <ol>
           <li>COD = les cahiers → nouveau sujet.</li>
           <li>être au présent + corrigés (accord m. pl.).</li>
           <li><i>Les cahiers <b>sont corrigés</b> par le maître.</i></li>
         </ol>'''),
        ('Exemple 2 — passé composé',
         '''<i>Les élèves ont lu le texte.</i> → être au PC + lu accordé :<br>
         <i>Le texte <b>a été lu</b> par les élèves.</i> (être au PC = <i>a été</i> / <i>ont été</i>).'''),
        ('Exemple 3 — pronominale',
         '''<i>Nous nous lavons les mains.</i> Pronom <i>nous</i> = même personne que le sujet → <b>pronominale</b>. Ce n’est pas un passif.'''),
    ],
    bulle=('garcon', 'Au passif, pense « être + participe ». Si tu vois <i>se</i> devant le verbe, pense « pronominale » avant de dire passif.'),
    attention='<i>Le riz est cuit par maman</i> = passif. <i>Le riz se cuit à la vapeur</i> = pronominale (sens passif parfois, mais forme pronominale). Au 6AF, on nomme la forme.',
    mini='''<i>Les dattes sont vendues par Fatimata.</i> — être + participe + par → <b>voix passive</b>. Actif : <i>Fatimata vend les dattes.</i>''',
    exos_a='Je reconnais',
    exos=[
        ('⭐', 'Active, passive ou pronominale ?<br>'
         + q_lignes([
             'Le riz est cuit par maman.',
             'Nous nous lavons les mains.',
             'Le maître explique la leçon.',
             'Les élèves se lèvent.',
             'Le poisson est salé par les pêcheurs.',
         ])),
        ('⭐', 'Mets au passif (présent).<br>'
         + q_lignes([
             'Le maître corrige les cahiers.',
             'Fatimata vend les dattes.',
             'Les élèves lisent le texte.',
         ]) + dots(2)),
        ('⭐⭐', 'Mets à l’actif.'
         + dots(1) +
         '<i>a) Les dattes sont vendues par Fatimata.</i>' + dots(1) +
         '<i>b) La leçon est expliquée par le maître.</i>' + dots(1) +
         '<i>c) Le filet est réparé par Sidi.</i>' + dots(1)),
        ('⭐⭐', 'Mets au passif au <b>passé composé</b>.'
         + dots(1) +
         '<i>a) Les élèves ont lu le texte.</i>' + dots(1) +
         '<i>b) Le maître a fermé la porte.</i>' + dots(1) +
         '<i>c) Les pêcheurs ont salé le poisson.</i>' + dots(1)),
        ('⭐⭐⭐', 'Accorde le participe au passif : <i>La porte est (fermé). Les rues sont (balayé). La leçon a été (compris) par les filles.</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Écris 6 phrases sur le marché : 2 actives, 2 passives, 2 pronominales. Transforme ensuite une active en passive.'
         + dots(2)),
    ],
    defi='Même information, trois voix : active, passive, pronominale (si possible). Thème : se préparer le matin.',
    defi_lines=1,
)),

make_unit(dict(
    num=21, title='Le présent du conditionnel',
    sub='Souhait · politesse · hypothèse (si + imparfait)',
    learn_badge='Ce qu’on ferait… si',
    t1='Le conditionnel présent',
    t2='Je forme et j’emploie — corrigé',
    t3='Exercices — conjuguer',
    t4='Exercices — souhait et hypothèse',
    objectifs=[
        'Former le conditionnel présent : radical du futur + terminaisons de l’imparfait.',
        'L’employer pour un souhait, une politesse ou une hypothèse (si + imparfait).',
        'Ne pas le confondre avec le futur (je mangerai / je mangerais).',
    ],
    rules=[
        'Le <span class="hl">conditionnel présent</span> se forme avec le <b>radical du futur</b> + les terminaisons de l’<b>imparfait</b> : <b>-ais, -ais, -ait, -ions, -iez, -aient</b>.',
        'Exemples : <i>je mangerais, tu viendrais, il ferait, nous irions, vous auriez, ils seraient</i>.',
        'Emplois : <b>politesse</b> <i>Je voudrais un verre d’eau.</i> · <b>souhait</b> <i>J’aimerais réussir.</i> · <b>hypothèse</b> <i>Si j’avais le temps, je réviserais.</i>',
        'Système : <span class="hl">si + imparfait</span>, l’autre verbe au <span class="hl">conditionnel</span>. <i>Si le vent tombait, nous irions au stade.</i>',
    ],
    table=(['Infinitif', 'Futur (je)', 'Conditionnel (je / nous)'], [
        ['manger', 'je mangerai', 'je mangerais / nous mangerions'],
        ['être / avoir', 'je serai / j’aurai', 'je serais / j’aurais'],
        ['aller / faire', 'j’irai / je ferai', 'j’irais / je ferais'],
        ['venir / pouvoir', 'je viendrai / je pourrai', 'je viendrais / je pourrais'],
    ]),
    methode=('Pour le former', [
        'Je dis le futur à la 1re personne : <i>je viendrai</i>.',
        'J’enlève -ai et je mets -ais : <i>je viendrais</i>.',
        'Pour nous : -ions (<i>nous viendrions</i>).',
    ]),
    astuce='Futur = certitude / promesse : <i>Demain je partirai.</i> Conditionnel = hypothèse / rêve : <i>Si je pouvais, je partirais.</i> La différence s’entend : -ai / -ais.',
    worked=[
        ('Exemple 1 — formation',
         '''<i>je (aimer) · nous (finir)</i> → futur <i>j’aimerai, nous finirons</i> → conditionnel <b>j’aimerais, nous finirions</b>.'''),
        ('Exemple 2 — si + imparfait',
         '''<i>Si j’avais une ouguiya de plus, je (acheter) des dattes.</i><br>
         Si + imparfait (<i>avais</i>) → <b>j’achèterais</b> des dattes.'''),
        ('Exemple 3 — politesse',
         '''<i>Je veux un thé.</i> (un peu direct) → <i>Je <b>voudrais</b> un thé.</i> (plus poli, conditionnel de <i>vouloir</i>).'''),
    ],
    bulle=('fille', 'Retiens la paire : <i>si j’avais… je ferais…</i> Jamais *si j’aurais au 6AF dans cette structure.'),
    attention='On n’écrit pas *si j’aurais. Après <i>si</i> de l’hypothèse, c’est l’<b>imparfait</b> : <i>si j’avais, si tu venais</i>.',
    mini='''<i>Si le vent tombait, nous irions au stade de Nouakchott.</i> — si + imparfait <i>tombait</i> ; conditionnel <i>irions</i>.''',
    exos_a='Je conjugue',
    exos=[
        ('⭐', 'Conjugue au conditionnel présent.<br>'
         + q_lignes(['je (aimer)', 'nous (finir)', 'tu (être)', 'il (avoir)', 'ils (aller)'])),
        ('⭐', 'Conjugue : je (faire), tu (venir), elle (pouvoir), vous (voir), on (réussir).'
         + dots(2)),
        ('⭐⭐', 'Complète au conditionnel.'
         + dots(1) +
         '<i>a) Si j’avais une ouguiya de plus, je (acheter) … des dattes.</i>' + dots(1) +
         '<i>b) Si tu venais à Kaédi, tu (voir) … le fleuve.</i>' + dots(1) +
         '<i>c) Si nous révisions davantage, nous (réussir) … .</i>' + dots(1)),
        ('⭐⭐', 'Transforme en politesse (conditionnel de vouloir / aimer / pouvoir).'
         + dots(1) +
         '<i>a) Je veux un thé.</i>' + dots(1) +
         '<i>b) Donne-moi ce cahier. → Je voudrais que tu… / Pourrais-tu…</i>' + dots(2)),
        ('⭐⭐⭐', 'Futur ou conditionnel ? Conjugue et justifie.<br>'
         '<i>a) Demain je (partir) … à Kaédi.</i><br>'
         '<i>b) Si je pouvais, je (partir) … à Kaédi.</i><br>'
         '<i>c) Nous (être) … contents si le maître (venir) … .</i>'
         + dots(2)),
        ('⭐⭐⭐', 'Écris 6 souhaits au conditionnel pour réussir le concours 6AF, dont 3 phrases avec <i>si + imparfait</i>.'
         + dots(2)),
    ],
    defi='Corrige : *Si j’aurais le temps, je réviserai. — Écris la phrase juste et explique la règle.',
    defi_lines=1,
)),

]
