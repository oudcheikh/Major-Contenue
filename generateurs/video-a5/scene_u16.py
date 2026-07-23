# -*- coding: utf-8 -*-
"""Vidéo U16 — مضاعفات الأعداد وقواسمها.  Rendu : venv/bin/manim -qh scene_u16.py VideoU16
Cœur de la vidéo : les مضاعفات SAUTENT sur le مستقيم العددي (bonds de 5 en 5),
la relation قاسم/مضاعف se lit dans les deux sens sur 210÷30=7, les قواعد قابلية
القسمة défilent en cartes, et le test 414 : 4+1+4=9 → ÷3 و÷9 دون قسمة!"""
import numpy as np
from manim import (VGroup, Line, Arc, Dot, Rectangle, RoundedRectangle,
                   SurroundingRectangle, CurvedArrow,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT, PI, DEGREES)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


class VideoU16(MajorScene):
    AUDIO = HERE / "audio_u16"
    UNIT_AR = "الوحدة 16"
    UNIT_COLOR = GREEN
    TITLE = "المضاعفات والقواسم"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 16"

    # ── 2. المضاعفات : أقفز على المستقيم ────────────────────────
    def s_mult(self):
        d = self.seg("mul1")
        head = titled("مضاعفات العدد: أضرب في 0، 1، 2، 3…", 30, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        row = VGroup(*[VGroup(num(f"5×{k}", 26, INK), num(str(5 * k), 38, GREEN)
                              ).arrange(DOWN, buff=0.2) for k in range(5)]
                     ).arrange(LEFT, buff=0.9).move_to([0, 0.8, 0])
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(x, scale=0.5, rate_func=BOUNCE) for x in row],
                              lag_ratio=0.2), run_time=1.8)
        self.wait(max(d - 2.7, 0.2))

        d = self.seg("mul2")
        # المستقيم العددي : bonds de droite à gauche (RTL)
        line = Line([5.6, -1.6, 0], [-5.6, -1.6, 0], color=INK, stroke_width=4)
        self.play(Create(line), run_time=0.8)
        xs = [4.8 - 2.4 * k for k in range(5)]
        ticks = VGroup()
        for k, x in enumerate(xs):
            t = Line([x, -1.45, 0], [x, -1.75, 0], color=INK, stroke_width=3)
            lb = num(str(5 * k), 28).move_to([x, -2.15, 0])
            ticks.add(VGroup(t, lb))
        self.play(LaggedStart(*[FadeIn(t) for t in ticks], lag_ratio=0.15), run_time=1.0)
        dot = Dot([xs[0], -1.6, 0], radius=0.12, color=ROSE)
        self.play(FadeIn(dot, scale=0.4), run_time=0.4)
        for k in range(4):
            hop = Arc(radius=1.2, start_angle=0, angle=PI, color=ROSE, stroke_width=4,
                      arc_center=[(xs[k] + xs[k + 1]) / 2, -1.6, 0])
            self.sfx("boing")
            self.play(Create(hop), dot.animate(rate_func=BOUNCE).move_to(
                [xs[k + 1], -1.6, 0]), run_time=0.75)
        lab = ar("أقفز 5 في كل مرة!", 28, "BOLD", ROSE).move_to([0, 0.0, 0])
        self.sfx("ding")
        self.play(FadeIn(lab, shift=UP * 0.3), run_time=0.8)
        self.wait(max(d - 6.0, 0.2))
        self.clear_all()

    # ── 3. القواسم : 210 ÷ 30 = 7 ───────────────────────────────
    def s_divis(self):
        d = self.seg("div1")
        head = titled("القواسم: قسمة تامة دون باق", 34, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 0.9, 0.2))

        d = self.seg("div2")
        calc = VGroup(num("210", 48), ar("÷", 34, "BOLD"), num("30", 48),
                      num("=", 42), num("7", 56, GREEN)).arrange(LEFT, buff=0.35)
        calc.move_to([0, 0.7, 0])
        self.sfx("pop")
        self.play(FadeIn(calc, shift=UP * 0.3), run_time=1.0)
        check = ar("تمامًا، دون باق!", 26, "BOLD", GREEN).next_to(calc, DOWN, buff=0.4)
        self.play(FadeIn(check, shift=UP * 0.2), run_time=0.8)
        r1 = VGroup(num("30", 34, BLUE), ar("قاسم لـ", 26, "BOLD", BLUE),
                    num("210", 34, BLUE)).arrange(LEFT, buff=0.3).move_to([2.9, -1.9, 0])
        r2 = VGroup(num("210", 34, ROSE), ar("مضاعف لـ", 26, "BOLD", ROSE),
                    num("30", 34, ROSE)).arrange(LEFT, buff=0.3).move_to([-2.9, -1.9, 0])
        b1 = SurroundingRectangle(r1, color=BLUE, corner_radius=0.15, buff=0.2)
        b2 = SurroundingRectangle(r2, color=ROSE, corner_radius=0.15, buff=0.2)
        self.sfx("pop")
        self.play(FadeIn(r1), Create(b1), run_time=0.9)
        self.sfx("pop")
        self.play(FadeIn(r2), Create(b2), run_time=0.9)
        self.wait(max(d - 3.6, 0.2))
        self.clear_all()

    # ── 4. قواعد قابلية القسمة ──────────────────────────────────
    def s_regles(self):
        d = self.seg("reg1")
        head = titled("القواعد الذهبية لقابلية القسمة", 32, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        c1 = RoundedRectangle(corner_radius=0.22, width=11.4, height=1.02, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to([0, 1.35, 0])
        c1t = ar("÷ 2 : العدد زوجي، ينتهي بـ 0، 2، 4، 6، 8", 25, "BOLD",
                 "#FFFFFF").move_to(c1)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("reg2")
        c2 = RoundedRectangle(corner_radius=0.22, width=11.4, height=1.02, fill_color=BLUE,
                              fill_opacity=0.92, stroke_color=INK).move_to([0, 0.2, 0])
        c2t = ar("÷ 5 : ينتهي بـ 0 أو 5 · ÷ 10 : ينتهي بـ 0", 25, "BOLD",
                 "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 0.9, 0.2))

        d = self.seg("reg3")
        c3 = RoundedRectangle(corner_radius=0.22, width=11.4, height=1.02, fill_color=ROSE,
                              fill_opacity=0.92, stroke_color=INK).move_to([0, -0.95, 0])
        c3t = ar("÷ 3 أو ÷ 9 : مجموع الأرقام يقبل القسمة على 3 أو 9", 25, "BOLD",
                 "#FFFFFF").move_to(c3)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c3, c3t), rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 0.9, 0.2))

        d = self.seg("reg4")
        c4 = RoundedRectangle(corner_radius=0.22, width=11.4, height=1.02, fill_color=LILA,
                              fill_opacity=0.92, stroke_color=INK).move_to([0, -2.1, 0])
        c4t = ar("÷ 6 : يقبل القسمة على 2 و3 معًا", 25, "BOLD", "#FFFFFF").move_to(c4)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(c4, c4t), rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 0.9, 0.2))
        self.clear_all()

    # ── 5. المثال المحوري : 414 ─────────────────────────────────
    def s_ex(self):
        d = self.seg("ex1")
        head = titled("لنجرّب على العدد 414", 38, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        n = num("414", 76).move_to([0, 0.9, 0])
        self.sfx("pop")
        self.play(FadeIn(n, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        # les chiffres tombent et s'additionnent
        digits = [n[0].copy(), n[1].copy(), n[2].copy()]
        sum_row = VGroup(num("4", 44, ROSE), num("+", 36, INK), num("1", 44, ROSE),
                         num("+", 36, INK), num("4", 44, ROSE),
                         num("=", 40), num("9", 54, GOLD)).arrange(LEFT, buff=0.3)
        sum_row.move_to([0, -0.7, 0])
        self.sfx("whoosh")
        self.play(ReplacementTransform(digits[0], sum_row[0]),
                  ReplacementTransform(digits[1], sum_row[2]),
                  ReplacementTransform(digits[2], sum_row[4]),
                  FadeIn(sum_row[1]), FadeIn(sum_row[3]), run_time=1.3)
        self.sfx("ding")
        self.play(FadeIn(sum_row[5]), GrowFromCenter(sum_row[6], rate_func=BOUNCE),
                  run_time=0.9)
        self.play(Flash(sum_row[6], color=GOLD, flash_radius=1.0), run_time=0.7)
        self.wait(max(d - 4.1, 0.2))

        d = self.seg("ex2")
        v1 = VGroup(ar("يقبل ÷ 3", 28, "BOLD", "#FFFFFF"))
        b1 = RoundedRectangle(corner_radius=0.22, width=4.4, height=1.05, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to([2.5, -2.2, 0])
        v1[0].move_to(b1)
        v2 = VGroup(ar("ويقبل ÷ 9", 28, "BOLD", "#FFFFFF"))
        b2 = RoundedRectangle(corner_radius=0.22, width=4.4, height=1.05, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to([-2.5, -2.2, 0])
        v2[0].move_to(b2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(b1, v1), rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(b2, v2), rate_func=BOUNCE), run_time=0.9)
        note = ar("دون أي عملية قسمة!", 30, "BOLD", GOLD).move_to([0, 2.0, 0])
        self.sfx("ding")
        self.play(FadeIn(note, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 2.7, 0.2))
        self.clear_all()

    # ── 6. مسألة الحليب : 270 ÷ 90 ──────────────────────────────
    def s_app(self):
        d = self.seg("app1")
        head = titled("مسألة: قوارير الحليب", 36, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # 3 قوارير
        bottles = VGroup()
        for i in range(3):
            body = RoundedRectangle(corner_radius=0.18, width=0.95, height=1.7,
                                    fill_color="#FFFFFF", fill_opacity=0.95,
                                    stroke_color=BLUE, stroke_width=3)
            neck = Rectangle(width=0.4, height=0.35, fill_color=BLUE, fill_opacity=0.9,
                             stroke_color=INK, stroke_width=2).next_to(body, UP, buff=0)
            cap = num("90", 24, BLUE).move_to(body)
            bottles.add(VGroup(body, neck, cap))
        bottles.arrange(LEFT, buff=0.6).move_to([2.9, -0.6, 0])
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(b, scale=0.5, rate_func=BOUNCE) for b in bottles],
                              lag_ratio=0.25), run_time=1.4)
        q = VGroup(ar("عندنا", 28, "BOLD"), num("270", 38, GOLD),
                   ar("سنتيلترًا — كم قارورة نملأ؟", 28, "BOLD")).arrange(LEFT, buff=0.3)
        q.move_to([-1.2, 1.3, 0])
        self.play(FadeIn(q, shift=DOWN * 0.3), run_time=0.9)
        self.wait(max(d - 2.3, 0.2))

        d = self.seg("app2")
        calc = VGroup(num("270", 42), ar("÷", 30, "BOLD"), num("90", 42),
                      num("=", 38), num("3", 52, GREEN),
                      ar("قوارير", 28, "BOLD", GREEN)).arrange(LEFT, buff=0.3)
        calc.move_to([-2.9, -0.9, 0])
        box = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        self.play(Flash(calc[4], color=GREEN, flash_radius=1.2), run_time=0.8)
        self.play(LaggedStart(*[Indicate(b, color=GREEN, scale_factor=1.15)
                                for b in bottles], lag_ratio=0.25), run_time=1.3)
        self.wait(max(d - 3.2, 0.2))
        self.clear_all()

    # ── 7. انتبه : مضاعف ≠ قاسم ─────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! لا تخلط بينهما", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=7.0, height=1.1, fill_color=ROSE,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.1 + UP * 0.5)
        c1t = ar("المضاعف أكبر من العدد أو يساويه", 25, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=7.0, height=1.1, fill_color=BLUE,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.1 + DOWN * 0.9)
        c2t = ar("القاسم أصغر منه أو يساويه", 25, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 8. السر : اجمع الأرقام فقط ──────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: اجمع الأرقام فقط!", 34, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.8)
        c = RoundedRectangle(corner_radius=0.25, width=10.2, height=1.5, fill_color=LILA,
                             fill_opacity=0.92, stroke_color=INK,
                             stroke_width=2).move_to([0, 0.2, 0])
        ct = ar("للفحص على 3 أو 9: لا قسمة أبدًا، المجموع يخبرك!", 27, "BOLD",
                "#FFFFFF").move_to(c)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(c, ct), rate_func=BOUNCE), run_time=1.1)
        self.play(Flash(VGroup(c, ct), color=LILA, flash_radius=3.0), run_time=0.9)
        self.wait(max(d - 3.8, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أميّز مضاعفات العدد وقواسمه",
            "أطبّق قواعد قابلية القسمة",
            "أستعملها في مسائل من حياتي",
        ])
        self.s_mult()
        self.s_divis()
        self.s_regles()
        self.s_ex()
        self.s_app()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
