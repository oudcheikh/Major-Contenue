# -*- coding: utf-8 -*-
"""Vidéo Sciences 3 — التصحر — VERSION CARTOON.  Rendu : ./build_science.sh 3
Style dessin animé : le sable AVANCE et recouvre la terre verte, l'arbre BASCULE,
les moutons BROUTENT et l'herbe disparaît, la dune menace la maison, la rangée
d'arbres POUSSE du sol et STOPPE la dune — un maximum d'images, un minimum de texte."""
import numpy as np
from manim import (VGroup, Rectangle, RoundedRectangle, Circle, Ellipse, Polygon,
                   SurroundingRectangle, Dot, Line, Arc, Arrow,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter, GrowFromEdge,
                   GrowArrow, Rotate, Flash, Indicate, Wiggle, LaggedStart,
                   UP, DOWN, LEFT, RIGHT, DEGREES, PI, rate_functions as rf)

from video_common import (MajorScene, ar, num, titled, chip,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)

DROP = rf.ease_out_bounce      # chute cartoon : rebondit à l'arrivée
SAND = "#E4C878"               # رمل الكثبان
SAND_EDGE = "#C7A94E"
BARK = "#8B5A2B"


# ─── mini-dessins « cartoon » (formes pures, zéro texte) ───────────────
def tree(h=1.1, col=GREEN):
    trunk = Line([0, -h * 0.5, 0], [0, h * 0.12, 0], color=BARK, stroke_width=8)
    leaves = Circle(radius=h * 0.42, fill_color=col, fill_opacity=1,
                    stroke_color=INK, stroke_width=2).move_to([0, h * 0.35, 0])
    return VGroup(trunk, leaves)


def plant(s=1.0):
    stem = Line([0, -0.5 * s, 0], [0, 0.35 * s, 0], color="#2b6e3a", stroke_width=5)
    return VGroup(stem,
                  Ellipse(width=0.4 * s, height=0.2 * s, fill_color=GREEN, fill_opacity=1,
                          stroke_width=0).move_to([-0.2 * s, 0.05 * s, 0]).rotate(0.5),
                  Ellipse(width=0.4 * s, height=0.2 * s, fill_color=GREEN, fill_opacity=1,
                          stroke_width=0).move_to([0.2 * s, 0.2 * s, 0]).rotate(-0.5),
                  Circle(radius=0.16 * s, fill_color=ROSE, fill_opacity=1,
                         stroke_color=INK, stroke_width=2).move_to([0, 0.45 * s, 0]))


def dead_plant(s=1.0):
    """plante fanée : tige penchée + feuilles dorées qui pendent."""
    stem = Line([0, -0.5 * s, 0], [0.14 * s, 0.3 * s, 0], color="#8a6b3f", stroke_width=5)
    return VGroup(stem,
                  Ellipse(width=0.36 * s, height=0.17 * s, fill_color=GOLD, fill_opacity=1,
                          stroke_width=0).move_to([0.34 * s, 0.14 * s, 0]).rotate(-1.0),
                  Ellipse(width=0.36 * s, height=0.17 * s, fill_color="#C9A94E",
                          fill_opacity=1, stroke_width=0)
                  .move_to([-0.08 * s, -0.02 * s, 0]).rotate(-1.3))


def wheat(s=1.0):
    stem = Line([0, -0.55 * s, 0], [0, 0.24 * s, 0], color="#B08850", stroke_width=4)
    grains = VGroup(*[Ellipse(width=0.2 * s, height=0.12 * s, fill_color=GOLD,
                              fill_opacity=1, stroke_color=INK, stroke_width=1.5)
                      .move_to([x * s, y * s, 0]).rotate(r)
                      for x, y, r in [(-0.1, 0.28, 0.6), (0.1, 0.38, -0.6),
                                      (-0.1, 0.5, 0.6), (0.1, 0.6, -0.6), (0, 0.74, 0)]])
    return VGroup(stem, grains)


