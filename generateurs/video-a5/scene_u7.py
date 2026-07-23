# -*- coding: utf-8 -*-
"""Vidéo U7 — المستقيمات المتوازية والمتقاطعة.  Rendu : venv/bin/manim -qh scene_u7.py VideoU7
Cœur de la vidéo : les droites se TRACENT à l'écran — les parallèles se prolongent
sans jamais se couper (سكة القطار), les sécantes marquent leur نقطة التقاطع,
les perpendiculaires reçoivent le petit carré de la زاوية قائمة."""
from manim import (VGroup, Line, DoubleArrow, Dot, Square, Polygon, Rectangle,
                   RoundedRectangle, Cross,
                   FadeIn, FadeOut, Write, Create, Transform, GrowFromCenter,
                   Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)

BROWN = "#a76b3f"


class VideoU7(MajorScene):
    AUDIO = HERE / "audio_u7"
    UNIT_AR = "الوحدة 7"
    UNIT_COLOR = BLUE
    TITLE = "المستقيمات المتوازية والمتقاطعة"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 7"

    # ── 2. المتوازيان : لا يلتقيان أبدًا ────────────────────────
    def s_paralleles(self):
        d = self.seg("par1")
        head = titled("المستقيمان المتوازيان", 40, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        l1 = Line([-3.2, 0.8, 0], [3.2, 0.8, 0], color=BLUE, stroke_width=6)
        l2 = Line([-3.2, -0.6, 0], [3.2, -0.6, 0], color=BLUE, stroke_width=6)
        self.sfx("whoosh")
        self.play(Create(l1), run_time=1.0)
        self.sfx("whoosh")
        self.play(Create(l2), run_time=1.0)
        self.wait(max(d - 2.9, 0.2))

        # par2 : on les PROLONGE — ils ne se coupent jamais
        d = self.seg("par2")
        L1 = Line([-5.9, 0.8, 0], [5.9, 0.8, 0], color=BLUE, stroke_width=6)
        L2 = Line([-5.9, -0.6, 0], [5.9, -0.6, 0], color=BLUE, stroke_width=6)
        self.sfx("whoosh")
        self.play(Transform(l1, L1), Transform(l2, L2), run_time=1.4)
        never = ar("لا يلتقيان أبدًا!", 30, "BOLD", GREEN).move_to([0, -1.9, 0])
        self.sfx("ding")
        self.play(FadeIn(never, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 2.3, 0.2))

        # par3 : نفس المسافة ici et là
        d = self.seg("par3")
        m1 = DoubleArrow([-4.5, 0.8, 0], [-4.5, -0.6, 0], color=GOLD, stroke_width=5,
                         buff=0, max_tip_length_to_length_ratio=0.18)
        lab1 = ar("نفس المسافة", 22, "BOLD", GOLD).move_to([-4.5, -1.2, 0])
        m2 = DoubleArrow([4.0, 0.8, 0], [4.0, -0.6, 0], color=GOLD, stroke_width=5,
                         buff=0, max_tip_length_to_length_ratio=0.18)
        lab2 = ar("نفس المسافة", 22, "BOLD", GOLD).move_to([4.0, -1.2, 0])
        self.sfx("pop")
        self.play(GrowFromCenter(m2, rate_func=BOUNCE), FadeIn(lab2), run_time=1.0)
        self.sfx("pop")
        self.play(GrowFromCenter(m1, rate_func=BOUNCE), FadeIn(lab1), run_time=1.0)
        self.wait(max(d - 2.0, 0.2))

        # par4 : سكة القطار
        d = self.seg("par4")
        self.play(FadeOut(m1), FadeOut(m2), FadeOut(lab1), FadeOut(lab2),
                  FadeOut(never), run_time=0.5)
        sleepers = VGroup(*[Rectangle(width=0.28, height=1.9, fill_color=BROWN,
                                      fill_opacity=0.9, stroke_color=INK, stroke_width=1.5)
                           .move_to([x, 0.1, 0])
                            for x in [5.0, 3.75, 2.5, 1.25, 0.0, -1.25, -2.5, -3.75, -5.0]])
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(s, shift=DOWN * 0.3, rate_func=BOUNCE)
                                for s in sleepers], lag_ratio=0.08),
                  l1.animate.set_color(INK), l2.animate.set_color(INK), run_time=1.3)
        rail = ar("سكة القطار: مستقيمات متوازية", 28, "BOLD", BROWN).move_to([0, -2.1, 0])
        self.sfx("ding")
        self.play(FadeIn(rail, shift=UP * 0.25, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 2.6, 0.2))
        self.clear_all()

    # ── 3. المتقاطعان : نقطة التقاطع ────────────────────────────
    def s_secantes(self):
        d = self.seg("sec1")
        head = titled("المستقيمان المتقاطعان", 40, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.l1 = Line([-3.6, -1.8, 0], [3.6, 1.0, 0], color=ROSE, stroke_width=6)
        self.l2 = Line([-3.6, 1.0, 0], [3.6, -1.8, 0], color=BLUE, stroke_width=6)
        self.sfx("whoosh")
        self.play(Create(self.l1), run_time=1.0)
        self.sfx("whoosh")
        self.play(Create(self.l2), run_time=1.0)
        self.wait(max(d - 2.9, 0.2))

        d = self.seg("sec2")
        pt = Dot([0, -0.4, 0], radius=0.11, color=REDA)
        self.sfx("ding")
        self.play(GrowFromCenter(pt, rate_func=BOUNCE), run_time=0.6)
        self.play(Flash(pt, color=REDA, flash_radius=0.7), run_time=0.8)
        lab = ar("نقطة التقاطع", 28, "BOLD", REDA).move_to([0, -2.4, 0])
        self.sfx("pop")
        self.play(FadeIn(lab, shift=UP * 0.25, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 2.2, 0.2))
        self.pt, self.lab_pt, self.head_sec = pt, lab, head

    # ── 4. المتعامدان : الزاوية القائمة ─────────────────────────
    def s_perpendiculaires(self):
        d = self.seg("perp1")
        head2 = titled("المستقيمان المتعامدان", 40, GREEN)
        H = Line([-3.6, -0.4, 0], [3.6, -0.4, 0], color=ROSE, stroke_width=6)
        V = Line([0, -2.0, 0], [0, 1.4, 0], color=BLUE, stroke_width=6)
        self.sfx("whoosh")
        self.play(Transform(self.l1, H), Transform(self.l2, V),
                  Transform(self.head_sec, head2), FadeOut(self.lab_pt), run_time=1.3)
        self.wait(max(d - 1.3, 0.2))

        d = self.seg("perp2")
        sq = Square(0.4, stroke_color=REDA, stroke_width=4).move_to([0.2, -0.2, 0])
        self.sfx("ding")
        self.play(Create(sq), run_time=0.8)
        deg = num("90°", 34, REDA).move_to([0.95, 0.3, 0])
        self.sfx("pop")
        self.play(FadeIn(deg, scale=0.5, rate_func=BOUNCE), run_time=0.7)
        lab = ar("متعامدان: زاوية قائمة", 28, "BOLD", GREEN).move_to([0, -2.6, 0])
        self.play(FadeIn(lab, shift=UP * 0.25, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 2.3, 0.2))
        self.clear_all()

    # ── 5. الرسم بالمسطرة والكوس ────────────────────────────────
    def s_dessin(self):
        d = self.seg("draw1")
        head = titled("أرسم متوازيين بالمسطرة والكوس", 34, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        ruler = Rectangle(width=7.2, height=0.7, fill_color=YELL, fill_opacity=0.7,
                          stroke_color=INK, stroke_width=2.5).move_to([0, -1.75, 0])
        lab_r = ar("المسطرة", 22, "BOLD", GOLD).move_to([0, -1.75, 0])
        self.sfx("pop")
        self.play(FadeIn(VGroup(ruler, lab_r), shift=UP * 0.3, rate_func=BOUNCE),
                  run_time=0.7)
        kos = Polygon([-1.5, -1.4, 0], [0.7, -1.4, 0], [-1.5, 0.8, 0],
                      fill_color=BLUE, fill_opacity=0.45, stroke_color=INK,
                      stroke_width=2.5)
        lab_k = ar("الكوس", 22, "BOLD", BLUE).move_to([-0.9, -0.85, 0])
        self.sfx("pop")
        self.play(FadeIn(VGroup(kos, lab_k), shift=DOWN * 0.3, rate_func=BOUNCE),
                  run_time=0.7)
        d1 = Line([-1.5, -1.4, 0], [-1.5, 1.6, 0], color=GREEN, stroke_width=6)
        self.sfx("whoosh")
        self.play(Create(d1), run_time=0.8)
        self.sfx("whoosh")
        self.play(VGroup(kos, lab_k).animate.shift(RIGHT * 2.6), run_time=0.9)
        d2 = Line([1.1, -1.4, 0], [1.1, 1.6, 0], color=GREEN, stroke_width=6)
        self.sfx("whoosh")
        self.play(Create(d2), run_time=0.8)
        lab = ar("متوازيان!", 30, "BOLD", GREEN).move_to([3.3, 0.3, 0])
        self.sfx("ding")
        self.play(FadeIn(lab, scale=0.5, rate_func=BOUNCE), run_time=0.6)
        self.wait(max(d - 5.4, 0.2))
        self.clear_all()

    # ── 6. انتبه : ليس كل متقاطعين متعامدين ─────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("ليس كل متقاطعين متعامدين!", 34, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        l1 = Line([1.0, -1.45, 0], [4.8, 0.45, 0], color=ROSE, stroke_width=6)
        l2 = Line([1.0, 0.45, 0], [4.8, -1.45, 0], color=BLUE, stroke_width=6)
        self.sfx("whoosh")
        self.play(Create(l1), Create(l2), run_time=1.2)
        # piège : Text mélangeant chiffres et « ؟ » arabe rend un mobject vide
        fake = VGroup(num("90°", 32, REDA), ar("؟", 30, "BOLD", REDA)
                      ).arrange(LEFT, buff=0.08).move_to([3.6, 0.1, 0])
        self.sfx("pop")
        self.play(FadeIn(fake, scale=0.5, rate_func=BOUNCE), run_time=0.7)
        cross = Cross(fake, stroke_color=REDA, stroke_width=5)
        self.sfx("boing")
        self.play(Create(cross), run_time=0.7)
        verdict = ar("تحقّق بالكوس!", 28, "BOLD", GREEN).move_to([2.9, -2.3, 0])
        self.sfx("ding")
        self.play(FadeIn(verdict, shift=UP * 0.25, rate_func=BOUNCE), run_time=0.8)
        self.play(Wiggle(garcon), run_time=1.0)
        self.wait(max(d - 5.4, 0.2))
        self.clear_all()

    # ── 7. السر : حافتا المسطرة متوازيتان ───────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ صغير قبل أن نفترق", 42, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        ruler = Rectangle(width=6.5, height=0.9, fill_color=YELL, fill_opacity=0.85,
                          stroke_color=INK, stroke_width=2.5).move_to([0, -0.1, 0])
        lab_r = ar("مسطرتي", 24, "BOLD", GOLD).move_to([0, -0.1, 0])
        self.sfx("pop")
        self.play(FadeIn(VGroup(ruler, lab_r), shift=UP * 0.3, rate_func=BOUNCE),
                  run_time=0.8)
        top = Line([-3.25, 0.35, 0], [3.25, 0.35, 0], color=BLUE, stroke_width=6)
        bot = Line([-3.25, -0.55, 0], [3.25, -0.55, 0], color=BLUE, stroke_width=6)
        self.sfx("whoosh")
        self.play(Create(top), run_time=0.8)
        self.sfx("whoosh")
        self.play(Create(bot), run_time=0.8)
        self.sfx("whoosh")
        self.play(FadeOut(VGroup(ruler, lab_r), shift=DOWN * 1.6), run_time=0.9)
        lab = ar("متوازيان!", 34, "BOLD", GREEN).move_to([0, -1.7, 0])
        self.sfx("ding")
        self.play(FadeIn(lab, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        self.play(Flash(lab, color=GREEN, flash_radius=1.8), run_time=0.8)
        self.wait(max(d - 5.9, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أتعرّف المتوازيين والمتقاطعين والمتعامدين",
            "أجد أمثلة لها في القسم والشارع",
            "أرسمها بدقة بالمسطرة والكوس",
        ])
        self.s_paralleles()
        self.s_secantes()
        self.s_perpendiculaires()
        self.s_dessin()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
