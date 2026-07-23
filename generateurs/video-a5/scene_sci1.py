# -*- coding: utf-8 -*-
"""Vidéo Sciences 1 — التوازن الغذائي — VERSION CARTOON.
Rendu : venv/bin/manim -qh scene_sci1.py VideoSci1
Style dessin animé : la pomme TOMBE et rebondit, le verre de lait SE REMPLIT,
le soleil SE LÈVE pour l'إفطار et la lune pour le عشاء, l'assiette TOURNE,
la plante POUSSE, la vapeur MONTE du plat — un maximum d'images, un minimum de texte."""
import numpy as np
from manim import (VGroup, Rectangle, RoundedRectangle, Circle, Ellipse, Polygon,
                   AnnularSector, SurroundingRectangle, Dot, Line, Arc,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter, GrowFromEdge,
                   Rotate, Flash, Indicate, Wiggle, LaggedStart,
                   UP, DOWN, LEFT, RIGHT, DEGREES, PI, rate_functions as rf)

from video_common import (MajorScene, ar, num, titled, chip, BG,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)

DROP = rf.ease_out_bounce      # chute cartoon : rebondit à l'arrivée


# ─── mini-dessins « cartoon » (formes pures, zéro texte) ───────────────
def apple(s=1.0):
    return VGroup(
        Circle(radius=0.42 * s, fill_color=REDA, fill_opacity=0.95,
               stroke_color=INK, stroke_width=2.5),
        Line([0, 0.36 * s, 0], [0.09 * s, 0.62 * s, 0], color="#6b4a2b", stroke_width=4),
        Ellipse(width=0.3 * s, height=0.16 * s, fill_color=GREEN, fill_opacity=1,
                stroke_width=0).move_to([0.2 * s, 0.55 * s, 0]),
    )


def galette(s=1.0):
    return VGroup(
        Ellipse(width=0.85 * s, height=0.5 * s, fill_color=YELL, fill_opacity=0.95,
                stroke_color=INK, stroke_width=2.5),
        *[Dot([x * s, y * s, 0], radius=0.035 * s, color=GOLD)
          for x, y in [(-0.2, 0.06), (0.05, -0.08), (0.22, 0.05)]],
    )


def bottle(s=1.0, fill=BLUE):
    return VGroup(
        RoundedRectangle(corner_radius=0.08 * s, width=0.45 * s, height=0.75 * s,
                         fill_color=fill, fill_opacity=0.5, stroke_color=INK,
                         stroke_width=2.5),
        Rectangle(width=0.2 * s, height=0.18 * s, fill_color=fill, fill_opacity=0.95,
                  stroke_color=INK, stroke_width=2).shift(UP * 0.46 * s),
    )


def fish(s=1.0, col=ROSE):
    return VGroup(
        Ellipse(width=0.8 * s, height=0.42 * s, fill_color=col, fill_opacity=0.9,
                stroke_color=INK, stroke_width=2.5),
        Polygon([0.35 * s, 0, 0], [0.62 * s, 0.2 * s, 0], [0.62 * s, -0.2 * s, 0],
                fill_color=col, fill_opacity=0.9, stroke_color=INK, stroke_width=2.5),
        Dot([-0.22 * s, 0.05 * s, 0], radius=0.04 * s, color=INK),
    )


def oildrop(s=1.0):
    return VGroup(
        Circle(radius=0.28 * s, fill_color=LILA, fill_opacity=0.85,
               stroke_color=INK, stroke_width=2.5),
        Polygon([-0.18 * s, 0.2 * s, 0], [0.18 * s, 0.2 * s, 0], [0, 0.62 * s, 0],
                fill_color=LILA, fill_opacity=0.85, stroke_color=INK, stroke_width=2.5),
    )


def candy(s=1.0):
    return VGroup(
        Circle(radius=0.24 * s, fill_color=GOLD, fill_opacity=0.95,
               stroke_color=INK, stroke_width=2.5),
        Polygon([0.22 * s, 0.1 * s, 0], [0.48 * s, 0.22 * s, 0], [0.48 * s, -0.02 * s, 0],
                fill_color=GOLD, fill_opacity=0.95, stroke_color=INK, stroke_width=2),
        Polygon([-0.22 * s, -0.1 * s, 0], [-0.48 * s, 0.02 * s, 0],
                [-0.48 * s, -0.22 * s, 0],
                fill_color=GOLD, fill_opacity=0.95, stroke_color=INK, stroke_width=2),
    )


