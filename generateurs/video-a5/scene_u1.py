# -*- coding: utf-8 -*-
"""Vidéo explicative U1 — الأعداد الكبيرة (v3 : synchro fine + vocabulaire du cahier).
Rendu :  venv/bin/manim -qm scene_u1.py VideoU1
Principe : 1 phrase de narration = 1 chunk audio (audio_u1/) = 1 bloc d'animation.
Chaque seg() lance l'audio au temps courant du rendu → la synchro est structurelle.
Vocabulaire = page U1 du cahier : خانة · خانات الأعداد · الصيغة القياسية/التفكيكية/اللفظية."""
import json
import random
from pathlib import Path

from manim import (Scene, Text, MarkupText, VGroup, Rectangle, RoundedRectangle,
                   Circle, Star, Line, Arrow, SurroundingRectangle, Cross,
                   ImageMobject, SVGMobject,
                   FadeIn, FadeOut, Write, Create, LaggedStart, Transform, GrowFromCenter,
                   Indicate, Wiggle, Flash,
                   UP, DOWN, LEFT, RIGHT, DL, DR, UL, UR, ORIGIN, config,
                   rate_functions as rf)

HERE = Path(__file__).parent
AUDIO = HERE / "audio_u1"
SFX = HERE / "sfx"
DUR = json.loads((AUDIO / "durations.json").read_text())

BG = "#FFF9EF"
INK = "#3A3A3A"
YELL = "#F6C445"
ROSE = "#EF6292"
GREEN = "#5BB86A"
BLUE = "#4A9DE0"
LILA = "#A47FDB"
REDA = "#E05252"
ROYAL = "#2563eb"
PALETTE = [YELL, ROSE, GREEN, BLUE, LILA]

config.background_color = BG
BOUNCE = rf.ease_out_back


def ar(txt, size=40, weight="NORMAL", color=INK):
    # MarkupText obligatoire : Text perd des glyphes sur l'arabe façonné
    return MarkupText(txt, font="Noto Sans Arabic", font_size=size, weight=weight, color=color)


def num(txt, size=54, color=INK, weight="BOLD"):
    return Text(txt, font="DejaVu Sans", font_size=size, weight=weight, color=color)


def chip(color):
    return Star(n=5, outer_radius=0.28, inner_radius=0.13, fill_color=color,
                fill_opacity=1, stroke_color=INK, stroke_width=1.5)


def titled(txt, size, color):
    t = ar(txt, size, "BOLD", color)
    c = chip(color).next_to(t, RIGHT, buff=0.35)
    return VGroup(t, c).to_edge(UP, buff=0.55)


