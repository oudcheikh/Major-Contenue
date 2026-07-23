# -*- coding: utf-8 -*-
"""Vidéo U20 — الزمن والأعداد الستينية.  Rendu : venv/bin/manim -qh scene_u20.py VideoU20
Cœur de la vidéo : une horloge dessinée dont les aiguilles TOURNENT (1 tour = 60 min = 1 h),
la cascade 1 h = 60 min = 3600 s, l'addition sexagésimale posée avec le carry de 60,
et la durée 9 h 15 → 11 h 40 comptée par القفزات sur le مستقيم (RTL : le temps va vers la gauche)."""
import math

import numpy as np
from manim import (VGroup, Line, Arrow, ArcBetweenPoints, Dot, Circle,
                   RoundedRectangle, SurroundingRectangle, Cross,
                   FadeIn, FadeOut, Write, Create, Transform, GrowFromCenter,
                   Rotate, Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT, TAU, rate_functions as rf)

from video_common import (MajorScene, ar, num, titled, pie,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


class VideoU20(MajorScene):
    AUDIO = HERE / "audio_u20"
    UNIT_AR = "الوحدة 20"
    UNIT_COLOR = BLUE
    TITLE = "الزمن والأعداد الستينية"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 20"

    # ── 2. الساعة : عقربان يدوران ───────────────────────────────
    def s_horloge(self):
        d = self.seg("clock1")
        head = titled("أقرأ الساعة", 44, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        cc = np.array([2.7, -0.5, 0.0])
        face = Circle(radius=1.75, stroke_color=INK, stroke_width=5,
                      fill_color="#FFFFFF", fill_opacity=0.95).move_to(cc)
        ticks = VGroup()
        for k in range(12):
            a = TAU * k / 12
            p1 = cc + np.array([math.sin(a) * 1.45, math.cos(a) * 1.45, 0])
            p2 = cc + np.array([math.sin(a) * 1.62, math.cos(a) * 1.62, 0])
            ticks.add(Line(p1, p2, color=INK, stroke_width=4))
        self.sfx("pop")
        self.play(Create(face), FadeIn(ticks), run_time=1.2)
        self.h_hand = Line(cc, cc + np.array([0, 0.85, 0]), color=INK, stroke_width=10)
        self.m_hand = Line(cc, cc + np.array([0, 1.32, 0]), color=ROSE, stroke_width=6)
        pivot = Dot(cc, radius=0.07, color=INK)
        self.play(Create(self.h_hand), Create(self.m_hand), FadeIn(pivot), run_time=0.9)
        lab_h = ar("العقرب القصير ← الساعات", 28, "BOLD", INK).move_to([-3.2, 0.4, 0])
        lab_m = ar("العقرب الطويل ← الدقائق", 28, "BOLD", ROSE).move_to([-3.2, -0.7, 0])
        self.sfx("pop")
        self.play(FadeIn(lab_h, shift=LEFT * 0.4), run_time=0.9)
        self.sfx("pop")
        self.play(FadeIn(lab_m, shift=LEFT * 0.4), run_time=0.9)
        self.wait(max(d - 4.8, 0.2))                     # somme anims = 4.8

        d = self.seg("clock2")   # dawra kamla : la grande aiguille fait un tour complet
        self.sfx("whoosh")
        self.play(Rotate(self.m_hand, angle=-TAU, about_point=cc),
                  Rotate(self.h_hand, angle=-TAU / 12, about_point=cc),
                  run_time=3.0, rate_func=rf.ease_in_out_sine)
        badge = VGroup(ar("دورة كاملة =", 30, "BOLD", ROSE),
                       num("60 min", 40, ROSE)).arrange(LEFT, buff=0.3)
        badge.move_to([-3.2, -1.9, 0])
        self.sfx("ding")
        self.play(FadeIn(badge, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 3.9, 0.2))                     # somme anims = 3.9
        self.clear_all()

    # ── 3. الشلال : 1 h = 60 min = 3600 s ──────────────────────
    def _tbox(self, txt, color, pos, w=2.9):
        b = RoundedRectangle(corner_radius=0.22, width=w, height=1.15, fill_color=color,
                             fill_opacity=0.95, stroke_color=INK, stroke_width=2).move_to(pos)
        t = num(txt, 42, INK).move_to(b)
        return VGroup(b, t)

    def s_cascade(self):
        d = self.seg("conv1")
        head = titled("وحدات الزمن: نظام ستيني", 40, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        b1 = self._tbox("1 h", YELL, [4.3, 0.7, 0])
        b2 = self._tbox("60 min", GREEN, [0.0, 0.7, 0])
        b3 = self._tbox("3600 s", BLUE, [-4.3, 0.7, 0])
        a12 = Arrow([2.75, 0.7, 0], [1.55, 0.7, 0], color=GOLD, stroke_width=6, buff=0)
        k12 = num("× 60", 28, GOLD).next_to(a12, UP, buff=0.15)
        a23 = Arrow([-1.55, 0.7, 0], [-2.75, 0.7, 0], color=GOLD, stroke_width=6, buff=0)
        k23 = num("× 60", 28, GOLD).next_to(a23, UP, buff=0.15)
        self.sfx("pop")
        self.play(GrowFromCenter(b1, rate_func=BOUNCE), run_time=0.8)
        self.play(Create(a12), FadeIn(k12), run_time=0.7)
        self.sfx("pop")
        self.play(GrowFromCenter(b2, rate_func=BOUNCE), run_time=0.8)
        minline = num("1 min = 60 s", 38).move_to([2.6, -1.35, 0])
        self.play(Write(minline), run_time=1.0)
        self.wait(max(d - 4.2, 0.2))                     # somme anims = 4.2

        d = self.seg("conv2")   # 60 × 60 = 3600
        self.play(Create(a23), FadeIn(k23), run_time=0.7)
        self.sfx("ding")
        self.play(GrowFromCenter(b3, rate_func=BOUNCE), run_time=0.8)
        eq36 = num("60 × 60 = 3600 s", 38).move_to([-2.6, -1.35, 0])
        self.play(Write(eq36), run_time=1.0)
        self.wait(max(d - 2.5, 0.2))                     # somme anims = 2.5

        d = self.seg("conv3")   # نظام ستيني أساسه 60
        badge = VGroup(ar("نظام ستيني أساسه", 30, "BOLD", LILA),
                       num("60", 40, LILA)).arrange(LEFT, buff=0.3).move_to([0, -2.55, 0])
        box = SurroundingRectangle(badge, color=LILA, corner_radius=0.15, buff=0.2)
        self.sfx("pop")
        self.play(FadeIn(badge, scale=0.5, rate_func=BOUNCE), Create(box), run_time=1.1)
        self.wait(max(d - 1.1, 0.2))                     # somme anims = 1.1

        d = self.seg("conv4")   # 2 h = 120 min
        self.play(FadeOut(minline), FadeOut(eq36), run_time=0.4)
        eq2h = num("2 h = 2 × 60 = 120 min", 44).move_to([0, -1.35, 0])
        self.play(Write(eq2h), run_time=1.4)
        self.play(Flash(eq2h, color=GREEN, flash_radius=2.6), run_time=0.9)
        self.wait(max(d - 2.7, 0.2))                     # somme anims = 2.7
        self.clear_all()

    # ── 4. الجمع الستيني : 1 h 50 min + 2 h 20 min ─────────────
    def s_addition(self):
        XH, XM = 1.7, -1.7
        d = self.seg("add1")
        head = titled("أجمع عددين ستينيين", 42, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        col_h = ar("الساعات", 24, "BOLD", "#999999").move_to([XH, 2.35, 0])
        col_m = ar("الدقائق", 24, "BOLD", "#999999").move_to([XM, 2.35, 0])
        r1h = num("1 h", 50).move_to([XH, 1.45, 0])
        r1m = num("50 min", 50).move_to([XM, 1.45, 0])
        r2h = num("2 h", 50).move_to([XH, 0.6, 0])
        r2m = num("20 min", 50).move_to([XM, 0.6, 0])
        sgn = num("+", 54, GOLD).move_to([-3.8, 0.6, 0])
        bar = Line([-4.1, 0.1, 0], [3.2, 0.1, 0], color=INK, stroke_width=5)
        self.play(FadeIn(col_h), FadeIn(col_m), run_time=0.6)
        self.play(Write(r1h), Write(r1m), run_time=1.0)      # de droite : h avant min
        self.play(Write(r2h), Write(r2m), FadeIn(sgn), Create(bar), run_time=1.2)
        self.wait(max(d - 3.7, 0.2))                     # somme anims = 3.7

        d = self.seg("add2")   # 50 + 20 = 70 > 60 !
        self.play(Indicate(VGroup(r1m, r2m), color=YELL, scale_factor=1.25), run_time=1.0)
        s70 = num("70", 50, REDA).move_to([XM, -0.75, 0])
        self.sfx("pop")
        self.play(FadeIn(s70, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.8)
        excl = ar("أكبر من ستين!", 26, "BOLD", REDA).next_to(s70, DOWN, buff=0.35)
        self.sfx("boing")
        self.play(FadeIn(excl, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 2.6, 0.2))                     # somme anims = 2.6

        d = self.seg("add3")   # أنزع 60 وأحمل 1 h
        eq70 = num("70 − 60 = 10", 38).move_to([XM, -1.95, 0])
        self.play(Write(eq70), FadeOut(excl), run_time=1.1)
        carry = num("+1 h", 30, REDA).move_to([XH, 2.05, 0])
        self.sfx("ding")
        self.play(FadeIn(carry, shift=UP * 0.4, rate_func=BOUNCE), FadeOut(col_h), run_time=0.8)
        s10 = num("10 min", 50, GREEN).move_to([XM, -0.75, 0])
        self.sfx("whoosh")
        self.play(Transform(s70, s10), run_time=0.9)
        self.wait(max(d - 2.8, 0.2))                     # somme anims = 2.8

        d = self.seg("add4")   # 1 + 2 + 1 = 4 h → الجواب 4 h 10 min
        self.play(Indicate(VGroup(r1h, r2h, carry), color=YELL, scale_factor=1.25), run_time=1.0)
        s4 = num("4 h", 50, GREEN).move_to([XH, -0.75, 0])
        self.sfx("pop")
        self.play(FadeIn(s4, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.8)
        result = VGroup(s4, s70)
        frame = SurroundingRectangle(result, color=GREEN, corner_radius=0.15, buff=0.25)
        self.sfx("ding")
        self.play(Create(frame), FadeOut(eq70), run_time=1.0)
        self.play(Flash(result, color=GREEN, flash_radius=2.6), run_time=0.9)
        self.wait(max(d - 3.7, 0.2))                     # somme anims = 3.7
        self.clear_all()

    # ── 5. المدة على المستقيم : 9 h 15 → 11 h 40 ───────────────
    def s_duree(self):
        d = self.seg("dur1")
        head = titled("أحسب المدة بين توقيتين", 40, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        rule = ar("المدة = ساعة الوصول − ساعة الانطلاق", 30, "BOLD", LILA).shift(UP * 1.7)
        rbox = SurroundingRectangle(rule, color=LILA, corner_radius=0.15, buff=0.2)
        self.play(FadeIn(rule), Create(rbox), run_time=1.0)
        line = Line([-5.6, -1.1, 0], [5.4, -1.1, 0], color=INK, stroke_width=4)
        self.play(Create(line), run_time=0.9)
        xs = [4.6, 1.6, -1.4, -3.9]                       # RTL : le temps avance vers la gauche
        labs = ["9 h 15", "10 h 15", "11 h 15", "11 h 40"]
        marks = VGroup()
        for x, lb in zip(xs, labs):
            marks.add(VGroup(Line([x, -1.28, 0], [x, -0.92, 0], color=INK, stroke_width=4),
                             num(lb, 28).move_to([x, -1.75, 0])))
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.2) for m in marks],
                              lag_ratio=0.25), run_time=1.6)
        self.wait(max(d - 4.4, 0.2))                     # somme anims = 4.4

        d = self.seg("dur2")   # القفزات : ساعة + ساعة + 25 min
        hops = [(4.6, 1.6, "ساعة", GREEN, True), (1.6, -1.4, "ساعة", GREEN, True),
                (-1.4, -3.9, "25 min", ROSE, False)]
        t = 0
        for x1, x2, lb, col, is_ar in hops:
            arc = ArcBetweenPoints(np.array([x1, -0.9, 0.0]), np.array([x2, -0.9, 0.0]),
                                   angle=TAU / 5, color=col, stroke_width=5)
            lab = (ar(lb, 26, "BOLD", col) if is_ar else num(lb, 26, col))
            lab.move_to([(x1 + x2) / 2, 0.15, 0])
            self.sfx("whoosh")
            self.play(Create(arc), run_time=0.7)
            self.play(FadeIn(lab, shift=UP * 0.2), run_time=0.4)
            t += 1.1
        res = VGroup(ar("المدة =", 32, "BOLD", GREEN),
                     num("2 h 25 min", 46, GREEN)).arrange(LEFT, buff=0.35).move_to([0, 0.9, 0])
        self.sfx("ding")
        self.play(FadeIn(res, scale=0.5, rate_func=BOUNCE), run_time=1.0)
        self.play(Flash(res, color=GREEN, flash_radius=2.6), run_time=0.8)
        self.wait(max(d - t - 1.8, 0.2))                 # somme anims = 5.1
        self.clear_all()

    # ── 6. انتبه : أستلف 60 لا 100 ──────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! أستلف ستين لا مئة", 38, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        ok_b = RoundedRectangle(corner_radius=0.22, width=3.4, height=1.1, fill_color=GREEN,
                                fill_opacity=0.92, stroke_color=INK).move_to([2.9, 0.6, 0])
        ok_t = num("60", 46, "#FFFFFF").move_to(ok_b)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(ok_b, ok_t), rate_func=BOUNCE), run_time=0.8)
        no_b = RoundedRectangle(corner_radius=0.22, width=3.4, height=1.1, fill_color=ROSE,
                                fill_opacity=0.92, stroke_color=INK).move_to([-0.9, 0.6, 0])
        no_t = num("100", 46, "#FFFFFF").move_to(no_b)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(no_b, no_t), rate_func=BOUNCE), run_time=0.8)
        cross = Cross(no_b, stroke_color=REDA, stroke_width=7)
        self.play(Create(cross), run_time=0.6)
        conv = num("1 min → 60 s", 38, REDA).move_to([1.0, -1.1, 0])
        self.sfx("ding")
        self.play(Write(conv), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 5.2, 0.2))                     # somme anims = 5.2
        self.clear_all()

    # ── 7. السر : نصف = 30 · ربع = 15 · ثلث = 20 ───────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ مفيد قبل أن نفترق", 42, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.6)
        trio = [("نصف ساعة", 2, "30 min", 3.9, GOLD),
                ("ربع ساعة", 4, "15 min", 0.0, BLUE),
                ("ثلث ساعة", 3, "20 min", -3.9, GREEN)]
        t = 0
        for lb, parts, mins, x, col in trio:            # de droite à gauche
            p = pie(parts, 1, radius=1.0, fill=col).move_to([x, 0.55, 0])
            m = num(mins, 36, col).next_to(p, DOWN, buff=0.3)
            l = ar(lb, 28, "BOLD", INK).next_to(m, DOWN, buff=0.2)
            self.sfx("pop")
            self.play(FadeIn(VGroup(p, m, l), scale=0.4, rate_func=BOUNCE), run_time=0.9)
            self.wait(0.6)
            t += 1.5
        morale = ar("احفظها تُسرع حسابك!", 30, "BOLD", LILA).move_to([0, -2.75, 0])
        self.sfx("ding")
        self.play(Write(morale), run_time=1.2)
        self.wait(max(d - t - 3.8, 0.2))                 # somme anims = 8.3
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أحوّل بين الساعات والدقائق والثواني",
            "أجمع وأطرح الأعداد الستينية",
            "أحسب المدة بين توقيتين",
        ])
        self.s_horloge()
        self.s_cascade()
        self.s_addition()
        self.s_duree()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
