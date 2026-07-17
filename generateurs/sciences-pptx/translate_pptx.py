import zipfile
import re

src = "كراسة العلوم الطبيعية_RTL.pptx"
dst = "كراسة العلوم الطبيعية_AR.pptx"

# (French/English text, Arabic translation)
# Order: longest strings first to avoid partial matches
REPLACEMENTS = [
    # ── Slide 2 ──
    ("Voir la vidéo", "شاهد الفيديو"),
    ("j’apprend", "أتعلم"),

    # ── Slide 3 ──
    ("LIPIDES PROTÉINES", "الدهون والبروتينات"),
    ("QCM Coche la bonne réponse :", "اختر الإجابة الصحيحة:"),
    ("Classe les aliments  Complète ce tableau :", "صنّف الأغذية وأكمل هذا الجدول:"),
    ("Riz  -Œufs -Huile végétale  -Haricots secs :", "أرز - بيض - زيت نباتي - فاصوليا جافة:"),
    (" 1. Quel aliment est complet ?", " ١. أي غذاء متكامل؟"),
    ("Les glucides servent à :", "السكريات تستخدم لـ:"),
    ("Donner de l’énergie", "إعطاء الطاقة"),
    (" a) Pour bien grandir et être en bonne santé", " أ) للنمو الجيد والحفاظ على الصحة"),
    (" b) Pour manger tout ce qu’on veut sans limite", " ب) لأكل كل ما نريد بدون حدود"),
    (" c) Parce que les aliments n’ont aucun effet sur la santé", " ج) لأن الأغذية لا تؤثر على الصحة"),
    ("Pourquoi est-il important d’avoir une alimentation équilibrée ?", "لماذا من المهم الحصول على تغذية متوازنة؟"),
    ("Parmi ces aliments, lequel appartient à la catégorie des produits laitiers ?", "من بين هذه الأغذية، أيها ينتمي إلى مجموعة منتجات الألبان؟"),
    ("Quel est l’aliment principal dans la catégorie des féculents ?", "ما هو الغذاء الرئيسي في مجموعة النشويات؟"),
    (" a) Le poisson", " أ) السمك"),
    (" b) Le yaourt", " ب) الزبادي"),
    (" c) Le pain", " ج) الخبز"),
    ("ALIMENTS", "الأغذية"),
    ("GLUCIDES", "السكريات"),
    ("protein sources", "مصادر البروتين"),
    ("carbohydrates", "الكربوهيدرات"),
    (" &amp; fruits", "والفواكه"),
    ("vegetables", "الخضروات"),
    ("liquids", "السوائل"),
    ("exercices", "تمارين"),
    ("Grandir", "النمو"),
    ("Fromage", "جبن"),
    ("Dormir", "النوم"),

    # ── Slide 4 ──
    ("Quelle boisson est la plus recommandée pour s’hydrater ?", "ما هو المشروب الأكثر موصى به للترطيب؟"),
    ("Pourquoi faut-il manger des fruits et légumes chaque jour ?", "لماذا يجب تناول الفواكه والخضروات كل يوم؟"),
    ("Les aliments qui apportent de l’énergie à notre corps sont les _____ ____________________.", "الأغذية التي تمنح الطاقة لجسمنا هي _______________."),
    ("Pour avoir des os solides, il est important de manger des ______________.", "للحصول على عظام قوية، من المهم تناول ______________."),
    ("L’eau est essentielle pour notre corps car elle permet ______________.", "الماء ضروري لجسمنا لأنه يسمح بـ ______________."),
    ("Il faut limiter les aliments trop ______________ et trop  ___________", "يجب تقليل الأغذية الكثيرة ______________ والكثيرة ______________"),
    (" Complète les phrases", " أكمل الجمل"),
    ("Léa mange chaque jour du pain, des pâtes et des sucreries. Elle boit du soda et mange rarement des fruits et légumes.", "ليا تأكل كل يوم خبزاً ومعكرونة وحلويات. تشرب المشروبات الغازية ونادراً ما تأكل الفواكه والخضروات."),
    ("Trace une ligne pour relier chaque aliment à son groupe alimentaire.", "ارسم خطاً لربط كل غذاء بمجموعته الغذائية."),
    ("Associe les aliments à leur groupe", "اربط الأغذية بمجموعتها"),
    ("Viandes et poissons", "اللحوم والأسماك"),
    ("Groupe alimentaire", "المجموعة الغذائية"),
    ("Complète les phrases", "أكمل الجمل"),
    ("Question :", "السؤال:"),
    (" Son alimentation est-elle équilibrée ? Pourquoi ?", " هل تغذيته/ها متوازنة؟ لماذا؟"),
    ("Son alimentation est-elle équilibrée ? Pourquoi ?", "هل تغذيته/ها متوازنة؟ لماذا؟"),
    (" a) Le jus de fruits", " أ) عصير الفواكه"),
    (" b) L’eau", " ب) الماء"),
    (" c) Le soda", " ج) المشروبات الغازية"),
    ("Féculents", "النشويات"),
    ("Pomme", "تفاحة"),
    ("Poulet", "دجاج"),
    ("Pâtes", "معكرونة"),
    ("Aliments ", "الأغذية "),
    ("Aliments", "الأغذية"),

    # ── Slide 5 ──
    ("Manger équilibré signifie ne manger que des légumes. (Vrai / Faux)", "الأكل المتوازن يعني تناول الخضروات فقط. (صح / خطأ)"),
    ("Les protéines aident à construire les muscles. (Vrai / Faux)", "البروتينات تساعد على بناء العضلات. (صح / خطأ)"),
    ("Le sucre est un aliment indispensable pour la santé. (Vrai / Faux)", "السكر غذاء لا غنى عنه للصحة. (صح / خطأ)"),
    ("Boire de l’eau est important pour rester en bonne santé. (Vrai / Faux)", "شرب الماء مهم للبقاء بصحة جيدة. (صح / خطأ)"),
    ("Entoure Vrai ou Faux", "ضع دائرة حول صح أو خطأ"),
    ("Aliments correspondants", "الأغذية المقابلة"),
    ("Produits laitiers", "منتجات الألبان"),
    ("Viandes, poissons, œufs", "اللحوم والأسماك والبيض"),
    ("Produits sucrés", "المنتجات السكرية"),
    ("Fruits et légumes", "الفواكه والخضروات"),
    ("Analyse d’un menu", "تحليل قائمة طعام"),
    ("Voici le menu du déjeuner de Paul :", "إليك قائمة غداء بول:"),
    ("🥖 Pain blanc + 🍫 Barre chocolatée + 🍔 Hamburger + 🍟 Frites + 🥤 Soda", "🥖 خبز أبيض + 🍫 قطعة شوكولاتة + 🍔 هامبورغر + 🍟 بطاطا مقلية + 🥤 مشروب غازي"),
    ("Ce menu est-il équilibré ? Explique pourquoi.", "هل هذه القائمة متوازنة؟ اشرح لماذا."),
    ("Propose une meilleure alternative pour rendre ce repas plus sain.", "اقترح بديلاً أفضل لجعل هذه الوجبة أكثر صحة."),
    ("Un enfant de 6e année doit consommer environ 2000 kcal par jour. Voici l’apport énergétique de certains aliments :", "يجب أن يستهلك طفل في السنة السادسة حوالي 2000 سعرة حرارية يومياً. إليك الطاقة التي توفرها بعض الأغذية:"),
    ("🍚 1 assiette de riz = 200 kcal", "🍚 طبق أرز = 200 سعرة"),
    ("🍗 1 morceau de poulet = 250 kcal", "🍗 قطعة دجاج = 250 سعرة"),
    ("🍎 1 pomme = 80 kcal", "🍎 تفاحة واحدة = 80 سعرة"),
    ("🥛 1 verre de lait = 150 kcal", "🥛 كوب حليب = 150 سعرة"),
    ("🍕 1 part de pizza = 300 kcal", "🍕 قطعة بيتزا = 300 سعرة"),
    ("🍟 1 portion de frites = 400 kcal", "🍟 حصة بطاطا مقلية = 400 سعرة"),
    ("🍫 1 barre de chocolat = 500 kcal", "🍫 قطعة شوكولاتة = 500 سعرة"),

    # ── Slide 6 ──
    ("Paul mange 1 assiette de riz, 1 morceau de poulet et 1 barre de chocolat. Combien de kcal a-t-il consommé ?", "بول يأكل طبق أرز وقطعة دجاج وقطعة شوكولاتة. كم سعرة حرارية استهلك؟"),
    ("Quel conseil lui donnerais-tu pour équilibrer son repas ?", "ما هي النصيحة التي ستقدمها له لتوازن وجبته؟"),
    ("Réponds en justifiant ta réponse.", "أجب مع تبرير إجابتك."),
    ("Les légumes apportent de l’énergie au corps. (Vrai / Faux)", "الخضروات تعطي الطاقة للجسم. (صح / خطأ)"),
    ("Il est bon de boire des sodas tous les jours. (Vrai / Faux)", "من الجيد شرب المشروبات الغازية كل يوم. (صح / خطأ)"),
    ("Les féculents comme le pain et le riz sont importants dans l’alimentation. (Vrai / Faux)", "النشويات كالخبز والأرز مهمة في التغذية. (صح / خطأ)"),

    # ── Slide 7 ──
    ("Petit-déjeuner :", "وجبة الإفطار:"),
    ("Il faut manger au moins 5 fruits et légumes par jour. (Vrai / Faux)", "يجب تناول 5 فواكه وخضروات على الأقل يومياً. (صح / خطأ)"),
    ("Imagine que tu es un nutritionniste !", "تخيّل أنك طبيب تغذية!"),
    ("Crée un menu équilibré pour une journée complète (Petit-déjeuner, Déjeuner, Goûter, Dîner).", "أنشئ قائمة متوازنة ليوم كامل (إفطار، غداء، وجبة خفيفة، عشاء)."),
    ("Il doit contenir tous les groupes alimentaires et éviter les excès de sucre et de gras.", "يجب أن تحتوي على جميع المجموعات الغذائية وتجنب الإفراط في السكر والدهون."),
    ("Exemple de présentation :", "مثال على التقديم:"),

    # ── Slide 8 ──
    ("Chapitre 2 : L’équilibre énergétique", "الفصل 2: التوازن الطاقوي"),
    ("L’équilibre énergétique est la relation entre l’énergie consommée et l’énergie dépensée par le corps.", "التوازن الطاقوي هو العلاقة بين الطاقة المستهلكة والطاقة التي ينفقها الجسم."),
    ("L’énergie provient des aliments et des boissons que nous consommons.", "الطاقة تأتي من الأغذية والمشروبات التي نستهلكها."),
    ("Le corps utilise cette énergie pour fonctionner (respirer, bouger, réfléchir).", "الجسم يستخدم هذه الطاقة للعمل (التنفس، الحركة، التفكير)."),
    ("Si l’énergie consommée est égale à l’énergie dépensée, le poids reste stable.", "إذا كانت الطاقة المستهلكة تساوي الطاقة المنفقة، يبقى الوزن ثابتاً."),
    ("Si ce n’est pas équilibré, on peut soit prendre du poids (excès), soit en perdre (manque).", "إذا لم يكن متوازناً، قد نكتسب وزناً (فائض) أو نفقده (نقص)."),

    # ── Slide 9 ──
    ("Questions courtes", "أسئلة قصيرة"),
    ("Affirmation", "تأكيد"),
    ("Qu’est-ce qu’un repas équilibré ?", "ما هي الوجبة المتوازنة؟"),
    ("2. Pourquoi le petit-déjeuner est-il important ?", "٢. لماذا يعد الإفطار مهماً؟"),
    ("L’énergie apportée doit être", "الطاقة المقدمة يجب أن تكون"),
    ("égale à celle dépensée", "مساوية لتلك المنفقة"),
    ("de lipides entraîne des", "في الدهون يؤدي إلى"),
    ("maladies cardiaques", "أمراض قلبية"),
    ("La ration alimentaire est la", "الحصة الغذائية هي"),
    ("même pour tous", "نفسها للجميع"),
    ("Vrai ou Faux", "صح أو خطأ"),
    ("Choisis la bonne réponse", "اختر الإجابة الصحيحة"),
    ("L’équilibre énergétique signifie que :", "التوازن الطاقوي يعني أن:"),
    (" a) Il faut manger le plus possible pour avoir de l’énergie", " أ) يجب الأكل أكثر ما يمكن للحصول على الطاقة"),
    (" b) L’énergie consommée doit être égale à l’énergie dépensée", " ب) الطاقة المستهلكة يجب أن تساوي الطاقة المنفقة"),
    (" c) On doit seulement manger des protéines", " ج) يجب تناول البروتينات فقط"),
    ("Trop", "الإفراط"),
    ("Vrai", "صح"),
    ("faux", "خطأ"),

    # ── Slide 10 ──
    ("Quand on mange plus que ce que notre corps dépense, cela peut entraîner :", "عندما نأكل أكثر مما ينفقه جسمنا، يمكن أن يؤدي ذلك إلى:"),
    (" a) Une bonne santé", " أ) صحة جيدة"),
    (" b) Une prise de poids et des maladies", " ب) اكتساب وزن وأمراض"),
    (" c) Un manque d’énergie", " ج) نقص الطاقة"),
    ("Les lipides sont des éléments importants dans l’alimentation, mais en trop grande quantité, ils peuvent :", "الدهون عناصر مهمة في التغذية، لكن بكميات كبيرة جداً يمكن أن:"),
    (" a) Donner plus de muscles", " أ) تعطي مزيداً من العضلات"),
    (" b) Provoquer des maladies cardiaques", " ب) تسبب أمراضاً قلبية"),
    (" c) Améliorer la digestion", " ج) تحسن الهضم"),
    ("Pour maintenir un bon équilibre énergétique, il faut :", "للحفاظ على توازن طاقوي جيد، يجب:"),
    (" a) Manger en grande quantité sans bouger", " أ) الأكل بكميات كبيرة دون حركة"),
    (" b) Faire de l’activité physique et bien manger", " ب) ممارسة النشاط البدني والأكل الجيد"),
    (" c) Éviter complètement les féculents", " ج) تجنب النشويات بشكل كامل"),

    # ── Slide 11 ──
    ("Maladies cardiaques", "أمراض قلبية"),
    ("L’énergie que nous utilisons provient des _____________ que nous mangeons.", "الطاقة التي نستخدمها تأتي من _____________ التي نأكلها."),
    ("Si nous mangeons plus d’énergie que nous en dépensons, nous risquons de ____________.", "إذا أكلنا طاقة أكثر مما ننفق، نخاطر بـ ____________."),
    ("Une personne qui fait beaucoup de sport a besoin de ___________ d’énergie qu’une personne qui reste assise toute la journée.", "الشخص الذي يمارس الرياضة كثيراً يحتاج إلى ___________ طاقة من الشخص الجالس طوال اليوم."),
    ("Les lipides sont nécessaires au corps, mais en trop grande quantité, ils peuvent causer des ____________.", "الدهون ضرورية للجسم، لكن بكميات كبيرة جداً يمكن أن تسبب ____________."),
    ("L’équilibre énergétique signifie que l’énergie ____________ doit être égale à l’énergie ____________.", "التوازن الطاقوي يعني أن الطاقة ____________ يجب أن تساوي الطاقة ____________."),
    ("Terme", "المصطلح"),
    ("Définition", "التعريف"),
    ("Quantité de calories que l’on ", "كمية السعرات "),
    ("dépense en bougeant", "التي تُصرف بالحركة"),
    ("Ensemble des aliments ", "مجموع الأغذية "),
    ("consommés en une journée", "المستهلكة في يوم"),
    ("Nutriments qui donnent de l’énergie mais peuvent causer des maladies s’ils sont consommés en excès", "مواد غذائية تعطي الطاقة لكنها يمكن أن تسبب أمراضاً إذا استُهلكت بإفراط"),
    ("Problèmes de santé liés à une ", "مشاكل صحية مرتبطة بـ "),
    ("mauvaise alimentation", "تغذية سيئة"),
    ("Relie chaque terme à sa définition", "اربط كل مصطلح بتعريفه"),
    ("Analyse de situation", "تحليل الوضعية"),
    (" Mathieu adore manger des hamburgers et des frites tous les jours. Il ne fait pas beaucoup de sport et préfère jouer aux jeux vidéo toute la journée.", " ماتيو يحب أكل الهامبورغر والبطاطا المقلية كل يوم. لا يمارس الرياضة كثيراً ويفضل اللعب بالألعاب الإلكترونية طوال اليوم."),
    ("Questions ", "الأسئلة "),
    ("Quels conseils peux-tu lui donner pour qu’il garde un bon équilibre énergétique ?", "ما هي النصائح التي يمكنك تقديمها له للحفاظ على توازن طاقوي جيد؟"),

    # ── Slide 12 ──
    ("Propose une journée de repas équilibrée pour Mathieu.", "اقترح يوماً من الوجبات المتوازنة لماتيو."),
    ("Un enfant dépense environ 500 kcal par heure lorsqu’il fait du sport et 100 kcal par heure en restant assis.", "يصرف الطفل حوالي 500 سعرة في الساعة عند ممارسة الرياضة و100 سعرة في الساعة عند الجلوس."),
    ("Paul mange 1800 kcal par jour. Il fait 2 heures de sport et reste assis 6 heures.", "بول يأكل 1800 سعرة يومياً. يمارس الرياضة ساعتين ويجلس 6 ساعات."),
    ("Combien de kcal Paul dépense-t-il grâce au sport ?", "كم سعرة حرارية ينفق بول بفضل الرياضة؟"),
    ("Combien de kcal dépense-t-il en restant assis ?", "كم سعرة ينفق بالجلوس؟"),
    ("Quelle est sa dépense énergétique totale sur la journée ?", "ما هو إجمالي إنفاقه الطاقوي في اليوم؟"),
    ("Son énergie consommée est-elle égale à son énergie dépensée ?", "هل طاقته المستهلكة تساوي طاقته المنفقة؟"),
    ("Questions :", "الأسئلة:"),

    # ── Slide 13 ──
    ("La désertification est la transformation des terres fertiles en terres sèches et pauvres, souvent semblables à un désert.", "التصحر هو تحول الأراضي الخصبة إلى أراضٍ جافة وفقيرة، تشبه في الغالب الصحراء."),
    ("Elle est causée par la sécheresse, le manque de pluie et les activités humaines comme la déforestation et le surpâturage.", "ينجم عن الجفاف وندرة الأمطار والأنشطة البشرية كإزالة الغابات والرعي الجائر."),
    ("Elle entraîne la perte de végétation, la diminution de la production agricole et la disparition de certaines espèces.", "يؤدي إلى فقدان الغطاء النباتي وتراجع الإنتاج الزراعي واختفاء بعض الأنواع."),
    ("Elle a des conséquences graves pour les populations, comme le manque de nourriture et d’eau.", "له عواقب وخيمة على السكان كنقص الغذاء والماء."),
    ("Pour lutter contre la désertification, il faut protéger les sols, planter des arbres et utiliser l’eau de manière raisonnable.", "لمكافحة التصحر، يجب حماية التربة وزراعة الأشجار واستخدام الماء بشكل عقلاني."),
    ("Chapitre 3 : La désertification", "الفصل 3: التصحر"),

    # ── Slide 14 ──
    ("Surpâturage (trop d’animaux sur un terrain)", "الرعي الجائر (كثرة الحيوانات على أرض واحدة)"),
    ("Liste cinq causes de la désertification :", "اذكر خمسة أسباب للتصحر:"),
    ("Ton village est menacé par le sable. Propose deux mesures à prendre :", "قريتك مهددة بالرمال. اقترح إجراءين:"),
    ("Qu’est-ce que la désertification ?", "ما هو التصحر؟"),
    (" a) L’extension des déserts à cause des activités humaines et du climat", " أ) توسع الصحاري بسبب الأنشطة البشرية والمناخ"),
    (" b) La construction de nouvelles villes dans le désert", " ب) بناء مدن جديدة في الصحراء"),
    (" c) L’apparition soudaine d’un désert en quelques jours", " ج) ظهور صحراء فجأة في أيام قليلة"),
    ("Quelle est une des principales causes de la désertification ?", "ما هو أحد الأسباب الرئيسية للتصحر؟"),
    (" a) La plantation excessive d’arbres", " أ) زراعة الأشجار بشكل مفرط"),
    (" b) La déforestation et l’agriculture intensive", " ب) إزالة الغابات والزراعة المكثفة"),
    (" c) La construction de barrages", " ج) بناء السدود"),
    ("Quelles sont les conséquences de la désertification ?", "ما هي عواقب التصحر؟"),
    (" a) Une augmentation des terres cultivables", " أ) زيادة الأراضي الزراعية"),
    (" b) Une diminution de l’eau et des sols fertiles", " ب) تراجع المياه والتربة الخصبة"),
    (" c) L’apparition de nouvelles espèces animales", " ج) ظهور أنواع حيوانية جديدة"),
    ("Comment peut-on lutter contre la désertification ?", "كيف يمكن مكافحة التصحر؟"),
    (" a) En coupant plus d’arbres pour utiliser le bois", " أ) بقطع المزيد من الأشجار لاستخدام الخشب"),
    (" b) En reboisant et en protégeant les sols", " ب) بإعادة التشجير وحماية التربة"),
    (" c) En utilisant plus de pesticides", " ج) باستخدام مزيد من المبيدات"),
    ("Causes", "الأسباب"),
    ("Conséquences", "العواقب"),
    ("Perte des terres cultivables", "فقدان الأراضي الزراعية"),
    ("Sécheresses plus fréquentes", "جفاف أكثر تكراراً"),
    ("Appauvrissement du sol", "إفقار التربة"),
    ("Associe chaque cause à ses conséquences", "اربط كل سبب بعواقبه"),

    # ── Slide 15 ──
    ("La désertification est causée par des facteurs ____________ et ____________.", "التصحر ناتج عن عوامل ____________ و____________."),
    ("Lorsqu’il y a peu de végétation, le sol devient ____________ et ne retient plus l’eau.", "عندما يكون الغطاء النباتي ضعيفاً، تصبح التربة ____________ ولا تحتجز الماء."),
    ("L’agriculture intensive et la coupe excessive d’arbres peuvent entraîner la ____________.", "الزراعة المكثفة والقطع المفرط للأشجار يمكن أن يؤديا إلى ____________."),
    ("Pour lutter contre la désertification, on peut planter des ____________ et limiter le ____________.", "لمكافحة التصحر، يمكن زراعة ____________ والحد من ____________."),
    ("Une région avait 30% de sa surface couverte par des arbres en 1990. Aujourd’hui, il n’en reste plus que 10%.", "كانت منطقة ما تغطي 30% من مساحتها بالأشجار عام 1990. اليوم لم يتبق سوى 10%."),
    ("De combien de pourcentage la couverture végétale a-t-elle diminué ?", "بكم انخفضت نسبة الغطاء النباتي؟"),
    ("Si rien n’est fait, combien de pourcentage restera-t-il en 2050 ?", "إذا لم يُتخذ أي إجراء، ما النسبة التي ستبقى عام 2050؟"),
    ("Propose des solutions pour stopper cette diminution.", "اقترح حلولاً لوقف هذا التراجع."),
    ("Situation :", "الوضعية:"),
    ("Dans une région d’Afrique, les habitants constatent que leurs terres deviennent de plus en plus sèches. Il pleut rarement et les cultures ne poussent plus bien. Les paysans coupent les arbres pour avoir du bois de chauffage, et les animaux mangent toute la végétation.", "في منطقة بأفريقيا، يلاحظ السكان أن أراضيهم تزداد جفافاً. نادراً ما تمطر والمحاصيل لم تعد تنمو بشكل جيد. يقطع المزارعون الأشجار للحصول على حطب الوقود، وتأكل الحيوانات كل الغطاء النباتي."),

    # ── Slide 16 ──
    ("Quelles sont les causes de ce problème ?", "ما هي أسباب هذه المشكلة؟"),
    ("Que peut-on faire pour améliorer la situation ?", "ماذا يمكن فعله لتحسين الوضع؟"),

    # ── Slide 17 ──
    ("Chapitre 4 : La pollution", "الفصل 4: التلوث"),
    ("La pollution est la dégradation de l’environnement par des substances nocives.", "التلوث هو تدهور البيئة بسبب مواد ضارة."),
    ("Elle peut toucher l’air, l’eau et le sol.", "يمكن أن يؤثر على الهواء والماء والتربة."),
    ("Elle est causée par les activités humaines comme les usines, les voitures et les déchets.", "ينجم عن الأنشطة البشرية كالمصانع والسيارات والنفايات."),
    ("Elle a des effets négatifs sur la santé des êtres vivants et sur la nature.", "له آثار سلبية على صحة الكائنات الحية والطبيعة."),
    ("Pour lutter contre la pollution, il faut réduire les déchets, recycler et protéger l’environnement.", "لمكافحة التلوث، يجب تقليل النفايات وإعادة التدوير وحماية البيئة."),

    # ── Slide 18 ──
    ("Quelle est une cause de la pollution de l’air ?", "ما هو أحد أسباب تلوث الهواء؟"),
    (" a) La plantation de forêts", " أ) زراعة الغابات"),
    (" b) L’utilisation excessive des voitures et des usines", " ب) الاستخدام المفرط للسيارات والمصانع"),
    (" c) Le tri des déchets", " ج) فرز النفايات"),
    ("Associe les mots à leur définition", "اربط الكلمات بتعريفاتها"),
    ("Décharge sauvage    ......................................................................................", "مكب نفايات    ......................................................................................"),
    ("Recyclage               ......................................................................................", "إعادة التدوير               ......................................................................................"),
    ("Donne deux moyens de lutter contre la pollution à l’école :", "أعطِ وسيلتين لمكافحة التلوث في المدرسة:"),
    ("QCM : Choisis la bonne réponse", "اختيار من متعدد: اختر الإجابة الصحيحة"),
    ("Quelle est une conséquence de la pollution de l’eau ?", "ما هي إحدى عواقب تلوث الماء؟"),
    (" a) L’augmentation de la biodiversité", " أ) زيادة التنوع البيولوجي"),
    (" b) La disparition des poissons et des animaux aquatiques", " ب) اختفاء الأسماك والحيوانات المائية"),
    (" c) La purification naturelle des rivières", " ج) التنقية الطبيعية للأنهار"),
    ("Que peut-on faire pour réduire la pollution ?", "ماذا يمكن فعله لتقليل التلوث؟"),
    (" a) Utiliser les transports en commun ou le vélo", " أ) استخدام وسائل النقل العام أو الدراجة"),
    (" b) Jeter ses déchets n’importe où", " ب) رمي النفايات في أي مكان"),
    (" c) Augmenter l’utilisation du plastique", " ج) زيادة استخدام البلاستيك"),
    ("Qu’est-ce que la pollution ?", "ما هو التلوث؟"),
    (" a) L’amélioration de la qualité de l’air et de l’eau", " أ) تحسين جودة الهواء والماء"),
    (" b) La dégradation de l’environnement par des substances nuisibles", " ب) تدهور البيئة بسبب مواد ضارة"),
    (" c) L’augmentation des plantes et des arbres", " ج) زيادة النباتات والأشجار"),

    # ── Slide 19 ──
    ("Type de pollution", "نوع التلوث"),
    ("Pollution de l’air", "تلوث الهواء"),
    ("Réduction des terres agricoles", "تراجع الأراضي الزراعية"),
    ("Pollution de l’eau", "تلوث الماء"),
    ("Stress et troubles du sommeil", "التوتر واضطرابات النوم"),
    ("Pollution des sols", "تلوث التربة"),
    ("Maladies respiratoires", "أمراض تنفسية"),
    ("Pollution sonore", "التلوث الصوتي"),
    ("Disparition des poissons", "اختفاء الأسماك"),
    ("La pollution est causée par les ____________ des humains.", "التلوث ناجم عن ____________ البشر."),
    ("Les gaz rejetés par les voitures et les usines provoquent la pollution de ____________.", "الغازات التي تطلقها السيارات والمصانع تسبب تلوث ____________."),
    ("La pollution de l’eau peut être causée par les déchets ____________ et les produits chimiques.", "يمكن أن يُسبَّب تلوث الماء بالنفايات ____________ والمواد الكيميائية."),
    ("Pour réduire la pollution, il est important de ____________ les déchets et d’utiliser des énergies ____________.", "لتقليل التلوث، من المهم ____________ النفايات واستخدام طاقات ____________."),
    ("Associe chaque type de pollution à ses conséquences", "اربط كل نوع تلوث بعواقبه"),
    ("Situation", "الوضعية"),
    ("Dans une ville, il y a beaucoup de circulation et les usines rejettent de la fumée noire. L’eau de la rivière voisine est devenue trouble et les poissons meurent. Les habitants commencent à avoir des problèmes de respiration.", "في مدينة ما، يوجد حركة مرور كثيفة وتطلق المصانع دخاناً أسود. مياه النهر المجاور أصبحت عكرة والأسماك تموت. بدأ السكان يعانون من مشاكل في التنفس."),
    ("Quels types de pollution observes-tu dans cette ville ?", "ما أنواع التلوث التي تلاحظها في هذه المدينة؟"),
    ("Quelles sont les causes de ces pollutions ?", "ما هي أسباب هذه الأنواع من التلوث؟"),

    # ── Slide 20 ──
    ("Que peuvent faire les habitants pour améliorer la situation ?", "ماذا يمكن للسكان فعله لتحسين الوضع؟"),
    ("Dans une école, 500 bouteilles en plastique sont utilisées chaque jour. L’école décide de réduire cette consommation en installant des fontaines à eau. Grâce à cette initiative, l’usage des bouteilles baisse de 60%.", "في مدرسة ما، تُستخدم 500 زجاجة بلاستيكية كل يوم. قررت المدرسة تقليل الاستهلاك بتركيب نوافير ماء. بفضل هذه المبادرة، انخفض استخدام الزجاجات بنسبة 60%."),
    ("Combien de bouteilles en plastique sont encore utilisées chaque jour après cette réduction ?", "كم زجاجة بلاستيكية لا تزال تُستخدم يومياً بعد هذا التخفيض؟"),
    ("Combien de bouteilles seront économisées en une semaine ?", "كم زجاجة سيتم توفيرها في أسبوع؟"),
    ("Pourquoi est-il important de réduire l’utilisation du plastique ?", "لماذا من المهم تقليل استخدام البلاستيك؟"),

    # ── Slide 21 ──
    ("Chapitre 5 : Eau et santé", "الفصل 5: الماء والصحة"),
    ("L’eau est indispensable à la vie et au bon fonctionnement du corps.", "الماء ضروري للحياة وللعمل الجيد للجسم."),
    ("Boire de l’eau propre permet de rester en bonne santé et d’éviter les maladies.", "شرب الماء النظيف يساعد على البقاء بصحة جيدة وتجنب الأمراض."),
    ("L’eau est utilisée pour l’hygiène (se laver, nettoyer) et prévenir les infections.", "يُستخدم الماء للنظافة (الاستحمام، التنظيف) ومنع الإصابات."),
    ("L’eau polluée peut transmettre des maladies dangereuses.", "الماء الملوث يمكن أن ينقل أمراضاً خطيرة."),
    ("Il faut économiser l’eau et protéger sa qualité pour préserver la santé.", "يجب توفير الماء وحماية جودته للحفاظ على الصحة."),

    # ── Slide 22 ──
    ("Maladie", "المرض"),
    ("Cause", "السبب"),
    ("Prévention", "الوقاية"),
    ("Paludisme", "الملاريا"),
    ("Choléra", "الكوليرا"),
    ("Complète le tableau", "أكمل الجدول"),
    ("L’eau potable est :", "الماء الصالح للشرب هو:"),
    ("Une eau claire sans microbes", "ماء صافٍ خالٍ من الميكروبات"),
    ("Une eau sucrée", "ماء محلى"),
    ("Une eau chaude", "ماء ساخن"),
    ("Pourquoi l’eau est-elle essentielle pour la santé ?", "لماذا الماء ضروري للصحة؟"),
    (" a) Elle aide à digérer les aliments", " أ) يساعد على هضم الطعام"),
    (" b) Elle permet d’avoir de l’énergie comme les aliments", " ب) يتيح الحصول على الطاقة كالأغذية"),
    (" c) Elle est seulement utile pour se laver", " ج) هو مفيد فقط للاستحمام"),
    ("Quelle quantité d’eau un enfant doit-il boire chaque jour ?", "كم يجب أن يشرب الطفل من الماء يومياً؟"),
    (" a) Environ 0,5 litre", " أ) حوالي 0.5 لتر"),
    (" b) Environ 1 à 1,5 litre", " ب) حوالي 1 إلى 1.5 لتر"),
    (" c) Environ 5 litres", " ج) حوالي 5 لترات"),
    ("Quelle est la principale cause de la pollution de l’eau ?", "ما هو السبب الرئيسي لتلوث الماء؟"),
    (" a) Les feuilles des arbres", " أ) أوراق الأشجار"),
    (" b) Les déchets et les produits chimiques", " ب) النفايات والمواد الكيميائية"),
    (" c) L’eau de pluie", " ج) مياه الأمطار"),
    ("Que peut provoquer le manque d’eau dans notre corps ?", "ماذا يمكن أن يسبب نقص الماء في جسمنا؟"),
    (" a) Une meilleure digestion", " أ) هضم أفضل"),
    (" b) De la fatigue et des maux de tête", " ب) تعب وصداع"),
    (" c) Une augmentation de la force musculaire", " ج) زيادة القوة العضلية"),
    ("Le corps humain est composé à environ ____________ % d’eau.", "يتكون جسم الإنسان من حوالي ____________ % من الماء."),
    ("Il est recommandé de boire environ ____________ litres d’eau par jour.", "يُنصح بشرب حوالي ____________ لتر من الماء يومياً."),
    ("L’eau aide notre corps à ____________ et à éliminer les ____________.", "الماء يساعد جسمنا على ____________ والتخلص من ____________."),
    ("Boire de l’eau propre est important pour éviter les ____________ et rester en bonne ____________.", "شرب الماء النظيف مهم لتجنب ____________ والبقاء في ____________ جيدة."),

    # ── Slide 23 ──
    ("Élément", "العنصر"),
    ("Rôle", "الدور"),
    ("Hydrate le corps et élimine les déchets", "يرطب الجسم ويزيل النفايات"),
    ("Rein", "الكلية"),
    ("Filtre les toxines dans le sang", "تصفية السموم في الدم"),
    ("Peau", "الجلد"),
    ("Évacue l’eau par la transpiration", "يطرد الماء عبر التعرق"),
    ("Estomac", "المعدة"),
    ("Utilise l’eau pour digérer les aliments", "تستخدم الماء لهضم الطعام"),
    ("Associe chaque élément à son rôle dans l’organisme", "اربط كل عنصر بدوره في الجسم"),
    ("Pourquoi Marie ne se sent-elle pas bien ?", "لماذا لا تشعر ماري بالتحسن؟"),
    ("Quels conseils peux-tu lui donner pour améliorer son état de santé ?", "ما هي النصائح التي يمكنك تقديمها لها لتحسين حالتها الصحية؟"),
    ("Marie boit très peu d’eau chaque jour. Elle préfère les sodas et oublie souvent de boire de l’eau. Après quelques jours, elle commence à ressentir de la fatigue et des maux de tête.", "ماري تشرب القليل جداً من الماء كل يوم. تفضل المشروبات الغازية وتنسى في الغالب شرب الماء. بعد أيام قليلة، بدأت تشعر بالتعب والصداع."),
    ("Quels sont les dangers de boire trop de sodas au lieu de l’eau ?", "ما هي مخاطر شرب الكثير من المشروبات الغازية بدلاً من الماء؟"),

    # ── Slide 24 ──
    ("Une famille utilise 10 litres d’eau pour se laver les mains chaque jour. Pour économiser l’eau, elle décide de réduire cette consommation de 30%.", "عائلة تستخدم 10 لترات من الماء لغسل اليدين كل يوم. لتوفير الماء، قررت تقليل الاستهلاك بنسبة 30%."),
    ("Combien de litres d’eau seront économisés chaque jour ?", "كم لتر من الماء سيُوفَّر كل يوم؟"),
    ("Pourquoi est-il important d’économiser l’eau potable ?", "لماذا من المهم توفير الماء الصالح للشرب؟"),
    ("Combien de litres d’eau seront économisés en une semaine ?", "كم لتر من الماء سيُوفَّر في أسبوع؟"),

    # ── Slide 25 ──
    ("Chapitre 6 : La vaccination", "الفصل 6: التطعيم"),
    ("La vaccination consiste à protéger le corps contre certaines maladies grâce à des vaccins.", "التطعيم هو حماية الجسم من بعض الأمراض بواسطة اللقاحات."),
    ("Un vaccin aide le corps à se défendre en préparant le système immunitaire.", "اللقاح يساعد الجسم على الدفاع عن نفسه بتهيئة الجهاز المناعي."),
    ("Elle permet de prévenir des maladies graves comme la rougeole ou la poliomyélite.", "يتيح الوقاية من أمراض خطيرة كالحصبة أو شلل الأطفال."),
    ("La vaccination protège aussi les autres en limitant la propagation des maladies.", "التطعيم يحمي الآخرين أيضاً بالحد من انتشار الأمراض."),
    ("Il est important de respecter le calendrier de vaccination pour être bien protégé.", "من المهم احترام جدول التطعيم للحماية الجيدة."),

    # ── Slide 26 ──
    ("Écris 3 maladies infantiles qu’on peut éviter grâce à la vaccination :", "اكتب 3 أمراض طفولية يمكن تجنبها بالتطعيم:"),
    ("Un traitement après la maladie", "علاج بعد المرض"),
    (" Une prévention avant la maladie", " وقاية قبل المرض"),
    ("Un médicament", "دواء"),
    ("Le carnet de vaccination sert à :", "دفتر التطعيم يُستخدم لـ:"),
    ("Suivre les notes d’école", "متابعة درجات المدرسة"),
    ("Noter les dates des vaccins", "تدوين مواعيد اللقاحات"),
    ("Faire des dessins", "رسم صور"),
    ("À quoi sert la vaccination ?", "ما الفائدة من التطعيم؟"),
    (" a) À soigner une maladie après l’avoir attrapée", " أ) لعلاج مرض بعد الإصابة به"),
    (" b) À protéger contre certaines maladies avant de les attraper", " ب) للوقاية من بعض الأمراض قبل الإصابة"),
    (" c) À renforcer les muscles du corps", " ج) لتقوية عضلات الجسم"),
    ("Comment fonctionne un vaccin ?", "كيف يعمل اللقاح؟"),
    (" a) Il donne au corps des microbes dangereux", " أ) يعطي الجسم ميكروبات خطيرة"),
    (" b) Il apprend au corps à se défendre contre une maladie", " ب) يعلم الجسم الدفاع ضد مرض ما"),
    (" c) Il remplace les globules rouges du sang", " ج) يحل محل كريات الدم الحمراء"),
    ("Pourquoi est-il important de se faire vacciner ?", "لماذا من المهم التطعيم؟"),
    (" a) Pour éviter d’attraper certaines maladies graves", " أ) لتجنب الإصابة ببعض الأمراض الخطيرة"),
    (" b) Pour être plus fort physiquement", " ب) لتكون أقوى جسدياً"),
    (" c) Pour remplacer une alimentation équilibrée", " ج) لاستبدال التغذية المتوازنة"),
    ("Qui doit être vacciné ?", "من يجب تطعيمه؟"),
    (" a) Seulement les adultes", " أ) البالغون فقط"),
    (" b) Seulement les enfants", " ب) الأطفال فقط"),
    (" c) Tout le monde, selon les recommandations des médecins", " ج) الجميع، وفق توصيات الأطباء"),

    # ── Slide 27 ──
    ("Mot", "الكلمة"),
    ("Vaccination", "التطعيم"),
    ("Action de recevoir un vaccin pour se protéger contre une maladie", "فعل تلقي اللقاح للحماية من مرض"),
    ("Immunité", "المناعة"),
    ("Capacité du corps à se défendre contre une maladie", "قدرة الجسم على الدفاع ضد مرض"),
    ("Microbe", "الميكروب"),
    ("Organisme invisible pouvant causer des maladies", "كائن دقيق غير مرئي يمكن أن يسبب أمراضاً"),
    ("Anticorps", "الأجسام المضادة"),
    ("Défenses produites par le corps après un vaccin ou une infection", "دفاعات ينتجها الجسم بعد لقاح أو إصابة"),
    ("Associe chaque mot à sa définition", "اربط كل كلمة بتعريفها"),
    ("Un vaccin permet au corps de se défendre contre ____________.", "اللقاح يتيح للجسم الدفاع ضد ____________."),
    ("Grâce à la vaccination, certaines maladies ont disparu comme ____________.", "بفضل التطعيم، اختفت بعض الأمراض مثل ____________."),
    ("Quand on reçoit un vaccin, notre corps fabrique des ____________ pour se protéger.", "عند تلقي اللقاح، يصنع جسمنا ____________ للحماية."),
    ("Les vaccins sont souvent administrés sous forme d’une ____________.", "تُعطى اللقاحات في الغالب على شكل ____________."),
    ("Tom doit aller chez le médecin pour recevoir un vaccin contre la rougeole. Il a peur de la piqûre et ne comprend pas pourquoi il doit être vacciné.", "توم يجب أن يذهب إلى الطبيب لتلقي لقاح ضد الحصبة. يخشى الحقنة ولا يفهم لماذا يجب تطعيمه."),
    ("Pourquoi est-il important que Tom reçoive ce vaccin ?", "لماذا من المهم أن يتلقى توم هذا اللقاح؟"),
    ("Que peux-tu lui dire pour le rassurer ?", "ماذا يمكنك قوله لطمأنته؟"),
    ("Que se passerait-il si personne ne se faisait vacciner contre la rougeole ?", "ماذا سيحدث لو لم يتطعم أحد ضد الحصبة؟"),

    # ── Slide 28 ──
    ("Dans une école de 500 élèves, 90% des enfants sont vaccinés contre la grippe.", "في مدرسة من 500 تلميذ، تم تطعيم 90% من الأطفال ضد الإنفلونزا."),
    ("Combien d’élèves ont été vaccinés ?", "كم تلميذاً تم تطعيمه؟"),
    ("Combien d’élèves ne sont pas vaccinés ?", "كم تلميذاً لم يتم تطعيمه؟"),
    ("Pourquoi est-il important que la majorité des élèves soient vaccinés ?", "لماذا من المهم أن يكون غالبية التلاميذ مطعمين؟"),

    # ── Generic terms (applied last to avoid clobbering longer strings) ──
    ("Pain", "خبز"),
    ("Lait", "حليب"),
    ("Eau", "الماء"),
]