class VideoU1(Scene):
    # ── infrastructure ──────────────────────────────────────────
    def seg(self, name):
        """Audio du chunk au temps courant ; retourne (durée, temps déjà consommé=0)."""
        self.add_sound(str(AUDIO / f"{name}.mp3"))
        return DUR[name]

    def sfx(self, name):
        self.add_sound(str(SFX / f"{name}.wav"))

    def clear_all(self):
        ms = [m for m in self.mobjects if id(m) not in self.keep]
        if ms:
            self.sfx("whoosh")
            self.play(*[FadeOut(m, shift=DOWN * 0.3) for m in ms], run_time=0.6)

    def boy(self, height=2.0):
        return SVGMobject(str(HERE / "assets/perso-garcon.svg")).scale_to_fit_height(height)

    def make_decor(self):
        rng = random.Random(6)
        decor = VGroup()
        # coins droits + bas-gauche : le logo occupe le haut-gauche
        spots = [(6.5, 3.1), (6.6, 0.5), (5.7, -3.2), (-6.5, -3.1), (-6.6, 1.4), (-5.6, -1.2)]
        for i, (x, y) in enumerate(spots):
            col = PALETTE[i % len(PALETTE)]
            if i % 2 == 0:
                m = Circle(radius=rng.uniform(0.18, 0.38), fill_color=col,
                           fill_opacity=0.30, stroke_width=0)
            else:
                m = Star(n=5, outer_radius=rng.uniform(0.16, 0.3), inner_radius=0.09,
                         fill_color=col, fill_opacity=0.40, stroke_width=0)
            m.move_to([x, y, 0]).rotate(rng.uniform(0, 3))
            decor.add(m)
        return decor

    # ── 1. INTRO ────────────────────────────────────────────────
    def s_intro(self):
        d = self.seg("intro1")
        self.logo = ImageMobject(str(HERE / "assets/major-logo.png"))
        self.logo.scale_to_fit_height(2.2).move_to(ORIGIN)
        brand = Text("Major", font="DejaVu Sans", weight="BOLD",
                     font_size=64, color=ROYAL).next_to(self.logo, DOWN, buff=0.35)
        self.sfx("ding")
        self.play(FadeIn(self.logo, scale=0.4, rate_func=BOUNCE),
                  FadeIn(brand, shift=UP * 0.2), run_time=1.3)
        self.wait(0.4)
        # → filigrane EN HAUT À GAUCHE (demande utilisateur)
        self.play(FadeOut(brand),
                  self.logo.animate.scale_to_fit_height(0.8).to_corner(UL, buff=0.3),
                  run_time=1.0)
        self.keep.add(id(self.logo))
        badge = RoundedRectangle(corner_radius=0.25, width=3.2, height=0.9,
                                 fill_color=YELL, fill_opacity=1, stroke_color=INK,
                                 stroke_width=2).shift(UP * 2.4)
        badge_t = ar("الوحدة 1", 34, "BOLD").move_to(badge)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(badge, badge_t), rate_func=BOUNCE), run_time=0.8)
        title = ar("الأعداد الكبيرة", 80, "BOLD").shift(UP * 0.55)
        self.play(Write(title), run_time=1.8)
        garcon = self.boy(2.1).to_corner(DR, buff=0.25)
        self.sfx("pop")
        self.play(FadeIn(garcon, scale=0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 6.2, 0.2))

        d = self.seg("intro2")   # objectifs du cahier
        obj1 = ar("أقرأ الأعداد الكبيرة وأكتبها بالأرقام والحروف", 32)
        obj2 = ar("أضع كل رقم في خانته الصحيحة", 32)
        s1 = chip(GREEN).scale(0.55)
        s2 = chip(BLUE).scale(0.55)
        r1 = VGroup(obj1, s1)
        r2 = VGroup(obj2, s2)
        s1.next_to(obj1, RIGHT, buff=0.3)
        s2.next_to(obj2, RIGHT, buff=0.3)
        r1.move_to(DOWN * 0.7).to_edge(RIGHT, buff=1.0)
        r2.move_to(DOWN * 1.55).to_edge(RIGHT, buff=1.0)
        self.sfx("pop")
        self.play(FadeIn(r1, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.1)
        self.sfx("pop")
        self.play(FadeIn(r2, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.1)
        rule = ar("أُشاهد ← أرسم ← أحسب", 30, "BOLD", color=ROSE).shift(DOWN * 2.7 + LEFT * 1.6)
        rule_box = SurroundingRectangle(rule, color=ROSE, corner_radius=0.15, buff=0.22)
        self.play(Create(rule_box), FadeIn(rule), run_time=1.3)
        self.wait(max(d - 3.5, 0.2))
        self.clear_all()

    # ── 2. القاعدة ──────────────────────────────────────────────
    def s_regle(self):
        d = self.seg("regle1")   # de l'ألف au مليون
        head = titled("الأعداد الكبيرة تمتد من الألف إلى المليون وأكثر", 36, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.8)
        n_alf = num("1 000", 60, color=GREEN).shift(RIGHT * 4 + UP * 0.7)
        l_alf = ar("ألف", 30, "BOLD", GREEN).next_to(n_alf, DOWN, buff=0.3)
        n_mil = num("1 000 000", 60, color=LILA).shift(LEFT * 3.4 + UP * 0.7)
        l_mil = ar("مليون", 30, "BOLD", LILA).next_to(n_mil, DOWN, buff=0.3)
        arrow = Arrow(n_alf.get_left() + LEFT * 0.2, n_mil.get_right() + RIGHT * 0.2,
                      color=INK, stroke_width=5)
        plus = ar("وأكثر...", 30, color="#777777").shift(DOWN * 1.8)
        self.play(FadeIn(VGroup(n_alf, l_alf), scale=0.6, rate_func=BOUNCE), run_time=0.8)
        self.play(Create(arrow), run_time=0.7)
        self.sfx("pop")
        self.play(FadeIn(VGroup(n_mil, l_mil), scale=0.6, rate_func=BOUNCE), run_time=0.8)
        self.play(FadeIn(plus), run_time=0.5)
        self.wait(max(d - 3.6, 0.2))

        d = self.seg("regle2")   # grouper 3 par 3
        self.play(FadeOut(VGroup(n_alf, l_alf, n_mil, l_mil, arrow, plus)),
                  FadeOut(head), run_time=0.5)
        head2 = titled("نجمع الأرقام ثلاثةً ثلاثةً انطلاقًا من اليمين", 36, BLUE)
        self.play(FadeIn(head2, shift=DOWN * 0.3), run_time=0.7)
        raw = num("245000", 96).shift(UP * 0.3)
        self.play(Write(raw), run_time=1.0)
        self.wait(1.6)
        grouped = num("245 000", 96).shift(UP * 0.3)
        self.sfx("whoosh")
        self.play(Transform(raw, grouped), run_time=1.2)
        self.sfx("ding")
        u_k = Line(LEFT * 0.9, RIGHT * 0.9, color=GREEN, stroke_width=7).next_to(grouped, DOWN, buff=0.25).shift(LEFT * 1.55)
        u_u = Line(LEFT * 0.9, RIGHT * 0.9, color=BLUE, stroke_width=7).next_to(grouped, DOWN, buff=0.25).shift(RIGHT * 1.6)
        self.play(Create(u_u), run_time=0.6)   # d'abord la droite (اليمين)
        self.play(Create(u_k), run_time=0.6)
        self.wait(max(d - 5.7, 0.2))

        d = self.seg("regle3")   # les noms des groupes
        lab = ar("أسماء المجموعات", 32, "BOLD", LILA).shift(DOWN * 0.85)
        self.play(FadeIn(lab, shift=UP * 0.3), run_time=0.9)
        self.wait(2.2)
        names = [("الوحدات", BLUE, 4.9), ("الآلاف", GREEN, 1.65), ("الملايين", YELL, -1.65), ("المليارات", ROSE, -4.9)]
        for txt, col, x in names:     # de droite à gauche, au rythme de l'énumération
            b = RoundedRectangle(corner_radius=0.18, width=2.9, height=0.85,
                                 fill_color=col, fill_opacity=0.9, stroke_color=INK, stroke_width=1.5)
            bt = ar(txt, 30, "BOLD", "#FFFFFF" if col != YELL else INK).move_to(b)
            g = VGroup(b, bt).move_to([x, -2.3, 0])
            self.sfx("pop")
            self.play(FadeIn(g, scale=0.4, rate_func=BOUNCE), run_time=0.75)
            self.wait(0.95)
        self.wait(max(d - 3.1 - 4 * 1.7, 0.2))
        self.clear_all()

    # ── 3. خانات الأعداد : une colonne PAR CHIFFRE ──────────────
    def s_tableau(self):
        d = self.seg("tab1")
        head = titled("خانات الأعداد", 42, GREEN)
        # de droite à gauche : وحدات، عشرات، مئات (bleu) puis آلاف، عشرات الآلاف، مئات الآلاف (vert)
        cols = [("الوحدات", BLUE, 5.45), ("العشرات", BLUE, 3.25), ("المئات", BLUE, 1.05),
                ("الآلاف", GREEN, -1.15), ("عشرات الآلاف", GREEN, -3.35), ("مئات الآلاف", GREEN, -5.55)]
        headers, cells = VGroup(), []
        for txt, col, x in cols:
            h = Rectangle(width=2.15, height=0.95, fill_color=col, fill_opacity=0.9,
                          stroke_color=INK).move_to([x, 0.85, 0])
            ht = ar(txt, 19, "BOLD", "#FFFFFF").move_to(h)
            c = Rectangle(width=2.15, height=1.25, stroke_color=INK).move_to([x, -0.25, 0])
            headers.add(VGroup(h, ht))
            cells.append(c)
        table = VGroup(headers, *cells)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), Create(table), run_time=2.0)
        self.wait(1.6)
        for i in range(6):    # énumération des 6 خانات, de droite à gauche
            self.play(Indicate(headers[i], scale_factor=1.13), run_time=0.75)
            self.wait(0.35)
        self.wait(max(d - 3.6 - 6 * 1.1, 0.2))

        d = self.seg("tab2")   # chaque chiffre vole dans SA خانة, de droite à gauche
        n = num("245 000", 46).shift(UP * 2.1 + LEFT * 0.2)
        self.play(FadeIn(n, scale=0.6), run_time=0.9)
        self.wait(3.2)
        # glyphes de « 245 000 » : idx 0..5 = 2,4,5,0,0,0 ; on part de la droite (idx 5)
        order = [(5, BLUE), (4, BLUE), (3, BLUE), (2, GREEN), (1, GREEN), (0, GREEN)]
        for k, (idx, col) in enumerate(order):
            digit = num("245000"[idx], 58, color=col)
            digit.move_to(n[idx].get_center())
            self.sfx("pop" if col == BLUE else "ding")
            self.play(digit.animate.move_to(cells[k]), run_time=0.8)
            self.wait(0.75)
        self.wait(max(d - 4.1 - 6 * 1.55, 0.2))

        d = self.seg("tab3")   # lecture
        strip = RoundedRectangle(corner_radius=0.2, width=9.4, height=1,
                                 fill_color=ROSE, fill_opacity=0.15, stroke_color=ROSE).shift(DOWN * 2.2)
        reading = ar("مئتان وخمسة وأربعون ألفًا", 38, "BOLD", ROSE).move_to(strip)
        self.sfx("ding")
        self.play(Create(strip), Write(reading), run_time=2.0)
        self.play(Indicate(reading, color=ROSE), run_time=1.0)
        self.wait(max(d - 3.0, 0.2))
        self.clear_all()

    # ── 4. الصيغ الثلاث (vocabulaire du cahier) ────────────────
    def sigh_row(self, label, color, content, y):
        b = RoundedRectangle(corner_radius=0.2, width=4.0, height=0.85,
                             fill_color=color, fill_opacity=0.92, stroke_color=INK, stroke_width=1.5)
        bt = ar(label, 28, "BOLD", "#FFFFFF" if color != YELL else INK).move_to(b)
        lab = VGroup(b, bt).move_to([3.4, y, 0])
        content.next_to(lab, LEFT, buff=0.7)
        return lab, content

    def s_sighat(self):
        d = self.seg("sigh1")
        head = titled("الصيغ الثلاث للعدد", 42, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(3.4)
        lab1, c1 = self.sigh_row("الصيغة القياسية", BLUE, num("245 000", 52, BLUE), 1.15)
        self.sfx("pop")
        self.play(FadeIn(VGroup(lab1, c1), shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.1)
        self.wait(max(d - 5.4, 0.2))

        d = self.seg("sigh2")
        lab2, c2 = self.sigh_row("الصيغة التفكيكية", GREEN, num("245 × 1 000", 52, GREEN), -0.15)
        self.sfx("pop")
        self.play(FadeIn(VGroup(lab2, c2), shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.1)
        self.play(Indicate(c2, color=GREEN), run_time=1.0)
        self.wait(max(d - 2.1, 0.2))

        d = self.seg("sigh3")
        lab3, c3 = self.sigh_row("الصيغة اللفظية", ROSE,
                                 ar("مئتان وخمسة وأربعون ألفًا", 30, "BOLD", ROSE), -1.45)
        self.sfx("pop")
        self.play(FadeIn(VGroup(lab3, c3), shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.1)
        self.wait(max(d - 1.1, 0.2))
        self.clear_all()

    # ── 5. الطريقة — appliquée pas à pas sur 6 084 512 ─────────
    def step_row(self, n, txt, color):
        bub = RoundedRectangle(corner_radius=0.28, width=0.8, height=0.8,
                               fill_color=color, fill_opacity=1, stroke_color=INK)
        bub_t = num(n, 34, color="#FFFFFF" if color != YELL else INK).move_to(bub)
        t = ar(txt, 28)
        t.next_to(bub, LEFT, buff=0.45)
        return VGroup(t, VGroup(bub, bub_t)).move_to(DOWN * 1.15)

    def mini_label(self, txt, color, x, y):
        b = RoundedRectangle(corner_radius=0.15, width=2.1, height=0.6,
                             fill_color=color, fill_opacity=0.92, stroke_color=INK, stroke_width=1.2)
        bt = ar(txt, 24, "BOLD", "#FFFFFF" if color != YELL else INK).move_to(b)
        return VGroup(b, bt).move_to([x, y, 0])

    def s_methode(self):
        d = self.seg("meth0")
        head = titled("كيف أقرأ عددًا كبيرًا؟", 44, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(2.2)
        raw = num("6084512", 84).shift(UP * 1.45)
        self.play(Write(raw), run_time=1.4)
        self.wait(max(d - 4.6, 0.2))

        # étape 1 : grouper — le nombre se regroupe SOUS LES YEUX, de la droite
        d = self.seg("meth1")
        step = self.step_row("1", "أجمع الأرقام ثلاثةً ثلاثةً انطلاقًا من اليمين", YELL)
        self.sfx("pop")
        self.play(FadeIn(step, shift=LEFT * 0.6, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.6)
        grouped = num("6 084 512", 84).shift(UP * 1.45)
        self.sfx("whoosh")
        self.play(Transform(raw, grouped), run_time=1.2)
        g_mill = VGroup(*grouped[0:1])
        g_th = VGroup(*grouped[1:4])
        g_un = VGroup(*grouped[4:7])
        y_line = grouped.get_bottom()[1] - 0.18
        lines = []
        for g, col in ((g_un, BLUE), (g_th, GREEN), (g_mill, YELL)):   # droite → gauche
            ln = Line([g.get_left()[0] - 0.05, y_line, 0], [g.get_right()[0] + 0.05, y_line, 0],
                      color=col, stroke_width=7)
            lines.append(ln)
            self.sfx("pop")
            self.play(Create(ln), run_time=0.5)
        self.sfx("ding")
        self.wait(max(d - 5.3, 0.2))

        # étape 2 : lire chaque groupe avec son nom
        d = self.seg("meth2a")
        step2 = self.step_row("2", "أقرأ كل مجموعة وأتبعها باسمها", GREEN)
        self.play(FadeOut(step, shift=DOWN * 0.3), run_time=0.4)
        self.play(FadeIn(step2, shift=LEFT * 0.6), run_time=0.6)
        self.wait(max(d - 1.0, 0.2))

        # la lecture s'écrit progressivement en bas, partie par partie (RTL)
        p1 = ar("ستة ملايين", 28, "BOLD", "#C99A1F")   # or foncé : plus lisible que YELL sur fond crème
        p2 = ar("وأربعة وثمانون ألفًا", 28, "BOLD", GREEN)
        p3 = ar("وخمسمائة واثنا عشر", 28, "BOLD", BLUE)
        p2.next_to(p1, LEFT, buff=0.28)
        p3.next_to(p2, LEFT, buff=0.28)
        reading = VGroup(p1, p2, p3)
        reading.move_to(DOWN * 2.35)

        d = self.seg("meth2b")   # « ستة ملايين »
        lab_m = self.mini_label("الملايين", YELL, g_mill.get_center()[0], y_line - 0.55)
        self.sfx("pop")
        self.play(FadeIn(lab_m, scale=0.4, rate_func=BOUNCE),
                  Indicate(g_mill, color=YELL, scale_factor=1.25), run_time=1.1)
        self.play(Write(p1), run_time=1.2)
        self.wait(max(d - 2.3, 0.2))

        d = self.seg("meth2c")   # « وأربعة وثمانون ألفًا »
        lab_t = self.mini_label("الآلاف", GREEN, g_th.get_center()[0], y_line - 0.55)
        self.sfx("pop")
        self.play(FadeIn(lab_t, scale=0.4, rate_func=BOUNCE),
                  Indicate(g_th, color=GREEN, scale_factor=1.25), run_time=1.1)
        self.play(Write(p2), run_time=1.2)
        self.wait(max(d - 2.3, 0.2))

        # étape 3 : le dernier groupe sans nom
        d = self.seg("meth3")
        step3 = self.step_row("3", "المجموعة الأخيرة (الوحدات) أقرؤها دون اسم", ROSE)
        self.play(FadeOut(step2, shift=DOWN * 0.3), run_time=0.4)
        self.play(FadeIn(step3, shift=LEFT * 0.6), run_time=0.6)
        self.wait(1.8)
        lab_u = self.mini_label("الوحدات", BLUE, g_un.get_center()[0], y_line - 0.55)
        self.sfx("pop")
        self.play(FadeIn(lab_u, scale=0.4, rate_func=BOUNCE),
                  Indicate(g_un, color=BLUE, scale_factor=1.25), run_time=1.1)
        self.play(Write(p3), run_time=1.2)
        self.wait(max(d - 5.1, 0.2))

        # lecture complète : on encadre et on célèbre
        d = self.seg("meth4")
        frame = SurroundingRectangle(reading, color=ROSE, corner_radius=0.18, buff=0.22)
        self.sfx("ding")
        self.play(Create(frame), run_time=0.9)
        self.play(Indicate(reading, color=ROSE, scale_factor=1.06), run_time=1.2)
        self.play(Flash(raw, color=YELL, flash_radius=2.6), run_time=0.9)
        self.wait(max(d - 3.0, 0.2))
        self.clear_all()

    # ── 6. انتبه : أصفار الوسط ─────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! لا تنسَ الأصفار في وسط العدد", 40, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        words = ar("«ثلاثة ملايين وخمسة»", 44).shift(UP * 1.2)
        self.play(Write(words), run_time=1.3)
        self.wait(max(d - 2.3, 0.2))

        d = self.seg("att2")   # construit 3 000 005 en suivant la voix
        full = num("3 000 005", 74, color=GREEN).shift(RIGHT * 1.9 + DOWN * 0.4)
        self.play(FadeIn(full, scale=0.6), run_time=0.9)
        self.play(Indicate(full[0], color=YELL, scale_factor=1.4), run_time=0.9)     # « ثلاثة »
        self.wait(0.5)
        self.play(Indicate(VGroup(*full[1:6]), color=LILA, scale_factor=1.3), run_time=1.3)  # « خمسة أصفار »
        self.wait(0.4)
        self.play(Indicate(full[6], color=YELL, scale_factor=1.4), run_time=0.9)     # « خمسة »
        self.wait(1.2)
        wrong = num("35", 70, color=REDA).shift(LEFT * 3.1 + DOWN * 0.4)
        self.play(FadeIn(wrong, scale=0.5), run_time=0.7)   # « وليس ثلاثة وخمسة »
        cross = Cross(wrong, stroke_color=REDA, stroke_width=8)
        self.sfx("boing")
        self.play(Create(cross), run_time=0.7)
        self.wait(max(d - 7.5, 0.2))

        d = self.seg("att3")
        check = ar("الصفر يحفظ مكان الخانة", 34, "BOLD", GREEN).shift(DOWN * 2.35 + RIGHT * 1.2)
        self.sfx("ding")
        self.play(Write(check), Flash(full, color=GREEN, flash_radius=2.4), run_time=1.4)
        self.play(Wiggle(garcon), run_time=1.0)
        self.wait(max(d - 2.4, 0.2))
        self.clear_all()

    # ── 7. السرّ + الختام ───────────────────────────────────────
    def s_outro(self):
        d = self.seg("astuce")
        head = titled("سرّ صغير قبل أن نفترق", 42, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        raw = num("8452391", 80).shift(UP * 0.4)
        self.play(Write(raw), run_time=1.2)
        self.wait(3.6)
        # petits traits après chaque 3 chiffres, en partant de la droite
        t1_x = (raw[3].get_right()[0] + raw[4].get_left()[0]) / 2
        t2_x = (raw[0].get_right()[0] + raw[1].get_left()[0]) / 2
        y = raw.get_center()[1]
        tick1 = Line(UP * 0.45, DOWN * 0.45, color=ROSE, stroke_width=6).move_to([t1_x, y - 0.55, 0])
        tick2 = Line(UP * 0.45, DOWN * 0.45, color=ROSE, stroke_width=6).move_to([t2_x, y - 0.55, 0])
        self.sfx("pop")
        self.play(Create(tick1), run_time=0.7)
        self.sfx("pop")
        self.play(Create(tick2), run_time=0.7)
        self.wait(1.6)
        grouped = num("8 452 391", 80, color=BLUE).shift(UP * 0.4)
        self.sfx("whoosh")
        self.play(Transform(raw, grouped), FadeOut(tick1), FadeOut(tick2), run_time=1.2)
        self.sfx("ding")
        self.wait(max(d - 10.0, 0.2))

        d = self.seg("outro")
        box = RoundedRectangle(corner_radius=0.25, width=9.2, height=1.4,
                               fill_color=YELL, fill_opacity=0.95, stroke_color=INK,
                               stroke_width=2).shift(DOWN * 1.9 + LEFT * 1.1)
        call = ar("والآن افتح كراسك وحلّ تمارين الوحدة 1", 36, "BOLD").move_to(box)
        garcon = self.boy(2.0).to_corner(DR, buff=0.25)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(box, call), rate_func=BOUNCE),
                  FadeIn(garcon, scale=0.3, rate_func=BOUNCE), run_time=1.4)
        rng = random.Random(31)
        stars = VGroup(*[
            Star(n=5, outer_radius=rng.uniform(0.14, 0.30), inner_radius=0.08,
                 fill_color=rng.choice(PALETTE), fill_opacity=0.95, stroke_width=0)
            .move_to([rng.uniform(-6.5, 6.5), rng.uniform(0.4, 3.4), 0])
            .rotate(rng.uniform(0, 3))
            for _ in range(16)])
        self.sfx("tada")
        self.play(LaggedStart(*[FadeIn(s, scale=0.2, shift=DOWN * 0.4, rate_func=BOUNCE)
                                for s in stars], lag_ratio=0.08), run_time=1.8)
        self.play(Wiggle(garcon), run_time=1.2)
        self.wait(max(d - 4.4, 0.2))

        # carte de fin : logo + Major
        others = [m for m in self.mobjects if id(m) not in self.keep and m is not self.logo]
        self.play(*[FadeOut(m) for m in others], run_time=0.8)
        self.play(self.logo.animate.scale_to_fit_height(2.2).move_to(UP * 0.4), run_time=1.2)
        brand = Text("Major", font="DejaVu Sans", weight="BOLD",
                     font_size=64, color=ROYAL).next_to(self.logo, DOWN, buff=0.35)
        self.sfx("ding")
        self.play(FadeIn(brand, shift=UP * 0.2), run_time=0.8)
        self.wait(1.9)
        self.play(FadeOut(self.logo), FadeOut(brand), run_time=0.8)

    def construct(self):
        self.keep = set()
        self.decor = self.make_decor()
        self.add(self.decor)
        self.keep.update(id(m) for m in self.decor)
        self.keep.add(id(self.decor))
        self.s_intro()
        self.s_regle()
        self.s_tableau()
        self.s_sighat()
        self.s_methode()
        self.s_attention()
        self.s_outro()