def sun(s=1.0):
    rays = VGroup(*[Line([0.55 * s * np.cos(a), 0.55 * s * np.sin(a), 0],
                         [0.78 * s * np.cos(a), 0.78 * s * np.sin(a), 0],
                         color=GOLD, stroke_width=4)
                    for a in np.linspace(0, 2 * PI, 8, endpoint=False)])
    return VGroup(Circle(radius=0.42 * s, fill_color=YELL, fill_opacity=1,
                         stroke_color=GOLD, stroke_width=3), rays)


def moon(s=1.0):
    return VGroup(
        Circle(radius=0.42 * s, fill_color=LILA, fill_opacity=0.9,
               stroke_color=INK, stroke_width=2.5),
        Circle(radius=0.36 * s, fill_color=BG, fill_opacity=1,
               stroke_width=0).shift(RIGHT * 0.22 * s + UP * 0.08 * s),
    )


def lightning(s=1.0):
    return Polygon([0, 0.55 * s, 0], [-0.28 * s, 0, 0], [-0.05 * s, 0, 0],
                   [-0.22 * s, -0.55 * s, 0], [0.3 * s, 0.08 * s, 0], [0.07 * s, 0.08 * s, 0],
                   fill_color=YELL, fill_opacity=1, stroke_color=GOLD, stroke_width=3)


def plant(s=1.0):
    stem = Line([0, -0.5 * s, 0], [0, 0.35 * s, 0], color="#2b6e3a", stroke_width=5)
    return VGroup(stem,
                  Ellipse(width=0.4 * s, height=0.2 * s, fill_color=GREEN, fill_opacity=1,
                          stroke_width=0).move_to([-0.2 * s, 0.05 * s, 0]).rotate(0.5),
                  Ellipse(width=0.4 * s, height=0.2 * s, fill_color=GREEN, fill_opacity=1,
                          stroke_width=0).move_to([0.2 * s, 0.2 * s, 0]).rotate(-0.5),
                  Circle(radius=0.16 * s, fill_color=ROSE, fill_opacity=1,
                         stroke_color=INK, stroke_width=2).move_to([0, 0.45 * s, 0]))


def shield(s=1.0, col=GREEN):
    return VGroup(
        Polygon([-0.42 * s, 0.45 * s, 0], [0.42 * s, 0.45 * s, 0], [0.42 * s, -0.05 * s, 0],
                [0, -0.55 * s, 0], [-0.42 * s, -0.05 * s, 0],
                fill_color=col, fill_opacity=0.9, stroke_color=INK, stroke_width=3),
        Line([-0.16 * s, 0.02 * s, 0], [-0.03 * s, -0.16 * s, 0], color="#FFFFFF",
             stroke_width=5),
        Line([-0.03 * s, -0.16 * s, 0], [0.2 * s, 0.18 * s, 0], color="#FFFFFF",
             stroke_width=5),
    )


def plate_full(radius=1.55):
    """صحن متوازن : disque en 4 secteurs proportionnés."""
    specs = [(140, YELL), (120, GREEN), (70, ROSE), (30, LILA)]
    g = VGroup()
    start = 90
    for ang, col in specs:
        g.add(AnnularSector(inner_radius=0, outer_radius=radius, angle=ang * DEGREES,
                            start_angle=start * DEGREES, fill_color=col, fill_opacity=0.9,
                            stroke_color=INK, stroke_width=2.5))
        start += ang
    g.add(Circle(radius=radius + 0.08, stroke_color=INK, stroke_width=3).set_fill(opacity=0))
    return g


