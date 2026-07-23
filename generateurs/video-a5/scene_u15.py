# -*- coding: utf-8 -*-
"""Vidéo U15 — النسب المئوية.  Rendu : venv/bin/manim -qh scene_u15.py VideoU15
Cœur de la vidéo : le شريط de 10 حصص (= 100 خانة) se COLORE à l'écran :
5 حصص = 50% = النصف, 25% = الربع sur le قرص ; puis 50% من 200 calculé et
vérifié, et la مسألة du cahier : كرة بـ 80 أوقية، تخفيض 25%."""
from manim import (VGroup, Rectangle, RoundedRectangle, Circle, Line, SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled, strip, pie, frac,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


class VideoU15(MajorScene):
    AUDIO = HERE / "audio_u15"
    UNIT_AR = "الوحدة 15"
    UNIT_COLOR = ROSE
    TITLE = "النسب المئوية"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 15"

    # ── 2. المفهوم : «من مئة» على الشريط ────────────────────────
    def s_def(self):
        d = self.seg("def1")
        head = titled("النسبة المئوية تعني: من مئة", 34, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        s = strip(10, 0, width=9.0, height=1.0, fill=ROSE).move_to([0, 0.6, 0])
        self.sfx("whoosh")
        self.play(Create(s), run_time=1.4)
        lab = VGroup(ar("الشريط كله =", 28, "BOLD"), num("100", 38, GOLD),
                     ar("خانة", 28, "BOLD")).arrange(LEFT, buff=0.3).move_to([0, 1.8, 0])
        self.sfx("pop")
        self.play(FadeIn(lab, shift=DOWN * 0.3), run_time=0.9)
        one = ar("الحصة الواحدة = %10", 26, "BOLD", BLUE).move_to([0, -0.6, 0])
        self.play(FadeIn(one, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - 3.2, 0.2))

        d = self.seg("def2")
        s5 = strip(10, 5, width=9.0, height=1.0, fill=ROSE).move_to([0, 0.6, 0])
        self.sfx("whoosh")
        self.play(Transform(s, s5), run_time=1.3)
        res = VGroup(num("%50", 44, ROSE), num("=", 40),
                     ar("النصف!", 32, "BOLD", GREEN)).arrange(LEFT, buff=0.35)
        res.move_to([0, -1.7, 0])
        box = SurroundingRectangle(res, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(res, shift=UP * 0.3), Create(box), run_time=1.0)
        self.wait(max(d - 2.3, 0.2))

        d = self.seg("def3")
        p = pie(4, 1, radius=1.1, fill=LILA).move_to([-4.6, 0.4, 0])
        pl = VGroup(num("%25", 34, LILA), num("=", 30),
                    ar("الربع", 26, "BOLD", LILA)).arrange(LEFT, buff=0.25)
        pl.next_to(p, DOWN, buff=0.35)
        self.sfx("pop")
        self.play(GrowFromCenter(p, rate_func=BOUNCE), FadeIn(pl, shift=UP * 0.2),
                  run_time=1.1)
        self.wait(max(d - 1.1, 0.2))
        self.clear_all()

    # ── 3. الطريقة : أضرب ثم أقسم على 100 ───────────────────────
    def s_meth(self):
        d = self.seg("meth1")
        head = titled("كيف أحسب نسبة من عدد؟", 36, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        c1 = RoundedRectangle(corner_radius=0.22, width=6.0, height=1.15, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.6 + UP * 0.4)
        c1n = num("1", 34, "#FFFFFF").move_to(c1.get_right() + LEFT * 0.55)
        c1t = ar("أضرب العدد في النسبة", 26, "BOLD", "#FFFFFF").move_to(
            c1.get_center() + LEFT * 0.3)
        c2 = RoundedRectangle(corner_radius=0.22, width=6.0, height=1.15, fill_color=BLUE,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.6 + DOWN * 1.0)
        c2n = num("2", 34, "#FFFFFF").move_to(c2.get_right() + LEFT * 0.55)
        c2t = ar("أقسم الناتج على 100", 26, "BOLD", "#FFFFFF").move_to(
            c2.get_center() + LEFT * 0.3)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1n, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2n, c2t), rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 2.7, 0.2))
        self.clear_all()

    # ── 4. مثال : %50 من 200 ────────────────────────────────────
    def s_calc(self):
        d = self.seg("calc1")
        head = titled("مثال: %50 من 200", 38, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        calc = VGroup(num("200", 44), ar("×", 32, "BOLD", GOLD), num("50", 44),
                      ar("÷", 32, "BOLD", ROSE), num("100", 44),
                      num("=", 40), num("100", 52, GREEN)).arrange(LEFT, buff=0.3)
        calc.move_to([0, 0.5, 0])
        self.sfx("pop")
        self.play(FadeIn(calc, shift=UP * 0.3), run_time=1.2)
        self.play(Flash(calc[6], color=GREEN, flash_radius=1.3), run_time=0.8)
        self.wait(max(d - 2.9, 0.2))

        d = self.seg("calc2")
        s = strip(2, 1, width=6.0, height=0.9, fill=GREEN).move_to([0, -1.3, 0])
        self.sfx("whoosh")
        self.play(Create(s), run_time=1.0)
        ver = VGroup(ar("النصف من", 28, "BOLD"), num("200", 38),
                     num("=", 34), num("100", 44, GREEN),
                     ar("متفقان!", 28, "BOLD", GOLD)).arrange(LEFT, buff=0.3)
        ver.move_to([0, -2.5, 0])
        self.sfx("ding")
        self.play(FadeIn(ver, shift=UP * 0.3), run_time=1.0)
        self.wait(max(d - 2.0, 0.2))
        self.clear_all()

    # ── 5. مسألة السوق : كرة 80 أوقية، تخفيض %25 ────────────────
    def s_prob(self):
        d = self.seg("prob1")
        head = titled("من السوق: تخفيض %25 على الكرة", 32, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        ball = VGroup()
        b = Circle(radius=0.85, fill_color=YELL, fill_opacity=1,
                   stroke_color=INK, stroke_width=3).move_to([4.2, 0.0, 0])
        b2 = Line([3.35, 0.0, 0], [5.05, 0.0, 0], color=INK, stroke_width=2.5)
        ball.add(b, b2)
        prix = VGroup(num("80", 44), ar("أوقية", 28, "BOLD")).arrange(LEFT, buff=0.3)
        prix.next_to(ball, DOWN, buff=0.35)
        tag = RoundedRectangle(corner_radius=0.18, width=2.3, height=0.85,
                               fill_color=REDA, fill_opacity=0.95,
                               stroke_color=INK, stroke_width=2.5).move_to([2.6, 1.3, 0])
        tagt = num("-25%", 34, "#FFFFFF").move_to(tag)
        self.sfx("pop")
        self.play(FadeIn(ball, scale=0.4, rate_func=BOUNCE), FadeIn(prix), run_time=1.0)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(tag, tagt), rate_func=BOUNCE), run_time=0.9)
        q = ar("ما قيمة التخفيض؟", 30, "BOLD", REDA).move_to([-2.6, 0.8, 0])
        self.play(FadeIn(q, shift=LEFT * 0.4), run_time=0.9)
        self.wait(max(d - 2.8, 0.2))

        d = self.seg("prob2")
        calc = VGroup(num("80", 42), ar("×", 30, "BOLD", GOLD), num("25", 42),
                      ar("÷", 30, "BOLD", ROSE), num("100", 42),
                      num("=", 38), num("20", 50, REDA),
                      ar("أوقية", 26, "BOLD", REDA)).arrange(LEFT, buff=0.28)
        calc.move_to([-1.2, -1.4, 0])
        box = SurroundingRectangle(calc, color=REDA, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        self.play(Flash(calc[6], color=REDA, flash_radius=1.2), run_time=0.8)
        self.wait(max(d - 1.9, 0.2))
        self.clear_all()

    # ── 6. انتبه : الثمن الجديد ─────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! التخفيض ليس الثمن الجديد", 32, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=7.2, height=1.1, fill_color=BLUE,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.0 + UP * 0.5)
        c1t = ar("الثمن الجديد = القديم − التخفيض", 26, "BOLD", "#FFFFFF").move_to(c1)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 2.0, 0.2))

        d = self.seg("att2")
        calc = VGroup(num("80", 42), num("−", 38, REDA), num("20", 42),
                      num("=", 38), num("60", 50, GREEN),
                      ar("أوقية", 26, "BOLD", GREEN)).arrange(LEFT, buff=0.28)
        calc.move_to([2.0, -1.1, 0])
        box = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        self.play(Flash(calc[4], color=GREEN, flash_radius=1.2), run_time=0.8)
        self.wait(max(d - 1.9, 0.2))
        self.clear_all()

    # ── 7. السر : الاختصارات ────────────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("اختصارات سريعة!", 38, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.4)
        rows = [("%50", "النصف", GREEN), ("%25", "الربع", BLUE),
                ("%10", "أقسم على 10", GOLD)]
        t = 0
        for i, (pc, txt, col) in enumerate(rows):
            c = RoundedRectangle(corner_radius=0.22, width=7.0, height=1.05,
                                 fill_color=col, fill_opacity=0.92,
                                 stroke_color=INK).move_to([0, 0.65 - 1.3 * i, 0])
            cv = num(pc, 34, "#FFFFFF").move_to(c.get_center() + RIGHT * 2.2)
            ceq = num("=", 30, "#FFFFFF").move_to(c.get_center() + RIGHT * 0.9)
            ct = ar(txt, 28, "BOLD", "#FFFFFF").move_to(c.get_center() + LEFT * 1.3)
            self.sfx("pop")
            self.play(GrowFromCenter(VGroup(c, cv, ceq, ct), rate_func=BOUNCE),
                      run_time=0.9)
            t += 0.9
        self.wait(max(d - 1.4 - t, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أفهم معنى النسبة المئوية: من مئة",
            "أحسب نسبة مئوية من عدد",
            "أحلّ مسائل التخفيض من السوق",
        ])
        self.s_def()
        self.s_meth()
        self.s_calc()
        self.s_prob()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
