# -*- coding: utf-8 -*-
"""Vidéo PITCH ÉCOLES 16:9 v4 « commerçant » — AIDA (~85 s).
Rendu : venv/bin/manim -r 1920,1080 --fps 30 --disable_caching scene_pitch.py VideoPitch
Fil de vente : douleur (que répondre au parent ?) → agitation (découvert trop tard) →
retournement + preuve (élèves Major) → zéro charge profs → منصة ذكية → bouche-à-oreille
= inscriptions → vision niveau par élève → urgence (première école) → démo GRATUITE.
Règles : pas de prix, pas de « directeur », pas de concours, jamais « QR »."""
import json
import random
from pathlib import Path

from manim import (Scene, Text, MarkupText, VGroup, Group, Rectangle, RoundedRectangle,
                   Circle, Star, Line, Polygon, SurroundingRectangle, Arrow,
                   ImageMobject, SVGMobject,
                   FadeIn, FadeOut, Write, Create, LaggedStart, GrowFromCenter,
                   Indicate, Wiggle,
                   UP, DOWN, LEFT, RIGHT, DL, DR, UL, UR, ORIGIN, config,
                   rate_functions as rf)

HERE = Path(__file__).parent
AUDIO = HERE / "audio_pitch"
SFX = HERE / "sfx"
PROMO = HERE / "assets/promo"
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


def star(color=YELL, r=0.26):
    return Star(n=5, outer_radius=r, inner_radius=r * 0.46, fill_color=color,
                fill_opacity=1, stroke_color=INK, stroke_width=1.5)


def stars_row(n, color=YELL, r=0.22):
    g = VGroup(*[star(color, r) for _ in range(n)])
    g.arrange(RIGHT, buff=0.12)
    return g


def page_img(name, height):
    p = ImageMobject(str(PROMO / name)).scale_to_fit_height(height)
    frame = SurroundingRectangle(p, color=INK, buff=0, corner_radius=0.02, stroke_width=3)
    return Group(p, frame)


def card(txt, color, width=6.6, height=1.1, size=40, tcolor=INK, fill_opacity=0.92):
    box = RoundedRectangle(corner_radius=0.28, width=width, height=height,
                           fill_color=color, fill_opacity=fill_opacity,
                           stroke_color=INK, stroke_width=2.5)
    t = ar(txt, size, "BOLD", tcolor)
    if t.width > width - 0.6:
        t.scale_to_fit_width(width - 0.6)
    t.move_to(box)
    return VGroup(box, t)


