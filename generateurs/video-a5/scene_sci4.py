# -*- coding: utf-8 -*-
"""Vidéo Sciences 4 — التلوث.  Rendu : ./build_science.sh 4
Cœur : تعريف التلوث · الأنواع الثلاثة (الهواء/الماء/التربة) مرسومة · الحل (نقلّل/نفرز/نعيد التدوير)
+ رمز إعادة التدوير · مثال محلول 100 كيس، تقليل 50٪ = 50 · انتبه · سرّ من نواكشوط."""
import numpy as np
from manim import (VGroup, Rectangle, RoundedRectangle, Circle, Ellipse, Polygon,
                   Line, CurvedArrow, SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter, Flash, Indicate,
                   Wiggle, LaggedStart, UP, DOWN, LEFT, RIGHT, DEGREES)

from video_common import (MajorScene, ar, num, titled, chip,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)

GREY = "#9AA0A6"
SMOKE = "#B7BCC2"
DARK = "#5C6067"
OIL = "#222428"
SOIL = "#8B5A2B"


def factory(scale=1.0):
    """مصنع : جسم رمادي + مدخنتان + دخان."""
    g = VGroup()
    body = Rectangle(width=2.0, height=1.15, fill_color=GREY, fill_opacity=1,
                     stroke_color=INK, stroke_width=2.5)
    roof = Polygon([-1.0, 0.575, 0], [1.0, 0.575, 0], [1.0, 0.95, 0], [0.5, 0.575, 0],
                   [0.5, 0.95, 0], [0.0, 0.575, 0], [0.0, 0.95, 0], [-0.5, 0.575, 0],
                   fill_color=DARK, fill_opacity=1, stroke_color=INK, stroke_width=2)
    ch1 = Rectangle(width=0.28, height=0.7, fill_color=DARK, fill_opacity=1,
                    stroke_color=INK, stroke_width=2).move_to([0.55, 1.1, 0])
    win = VGroup(*[Rectangle(width=0.32, height=0.32, fill_color=YELL, fill_opacity=0.9,
                             stroke_color=INK, stroke_width=1.5).move_to([x, -0.15, 0])
                   for x in (-0.55, 0.0, 0.55)])
    g.add(body, roof, ch1, win)
    return g.scale(scale)


def smoke_puffs(top):
    puffs = VGroup()
    pts = [(0.0, 0.0, 0.30), (0.25, 0.45, 0.34), (0.62, 0.78, 0.40), (1.05, 1.05, 0.46)]
    for dx, dy, r in pts:
        puffs.add(Circle(radius=r, fill_color=SMOKE, fill_opacity=0.85, stroke_width=0)
                  .move_to(top + RIGHT * dx + UP * dy))
    return puffs


