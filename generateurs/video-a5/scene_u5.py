# -*- coding: utf-8 -*-
"""Vidéo U5 — القسمة.  Rendu : venv/bin/manim -qh scene_u5.py VideoU5
Cœur de la vidéo : la division se FAIT à l'écran — des تمرات (points dorés) se
déplacent une à une dans des أطباق (assiettes), puis القسمة مع الباقي : les deux
تمرات restantes restent dehors, en rouge."""
from manim import (VGroup, Ellipse, Circle, RoundedRectangle,
                   FadeIn, FadeOut, Write, Create, Transform, GrowFromCenter,
                   Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)

DATE_COL = "#d78d33"     # couleur تمرة (datte)
PLATE_XS = [3.2, 0.0, -3.2]          # طبق 1 à droite (RTL)
SLOTS = [(-0.62, 0.12), (-0.21, -0.16), (0.21, 0.12), (0.62, -0.16)]


def date_dot():
    return Circle(radius=0.17, fill_color=DATE_COL, fill_opacity=1,
                  stroke_color=INK, stroke_width=2)


def plate():
    return Ellipse(width=2.4, height=1.4, fill_color="#FFFFFF", fill_opacity=0.92,
                   stroke_color=DATE_COL, stroke_width=3)


class VideoU5(MajorScene):
    AUDIO = HERE / "audio_u5"
    UNIT_AR = "الوحدة 5"
    UNIT_COLOR = LILA
    TITLE = "القسمة"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 5"

    def make_dates(self, n, cols):
        """n تمرات en grille 2 lignes, remplie de droite à gauche (RTL)."""
        g = VGroup()
        x0 = (cols - 1) * 0.55
        for i in range(n):
            r, c = divmod(i, cols)
            d = date_dot().move_to([x0 - c * 1.1, 1.55 - r * 0.6, 0])
            g.add(d)
        return g

    # ── 2. التوزيع بالتساوي : 12 ÷ 3 = 4 ───────────────────────
    def s_partage(self):
        d = self.seg("def1")
        head = titled("القسمة: توزيع إلى حصص متساوية", 36, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        dates = self.make_dates(12, 6)
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(t, scale=0.3, rate_func=BOUNCE) for t in dates],
                              lag_ratio=0.06), run_time=1.5)
        plates = VGroup(*[plate().move_to([x, -1.7, 0]) for x in PLATE_XS])
        self.sfx("pop")
        self.play(LaggedStart(*[GrowFromCenter(p, rate_func=BOUNCE) for p in plates],
                              lag_ratio=0.15), run_time=1.0)
        self.wait(max(d - 3.4, 0.2))

        # dist1 : tour par tour, une تمرة par طبق (les points SE DÉPLACENT)
        d = self.seg("dist1")
        for r in range(4):                       # 4 tours de distribution
            self.sfx("pop")
            self.play(*[dates[3 * r + p].animate.move_to(
                [PLATE_XS[p] + SLOTS[r][0], -1.7 + SLOTS[r][1], 0])
                for p in range(3)], run_time=0.7)
        self.wait(max(d - 2.8, 0.2))

        # dist2 : 4 dans chaque طبق
        d = self.seg("dist2")
        fours = VGroup()
        t = 0
        for p in range(3):                       # droite → gauche (RTL)
            grp = VGroup(plates[p], *[dates[3 * r + p] for r in range(4)])
            self.play(Indicate(grp, color=GREEN, scale_factor=1.12), run_time=0.7)
            f = num("4", 40, GREEN).move_to([PLATE_XS[p], -2.85, 0])
            self.sfx("pop")
            self.play(FadeIn(f, shift=UP * 0.25, rate_func=BOUNCE), run_time=0.5)
            fours.add(f)
            t += 1.2
        self.wait(max(d - t, 0.2))

        # def2 : 12 ÷ 3 = 4 + المقسوم / المقسوم عليه / خارج القسمة
        d = self.seg("def2")
        eq = num("12 ÷ 3 = 4", 58).move_to([0, 0.55, 0])
        self.sfx("ding")
        self.play(Write(eq), run_time=1.2)
        # eq sans espaces : 1 2 ÷ 3 = 4  → indices 0..5
        l1 = ar("المقسوم", 24, "BOLD", LILA).next_to(VGroup(eq[0], eq[1]), DOWN, buff=0.3)
        l2 = ar("المقسوم عليه", 24, "BOLD", BLUE).next_to(eq[3], DOWN, buff=0.9)
        l3 = ar("خارج القسمة", 24, "BOLD", GREEN).next_to(eq[5], DOWN, buff=0.3)
        self.wait(1.0)
        self.sfx("pop")
        self.play(FadeIn(l1, shift=UP * 0.2), VGroup(eq[0], eq[1]).animate.set_color(LILA),
                  run_time=0.8)
        self.sfx("pop")
        self.play(FadeIn(l2, shift=UP * 0.2), eq[3].animate.set_color(BLUE), run_time=0.8)
        self.sfx("pop")
        self.play(FadeIn(l3, shift=UP * 0.2), eq[5].animate.set_color(GREEN), run_time=0.8)
        self.wait(max(d - 4.6, 0.2))
        self.clear_all()

    # ── 3. الطريقة : أبحث في جدول الضرب ─────────────────────────
    def s_table_mult(self):
        d = self.seg("mult1")
        head = titled("أبحث في جدول الضرب", 42, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        q = num("3 × ? = 12", 62).move_to([0, 0.7, 0])
        q[2].set_color(REDA)                     # le « ? » en rouge
        self.play(Write(q), run_time=1.2)
        self.wait(max(d - 2.1, 0.2))

        d = self.seg("mult2")
        a = num("3 × 4 = 12", 62).move_to([0, 0.7, 0])
        a[2].set_color(GREEN)
        self.sfx("whoosh")
        self.play(Transform(q, a), run_time=1.0)
        concl = num("12 ÷ 3 = 4", 54, LILA).move_to([0, -0.9, 0])
        self.sfx("ding")
        self.play(FadeIn(concl, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.play(Flash(concl, color=LILA, flash_radius=2.2), run_time=0.9)
        self.wait(max(d - 2.8, 0.2))
        self.clear_all()

    # ── 4. القسمة مع الباقي : 14 ÷ 3 = 4 والباقي 2 ─────────────
    def s_reste(self):
        d = self.seg("rem1")
        head = titled("القسمة مع الباقي", 42, REDA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        dates = self.make_dates(14, 7)
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(t, scale=0.3, rate_func=BOUNCE) for t in dates],
                              lag_ratio=0.05), run_time=1.5)
        plates = VGroup(*[plate().move_to([x, -1.7, 0]) for x in PLATE_XS])
        self.sfx("pop")
        self.play(LaggedStart(*[GrowFromCenter(p, rate_func=BOUNCE) for p in plates],
                              lag_ratio=0.15), run_time=1.0)
        self.wait(max(d - 3.4, 0.2))

        # rem2 : 12 distribuées, 2 restent dehors en ROUGE
        d = self.seg("rem2")
        for r in range(4):
            self.sfx("pop")
            self.play(*[dates[3 * r + p].animate.move_to(
                [PLATE_XS[p] + SLOTS[r][0], -1.7 + SLOTS[r][1], 0])
                for p in range(3)], run_time=0.7)
        left1, left2 = dates[12], dates[13]
        self.sfx("boing")
        self.play(left1.animate.set_fill(REDA).move_to([2.95, 0.95, 0]),
                  left2.animate.set_fill(REDA).move_to([2.35, 0.95, 0]), run_time=1.0)
        lab_r = ar("الباقي", 26, "BOLD", REDA).move_to([2.65, 0.4, 0])
        self.sfx("ding")
        self.play(FadeIn(lab_r, shift=UP * 0.2, rate_func=BOUNCE), run_time=0.6)
        self.wait(max(d - 4.4, 0.2))

        # rem3 : l'écriture 14 ÷ 3 = 4 والباقي 2
        d = self.seg("rem3")
        eq = num("14 ÷ 3 = 4", 50)
        w_rest = ar("والباقي", 28, "BOLD", REDA).next_to(eq, LEFT, buff=0.4)
        n_rest = num("2", 50, REDA).next_to(w_rest, LEFT, buff=0.35)
        line = VGroup(eq, w_rest, n_rest).move_to([-0.4, -0.15, 0])
        self.sfx("pop")
        self.play(Write(line), run_time=1.4)
        self.play(Indicate(VGroup(left1, left2), color=REDA, scale_factor=1.4), run_time=0.8)
        self.wait(max(d - 2.2, 0.2))

        # rem4 : le تحقق — 3×4=12 puis 12+2=14
        d = self.seg("rem4")
        self.sfx("whoosh")
        self.play(FadeOut(plates), *[FadeOut(dates[i]) for i in range(12)], run_time=0.6)
        c1 = num("3 × 4 = 12", 44, GREEN).move_to([0, -1.35, 0])
        c2 = num("12 + 2 = 14", 44, GREEN).move_to([0, -2.2, 0])
        self.sfx("pop")
        self.play(Write(c1), run_time=1.0)
        self.sfx("pop")
        self.play(Write(c2), run_time=1.0)
        self.sfx("ding")
        self.play(Flash(c2, color=GREEN, flash_radius=2.4), run_time=0.9)
        self.wait(max(d - 3.5, 0.2))
        self.clear_all()

    # ── 5. انتبه : الترتيب مهم ──────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! الترتيب مهم في القسمة", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=4.2, height=1.05, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to([2.9, 0.8, 0])
        c1t = num("12 ÷ 2 = 6", 38, "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=4.2, height=1.05, fill_color=ROSE,
                              fill_opacity=0.92, stroke_color=INK).move_to([2.9, -1.3, 0])
        c2t = num("2 ÷ 12", 38, "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.8)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.8)
        neq = num("≠", 54, REDA).move_to([2.9, -0.25, 0])
        self.sfx("boing")
        self.play(GrowFromCenter(neq, rate_func=BOUNCE), run_time=0.8)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 4.5, 0.2))
        self.clear_all()

    # ── 6. السر : ÷1 و ÷ نفسه ───────────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ صغير قبل أن نفترق", 42, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.6)
        lab1 = ar("يبقى كما هو", 28, "BOLD", GOLD).move_to([3.4, 0.6, 0])
        eq1 = num("9 ÷ 1 = 9", 48, GREEN).move_to([-1.6, 0.6, 0])
        self.sfx("pop")
        self.play(FadeIn(lab1, shift=LEFT * 0.4, rate_func=BOUNCE), Write(eq1), run_time=1.1)
        self.wait(1.0)
        lab2 = ar("يساوي واحدًا", 28, "BOLD", GOLD).move_to([3.4, -0.9, 0])
        eq2 = num("7 ÷ 7 = 1", 48, BLUE).move_to([-1.6, -0.9, 0])
        self.sfx("pop")
        self.play(FadeIn(lab2, shift=LEFT * 0.4, rate_func=BOUNCE), Write(eq2), run_time=1.1)
        self.sfx("ding")
        self.play(Flash(VGroup(eq1, eq2), color=LILA, flash_radius=3.0), run_time=0.9)
        self.wait(max(d - 5.7, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أفهم القسمة على أنها توزيع بالتساوي",
            "أستعمل جداول الضرب لأجد خارج القسمة",
            "أحسب القسمة مع الباقي",
        ])
        self.s_partage()
        self.s_table_mult()
        self.s_reste()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
