# -*- coding: utf-8 -*-
"""Vidéo Sciences 2 — التوازن الطاقوي — VERSION CARTOON.
Rendu : venv/bin/manim -qh scene_sci2.py VideoSci2
Style dessin animé : l'assiette et le ballon TOMBENT et rebondissent, les aliments
GLISSENT dans le corps, la balance OSCILLE vraiment, l'aiguille de l'horloge TOURNE,
les nombres SAUTENT, les vignettes d'activités BONDISSENT — peu de texte, tout bouge."""
import numpy as np
from manim import (VGroup, Rectangle, RoundedRectangle, Circle, Ellipse, Polygon,
                   SurroundingRectangle, Dot, Line, Arc, Arrow,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter, GrowArrow,
                   Rotate, Flash, Indicate, Wiggle, LaggedStart,
                   UP, DOWN, LEFT, RIGHT, PI, DR, rate_functions as rf)

from video_common import (MajorScene, ar, num, titled, chip,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)

DROP = rf.ease_out_bounce      # chute cartoon : rebondit à l'arrivée


# ─── mini-dessins « cartoon » (formes pures, zéro texte) ───────────────
def galette(s=1.0):
    return VGroup(
        Ellipse(width=0.85 * s, height=0.5 * s, fill_color=YELL, fill_opacity=0.95,
                stroke_color=INK, stroke_width=2.5),
        *[Dot([x * s, y * s, 0], radius=0.035 * s, color=GOLD)
          for x, y in [(-0.2, 0.06), (0.05, -0.08), (0.22, 0.05)]],
    )


def apple(s=1.0):
    return VGroup(
        Circle(radius=0.42 * s, fill_color=REDA, fill_opacity=0.95,
               stroke_color=INK, stroke_width=2.5),
        Line([0, 0.36 * s, 0], [0.09 * s, 0.62 * s, 0], color="#6b4a2b", stroke_width=4),
        Ellipse(width=0.3 * s, height=0.16 * s, fill_color=GREEN, fill_opacity=1,
                stroke_width=0).move_to([0.2 * s, 0.55 * s, 0]),
    )


def bottle(s=1.0, fill=BLUE):
    return VGroup(
        RoundedRectangle(corner_radius=0.08 * s, width=0.45 * s, height=0.75 * s,
                         fill_color=fill, fill_opacity=0.5, stroke_color=INK,
                         stroke_width=2.5),
        Rectangle(width=0.2 * s, height=0.18 * s, fill_color=fill, fill_opacity=0.95,
                  stroke_color=INK, stroke_width=2).shift(UP * 0.46 * s),
    )


def lightning(s=1.0):
    return Polygon([0, 0.55 * s, 0], [-0.28 * s, 0, 0], [-0.05 * s, 0, 0],
                   [-0.22 * s, -0.55 * s, 0], [0.3 * s, 0.08 * s, 0], [0.07 * s, 0.08 * s, 0],
                   fill_color=YELL, fill_opacity=1, stroke_color=GOLD, stroke_width=3)


def football(s=1.0):
    penta = Polygon(*[[0.17 * s * np.cos(np.deg2rad(90 + k * 72)),
                       0.17 * s * np.sin(np.deg2rad(90 + k * 72)), 0] for k in range(5)],
                    fill_color=INK, fill_opacity=1, stroke_width=0)
    seams = VGroup(*[Line([0.17 * s * np.cos(a), 0.17 * s * np.sin(a), 0],
                          [0.4 * s * np.cos(a), 0.4 * s * np.sin(a), 0],
                          color=INK, stroke_width=2.5)
                     for a in np.deg2rad([90, 162, 234, 306, 18])])
    return VGroup(Circle(radius=0.44 * s, fill_color="#FFFFFF", fill_opacity=1,
                         stroke_color=INK, stroke_width=3), penta, seams)


def sweat(s=1.0):
    return VGroup(
        Circle(radius=0.16 * s, fill_color=BLUE, fill_opacity=0.85,
               stroke_color=INK, stroke_width=2),
        Polygon([-0.11 * s, 0.11 * s, 0], [0.11 * s, 0.11 * s, 0], [0, 0.4 * s, 0],
                fill_color=BLUE, fill_opacity=0.85, stroke_color=INK, stroke_width=2),
    )