def car(scale=1.0):
    g = VGroup()
    body = RoundedRectangle(corner_radius=0.15, width=1.9, height=0.55,
                            fill_color=BLUE, fill_opacity=0.9, stroke_color=INK, stroke_width=2.5)
    cabin = RoundedRectangle(corner_radius=0.12, width=1.0, height=0.45,
                             fill_color=BLUE, fill_opacity=0.6, stroke_color=INK,
                             stroke_width=2).move_to([0.05, 0.42, 0])
    w1 = Circle(radius=0.22, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([-0.55, -0.35, 0])
    w2 = Circle(radius=0.22, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([0.55, -0.35, 0])
    g.add(body, cabin, w1, w2)
    return g.scale(scale)


def fish(col=YELL, scale=1.0):
    g = VGroup()
    body = Ellipse(width=1.0, height=0.55, fill_color=col, fill_opacity=0.95,
                   stroke_color=INK, stroke_width=2.5)
    tail = Polygon([0.45, 0, 0], [0.9, 0.32, 0], [0.9, -0.32, 0],
                   fill_color=col, fill_opacity=0.95, stroke_color=INK, stroke_width=2.5)
    eye = Circle(radius=0.07, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([-0.32, 0.1, 0])
    g.add(tail, body, eye)
    return g.scale(scale)


def bag(col=GREY, scale=1.0):
    """كيس بلاستيكي : جسم + مقبضان."""
    g = VGroup()
    body = RoundedRectangle(corner_radius=0.08, width=0.62, height=0.7,
                            fill_color=col, fill_opacity=0.9, stroke_color=INK, stroke_width=2)
    h1 = Line([-0.18, 0.35, 0], [-0.12, 0.6, 0], color=INK, stroke_width=2.5)
    h2 = Line([0.18, 0.35, 0], [0.12, 0.6, 0], color=INK, stroke_width=2.5)
    g.add(body, h1, h2)
    return g.scale(scale)


def recycle(r=0.85, col=GREEN):
    """رمز إعادة التدوير : ثلاثة أسهم منحنية تلاحق بعضها."""
    g = VGroup()
    angs = [90, 210, 330]
    pts = [np.array([r * np.cos(a * DEGREES), r * np.sin(a * DEGREES), 0]) for a in angs]
    for i in range(3):
        a = CurvedArrow(pts[i], pts[(i + 1) % 3], angle=-1.1, color=col,
                        stroke_width=9, tip_length=0.28)
        g.add(a)
    return g


class VideoSci4(MajorScene):
    AUDIO = HERE / "audio_sci4"
    UNIT_AR = "علوم · درس 4"
    UNIT_COLOR = BLUE
    TITLE = "التلوث"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين درس التلوث"

    # ── 2. التعريف ──────────────────────────────────────────────
    def s_def(self):
        d = self.seg("def1")
        head = titled("ما هو التلوث؟", 34, BLUE)
        box = RoundedRectangle(corner_radius=0.28, width=11.6, height=2.3,
                               fill_color=BLUE, fill_opacity=0.12,
                               stroke_color=BLUE, stroke_width=3).move_to(DOWN * 0.2)
        t1 = ar("تدهور البيئة بسبب مواد ضارة", 32, "BOLD", INK).move_to(box.get_center() + UP * 0.5)
        t2 = ar("من أنشطة الإنسان: المصانع والسيارات والنفايات", 28, "BOLD", REDA)
        if t2.width > 10.8:
            t2.scale_to_fit_width(10.8)
        t2.move_to(box.get_center() + DOWN * 0.45)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.sfx("ding")
        self.play(GrowFromCenter(box, rate_func=BOUNCE), Write(t1), run_time=1.3)
        self.play(FadeIn(t2, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - 3.1, 0.2))
        self.clear_all()

    # ── 3. تلوث الهواء ──────────────────────────────────────────
    def s_air(self):
        d = self.seg("air1")
        head = titled("تلوث الهواء", 36, GREY)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        fac = factory(1.0).move_to([2.9, 0.35, 0])
        smk = smoke_puffs(fac.get_top() + RIGHT * 0.55 + DOWN * 0.05)
        c = car(1.0).move_to([2.9, -1.9, 0])
        self.sfx("whoosh")
        self.play(Create(fac), run_time=1.0)
        self.sfx("pop")
        self.play(LaggedStart(*[GrowFromCenter(p) for p in smk], lag_ratio=0.25), run_time=1.1)
        self.sfx("pop")
        self.play(FadeIn(c, shift=LEFT * 0.4, rate_func=BOUNCE), run_time=0.8)
        lab = ar("← أمراض تنفسية", 32, "BOLD", REDA).move_to([-3.2, -0.2, 0])
        self.sfx("ding")
        self.play(Write(lab), run_time=1.0)
        self.play(Indicate(smk, color=DARK), run_time=0.9)
        self.wait(max(d - 5.7, 0.2))
        self.clear_all()

    # ── 4. تلوث الماء ───────────────────────────────────────────
    def s_water(self):
        d = self.seg("water1")
        head = titled("تلوث الماء", 36, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        water = Rectangle(width=6.0, height=2.6, fill_color=BLUE, fill_opacity=0.45,
                          stroke_color=INK, stroke_width=2.5).move_to([2.5, -0.55, 0])
        self.sfx("whoosh")
        self.play(Create(water), run_time=1.0)
        f = fish(YELL, 1.0).move_to([1.9, -0.9, 0])
        self.sfx("pop")
        self.play(FadeIn(f, shift=LEFT * 0.4, rate_func=BOUNCE), run_time=0.8)
        oil = VGroup(*[Circle(radius=r, fill_color=OIL, fill_opacity=0.9, stroke_width=0)
                       .move_to([x, water.get_top()[1] - 0.18, 0])
                       for x, r in [(0.9, 0.22), (2.2, 0.30), (3.5, 0.24), (4.3, 0.18)]])
        self.sfx("pop")
        self.play(LaggedStart(*[GrowFromCenter(o) for o in oil], lag_ratio=0.2), run_time=1.1)
        lab = ar("اختفاء الأسماك →", 32, "BOLD", REDA).move_to([-3.1, 0.9, 0])
        self.sfx("ding")
        self.play(Write(lab), run_time=1.0)
        self.play(Wiggle(f), run_time=0.9)
        self.wait(max(d - 5.7, 0.2))
        self.clear_all()

    # ── 5. تلوث التربة ──────────────────────────────────────────
    def s_soil(self):
        d = self.seg("soil1")
        head = titled("تلوث التربة", 36, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        ground = Rectangle(width=9.6, height=1.5, fill_color=SOIL, fill_opacity=0.9,
                           stroke_color=INK, stroke_width=2.5).move_to([0.4, -1.9, 0])
        self.sfx("whoosh")
        self.play(Create(ground), run_time=1.0)
        bags = VGroup()
        for i, x in enumerate([-3.2, -1.6, 0.0, 1.6, 3.3]):
            b = bag([GREY, LILA, ROSE, GREEN, GOLD][i], 0.95).move_to([x, -1.35, 0])
            bags.add(b)
        t = 0
        for b in bags:
            self.sfx("pop")
            self.play(FadeIn(b, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.5)
            t += 0.5
        lab = ar("الأكياس تبقى سنوات في الأرض", 30, "BOLD", REDA).move_to([0.2, 0.9, 0])
        if lab.width > 11.0:
            lab.scale_to_fit_width(11.0)
        self.sfx("ding")
        self.play(Write(lab), run_time=1.1)
        self.wait(max(d - t - 2.1, 0.2))
        self.clear_all()

    # ── 6. الحل ─────────────────────────────────────────────────
    def s_sol(self):
        d = self.seg("sol1")
        head = titled("كيف نكافح التلوث؟", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        steps = [("نقلّل", YELL), ("نفرز", BLUE), ("نعيد التدوير", GREEN)]
        pills = VGroup()
        for i, (lab, col) in enumerate(steps):
            p = RoundedRectangle(corner_radius=0.4, width=3.5, height=1.4,
                                 fill_color=col, fill_opacity=0.92,
                                 stroke_color=INK, stroke_width=2.5)
            pt = ar(lab, 30, "BOLD", "#FFFFFF")
            if pt.width > 3.0:
                pt.scale_to_fit_width(3.0)
            pt.move_to(p)
            pills.add(VGroup(p, pt).move_to([3.9 - i * 3.9, 1.1, 0]))
        for p in pills:
            self.sfx("ding")
            self.play(GrowFromCenter(p, rate_func=BOUNCE), run_time=0.7)
        rec = recycle(0.9, GREEN).move_to([0, -1.5, 0])
        self.sfx("whoosh")
        self.play(Create(rec), run_time=1.3)
        self.play(Indicate(rec, color=GREEN, scale_factor=1.15), run_time=0.9)
        self.wait(max(d - 5.2, 0.2))
        self.clear_all()

    # ── 7. مثال محلول ───────────────────────────────────────────
    def s_example(self):
        d = self.seg("ex1")
        head = titled("مثال محلول: أكياس المدرسة", 32, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        b = bag(GREY, 1.6).move_to([-4.0, 1.05, 0])
        b_val = VGroup(num("100", 44, INK), ar("كيس", 26, "BOLD", INK)
                       ).arrange(LEFT, buff=0.25).next_to(b, DOWN, buff=0.35)
        self.sfx("pop")
        self.play(FadeIn(b, scale=0.5, rate_func=BOUNCE), FadeIn(b_val), run_time=0.9)
        arrow = ar("تقليل ←", 30, "BOLD", GREEN).move_to([-0.5, 1.05, 0])
        red = VGroup(num("50", 60, REDA), num("%", 44, REDA)).arrange(LEFT, buff=0.1).move_to([2.9, 1.05, 0])
        redbox = SurroundingRectangle(red, color=REDA, corner_radius=0.15, buff=0.3)
        self.sfx("ding")
        self.play(Write(arrow), run_time=0.8)
        self.play(FadeIn(red, scale=0.6, rate_func=BOUNCE), Create(redbox), run_time=1.0)
        self.wait(max(d - 3.6, 0.2))

        d = self.seg("ex2")
        calc = VGroup(num("100", 42), num("×", 34, GOLD), num("50", 42),
                      num("÷", 34, GOLD), num("100", 42), num("=", 38),
                      num("50", 54, GREEN)).arrange(LEFT, buff=0.28)
        unit = ar("كيسًا", 30, "BOLD", GREEN)
        row = VGroup(calc, unit).arrange(LEFT, buff=0.4).move_to([0, -1.9, 0])
        box = SurroundingRectangle(row, color=GREEN, corner_radius=0.15, buff=0.25)
        self.sfx("ding")
        self.play(FadeIn(row, shift=UP * 0.3), Create(box), run_time=1.1)
        self.sfx("tada")
        self.play(Flash(calc[6], color=GREEN, flash_radius=1.2), run_time=0.9)
        self.wait(max(d - 2.0, 0.2))
        self.clear_all()

    # ── 8. انتبه ────────────────────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه!", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=8.4, height=1.2, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 1.7 + UP * 0.6)
        c1t = ar("رمي النفايات في أيّ مكان", 28, "BOLD", "#FFFFFF")
        if c1t.width > 7.8:
            c1t.scale_to_fit_width(7.8)
        c1t.move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=8.4, height=1.2, fill_color=INK,
                              fill_opacity=0.9, stroke_color=INK).move_to(RIGHT * 1.7 + DOWN * 0.9)
        c2t = ar("يلوّث الماء والتربة معًا", 28, "BOLD", "#FFFFFF")
        if c2t.width > 7.8:
            c2t.scale_to_fit_width(7.8)
        c2t.move_to(c2)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 9. سرّ من محيطنا ────────────────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ من محيطنا", 34, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        box = RoundedRectangle(corner_radius=0.3, width=10.6, height=1.5, fill_color=LILA,
                               fill_opacity=0.18, stroke_color=LILA, stroke_width=3).move_to(UP * 1.1)
        t = ar("حولك أمثلة كثيرة: نفايات الأسواق في نواكشوط", 30, "BOLD", INK)
        if t.width > 10.0:
            t.scale_to_fit_width(10.0)
        t.move_to(box)
        self.sfx("ding")
        self.play(GrowFromCenter(box, rate_func=BOUNCE), Write(t), run_time=1.3)
        obs = ar("لاحظها ثم:", 30, "BOLD", ROSE).move_to([0, -0.5, 0])
        self.sfx("pop")
        self.play(FadeIn(obs, shift=UP * 0.3), run_time=0.8)
        steps = [("قلّل", YELL), ("افرز", BLUE), ("أعِد التدوير", GREEN)]
        pills = VGroup()
        for i, (lab, col) in enumerate(steps):
            p = RoundedRectangle(corner_radius=0.35, width=3.3, height=1.1,
                                 fill_color=col, fill_opacity=0.92,
                                 stroke_color=INK, stroke_width=2.5)
            pt = ar(lab, 28, "BOLD", "#FFFFFF")
            if pt.width > 2.8:
                pt.scale_to_fit_width(2.8)
            pt.move_to(p)
            pills.add(VGroup(p, pt).move_to([3.7 - i * 3.7, -1.9, 0]))
        t2 = 0
        for p in pills:
            self.sfx("ding")
            self.play(GrowFromCenter(p, rate_func=BOUNCE), run_time=0.7)
            t2 += 0.7
        self.wait(max(d - t2 - 3.1, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أعرّف التلوث وأنواعه",
            "أذكر أسبابه وآثاره",
            "أقترح وسائل لمكافحته",
        ])
        self.s_def()
        self.s_air()
        self.s_water()
        self.s_soil()
        self.s_sol()
        self.s_example()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
