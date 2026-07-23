# -*- coding: utf-8 -*-
"""Vidéo U26 — الكتلة القائمة والصافية والفارغ.  Rendu : venv/bin/manim -qh scene_u26.py VideoU26
Cœur de la vidéo : le bocal de miel DESSINÉ (RoundedRectangle + gouttes) posé sur une
balance — plein = القائمة, on retire le miel = الفارغ, la formule se construit pas à pas
avec l'exemple chiffré du cahier (1,2 kg − 200 g = 1 000 g)."""
import random

from manim import (VGroup, Line, Arrow, Circle, Polygon, Rectangle, RoundedRectangle,
                   SurroundingRectangle, DashedLine,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter, Transform,
                   Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT, DR)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


def jar(width=1.9, height=2.3, drops=10, seed=7):
    """Bocal dessiné : corps + couvercle + gouttes de miel (retirables)."""
    body = RoundedRectangle(corner_radius=0.22, width=width, height=height,
                            fill_color="#FFFFFF", fill_opacity=0.92,
                            stroke_color=INK, stroke_width=4)
    lid = RoundedRectangle(corner_radius=0.08, width=width * 0.62, height=0.3,
                           fill_color=GOLD, fill_opacity=1,
                           stroke_color=INK, stroke_width=3)
    lid.next_to(body, UP, buff=0.02)
    rng = random.Random(seed)
    content = VGroup()
    for _ in range(drops):
        r = rng.uniform(0.13, 0.2)
        x = rng.uniform(-width / 2 + 0.3, width / 2 - 0.3)
        y = rng.uniform(-height / 2 + 0.28, height / 2 - 0.5)
        content.add(Circle(radius=r, fill_color=YELL, fill_opacity=1,
                           stroke_color=GOLD, stroke_width=2).move_to([x, y, 0]))
    return VGroup(body, lid, content)   # [0]=corps [1]=couvercle [2]=miel


def balance(width=2.6):
    """Petite balance : plateau + pied + socle + cadran."""
    plate = Line(LEFT * width / 2, RIGHT * width / 2, color=INK, stroke_width=6)
    foot = Polygon([-0.45, -0.85, 0], [0.45, -0.85, 0], [0, 0, 0],
                   fill_color="#B9B9B9", fill_opacity=1, stroke_color=INK, stroke_width=3)
    base = RoundedRectangle(corner_radius=0.08, width=1.7, height=0.28,
                            fill_color="#8E8E8E", fill_opacity=1,
                            stroke_color=INK, stroke_width=3)
    base.next_to(foot, DOWN, buff=0)
    dial = Circle(radius=0.3, fill_color="#FFFFFF", fill_opacity=1,
                  stroke_color=INK, stroke_width=3).move_to([0, -0.45, 0])
    needle = Line([0, -0.45, 0], [0.16, -0.28, 0], color=REDA, stroke_width=4)
    foot.shift(DOWN * 0.02)
    return VGroup(plate, foot, base, dial, needle)


def fbox(txt, color, width=None, size=30):
    t = ar(txt, size, "BOLD", "#FFFFFF")
    r = RoundedRectangle(corner_radius=0.2, width=(width or t.width + 0.7),
                         height=t.height + 0.5, fill_color=color, fill_opacity=0.95,
                         stroke_color=INK, stroke_width=2)
    t.move_to(r)
    return VGroup(r, t)


