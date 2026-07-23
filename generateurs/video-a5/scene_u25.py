# -*- coding: utf-8 -*-
"""Vidéo U25 — الفواصل.  Rendu : venv/bin/manim -qh scene_u25.py VideoU25
Cœur de la vidéo : le PIÈGE classique démontré — 100 m, un poteau tous les 10 m
← 11 poteaux (pas 10 !) comptés UN PAR UN à l'écran ; puis le cercle fermé
(6 poteaux = 6 فواصل) et les deux cas restants (دون طرفين −1 · طرف واحد =)."""
from manim import (VGroup, Rectangle, RoundedRectangle, Line, DoubleArrow, Circle, Cross,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter, LaggedStart,
                   Indicate, Wiggle, Flash,
                   UP, DOWN, LEFT, RIGHT, DEGREES)
import numpy as np

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


def poteau(x, y, color=LILA, h=0.55):
    return Rectangle(width=0.14, height=h, fill_color=color, fill_opacity=1,
                     stroke_color=INK, stroke_width=1.5).move_to([x, y, 0])


def rtl_row(pieces, buff=0.3):
    """Aligne des morceaux de DROITE à GAUCHE (le 1er est le plus à droite)."""
    for i in range(1, len(pieces)):
        pieces[i].next_to(pieces[i - 1], LEFT, buff=buff)
    return VGroup(*pieces)