def runner(s=1.0):
    body = VGroup(
        Circle(radius=0.17 * s, fill_color=ROSE, fill_opacity=0.9,
               stroke_color=INK, stroke_width=2.5).move_to([-0.08 * s, 0.62 * s, 0]),
        Line([-0.05 * s, 0.44 * s, 0], [0.05 * s, -0.05 * s, 0], color=INK, stroke_width=5),
        Line([-0.02 * s, 0.3 * s, 0], [-0.35 * s, 0.14 * s, 0], color=INK, stroke_width=4.5),
        Line([-0.02 * s, 0.3 * s, 0], [0.3 * s, 0.42 * s, 0], color=INK, stroke_width=4.5),
        Line([0.05 * s, -0.05 * s, 0], [-0.38 * s, -0.5 * s, 0], color=INK, stroke_width=5),
        Line([0.05 * s, -0.05 * s, 0], [0.36 * s, -0.42 * s, 0], color=INK, stroke_width=5),
    )
    speed = VGroup(*[Line([0.5 * s, y * s, 0], [0.95 * s, y * s, 0],
                          color=GREEN, stroke_width=4)
                     for y in (0.45, 0.18, -0.1)])
    return VGroup(body, speed)


def swimmer(s=1.0):
    waves = VGroup(*[Arc(radius=0.3 * s, start_angle=0, angle=PI,
                         color=BLUE, stroke_width=4).move_to([x * s, -0.3 * s, 0])
                     for x in (-0.62, 0, 0.62)])
    head = Circle(radius=0.17 * s, fill_color=ROSE, fill_opacity=0.9,
                  stroke_color=INK, stroke_width=2.5).move_to([-0.2 * s, 0.12 * s, 0])
    arm = Arc(radius=0.38 * s, start_angle=0.3, angle=1.9, color=INK,
              stroke_width=5).move_to([0.3 * s, 0.22 * s, 0])
    drops = VGroup(*[Dot([x * s, y * s, 0], radius=0.045 * s, color=BLUE)
                     for x, y in [(0.62, 0.5), (0.8, 0.28)]])
    return VGroup(waves, head, arm, drops)


def school_walk(s=1.0):
    house = VGroup(
        Rectangle(width=0.75 * s, height=0.62 * s, fill_color="#FFFFFF", fill_opacity=1,
                  stroke_color=INK, stroke_width=3).move_to([-0.62 * s, -0.12 * s, 0]),
        Polygon([-1.06 * s, 0.19 * s, 0], [-0.18 * s, 0.19 * s, 0], [-0.62 * s, 0.62 * s, 0],
                fill_color=REDA, fill_opacity=0.95, stroke_color=INK, stroke_width=3),
        Rectangle(width=0.2 * s, height=0.3 * s, fill_color=GOLD, fill_opacity=1,
                  stroke_color=INK, stroke_width=2).move_to([-0.62 * s, -0.28 * s, 0]),
    )
    walker = VGroup(
        Circle(radius=0.15 * s, fill_color=ROSE, fill_opacity=0.9,
               stroke_color=INK, stroke_width=2.5).move_to([0.62 * s, 0.42 * s, 0]),
        Line([0.62 * s, 0.27 * s, 0], [0.62 * s, -0.12 * s, 0], color=INK, stroke_width=5),
        Line([0.62 * s, 0.1 * s, 0], [0.4 * s, -0.05 * s, 0], color=INK, stroke_width=4),
        Line([0.62 * s, -0.12 * s, 0], [0.42 * s, -0.45 * s, 0], color=INK, stroke_width=5),
        Line([0.62 * s, -0.12 * s, 0], [0.82 * s, -0.45 * s, 0], color=INK, stroke_width=5),
    )
    ground = Line([-1.1 * s, -0.48 * s, 0], [1.0 * s, -0.48 * s, 0],
                  color=GOLD, stroke_width=3)
    return VGroup(house, walker, ground)


