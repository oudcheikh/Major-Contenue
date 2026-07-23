# -*- coding: utf-8 -*-
"""Vidéo U4 — الضرب.  Rendu : venv/bin/manim -qh scene_u4.py VideoU4
Le concept est MONTRÉ : 4 groupes de 3 coquillages → 3+3+3+3 → 4×3,
la multiplication posée 234×3 s'anime chiffre par chiffre avec la retenue."""
from manim import (VGroup, Circle, Line, RoundedRectangle, SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, Transform, GrowFromCenter,
                   Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT, DR)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)

COLS = [-1.1, 0.0, 1.1]        # مئات، عشرات، آحاد
KHANAT3 = ["المئات", "العشرات", "الآحاد"]


def shell_group(n_shells, color):
    """Petit groupe : boîte arrondie contenant n coquillages (points colorés)."""
    box = RoundedRectangle(corner_radius=0.25, width=1.9, height=1.5,
                           fill_color=color, fill_opacity=0.18, stroke_color=color, stroke_width=3)
    dots = VGroup(*[Circle(radius=0.21, fill_color=color, fill_opacity=1, stroke_color=INK,
                           stroke_width=2) for _ in range(n_shells)])
    dots.arrange(RIGHT, buff=0.22).move_to(box)
    return VGroup(box, dots)