def waterdrop(s=1.0, col=BLUE):
    return VGroup(
        Circle(radius=0.3 * s, fill_color=col, fill_opacity=0.85,
               stroke_color=INK, stroke_width=2.5),
        Polygon([-0.2 * s, 0.22 * s, 0], [0.2 * s, 0.22 * s, 0], [0, 0.68 * s, 0],
                fill_color=col, fill_opacity=0.85, stroke_color=INK, stroke_width=2.5))


def slash(s=1.0):
    return Line([-0.55 * s, -0.55 * s, 0], [0.55 * s, 0.55 * s, 0],
                color=REDA, stroke_width=8)


def sun(s=1.0):
    rays = VGroup(*[Line([0.55 * s * np.cos(a), 0.55 * s * np.sin(a), 0],
                         [0.78 * s * np.cos(a), 0.78 * s * np.sin(a), 0],
                         color=GOLD, stroke_width=4)
                    for a in np.linspace(0, 2 * PI, 8, endpoint=False)])
    return VGroup(Circle(radius=0.42 * s, fill_color=YELL, fill_opacity=1,
                         stroke_color=GOLD, stroke_width=3), rays)


def sheep(s=1.0):
    body = Ellipse(width=0.8 * s, height=0.5 * s, fill_color="#FFFFFF", fill_opacity=1,
                   stroke_color=INK, stroke_width=2.5)
    legs = VGroup(Line([-0.2 * s, -0.2 * s, 0], [-0.2 * s, -0.5 * s, 0],
                       color=INK, stroke_width=3.5),
                  Line([0.2 * s, -0.2 * s, 0], [0.2 * s, -0.5 * s, 0],
                       color=INK, stroke_width=3.5))
    head = Circle(radius=0.15 * s, fill_color="#6b6b6b", fill_opacity=1,
                  stroke_color=INK, stroke_width=2).move_to([-0.42 * s, 0.1 * s, 0])
    return VGroup(legs, body, head)


def grass_tuft(s=1.0):
    return VGroup(*[Line([0, 0, 0], [dx * s, 0.3 * s, 0], color=GREEN, stroke_width=3.5)
                    for dx in (-0.1, 0, 0.1)])


def shield(s=1.0, col=GREEN):
    return VGroup(
        Polygon([-0.42 * s, 0.45 * s, 0], [0.42 * s, 0.45 * s, 0], [0.42 * s, -0.05 * s, 0],
                [0, -0.55 * s, 0], [-0.42 * s, -0.05 * s, 0],
                fill_color=col, fill_opacity=0.9, stroke_color=INK, stroke_width=3),
        Line([-0.16 * s, 0.02 * s, 0], [-0.03 * s, -0.16 * s, 0], color="#FFFFFF",
             stroke_width=5),
        Line([-0.03 * s, -0.16 * s, 0], [0.2 * s, 0.18 * s, 0], color="#FFFFFF",
             stroke_width=5))


def faucet(s=1.0):
    pipe = RoundedRectangle(corner_radius=0.06 * s, width=0.95 * s, height=0.28 * s,
                            fill_color="#9AA7B5", fill_opacity=1,
                            stroke_color=INK, stroke_width=2.5)
    spout = Rectangle(width=0.22 * s, height=0.36 * s, fill_color="#9AA7B5",
                      fill_opacity=1, stroke_color=INK, stroke_width=2.5
                      ).move_to([-0.36 * s, -0.28 * s, 0])
    handle = Circle(radius=0.13 * s, fill_color=GOLD, fill_opacity=1,
                    stroke_color=INK, stroke_width=2).move_to([0.12 * s, 0.28 * s, 0])
    return VGroup(pipe, spout, handle)


