# -*- coding: utf-8 -*-
"""Vidéo PROMO 9:16 — présentation du دفتر ماجور (avantages, parcours, suivi).
Rendu : venv/bin/manim --disable_caching scene_promo.py VideoPromo  (1080×1920 réglé ici).
Principe identique aux vidéos d'unités : 1 phrase = 1 chunk audio (audio_promo/) = 1 bloc.
Spécificité : montre de VRAIES pages des cahiers (assets/promo/) + le vrai QR."""
import json
import random
from pathlib import Path

from manim import (Scene, Text, MarkupText, VGroup, Group, Rectangle, RoundedRectangle,
                   Circle, Star, Line, Polygon, SurroundingRectangle,
                   ImageMobject, SVGMobject,
                   FadeIn, FadeOut, Write, Create, LaggedStart, GrowFromCenter,
                   Indicate, Wiggle,
                   UP, DOWN, LEFT, RIGHT, DL, DR, UL, UR, ORIGIN, config,
                   rate_functions as rf)

HERE = Path(__file__).parent
AUDIO = HERE / "audio_promo"
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
ROYAL = "#2563eb"
PALETTE = [YELL, ROSE, GREEN, BLUE, LILA]

# ── format vertical 9:16 (statuts WhatsApp) ──
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 30
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


def stars_row(n, color=YELL, r=0.24):
    g = VGroup(*[star(color, r) for _ in range(n)])
    g.arrange(RIGHT, buff=0.12)
    return g


def page_img(name, height):
    p = ImageMobject(str(PROMO / name)).scale_to_fit_height(height)
    frame = SurroundingRectangle(p, color=INK, buff=0, corner_radius=0.02, stroke_width=3)
    return Group(p, frame)


def zone(page, rx, ry, rw, rh, color=ROSE):
    """Cadre sur une zone d'une page : coords relatives (0..1, origine haut-gauche)."""
    img = page[0]
    w, h = img.width, img.height
    c = img.get_center()
    x = c[0] - w / 2 + (rx + rw / 2) * w
    y = c[1] + h / 2 - (ry + rh / 2) * h
    return RoundedRectangle(corner_radius=0.12, width=rw * w, height=rh * h,
                            stroke_color=color, stroke_width=6, fill_opacity=0).move_to([x, y, 0])


def card(txt, color, width=6.6, height=1.1, size=40):
    box = RoundedRectangle(corner_radius=0.28, width=width, height=height,
                           fill_color=color, fill_opacity=0.92, stroke_color=INK, stroke_width=2.5)
    t = ar(txt, size, "BOLD")
    if t.width > width - 0.6:
        t.scale_to_fit_width(width - 0.6)
    t.move_to(box)
    return VGroup(box, t)


