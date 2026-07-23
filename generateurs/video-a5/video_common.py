# -*- coding: utf-8 -*-
"""Socle commun des vidéos Major (toutes unités).
Règles : فصحى (ar-SA-HamedNeural) · MarkupText pour l'arabe · logo en haut à gauche ·
1 phrase = 1 chunk audio = 1 bloc d'animation · vocabulaire du cahier (خانة، jamais منزلة)."""
import json
import random
from pathlib import Path

from manim import (Scene, Text, MarkupText, VGroup, Rectangle, RoundedRectangle,
                   Circle, Star, Line, AnnularSector, SurroundingRectangle,
                   ImageMobject, SVGMobject,
                   FadeIn, FadeOut, Write, Create, LaggedStart, GrowFromCenter,
                   Wiggle, UP, DOWN, LEFT, RIGHT, DL, DR, UL, ORIGIN, DEGREES,
                   config, rate_functions as rf)

HERE = Path(__file__).parent
SFX = HERE / "sfx"

BG = "#FFF9EF"
INK = "#3A3A3A"
YELL = "#F6C445"
ROSE = "#EF6292"
GREEN = "#5BB86A"
BLUE = "#4A9DE0"
LILA = "#A47FDB"
REDA = "#E05252"
ROYAL = "#2563eb"
GOLD = "#C99A1F"
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


def frac(n, d, size=54, color=INK):
    """Fraction empilée : بسط / trait / مقام."""
    top = num(str(n), size, color)
    bot = num(str(d), size, color)
    w = max(top.width, bot.width) + 0.35
    bar = Line(LEFT * w / 2, RIGHT * w / 2, color=color, stroke_width=max(4, size / 11))
    top.next_to(bar, UP, buff=0.16)
    bot.next_to(bar, DOWN, buff=0.16)
    return VGroup(top, bar, bot)


def pie(parts, filled, radius=1.15, fill=YELL):
    """Disque en `parts` حصص égales, `filled` premières colorées."""
    g = VGroup()
    for i in range(parts):
        s = AnnularSector(inner_radius=0, outer_radius=radius, angle=360 / parts * DEGREES,
                          start_angle=90 * DEGREES + i * 360 / parts * DEGREES,
                          fill_color=fill if i < filled else "#FFFFFF",
                          fill_opacity=1 if i < filled else 0.9,
                          stroke_color=INK, stroke_width=3)
        g.add(s)
    return g


def strip(cells, filled, width=4.2, height=0.75, fill=BLUE):
    """Barre en `cells` حصص égales, `filled` premières colorées (depuis la droite, RTL)."""
    g = VGroup()
    cw = width / cells
    for i in range(cells):
        r = Rectangle(width=cw, height=height,
                      fill_color=fill if i < filled else "#FFFFFF",
                      fill_opacity=1 if i < filled else 0.9,
                      stroke_color=INK, stroke_width=2.5)
        r.move_to([width / 2 - cw / 2 - i * cw, 0, 0])   # remplit depuis la droite
        g.add(r)
    return g