# Split-fragment replacements: replace first frag with full Arabic, second frag with empty/remnant
SPLIT_REPLACEMENTS = [
    # (frag1_in_at, replacement1, frag2_in_at, replacement2)
    # Slide 3: fats & oils
    ("f", "الدهون والزيوت", "ats &amp; oils", ""),
    # Slide 4 split words
    ("Sit", "وضعية للتحليل", "uation à analyser", ""),
    ("Pr", "منتجات الألبان", "oduits laitiers", ""),
    ("Fr", "الفواكه والخضروات", "uits et légumes", ""),
    # Slide 5
    ("Gr", "المجموعة الغذائية", "oupe alimentaire", ""),
    # Slide 7
    ("D", "الغداء", "éjeuner ", ""),
    ("Goût", "وجبة خفيفة", "er ", ""),
    ("Dî", "العشاء", "ner", ""),
    # Slide 11
    ("É", "الطاقة", "nergie", ""),
    ("Rati", "الحصة الغذائية", "on alimentaire", ""),
    ("L", "الدهون", "ipides", ""),
    # Slide 14
    ("Défo", "إزالة الغابات", "restation", ""),
    ("Réchauffeme", "الاحترار المناخي", "nt climatique", ""),
    ("Agr", "الزراعة المكثفة", "iculture intensive", ""),
    ("Dég", "تدهور التربة", "radation des sols", ""),
    # Slide 18: P + ollution...  (keep dots from second frag)
    ("P", "التلوث", None, None),   # special: handled with regex
    ("M", "الكلمة", "ot", ""),
    # Slide 26
    (" La vaccin", " التطعيم هو:", "ation est :", ""),
]