class VideoU26(MajorScene):
    AUDIO = HERE / "audio_u26"
    UNIT_AR = "الوحدة 26"
    UNIT_COLOR = BLUE
    TITLE = "الكتلة القائمة والصافية والفارغ"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 26"

    # ── 2. القارورة : المنتوج + الغلاف ─────────────────────────
    def s_jar(self):
        d = self.seg("jar1")
        head = titled("القارورة: منتوج + غلاف", 40, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.jar = jar().shift(RIGHT * 3.4 + DOWN * 0.6)
        self.sfx("pop")
        self.play(GrowFromCenter(self.jar, rate_func=BOUNCE), run_time=1.1)
        body, lid, honey = self.jar
        lab_p = ar("المنتوج: العسل", 30, "BOLD", GOLD).move_to(LEFT * 2.2 + UP * 0.3)
        a_p = Arrow(lab_p.get_right(), honey.get_left() + LEFT * 0.05, color=GOLD,
                    stroke_width=4, max_tip_length_to_length_ratio=0.12)
        self.sfx("ding")
        self.play(FadeIn(lab_p, shift=RIGHT * 0.3), Create(a_p), run_time=1.0)
        lab_g = ar("الغلاف: القارورة", 30, "BOLD", ROSE).move_to(LEFT * 2.2 + DOWN * 1.7)
        a_g = Arrow(lab_g.get_right(), body.get_corner(DR) + LEFT * 0.15 + UP * 0.15,
                    color=ROSE, stroke_width=4, max_tip_length_to_length_ratio=0.12)
        self.sfx("ding")
        self.play(FadeIn(lab_g, shift=RIGHT * 0.3), Create(a_g), run_time=1.0)
        self.wait(max(d - 4.0, 0.2))
        self.arrows = VGroup(lab_p, a_p, lab_g, a_g)

        # jar2 : القائمة = القارورة مملوءة
        d = self.seg("jar2")
        frame = SurroundingRectangle(self.jar, color=BLUE, corner_radius=0.2, buff=0.18)
        lab_q = ar("الكتلة القائمة", 32, "BOLD", BLUE).next_to(frame, DOWN, buff=0.25)
        self.sfx("ding")
        self.play(FadeOut(self.arrows), Create(frame), FadeIn(lab_q), run_time=1.1)
        self.play(Indicate(self.jar, color=BLUE, scale_factor=1.08), run_time=1.0)
        self.wait(max(d - 2.1, 0.2))

        # jar3 : الصافية (le miel) و الفارغ (bocal vide)
        d = self.seg("jar3")
        self.play(FadeOut(frame), FadeOut(lab_q), run_time=0.5)
        lab_s = ar("الكتلة الصافية", 30, "BOLD", GREEN).move_to(RIGHT * 3.4 + UP * 1.6)
        self.sfx("pop")
        self.play(FadeIn(lab_s, shift=DOWN * 0.2, rate_func=BOUNCE),
                  Indicate(honey, color=GREEN, scale_factor=1.15), run_time=1.2)
        empty = jar(drops=0).shift(LEFT * 3.6 + DOWN * 0.6)
        lab_f = ar("الفارغ", 30, "BOLD", ROSE).next_to(empty, UP, buff=0.3)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(empty, lab_f), rate_func=BOUNCE), run_time=1.1)
        self.wait(max(d - 2.8, 0.2))
        self.clear_all()

    # ── 3. القواعد الثلاث ───────────────────────────────────────
    def s_formules(self):
        d = self.seg("form1")
        head = titled("قواعد الكتلة الثلاث", 42, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # RTL : القائمة apparaît à droite, puis =, puis الصافية + الفارغ vers la gauche
        b_q = fbox("الكتلة القائمة", BLUE)
        b_s = fbox("الكتلة الصافية", GREEN)
        b_f = fbox("الفارغ", ROSE, width=2.2)
        eq = num("=", 48, GOLD)
        pl = num("+", 48, GOLD)
        row = VGroup(b_f, pl, b_s, eq, b_q).arrange(RIGHT, buff=0.4).move_to(UP * 0.7)
        self.sfx("pop")
        self.play(FadeIn(b_q, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        self.play(FadeIn(eq), run_time=0.4)
        self.sfx("pop")
        self.play(FadeIn(b_s, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        self.sfx("pop")
        self.play(FadeIn(pl), FadeIn(b_f, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 2.8, 0.2))

        d = self.seg("form2")
        r2 = ar("الكتلة الصافية = القائمة − الفارغ", 32, "BOLD", GREEN).move_to(DOWN * 0.9)
        r3 = ar("الفارغ = القائمة − الصافية", 32, "BOLD", ROSE).move_to(DOWN * 2.0)
        self.sfx("whoosh")
        self.play(Write(r2), run_time=1.3)
        self.sfx("whoosh")
        self.play(Write(r3), run_time=1.3)
        self.wait(max(d - 2.6, 0.2))
        self.clear_all()

    # ── 4. مثال العسل على الميزان : 1,2 kg − 200 g ─────────────
    def s_exemple(self):
        d = self.seg("ex1")
        head = titled("مثال: قارورة العسل", 40, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # bocal plein sur la balance (droite), bocal vide (gauche) — RTL
        bal = balance().shift(RIGHT * 3.4 + DOWN * 2.2)
        full = jar().shift(RIGHT * 3.4 + DOWN * 0.75)
        self.sfx("pop")
        self.play(FadeIn(bal), GrowFromCenter(full, rate_func=BOUNCE), run_time=1.2)
        w_full = num("1,2 kg", 40, BLUE).next_to(full, UP, buff=0.25)
        lab_q = ar("القائمة", 26, "BOLD", BLUE).next_to(w_full, LEFT, buff=0.35)
        self.sfx("ding")
        self.play(FadeIn(VGroup(w_full, lab_q), shift=UP * 0.2, rate_func=BOUNCE), run_time=0.9)
        empty = jar(drops=0).shift(LEFT * 3.6 + DOWN * 0.75)
        w_emp = num("200 g", 40, ROSE).next_to(empty, UP, buff=0.25)
        lab_f = ar("الفارغ", 26, "BOLD", ROSE).next_to(w_emp, LEFT, buff=0.35)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(empty, w_emp, lab_f), rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 4.0, 0.2))

        # ex2 : توحيد الوحدات
        d = self.seg("ex2")
        conv = num("1,2 kg = 1 200 g", 44, BLUE).move_to(DOWN * 0.3 + LEFT * 0.2)
        self.sfx("whoosh")
        self.play(Write(conv), run_time=1.4)
        self.play(Indicate(conv, color=GOLD, scale_factor=1.12), run_time=0.9)
        self.wait(max(d - 2.3, 0.2))

        # ex3 : on retire le miel du bocal → الطرح
        d = self.seg("ex3")
        honey = full[2]
        out = honey.copy().scale(0.9).next_to(empty, RIGHT, buff=0.6).shift(UP * 0.1)
        self.sfx("whoosh")
        self.play(Transform(honey, out), run_time=1.2)
        calc = num("1 200 − 200 = 1 000 g", 44, GREEN).move_to(DOWN * 1.6 + LEFT * 0.2)
        self.sfx("pop")
        self.play(Write(calc), FadeOut(conv), run_time=1.4)
        res = ar("الكتلة الصافية = كيلوغرام واحد", 30, "BOLD", GREEN).move_to(DOWN * 2.7 + LEFT * 0.2)
        frame = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.2)
        self.sfx("ding")
        self.play(Create(frame), FadeIn(res), run_time=1.0)
        self.play(Flash(calc, color=GREEN, flash_radius=2.6), run_time=0.9)
        self.wait(max(d - 4.5, 0.2))
        self.clear_all()

    # ── 5. انتبه : وحّد الوحدتين ────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! وحّد الوحدتين قبل الطرح", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        bad = num("5 kg − 500 g", 44, REDA).move_to(RIGHT * 2.6 + UP * 0.8)
        self.sfx("boing")
        self.play(FadeIn(bad, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        arr = num("↓", 40, GOLD).next_to(bad, DOWN, buff=0.25)
        good = num("5 000 g − 500 g = 4 500 g", 42, GREEN).next_to(arr, DOWN, buff=0.25)
        self.sfx("whoosh")
        self.play(FadeIn(arr), Write(good), run_time=1.6)
        self.sfx("ding")
        self.play(Flash(good, color=GREEN, flash_radius=2.6), Wiggle(garcon), run_time=1.2)
        self.wait(max(d - 4.7, 0.2))
        self.clear_all()

    # ── 6. السر : القائمة أكبر دائمًا من الصافية ────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي قبل أن نفترق", 40, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.2)
        b_q = Rectangle(width=5.6, height=0.85, fill_color=BLUE, fill_opacity=0.95,
                        stroke_color=INK, stroke_width=2.5).move_to(RIGHT * 0.9 + UP * 0.7)
        l_q = ar("الكتلة القائمة", 28, "BOLD", BLUE).next_to(b_q, RIGHT, buff=0.35)
        b_s = Rectangle(width=4.4, height=0.85, fill_color=GREEN, fill_opacity=0.95,
                        stroke_color=INK, stroke_width=2.5)
        b_s.move_to([b_q.get_right()[0] - 2.2, -0.55, 0])
        l_s = ar("الكتلة الصافية", 28, "BOLD", GREEN).next_to(b_s, RIGHT, buff=0.35)
        l_s.align_to(l_q, LEFT)
        self.sfx("pop")
        self.play(FadeIn(VGroup(b_q, l_q), shift=LEFT * 0.4, rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(FadeIn(VGroup(b_s, l_s), shift=LEFT * 0.4, rate_func=BOUNCE), run_time=0.9)
        morale = ar("القائمة أكبر دائمًا من الصافية!", 32, "BOLD", LILA).move_to(DOWN * 2.1)
        self.sfx("ding")
        self.play(Write(morale), run_time=1.4)
        self.play(Indicate(b_q, color=GOLD, scale_factor=1.06), run_time=0.9)
        self.wait(max(d - 6.3, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أميّز الكتلة القائمة والصافية والفارغ",
            "أستعمل العلاقات الثلاث بينها",
            "أوحّد الوحدات قبل الحساب",
        ])
        self.s_jar()
        self.s_formules()
        self.s_exemple()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
