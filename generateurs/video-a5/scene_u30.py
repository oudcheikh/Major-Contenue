# -*- coding: utf-8 -*-
"""Vidéo U30 — الدائرة والقرص.  Rendu : venv/bin/manim -qh scene_u30.py VideoU30
Cœur de la vidéo : la Circle avec rayon tracé (Line + نصف القطر), le قطر qui traverse,
π ≈ 3,14 en vedette, المحيط = القطر × 3,14 puis 2 × نق × 3,14 construit pas à pas,
et le calcul du cahier animé : نق = 5 cm ← محيط 31,4 ← مساحة 78,5."""
from manim import (VGroup, Line, Dot, Circle, RoundedRectangle, SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter,
                   Indicate, Wiggle, Flash,
                   UP, DOWN, LEFT, RIGHT, DEGREES)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


class VideoU30(MajorScene):
    AUDIO = HERE / "audio_u30"
    UNIT_AR = "الوحدة 30"
    UNIT_COLOR = BLUE
    TITLE = "الدائرة والقرص"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 30"

    # ── aides ───────────────────────────────────────────────────
    def card(self, txt, size, fill, pos):
        t = ar(txt, size, "BOLD", "#FFFFFF")
        r = RoundedRectangle(corner_radius=0.22, width=t.width + 0.8, height=t.height + 0.55,
                             fill_color=fill, fill_opacity=0.92, stroke_color=INK, stroke_width=2)
        return VGroup(r, t).move_to(pos)

    # ── 2. الدائرة : المركز، نق، القطر ─────────────────────────
    def s_cercle(self):
        d = self.seg("def1")
        head = titled("أرسم الدائرة بالمدور", 40, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        circ = Circle(radius=1.8, stroke_color=BLUE, stroke_width=6).move_to(RIGHT * 3.2 + DOWN * 0.7)
        center = Dot(circ.get_center(), color=INK, radius=0.08)
        c_lab = ar("المركز", 26, "BOLD", GOLD).next_to(center, DOWN, buff=0.18)
        self.sfx("whoosh")
        self.play(Create(circ), run_time=1.6)
        self.sfx("pop")
        self.play(FadeIn(center, scale=0.3, rate_func=BOUNCE), FadeIn(c_lab), run_time=0.8)
        self.wait(max(d - 3.3, 0.2))                                        # somme = 3.3

        d = self.seg("def2")   # نصف القطر + tous égaux
        ray = Line(circ.get_center(), circ.point_at_angle(150 * DEGREES),
                   color=GREEN, stroke_width=7)
        r_lab = ar("نصف القطر (نق)", 28, "BOLD", GREEN)
        r_lab.next_to(circ, LEFT, buff=0.5).shift(UP * 1.1)
        self.sfx("whoosh")
        self.play(Create(ray), run_time=1.0)
        self.sfx("pop")
        self.play(FadeIn(r_lab, shift=LEFT * 0.3, rate_func=BOUNCE), run_time=0.8)
        ray2 = Line(circ.get_center(), circ.point_at_angle(60 * DEGREES),
                    color=GREEN, stroke_width=7)
        eq = ar("كلها متساوية!", 26, "BOLD", GREEN).next_to(r_lab, DOWN, buff=0.35)
        self.play(Create(ray2), FadeIn(eq), run_time=1.0)
        self.wait(max(d - 2.8, 0.2))                                        # somme = 2.8
        self.play(FadeOut(ray2), FadeOut(eq), run_time=0.4)

        d = self.seg("def3")   # القطر
        diam = Line(circ.point_at_angle(180 * DEGREES), circ.point_at_angle(0 * DEGREES),
                    color=ROSE, stroke_width=7)
        d_lab = ar("القطر", 28, "BOLD", ROSE).next_to(circ, DOWN, buff=0.3)
        self.sfx("whoosh")
        self.play(Create(diam), FadeIn(d_lab), run_time=1.1)
        form = ar("القطر = نق × 2", 34, "BOLD", ROSE).move_to(LEFT * 3.6 + DOWN * 0.9)
        fbox = SurroundingRectangle(form, color=ROSE, corner_radius=0.15, buff=0.25)
        self.sfx("ding")
        self.play(Write(form), Create(fbox), run_time=1.3)
        self.wait(max(d - 2.8, 0.2))                                        # somme = 0.4+2.4
        self.clear_all()

    # ── 3. العدد π en vedette ───────────────────────────────────
    def s_pi(self):
        d = self.seg("pi1")
        head = titled("نجم الدرس: العدد π", 40, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        big = num("π ≈ 3,14", 96, LILA).move_to(DOWN * 0.5)
        box = SurroundingRectangle(big, color=LILA, corner_radius=0.25, buff=0.4)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(big, box), rate_func=BOUNCE), run_time=1.1)
        self.play(Flash(big, color=LILA, flash_radius=3.2), run_time=0.9)
        self.wait(max(d - 2.9, 0.2))                                        # somme = 2.9
        self.clear_all()

    # ── 4. المحيط : القطر × 3,14 puis 2 × نق × 3,14 ────────────
    def s_perimetre(self):
        d = self.seg("per1")
        head = titled("محيط الدائرة", 42, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        circ = Circle(radius=1.1, stroke_color=GOLD, stroke_width=7).move_to(RIGHT * 4.4 + DOWN * 1.1)
        diam = Line(circ.point_at_angle(180 * DEGREES), circ.point_at_angle(0 * DEGREES),
                    color=ROSE, stroke_width=6)
        self.sfx("whoosh")
        self.play(Create(circ), Create(diam), run_time=1.2)
        c1 = self.card("المحيط = القطر × 3,14", 34, GOLD, UP * 0.8 + LEFT * 1.4)
        self.sfx("pop")
        self.play(GrowFromCenter(c1, rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 3.1, 0.2))                                        # somme = 3.1

        d = self.seg("per2")   # pas à pas : القطر = نق × 2 ← المحيط = 2 × نق × 3,14
        step = ar("القطر = نق × 2", 28, "BOLD", ROSE).move_to(DOWN * 0.5 + LEFT * 1.4)
        self.play(FadeIn(step, shift=UP * 0.2), run_time=0.9)
        self.wait(1.4)
        c2 = self.card("المحيط = 2 × نق × 3,14", 34, BLUE, DOWN * 1.8 + LEFT * 1.4)
        self.sfx("ding")
        self.play(GrowFromCenter(c2, rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 3.3, 0.2))                                        # somme = 3.3
        self.clear_all()

    # ── 5. مثال الكراس : نق = 5 cm ──────────────────────────────
    def s_exemple(self):
        d = self.seg("ex1")
        head = titled("مثال: دائرة نق = 5 cm", 38, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        circ = Circle(radius=1.4, stroke_color=BLUE, stroke_width=6).move_to(RIGHT * 3.9 + DOWN * 0.9)
        ray = Line(circ.get_center(), circ.point_at_angle(160 * DEGREES),
                   color=GREEN, stroke_width=6)
        r_val = num("5 cm", 28, GREEN).next_to(circ, UP, buff=0.2)
        self.sfx("whoosh")
        self.play(Create(circ), Create(ray), FadeIn(r_val), run_time=1.3)
        lab1 = ar("القطر:", 30, "BOLD", ROSE).move_to(LEFT * 0.2 + UP * 0.6)
        calc1 = num("5 × 2 = 10 cm", 44, ROSE).next_to(lab1, LEFT, buff=0.4)
        self.sfx("pop")
        self.play(FadeIn(lab1), Write(calc1), run_time=1.3)
        self.wait(max(d - 3.5, 0.2))                                        # somme = 3.5

        d = self.seg("ex2")   # المحيط = 31,4 cm
        lab2 = ar("المحيط:", 30, "BOLD", GREEN).move_to(LEFT * 0.2 + DOWN * 0.9)
        calc2 = num("10 × 3,14 = 31,4 cm", 44, GREEN).next_to(lab2, LEFT, buff=0.4)
        box = SurroundingRectangle(calc2, color=GREEN, corner_radius=0.15, buff=0.2)
        self.sfx("pop")
        self.play(FadeIn(lab2), Write(calc2), run_time=1.4)
        self.sfx("ding")
        self.play(Create(box), run_time=0.8)
        self.play(Flash(calc2, color=GREEN, flash_radius=2.8), run_time=0.9)
        self.wait(max(d - 3.1, 0.2))                                        # somme = 3.1
        self.clear_all()

    # ── 6. مساحة القرص ──────────────────────────────────────────
    def s_aire(self):
        d = self.seg("area1")
        head = titled("مساحة القرص", 42, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        disk = Circle(radius=1.4, stroke_color=INK, stroke_width=4,
                      fill_color=GREEN, fill_opacity=0.4).move_to(RIGHT * 3.9 + DOWN * 0.9)
        ray = Line(disk.get_center(), disk.point_at_angle(20 * DEGREES),
                   color=INK, stroke_width=5)
        r_lab = ar("نق", 26, "BOLD", INK).next_to(disk, UP, buff=0.2)
        self.sfx("whoosh")
        self.play(GrowFromCenter(disk), Create(ray), FadeIn(r_lab), run_time=1.3)
        c1 = self.card("المساحة = نق × نق × 3,14", 32, GREEN, UP * 0.6 + LEFT * 1.8)
        self.sfx("pop")
        self.play(GrowFromCenter(c1, rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 3.2, 0.2))                                        # somme = 3.2

        d = self.seg("ex3")   # 5 × 5 × 3,14 = 78,5 cm²
        calc = num("5 × 5 × 3,14 = 78,5 cm²", 44, GREEN).move_to(DOWN * 1.2 + LEFT * 1.5)
        box = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("pop")
        self.play(Write(calc), run_time=1.4)
        self.sfx("ding")
        self.play(Create(box), run_time=0.8)
        note = ar("وحدة مربعة!", 26, "BOLD", REDA).next_to(box, DOWN, buff=0.25)
        self.play(FadeIn(note, shift=UP * 0.2), Flash(calc, color=GREEN, flash_radius=3.0),
                  run_time=1.0)
        self.wait(max(d - 3.2, 0.2))                                        # somme = 3.2
        self.clear_all()

    # ── 7. انتبه : القطر ≠ نق ──────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! لا تأخذ القطر مكان نق", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = self.card("القطر = 10 cm", 30, ROSE, RIGHT * 2.9 + UP * 0.5)
        c2 = self.card("إذن نق = 5 cm فقط!", 30, GREEN, RIGHT * 2.9 + DOWN * 0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(c1, rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(c2, rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))                                        # somme = 3.9
        self.clear_all()

    # ── 8. السر ────────────────────────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي قبل أن نفترق", 40, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.2)
        c1 = self.card("المحيط ← القطر × 3,14", 30, GOLD, UP * 0.7)
        c2 = self.card("المساحة ← نق × نق × 3,14", 30, GREEN, DOWN * 0.6)
        self.sfx("pop")
        self.play(GrowFromCenter(c1, rate_func=BOUNCE), run_time=0.9)
        self.wait(1.2)
        self.sfx("pop")
        self.play(GrowFromCenter(c2, rate_func=BOUNCE), run_time=0.9)
        morale = ar("المحيط بـ cm والمساحة بـ cm² !", 30, "BOLD", LILA).move_to(DOWN * 2.0)
        self.sfx("ding")
        self.play(Write(morale), run_time=1.3)
        self.wait(max(d - 6.5, 0.2))                                        # somme = 6.5
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أميّز نصف القطر (نق) والقطر",
            "أحسب المحيط: القطر × 3,14",
            "أحسب مساحة القرص: نق × نق × 3,14",
        ])
        self.s_cercle()
        self.s_pi()
        self.s_perimetre()
        self.s_exemple()
        self.s_aire()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