class MajorScene(Scene):
    """Base commune : audio par chunk, SFX, logo, décor, personnage, intro/outro standard."""
    AUDIO = None          # Path du dossier audio de l'unité
    UNIT_AR = ""          # « الوحدة 2 »
    UNIT_COLOR = YELL     # couleur du badge de l'unité
    TITLE = ""            # titre arabe de l'unité
    OUTRO_CALL = ""       # « والآن افتح كراسك... » affiché dans la boîte jaune

    def seg(self, name):
        self.add_sound(str(self.AUDIO / f"{name}.mp3"))
        return self.DUR[name]

    def sfx(self, name):
        self.add_sound(str(SFX / f"{name}.wav"))

    def clear_all(self):
        ms = [m for m in self.mobjects if id(m) not in self.keep]
        if ms:
            self.sfx("whoosh")
            self.play(*[FadeOut(m, shift=DOWN * 0.3) for m in ms], run_time=0.6)

    def boy(self, height=2.0):
        return SVGMobject(str(HERE / "assets/perso-garcon.svg")).scale_to_fit_height(height)

    def girl(self, height=2.0):
        return SVGMobject(str(HERE / "assets/perso-fille.svg")).scale_to_fit_height(height)

    def make_decor(self):
        rng = random.Random(6)
        decor = VGroup()
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

    def setup_common(self):
        self.DUR = json.loads((self.AUDIO / "durations.json").read_text())
        self.keep = set()
        self.decor = self.make_decor()
        self.add(self.decor)
        self.keep.update(id(m) for m in self.decor)
        self.keep.add(id(self.decor))

    # ── blocs standard ──────────────────────────────────────────
    def s_intro_card(self, seg_name):
        """Logo plein écran → filigrane haut-gauche, badge d'unité, titre, personnage."""
        d = self.seg(seg_name)
        self.logo = ImageMobject(str(HERE / "assets/major-logo.png"))
        self.logo.scale_to_fit_height(2.2).move_to(ORIGIN)
        brand = Text("Major", font="DejaVu Sans", weight="BOLD",
                     font_size=64, color=ROYAL).next_to(self.logo, DOWN, buff=0.35)
        self.sfx("ding")
        self.play(FadeIn(self.logo, scale=0.4, rate_func=BOUNCE),
                  FadeIn(brand, shift=UP * 0.2), run_time=1.3)
        self.wait(0.4)
        self.play(FadeOut(brand),
                  self.logo.animate.scale_to_fit_height(0.8).to_corner(UL, buff=0.3),
                  run_time=1.0)
        self.keep.add(id(self.logo))
        badge = RoundedRectangle(corner_radius=0.25, width=3.2, height=0.9,
                                 fill_color=self.UNIT_COLOR, fill_opacity=1,
                                 stroke_color=INK, stroke_width=2).shift(UP * 2.4)
        badge_t = ar(self.UNIT_AR, 34, "BOLD").move_to(badge)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(badge, badge_t), rate_func=BOUNCE), run_time=0.8)
        title = ar(self.TITLE, 80, "BOLD").shift(UP * 0.55)
        self.play(Write(title), run_time=1.8)
        garcon = self.boy(2.1).to_corner(DR, buff=0.25)
        self.sfx("pop")
        self.play(FadeIn(garcon, scale=0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 6.2, 0.2))

    def s_objectifs(self, seg_name, objectifs):
        """Objectifs du cahier + règle d'or, puis clear."""
        d = self.seg(seg_name)
        t = 0
        for i, txt in enumerate(objectifs):
            o = ar(txt, 32)
            s = chip([GREEN, BLUE, LILA][i % 3]).scale(0.55)
            s.next_to(o, RIGHT, buff=0.3)
            row = VGroup(o, s).move_to(DOWN * (0.55 + 0.85 * i)).to_edge(RIGHT, buff=1.0)
            self.sfx("pop")
            self.play(FadeIn(row, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.0)
            t += 1.0
        rule = ar("أُشاهد ← أرسم ← أحسب", 30, "BOLD", color=ROSE)
        rule.shift(DOWN * (0.75 + 0.85 * len(objectifs)) + LEFT * 1.6)
        rule_box = SurroundingRectangle(rule, color=ROSE, corner_radius=0.15, buff=0.22)
        self.play(Create(rule_box), FadeIn(rule), run_time=1.2)
        self.wait(max(d - t - 1.2, 0.2))
        self.clear_all()

    def s_outro_end(self, seg_name):
        """Boîte d'appel au cahier + pluie d'étoiles + carte de fin logo/Major."""
        d = self.seg(seg_name)
        box = RoundedRectangle(corner_radius=0.25, width=9.2, height=1.4,
                               fill_color=YELL, fill_opacity=0.95, stroke_color=INK,
                               stroke_width=2).shift(DOWN * 1.9 + LEFT * 1.1)
        call = ar(self.OUTRO_CALL, 36, "BOLD")
        if call.width > 8.6:
            call.scale_to_fit_width(8.6)
        call.move_to(box)
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
        others = [m for m in self.mobjects if id(m) not in self.keep and m is not self.logo]
        self.play(*[FadeOut(m) for m in others], run_time=0.8)
        self.play(self.logo.animate.scale_to_fit_height(2.2).move_to(UP * 0.4), run_time=1.2)
        brand = Text("Major", font="DejaVu Sans", weight="BOLD",
                     font_size=64, color=ROYAL).next_to(self.logo, DOWN, buff=0.35)
        self.sfx("ding")
        self.play(FadeIn(brand, shift=UP * 0.2), run_time=0.8)
        self.wait(1.9)
        self.play(FadeOut(self.logo), FadeOut(brand), run_time=0.8)