def house_mr(s=0.72, col=ROSE, dome=True):
    """بيت موريتاني : مربع + قبة أو سقف مستوٍ."""
    body = Rectangle(width=s, height=s * 0.78, fill_color="#FFF6E0", fill_opacity=1,
                     stroke_color=INK, stroke_width=2.5)
    if dome:
        roof = Arc(radius=s * 0.4, angle=PI, start_angle=0, fill_color=col,
                   fill_opacity=1, stroke_color=INK, stroke_width=2.5)
        roof.next_to(body, UP, buff=-0.02)
    else:
        roof = Rectangle(width=s * 1.14, height=s * 0.14, fill_color=col, fill_opacity=1,
                         stroke_color=INK, stroke_width=2.5).next_to(body, UP, buff=0)
    door = RoundedRectangle(corner_radius=0.05 * s, width=s * 0.3, height=s * 0.42,
                            fill_color=INK, fill_opacity=0.85, stroke_width=0)
    door.move_to([body.get_center()[0], body.get_bottom()[1] + s * 0.21, 0])
    return VGroup(body, roof, door)


def dune(w=3.4, h=1.4):
    pts = [[-w / 2, 0, 0], [-w * 0.24, h * 0.62, 0], [w * 0.08, h * 0.92, 0],
           [w * 0.34, h * 0.55, 0], [w / 2, 0, 0]]
    return Polygon(*pts, fill_color=SAND, fill_opacity=1,
                   stroke_color=SAND_EDGE, stroke_width=3)


def sand_sheet(w=15.0, h=1.0):
    """nappe de sable pleine largeur au sommet ondulé (avance sur la terre)."""
    xs = np.linspace(-w / 2, w / 2, 9)
    top = [[x, h * (0.5 + 0.4 * np.sin(i * 1.9)), 0] for i, x in enumerate(xs)]
    pts = top + [[w / 2, -h, 0], [-w / 2, -h, 0]]
    return Polygon(*pts, fill_color=SAND, fill_opacity=1,
                   stroke_color=SAND_EDGE, stroke_width=3)