class VideoPitch(Scene):
    def seg(self, name):
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
        spots = [(6.5, 3.1), (6.6, 0.5), (5.7, -3.2), (-6.5, -3.1), (-6.6, 1.4), (-5.6, -1.2)]
        for i, (x, y) in enumerate(spots):
            col = PALETTE[i % len(PALETTE)]
            if i % 2 == 0:
                m = Circle(radius=rng.uniform(0.18, 0.36), fill_color=col,
                           fill_opacity=0.30, stroke_width=0)
            else:
                m = Star(n=5, outer_radius=rng.uniform(0.16, 0.3), inner_radius=0.09,
                         fill_color=col, fill_opacity=0.40, stroke_width=0)
            m.move_to([x, y, 0]).rotate(rng.uniform(0, 3))
            decor.add(m)
        return decor

    # ── 1. DOULEUR : la question du parent ─────────────────────
    def s_hook(self):
        d = self.seg("hook")
        self.logo = ImageMobject(str(HERE / "assets/major-logo.png"))
        self.logo.scale_to_fit_height(2.2).move_to(ORIGIN)
        brand = Text("Major", font="DejaVu Sans", weight="BOLD",
                     font_size=64, color=ROYAL).next_to(self.logo, DOWN, buff=0.35)
        self.sfx("ding")
        self.play(FadeIn(self.logo, scale=0.4, rate_func=BOUNCE),
                  FadeIn(brand, shift=UP * 0.2), run_time=1.1)
        self.play(FadeOut(brand),
                  self.logo.animate.scale_to_fit_height(0.8).to_corner(UL, buff=0.3),
                  run_time=0.8)
        self.keep.add(id(self.logo))
        # bulle du parent
        bulle = RoundedRectangle(corner_radius=0.4, width=10.6, height=2.0,
                                 fill_color="#FFFFFF", fill_opacity=1,
                                 stroke_color=ROSE, stroke_width=6).move_to(UP * 1.1)
        q = ar("أين وصل مستوى ابني؟", 60, "BOLD").move_to(bulle)
        tail = Polygon([1.8, 0, 0], [3.0, 0, 0], [3.4, -0.9, 0],
                       fill_color="#FFFFFF", fill_opacity=1, stroke_color=ROSE,
                       stroke_width=6).move_to(RIGHT * 3.3 + UP * 0.0).shift(UP * 0.0)
        tail.move_to(bulle.get_bottom() + RIGHT * 2.6 + DOWN * 0.35)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(bulle, tail, q), rate_func=BOUNCE), run_time=1.0)
        rep = ar("ماذا تجيبونه؟", 56, "BOLD", ROYAL).move_to(DOWN * 1.7)
        qmark = num("؟", 120, ROSE).move_to(DOWN * 1.7 + LEFT * 4.2)
        self.sfx("boing")
        self.play(FadeIn(rep, shift=UP * 0.3), GrowFromCenter(qmark, rate_func=BOUNCE),
                  run_time=0.9)
        self.wait(max(d - 3.8, 0.2))
        self.clear_all()

    # ── 2. AGITATION : découvert trop tard ─────────────────────
    def s_pain(self):
        d = self.seg("pain")
        lbl = ar("أشهر السنة الدراسية", 38, "BOLD", ROYAL).to_edge(UP, buff=0.7)
        self.play(FadeIn(lbl, shift=DOWN * 0.2), run_time=0.6)
        cells = VGroup()
        for i in range(9):
            sq = RoundedRectangle(corner_radius=0.12, width=1.15, height=1.15,
                                  fill_color="#EEEAE0", fill_opacity=1,
                                  stroke_color=INK, stroke_width=2)
            # RTL : le mois 1 à droite
            sq.move_to(RIGHT * (4.8 - i * 1.3) + UP * 1.0)
            n = num(str(i + 1), 40).move_to(sq)
            cells.add(VGroup(sq, n))
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cells],
                              lag_ratio=0.08), run_time=1.2)
        # le problème n'apparaît qu'au mois 9 — trop tard
        last = cells[8][0]
        cross = Text("✗", font="DejaVu Sans", font_size=72, weight="BOLD", color=REDA)
        cross.move_to(last)
        self.sfx("boing")
        self.play(last.animate.set_fill(ROSE, opacity=0.85), GrowFromCenter(cross),
                  run_time=0.8)
        c1 = card("اكتشاف الضعف متأخرًا = فات الأوان", REDA, 10.2, 1.3, 46,
                  tcolor="#FFFFFF").move_to(DOWN * 1.3)
        self.sfx("whoosh")
        self.play(GrowFromCenter(c1, rate_func=BOUNCE), run_time=0.9)
        c2 = ar("...ويغضب الأولياء", 44, "BOLD", REDA).move_to(DOWN * 2.9)
        self.play(FadeIn(c2, shift=UP * 0.3), run_time=0.7)
        self.wait(max(d - 4.2, 0.2))
        self.clear_all()

    # ── 3. RETOURNEMENT + PREUVE ───────────────────────────────
    def s_flip(self):
        d = self.seg("flip")
        covers = Group(page_img("cover-arabe.png", 4.4).move_to(LEFT * 4.4 + UP * 1.4),
                       page_img("cover-math.png", 4.4).move_to(UP * 1.4),
                       page_img("cover-hg.png", 4.4).move_to(RIGHT * 4.4 + UP * 1.4))
        self.sfx("tada")
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.6, scale=0.8, rate_func=BOUNCE)
                                for c in covers], lag_ratio=0.22), run_time=1.6)
        c1 = card("مستوى كل تلميذ أمامكم من الأسبوع الأول", GREEN, 11.0, 1.3, 46,
                  tcolor="#FFFFFF").move_to(DOWN * 1.7)
        self.sfx("ding")
        self.play(GrowFromCenter(c1, rate_func=BOUNCE), run_time=0.9)
        badge = card("مجرّب مع تلاميذ ماجور — وأثبت نتائجه", ROSE, 9.4, 1.15, 42)
        badge.move_to(DOWN * 3.2)
        self.sfx("pop")
        self.play(GrowFromCenter(badge, rate_func=BOUNCE), run_time=0.9)
        ss = VGroup(*[star(YELL, 0.3).move_to(c[1].get_corner(UR) + LEFT * 0.1 + DOWN * 0.1)
                      for c in covers])
        self.sfx("pop")
        self.play(LaggedStart(*[GrowFromCenter(s, rate_func=BOUNCE) for s in ss],
                              lag_ratio=0.3), run_time=1.0)
        self.play(Wiggle(badge), run_time=1.0)
        self.wait(max(d - 5.4, 0.2))
        self.clear_all()

    # ── 4. PROFS : rien à préparer ─────────────────────────────
    def s_prof(self):
        d = self.seg("prof")
        page = page_img("page-exos.png", 6.9).move_to(LEFT * 4.4)
        self.play(FadeIn(page, shift=UP * 0.5), run_time=0.9)
        head = card("معلموكم لن يحضّروا شيئًا", GREEN, 7.0, 1.2, 46).move_to(RIGHT * 2.9 + UP * 2.6)
        self.sfx("ding")
        self.play(GrowFromCenter(head, rate_func=BOUNCE), run_time=0.8)
        items = [("تذكير ومثال محلول", BLUE), ("تمارين متدرجة", YELL), ("للدعم والواجبات", LILA)]
        rows = VGroup()
        for i, (txt, col) in enumerate(items):
            c = card(txt, col, 5.6, 1.15, 42)
            g = VGroup(c)
            if i == 1:
                s = stars_row(3).next_to(c, LEFT, buff=0.35)
                g.add(s)
            g.move_to(RIGHT * 2.9 + UP * (0.9 - 1.5 * i))
            rows.add(g)
        for row in rows:
            self.sfx("pop")
            self.play(FadeIn(row, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 4.1, 0.2))
        self.page_exos = page

    # ── 5. LA PLATEFORME INTELLIGENTE ──────────────────────────
    def s_digital(self):
        d = self.seg("digital")
        self.sfx("whoosh")
        page = page_img("page-lecon.png", 6.9).move_to(LEFT * 4.6).rotate(0.04)
        prev = [m for m in self.mobjects if id(m) not in self.keep and m is not self.page_exos]
        self.play(*[FadeOut(m, shift=DOWN * 0.3) for m in prev],
                  FadeOut(self.page_exos), FadeIn(page, shift=UP * 0.4), run_time=0.9)
        qr = ImageMobject(str(PROMO / "qr.png")).scale_to_fit_height(2.0)
        qr.move_to(LEFT * 0.9 + UP * 1.6)
        qr_frame = SurroundingRectangle(qr, color=YELL, buff=0.1, corner_radius=0.12,
                                        stroke_width=6)
        self.sfx("ding")
        self.play(FadeIn(qr, scale=0.4, rate_func=BOUNCE), Create(qr_frame), run_time=0.9)
        phone = RoundedRectangle(corner_radius=0.35, width=3.6, height=6.4,
                                 fill_color="#FFFFFF", fill_opacity=1,
                                 stroke_color=INK, stroke_width=6).move_to(RIGHT * 3.9)
        speaker = RoundedRectangle(corner_radius=0.05, width=1.0, height=0.1,
                                   fill_color=INK, fill_opacity=1, stroke_width=0)
        speaker.move_to(phone.get_top() + DOWN * 0.3)
        self.sfx("whoosh")
        self.play(FadeIn(VGroup(phone, speaker), shift=LEFT * 0.6), run_time=0.8)
        self.play(qr.animate.scale_to_fit_height(1.3).move_to(phone.get_top() + DOWN * 1.2),
                  FadeOut(qr_frame), run_time=0.7)
        scan = Line(LEFT * 0.75, RIGHT * 0.75, color=GREEN, stroke_width=5)
        scan.move_to(qr.get_top())
        self.play(scan.animate.move_to(qr.get_bottom()), run_time=0.4)
        # le QR laisse place au bandeau « plateforme intelligente »
        banner = card("المنصة الذكية", ROYAL, 3.0, 0.9, 32, tcolor="#FFFFFF",
                      fill_opacity=1).move_to(qr)
        self.sfx("ding")
        self.play(FadeOut(scan), FadeOut(qr),
                  GrowFromCenter(banner, rate_func=BOUNCE), run_time=0.6)
        apps = [("بطاقة مراجعة", BLUE), ("أسئلة تفاعلية", GREEN), ("فيديو لكل درس", ROSE)]
        cards = VGroup()
        for i, (txt, col) in enumerate(apps):
            c = card(txt, col, 2.9, 0.95, 30)
            c.move_to(phone.get_top() + DOWN * (2.4 + 1.2 * i))
            cards.add(c)
        for c in cards:
            self.sfx("pop")
            self.play(GrowFromCenter(c, rate_func=BOUNCE), run_time=0.6)
        self.wait(max(d - 5.7, 0.2))
        self.clear_all()

    # ── 6. PARENTS : le bouche-à-oreille qui remplit l'école ──
    def s_parents(self):
        d = self.seg("parents")
        chain = [("يرون كل يوم ما تقدمونه", BLUE), ("يتحدثون عن مدرستكم", GREEN),
                 ("أولياء جدد لمدرستكم", ROSE)]
        cards = VGroup()
        for i, (txt, col) in enumerate(chain):
            c = card(txt, col, 4.3, 1.5, 36)
            c.move_to(RIGHT * (4.6 - 4.6 * i) + UP * 1.6)   # RTL : 1er à droite
            cards.add(c)
        arrows = VGroup()
        for i in range(2):
            a = Arrow(cards[i].get_left(), cards[i + 1].get_right(), buff=0.12,
                      color=INK, stroke_width=6, max_tip_length_to_length_ratio=0.35)
            arrows.add(a)
        for i, c in enumerate(cards):
            self.sfx("pop")
            self.play(GrowFromCenter(c, rate_func=BOUNCE), run_time=0.8)
            if i < 2:
                self.play(Create(arrows[i]), run_time=0.4)
        big = card("الولي الراضي = أفضل إعلان لمدرستكم", YELL, 10.6, 1.4, 48)
        big.move_to(DOWN * 1.3)
        self.sfx("tada")
        self.play(GrowFromCenter(big, rate_func=BOUNCE), run_time=0.9)
        boy = self.boy(2.2).move_to(DOWN * 2.9 + RIGHT * 4.9)
        self.sfx("pop")
        self.play(FadeIn(boy, scale=0.3, rate_func=BOUNCE), run_time=0.7)
        self.play(Indicate(big[1], scale_factor=1.08), run_time=0.8)
        self.wait(max(d - 5.4, 0.2))
        self.clear_all()

    # ── 7. VISION : le niveau de chaque élève, très clair ──────
    def s_vision(self):
        d = self.seg("vision")
        head = card("رؤية واضحة لمستوى كل تلميذ", BLUE, 9.6, 1.2, 46).to_edge(UP, buff=0.4)
        self.sfx("ding")
        self.play(GrowFromCenter(head, rate_func=BOUNCE), run_time=0.9)
        eleves = [("أحمد", 9, GREEN), ("مريم", 7, GREEN), ("محمد", 4, ROSE), ("فاطمة", 8, GREEN)]
        rows = VGroup()
        for i, (nom, note, col) in enumerate(eleves):
            box = RoundedRectangle(corner_radius=0.18, width=10.6, height=1.15,
                                   fill_color="#FFFFFF", fill_opacity=0.95,
                                   stroke_color=INK, stroke_width=2)
            t = ar(nom, 34, "BOLD").move_to(box.get_right() + LEFT * 1.1)
            cells = VGroup()
            for j in range(10):
                sq = Rectangle(width=0.52, height=0.5,
                               fill_color=col if j < note else "#EEEAE0",
                               fill_opacity=1, stroke_color=INK, stroke_width=1.5)
                sq.move_to(box.get_right() + LEFT * (2.4 + j * 0.52))
                cells.add(sq)
            statut = (ar("ممتاز", 28, "BOLD", GREEN) if note >= 8 else
                      ar("جيد", 28, "BOLD", GREEN) if note >= 6 else
                      ar("يحتاج دعمًا", 28, "BOLD", ROSE))
            statut.move_to(box.get_left() + RIGHT * 1.3)
            row = VGroup(box, t, cells, statut).move_to(UP * (1.85 - 1.22 * i))
            rows.add(row)
            self.sfx("pop")
            self.play(FadeIn(row, shift=LEFT * 0.4), run_time=0.55)
        alerte = SurroundingRectangle(rows[2], color=ROSE, corner_radius=0.2,
                                      buff=0.08, stroke_width=6)
        self.sfx("boing")
        self.play(Create(alerte), run_time=0.7)
        lbl = card("نعالج الضعف في وقته — ونصنع التفوق", ROSE, 9.2, 1.1, 40)
        lbl.to_edge(DOWN, buff=0.3)
        self.play(GrowFromCenter(lbl, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 4.6, 0.2))
        self.clear_all()

    # ── 8. URGENCE : soyez la première école ───────────────────
    def s_urgence(self):
        d = self.seg("urgence")
        chips = VGroup(card("بلا تكوين", LILA, 3.6, 1.1, 42),
                       card("بلا تعقيد", BLUE, 3.6, 1.1, 42))
        chips.arrange(LEFT, buff=0.7).move_to(UP * 2.4)
        self.sfx("pop")
        self.play(LaggedStart(*[GrowFromCenter(c, rate_func=BOUNCE) for c in chips],
                              lag_ratio=0.35), run_time=1.0)
        duo = card("دفتر + منصة ذكية", GREEN, 5.8, 1.2, 44).move_to(UP * 0.6)
        self.sfx("ding")
        self.play(GrowFromCenter(duo, rate_func=BOUNCE), run_time=0.8)
        first = card("كونوا أول مدرسة تقدم هذا لتلاميذها", YELL, 11.4, 1.6, 52)
        first.move_to(DOWN * 1.7)
        self.sfx("tada")
        self.play(GrowFromCenter(first, rate_func=BOUNCE), run_time=1.0)
        self.play(Wiggle(first[1]), run_time=0.9)
        self.wait(max(d - 3.7, 0.2))
        self.clear_all()

    # ── 9. CTA : démo gratuite, zéro risque ────────────────────
    def s_cta(self):
        d = self.seg("cta")
        big = ImageMobject(str(HERE / "assets/major-logo.png")).scale_to_fit_height(2.2)
        big.move_to(UP * 2.2)
        brand = Text("Major", font="DejaVu Sans", weight="BOLD",
                     font_size=64, color=ROYAL).next_to(big, DOWN, buff=0.3)
        self.sfx("ding")
        self.play(FadeIn(big, scale=0.4, rate_func=BOUNCE), FadeIn(brand, shift=UP * 0.2),
                  run_time=1.0)
        box = card("عرض تجريبي مجاني في مدرستكم", YELL, 11.0, 1.6, 52).move_to(DOWN * 0.7)
        self.sfx("tada")
        self.play(GrowFromCenter(box, rate_func=BOUNCE), run_time=0.9)
        sub = ar("شاهدوا الفرق بأنفسكم", 44, "BOLD", ROSE).move_to(DOWN * 2.1)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.7)
        slogan = ar("ماجور — شريك نجاح مدرستكم", 40, "BOLD", ROYAL).move_to(DOWN * 3.2)
        self.play(FadeIn(slogan, shift=UP * 0.2), run_time=0.7)
        rng = random.Random(9)
        rain = VGroup()
        for i in range(16):
            # jamais sur les textes (bande basse centrale)
            while True:
                x, y = rng.uniform(-6.6, 6.6), rng.uniform(-3.7, 3.7)
                if not (-6.0 < x < 6.0 and -3.6 < y < 0.2):
                    break
            rain.add(star(PALETTE[i % 5], rng.uniform(0.13, 0.28)).move_to([x, y, 0]))
        self.play(LaggedStart(*[FadeIn(s, scale=0.2, rate_func=BOUNCE) for s in rain],
                              lag_ratio=0.06), run_time=1.2)
        self.play(Indicate(box[1], scale_factor=1.08), run_time=0.8)
        self.wait(max(d - 5.3, 0.5))
        self.wait(0.8)

    # ── assemblage ─────────────────────────────────────────────
    def construct(self):
        self.keep = set()
        decor = self.make_decor()
        self.add(decor)
        self.keep.update(id(m) for m in decor)
        self.keep.add(id(decor))
        self.s_hook()
        self.s_pain()
        self.s_flip()
        self.s_prof()
        self.s_digital()
        self.s_parents()
        self.s_vision()
        self.s_urgence()
        self.s_cta()