class VideoU4(MajorScene):
    AUDIO = HERE / "audio_u4"
    UNIT_AR = "الوحدة 4"
    UNIT_COLOR = BLUE
    TITLE = "الضرب"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 4"

    # ── 2. المفهوم : جمع متكرر ──────────────────────────────────
    def s_concept(self):
        d = self.seg("conc1")
        head = titled("الضرب جمعٌ متكرر", 42, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        cols = [YELL, GREEN, ROSE, LILA]
        self.groups = VGroup(*[shell_group(3, c) for c in cols])
        self.groups.arrange(RIGHT, buff=0.55).move_to(UP * 0.9)
        self.play(LaggedStart(*[FadeIn(g, scale=0.4, rate_func=BOUNCE) for g in self.groups],
                              lag_ratio=0.2), run_time=1.8)
        self.wait(max(d - 2.7, 0.2))

        d = self.seg("conc2")   # 3+3+3+3 se construit groupe par groupe
        parts = []
        t = 0
        self.wait(2.4)
        t += 2.4
        for i, g in enumerate(self.groups[::-1]):   # de droite à gauche (RTL)
            self.play(Indicate(g, color=GOLD, scale_factor=1.12), run_time=0.7)
            p = num("3" if i == 0 else "+ 3", 46, GOLD)
            xs = 2.4 - i * 1.5
            p.move_to([xs, -0.9, 0])
            self.sfx("pop")
            self.play(FadeIn(p, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.5)
            parts.append(p)
            t += 1.2
        eq12 = num("= 12", 46, GOLD).move_to([2.4 - 4 * 1.5 - 0.4, -0.9, 0])
        self.sfx("ding")
        self.play(FadeIn(eq12, scale=0.6), run_time=0.7)
        t += 0.7
        self.wait(max(d - t, 0.2))
        self.sum_row = VGroup(*parts, eq12)

        d = self.seg("conc3")   # → 4 × 3 = 12
        mult = num("4 × 3 = 12", 64, BLUE).move_to(DOWN * 2.3)
        self.wait(1.8)
        self.sfx("whoosh")
        self.play(Transform(self.sum_row, mult), run_time=1.2)
        self.sfx("ding")
        self.play(Flash(self.sum_row, color=BLUE, flash_radius=2.4), run_time=0.9)
        self.wait(max(d - 3.9, 0.2))

        d = self.seg("conc4")   # عاملان وجداء
        lab_f = ar("عاملان", 26, "BOLD", GREEN).move_to([2.1, -3.15, 0])
        lab_p = ar("الجداء", 26, "BOLD", ROSE).move_to([-2.2, -3.15, 0])
        self.sfx("pop")
        self.play(FadeIn(lab_f, shift=UP * 0.2, rate_func=BOUNCE), run_time=0.9)
        self.wait(1.2)
        self.sfx("pop")
        self.play(FadeIn(lab_p, shift=UP * 0.2, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 3.0, 0.2))
        self.clear_all()

    # ── 3. الخاصية : تبديل العاملين + جداول ────────────────────
    def s_commut(self):
        d = self.seg("comm1")
        head = titled("أبدّل العاملين والجداء لا يتغير", 38, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        a = num("4 × 3", 60).move_to(RIGHT * 2.8 + DOWN * 0.3)
        b = num("3 × 4", 60).move_to(LEFT * 2.8 + DOWN * 0.3)
        eq = num("=", 60, GREEN).move_to(DOWN * 0.3)
        self.play(Write(a), run_time=0.9)
        self.wait(1.8)
        self.sfx("whoosh")
        self.play(GrowFromCenter(eq), FadeIn(b, scale=0.5, rate_func=BOUNCE), run_time=1.1)
        both = ar("النتيجة واحدة: 12", 30, "BOLD", GREEN).move_to(DOWN * 1.9)
        self.sfx("ding")
        self.play(Write(both), run_time=1.1)
        self.wait(max(d - 5.0, 0.2))

        d = self.seg("tab1")   # جداول 1..12
        self.play(FadeOut(a), FadeOut(b), FadeOut(eq), FadeOut(both), FadeOut(head), run_time=0.5)
        head2 = titled("أحفظ جداول الضرب حتى 12", 40, GOLD)
        self.play(FadeIn(head2, shift=DOWN * 0.3), run_time=0.8)
        from video_common import PALETTE
        chips = VGroup()
        for i in range(12):
            c = PALETTE[i % len(PALETTE)]
            b_ = RoundedRectangle(corner_radius=0.18, width=1.5, height=1.0, fill_color=c,
                                  fill_opacity=0.9, stroke_color=INK, stroke_width=1.5)
            t_ = num(f"×{i + 1}", 30, "#FFFFFF" if c != YELL else INK).move_to(b_)
            chips.add(VGroup(b_, t_))
        chips.arrange_in_grid(rows=2, buff=0.28).move_to(DOWN * 0.7)
        self.sfx("tada")
        self.play(LaggedStart(*[FadeIn(ch, scale=0.3, rate_func=BOUNCE) for ch in chips],
                              lag_ratio=0.07), run_time=2.4)
        self.wait(max(d - 3.7, 0.2))
        self.clear_all()

    # ── 4. الضرب العمودي : 234 × 3 ─────────────────────────────
    def s_vertical(self):
        d = self.seg("mult1")
        head = titled("الضرب العمودي", 42, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        labels = VGroup(*[ar(k, 20, "BOLD", "#999999").move_to([COLS[i], 2.35, 0])
                          for i, k in enumerate(KHANAT3)])
        top = VGroup(*[num(ch, 56).move_to([COLS[i], 1.55, 0]) for i, ch in enumerate("234")])
        bot = num("3", 56).move_to([COLS[2], 0.65, 0])
        sgn = num("×", 56, GOLD).move_to([-2.1, 0.65, 0])
        bar = Line([-2.4, 0.05, 0], [1.8, 0.05, 0], color=INK, stroke_width=5)
        self.play(FadeIn(labels), Write(top), run_time=1.3)
        self.play(Write(bot), FadeIn(sgn), Create(bar), run_time=1.2)
        self.wait(max(d - 3.4, 0.2))

        d = self.seg("mult2")   # 3×4=12 → 2, retenue 1
        self.play(Indicate(VGroup(top[2], bot), color=YELL, scale_factor=1.3), run_time=1.0)
        self.wait(2.0)
        r2 = num("2", 56, ROSE).move_to([COLS[2], -0.65, 0])
        self.sfx("pop")
        self.play(FadeIn(r2, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.8)
        c1 = num("1", 30, REDA).move_to([COLS[1], 2.0, 0])
        self.sfx("ding")
        self.play(FadeIn(c1, shift=UP * 0.4, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 4.6, 0.2))

        d = self.seg("mult3")   # 3×3=9 +1=10 → 0, retenue 1
        self.play(Indicate(VGroup(top[1], bot, c1), color=YELL, scale_factor=1.3), run_time=1.0)
        self.wait(2.4)
        r0 = num("0", 56, ROSE).move_to([COLS[1], -0.65, 0])
        self.sfx("pop")
        self.play(FadeIn(r0, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.8)
        c2 = num("1", 30, REDA).move_to([COLS[0], 2.0, 0])
        self.sfx("ding")
        self.play(FadeIn(c2, shift=UP * 0.4, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 5.0, 0.2))

        d = self.seg("mult4")   # 3×2=6 +1=7 → جداء 702
        self.play(Indicate(VGroup(top[0], bot, c2), color=YELL, scale_factor=1.3), run_time=1.0)
        self.wait(1.8)
        r7 = num("7", 56, ROSE).move_to([COLS[0], -0.65, 0])
        self.sfx("pop")
        self.play(FadeIn(r7, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.8)
        result = VGroup(r7, r0, r2)
        frame = SurroundingRectangle(result, color=ROSE, corner_radius=0.15, buff=0.22)
        lab = ar("الجداء", 28, "BOLD", ROSE).next_to(frame, RIGHT, buff=0.5)
        self.sfx("ding")
        self.play(Create(frame), FadeIn(lab), run_time=1.0)
        self.play(Flash(result, color=ROSE, flash_radius=2.2), run_time=0.9)
        self.wait(max(d - 5.5, 0.2))
        self.clear_all()

    # ── 5. السر : جدول 9 ────────────────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ جدول التسعة", 42, LILA)
        garcon = self.boy(1.8).to_edge(LEFT, buff=0.25).shift(DOWN * 1.5)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        rule = ar("مجموع رقمي النتيجة = 9 دائمًا", 32, "BOLD", LILA).shift(UP * 1.35 + RIGHT * 0.6)
        self.play(Write(rule), run_time=1.4)
        self.wait(1.6)
        ex1 = num("9 × 2 = 18", 46).move_to(RIGHT * 2.6 + UP * 0.1)
        s1 = num("1 + 8 = 9", 40, GREEN).move_to(LEFT * 2.9 + UP * 0.1)
        self.sfx("pop")
        self.play(Write(ex1), run_time=1.0)
        self.wait(1.0)
        self.sfx("ding")
        self.play(FadeIn(s1, shift=LEFT * 0.4, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.4)
        ex2 = num("9 × 3 = 27", 46).move_to(RIGHT * 2.6 + DOWN * 1.3)
        s2 = num("2 + 7 = 9", 40, GREEN).move_to(LEFT * 2.9 + DOWN * 1.3)
        self.sfx("pop")
        self.play(Write(ex2), run_time=1.0)
        self.wait(1.0)
        self.sfx("ding")
        self.play(FadeIn(s2, shift=LEFT * 0.4, rate_func=BOUNCE), run_time=1.0)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 11.5, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أفهم الضرب على أنه جمع متكرر",
            "أحفظ جداول الضرب حتى 12",
            "أضع الضرب عموديًا وأنجزه",
        ])
        self.s_concept()
        self.s_commut()
        self.s_vertical()
        self.s_astuce()
        self.s_outro_end("outro")