def food_card(label, col, icon, w=3.9, h=1.05):
    box = RoundedRectangle(corner_radius=0.18, width=w, height=h,
                           fill_color="#FFFFFF", fill_opacity=1,
                           stroke_color=col, stroke_width=3)
    ic = icon.scale(0.75).move_to(box.get_right() + LEFT * 0.55)
    t = ar(label, 24, "BOLD", INK)
    avail = w - 1.35
    if t.width > avail:
        t.scale_to_fit_width(avail)
    t.move_to(box.get_center() + LEFT * 0.4)
    return VGroup(box, ic, t)


class VideoSci1(MajorScene):
    AUDIO = HERE / "audio_sci1"
    UNIT_AR = "علوم · درس 1"
    UNIT_COLOR = GREEN
    TITLE = "التوازن الغذائي"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين التوازن الغذائي"

    # ── 2. التعريف : les aliments défilent autour de l'enfant ──
    def s_def(self):
        d = self.seg("def1")
        head = titled("ما هو التوازن الغذائي؟", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        kid = self.boy(2.2).move_to([0, -1.6, 0])
        self.sfx("pop")
        self.play(FadeIn(kid, scale=0.3, rate_func=BOUNCE), run_time=0.8)
        # les aliments tombent du ciel autour de lui, un par un
        foods = [apple(0.9).move_to([-3.4, 4.2, 0]), galette(1.1).move_to([-1.7, 4.4, 0]),
                 bottle(1.1).move_to([1.7, 4.3, 0]), fish(0.95).move_to([3.4, 4.2, 0])]
        targets = [[-3.4, 0.5, 0], [-1.7, 0.9, 0], [1.7, 0.8, 0], [3.4, 0.5, 0]]
        for f, tg in zip(foods, targets):
            self.add(f)
            self.sfx("boing")
            self.play(f.animate.move_to(tg), run_time=0.8, rate_func=DROP)
        t = ar("أطعمة متنوعة بكميات مناسبة", 30, "BOLD", GREEN).move_to(UP * 1.9)
        self.sfx("ding")
        self.play(Write(t), Wiggle(kid), run_time=1.4)
        self.wait(max(d - 6.3, 0.2))
        self.clear_all()

    # ── 3. المجموعات الست : cartes illustrées qui sautent ──────
    def s_groupes(self):
        d = self.seg("grp1")
        head = titled("المجموعات الغذائية الست", 34, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        groups = [("الفواكه والخضروات", GREEN, apple(0.9)),
                  ("النشويات", YELL, galette(1.0)),
                  ("منتجات الألبان", BLUE, bottle(1.0)),
                  ("اللحوم والأسماك والبيض", ROSE, fish(0.9)),
                  ("الدهون", LILA, oildrop(0.9)),
                  ("المنتجات السكرية", GOLD, candy(0.9))]
        cards = VGroup()
        for i, (lab, col, ic) in enumerate(groups):
            row, coln = divmod(i, 3)
            c = food_card(lab, col, ic).move_to([4.15 - coln * 4.15, 0.55 - row * 1.45, 0])
            cards.add(c)
        t = 0
        for c in cards:
            self.sfx("pop")
            self.play(FadeIn(c, shift=DOWN * 0.6, scale=0.6, rate_func=BOUNCE), run_time=0.55)
            t += 0.55
        # les dessins gigotent tous ensemble : ça vit !
        self.play(LaggedStart(*[Wiggle(c[1]) for c in cards], lag_ratio=0.12), run_time=2.2)
        self.wait(max(d - t - 3.1, 0.2))
        self.clear_all()

    # ── 4. الأدوار : éclair, plante qui pousse, bouclier ───────
    def s_roles(self):
        d = self.seg("role1")
        head = titled("لكل مجموعة دورها", 36, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # 3 podiums : الطاقة (éclair) · النمو (plante qui pousse) · الحماية (bouclier)
        spots = [3.7, 0, -3.7]
        labels = [("الطاقة", YELL), ("النمو", ROSE), ("حماية الجسم", GREEN)]
        pods = VGroup()
        for x, (lab, col) in zip(spots, labels):
            p = RoundedRectangle(corner_radius=0.2, width=3.2, height=0.8,
                                 fill_color=col, fill_opacity=0.92,
                                 stroke_color=INK, stroke_width=2.5).move_to([x, -1.9, 0])
            pt = ar(lab, 26, "BOLD", "#FFFFFF").move_to(p)
            if pt.width > 2.7:
                pt.scale_to_fit_width(2.7)
            pods.add(VGroup(p, pt))
        # l'éclair frappe
        z = lightning(1.5).move_to([3.7, 0.1, 0])
        self.sfx("ding")
        self.play(GrowFromCenter(pods[0], rate_func=BOUNCE),
                  FadeIn(z, scale=1.8), run_time=0.8)
        self.play(Flash(z, color=YELL, flash_radius=1.3), run_time=0.5)
        # la plante pousse depuis le sol
        pl = plant(1.6).move_to([0, 0.1, 0])
        self.sfx("pop")
        self.play(GrowFromCenter(pods[1], rate_func=BOUNCE),
                  GrowFromEdge(pl, DOWN), run_time=1.1)
        # le bouclier arrive en tournant
        sh = shield(1.4).move_to([-3.7, 0.1, 0])
        self.sfx("ding")
        self.play(GrowFromCenter(pods[2], rate_func=BOUNCE),
                  FadeIn(sh, scale=0.3, rate_func=BOUNCE), run_time=0.9)
        self.play(Indicate(sh, color=GREEN), run_time=0.7)
        self.wait(max(d - 4.9, 0.2))
        self.clear_all()

    # ── 5. الصحن : il tourne comme une toupie puis se pose ─────
    def s_plate(self):
        d = self.seg("plate1")
        head = titled("صحني المتوازن", 36, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        pl = plate_full(1.6).move_to([3.0, -0.5, 0])
        self.sfx("whoosh")
        self.play(Create(pl), run_time=1.2)
        self.play(Rotate(pl, angle=-2 * PI, about_point=pl.get_center()),
                  run_time=1.6, rate_func=rf.ease_out_quad)
        legend = [("خضروات وفواكه — الحماية", GREEN, 1),
                  ("نشويات — الطاقة", YELL, 0),
                  ("بروتينات — النمو", ROSE, 2),
                  ("قليل جدًا من السكر", LILA, 3)]
        t = 0
        for i, (lab, col, sector) in enumerate(legend):
            dot = Circle(radius=0.16, fill_color=col, fill_opacity=1,
                         stroke_color=INK, stroke_width=1.5)
            txt = ar(lab, 24, "BOLD", INK)
            r = VGroup(txt, dot.next_to(txt, RIGHT, buff=0.3)).move_to([-2.6, 0.9 - i * 0.85, 0])
            self.sfx("pop")
            # la part du plat gonfle quand on la nomme
            self.play(FadeIn(r, shift=LEFT * 0.3, rate_func=BOUNCE),
                      Indicate(pl[sector], color=col, scale_factor=1.15), run_time=0.75)
            t += 0.75
        self.wait(max(d - t - 3.7, 0.2))
        self.clear_all()

    # ── 6. الوجبات : le soleil se lève, passe, la lune arrive ──
    def s_meals(self):
        d = self.seg("meal1")
        head = titled("ثلاث وجبات في اليوم", 36, YELL)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        horizon = Line([-6.5, -0.6, 0], [6.5, -0.6, 0], color=GOLD, stroke_width=3)
        self.play(Create(horizon), run_time=0.5)
        meals = [("الإفطار", YELL, sun(0.9), [4.3, 0.6, 0]),
                 ("الغداء", ROSE, sun(1.05), [0, 1.6, 0]),
                 ("العشاء", BLUE, moon(0.9), [-4.3, 0.6, 0])]
        t = 0
        for lab, col, astre, pos in meals:
            astre.move_to([pos[0], -1.6, 0])          # part sous l'horizon…
            card = RoundedRectangle(corner_radius=0.22, width=2.9, height=0.85,
                                    fill_color=col, fill_opacity=0.92,
                                    stroke_color=INK, stroke_width=2.5).move_to([pos[0], -1.7, 0])
            ct = ar(lab, 26, "BOLD", "#FFFFFF").move_to(card)
            self.add(astre)
            self.sfx("whoosh")
            self.play(astre.animate.move_to(pos), run_time=0.9,
                      rate_func=rf.ease_out_back)   # …et se lève !
            self.sfx("pop")
            self.play(GrowFromCenter(VGroup(card, ct), rate_func=BOUNCE), run_time=0.5)
            t += 1.4
        drop = VGroup(
            Circle(radius=0.32, fill_color=BLUE, fill_opacity=0.7, stroke_color=INK,
                   stroke_width=2.5),
            Polygon([-0.2, 0.24, 0], [0.2, 0.24, 0], [0, 0.7, 0],
                    fill_color=BLUE, fill_opacity=0.7, stroke_color=INK, stroke_width=2.5),
        ).move_to([0, 4.2, 0])
        wt = ar("+ الماء الكافي", 26, "BOLD", BLUE).move_to([0, -3.1, 0])
        self.add(drop)
        self.sfx("boing")
        self.play(drop.animate.move_to([0, -0.1, 0]), run_time=0.9, rate_func=DROP)
        self.play(FadeIn(wt, shift=UP * 0.2), run_time=0.5)
        self.wait(max(d - t - 2.8, 0.2))
        self.clear_all()

    # ── 7. مثال : la pomme tombe, le verre se remplit ──────────
    def s_example(self):
        d = self.seg("ex1")
        head = titled("مثال محلول: طاقة وجبة خفيفة", 32, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # la pomme TOMBE du haut et rebondit
        ap = apple(1.7).move_to([-3.6, 4.3, 0])
        self.add(ap)
        self.sfx("boing")
        self.play(ap.animate.move_to([-3.6, 0.6, 0]), run_time=1.0, rate_func=DROP)
        a_val = VGroup(num("80", 40, REDA), ar("سعرة", 24, "BOLD", REDA)
                       ).arrange(LEFT, buff=0.25).next_to(ap, DOWN, buff=0.4)
        self.sfx("pop")
        self.play(FadeIn(a_val, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.6)
        # le verre de lait SE REMPLIT sous nos yeux
        glass = VGroup(
            Line([-1.15, 1.5, 0], [-1.05, -0.3, 0], color=INK, stroke_width=3.5),
            Line([-0.05, 1.5, 0], [-0.15, -0.3, 0], color=INK, stroke_width=3.5),
            Line([-1.05, -0.3, 0], [-0.15, -0.3, 0], color=INK, stroke_width=3.5),
        ).shift(RIGHT * 0.1)
        milk = Rectangle(width=0.85, height=0.05, fill_color="#DCEBFF", fill_opacity=1,
                         stroke_color="#b9cfe8", stroke_width=1.5).move_to([-0.6, -0.25, 0])
        self.play(Create(glass), run_time=0.7)
        self.add(milk)
        self.sfx("whoosh")
        self.play(milk.animate.stretch_to_fit_height(1.55).move_to([-0.6, 0.5, 0]),
                  run_time=1.3, rate_func=rf.ease_in_out_sine)
        m_val = VGroup(num("150", 40, BLUE), ar("سعرة", 24, "BOLD", BLUE)
                       ).arrange(LEFT, buff=0.25).move_to([-0.6, -1.1, 0])
        self.sfx("pop")
        self.play(FadeIn(m_val, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.6)
        self.wait(max(d - 5.1, 0.2))

        d = self.seg("ex2")
        # les nombres SAUTENT dans le calcul un par un
        calc = VGroup(num("80", 42), num("+", 34, GOLD), num("150", 42),
                      num("=", 38), num("230", 54, GREEN)).arrange(LEFT, buff=0.3)
        unit = ar("سعرة حرارية", 28, "BOLD", GREEN)
        row = VGroup(calc, unit).arrange(LEFT, buff=0.4).move_to([0.6, -2.1, 0])
        box = SurroundingRectangle(row, color=GREEN, corner_radius=0.15, buff=0.25)
        self.sfx("ding")
        self.play(LaggedStart(*[FadeIn(m, shift=DOWN * 0.5, scale=0.5, rate_func=BOUNCE)
                                for m in [*calc, unit]], lag_ratio=0.15), run_time=1.6)
        self.play(Create(box), run_time=0.6)
        self.play(Flash(calc[4], color=GREEN, flash_radius=1.2), run_time=0.7)
        kid = self.boy(1.8).to_corner(DOWN + RIGHT, buff=0.3)
        tag = ar("وجبة خفيفة متوازنة!", 30, "BOLD", ROSE).move_to([0.6, -3.25, 0])
        self.sfx("tada")
        self.play(FadeIn(tag, scale=0.6, rate_func=BOUNCE),
                  FadeIn(kid, scale=0.3, rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(kid), run_time=1.0)
        self.wait(max(d - 4.8, 0.2))
        self.clear_all()

    # ── 8. انتبه ────────────────────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! لا تكفي مجموعة واحدة", 34, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=7.2, height=1.1, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.3 + UP * 0.5)
        c1t = ar("الخضروات وحدها لا تكفي", 27, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=7.2, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.3 + DOWN * 0.9)
        c2t = ar("الجسم يحتاج كل المجموعات معًا", 27, "BOLD", "#FFFFFF").move_to(c2)
        g1 = VGroup(c1, c1t)
        self.sfx("boing")
        self.play(GrowFromCenter(g1, rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(g1, scale_value=1.06, rotation_angle=0.02), run_time=0.8)  # elle tremble : c'est NON
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 4.7, 0.2))
        self.clear_all()

    # ── 9. سرّ المائدة : le plat fume, les bonus sautent dessus ─
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ من مائدتنا الموريتانية", 32, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # le grand plat de رز بالسمك : assiette + monticule + poisson dessus
        dish = VGroup(
            Ellipse(width=4.6, height=1.1, fill_color="#FFFFFF", fill_opacity=1,
                    stroke_color=INK, stroke_width=3),
            Arc(radius=1.55, angle=PI, fill_color=YELL, fill_opacity=0.95,
                stroke_color=INK, stroke_width=2.5).stretch_to_fit_height(1.1).shift(UP * 0.15),
            fish(1.3).shift(UP * 0.75),
        ).move_to([0, -0.4, 0])
        self.sfx("pop")
        self.play(FadeIn(dish, shift=UP * 0.8, scale=0.5, rate_func=BOUNCE), run_time=1.0)
        # la vapeur monte du plat (petits ronds qui s'élèvent et s'effacent)
        for _ in range(2):
            puffs = VGroup(*[Circle(radius=0.12 + 0.04 * i, stroke_color="#bbbbbb",
                                    stroke_width=3, fill_opacity=0)
                             .move_to([x, 0.6, 0])
                             for i, x in enumerate([-0.9, 0, 0.9])])
            self.play(LaggedStart(*[p.animate.shift(UP * 1.3).set_opacity(0)
                                    for p in puffs], lag_ratio=0.2), run_time=1.4)
            self.remove(puffs)
        lab = ar("الأرز بالسمك = نشويات + بروتينات", 28, "BOLD", INK).move_to([0, -2.4, 0])
        self.sfx("ding")
        self.play(Write(lab), run_time=1.0)
        # les bonus TOMBENT à côté du plat : légumes + lait
        ap2 = apple(0.9).move_to([3.9, 4.2, 0])
        bt2 = bottle(1.2).move_to([-3.9, 4.2, 0])
        self.add(ap2, bt2)
        self.sfx("boing")
        self.play(ap2.animate.move_to([3.9, -0.3, 0]), run_time=0.8, rate_func=DROP)
        self.sfx("boing")
        self.play(bt2.animate.move_to([-3.9, -0.3, 0]), run_time=0.8, rate_func=DROP)
        plus = ar("وجبة متوازنة!", 28, "BOLD", GREEN).move_to([0, -3.2, 0])
        self.sfx("tada")
        self.play(FadeIn(plus, scale=0.5, rate_func=BOUNCE), run_time=0.7)
        self.wait(max(d - 9.4, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أعرف المجموعات الغذائية الست",
            "أفهم دور كل مجموعة: طاقة ونمو وحماية",
            "أركّب وجبة متوازنة من مائدتنا",
        ])
        self.s_def()
        self.s_groupes()
        self.s_roles()
        self.s_plate()
        self.s_meals()
        self.s_example()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