def build_balance(col=GOLD, s=1.0, center=(0.0, 0.0)):
    """Balance en 2 morceaux : `stand` fixe + `rocker` qui oscille autour de `pivot`."""
    cx, cy = center
    off = np.array([cx, cy, 0])
    base = Polygon([-0.75 * s, -1.35 * s, 0], [0.75 * s, -1.35 * s, 0], [0, -0.05 * s, 0],
                   fill_color=col, fill_opacity=0.85, stroke_color=INK, stroke_width=3)
    knob = Circle(radius=0.15 * s, fill_color=col, fill_opacity=1,
                  stroke_color=INK, stroke_width=2).move_to([0, 0.02 * s, 0])
    stand = VGroup(base, knob).shift(off)
    beam = Line(LEFT * 2.6 * s, RIGHT * 2.6 * s, color=INK, stroke_width=8).shift(UP * 0.02 * s)
    rocker = VGroup(beam)
    for x in (-2.6 * s, 2.6 * s):
        chain = VGroup(Line([x, 0.02 * s, 0], [x - 0.55 * s, -0.85 * s, 0]),
                       Line([x, 0.02 * s, 0], [x + 0.55 * s, -0.85 * s, 0])).set_stroke(INK, 3)
        dish = Ellipse(width=1.55 * s, height=0.42 * s, fill_color=col, fill_opacity=0.42,
                       stroke_color=INK, stroke_width=4).move_to([x, -0.9 * s, 0])
        rocker.add(chain, dish)
    rocker.shift(off)
    pivot = off + np.array([0, 0.02 * s, 0])
    return stand, rocker, pivot


def clock(radius=1.0):
    """ساعة : وجه دائري + شرطات + عقربان."""
    face = Circle(radius=radius, fill_color="#FFFFFF", fill_opacity=1,
                  stroke_color=INK, stroke_width=4)
    ticks = VGroup()
    for k in range(12):
        a = np.deg2rad(90 - k * 30)
        p1 = np.array([np.cos(a), np.sin(a), 0]) * radius
        p2 = np.array([np.cos(a), np.sin(a), 0]) * (radius - 0.16)
        ticks.add(Line(p2, p1, color=INK, stroke_width=3))
    hour = Line([0, 0, 0], [0.0, 0.52, 0], color=REDA, stroke_width=6)
    minute = Line([0, 0, 0], [0.62, 0.0, 0], color=BLUE, stroke_width=5)
    pin = Dot(radius=0.07, color=INK)
    return VGroup(face, ticks, hour, minute, pin)


