# -*- coding: utf-8 -*-
"""Vidéo U23 — السلم والخرائط.  Rendu : venv/bin/manim -qh scene_u23.py VideoU23
Cœur de la vidéo : le segment « sur la carte » (petit, 5 cm) et le même segment
« en réalité » (long, 150 km), le سلم 1/3 000 000 en frac(), conversion animée
dans les deux sens (× le مقام pour la réalité, ÷ le مقام pour le dessin)."""
from manim import (VGroup, Rectangle, RoundedRectangle, Line, Arrow, Circle,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter,
                   Indicate, Wiggle, Flash,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled, frac,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


def dot(x, y, color=REDA):
    return Circle(radius=0.08, fill_color=color, fill_opacity=1,
                  stroke_color=INK, stroke_width=1.5).move_to([x, y, 0])


def rtl_row(pieces, buff=0.35):
    """Aligne des morceaux de DROITE à GAUCHE (le 1er est le plus à droite)."""
    for i in range(1, len(pieces)):
        pieces[i].next_to(pieces[i - 1], LEFT, buff=buff)
    return VGroup(*pieces)


class VideoU23(MajorScene):
    AUDIO = HERE / "audio_u23"
    UNIT_AR = "الوحدة 23"
    UNIT_COLOR = GREEN
    TITLE = "السلم والخرائط"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 23"

    # ── 2. المفهوم : الحقيقة الكبيرة تصغر في ورقة ───────────────
    def s_concept(self):
        d = self.seg("def1")
        head = titled("بلاد شاسعة في ورقة صغيرة", 38, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # RTL : la réalité (grande) à droite, la carte (petite) à gauche
        real = Rectangle(width=3.8, height=2.7, fill_color=GREEN, fill_opacity=0.18,
                         stroke_color=INK, stroke_width=3).move_to(RIGHT * 3.4 + DOWN * 0.7)
        real_lab = ar("الحقيقة", 30, "BOLD", GREEN).next_to(real, DOWN, buff=0.3)
        carte = Rectangle(width=1.5, height=1.05, fill_color=BLUE, fill_opacity=0.25,
                          stroke_color=INK, stroke_width=3).move_to(LEFT * 3.4 + DOWN * 0.7)
        carte_lab = ar("الخريطة", 30, "BOLD", BLUE).next_to(carte, DOWN, buff=0.3)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(real, real_lab), rate_func=BOUNCE), run_time=1.1)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(carte, carte_lab), rate_func=BOUNCE), run_time=1.1)
        self.wait(max(d - 3.1, 0.2))

        d = self.seg("def2")   # السلم : la flèche qui rétrécit + le كسر
        arr = Arrow(real.get_left(), carte.get_right(), color=GOLD, stroke_width=6,
                    max_tip_length_to_length_ratio=0.12)
        self.sfx("whoosh")
        self.play(Create(arr), run_time=0.8)
        f = frac(1, 100, 44).move_to(DOWN * 1.8)
        f_lab = ar("السلم", 28, "BOLD", ROSE).next_to(f, RIGHT, buff=0.5)
        self.sfx("pop")
        self.play(FadeIn(f, scale=0.5, rate_func=BOUNCE), FadeIn(f_lab), run_time=1.0)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("def3")   # 1 cm sur le dessin = 100 cm = 1 m réel
        self.play(FadeOut(real), FadeOut(real_lab), FadeOut(carte), FadeOut(carte_lab),
                  FadeOut(arr), run_time=0.5)
        seg_p = Line(RIGHT * 4.4 + UP * 0.4, RIGHT * 3.9 + UP * 0.4, color=BLUE, stroke_width=7)
        lab_p = VGroup(num("1 cm", 34, BLUE), ar("على التصميم", 22)).arrange(DOWN, buff=0.15)
        lab_p.next_to(seg_p, DOWN, buff=0.3)
        self.sfx("pop")
        self.play(Create(seg_p), FadeIn(lab_p), run_time=0.9)
        arr2 = Arrow(RIGHT * 3.3 + UP * 0.4, RIGHT * 1.5 + UP * 0.4, color=GOLD, stroke_width=5,
                     max_tip_length_to_length_ratio=0.2)
        seg_r = Line(RIGHT * 0.9 + UP * 0.4, LEFT * 4.1 + UP * 0.4, color=GREEN, stroke_width=7)
        lab_r = VGroup(num("100 cm = 1 m", 34, GREEN), ar("في الحقيقة", 22)).arrange(DOWN, buff=0.15)
        lab_r.next_to(seg_r, DOWN, buff=0.3)
        self.sfx("whoosh")
        self.play(Create(arr2), run_time=0.6)
        self.sfx("ding")
        self.play(Create(seg_r), FadeIn(lab_r), run_time=1.0)
        self.wait(max(d - 3.0, 0.2))
        self.clear_all()

    # ── 3. من الخريطة إلى الحقيقة : 5 cm ← 150 km ───────────────
    def s_carte(self):
        d = self.seg("map1")
        head = titled("من الخريطة إلى الحقيقة", 40, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # petit segment « carte » : 5 cm entre les 2 villes
        seg_c = Line(RIGHT * 2.4 + UP * 1.4, RIGHT * 0.8 + UP * 1.4, color=BLUE, stroke_width=7)
        d1, d2 = dot(2.4, 1.4), dot(0.8, 1.4)
        v1 = ar("انواكشوط", 22, "BOLD").next_to(d1, DOWN, buff=0.25)
        v2 = ar("ابوتلميت", 22, "BOLD").next_to(d2, DOWN, buff=0.25)
        mes = num("5 cm", 36, BLUE).next_to(seg_c, UP, buff=0.25)
        self.sfx("pop")
        self.play(Create(seg_c), FadeIn(d1), FadeIn(d2), run_time=1.0)
        self.play(FadeIn(v1), FadeIn(v2), FadeIn(mes), run_time=0.8)
        f = frac("1", "3 000 000", 34).move_to(LEFT * 4.4 + UP * 1.3)
        f_lab = ar("السلم", 24, "BOLD", ROSE).next_to(f, UP, buff=0.25)
        self.sfx("pop")
        self.play(FadeIn(VGroup(f, f_lab), scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 3.6, 0.2))

        d = self.seg("map2")   # × le مقام
        hint = ar("أضرب في مقام السلم", 26, "BOLD", GOLD).move_to(RIGHT * 3.6 + DOWN * 0.2)
        self.sfx("whoosh")
        self.play(FadeIn(hint, shift=LEFT * 0.4), run_time=0.8)
        calc = num("5 × 3 000 000 = 15 000 000 cm", 40).move_to(DOWN * 1.1 + LEFT * 0.6)
        self.play(Write(calc), run_time=1.4)
        self.wait(max(d - 2.2, 0.2))

        d = self.seg("map3")   # le long segment réel : 150 km
        seg_r = Line(RIGHT * 2.9 + DOWN * 2.6, LEFT * 2.9 + DOWN * 2.6, color=GREEN, stroke_width=8)
        d3, d4 = dot(2.9, -2.6, GREEN), dot(-2.9, -2.6, GREEN)
        km = num("150 km", 44, GREEN).next_to(seg_r, UP, buff=0.2)
        self.sfx("ding")
        self.play(Create(seg_r), FadeIn(d3), FadeIn(d4), run_time=1.1)
        self.sfx("pop")
        self.play(FadeIn(km, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.8)
        self.play(Flash(km, color=GREEN, flash_radius=1.8), run_time=0.8)
        self.wait(max(d - 2.7, 0.2))
        self.clear_all()

    # ── 4. من الحقيقة إلى التصميم : 7 m ← 7 cm ──────────────────
    def s_inverse(self):
        d = self.seg("inv1")
        head = titled("والآن العكس: من الحقيقة إلى التصميم", 36, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        mur = Line(RIGHT * 3.0 + UP * 1.2, LEFT * 2.0 + UP * 1.2, color=GREEN, stroke_width=8)
        mur_lab = VGroup(num("7 m", 40, GREEN), ar("جدار في الحقيقة", 22)).arrange(DOWN, buff=0.15)
        mur_lab.next_to(mur, DOWN, buff=0.3)
        self.sfx("pop")
        self.play(Create(mur), FadeIn(mur_lab), run_time=1.1)
        f = frac(1, 100, 34).move_to(LEFT * 4.6 + UP * 1.0)
        self.sfx("pop")
        self.play(FadeIn(f, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 2.9, 0.2))

        d = self.seg("inv2")   # 7 m = 700 cm puis ÷ 100
        conv = num("7 m = 700 cm", 38).move_to(DOWN * 0.5 + RIGHT * 2.2)
        self.play(Write(conv), run_time=1.0)
        hint = ar("أقسم على المقام", 24, "BOLD", GOLD).move_to(DOWN * 0.5 + LEFT * 3.4)
        self.sfx("whoosh")
        self.play(FadeIn(hint, shift=LEFT * 0.3), run_time=0.7)
        calc = num("700 ÷ 100 = 7 cm", 44, ROSE).move_to(DOWN * 1.6)
        self.sfx("ding")
        self.play(Write(calc), run_time=1.2)
        petit = Line(RIGHT * 0.35 + DOWN * 2.7, LEFT * 0.35 + DOWN * 2.7,
                     color=ROSE, stroke_width=7)
        self.sfx("pop")
        self.play(Create(petit), run_time=0.6)
        self.wait(max(d - 3.5, 0.2))
        self.clear_all()

    # ── 5. القاعدة الذهبية : أضرب / أقسم ────────────────────────
    def s_regle(self):
        d = self.seg("regle1")
        c1 = RoundedRectangle(corner_radius=0.22, width=8.6, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(UP * 0.6)
        c1t = ar("من التصميم إلى الحقيقة ← أضرب في المقام", 28, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=8.6, height=1.1, fill_color=ROSE,
                              fill_opacity=0.92, stroke_color=INK).move_to(DOWN * 0.85)
        c2t = ar("من الحقيقة إلى التصميم ← أقسم على المقام", 28, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 1.8, 0.2))
        self.clear_all()

    # ── 6. انتبه : توحيد الوحدات ────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! وحّد الوحدتين قبل الحساب", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        box = RoundedRectangle(corner_radius=0.22, width=5.0, height=1.15, fill_color=REDA,
                               fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.4 + DOWN * 0.4)
        boxt = num("7 m = 700 cm", 40, "#FFFFFF").move_to(box)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(box, boxt), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.0, 0.2))
        self.clear_all()

    # ── 7. السر : كيف أجد السلم؟ ────────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: كيف أجد السلم؟", 38, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        pieces = [ar("السلم", 32, "BOLD", LILA),
                  num("=", 40),
                  ar("البعد على التصميم", 30, "BOLD", BLUE),
                  num("÷", 40, GOLD),
                  ar("البعد الحقيقي", 30, "BOLD", GREEN)]
        formule = rtl_row(pieces).move_to(UP * 0.6)
        for p in pieces:      # apparition de droite à gauche
            self.sfx("pop")
            self.play(FadeIn(p, shift=LEFT * 0.3, rate_func=BOUNCE), run_time=0.45)
        ex = num("5 cm ÷ 15 000 000 cm", 38).move_to(DOWN * 0.9)
        self.play(Write(ex), run_time=1.1)
        res = frac("1", "3 000 000", 36, GREEN).move_to(DOWN * 2.4)
        self.sfx("ding")
        self.play(FadeIn(res, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.play(Flash(res, color=GREEN, flash_radius=1.8), run_time=0.8)
        self.wait(max(d - 6.1, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أفهم معنى سلم الخريطة",
            "أحسب البعد الحقيقي من الخريطة وبالعكس",
            "أوحّد الوحدات قبل كل حساب",
        ])
        self.s_concept()
        self.s_carte()
        self.s_inverse()
        self.s_regle()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