class VideoSci3(MajorScene):
    AUDIO = HERE / "audio_sci3"
    UNIT_AR = "علوم · درس 3"
    UNIT_COLOR = ROSE
    TITLE = "التصحر"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين درس التصحر"

    # ── 2. التعريف : le sable recouvre la terre verte SOUS NOS YEUX ──
    def s_def(self):
        d = self.seg("def1")                                        # 7.82
        head = titled("ما هو التصحر؟", 34, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # la terre verte et ses plantes
        land = Rectangle(width=13.6, height=0.5, fill_color=GREEN, fill_opacity=0.9,
                         stroke_color="#2b6e3a", stroke_width=3).move_to([0, -2.75, 0])
        greens = VGroup(tree(1.2).move_to([3.6, -1.9, 0]),
                        plant(1.1).move_to([1.4, -2.1, 0]),
                        tree(1.0, "#7BCB8A").move_to([-0.9, -2.0, 0]),
                        plant(0.95).move_to([-3.2, -2.15, 0]))
        lab1 = ar("أرض خصبة", 28, "BOLD", GREEN).move_to([4.6, 0.6, 0])
        self.sfx("pop")
        self.play(FadeIn(land), FadeIn(lab1, shift=DOWN * 0.2),
                  LaggedStart(*[GrowFromEdge(g, DOWN) for g in greens],
                              lag_ratio=0.2), run_time=1.3)
        # LE plan signature : le sable AVANCE et les plantes se FANENT
        sheet = sand_sheet().move_to([14.8, -2.75, 0])
        self.add(sheet)
        lab2 = ar("أرض جافة تشبه الصحراء", 28, "BOLD", GOLD).move_to([-3.4, 0.6, 0])
        self.sfx("whoosh")
        self.play(sheet.animate.shift(LEFT * 14.8),
                  LaggedStart(*[g.animate.rotate(-55 * DEGREES).set_opacity(0)
                                for g in greens], lag_ratio=0.22),
                  run_time=2.6, rate_func=rf.ease_in_out_sine)
        du = dune(4.0, 1.5).move_to([0.4, -2.3, 0])
        du.shift(UP * ((-2.3) - du.get_bottom()[1] - 0.35))
        self.sfx("boing")
        self.play(GrowFromEdge(du, DOWN, rate_func=BOUNCE),
                  FadeIn(lab2, shift=DOWN * 0.2), run_time=0.9)
        t = ar("تحوّل الأراضي الخصبة إلى أراضٍ جافة", 30, "BOLD", INK).move_to([0, 1.9, 0])
        self.sfx("ding")
        self.play(Write(t), run_time=1.0)
        self.wait(max(d - 6.7, 0.2))
        self.clear_all()

    # ── 3. الأسباب : soleil qui grossit, arbre qui tombe, moutons ──
    def s_causes(self):
        d = self.seg("cause1")                                      # 8.13
        head = titled("أسباب التصحر", 36, REDA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # (1) الجفاف : le soleil GROSSIT
        su = sun(0.85).move_to([4.3, 1.0, 0])
        lb1 = ar("الجفاف", 26, "BOLD", GOLD).move_to([4.3, -2.5, 0])
        self.sfx("pop")
        self.play(FadeIn(su, scale=0.4, rate_func=BOUNCE), run_time=0.5)
        self.sfx("ding")
        self.play(su.animate.scale(1.4), FadeIn(lb1, shift=UP * 0.2), run_time=0.8)
        # (2) إزالة الغابات : l'arbre BASCULE et tombe
        tr = tree(1.5).move_to([0, 0.4, 0])
        lb2 = ar("إزالة الغابات", 26, "BOLD", GREEN).move_to([0, -2.5, 0])
        self.sfx("pop")
        self.play(FadeIn(tr, scale=0.4, rate_func=BOUNCE), run_time=0.5)
        foot = tr.get_bottom()
        self.sfx("boing")
        self.play(Rotate(tr, -80 * DEGREES, about_point=foot),
                  FadeIn(lb2, shift=UP * 0.2), run_time=0.9, rate_func=DROP)
        # (3) الرعي الجائر : les moutons broutent, l'herbe disparaît
        grass = VGroup(*[grass_tuft(1.0).move_to([-5.7 + i * 0.55, -0.75, 0])
                         for i in range(5)])
        flock = VGroup(sheep(0.85).move_to([-3.0, -0.35, 0]),
                       sheep(0.7).move_to([-2.4, -0.75, 0]),
                       sheep(0.75).move_to([-3.6, -0.85, 0]))
        lb3 = ar("الرعي الجائر", 26, "BOLD", REDA).move_to([-4.3, -2.5, 0])
        self.sfx("pop")
        self.play(FadeIn(grass), FadeIn(flock, shift=LEFT * 0.4, rate_func=BOUNCE),
                  run_time=0.6)
        self.sfx("whoosh")
        self.play(flock.animate.shift(LEFT * 1.6),
                  LaggedStart(*[FadeOut(g, scale=0.3) for g in grass], lag_ratio=0.2),
                  FadeIn(lb3, shift=UP * 0.2), run_time=1.4)
        self.wait(max(d - 5.6, 0.2))
        self.clear_all()

    # ── 4. العواقب : trois vignettes qui TOMBENT avec rebond ───────
    def s_effects(self):
        d = self.seg("effect1")                                     # 9.45
        head = titled("عواقب التصحر", 36, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        icons = [VGroup(dead_plant(1.5)),
                 VGroup(wheat(1.5), slash(1.1)),
                 VGroup(waterdrop(1.5), slash(1.1))]
        labels = ["فقدان الغطاء النباتي", "تراجع الإنتاج الزراعي", "نقص الغذاء والماء"]
        cols = [GREEN, GOLD, BLUE]
        t = 0.9
        for i, (ic, lab, col) in enumerate(zip(icons, labels, cols)):
            x = 4.2 - i * 4.2
            ic.move_to([x, 4.3, 0])
            self.add(ic)
            self.sfx("boing")
            self.play(ic.animate.move_to([x, 0.7, 0]), run_time=0.8, rate_func=DROP)
            lb = ar(lab, 24, "BOLD", col)
            if lb.width > 3.8:
                lb.scale_to_fit_width(3.8)
            lb.move_to([x, -1.0, 0])
            self.sfx("pop")
            self.play(FadeIn(lb, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.5)
            t += 1.3
        self.play(LaggedStart(*[Wiggle(ic) for ic in icons], lag_ratio=0.15),
                  run_time=1.6)
        self.wait(max(d - t - 1.6, 0.2))
        self.clear_all()

    # ── 5. موريتانيا : la dune AVANCE vers les maisons ─────────────
    def s_mr(self):
        d = self.seg("mr1")                                         # 10.41
        head = titled("التصحر في موريتانيا", 34, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        ground = Line([-6.5, -2.6, 0], [6.5, -2.6, 0], color=SAND_EDGE, stroke_width=4)
        self.play(Create(ground), run_time=0.4)
        village = VGroup(house_mr(0.85, ROSE, dome=True),
                         house_mr(0.72, BLUE, dome=False),
                         house_mr(0.78, YELL, dome=True))
        for i, hh in enumerate(village):
            hh.move_to([-4.9 + i * 1.35, -2.0, 0])
            hh.align_to(ground, DOWN)
        self.sfx("pop")
        self.play(FadeIn(village, shift=UP * 0.4, rate_func=BOUNCE), run_time=0.8)
        du = dune(3.8, 1.7).move_to([5.1, -2.0, 0])
        du.align_to(ground, DOWN)
        self.sfx("whoosh")
        self.play(GrowFromEdge(du, DOWN, rate_func=BOUNCE), run_time=0.6)
        arrow = Arrow([2.6, -1.5, 0], [-0.6, -1.5, 0], color=REDA, stroke_width=9,
                      max_tip_length_to_length_ratio=0.16, buff=0.1)
        at = ar("زحف الرمال", 26, "BOLD", REDA).move_to([1.4, -0.55, 0])
        self.sfx("boing")
        self.play(GrowArrow(arrow), FadeIn(at, shift=DOWN * 0.2), run_time=0.7)
        # la dune AVANCE vers le village…
        self.sfx("whoosh")
        self.play(du.animate.shift(LEFT * 2.1), run_time=2.0,
                  rate_func=rf.ease_in_out_sine)
        # …le personnage surgit, inquiet
        kid = self.boy(1.9).move_to([-0.2, -1.6, 0])
        self.sfx("pop")
        self.play(FadeIn(kid, scale=0.3, rate_func=BOUNCE), run_time=0.7)
        self.play(Wiggle(kid), run_time=0.9)
        chips = VGroup()
        for i, (lab, col) in enumerate([("نواكشوط", GOLD), ("آدرار", ROSE)]):
            box = RoundedRectangle(corner_radius=0.22, width=2.5, height=0.75,
                                   fill_color=col, fill_opacity=0.94,
                                   stroke_color=INK, stroke_width=2.5
                                   ).move_to([1.6 - i * 3.2, 1.6, 0])
            bt = ar(lab, 24, "BOLD", "#FFFFFF").move_to(box)
            chips.add(VGroup(box, bt))
        self.sfx("ding")
        self.play(LaggedStart(*[GrowFromCenter(c, rate_func=BOUNCE) for c in chips],
                              lag_ratio=0.3), run_time=0.9)
        self.wait(max(d - 7.9, 0.2))
        self.clear_all()

    # ── 6. الحلول : bouclier, arbre qui pousse, robinet ────────────
    def s_sol(self):
        d = self.seg("sol1")                                        # 7.65
        head = titled("حلول لمكافحة التصحر", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # (1) حماية التربة : le bouclier TOMBE sur la butte de terre
        mound = Arc(radius=0.85, angle=PI, start_angle=0, fill_color="#B08850",
                    fill_opacity=1, stroke_color=INK, stroke_width=2.5
                    ).move_to([4.3, -0.9, 0])
        lb1 = ar("حماية التربة", 24, "BOLD", GOLD).move_to([4.3, -2.1, 0])
        self.sfx("pop")
        self.play(FadeIn(mound, shift=UP * 0.3), FadeIn(lb1), run_time=0.5)
        sh = shield(1.15).move_to([4.3, 4.3, 0])
        self.add(sh)
        self.sfx("boing")
        self.play(sh.animate.move_to([4.3, 0.05, 0]), run_time=0.8, rate_func=DROP)
        # (2) زراعة الأشجار : l'arbre POUSSE du sol
        soil = Line([-1.2, -1.0, 0], [1.2, -1.0, 0], color=SAND_EDGE, stroke_width=4)
        tr = tree(1.9).move_to([0, 0.0, 0])
        tr.align_to(soil, DOWN)
        lb2 = ar("زراعة الأشجار", 24, "BOLD", GREEN).move_to([0, -2.1, 0])
        self.add(soil)
        self.sfx("pop")
        self.play(GrowFromEdge(tr, DOWN), FadeIn(lb2), run_time=1.0)
        self.play(Wiggle(tr[1]), run_time=0.6)
        # (3) الماء بعقلانية : une seule goutte tombe du robinet
        fc = faucet(1.25).move_to([-4.3, 0.7, 0])
        lb3 = ar("الماء بعقلانية", 24, "BOLD", BLUE).move_to([-4.3, -2.1, 0])
        self.sfx("pop")
        self.play(FadeIn(fc, scale=0.4, rate_func=BOUNCE), FadeIn(lb3), run_time=0.6)
        dr = waterdrop(0.7).rotate(PI).move_to([-4.75, 0.05, 0])
        self.add(dr)
        self.sfx("ding")
        self.play(dr.animate.move_to([-4.75, -1.0, 0]), run_time=0.7, rate_func=DROP)
        self.wait(max(d - 5.1, 0.2))
        self.clear_all()

    # ── 7. الحزام الأخضر : les arbres POUSSENT et STOPPENT la dune ─
    def s_belt(self):
        d = self.seg("sol2")                                        # 9.38
        head = titled("الحزام الأخضر", 36, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        ground = Line([-6.5, -2.5, 0], [6.5, -2.5, 0], color=SAND_EDGE, stroke_width=4)
        self.play(Create(ground), run_time=0.3)
        village = VGroup(house_mr(0.78, ROSE, dome=True), house_mr(0.7, BLUE, dome=False))
        for i, hh in enumerate(village):
            hh.move_to([-4.9 + i * 1.25, -2.0, 0])
            hh.align_to(ground, DOWN)
        du = dune(3.2, 1.5).move_to([5.0, -2.0, 0])
        du.align_to(ground, DOWN)
        self.sfx("whoosh")
        self.play(GrowFromEdge(du, DOWN, rate_func=BOUNCE),
                  FadeIn(village, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.7)
        # la dune avance encore…
        self.sfx("whoosh")
        self.play(du.animate.shift(LEFT * 1.4), run_time=1.2,
                  rate_func=rf.ease_in_out_sine)
        # …mais la rangée d'arbres POUSSE DU SOL, un par un !
        trees = VGroup()
        for i in range(5):
            tr = tree(1.35, GREEN).move_to([1.6 - i * 0.62, -2.0, 0])
            tr.align_to(ground, DOWN)
            trees.add(tr)
        for tr in trees:
            self.sfx("pop")
            self.play(GrowFromEdge(tr, DOWN), run_time=0.35)
        # la dune essaie de pousser… et REBONDIT sur le mur d'arbres
        self.sfx("boing")
        self.play(du.animate.shift(LEFT * 0.5), run_time=0.8,
                  rate_func=rf.there_and_back)
        self.play(Flash(trees[2], color=GREEN, flash_radius=1.4), run_time=0.5)
        label = ar("الحزام الأخضر يوقف الرمال", 30, "BOLD", GREEN).move_to(UP * 1.6)
        lbox = SurroundingRectangle(label, color=GREEN, corner_radius=0.15, buff=0.25)
        self.sfx("ding")
        self.play(Create(lbox), FadeIn(label), run_time=0.9)
        self.wait(max(d - 7.9, 0.2))
        self.clear_all()

    # ── 8. مثال محلول : les barres GRANDISSENT depuis le sol ───────
    def s_example(self):
        d = self.seg("ex1")                                         # 9.57
        head = titled("مثال محلول: الغطاء النباتي", 32, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        base = -2.3
        floor = Line([-4.6, base, 0], [4.6, base, 0], color=SAND_EDGE, stroke_width=4)
        self.play(Create(floor), run_time=0.4)
        # barre 40٪ (قبل — à droite, sens RTL) : elle POUSSE du sol
        b1 = Rectangle(width=1.6, height=0.06, fill_color=GREEN, fill_opacity=0.9,
                       stroke_color=INK, stroke_width=2.5).move_to([2.6, base + 0.03, 0])
        self.add(b1)
        self.sfx("whoosh")
        self.play(b1.animate.stretch_to_fit_height(2.2).move_to([2.6, base + 1.1, 0]),
                  run_time=1.1, rate_func=rf.ease_out_back)
        # petit arbre sur la barre, pourcentage AU-DESSUS de l'arbre
        tr1 = tree(0.7).move_to([2.6, base + 2.55, 0])
        v1 = num("40%", 44, GREEN).next_to(tr1, UP, buff=0.2)
        l1 = ar("قبل", 26, "BOLD", INK).next_to(b1, DOWN, buff=0.25)
        self.sfx("pop")
        self.play(GrowFromEdge(tr1, DOWN),
                  FadeIn(v1, shift=UP * 0.3, rate_func=BOUNCE), FadeIn(l1), run_time=0.7)
        # barre 25٪ (بعد — à gauche)
        b2 = Rectangle(width=1.6, height=0.06, fill_color=GOLD, fill_opacity=0.9,
                       stroke_color=INK, stroke_width=2.5).move_to([-2.6, base + 0.03, 0])
        self.add(b2)
        self.sfx("whoosh")
        self.play(b2.animate.stretch_to_fit_height(1.38).move_to([-2.6, base + 0.69, 0]),
                  run_time=1.0, rate_func=rf.ease_out_back)
        dp = dead_plant(0.8).move_to([-2.6, base + 1.85, 0])
        v2 = num("25%", 44, GOLD).next_to(dp, UP, buff=0.2)
        l2 = ar("بعد", 26, "BOLD", INK).next_to(b2, DOWN, buff=0.25)
        self.sfx("pop")
        self.play(FadeIn(dp, shift=UP * 0.2),
                  FadeIn(v2, shift=UP * 0.3, rate_func=BOUNCE), FadeIn(l2), run_time=0.7)
        arrow = Arrow([1.5, 1.0, 0], [-1.4, 0.1, 0], color=REDA, stroke_width=8,
                      max_tip_length_to_length_ratio=0.15, buff=0.1)
        self.sfx("boing")
        self.play(GrowArrow(arrow), run_time=0.7)
        self.wait(max(d - 5.5, 0.2))

        d = self.seg("ex2")                                         # 7.29
        # les nombres SAUTENT un par un
        calc = VGroup(num("40", 46), num("−", 40, REDA), num("25", 46),
                      num("=", 42), num("15", 56, ROSE)).arrange(LEFT, buff=0.32)
        unit = ar("في المائة", 30, "BOLD", ROSE)
        row = VGroup(calc, unit).arrange(LEFT, buff=0.4).move_to([0, 2.05, 0])
        box = SurroundingRectangle(row, color=ROSE, corner_radius=0.15, buff=0.28)
        self.sfx("ding")
        self.play(LaggedStart(*[FadeIn(m, shift=DOWN * 0.5, scale=0.5, rate_func=BOUNCE)
                                for m in [*calc, unit]], lag_ratio=0.15), run_time=1.6)
        self.play(Create(box), run_time=0.5)
        self.play(Flash(calc[4], color=ROSE, flash_radius=1.3), run_time=0.7)
        tag = ar("انخفض الغطاء النباتي!", 28, "BOLD", REDA).move_to([0, 0.35, 0])
        self.sfx("tada")
        self.play(FadeIn(tag, scale=0.6, rate_func=BOUNCE), FadeOut(arrow), run_time=0.8)
        self.wait(max(d - 3.6, 0.2))
        self.clear_all()

    # ── 9. السور الأخضر الكبير : les arbres traversent la carte ────
    def s_astuce(self):
        d = self.seg("astuce")                                      # 11.59
        head = titled("سرّ أخضر", 34, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # carte simplifiée de la Mauritanie
        mmap = Polygon([-2.9, 0.9, 0], [-1.4, 1.9, 0], [2.5, 1.9, 0], [2.5, -0.1, 0],
                       [3.1, -0.5, 0], [1.6, -1.5, 0], [-0.8, -1.5, 0], [-2.0, -0.9, 0],
                       fill_color=SAND, fill_opacity=0.9,
                       stroke_color=GOLD, stroke_width=4).shift(DOWN * 0.35)
        self.sfx("whoosh")
        self.play(FadeIn(mmap, scale=0.6, rate_func=BOUNCE), run_time=1.0)
        # la ligne d'arbres POUSSE d'est en ouest à travers la carte
        belt = VGroup(*[tree(0.8, GREEN).move_to([2.1 - i * 0.68, -0.15, 0])
                        for i in range(7)])
        for tr in belt:
            self.sfx("pop")
            self.play(GrowFromEdge(tr, DOWN), run_time=0.28)
        banner = RoundedRectangle(corner_radius=0.25, width=10.6, height=1.0,
                                  fill_color=GREEN, fill_opacity=0.92,
                                  stroke_color=INK, stroke_width=2.5).move_to(UP * 2.25)
        bt = ar("مشروع السور الأخضر الكبير يمرّ عبر موريتانيا", 28, "BOLD", "#FFFFFF")
        if bt.width > 10.0:
            bt.scale_to_fit_width(10.0)
        bt.move_to(banner)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(banner, bt), rate_func=BOUNCE), run_time=0.9)
        # l'école plante son arbre !
        school = VGroup(house_mr(0.95, BLUE, dome=False))
        school.move_to([-4.7, -2.85, 0])
        sch_tr = tree(1.0).move_to([-3.5, -2.75, 0])
        txt = ar("مدرستك تشارك!", 28, "BOLD", ROSE).move_to([0.6, -2.95, 0])
        self.sfx("pop")
        self.play(FadeIn(school, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.6)
        self.sfx("pop")
        self.play(GrowFromEdge(sch_tr, DOWN), run_time=0.5)
        kid = self.boy(1.8).move_to([4.9, -2.7, 0])
        self.sfx("tada")
        self.play(FadeIn(txt, scale=0.5, rate_func=BOUNCE),
                  FadeIn(kid, scale=0.3, rate_func=BOUNCE), run_time=0.8)
        self.play(Wiggle(kid), run_time=0.9)
        self.wait(max(d - 8.5, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أعرّف التصحر وأذكر أسبابه",
            "أشرح عواقبه على الإنسان والبيئة",
            "أقترح حلولاً لمكافحة زحف الرمال",
        ])
        self.s_def()
        self.s_causes()
        self.s_effects()
        self.s_mr()
        self.s_sol()
        self.s_belt()
        self.s_example()
        self.s_astuce()
        self.s_outro_end("outro")
