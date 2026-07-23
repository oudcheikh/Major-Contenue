# -*- coding: utf-8 -*-
"""Vidéo U31 — المجسمات والحجوم والسعات.  Rendu : venv/bin/manim -qh scene_u31.py VideoU31
Cœur de la vidéo : le مكعب se DESSINE en perspective (6 أوجه، 12 حرفًا، 8 رؤوس
comptés en direct), le حجم 2×2×2=8 se calcule, la علاقة ذهبية 1 L = 1 dm³
s'encadre en or, et le خزان 3×2×1 se remplit : 6 م³ = 6000 لتر !"""
import numpy as np
from manim import (VGroup, Line, DashedLine, Polygon, Circle, Ellipse, Rectangle,
                   RoundedRectangle, SurroundingRectangle, Dot,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


def cube(s=1.8, color=BLUE, dx=0.55, dy=0.45):
    """مكعب en perspective cavalière : face avant + face arrière + arêtes."""
    front = Polygon([-s / 2, -s / 2, 0], [s / 2, -s / 2, 0],
                    [s / 2, s / 2, 0], [-s / 2, s / 2, 0],
                    fill_color=color, fill_opacity=0.35, stroke_color=INK, stroke_width=3.5)
    back = front.copy().set_fill(opacity=0.15).shift(RIGHT * dx + UP * dy)
    edges = VGroup(*[Line(front.get_vertices()[i], back.get_vertices()[i],
                          color=INK, stroke_width=3) for i in range(4)])
    return VGroup(back, edges, front)


def pave(w=2.6, h=1.4, color=GREEN, dx=0.55, dy=0.45):
    """متوازي المستطيلات en perspective."""
    front = Polygon([-w / 2, -h / 2, 0], [w / 2, -h / 2, 0],
                    [w / 2, h / 2, 0], [-w / 2, h / 2, 0],
                    fill_color=color, fill_opacity=0.35, stroke_color=INK, stroke_width=3.5)
    back = front.copy().set_fill(opacity=0.15).shift(RIGHT * dx + UP * dy)
    edges = VGroup(*[Line(front.get_vertices()[i], back.get_vertices()[i],
                          color=INK, stroke_width=3) for i in range(4)])
    return VGroup(back, edges, front)


class VideoU31(MajorScene):
    AUDIO = HERE / "audio_u31"
    UNIT_AR = "الوحدة 31"
    UNIT_COLOR = BLUE
    TITLE = "المجسمات والحجوم والسعات"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 31"

    # ── 2. المجسمات ─────────────────────────────────────────────
    def s_solides(self):
        d = self.seg("sol1")
        head = titled("المكعب: 6 أوجه · 12 حرفًا · 8 رؤوس", 30, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        cb = cube(2.2, BLUE).move_to([2.9, -0.4, 0])
        self.sfx("whoosh")
        self.play(Create(cb), run_time=1.6)
        facts = [("6 أوجه مربعة", GREEN), ("12 حرفًا", ROSE), ("8 رؤوس", GOLD)]
        t = 0
        for i, (txt, col) in enumerate(facts):
            lab = ar(txt, 28, "BOLD", col).move_to([-2.9, 0.6 - 1.0 * i, 0])
            self.sfx("pop")
            self.play(FadeIn(lab, shift=LEFT * 0.4, rate_func=BOUNCE), run_time=0.8)
            t += 0.8
        # les رؤوس clignotent
        dots = VGroup(*[Dot(v, radius=0.09, color=GOLD)
                        for v in cb[2].get_vertices()] +
                      [Dot(v, radius=0.09, color=GOLD) for v in cb[0].get_vertices()])
        self.play(LaggedStart(*[FadeIn(dt, scale=0.3) for dt in dots],
                              lag_ratio=0.1), run_time=1.0)
        self.wait(max(d - 2.5 - t - 1.0, 0.2))
        self.clear_all()

        d = self.seg("sol2")
        head2 = titled("متوازي المستطيلات: 3 أبعاد", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head2, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        pv = pave(3.2, 1.7, GREEN).move_to([1.6, -0.5, 0])
        self.sfx("whoosh")
        self.play(Create(pv), run_time=1.4)
        dims = [(ar("الطول", 24, "BOLD", ROSE), pv[2].get_bottom() + DOWN * 0.4),
                (ar("العرض", 24, "BOLD", GOLD),
                 pv[2].get_corner(DOWN + RIGHT) + np.array([0.65, 0.2, 0])),
                (ar("الارتفاع", 24, "BOLD", BLUE), pv[2].get_left() + LEFT * 0.75)]
        for lab, pos in dims:
            lab.move_to(pos)
            self.sfx("pop")
            self.play(FadeIn(lab, scale=0.5, rate_func=BOUNCE), run_time=0.6)
        self.wait(max(d - 4.1, 0.2))
        self.clear_all()

        d = self.seg("sol3")
        head3 = titled("الأسطوانة والكرة", 36, LILA)
        self.sfx("pop")
        self.play(FadeIn(head3, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # أسطوانة : rectangle + deux ellipses
        cyl = VGroup(
            Rectangle(width=1.9, height=2.3, fill_color=LILA, fill_opacity=0.3,
                      stroke_width=0),
            Line([-0.95, -1.15, 0], [-0.95, 1.15, 0], color=INK, stroke_width=3.5),
            Line([0.95, -1.15, 0], [0.95, 1.15, 0], color=INK, stroke_width=3.5),
            Ellipse(width=1.9, height=0.55, fill_color=LILA, fill_opacity=0.5,
                    stroke_color=INK, stroke_width=3.5).shift(UP * 1.15),
            Ellipse(width=1.9, height=0.55, fill_color=LILA, fill_opacity=0.3,
                    stroke_color=INK, stroke_width=3.5).shift(DOWN * 1.15),
        ).move_to([2.4, -0.7, 0])
        cyl_l = ar("قاعدتان قرصيتان", 24, "BOLD", LILA).move_to([2.4, -2.6, 0])
        self.sfx("pop")
        self.play(Create(cyl), FadeIn(cyl_l, shift=UP * 0.2), run_time=1.4)
        sph = VGroup(
            Circle(radius=1.15, fill_color=ROSE, fill_opacity=0.3,
                   stroke_color=INK, stroke_width=3.5),
            Ellipse(width=2.3, height=0.5, stroke_color=INK, stroke_width=2.5
                    ).set_opacity(0.5),
            Dot(ORIGIN_ := [0, 0, 0], radius=0.08, color=ROSE),
        ).move_to([-2.6, -0.7, 0])
        sph_l = ar("الكرة: كل النقاط تبعد بنفس المسافة", 22, "BOLD", ROSE
                   ).move_to([-2.6, -2.6, 0])
        self.sfx("pop")
        self.play(Create(sph), FadeIn(sph_l, shift=UP * 0.2), run_time=1.4)
        self.wait(max(d - 3.7, 0.2))
        self.clear_all()

    # ── 3. الحجوم ───────────────────────────────────────────────
    def s_volumes(self):
        d = self.seg("vol1")
        head = titled("حجم المكعب: الحرف × الحرف × الحرف", 30, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        cb = cube(1.9, BLUE).move_to([3.0, -0.5, 0])
        dim = num("2 cm", 26, GOLD).next_to(cb, DOWN, buff=0.35)
        self.sfx("whoosh")
        self.play(Create(cb), FadeIn(dim), run_time=1.3)
        calc = VGroup(num("2", 42), num("×", 34, GOLD), num("2", 42),
                      num("×", 34, GOLD), num("2", 42),
                      num("=", 38), num("8", 52, GREEN)).arrange(LEFT, buff=0.28)
        unit = ar("سنتيمترات مكعبة", 26, "BOLD", GREEN)
        row = VGroup(calc, unit).arrange(LEFT, buff=0.4).move_to([-1.9, -0.5, 0])
        self.sfx("ding")
        self.play(FadeIn(row, shift=UP * 0.3), run_time=1.1)
        self.play(Flash(calc[6], color=GREEN, flash_radius=1.1), run_time=0.7)
        self.wait(max(d - 4.0, 0.2))
        self.clear_all()

        d = self.seg("vol2")
        box = RoundedRectangle(corner_radius=0.25, width=11.0, height=1.35,
                               fill_color=GREEN, fill_opacity=0.92,
                               stroke_color=INK, stroke_width=2).move_to([0, 0.7, 0])
        boxt = ar("حجم متوازي المستطيلات = الطول × العرض × الارتفاع", 27, "BOLD",
                  "#FFFFFF").move_to(box)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(box, boxt), rate_func=BOUNCE), run_time=1.1)
        self.wait(max(d - 1.1, 0.2))

        d = self.seg("unit1")
        r1 = VGroup(ar("في جدول الحجوم:", 28, "BOLD", LILA),
                    ar("3 خانات لكل وحدة!", 28, "BOLD", GOLD)).arrange(LEFT, buff=0.4)
        r1.move_to([0, -0.7, 0])
        self.sfx("pop")
        self.play(FadeIn(r1, shift=UP * 0.3), run_time=0.9)
        r2 = VGroup(num("1", 42), ar("م³", 30, "BOLD"), num("=", 36),
                    num("1000", 46, BLUE), ar("دسم³", 30, "BOLD", BLUE)
                    ).arrange(LEFT, buff=0.3).move_to([0, -1.9, 0])
        b2 = SurroundingRectangle(r2, color=BLUE, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(r2, shift=UP * 0.3), Create(b2), run_time=1.0)
        self.wait(max(d - 1.9, 0.2))
        self.clear_all()

    # ── 4. السعات والعلاقة الذهبية ──────────────────────────────
    def s_capacites(self):
        d = self.seg("cap1")
        head = titled("السعات: باللتر نقيس السوائل", 34, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        bottle = VGroup(
            RoundedRectangle(corner_radius=0.22, width=1.3, height=2.3,
                             fill_color=BLUE, fill_opacity=0.45,
                             stroke_color=INK, stroke_width=3),
            Rectangle(width=0.5, height=0.45, fill_color=BLUE, fill_opacity=0.9,
                      stroke_color=INK, stroke_width=2.5).shift(UP * 1.35),
            num("1 L", 30, BLUE))
        bottle[2].move_to(bottle[0])
        bottle.move_to([3.3, -0.6, 0])
        self.sfx("pop")
        self.play(FadeIn(bottle, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        eq = VGroup(num("1", 40), ar("لتر", 28, "BOLD"), num("=", 34),
                    num("100", 42, GREEN), ar("سل", 28, "BOLD", GREEN),
                    num("=", 34), num("1000", 42, ROSE), ar("مل", 28, "BOLD", ROSE)
                    ).arrange(LEFT, buff=0.28).move_to([-1.4, -0.6, 0])
        self.sfx("ding")
        self.play(FadeIn(eq, shift=UP * 0.3), run_time=1.0)
        self.wait(max(d - 1.9, 0.2))
        self.clear_all()

        d = self.seg("gold1")
        head2 = titled("العلاقة الذهبية — احفظها!", 36, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head2, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        g1 = VGroup(num("1", 48), ar("لتر", 34, "BOLD"), num("=", 42),
                    num("1", 48, GOLD), ar("دسم³", 34, "BOLD", GOLD)
                    ).arrange(LEFT, buff=0.3).move_to([0, 0.6, 0])
        b1 = SurroundingRectangle(g1, color=GOLD, corner_radius=0.18, buff=0.3,
                                  stroke_width=5)
        self.sfx("ding")
        self.play(FadeIn(g1, scale=0.6, rate_func=BOUNCE), Create(b1), run_time=1.2)
        self.play(Flash(g1, color=GOLD, flash_radius=2.4), run_time=0.9)
        g2 = VGroup(num("1", 42), ar("م³", 30, "BOLD"), num("=", 38),
                    num("1000", 46, BLUE), ar("لتر", 30, "BOLD", BLUE)
                    ).arrange(LEFT, buff=0.3).move_to([0, -1.3, 0])
        self.sfx("pop")
        self.play(FadeIn(g2, shift=UP * 0.3), run_time=1.0)
        self.wait(max(d - 4.0, 0.2))
        self.clear_all()

    # ── 5. مثال الكراس : الخزان ─────────────────────────────────
    def s_ex(self):
        d = self.seg("ex1")
        head = titled("خزان الماء: 3 م × 2 م × 1 م", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        pv = pave(3.4, 1.5, BLUE).move_to([2.6, -0.5, 0])
        d1 = num("3 m", 24, ROSE).next_to(pv[2], DOWN, buff=0.3)
        d2 = num("1 m", 24, BLUE).next_to(pv[2], LEFT, buff=0.3)
        d3 = num("2 m", 24, GOLD).move_to(pv[2].get_corner(DOWN + RIGHT)
                                          + np.array([0.75, 0.25, 0]))
        self.sfx("whoosh")
        self.play(Create(pv), run_time=1.2)
        self.play(FadeIn(d1), FadeIn(d2), FadeIn(d3), run_time=0.8)
        calc = VGroup(num("3", 40), num("×", 32, GOLD), num("2", 40),
                      num("×", 32, GOLD), num("1", 40), num("=", 36),
                      num("6", 50, GREEN), ar("م³", 30, "BOLD", GREEN)
                      ).arrange(LEFT, buff=0.26).move_to([-2.8, -0.5, 0])
        box = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        self.wait(max(d - 4.0, 0.2))

        d = self.seg("ex2")
        conv = VGroup(num("6", 42), ar("م³", 30, "BOLD"), num("=", 36),
                      num("6000", 48, BLUE), ar("لتر من الماء!", 30, "BOLD", BLUE)
                      ).arrange(LEFT, buff=0.28).move_to([0, -2.4, 0])
        b2 = SurroundingRectangle(conv, color=BLUE, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(conv, shift=UP * 0.3), Create(b2), run_time=1.1)
        # le خزان se remplit
        water = Rectangle(width=3.35, height=1.45, fill_color=BLUE, fill_opacity=0.55,
                          stroke_width=0).move_to(pv[2].get_center())
        water.stretch_to_fit_height(0.05).align_to(pv[2], DOWN).shift(UP * 0.03)
        self.add(water)
        self.sfx("whoosh")
        self.play(water.animate.stretch_to_fit_height(1.42).move_to(
            pv[2].get_center()), run_time=1.6)
        self.play(Flash(conv[3], color=BLUE, flash_radius=1.5), run_time=0.8)
        self.wait(max(d - 3.5, 0.2))
        self.clear_all()

    # ── 6. انتبه : ضرب لا جمع ───────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! الحجم ضربٌ لا جمع", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=6.6, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.3 + UP * 0.5)
        c1t = VGroup(num("3 × 2 × 1 = 6", 30, "#FFFFFF"),
                     ar("صحيح", 24, "BOLD", "#FFFFFF")).arrange(LEFT, buff=0.5).move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=6.6, height=1.1, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.3 + DOWN * 0.9)
        c2t = VGroup(num("3 + 2 + 1", 30, "#FFFFFF"),
                     ar("خطأ!", 24, "BOLD", "#FFFFFF")).arrange(LEFT, buff=0.5).move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 7. السر : رقمان للمساحات، ثلاثة للحجوم ──────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: عدد الأرقام في الجدول", 32, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.8)
        c1 = RoundedRectangle(corner_radius=0.22, width=7.4, height=1.1, fill_color=BLUE,
                              fill_opacity=0.92, stroke_color=INK).move_to(UP * 0.5)
        c1t = ar("المساحات (م²): رقمان لكل عمود", 27, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=7.4, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(DOWN * 0.9)
        c2t = ar("الحجوم (م³): ثلاثة أرقام لكل عمود", 27, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=1.0)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 3.8, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أتعرّف المكعب ومتوازي المستطيلات",
            "أحسب الحجوم: الطول × العرض × الارتفاع",
            "أحفظ العلاقة الذهبية: 1 لتر = 1 دسم³",
        ])
        self.s_solides()
        self.s_volumes()
        self.s_capacites()
        self.s_ex()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
