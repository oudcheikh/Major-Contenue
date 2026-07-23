# -*- coding: utf-8 -*-
"""Vidéo U27 — المثلثات.  Rendu : venv/bin/manim -qh scene_u27.py VideoU27
Cœur de la vidéo : les triangles TRACÉS (Polygon) — كيفي، قائم (RightAngle)،
متساوي الساقين ومتساوي الأضلاع (tirets d'égalité) — l'inscription au compas 3-4-5,
la hauteur en pointillés (DashedLine) et المساحة = القاعدة × الارتفاع ÷ 2 sur 6 × 4."""
import numpy as np

from manim import (VGroup, Line, DashedLine, DashedVMobject, Polygon, Arc, Dot, Circle,
                   RightAngle, SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter,
                   Indicate, Wiggle, Flash, Circumscribe,
                   UP, DOWN, LEFT, RIGHT, DEGREES)

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


def tri(pts, color, opacity=0.45):
    return Polygon(*[np.array(p, float) for p in pts], fill_color=color,
                   fill_opacity=opacity, stroke_color=INK, stroke_width=4)


class VideoU27(MajorScene):
    AUDIO = HERE / "audio_u27"
    UNIT_AR = "الوحدة 27"
    UNIT_COLOR = ROSE
    TITLE = "المثلثات"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 27"

    # ── 2. الأنواع : 4 مثلثات تظهر من اليمين إلى اليسار ─────────
    def s_types(self):
        d = self.seg("typ1")
        head = titled("أنواع المثلثات", 44, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        big = tri([(-1.6, -1.1, 0), (1.5, -1.1, 0), (0.5, 1.2, 0)], ROSE).shift(DOWN * 0.4)
        self.sfx("pop")
        self.play(Create(big), run_time=1.1)
        dots = VGroup(*[Dot(v, radius=0.11, color=GOLD) for v in big.get_vertices()])
        self.sfx("ding")
        self.play(FadeIn(dots, scale=0.4, rate_func=BOUNCE), run_time=0.8)
        lab = ar("3 أضلاع · 3 زوايا · 3 رؤوس", 30, "BOLD", GOLD).move_to(DOWN * 2.6)
        self.play(Write(lab), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.play(FadeOut(big), FadeOut(dots), FadeOut(lab), run_time=0.5)

        # typ2..typ5 : RTL — كيفي à droite … متساوي الأضلاع à gauche
        y = -0.7
        # كيفي (scalène)
        d = self.seg("typ2")
        t1 = tri([(4.0, y - 0.9, 0), (6.2, y - 0.9, 0), (5.4, y + 0.9, 0)], YELL)
        l1 = ar("كيفي", 28, "BOLD").move_to([5.1, y - 1.75, 0])
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(t1, l1), rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 1.4, 0.2))
        # قائم الزاوية + RightAngle
        d = self.seg("typ3")
        v = [(0.7, y - 0.9, 0), (2.8, y - 0.9, 0), (2.8, y + 1.0, 0)]
        t2 = tri(v, BLUE)
        l2 = ar("قائم الزاوية", 28, "BOLD").move_to([1.75, y - 1.75, 0])
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(t2, l2), rate_func=BOUNCE), run_time=0.9)
        ra = RightAngle(Line(v[1], v[0]), Line(v[1], v[2]), length=0.35,
                        color=REDA, stroke_width=4.5)
        self.sfx("ding")
        self.play(Create(ra), run_time=0.8)
        self.wait(max(d - 2.2, 0.2))
        # متساوي الساقين + tirets
        d = self.seg("typ4")
        v = [(-2.7, y - 0.9, 0), (-0.9, y - 0.9, 0), (-1.8, y + 1.0, 0)]
        t3 = tri(v, GREEN)
        l3 = ar("متساوي الساقين", 26, "BOLD").move_to([-1.8, y - 1.75, 0])
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(t3, l3), rate_func=BOUNCE), run_time=0.9)
        self.sfx("ding")
        self.play(Create(ticks(v[0], v[2])), Create(ticks(v[1], v[2])), run_time=0.8)
        self.wait(max(d - 2.2, 0.2))
        # متساوي الأضلاع + 3 tirets
        d = self.seg("typ5")
        s = 2.0
        v = [(-6.3, y - 0.9, 0), (-6.3 + s, y - 0.9, 0), (-6.3 + s / 2, y - 0.9 + s * 0.866, 0)]
        t4 = tri(v, LILA)
        l4 = ar("متساوي الأضلاع", 26, "BOLD").move_to([-5.3, y - 1.75, 0])
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(t4, l4), rate_func=BOUNCE), run_time=0.9)
        self.sfx("ding")
        self.play(Create(ticks(v[0], v[1])), Create(ticks(v[1], v[2])),
                  Create(ticks(v[2], v[0])), run_time=0.9)
        self.wait(max(d - 2.3, 0.2))
        self.clear_all()

    # ── 3. الإنشاء بالمدور (3-4-5) ثم الارتفاع ──────────────────
    def s_construction(self):
        d = self.seg("cons1")
        head = titled("أنشئ مثلثًا بالمسطرة والمدور", 38, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        B = np.array([2.25, -1.4, 0.0])     # ب à droite (RTL)
        J = np.array([-2.25, -1.4, 0.0])    # ج à gauche
        A = np.array([0.63, 0.76, 0.0])     # tracé 3-4-5 (base 5)
        base = Line(B, J, color=INK, stroke_width=5)
        lab_b = ar("ب", 30, "BOLD", BLUE).next_to(B, DOWN + RIGHT, buff=0.12)
        lab_j = ar("ج", 30, "BOLD", BLUE).next_to(J, DOWN + LEFT, buff=0.12)
        lab5 = num("5 cm", 34, GOLD).next_to(base, DOWN, buff=0.3)
        self.sfx("whoosh")
        self.play(Create(base), run_time=1.1)
        self.sfx("pop")
        self.play(FadeIn(lab_b), FadeIn(lab_j), FadeIn(lab5), run_time=0.8)
        self.wait(max(d - 2.8, 0.2))

        d = self.seg("cons2")
        arc_b = Arc(radius=2.7, arc_center=B, start_angle=108 * DEGREES,
                    angle=38 * DEGREES, color=REDA, stroke_width=4)
        r_b = num("3 cm", 26, REDA).move_to(B + np.array([-1.0, 0.9, 0]))
        self.sfx("whoosh")
        self.play(Create(arc_b), FadeIn(r_b), run_time=1.2)
        self.wait(1.4)
        arc_j = Arc(radius=3.6, arc_center=J, start_angle=18 * DEGREES,
                    angle=38 * DEGREES, color=GREEN, stroke_width=4)
        r_j = num("4 cm", 26, GREEN).move_to(J + np.array([1.7, 0.5, 0]))
        self.sfx("whoosh")
        self.play(Create(arc_j), FadeIn(r_j), run_time=1.2)
        self.wait(1.6)
        pA = Dot(A, radius=0.11, color=GOLD)
        lab_a = ar("أ", 30, "BOLD", GOLD).next_to(pA, UP, buff=0.15)
        self.sfx("ding")
        self.play(FadeIn(pA, scale=0.3, rate_func=BOUNCE), FadeIn(lab_a), run_time=0.8)
        c1 = Line(A, B, color=INK, stroke_width=5)
        c2 = Line(A, J, color=INK, stroke_width=5)
        self.sfx("pop")
        self.play(Create(c1), Create(c2), FadeOut(r_b), FadeOut(r_j), run_time=1.2)
        self.wait(max(d - 7.4, 0.2))

        # haut1 : الارتفاع en pointillés + زاوية قائمة عند القدم
        d = self.seg("haut1")
        F = np.array([A[0], -1.4, 0.0])
        h = DashedLine(A, F, color=BLUE, stroke_width=5, dash_length=0.18)
        self.sfx("whoosh")
        self.play(FadeOut(arc_b), FadeOut(arc_j), Create(h), run_time=1.2)
        ra = RightAngle(Line(F, B), Line(F, A), length=0.3, color=REDA, stroke_width=4)
        lab_h = ar("الارتفاع", 28, "BOLD", BLUE).next_to(h, RIGHT, buff=0.3).shift(UP * 0.3)
        self.sfx("ding")
        self.play(Create(ra), FadeIn(lab_h, shift=LEFT * 0.3), run_time=1.0)
        lab_q = ar("القاعدة", 28, "BOLD", GOLD).next_to(lab5, DOWN, buff=0.15)
        self.play(FadeIn(lab_q), Indicate(base, color=GOLD, scale_factor=1.05), run_time=1.0)
        self.wait(max(d - 3.2, 0.2))
        self.clear_all()

    # ── 4. المساحة : القاعدة × الارتفاع ÷ 2 على مثال 6 × 4 ─────
    def s_aire(self):
        d = self.seg("aire1")
        head = titled("مساحة المثلث", 44, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        formule = ar("المساحة = القاعدة × الارتفاع ÷ 2", 40, "BOLD", GREEN).move_to(UP * 0.9)
        box = SurroundingRectangle(formule, color=GREEN, corner_radius=0.18, buff=0.3)
        self.sfx("ding")
        self.play(Write(formule), run_time=1.6)
        self.play(Create(box), run_time=0.8)
        self.wait(max(d - 3.3, 0.2))

        d = self.seg("aire2")
        # triangle 6 × 4 à droite (RTL), calculs à gauche
        B = np.array([5.9, -2.5, 0.0]); J = np.array([2.3, -2.5, 0.0])
        A = np.array([3.5, -0.1, 0.0]); F = np.array([3.5, -2.5, 0.0])
        t = tri([tuple(B), tuple(J), tuple(A)], ROSE)
        b_lab = num("6 cm", 30, GOLD).next_to(Line(B, J), DOWN, buff=0.2)
        h = DashedLine(A, F, color=BLUE, stroke_width=4.5, dash_length=0.16)
        h_lab = num("4 cm", 30, BLUE).next_to(h, RIGHT, buff=0.18).shift(UP * 0.2)
        self.sfx("pop")
        self.play(Create(t), FadeIn(b_lab), run_time=1.1)
        self.sfx("whoosh")
        self.play(Create(h), FadeIn(h_lab), run_time=0.9)
        self.wait(1.8)
        c1 = num("6 × 4 = 24", 42).move_to(LEFT * 3.4 + DOWN * 1.1)
        self.sfx("pop")
        self.play(Write(c1), run_time=1.2)
        self.wait(1.6)
        c2 = num("24 ÷ 2 = 12 cm²", 42, GREEN).move_to(LEFT * 3.4 + DOWN * 2.3)
        self.sfx("ding")
        self.play(Write(c2), run_time=1.2)
        self.play(Flash(c2, color=GREEN, flash_radius=2.4), run_time=0.9)
        self.wait(max(d - 8.7, 0.2))
        self.clear_all()

    # ── 5. انتبه : لا تنسَ ÷ 2 ──────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! لا تنسَ القسمة على 2", 38, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        part = ar("القاعدة × الارتفاع", 36, "BOLD").move_to(RIGHT * 2.6 + UP * 0.3)
        div2 = num("÷ 2", 46, REDA).next_to(part, LEFT, buff=0.4)
        self.sfx("pop")
        self.play(Write(part), run_time=1.2)
        self.sfx("boing")
        self.play(FadeIn(div2, scale=0.4, rate_func=BOUNCE), run_time=0.9)
        self.play(Circumscribe(div2, color=REDA, buff=0.18), run_time=1.0)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 5.2, 0.2))
        self.clear_all()

    # ── 6. السر : رسم تقريبي وأبدأ بأطول ضلع ────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي قبل الإنشاء", 40, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.0)
        B = np.array([4.6, -1.9, 0.0]); J = np.array([0.8, -1.9, 0.0])
        A = np.array([1.9, 0.4, 0.0])
        sketch = DashedVMobject(tri([tuple(B), tuple(J), tuple(A)], LILA, 0.18),
                                num_dashes=42)
        l5 = num("5", 30, GOLD).next_to(Line(B, J), DOWN, buff=0.2)
        l3 = num("3", 30, INK).move_to((B + A) / 2 + np.array([0.45, 0.1, 0]))
        l4 = num("4", 30, INK).move_to((J + A) / 2 + np.array([-0.45, 0.1, 0]))
        self.sfx("pop")
        self.play(Create(sketch), run_time=1.3)
        self.play(FadeIn(l5), FadeIn(l3), FadeIn(l4), run_time=0.8)
        self.wait(1.5)
        longest = Line(B, J, color=GOLD, stroke_width=8)
        morale = ar("أبدأ دائمًا بأطول ضلع!", 32, "BOLD", LILA).move_to(LEFT * 3.6 + DOWN * 0.8)
        self.sfx("ding")
        self.play(Create(longest), Write(morale), run_time=1.4)
        self.play(Indicate(longest, color=GOLD, scale_factor=1.1), run_time=0.9)
        self.wait(max(d - 6.9, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أتعرّف أنواع المثلثات وأنشئها",
            "أرسم ارتفاع المثلث",
            "أحسب المساحة بالقاعدة والارتفاع",
        ])
        self.s_types()
        self.s_construction()
        self.s_aire()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