class VideoU25(MajorScene):
    AUDIO = HERE / "audio_u25"
    UNIT_AR = "الوحدة 25"
    UNIT_COLOR = LILA
    TITLE = "الفواصل"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 25"

    # ── 2. المفهوم : ما الفاصلة؟ ────────────────────────────────
    def s_concept(self):
        d = self.seg("def1")
        head = titled("ما الفاصلة؟", 42, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        sol = Line(RIGHT * 3.4 + DOWN * 1.6, LEFT * 3.4 + DOWN * 1.6, color=INK, stroke_width=5)
        self.play(Create(sol), run_time=0.7)
        xs = [3.4, 1.13, -1.13, -3.4]        # 4 arbres plantés de droite à gauche
        arbres = VGroup(*[poteau(x, -1.3, GREEN) for x in xs])
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(a, shift=UP * 0.3, rate_func=BOUNCE) for a in arbres],
                              lag_ratio=0.25), run_time=1.2)
        fleche = DoubleArrow([3.4, -0.65, 0], [1.13, -0.65, 0], color=ROSE, stroke_width=5,
                             max_tip_length_to_length_ratio=0.15, buff=0)
        f_lab = ar("فاصلة", 28, "BOLD", ROSE).next_to(fleche, UP, buff=0.2)
        self.sfx("ding")
        self.play(Create(fleche), FadeIn(f_lab), run_time=1.0)
        self.wait(max(d - 3.8, 0.2))
        self.clear_all()

    # ── 3. الفخ المشهور : 100 م ← 11 عمودًا لا 10 ───────────────
    def s_piege(self):
        d = self.seg("piege1")
        head = titled("السؤال المشهور!", 40, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # données, de droite à gauche
        d1 = VGroup(num("100 m", 40), ar("طول الطريق", 22)).arrange(DOWN, buff=0.12)
        d1.move_to(RIGHT * 4.2 + UP * 1.6)
        d2 = VGroup(num("10 m", 40), ar("بين كل عمودين", 22)).arrange(DOWN, buff=0.12)
        d2.move_to(UP * 1.6)
        d3 = ar("وفي كل طرف عمود", 24, "BOLD", GOLD).move_to(LEFT * 4.2 + UP * 1.6)
        self.sfx("pop")
        self.play(FadeIn(d1, shift=LEFT * 0.3, rate_func=BOUNCE), run_time=0.7)
        self.sfx("pop")
        self.play(FadeIn(d2, shift=LEFT * 0.3, rate_func=BOUNCE), run_time=0.7)
        self.sfx("pop")
        self.play(FadeIn(d3, shift=LEFT * 0.3, rate_func=BOUNCE), run_time=0.7)
        sol = Line(RIGHT * 3.1 + DOWN * 2.2, LEFT * 3.1 + DOWN * 2.2, color=INK, stroke_width=5)
        z0 = num("0", 24, "#999999").move_to([3.1, -2.65, 0])
        z100 = num("100 m", 24, "#999999").move_to([-3.1, -2.65, 0])
        self.play(Create(sol), FadeIn(z0), FadeIn(z100), run_time=0.9)
        self.wait(max(d - 3.9, 0.2))

        d = self.seg("piege2")   # la mauvaise réponse
        self.guess = ar("عشرة أعمدة؟", 38, "BOLD", REDA).move_to(UP * 0.3)
        self.sfx("boing")
        self.play(FadeIn(self.guess, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 0.9, 0.2))

        d = self.seg("piege3")   # on compte les 11 poteaux UN PAR UN (RTL : du 0 à droite)
        self.poteaux = VGroup()
        for i in range(11):
            x = 3.1 - i * 0.62
            p = poteau(x, -1.9, LILA, h=0.5)
            c = num(str(i + 1), 26, INK if i < 10 else REDA).move_to([x, -1.35, 0])
            self.poteaux.add(VGroup(p, c))
            self.sfx("pop")
            self.play(FadeIn(self.poteaux[-1], shift=UP * 0.2, rate_func=BOUNCE), run_time=0.35)
        self.play(Indicate(self.poteaux[-1], color=REDA, scale_factor=1.5), run_time=0.8)
        self.wait(max(d - 4.65, 0.2))

        d = self.seg("piege4")   # 10 فواصل لكن 11 عمودًا
        croix = Cross(self.guess, stroke_color=REDA, stroke_width=6)
        self.sfx("boing")
        self.play(Create(croix), run_time=0.7)
        calc = rtl_row([num("100 ÷ 10 = 10", 40),
                        ar("فواصل", 26, "BOLD", BLUE)], buff=0.35).move_to(DOWN * 0.55 + RIGHT * 2.2)
        self.play(Write(calc), run_time=1.0)
        verdict = rtl_row([num("11", 54, GREEN),
                           ar("عمودًا!", 30, "BOLD", GREEN)], buff=0.3).move_to(DOWN * 0.55 + LEFT * 3.6)
        self.sfx("ding")
        self.play(FadeIn(verdict, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.play(Indicate(self.poteaux[0], color=GOLD, scale_factor=1.5), run_time=0.8)
        self.wait(max(d - 3.4, 0.2))
        self.clear_all()

    # ── 4. القاعدة الأولى : الأشياء = الفواصل + 1 ───────────────
    def s_regle(self):
        d = self.seg("regle1")
        contenu = rtl_row([ar("طرفان مشغولان: عدد الأشياء = عدد الفواصل", 28, "BOLD", "#FFFFFF"),
                           num("+ 1", 36, "#FFFFFF")], buff=0.3)
        boite = RoundedRectangle(corner_radius=0.25, width=contenu.width + 0.9, height=1.3,
                                 fill_color=GREEN, fill_opacity=0.95, stroke_color=INK,
                                 stroke_width=2).move_to(UP * 0.2)
        contenu.move_to(boite)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(boite, contenu), rate_func=BOUNCE), run_time=1.0)
        self.play(Indicate(contenu[1], color=YELL, scale_factor=1.4), run_time=0.8)
        self.wait(max(d - 1.8, 0.2))
        self.clear_all()

    # ── 5. الخط المغلق : الدائرة 6 = 6 ─────────────────────────
    def s_cercle(self):
        d = self.seg("cercle1")
        head = titled("الخط المغلق: الدائرة", 38, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        cercle = Circle(radius=1.7, stroke_color=BLUE, stroke_width=5).move_to(DOWN * 0.8)
        self.play(Create(cercle), run_time=1.0)
        pts = []
        for i in range(6):    # sens horaire = de droite à gauche en haut
            a = (90 - i * 60) * DEGREES
            pts.append([1.7 * np.cos(a), -0.8 + 1.7 * np.sin(a), 0])
        piquets = VGroup(*[Circle(radius=0.14, fill_color=ROSE, fill_opacity=1,
                                  stroke_color=INK, stroke_width=2).move_to(p) for p in pts])
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(p, scale=0.3, rate_func=BOUNCE) for p in piquets],
                              lag_ratio=0.2), run_time=1.5)
        self.wait(max(d - 3.4, 0.2))

        d = self.seg("cercle2")   # on compte les فواصل : 6 aussi
        t = 0
        for i in range(6):
            a = (60 - i * 60) * DEGREES   # milieu de chaque arc
            lab = num(str(i + 1), 28, BLUE).move_to(
                [2.25 * np.cos(a), -0.8 + 2.25 * np.sin(a), 0])
            self.sfx("pop")
            self.play(FadeIn(lab, scale=0.4, rate_func=BOUNCE), run_time=0.35)
            t += 0.35
        verdict = VGroup(num("6 = 6", 50, GREEN),
                         ar("الأشياء = الفواصل", 24, "BOLD", GREEN)).arrange(DOWN, buff=0.2)
        verdict.move_to(RIGHT * 4.6 + DOWN * 0.8)
        self.sfx("ding")
        self.play(FadeIn(verdict, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.play(Flash(verdict[0], color=GREEN, flash_radius=1.6), run_time=0.8)
        self.wait(max(d - t - 1.7, 0.2))
        self.clear_all()

    # ── 6. الحالتان الأخريان ────────────────────────────────────
    def s_cas(self):
        d = self.seg("cas1")
        head = titled("حالتان أخريان", 38, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # droite : دون الطرفين (3 poteaux, 4 فواصل)
        sol1 = Line(RIGHT * 5.6 + DOWN * 0.4, RIGHT * 1.0 + DOWN * 0.4, color=INK, stroke_width=4)
        p1 = VGroup(*[poteau(x, -0.12, ROSE, 0.45) for x in (4.45, 3.3, 2.15)])
        l1 = rtl_row([ar("دون الطرفين:", 24, "BOLD", REDA), num("− 1", 32, REDA)],
                     buff=0.25).move_to(RIGHT * 3.3 + DOWN * 1.3)
        self.sfx("pop")
        self.play(Create(sol1), FadeIn(p1, shift=UP * 0.2), FadeIn(l1), run_time=1.1)
        # gauche : طرف واحد (4 poteaux, 4 فواصل)
        sol2 = Line(LEFT * 1.0 + DOWN * 0.4, LEFT * 5.6 + DOWN * 0.4, color=INK, stroke_width=4)
        p2 = VGroup(*[poteau(x, -0.12, GREEN, 0.45) for x in (-1.0, -2.15, -3.3, -4.45)])
        l2 = rtl_row([ar("طرف واحد: يتساويان", 24, "BOLD", GREEN)]).move_to(LEFT * 3.3 + DOWN * 1.3)
        self.sfx("pop")
        self.play(Create(sol2), FadeIn(p2, shift=UP * 0.2), FadeIn(l2), run_time=1.1)
        self.wait(max(d - 3.1, 0.2))
        self.clear_all()

    # ── 7. انتبه : الدائرة لا تزيد واحدًا ───────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! في الدائرة لا نزيد واحدًا", 34, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        box = RoundedRectangle(corner_radius=0.22, width=6.2, height=1.15, fill_color=ROSE,
                               fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.1 + DOWN * 0.4)
        boxt = ar("عدد الأشياء = عدد الفواصل تمامًا", 28, "BOLD", "#FFFFFF").move_to(box)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(box, boxt), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.0, 0.2))
        self.clear_all()

    # ── 8. السر : ارسم قبل أن تحسب ──────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: ارسم قبل أن تحسب", 36, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        croquis = Line(RIGHT * 2.4 + DOWN * 0.6, LEFT * 2.4 + DOWN * 0.6,
                       color=INK, stroke_width=4)
        self.sfx("whoosh")
        self.play(Create(croquis), run_time=0.9)
        pts = VGroup(*[Circle(radius=0.12, fill_color=REDA, fill_opacity=1,
                              stroke_color=INK, stroke_width=2).move_to([x, -0.6, 0])
                       for x in (2.4, 0.8, -0.8, -2.4)])
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(p, scale=0.3, rate_func=BOUNCE) for p in pts],
                              lag_ratio=0.25), run_time=1.2)
        slogan = ar("خط ونقاط!", 34, "BOLD", ROSE).move_to(DOWN * 1.9)
        self.sfx("ding")
        self.play(Write(slogan), run_time=1.0)
        self.wait(max(d - 4.1, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أميّز الخط المغلق والخط المفتوح",
            "أختار القاعدة: أزيد واحدًا أو أنقص أو لا شيء",
            "أحل مسائل الأشجار والأعمدة",
        ])
        self.s_concept()
        self.s_piege()
        self.s_regle()
        self.s_cercle()
        self.s_cas()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
