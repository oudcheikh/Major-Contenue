# -*- coding: utf-8 -*-
"""Vidéo U11 — ضرب الكسور.  Rendu : venv/bin/manim -qh scene_u11.py VideoU11
Cœur de la vidéo : 1/2 × 3/4 animé — les deux بسط s'illuminent et fusionnent vers le
بسط du résultat (idem مقام), puis vérification visuelle sur le شريط : ثلث النصف = السدس."""
from manim import (VGroup, Line, SurroundingRectangle, RoundedRectangle,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash,
                   UP, DOWN, LEFT, RIGHT, DR)

from video_common import (MajorScene, ar, num, titled, frac, strip,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


class VideoU11(MajorScene):
    AUDIO = HERE / "audio_u11"
    UNIT_AR = "الوحدة 11"
    UNIT_COLOR = GREEN
    TITLE = "ضرب الكسور"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 11"

    # ── 2. القاعدة : بسط × بسط، مقام × مقام ─────────────────────
    def s_regle(self):
        d = self.seg("rule1")
        head = titled("القاعدة: البسط × البسط والمقام × المقام", 32, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(1.6)
        c1 = RoundedRectangle(corner_radius=0.22, width=5.2, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.9 + UP * 0.7)
        c1t = ar("أضرب البسط في البسط", 28, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=5.2, height=1.1, fill_color=BLUE,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.9 + DOWN * 0.7)
        c2t = ar("أضرب المقام في المقام", 28, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.wait(1.4)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 5.7, 0.2))

        d = self.seg("rule2")
        c3 = RoundedRectangle(corner_radius=0.22, width=5.2, height=1.1, fill_color=ROSE,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.9 + DOWN * 2.1)
        c3t = ar("ثم أبسّط إن أمكن", 28, "BOLD", "#FFFFFF").move_to(c3)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(c3, c3t), rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 0.9, 0.2))
        self.clear_all()

    # ── 3. المثال المحوري : 1/2 × 3/4 = 3/8 ─────────────────────
    def s_exemple(self):
        d = self.seg("ex1")
        head = titled("مثال: النصف × ثلاثة أرباع", 36, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        f1 = frac(1, 2, 58).move_to([3.4, 0.9, 0])       # يظهر أولًا على اليمين
        sgn = num("×", 56, GOLD).move_to([2.3, 0.9, 0])
        f2 = frac(3, 4, 58).move_to([1.2, 0.9, 0])
        self.sfx("pop")
        self.play(FadeIn(f1, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(FadeIn(sgn, scale=0.5), FadeIn(f2, scale=0.5, rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 2.8, 0.2))

        eqs = num("=", 56).move_to([0.0, 0.9, 0])
        rf = frac(3, 8, 58).move_to([-1.4, 0.9, 0])
        rf[0].set_color(GREEN)
        rf[2].set_color(BLUE)

        # ex2 : البسطان يشتعلان ويندمجان في بسط الناتج
        d = self.seg("ex2")
        self.play(Indicate(f1[0], color=GREEN, scale_factor=1.5),
                  Indicate(f2[0], color=GREEN, scale_factor=1.5), run_time=1.0)
        self.wait(1.2)
        self.sfx("whoosh")
        self.play(FadeIn(eqs), Create(rf[1]), run_time=0.8)
        c1, c2 = f1[0].copy().set_color(GREEN), f2[0].copy().set_color(GREEN)
        self.sfx("pop")
        self.play(ReplacementTransform(VGroup(c1, c2), rf[0]), run_time=1.1)
        self.wait(max(d - 4.1, 0.2))

        # ex3 : المقامان كذلك
        d = self.seg("ex3")
        self.play(Indicate(f1[2], color=BLUE, scale_factor=1.5),
                  Indicate(f2[2], color=BLUE, scale_factor=1.5), run_time=1.0)
        self.wait(1.4)
        c3, c4 = f1[2].copy().set_color(BLUE), f2[2].copy().set_color(BLUE)
        self.sfx("pop")
        self.play(ReplacementTransform(VGroup(c3, c4), rf[2]), run_time=1.1)
        self.wait(max(d - 3.5, 0.2))

        # ex4 : الناتج مؤطر
        d = self.seg("ex4")
        frame = SurroundingRectangle(rf, color=GREEN, corner_radius=0.15, buff=0.25)
        lab = ar("ثلاثة أثمان", 30, "BOLD", GREEN).next_to(frame, DOWN, buff=0.35)
        self.sfx("ding")
        self.play(Create(frame), FadeIn(lab), run_time=1.0)
        self.play(Flash(rf, color=GREEN, flash_radius=1.7), run_time=0.9)
        self.wait(max(d - 1.9, 0.2))
        self.clear_all()

    # ── 4. أتحقق بالرسم : ثلث النصف = السدس ─────────────────────
    def s_verif(self):
        d = self.seg("ver1")
        head = titled("كلمة «مِن» تعني الضرب!", 36, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(1.8)
        phrase = ar("ثلث النصف", 38, "BOLD", LILA).move_to([3.6, 1.2, 0])
        self.sfx("pop")
        self.play(FadeIn(phrase, scale=0.6, rate_func=BOUNCE), run_time=0.9)
        fA = frac(1, 3, 48).move_to([0.9, 1.2, 0])
        sg = num("×", 44, GOLD).move_to([-0.1, 1.2, 0])
        fB = frac(1, 2, 48).move_to([-1.1, 1.2, 0])
        self.sfx("whoosh")
        self.play(FadeIn(VGroup(fA, sg, fB), shift=LEFT * 0.5), run_time=1.0)
        self.wait(max(d - 4.6, 0.2))

        d = self.seg("ver2")
        s1 = strip(2, 1, width=5.6, height=0.95, fill=YELL).move_to([0.6, -0.7, 0])
        self.sfx("pop")
        self.play(FadeIn(s1, scale=0.7, rate_func=BOUNCE), run_time=0.9)
        self.wait(1.6)
        s2 = strip(6, 3, width=5.6, height=0.95, fill=YELL).move_to([0.6, -0.7, 0])
        self.sfx("whoosh")
        self.play(Transform(s1, s2), run_time=1.1)   # النصف مقسوم إلى 3 حصص
        self.wait(1.5)
        s3 = strip(6, 1, width=5.6, height=0.95, fill=GREEN).move_to([0.6, -0.7, 0])
        self.sfx("ding")
        self.play(Transform(s1, s3), run_time=1.0)   # نأخذ حصة واحدة من 6
        res = frac(1, 6, 48, GREEN).move_to([-4.2, -0.9, 0])
        lab = ar("السُّدُس", 30, "BOLD", GREEN).next_to(res, DOWN, buff=0.3)
        self.sfx("pop")
        self.play(FadeIn(VGroup(res, lab), scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 7.0, 0.2))
        self.clear_all()

    # ── 5. مسألة الكراس : ثلثا كتاب من 60 صفحة ──────────────────
    def s_probleme(self):
        d = self.seg("app1")
        head = titled("مسألة: كتاب المختار", 38, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        row = VGroup(ar("الكتاب:", 30, "BOLD"), num("60", 46, BLUE),
                     ar("صفحة", 30, "BOLD")).arrange(LEFT, buff=0.3).move_to([0.4, 1.4, 0])
        self.sfx("pop")
        self.play(FadeIn(row, shift=LEFT * 0.4, rate_func=BOUNCE), run_time=0.9)
        s0 = strip(3, 0, width=6.3, height=1.0, fill=GREEN).move_to([0.4, -0.1, 0])
        self.play(Create(s0), run_time=0.9)
        q = ar("قرأ الثلثين — كم صفحة؟", 28, "BOLD", GOLD).move_to([0.4, -1.35, 0])
        self.play(FadeIn(q, shift=LEFT * 0.4), run_time=0.8)
        self.wait(max(d - 3.5, 0.2))

        d = self.seg("app2")
        s2 = strip(3, 2, width=6.3, height=1.0, fill=GREEN).move_to([0.4, -0.1, 0])
        self.sfx("whoosh")
        self.play(Transform(s0, s2), run_time=1.0)
        n1 = num("20", 38).move_to(s2[0].get_center())
        n2 = num("20", 38).move_to(s2[1].get_center())
        self.sfx("pop")
        self.play(FadeIn(n1, scale=0.5, rate_func=BOUNCE), run_time=0.6)
        self.sfx("pop")
        self.play(FadeIn(n2, scale=0.5, rate_func=BOUNCE), run_time=0.6)
        self.wait(1.6)
        res = VGroup(ar("قرأ", 30, "BOLD", GREEN), num("40", 50, GREEN),
                     ar("صفحة", 30, "BOLD", GREEN)).arrange(LEFT, buff=0.3)
        res.move_to([0.4, -2.5, 0])
        box = SurroundingRectangle(res, color=GREEN, corner_radius=0.15, buff=0.2)
        self.sfx("ding")
        self.play(FadeIn(res, scale=0.6, rate_func=BOUNCE), Create(box), run_time=1.0)
        self.play(Flash(res, color=GREEN, flash_radius=2.0), run_time=0.9)
        self.wait(max(d - 5.7, 0.2))
        self.clear_all()

    # ── 6. انتبه : القاعدة للضرب فقط ────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! القاعدة للضرب فقط", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=5.6, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.7 + UP * 0.5)
        c1t = ar("في الضرب: مقام × مقام", 28, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=5.6, height=1.1, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.7 + DOWN * 0.9)
        c2t = ar("في الجمع: لا أجمع المقامات!", 26, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 7. السر : أبسّط بعد الضرب (2/3 × 3/4 = 6/12 = 1/2) ──────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: أبسّط بعد الضرب!", 36, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.8)
        fa = frac(2, 3, 52).move_to([3.2, 0.4, 0])
        sg = num("×", 52, GOLD).move_to([2.1, 0.4, 0])
        fb = frac(3, 4, 52).move_to([1.0, 0.4, 0])
        for m in (fa, sg, fb):     # ظهور من اليمين إلى اليسار
            self.sfx("pop")
            self.play(FadeIn(m, scale=0.5, rate_func=BOUNCE), run_time=0.7)
        self.wait(1.2)
        e1 = num("=", 52).move_to([-0.1, 0.4, 0])
        fc = frac(6, 12, 52).move_to([-1.5, 0.4, 0])
        self.sfx("pop")
        self.play(FadeIn(VGroup(e1, fc), scale=0.6, rate_func=BOUNCE), run_time=0.9)
        self.wait(2.0)
        e2 = num("=", 52).move_to([-3.0, 0.4, 0])
        fd = frac(1, 2, 52, GREEN).move_to([-4.2, 0.4, 0])
        self.sfx("ding")
        self.play(FadeIn(e2), ReplacementTransform(fc.copy(), fd), run_time=1.0)
        lab = ar("قسمتُ البسط والمقام على 6", 26, "BOLD", LILA).move_to([-2.4, -1.3, 0])
        self.play(FadeIn(lab, shift=UP * 0.3), run_time=0.9)
        self.play(Flash(fd, color=GREEN, flash_radius=1.5), run_time=0.9)
        self.wait(max(d - 11.6, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أضرب كسرين: البسط في البسط والمقام في المقام",
            "أبسّط الكسر الناتج بعد الضرب",
            "أحلّ مسائل الضرب من حياتنا اليومية",
        ])
        self.s_regle()
        self.s_exemple()
        self.s_verif()
        self.s_probleme()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