def apply_regex_replacements(xml):
    # Matching exercise labels with trailing dots (variable dot count)
    xml = re.sub(r'<a:t>(Décharge sauvage)(\s*\.+[^<]*)</a:t>', r'<a:t>مكب نفايات\2</a:t>', xml)
    xml = re.sub(r'<a:t>(Recyclage)(\s*\.+[^<]*)</a:t>', r'<a:t>إعادة التدوير\2</a:t>', xml)
    # "ollution" fragment after P was replaced
    xml = re.sub(r'<a:t>ollution(\s*\.+[^<]*)</a:t>', r'<a:t>\1</a:t>', xml)
    return xml


def apply_split_replacements(xml):
    for item in SPLIT_REPLACEMENTS:
        f1, r1, f2, r2 = item
        if f1 == "P" and f2 is None:
            # Special: replace <a:t>P</a:t> and strip 'ollution' from next <a:t>
            xml = xml.replace("<a:t>P</a:t>", "<a:t>التلوث</a:t>")
            xml = re.sub(r'<a:t>ollution(\s*\.+)', r'<a:t>\1', xml)
        else:
            tag1 = f"<a:t>{f1}</a:t>"
            tag2 = f"<a:t>{f2}</a:t>" if f2 else None
            repl1 = f"<a:t>{r1}</a:t>"
            repl2 = f"<a:t>{r2}</a:t>" if r2 is not None else f"<a:t></a:t>"
            if tag1 in xml:
                xml = xml.replace(tag1, repl1, 1)
            if tag2 and tag2 in xml:
                xml = xml.replace(tag2, repl2, 1)
    return xml


def apply_text_replacements(xml):
    # Normalize all apostrophe variants in <a:t> content to straight apostrophe
    def normalize_at(m):
        content = m.group(1).replace('\u2019', "'").replace('\u2018', "'")
        return '<a:t>' + content + '</a:t>'
    xml = re.sub(r'<a:t>([^<]*)</a:t>', normalize_at, xml)

    for fr, ar in REPLACEMENTS:
        # Also normalize dict key to straight apostrophe
        fr_norm = fr.replace('\u2019', "'").replace('\u2018', "'")
        pattern = r'<a:t>(\s*)' + re.escape(fr_norm) + r'(\s*)</a:t>'
        replacement = r'<a:t>\1' + ar + r'\2</a:t>'
        xml = re.sub(pattern, replacement, xml)
    return xml


with zipfile.ZipFile(src, "r") as zin:
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename.startswith("ppt/slides/slide") and item.filename.endswith(".xml"):
                text = data.decode("utf-8")
                text = apply_split_replacements(text)
                text = apply_regex_replacements(text)
                text = apply_text_replacements(text)
                data = text.encode("utf-8")
                print(f"Traité: {item.filename}")
            zout.writestr(item, data)

print("\nFichier créé:", dst)
