# -*- coding: utf-8 -*-
"""Vidéo U28 — الأشكال الرباعية.  Rendu : venv/bin/manim -qh scene_u28.py VideoU28
Cœur de la vidéo : les 5 quadrilatères TRACÉS un à un (Square, Rectangle, Polygon)
avec leurs propriétés visibles — tirets d'égalité, petits carrés des angles droits,
diagonales du معين — puis tableau récapitulatif et l'exemple du cahier (مربع ضلعه 5)."""
import numpy as np

from manim import (VGroup, Line, DashedLine, DashedVMobject, Polygon, Square, Rectangle,
                   RoundedRectangle, SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter, LaggedStart,
                   Indicate, Wiggle, Flash,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


def ticks(p1, p2, n=1, color=REDA):
    """n tirets d'égalité perpendiculaires au milieu du segment [p1 p2]."""
    p1, p2 = np.array(p1, float), np.array(p2, float)
    mid = (p1 + p2) / 2
    u = (p2 - p1) / np.linalg.norm(p2 - p1)
    perp = np.array([-u[1], u[0], 0.0])
    g = VGroup()
    for i in range(n):
        c = mid + u * (i - (n - 1) / 2) * 0.15
        g.add(Line(c - perp * 0.14, c + perp * 0.14, color=color, stroke_width=4.5))
    return g


def corner_mark(p, dx, dy, s=0.28, color=REDA):
    """Petit carré d'angle droit au sommet p, vers les directions unitaires dx et dy."""
    p, dx, dy = np.array(p, float), np.array(dx, float), np.array(dy, float)
    return VGroup(Line(p + dx * s, p + dx * s + dy * s, color=color, stroke_width=3.5),
                  Line(p + dy * s, p + dx * s + dy * s, color=color, stroke_width=3.5))


class VideoU28(MajorScene):
    AUDIO = HERE / "audio_u28"
    UNIT_AR = "الوحدة 28"
    UNIT_COLOR = GREEN
    TITLE = "الأشكال الرباعية"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 28"

    SHAPE_POS = RIGHT * 3.1 + DOWN * 0.55

    def prop(self, txt, color):
        return ar(txt, 30, "BOLD", color).move_to(LEFT * 3.1 + DOWN * 0.55)

    # ── 2. الأشكال الخمسة واحدًا واحدًا ─────────────────────────
    def s_shapes(self):
        d = self.seg("quad1")
        head = titled("الأشكال الرباعية", 44, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        quad = Polygon([-1.7, -1.0, 0], [1.5, -1.2, 0], [1.9, 0.9, 0], [-1.1, 1.1, 0],
                       fill_color=GREEN, fill_opacity=0.35,
                       stroke_color=INK, stroke_width=4).shift(DOWN * 0.5)
        self.sfx("pop")
        self.play(Create(quad), run_time=1.1)
        lab = ar("4 أضلاع · 4 زوايا · 4 رؤوس", 30, "BOLD", GOLD).move_to(DOWN * 2.7)
        self.play(Write(lab), run_time=1.1)
        self.wait(max(d - 3.1, 0.2))
        self.play(FadeOut(quad), FadeOut(lab), run_time=0.5)

        # المربع
        d = self.seg("quad2")
        sq = Square(side_length=2.3, fill_color=YELL, fill_opacity=0.5,
                    stroke_color=INK, stroke_width=4).move_to(self.SHAPE_POS)
        v = sq.get_vertices()   # UR, UL, DL, DR
        marks = VGroup(*[ticks(v[i], v[(i + 1) % 4]) for i in range(4)],
                       corner_mark(v[2], (1, 0, 0), (0, 1, 0)),
                       corner_mark(v[3], (-1, 0, 0), (0, 1, 0)))
        name = ar("المربع", 32, "BOLD", GOLD).next_to(sq, UP, buff=0.3)
        p = self.prop("4 أضلاع متساوية\n4 زوايا قائمة", GOLD)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(sq, name), rate_func=BOUNCE), run_time=0.9)
        self.sfx("ding")
        self.play(Create(marks), FadeIn(p, shift=RIGHT * 0.4), run_time=1.1)
        self.wait(max(d - 2.0, 0.2))
        g_prev = VGroup(sq, marks, name, p)

        # المستطيل
        d = self.seg("quad3")
        rc = Rectangle(width=3.3, height=2.0, fill_color=BLUE, fill_opacity=0.45,
                       stroke_color=INK, stroke_width=4).move_to(self.SHAPE_POS)
        v = rc.get_vertices()
        marks = VGroup(ticks(v[2], v[3]), ticks(v[1], v[0]),
                       ticks(v[2], v[1], 2), ticks(v[3], v[0], 2),
                       corner_mark(v[2], (1, 0, 0), (0, 1, 0)),
                       corner_mark(v[3], (-1, 0, 0), (0, 1, 0)))
        lo = ar("الطول", 24, "BOLD", BLUE).next_to(rc, DOWN, buff=0.18)
        la = ar("العرض", 24, "BOLD", BLUE).next_to(rc, RIGHT, buff=0.18)
        name = ar("المستطيل", 32, "BOLD", BLUE).next_to(rc, UP, buff=0.3)
        p = self.prop("متقابلاته متساوية\n4 زوايا قائمة", BLUE)
        self.play(FadeOut(g_prev), run_time=0.4)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(rc, name), rate_func=BOUNCE), run_time=0.9)
        self.sfx("ding")
        self.play(Create(marks), FadeIn(p, shift=RIGHT * 0.4),
                  FadeIn(lo), FadeIn(la), run_time=1.1)
        self.wait(max(d - 2.4, 0.2))
        g_prev = VGroup(rc, marks, lo, la, name, p)

        # المعين + قطران متعامدان
        d = self.seg("quad4")
        c = np.array([self.SHAPE_POS[0], self.SHAPE_POS[1], 0.0])
        pts = [c + np.array(o) for o in
               [(0, 1.35, 0), (1.0, 0, 0), (0, -1.35, 0), (-1.0, 0, 0)]]
        lo_z = Polygon(*pts, fill_color=ROSE, fill_opacity=0.45,
                       stroke_color=INK, stroke_width=4)
        marks = VGroup(*[ticks(pts[i], pts[(i + 1) % 4]) for i in range(4)])
        d1 = DashedLine(pts[0], pts[2], color=INK, stroke_width=3.5, dash_length=0.14)
        d2 = DashedLine(pts[1], pts[3], color=INK, stroke_width=3.5, dash_length=0.14)
        ra = corner_mark(c, (0.7, 0, 0), (0, 0.7, 0), s=0.24)
        name = ar("المعين", 32, "BOLD", ROSE).next_to(lo_z, UP, buff=0.25)
        p = self.prop("4 أضلاع متساوية\nقطران متعامدان", ROSE)
        self.play(FadeOut(g_prev), run_time=0.4)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(lo_z, name), rate_func=BOUNCE), run_time=0.9)
        self.sfx("ding")
        self.play(Create(marks), Create(d1), Create(d2), run_time=1.0)
        self.play(Create(ra), FadeIn(p, shift=RIGHT * 0.4), run_time=0.8)
        self.wait(max(d - 3.1, 0.2))
        g_prev = VGroup(lo_z, marks, d1, d2, ra, name, p)

        # متوازي الأضلاع
        d = self.seg("quad5")
        pts = [c + np.array(o) for o in
               [(-1.9, -1.0, 0), (1.1, -1.0, 0), (1.9, 1.0, 0), (-1.1, 1.0, 0)]]
        para = Polygon(*pts, fill_color=GREEN, fill_opacity=0.45,
                       stroke_color=INK, stroke_width=4)
        marks = VGroup(ticks(pts[0], pts[1]), ticks(pts[3], pts[2]),
                       ticks(pts[1], pts[2], 2), ticks(pts[0], pts[3], 2))
        name = ar("متوازي الأضلاع", 30, "BOLD", GREEN).next_to(para, UP, buff=0.25)
        p = self.prop("متقابلاته متوازية\nومتساوية", GREEN)
        self.play(FadeOut(g_prev), run_time=0.4)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(para, name), rate_func=BOUNCE), run_time=0.9)
        self.sfx("ding")
        self.play(Create(marks), FadeIn(p, shift=RIGHT * 0.4), run_time=1.0)
        self.wait(max(d - 2.3, 0.2))
        g_prev = VGroup(para, marks, name, p)

        # شبه المنحرف
        d = self.seg("quad6")
        pts = [c + np.array(o) for o in
               [(-2.0, -1.0, 0), (2.0, -1.0, 0), (1.1, 1.0, 0), (-1.1, 1.0, 0)]]
        trap = Polygon(*pts, fill_color=LILA, fill_opacity=0.45,
                       stroke_color=INK, stroke_width=4)
        gb = ar("القاعدة الكبيرة", 22, "BOLD", LILA).next_to(trap, DOWN, buff=0.18)
        pb = ar("القاعدة الصغيرة", 22, "BOLD", LILA).next_to(trap, UP, buff=0.5)
        name = ar("شبه المنحرف", 30, "BOLD", LILA).next_to(pb, UP, buff=0.2)
        p = self.prop("ضلعان متقابلان\nمتوازيان فقط", LILA)
        self.play(FadeOut(g_prev), run_time=0.4)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(trap, name), rate_func=BOUNCE), run_time=0.9)
        self.sfx("ding")
        self.play(Indicate(Line(pts[0], pts[1]), color=GOLD),
                  FadeIn(gb), FadeIn(pb), FadeIn(p, shift=RIGHT * 0.4), run_time=1.1)
        self.wait(max(d - 2.4, 0.2))
        self.clear_all()

    # ── 3. الجدول التلخيصي ──────────────────────────────────────
    def s_table(self):
        d = self.seg("tab1")
        head = titled("جدول الأشكال الخمسة", 40, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        rows_data = [
            ("المربع", "4 أضلاع متساوية · 4 زوايا قائمة", YELL),
            ("المستطيل", "متقابلاته متساوية · 4 زوايا قائمة", BLUE),
            ("المعين", "4 أضلاع متساوية · قطران متعامدان", ROSE),
            ("متوازي الأضلاع", "متقابلاته متوازية ومتساوية", GREEN),
            ("شبه المنحرف", "ضلعان متقابلان متوازيان", LILA),
        ]
        table = VGroup()
        for i, (nm, pr, col) in enumerate(rows_data):
            chipbox = RoundedRectangle(corner_radius=0.16, width=3.6, height=0.72,
                                       fill_color=col, fill_opacity=0.95,
                                       stroke_color=INK, stroke_width=2)
            chipbox.move_to([4.0, 1.3 - i * 0.92, 0])
            nm_t = ar(nm, 26, "BOLD", "#FFFFFF").move_to(chipbox)
            pr_t = ar(pr, 26).next_to(chipbox, LEFT, buff=0.5)
            table.add(VGroup(chipbox, nm_t, pr_t))
        self.sfx("tada")
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.5, rate_func=BOUNCE)
                                for r in table], lag_ratio=0.18), run_time=2.6)
        self.wait(max(d - 3.5, 0.2))
        self.clear_all()

    # ── 4. المحيط ثم مثال المربع ضلعه 5 ─────────────────────────
    def s_perimetre(self):
        d = self.seg("per1")
        head = titled("المحيط", 44, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        f1 = ar("محيط المربع = الضلع × 4", 34, "BOLD", GOLD).move_to(UP * 0.6)
        b1 = SurroundingRectangle(f1, color=GOLD, corner_radius=0.16, buff=0.25)
        f2 = ar("محيط المستطيل = (الطول + العرض) × 2", 34, "BOLD", BLUE).move_to(DOWN * 0.9)
        b2 = SurroundingRectangle(f2, color=BLUE, corner_radius=0.16, buff=0.25)
        self.sfx("pop")
        self.play(Write(f1), Create(b1), run_time=1.4)
        self.wait(1.4)
        self.sfx("pop")
        self.play(Write(f2), Create(b2), run_time=1.4)
        self.wait(max(d - 5.1, 0.2))
        self.clear_all()

    def s_exemple(self):
        d = self.seg("ex1")
        head = titled("مثال: مربع ضلعه 5 cm", 38, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        sq = Square(side_length=2.6, fill_color=YELL, fill_opacity=0.4,
                    stroke_color=INK, stroke_width=4).move_to(RIGHT * 3.1 + DOWN * 0.7)
        side = num("5 cm", 32, GOLD).next_to(sq, DOWN, buff=0.25)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(sq, side), rate_func=BOUNCE), run_time=1.0)
        contour = Square(side_length=2.6, stroke_color=GOLD,
                         stroke_width=9).move_to(sq)
        self.sfx("whoosh")
        self.play(Create(contour), run_time=1.2)
        c1 = num("5 × 4 = 20 cm", 42, GOLD).move_to(LEFT * 3.2 + UP * 0.1)
        self.sfx("ding")
        self.play(Write(c1), run_time=1.2)
        self.wait(max(d - 4.3, 0.2))

        d = self.seg("ex2")
        self.play(FadeOut(contour), sq.animate.set_fill(YELL, 0.85), run_time=0.9)
        c2 = num("5 × 5 = 25 cm²", 42, GREEN).move_to(LEFT * 3.2 + DOWN * 1.3)
        frame = SurroundingRectangle(c2, color=GREEN, corner_radius=0.15, buff=0.2)
        self.sfx("pop")
        self.play(Write(c2), run_time=1.2)
        self.sfx("ding")
        self.play(Create(frame), run_time=0.7)
        self.play(Flash(c2, color=GREEN, flash_radius=2.4), run_time=0.9)
        self.wait(max(d - 3.7, 0.2))
        self.clear_all()

    # ── 5. انتبه : المحيط ≠ المساحة ─────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! المحيط غير المساحة", 38, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=8.2, height=1.05, fill_color=BLUE,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 1.6 + UP * 0.5)
        c1t = ar("المحيط = (الطول + العرض) × 2", 28, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=8.2, height=1.05, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 1.6 + DOWN * 1.0)
        c2t = ar("المساحة = الطول × العرض", 28, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 6. السر : السياج والداخل ────────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي قبل أن نفترق", 40, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.0)
        champ = Rectangle(width=4.6, height=2.6, fill_color=GREEN, fill_opacity=0.55,
                          stroke_width=0).move_to(RIGHT * 2.6 + DOWN * 0.8)
        fence = DashedVMobject(Rectangle(width=5.0, height=3.0, stroke_color=GOLD,
                                         stroke_width=8).move_to(champ), num_dashes=36)
        self.sfx("pop")
        self.play(FadeIn(champ, scale=0.7, rate_func=BOUNCE), run_time=0.9)
        self.sfx("whoosh")
        self.play(Create(fence), run_time=1.3)
        l1 = ar("المحيط: السياج حوله (m)", 30, "BOLD", GOLD).move_to(LEFT * 3.7 + UP * 0.1)
        l2 = ar("المساحة: ما بداخله (m²)", 30, "BOLD", GREEN).move_to(LEFT * 3.7 + DOWN * 1.4)
        self.sfx("ding")
        self.play(Write(l1), run_time=1.2)
        self.play(Indicate(fence, color=GOLD, scale_factor=1.05), run_time=0.9)
        self.sfx("ding")
        self.play(Write(l2), run_time=1.2)
        self.play(Indicate(champ, color=GREEN, scale_factor=1.06), run_time=0.9)
        self.wait(max(d - 7.4, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أتعرّف خصائص الأشكال الرباعية الخمسة",
            "أحسب محيط المربع والمستطيل",
            "أحسب مساحة كل شكل بقاعدته",
        ])
        self.s_shapes()
        self.s_table()
        self.s_perimetre()
        self.s_exemple()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