class VideoPromo(Scene):
    # ── infrastructure (identique aux unités) ───────────────────
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

    def girl(self, height=2.0):
        return SVGMobject(str(HERE / "assets/perso-fille.svg")).scale_to_fit_height(height)

    def make_decor(self):
        rng = random.Random(6)
        decor = VGroup()
        spots = [(3.8, 6.9), (4.0, 2.6), (3.6, -3.0), (3.7, -6.9),
                 (-3.8, -6.6), (-4.0, 3.6), (-3.5, -1.4), (-3.9, 6.6)]
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

    # ── 1. INTRO : logo + دفتر ماجور + couverture ───────────────
    def s_intro(self):
        d = self.seg("intro1")
        self.logo = ImageMobject(str(HERE / "assets/major-logo.png"))
        self.logo.scale_to_fit_height(2.4).move_to(UP * 2.0)
        brand = Text("Major", font="DejaVu Sans", weight="BOLD",
                     font_size=72, color=ROYAL).next_to(self.logo, DOWN, buff=0.4)
        self.sfx("ding")
        self.play(FadeIn(self.logo, scale=0.4, rate_func=BOUNCE),
                  FadeIn(brand, shift=UP * 0.2), run_time=1.2)
        self.play(FadeOut(brand),
                  self.logo.animate.scale_to_fit_height(0.85).to_corner(UL, buff=0.35),
                  run_time=0.9)
        self.keep.add(id(self.logo))
        title = ar("دفتر ماجور", 88, "BOLD", ROYAL).move_to(UP * 6.2)
        sub = ar("السنة السادسة الأساسية • 6AF", 36, "BOLD", INK).next_to(title, DOWN, buff=0.35)
        self.sfx("pop")
        self.play(Write(title), FadeIn(sub, shift=UP * 0.2), run_time=1.6)
        cover = page_img("cover-math.png", 8.6).move_to(DOWN * 0.9)
        self.play(FadeIn(cover, shift=UP * 0.6, scale=0.85, rate_func=BOUNCE), run_time=1.2)
        garcon = self.boy(2.2).to_corner(DR, buff=0.35)
        self.sfx("pop")
        self.play(FadeIn(garcon, scale=0.3, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 5.7, 0.2))
        self.cover, self.garcon, self.sub = cover, garcon, sub

    # ── 2. Un seul دفتر : cours + exercices + suivi ─────────────
    def s_un_seul(self):
        d = self.seg("intro2")
        c2 = page_img("cover-arabe.png", 5.6).move_to(LEFT * 2.3 + UP * 2.2).rotate(0.10)
        c3 = page_img("cover-hg.png", 5.6).move_to(RIGHT * 2.3 + UP * 2.2).rotate(-0.10)
        self.sfx("whoosh")
        self.play(FadeOut(self.garcon), FadeOut(self.sub),
                  self.cover.animate.scale_to_fit_height(6.2).move_to(UP * 2.2),
                  FadeIn(c2, shift=RIGHT * 0.5), FadeIn(c3, shift=LEFT * 0.5), run_time=1.2)
        chips = VGroup(card("الدرس", BLUE, 2.5, 1.0),
                       card("التمارين", GREEN, 2.5, 1.0),
                       card("المتابعة", ROSE, 2.5, 1.0))
        chips.arrange(LEFT, buff=0.35).move_to(DOWN * 3.2)   # RTL : premier à droite
        self.play(LaggedStart(*[GrowFromCenter(c, rate_func=BOUNCE) for c in chips],
                              lag_ratio=0.35), run_time=1.8)
        arrow_t = ar("من أول السنة إلى يوم المسابقة", 34, "BOLD", ROYAL).move_to(DOWN * 4.6)
        self.play(FadeIn(arrow_t, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 3. Avantage : تذكير + exemple corrigé ──────────────────
    def s_rappel(self):
        d = self.seg("av_rappel")
        head = card("في كل وحدة: تذكير قصير", YELL, 7.4, 1.15, 44).move_to(UP * 6.6)
        self.sfx("pop")
        self.play(GrowFromCenter(head, rate_func=BOUNCE), run_time=0.8)
        page = page_img("page-lecon.png", 11.5).move_to(DOWN * 1.1)
        self.play(FadeIn(page, shift=UP * 0.5), run_time=1.0)
        z = zone(page, 0.05, 0.395, 0.90, 0.175, ROSE)
        self.sfx("ding")
        self.play(Create(z), run_time=1.0)
        lbl = ar("مثال محلول خطوة خطوة", 32, "BOLD", ROSE)
        lbl_box = RoundedRectangle(corner_radius=0.2, width=lbl.width + 0.7, height=0.85,
                                   fill_color="#FFFFFF", fill_opacity=0.95,
                                   stroke_color=ROSE, stroke_width=3)
        lbl_g = VGroup(lbl_box, lbl).move_to(DOWN * 7.0)
        self.play(FadeIn(lbl_g, shift=UP * 0.3), run_time=0.8)
        self.wait(max(d - 3.6, 0.2))
        self.page_lecon = page
        self.play(FadeOut(z), FadeOut(lbl_g), FadeOut(head), run_time=0.5)

    # ── 4. Avantage : exercices ⭐ → ⭐⭐⭐ ─────────────────────
    def s_stars(self):
        d = self.seg("av_stars")
        self.sfx("whoosh")
        page = page_img("page-exos.png", 10.0).move_to(UP * 2.6)
        self.play(FadeOut(self.page_lecon), FadeIn(page, shift=UP * 0.4), run_time=1.0)
        rows = VGroup()
        labels = [("نموذج محلول", 1, GREEN), ("أتدرب", 2, BLUE), ("أتحدى نفسي", 3, ROSE)]
        for i, (txt, n, col) in enumerate(labels):
            t = ar(txt, 36, "BOLD")
            s = stars_row(n)
            box = RoundedRectangle(corner_radius=0.24, width=6.8, height=1.05,
                                   fill_color=col, fill_opacity=0.28,
                                   stroke_color=col, stroke_width=3)
            t.move_to(box.get_center() + LEFT * 0.9)
            s.move_to(box.get_right() + LEFT * (s.width / 2 + 0.4))
            row = VGroup(box, t, s).move_to(DOWN * (3.6 + 1.35 * i))
            rows.add(row)
        for row in rows:
            self.sfx("pop")
            self.play(FadeIn(row, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(rows[2][2]), run_time=1.0)
        self.wait(max(d - 4.7, 0.2))
        self.page_exos = page
        self.rows_stars = rows

    # ── 5. Avantage : règle d'or أشاهد أرسم أحسب ───────────────
    def s_regle(self):
        d = self.seg("av_regle")
        self.sfx("whoosh")
        page = page_img("page-regle.png", 11.5).move_to(UP * 1.6)
        self.play(FadeOut(self.rows_stars, shift=DOWN * 0.4), FadeOut(self.page_exos),
                  FadeIn(page, shift=UP * 0.5), run_time=1.0)
        z = zone(page, 0.05, 0.20, 0.90, 0.13, GREEN)
        self.sfx("ding")
        self.play(Create(z), run_time=1.0)
        rule = ar("أُشاهد ← أرسم ← أحسب", 44, "BOLD", "#FFFFFF")
        rule_box = RoundedRectangle(corner_radius=0.26, width=rule.width + 0.9, height=1.2,
                                    fill_color=GREEN, fill_opacity=1,
                                    stroke_color=INK, stroke_width=3)
        rule_g = VGroup(rule_box, rule.move_to(rule_box)).move_to(DOWN * 6.4)
        self.sfx("tada")
        self.play(GrowFromCenter(rule_g, rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 3.0, 0.2))
        self.page_regle, self.zone_regle, self.rule_g = page, z, rule_g

    # ── 6. Avantage : vraies zones d'écriture ──────────────────
    def s_ecrire(self):
        d = self.seg("av_ecrire")
        self.sfx("whoosh")
        page = page_img("page-exos.png", 11.5).move_to(DOWN * 0.6)
        self.play(FadeOut(self.zone_regle), FadeOut(self.rule_g), FadeOut(self.page_regle),
                  FadeIn(page, shift=UP * 0.5), run_time=1.0)
        head = card("مساحات كتابة واسعة", LILA, 7.0, 1.15, 44).move_to(UP * 6.6)
        self.sfx("pop")
        self.play(GrowFromCenter(head, rate_func=BOUNCE), run_time=0.8)
        zs = VGroup(zone(page, 0.33, 0.475, 0.62, 0.155, LILA),
                    zone(page, 0.05, 0.685, 0.90, 0.075, LILA),
                    zone(page, 0.30, 0.845, 0.65, 0.115, LILA))
        self.play(LaggedStart(*[Create(z) for z in zs], lag_ratio=0.4), run_time=2.0)
        self.wait(max(d - 3.8, 0.2))
        self.clear_all()

    # ── 7. Parcours quotidien ──────────────────────────────────
    def s_parcours(self):
        d = self.seg("parcours")
        head = card("كل يوم وحدة صغيرة", YELL, 7.0, 1.2, 46).move_to(UP * 6.3)
        self.sfx("ding")
        self.play(GrowFromCenter(head, rate_func=BOUNCE), run_time=0.9)
        steps = [("أقرأ التذكير", BLUE, 1), ("أحل التمارين", GREEN, 2), ("أتحدى نفسي", ROSE, 3)]
        cards = VGroup()
        for i, (txt, col, n) in enumerate(steps):
            c = card(txt, col, 5.6, 1.5, 46)
            s = stars_row(n, YELL, 0.22).next_to(c, LEFT, buff=0.4)
            g = VGroup(c, s).move_to(UP * (3.2 - 2.6 * i) + RIGHT * 0.4)
            cards.add(g)
        arrows = VGroup()
        for i in range(2):
            a = Line(cards[i].get_bottom() + DOWN * 0.15, cards[i + 1].get_top() + UP * 0.15,
                     color=INK, stroke_width=5)
            arrows.add(a)
        for i, g in enumerate(cards):
            self.sfx("pop")
            self.play(FadeIn(g, shift=LEFT * 0.6, rate_func=BOUNCE), run_time=0.9)
            if i < 2:
                self.play(Create(arrows[i]), run_time=0.4)
        boy = self.boy(2.6).move_to(DOWN * 5.6 + LEFT * 2.2)
        self.sfx("pop")
        self.play(FadeIn(boy, scale=0.3, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 5.2, 0.2))
        self.clear_all()

    # ── 8-9. QR → bilan de révision sur le téléphone ───────────
    def s_qr(self):
        d = self.seg("qr1")
        page = page_img("page-lecon.png", 7.0).move_to(UP * 3.9 + LEFT * 1.4).rotate(0.05)
        self.play(FadeIn(page, shift=UP * 0.4), run_time=0.9)
        qr = ImageMobject(str(PROMO / "qr.png")).scale_to_fit_height(2.6)
        qr.move_to(UP * 3.3 + RIGHT * 2.6)
        qr_frame = SurroundingRectangle(qr, color=YELL, buff=0.12, corner_radius=0.15,
                                        stroke_width=7)
        self.sfx("ding")
        self.play(FadeIn(qr, scale=0.4, rate_func=BOUNCE), Create(qr_frame), run_time=1.1)
        self.wait(max(d - 2.0, 0.2))

        d = self.seg("qr2")
        phone = RoundedRectangle(corner_radius=0.4, width=4.9, height=8.6,
                                 fill_color="#FFFFFF", fill_opacity=1,
                                 stroke_color=INK, stroke_width=7).move_to(DOWN * 3.4)
        speaker = RoundedRectangle(corner_radius=0.06, width=1.2, height=0.12,
                                   fill_color=INK, fill_opacity=1, stroke_width=0)
        speaker.move_to(phone.get_top() + DOWN * 0.35)
        self.sfx("whoosh")
        self.play(FadeIn(VGroup(phone, speaker), shift=UP * 0.8), run_time=0.9)
        # scan : le QR « entre » dans le téléphone
        self.play(qr.animate.scale_to_fit_height(1.7).move_to(phone.get_top() + DOWN * 1.5),
                  FadeOut(qr_frame), run_time=0.8)
        scan = Line(LEFT * 1.0, RIGHT * 1.0, color=GREEN, stroke_width=6)
        scan.move_to(qr.get_top())
        self.play(scan.animate.move_to(qr.get_bottom()), run_time=0.5)
        self.play(FadeOut(scan), run_time=0.2)
        apps = [("بطاقة مراجعة", BLUE), ("أسئلة تفاعلية", GREEN), ("فيديو الدرس", ROSE)]
        cards = VGroup()
        for i, (txt, col) in enumerate(apps):
            c = card(txt, col, 3.9, 1.15, 34)
            c.move_to(phone.get_top() + DOWN * (3.1 + 1.45 * i))
            cards.add(c)
        play_tri = Polygon([-0.14, 0.18, 0], [-0.14, -0.18, 0], [0.18, 0, 0],
                           fill_color="#FFFFFF", fill_opacity=1, stroke_color=INK,
                           stroke_width=2).move_to(cards[2][0].get_left() + RIGHT * 0.45)
        for c in cards:
            self.sfx("pop")
            self.play(GrowFromCenter(c, rate_func=BOUNCE), run_time=0.7)
        self.play(FadeIn(play_tri, scale=0.4), run_time=0.4)
        self.wait(max(d - 4.7, 0.2))
        self.clear_all()

    # ── 10. Suivi des parents ──────────────────────────────────
    def s_parents(self):
        d = self.seg("parent1")
        head = card("متابعة الوالدين", ROSE, 6.6, 1.2, 48).move_to(UP * 6.3)
        self.sfx("ding")
        self.play(GrowFromCenter(head, rate_func=BOUNCE), run_time=0.9)
        fille = self.boy(2.6).move_to(UP * 3.4 + LEFT * 2.2)
        lbl = ar("تقدم هذا الأسبوع", 38, "BOLD", ROYAL).move_to(UP * 0.9)
        self.play(FadeIn(fille, scale=0.3, rate_func=BOUNCE), FadeIn(lbl), run_time=0.9)
        days = ["السبت", "الأحد", "الاثنين", "الثلاثاء", "الأربعاء"]
        rows = VGroup()
        for i, day in enumerate(days):
            t = ar(day, 30, "BOLD")
            box = RoundedRectangle(corner_radius=0.18, width=6.4, height=0.95,
                                   fill_color="#FFFFFF", fill_opacity=0.95,
                                   stroke_color=INK, stroke_width=2)
            t.move_to(box.get_right() + LEFT * 1.3)
            check = Text("✓", font="DejaVu Sans", font_size=44, weight="BOLD", color=GREEN)
            check.move_to(box.get_left() + RIGHT * 0.8)
            s = stars_row(3, YELL, 0.16).move_to(box.get_center() + LEFT * 0.6)
            row = VGroup(box, t, check, s).move_to(DOWN * (0.4 + 1.2 * i))
            rows.add(row)
        for row in rows:
            self.sfx("pop")
            self.play(FadeIn(row, shift=LEFT * 0.4), run_time=0.55)
        self.wait(max(d - 4.6, 0.2))

        d = self.seg("parent2")
        msgs = [("الحلول موجودة", BLUE), ("الفيديو يشرح", GREEN), ("دورك أن تشجع", ROSE)]
        chips = VGroup()
        for i, (txt, col) in enumerate(msgs):
            c = card(txt, col, 4.6, 1.0, 36)
            chips.add(c)
        chips.arrange(DOWN, buff=0.35).move_to(DOWN * 5.9)
        self.play(FadeOut(rows[3:], shift=DOWN * 0.3), run_time=0.4)
        for c in chips:
            self.sfx("pop")
            self.play(FadeIn(c, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 2.8, 0.2))
        self.clear_all()

    # ── 12. École / prof ───────────────────────────────────────
    def s_ecole(self):
        d = self.seg("ecole1")
        head = card("في القسم مع المعلم", GREEN, 7.0, 1.2, 46).move_to(UP * 6.3)
        self.sfx("ding")
        self.play(GrowFromCenter(head, rate_func=BOUNCE), run_time=0.9)
        board = RoundedRectangle(corner_radius=0.25, width=7.9, height=6.8,
                                 fill_color="#2E5E3F", fill_opacity=1,
                                 stroke_color="#8B5A2B", stroke_width=10).move_to(UP * 1.9)
        bt = ar("31 وحدة على البرنامج الرسمي", 40, "BOLD", "#FFFFFF")
        if bt.width > 6.9:
            bt.scale_to_fit_width(6.9)
        bt.move_to(board.get_top() + DOWN * 0.85)
        self.play(FadeIn(board), Write(bt), run_time=1.2)
        cells = VGroup()
        for i in range(31):
            r, c = divmod(i, 7)
            sq = RoundedRectangle(corner_radius=0.08, width=0.72, height=0.72,
                                  fill_color=PALETTE[i % 5], fill_opacity=0.9,
                                  stroke_color="#FFFFFF", stroke_width=2)
            sq.move_to(board.get_center() + UP * 0.75 + DOWN * (r * 0.85)
                       + RIGHT * ((c - 3) * 0.85))
            cells.add(sq)
        self.play(LaggedStart(*[GrowFromCenter(sq) for sq in cells], lag_ratio=0.04),
                  run_time=1.8)
        chips = VGroup(card("للدعم", BLUE, 3.4, 1.0, 38), card("للواجبات", LILA, 3.4, 1.0, 38))
        chips.arrange(LEFT, buff=0.5).move_to(DOWN * 2.7)
        self.sfx("pop")
        self.play(LaggedStart(*[GrowFromCenter(c, rate_func=BOUNCE) for c in chips],
                              lag_ratio=0.4), run_time=1.2)
        prof = self.boy(2.6).move_to(DOWN * 5.3 + RIGHT * 2.0)
        self.sfx("pop")
        self.play(FadeIn(prof, scale=0.3, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 5.9, 0.2))
        self.clear_all()

    # ── 13-14. OUTRO ───────────────────────────────────────────
    def s_outro(self):
        d = self.seg("outro1")
        trio = [("يتعلم الطفل", BLUE), ("يطمئن الوالدان", GREEN), ("يرتاح المعلم", ROSE)]
        cards = VGroup()
        for i, (txt, col) in enumerate(trio):
            c = card(txt, col, 6.4, 1.6, 52)
            s = star(col, 0.3).next_to(c, LEFT, buff=0.35)
            cards.add(VGroup(c, s).move_to(UP * (3.4 - 2.4 * i) + RIGHT * 0.3))
        for c in cards:
            self.sfx("pop")
            self.play(FadeIn(c, shift=LEFT * 0.6, rate_func=BOUNCE), run_time=0.9)
        cover = page_img("cover-math.png", 4.6).move_to(DOWN * 5.2)
        self.play(FadeIn(cover, shift=UP * 0.4), run_time=0.9)
        self.wait(max(d - 3.6, 0.2))

        d = self.seg("outro2")
        self.clear_all()
        big = ImageMobject(str(HERE / "assets/major-logo.png")).scale_to_fit_height(3.2)
        big.move_to(UP * 2.6)
        brand = Text("Major", font="DejaVu Sans", weight="BOLD",
                     font_size=88, color=ROYAL).next_to(big, DOWN, buff=0.45)
        box = RoundedRectangle(corner_radius=0.3, width=8.0, height=1.5,
                               fill_color=YELL, fill_opacity=0.97,
                               stroke_color=INK, stroke_width=3).move_to(DOWN * 2.6)
        call = ar("دفتر ماجور • رفيق النجاح", 48, "BOLD").move_to(box)
        self.sfx("tada")
        self.play(FadeIn(big, scale=0.4, rate_func=BOUNCE), FadeIn(brand, shift=UP * 0.2),
                  run_time=1.1)
        self.play(GrowFromCenter(VGroup(box, call), rate_func=BOUNCE), run_time=0.9)
        rng = random.Random(9)
        rain = VGroup(*[star(PALETTE[i % 5], rng.uniform(0.14, 0.3)).move_to(
            [rng.uniform(-4.0, 4.0), rng.uniform(-7.5, 7.5), 0]) for i in range(18)])
        self.play(LaggedStart(*[FadeIn(s, scale=0.2, rate_func=BOUNCE) for s in rain],
                              lag_ratio=0.06), run_time=1.4)
        self.wait(max(d - 3.4, 0.5))
        self.wait(0.8)

    # ── assemblage ─────────────────────────────────────────────
    def construct(self):
        self.keep = set()
        decor = self.make_decor()
        self.add(decor)
        self.keep.update(id(m) for m in decor)
        self.keep.add(id(decor))
        self.s_intro()
        self.s_un_seul()
        self.s_rappel()
        self.s_stars()
        self.s_regle()
        self.s_ecrire()
        self.s_parcours()
        self.s_qr()
        self.s_parents()
        self.s_ecole()
        self.s_outro()