class VideoSci2(MajorScene):
    AUDIO = HERE / "audio_sci2"
    UNIT_AR = "علوم · درس 2"
    UNIT_COLOR = YELL
    TITLE = "التوازن الطاقوي"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين التوازن الطاقوي"

    # ── 2. التعريف : l'assiette tombe à droite, le ballon à gauche ──
    def s_def(self):
        d = self.seg("def1")
        head = titled("ما هو التوازن الطاقوي؟", 34, YELL)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        kid = self.boy(2.2).move_to([0, -1.6, 0])
        self.sfx("pop")
        self.play(FadeIn(kid, scale=0.3, rate_func=BOUNCE), run_time=0.8)
        # l'assiette de nourriture TOMBE du ciel à droite (RTL : on commence par manger)
        plate = VGroup(
            Ellipse(width=2.3, height=0.75, fill_color="#FFFFFF", fill_opacity=1,
                    stroke_color=INK, stroke_width=3),
            galette(1.0).shift(UP * 0.28 + RIGHT * 0.45),
            apple(0.85).shift(UP * 0.4 + LEFT * 0.5),
        ).move_to([3.8, 4.4, 0])
        self.add(plate)
        self.sfx("boing")
        self.play(plate.animate.move_to([3.8, 0.45, 0]), run_time=0.8, rate_func=DROP)
        w1 = ar("نأكل", 34, "BOLD", ROSE).move_to([3.8, -1.1, 0])
        self.sfx("pop")
        self.play(FadeIn(w1, scale=0.5, rate_func=BOUNCE), run_time=0.5)
        # le ballon TOMBE à gauche : on dépense en jouant
        ball = football(1.15).move_to([-3.8, 4.4, 0])
        self.add(ball)
        self.sfx("boing")
        self.play(ball.animate.move_to([-3.8, 0.45, 0]), run_time=0.8, rate_func=DROP)
        w2 = ar("ننفق", 34, "BOLD", BLUE).move_to([-3.8, -1.1, 0])
        self.sfx("pop")
        self.play(FadeIn(w2, scale=0.5, rate_func=BOUNCE), run_time=0.5)
        self.sfx("ding")
        self.play(Wiggle(kid), run_time=1.0)
        self.wait(max(d - 5.3, 0.2))
        self.clear_all()

    # ── 3. الطاقة تدخل وتخرج : les aliments glissent dans le corps ──
    def s_io(self):
        d = self.seg("io1")
        head = titled("طاقة تدخل وطاقة تخرج", 34, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        body = RoundedRectangle(corner_radius=0.3, width=3.0, height=2.6,
                                fill_color=GREEN, fill_opacity=0.25,
                                stroke_color=GREEN, stroke_width=3).move_to([0, -0.3, 0])
        body_t = ar("الجسم", 34, "BOLD", GREEN).move_to(body)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(body, body_t), rate_func=BOUNCE), run_time=0.8)
        # flèche entrante (depuis la droite) + les aliments GLISSENT dedans un par un
        in_arrow = Arrow([4.3, -0.3, 0], [1.7, -0.3, 0], color=ROSE,
                         stroke_width=9, max_tip_length_to_length_ratio=0.18)
        in_lab = ar("ندخل الطاقة بالأكل والشرب", 25, "BOLD", ROSE).move_to([3.35, 1.35, 0])
        self.sfx("whoosh")
        self.play(GrowArrow(in_arrow), FadeIn(in_lab, shift=DOWN * 0.2), run_time=0.9)
        for food in (galette(1.0), bottle(1.0)):
            food.move_to([5.2, 0.35, 0])
            self.add(food)
            self.sfx("whoosh")
            self.play(food.animate.move_to([0, -0.3, 0]).scale(0.25),
                      run_time=0.9, rate_func=rf.ease_in_out_sine)
            self.remove(food)
        # flèche sortante (vers la gauche) + gouttes de sueur et étoile qui SORTENT
        out_arrow = Arrow([-1.7, -0.3, 0], [-4.3, -0.3, 0], color=BLUE,
                          stroke_width=9, max_tip_length_to_length_ratio=0.18)
        out_lab = ar("ننفقها بالتنفس والحركة والتفكير", 25, "BOLD", BLUE).move_to([-3.35, -1.9, 0])
        self.sfx("whoosh")
        self.play(GrowArrow(out_arrow), FadeIn(out_lab, shift=UP * 0.2), run_time=0.9)
        outs = [sweat(1.1), chip(GOLD).scale(0.9), sweat(0.9)]
        tgts = [[-4.6, 0.5, 0], [-5.2, -0.1, 0], [-4.9, 1.1, 0]]
        for o, tg in zip(outs, tgts):
            o.move_to([-1.4, 0.1, 0]).scale(0.3)
            self.add(o)
            self.sfx("pop")
            self.play(o.animate.move_to(tg).scale(3.0), run_time=0.55,
                      rate_func=rf.ease_out_quad)
        self.play(LaggedStart(*[FadeOut(o, shift=UP * 0.4) for o in outs],
                              lag_ratio=0.15), run_time=0.7)
        self.wait(max(d - 7.65, 0.2))
        self.clear_all()

    # ── 4. الميزان : il OSCILLE vraiment puis s'équilibre ──────
    def s_balance(self):
        d = self.seg("bal1")
        head = titled("ميزان الطاقة", 36, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        stand, rocker, pivot = build_balance(GOLD, 1.0, (0.0, 0.35))
        self.sfx("whoosh")
        self.play(Create(stand), Create(rocker), run_time=1.2)
        r_lab = ar("نأكل", 30, "BOLD", ROSE).move_to([2.6, -1.55, 0])
        l_lab = ar("ننفق", 30, "BOLD", BLUE).move_to([-2.6, -1.55, 0])
        self.sfx("pop")
        self.play(FadeIn(r_lab, shift=UP * 0.2, rate_func=BOUNCE),
                  FadeIn(l_lab, shift=UP * 0.2, rate_func=BOUNCE), run_time=0.7)
        # la galette TOMBE dans la كفّة de droite…
        gal = galette(1.05).move_to([2.6, 4.3, 0])
        self.add(gal)
        self.sfx("boing")
        self.play(gal.animate.move_to([2.6, -0.15, 0]), run_time=0.7, rate_func=DROP)
        rocker.add(gal)
        # …l'éclair d'énergie TOMBE dans celle de gauche
        z = lightning(0.95).move_to([-2.6, 4.3, 0])
        self.add(z)
        self.sfx("boing")
        self.play(z.animate.move_to([-2.6, -0.1, 0]), run_time=0.7, rate_func=DROP)
        rocker.add(z)
        # la balance OSCILLE : droite, gauche, puis équilibre
        self.play(Rotate(rocker, angle=-0.12, about_point=pivot),
                  run_time=0.6, rate_func=rf.ease_in_out_sine)
        self.play(Rotate(rocker, angle=0.24, about_point=pivot),
                  run_time=0.7, rate_func=rf.ease_in_out_sine)
        self.play(Rotate(rocker, angle=-0.12, about_point=pivot),
                  run_time=0.6, rate_func=rf.ease_in_out_sine)
        eq = ar("نأكل = ننفق", 34, "BOLD", INK).move_to([0, 2.15, 0])
        self.play(Write(eq), run_time=0.8)
        res = RoundedRectangle(corner_radius=0.22, width=5.0, height=1.0, fill_color=GREEN,
                               fill_opacity=0.92, stroke_color=INK,
                               stroke_width=2.5).move_to([0, -2.9, 0])
        res_t = ar("الوزن ثابت وصحة جيدة", 28, "BOLD", "#FFFFFF").move_to(res)
        self.sfx("tada")
        self.play(GrowFromCenter(VGroup(res, res_t), rate_func=BOUNCE), run_time=0.9)
        self.play(Flash(res_t, color=GREEN, flash_radius=1.6), run_time=0.5)
        self.wait(max(d - 8.3, 0.2))
        self.clear_all()

    # ── 5. الفائض والنقص : la balance penche, cartes qui gonflent ──
    def s_cases(self):
        d = self.seg("case1")
        head = titled("عند الفائض أو النقص", 34, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        stand, rocker, pivot = build_balance(LILA, 0.8, (0.0, 0.85))
        self.sfx("whoosh")
        self.play(Create(stand), Create(rocker), run_time=0.9)
        # 1) trop de nourriture : la كفّة de droite DESCEND lourdement
        gal = galette(0.9).move_to([2.08, 4.3, 0])
        ap = apple(0.75).move_to([2.45, 4.5, 0])
        self.add(gal, ap)
        self.sfx("boing")
        self.play(gal.animate.move_to([1.95, 0.55, 0]),
                  ap.animate.move_to([2.4, 0.6, 0]), run_time=0.6, rate_func=DROP)
        rocker.add(gal, ap)
        self.sfx("whoosh")
        self.play(Rotate(rocker, angle=-0.2, about_point=pivot),
                  run_time=0.8, rate_func=rf.ease_out_back)
        c1 = RoundedRectangle(corner_radius=0.24, width=5.6, height=1.05, fill_color=ROSE,
                              fill_opacity=0.92, stroke_color=INK,
                              stroke_width=2.5).move_to([3.5, -2.55, 0])
        c1t = ar("اكتساب وزن زائد وأمراض", 26, "BOLD", "#FFFFFF").move_to(c1)
        g1 = VGroup(c1, c1t)
        self.sfx("pop")
        self.play(GrowFromCenter(g1, rate_func=BOUNCE), run_time=0.8)
        self.play(Indicate(g1, color=ROSE, scale_factor=1.12), run_time=0.6)
        # 2) l'inverse : la nourriture s'en va, l'effort pèse à gauche
        z = lightning(0.8).move_to([-2.08, 4.3, 0])
        rocker.remove(gal, ap)
        self.add(z)
        self.sfx("boing")
        self.play(FadeOut(gal, shift=UP * 0.6), FadeOut(ap, shift=UP * 0.6),
                  z.animate.move_to([-2.35, 0.9, 0]), run_time=0.6, rate_func=DROP)
        rocker.add(z)
        self.sfx("whoosh")
        self.play(Rotate(rocker, angle=0.4, about_point=pivot),
                  run_time=0.8, rate_func=rf.ease_out_back)
        c2 = RoundedRectangle(corner_radius=0.24, width=5.6, height=1.05, fill_color=BLUE,
                              fill_opacity=0.92, stroke_color=INK,
                              stroke_width=2.5).move_to([-3.5, -2.55, 0])
        c2t = ar("نقص في الوزن وتعب", 26, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.8)
        # le personnage s'affaisse de fatigue
        garcon = self.boy(1.6).move_to([-5.9, -0.6, 0])
        self.sfx("pop")
        self.play(FadeIn(garcon, scale=0.4, rate_func=BOUNCE), run_time=0.5)
        self.play(garcon.animate.shift(DOWN * 0.35).rotate(0.12), run_time=0.6,
                  rate_func=rf.ease_in_out_sine)
        self.wait(max(d - 7.9, 0.2))
        self.clear_all()

    # ── 6. مثال محلول : l'aiguille TOURNE, le compteur saute ──
    def s_example(self):
        d = self.seg("ex1")
        head = titled("مثال محلول: من كراسك", 32, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        cl = clock(1.0).move_to([-4.3, 0.05, 0])
        self.sfx("whoosh")
        self.play(Create(cl), run_time=1.0)
        lab = ar("ساعة رياضة واحدة", 28, "BOLD", INK).move_to([-4.3, 1.75, 0])
        self.sfx("ding")
        self.play(FadeIn(lab, shift=DOWN * 0.2, rate_func=BOUNCE), run_time=0.7)
        # l'aiguille des minutes fait UN TOUR COMPLET : une heure passe !
        self.sfx("whoosh")
        self.play(Rotate(cl[3], angle=-2 * PI, about_point=cl[0].get_center()),
                  run_time=1.5, rate_func=rf.ease_in_out_sine)
        val = VGroup(num("300", 50, REDA), ar("سعرة", 26, "BOLD", REDA)
                     ).arrange(LEFT, buff=0.25).move_to([-4.3, -1.7, 0])
        self.sfx("boing")
        self.play(FadeIn(val, shift=DOWN * 0.5, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        self.play(Flash(val[0], color=REDA, flash_radius=1.1), run_time=0.5)
        self.wait(max(d - 5.4, 0.2))

        d = self.seg("ex2")
        q = ar("فكم تنفق ساعتان؟", 32, "BOLD", BLUE).move_to([1.8, 1.55, 0])
        self.sfx("pop")
        self.play(FadeIn(q, shift=DOWN * 0.2, rate_func=BOUNCE), run_time=0.7)
        # les nombres SAUTENT un par un dans le calcul
        calc = VGroup(num("2", 46), num("×", 38, GOLD), num("300", 46),
                      num("=", 40), num("600", 58, GREEN)).arrange(LEFT, buff=0.3)
        unit = ar("سعرة حرارية", 28, "BOLD", GREEN)
        row = VGroup(calc, unit).arrange(LEFT, buff=0.4).move_to([1.8, -0.35, 0])
        box = SurroundingRectangle(row, color=GREEN, corner_radius=0.15, buff=0.26)
        self.sfx("ding")
        self.play(LaggedStart(*[FadeIn(m, shift=DOWN * 0.5, scale=0.5, rate_func=BOUNCE)
                                for m in [*calc, unit]], lag_ratio=0.15), run_time=1.6)
        self.play(Create(box), run_time=0.5)
        self.play(Flash(calc[4], color=GREEN, flash_radius=1.3), run_time=0.7)
        # l'enfant surgit et fête le résultat
        kid = self.boy(1.8).to_corner(DR, buff=0.3)
        tag = ar("طاقة كثيرة تُنفَق!", 30, "BOLD", ROSE).move_to([1.8, -2.4, 0])
        self.sfx("tada")
        self.play(FadeIn(tag, scale=0.6, rate_func=BOUNCE),
                  FadeIn(kid, scale=0.3, rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(kid), run_time=1.0)
        self.wait(max(d - 5.4, 0.2))
        self.clear_all()

    # ── 7. انتبه : l'écran hypnotise, le ballon sauve ───────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! ما يكسر التوازن", 34, REDA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # une télé dessinée + un enfant assis devant, immobile
        tv = VGroup(
            RoundedRectangle(corner_radius=0.15, width=3.6, height=2.5,
                             fill_color=INK, fill_opacity=0.9, stroke_color=INK,
                             stroke_width=4),
            RoundedRectangle(corner_radius=0.1, width=3.15, height=2.05,
                             fill_color=BLUE, fill_opacity=0.55, stroke_width=0),
            Line([-0.55, -1.5, 0], [0.55, -1.5, 0], color=INK, stroke_width=6),
            Line([0, -1.25, 0], [0, -1.5, 0], color=INK, stroke_width=6),
        ).move_to([4.2, -0.5, 0])
        self.sfx("whoosh")
        self.play(Create(tv), run_time=0.9)
        garcon = self.boy(1.6).move_to([1.6, -1.55, 0])
        self.play(FadeIn(garcon, shift=RIGHT * 0.4), run_time=0.6)   # il reste figé…
        c1 = RoundedRectangle(corner_radius=0.24, width=6.2, height=1.7, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK,
                              stroke_width=2.5).move_to([-3.3, 0.65, 0])
        c1t1 = ar("الجلوس الطويل أمام الشاشات", 26, "BOLD", "#FFFFFF").move_to(
            c1.get_center() + UP * 0.32)
        c1t2 = ar("مع الأكل الكثير يكسر التوازن", 26, "BOLD", "#FFF3C4").move_to(
            c1.get_center() + DOWN * 0.34)
        g1 = VGroup(c1, c1t1, c1t2)
        self.sfx("boing")
        self.play(GrowFromCenter(g1, rate_func=BOUNCE), run_time=0.8)
        self.play(Wiggle(g1, scale_value=1.06, rotation_angle=0.02), run_time=0.8)  # ça tremble : danger !
        # le ballon TOMBE à côté : la solution, c'est bouger
        ball = football(1.0).move_to([-1.2, 4.3, 0])
        self.add(ball)
        self.sfx("boing")
        self.play(ball.animate.move_to([-1.2, -1.6, 0]), run_time=0.8, rate_func=DROP)
        c2 = RoundedRectangle(corner_radius=0.24, width=4.6, height=0.95, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK,
                              stroke_width=2.5).move_to([-4.1, -2.75, 0])
        c2t = ar("تحرّك والعب كل يوم", 26, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 5.6, 0.2))
        self.clear_all()

    # ── 8. سرّ : les 3 activités BONDISSENT à l'écran ───────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ: أنشطة تنفق الطاقة", 32, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        acts = [("الجري", GREEN, runner(1.5)),
                ("السباحة", BLUE, swimmer(1.5)),
                ("المشي إلى المدرسة", ROSE, school_walk(1.5))]
        cards = VGroup()
        for i, (lab, col, drawing) in enumerate(acts):
            p = RoundedRectangle(corner_radius=0.3, width=4.0, height=3.3,
                                 fill_color=col, fill_opacity=0.14,
                                 stroke_color=col, stroke_width=3)
            drawing.move_to(p.get_center() + UP * 0.45)
            pt = ar(lab, 26, "BOLD", col)
            if pt.width > 3.4:
                pt.scale_to_fit_width(3.4)
            pt.move_to(p.get_center() + DOWN * 1.2)
            cards.add(VGroup(p, drawing, pt).move_to([4.35 - i * 4.35, -0.55, 0]))
        # elles SAUTENT l'une après l'autre (de droite à gauche, RTL)
        for c in cards:
            self.sfx("boing")
            self.play(FadeIn(c, shift=DOWN * 0.7, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        # puis les dessins gigotent tous ensemble : ça vit !
        self.play(LaggedStart(*[Wiggle(c[1]) for c in cards], lag_ratio=0.15), run_time=1.8)
        note = ar("كلها تحافظ على توازنك!", 28, "BOLD", GOLD).move_to([0, -3.15, 0])
        self.sfx("tada")
        self.play(FadeIn(note, scale=0.6, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 5.9, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أعرّف التوازن الطاقوي",
            "أفهم ماذا يحدث عند الفائض أو النقص",
            "أوازن بين الأكل والنشاط البدني",
        ])
        self.s_def()
        self.s_io()
        self.s_balance()
        self.s_cases()
        self.s_example()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
