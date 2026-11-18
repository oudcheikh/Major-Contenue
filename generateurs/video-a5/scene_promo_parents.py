# -*- coding: utf-8 -*-
"""Vidéo PROMO PARENTS 9:16 (12/11/2026) — marketing, ~1 min, VOIX DE L'UTILISATEUR.
Rendu : venv/bin/manim --disable_caching scene_promo_parents.py VideoPromoParents
Audio : voix-clone/sortie/promo-parents/phrase-NN.wav (texte : voix-clone/textes/promo-parents.txt ;
« Major » y est prononcé à la française, inséré par voix-clone/assembler_major.py).
1 phrase = 1 bloc d'animation ; chaque bloc se cale sur l'horloge du rendu (renderer.time),
donc la synchro tient même si une phrase est régénérée avec une autre durée."""
import json
import os
import random
from pathlib import Path

from manim import (Scene, Text, VGroup, Group, RoundedRectangle, Circle, Line, Polygon,
                   SurroundingRectangle, ImageMobject, Difference,
                   FadeIn, FadeOut, Write, Create, LaggedStart, GrowFromCenter,
                   Indicate, Wiggle, UP, DOWN, LEFT, RIGHT, UL, config)

from scene_promo import (ar, star, stars_row, zone, card,
                         INK, YELL, ROSE, GREEN, BLUE, LILA, ROYAL, PALETTE, BOUNCE)

if os.environ.get("APERCU"):          # rendu d'essai rapide en 540×960
    config.pixel_width, config.pixel_height, config.frame_rate = 540, 960, 15

HERE = Path(__file__).parent
VOIX =HERE.parent / "voix-clone/sortie/promo-parents"
SFX = HERE / "sfx"
P2 = HERE / "assets/promo2"
DUR = json.loads((VOIX / "durations.json").read_text())
GAP = 0.35          # respiration après chaque phrase
ORANGE = "#EE7A1B"  # orange des nouvelles couvertures

# Laisser vide tant que le canal de vente n'est pas fixé ; sinon ex. "واتساب: 00 00 00 00"
CONTACT = ""


def cover(name, height):
    p = ImageMobject(str(P2 / f"cover-{name}.png")).scale_to_fit_height(height)
    frame = SurroundingRectangle(p, color=INK, buff=0, stroke_width=3)
    return Group(p, frame)


def pg(name, height):
    """Page du cahier (assets/promo2) encadrée ; même structure que page_img pour zone()."""
    p = ImageMobject(str(P2 / name)).scale_to_fit_height(height)
    frame = SurroundingRectangle(p, color=INK, buff=0, corner_radius=0.02, stroke_width=3)
    return Group(p, frame)


def pill(txt, color, size=34, fg="#FFFFFF"):
    t = ar(txt, size, "BOLD", fg)
    box = RoundedRectangle(corner_radius=0.32, width=t.width + 0.8, height=t.height + 0.5,
                           fill_color=color, fill_opacity=1, stroke_color=INK, stroke_width=2.5)
    return VGroup(box, t.move_to(box))


def fit(m, w):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


class VideoPromoParents(Scene):
    # ── infrastructure ─────────────────────────────────────────
    def seg(self, i):
        name = f"phrase-{i:02d}"
        # La voix clonée sort à 0 dBFS crête (−16 dB moyen, contre −22 pour edge-tts) :
        # −3 dB laisse de la marge pour les bruitages et la musique mixés par-dessus.
        self.add_sound(str(VOIX / f"{name}.wav"), gain=-3)
        self.t_end = self.renderer.time + DUR[name] + GAP

    def fill(self):
        self.wait(max(self.t_end - self.renderer.time, 0.1))

    def sfx(self, name):
        self.add_sound(str(SFX / f"{name}.wav"))

    def clear_all(self, rt=0.5):
        ms = [m for m in self.mobjects if id(m) not in self.keep]
        if ms:
            self.sfx("whoosh")
            self.play(*[FadeOut(m, shift=DOWN * 0.3) for m in ms], run_time=rt)

    def make_decor(self):
        rng = random.Random(12)
        decor = VGroup()
        spots = [(3.8, 6.9), (4.0, 2.6), (3.6, -3.0), (3.7, -6.9),
                 (-3.8, -6.6), (-4.0, 3.6), (-3.5, -1.4), (-3.9, 6.0)]
        for i, (x, y) in enumerate(spots):
            col = PALETTE[i % len(PALETTE)]
            r = rng.uniform(0.16, 0.32)
            m = (Circle(radius=r, fill_color=col, fill_opacity=0.28, stroke_width=0) if i % 2 == 0
                 else star(col, r).set_stroke(width=0).set_fill(opacity=0.38))
            decor.add(m.move_to([x, y, 0]).rotate(rng.uniform(0, 3)))
        return decor

    def phone(self, height=8.6):
        body = RoundedRectangle(corner_radius=0.4, width=height * 0.57, height=height,
                                fill_color="#FFFFFF", fill_opacity=1,
                                stroke_color=INK, stroke_width=7)
        speaker = RoundedRectangle(corner_radius=0.06, width=1.2, height=0.12,
                                   fill_color=INK, fill_opacity=1, stroke_width=0)
        speaker.move_to(body.get_top() + DOWN * 0.35)
        return VGroup(body, speaker)

    # ── 1. Accroche : le parent, chaque soir ───────────────────
    def s_hook(self):
        self.seg(1)
        moon = Difference(Circle(radius=0.75), Circle(radius=0.65).shift(RIGHT * 0.38 + UP * 0.22),
                          fill_color=YELL, fill_opacity=1, stroke_color=INK, stroke_width=2)
        moon.move_to(UP * 6.5 + RIGHT * 2.8)
        soir = ar("كل مساء...", 64, "BOLD", ROYAL).move_to(UP * 6.4 + LEFT * 0.6)
        self.play(FadeIn(moon, scale=0.4, rate_func=BOUNCE), Write(soir), run_time=1.0)
        kids = ImageMobject(str(P2 / "enfants.png")).scale_to_fit_width(8.2).move_to(UP * 1.6)
        frame = SurroundingRectangle(kids, color=INK, buff=0, corner_radius=0.05, stroke_width=3)
        self.play(FadeIn(Group(kids, frame), shift=UP * 0.5), run_time=0.8)
        q = card("كيف أساعد طفلي في المراجعة؟", ROSE, 8.2, 1.5, 46).move_to(DOWN * 4.0)
        self.sfx("boing")
        self.play(GrowFromCenter(q, rate_func=BOUNCE), run_time=0.8)
        spots = [(-3.5, -2.3, 100), (3.5, -2.5, 90), (-3.0, -6.1, 110), (3.1, -6.0, 100), (0, -6.6, 80)]
        marks = VGroup(*[ar("؟", s, "BOLD", PALETTE[i % 5]).move_to([x, y, 0])
                         for i, (x, y, s) in enumerate(spots)])
        self.play(LaggedStart(*[FadeIn(m, scale=0.3, rate_func=BOUNCE) for m in marks],
                              lag_ratio=0.15), run_time=1.0)
        self.play(Wiggle(q), run_time=0.9)
        self.fill()
        self.clear_all()

    # ── 2. La solution : هذا دفتر ماجور ────────────────────────
    def s_solution(self):
        self.seg(2)
        self.logo = ImageMobject(str(HERE / "assets/major-logo.png")).scale_to_fit_height(2.0)
        self.logo.move_to(UP * 5.4)
        sol = ar("الحل بين أيديكم", 50, "BOLD", INK).move_to(UP * 3.6)
        self.sfx("ding")
        self.play(FadeIn(self.logo, scale=0.4, rate_func=BOUNCE), FadeIn(sol, shift=UP * 0.2),
                  run_time=0.9)
        title = ar("هذا دفتر ماجور", 92, "BOLD", ROYAL).move_to(UP * 2.0)
        self.play(Write(title), run_time=1.0)
        cv = cover("math", 8.0).move_to(DOWN * 3.6)
        self.sfx("tada")
        self.play(FadeIn(cv, shift=UP * 0.8, scale=0.7, rate_func=BOUNCE), run_time=0.9)
        self.fill()
        self.play(FadeOut(sol), FadeOut(title),
                  self.logo.animate.scale_to_fit_height(0.85).to_corner(UL, buff=0.35),
                  cv.animate.scale_to_fit_height(5.4).move_to(UP * 3.1 + RIGHT * 2.1).rotate(-0.08),
                  run_time=0.7)
        self.keep.add(id(self.logo))
        self.cv_math = cv

    # ── 3. La collection : toutes les matières ─────────────────
    def s_collection(self):
        self.seg(3)
        others = [cover(n, 5.4) for n in ("arabe", "hg", "fr")]
        others[0].move_to(UP * 3.1 + LEFT * 2.1).rotate(0.08)
        others[1].move_to(DOWN * 2.7 + RIGHT * 2.1).rotate(0.06)
        others[2].move_to(DOWN * 2.7 + LEFT * 2.1).rotate(-0.06)
        for c in others:
            self.sfx("pop")
            self.play(FadeIn(c, scale=0.5, rate_func=BOUNCE), run_time=0.55)
        band = pill("لكل مواد السنة السادسة", ORANGE, 44).move_to(DOWN * 6.6)
        tags = VGroup(pill("ذكية", ROSE, 36), pill("تفاعلية", GREEN, 36))
        tags.arrange(LEFT, buff=0.5).move_to(UP * 0.2)
        self.play(GrowFromCenter(tags[0], rate_func=BOUNCE), GrowFromCenter(tags[1], rate_func=BOUNCE),
                  run_time=0.7)
        self.play(FadeIn(band, shift=UP * 0.3), run_time=0.6)
        self.fill()
        self.clear_all()

    # ── 4. Dans chaque leçon : rappel + exemple résolu ─────────
    # Vraie page du PDF actuel (الكسور والمقارنة, p. 12) : règles en haut, مثال محلول, exercices.
    def s_lecon(self):
        self.seg(4)
        head = card("في كل درس", YELL, 6.4, 1.15, 48).move_to(UP * 6.6)
        page = pg("page-kusur.png", 11.0).move_to(DOWN * 0.6)
        self.sfx("pop")
        self.play(GrowFromCenter(head, rate_func=BOUNCE), FadeIn(page, shift=UP * 0.5), run_time=0.8)
        z1 = zone(page, 0.03, 0.175, 0.94, 0.20, BLUE)
        l1 = pill("تذكير قصير", BLUE, 36).next_to(z1, DOWN, buff=-0.35).shift(LEFT * 2.0)
        self.sfx("ding")
        self.play(Create(z1), FadeIn(l1, shift=UP * 0.3), run_time=0.8)
        z2 = zone(page, 0.03, 0.374, 0.94, 0.058, ROSE)
        l2 = pill("مثال محلول خطوة خطوة", ROSE, 36).move_to(DOWN * 6.9)
        self.sfx("ding")
        self.play(Create(z2), FadeIn(l2, shift=UP * 0.3), run_time=0.8)
        self.fill()
        self.play(FadeOut(z1), FadeOut(l1), FadeOut(z2), FadeOut(l2), FadeOut(head), run_time=0.4)
        self.page = page

    # ── 5. Exercices progressifs ⭐ → ⭐⭐⭐ ──────────────────────
    def s_exos(self):
        self.seg(5)
        head = card("تمارين متدرجة", GREEN, 6.6, 1.15, 48).move_to(UP * 6.6)
        page = self.page
        self.play(GrowFromCenter(head, rate_func=BOUNCE),
                  page.animate.scale_to_fit_height(8.4).move_to(UP * 1.6), run_time=0.8)
        z3 = zone(page, 0.03, 0.432, 0.94, 0.25, GREEN)
        self.sfx("ding")
        self.play(Create(z3), run_time=0.5)
        rows = VGroup()
        for i, (txt, n, col) in enumerate([("سهل", 1, GREEN), ("متوسط", 2, BLUE), ("تحدٍّ", 3, ROSE)]):
            box = RoundedRectangle(corner_radius=0.22, width=6.4, height=0.95,
                                   fill_color=col, fill_opacity=0.28, stroke_color=col, stroke_width=3)
            t = ar(txt, 36, "BOLD").move_to(box.get_center() + LEFT * 1.2)
            s = stars_row(n, YELL, 0.22)
            s.move_to(box.get_right() + LEFT * (s.width / 2 + 0.4))
            rows.add(VGroup(box, t, s).move_to(DOWN * (4.1 + 1.15 * i)))
        for row in rows:
            self.sfx("pop")
            self.play(FadeIn(row, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=0.5)
        self.play(Wiggle(rows[2][2]), run_time=0.7)
        self.fill()
        self.clear_all()

    # ── 6-7. Téléphone → المنصة الذكية ──────────────────────────
    def s_plateforme(self):
        self.seg(6)
        page = pg("page-kusur.png", 6.2).move_to(UP * 4.2 + RIGHT * 1.6).rotate(-0.05)
        qr = ImageMobject(str(HERE / "assets/promo/qr.png")).scale_to_fit_height(2.2)
        qr.move_to(UP * 4.0 + LEFT * 2.4)
        qr_frame = SurroundingRectangle(qr, color=YELL, buff=0.12, corner_radius=0.15, stroke_width=7)
        self.play(FadeIn(page, shift=UP * 0.4), FadeIn(qr, scale=0.4, rate_func=BOUNCE),
                  Create(qr_frame), run_time=0.8)
        ph = self.phone(8.4).move_to(DOWN * 3.3)
        self.sfx("whoosh")
        self.play(FadeIn(ph, shift=UP * 0.8), run_time=0.6)
        self.play(qr.animate.scale_to_fit_height(1.5).move_to(ph.get_top() + DOWN * 1.4),
                  FadeOut(qr_frame), run_time=0.6)
        scan = Line(LEFT * 0.9, RIGHT * 0.9, color=GREEN, stroke_width=6).move_to(qr.get_top())
        self.play(scan.animate.move_to(qr.get_bottom()), run_time=0.4)
        banner = pill("المنصة الذكية", ROYAL, 38)
        fit(banner, ph[0].width - 0.4).move_to(qr)
        self.sfx("ding")
        self.play(FadeOut(scan), FadeOut(qr), GrowFromCenter(banner, rate_func=BOUNCE), run_time=0.6)
        self.fill()

        self.seg(7)
        apps = [("بطاقات مراجعة", BLUE), ("أسئلة تفاعلية", GREEN), ("شرح بالصوت والصورة", ROSE)]
        cards = VGroup()
        for i, (txt, col) in enumerate(apps):
            c = card(txt, col, ph[0].width - 0.6, 1.1, 32)
            cards.add(c.move_to(ph.get_top() + DOWN * (2.8 + 1.45 * i)))
        tri = Polygon([-0.14, 0.18, 0], [-0.14, -0.18, 0], [0.18, 0, 0], fill_color="#FFFFFF",
                      fill_opacity=1, stroke_color=INK, stroke_width=2)
        tri.move_to(cards[2][0].get_left() + RIGHT * 0.4)
        # le triangle « lecture » prend la gauche de la carte : on décale le texte à droite
        txt = cards[2][1]
        txt.scale_to_fit_width(cards[2][0].width - 1.3).move_to(cards[2][0]).shift(RIGHT * 0.3)
        for c in cards:
            self.sfx("pop")
            self.play(GrowFromCenter(c, rate_func=BOUNCE), run_time=0.55)
        self.play(FadeIn(tri, scale=0.4), Indicate(cards[2]), run_time=0.6)
        bravo = VGroup(ar("أحسنت!", 44, "BOLD", GREEN), stars_row(3, YELL, 0.26)).arrange(DOWN, buff=0.2)
        bravo.move_to(ph.get_bottom() + UP * 1.3)
        self.sfx("tada")
        self.play(FadeIn(bravo, scale=0.4, rate_func=BOUNCE), run_time=0.6)
        self.fill()
        self.clear_all()

    # ── 8. Le parent n'a pas besoin d'être enseignant ──────────
    def s_parents(self):
        self.seg(8)
        head = ar("لا تحتاجون أن تكونوا معلمين", 50, "BOLD", ROYAL)
        fit(head, 8.2).move_to(UP * 6.2)
        self.play(Write(head), run_time=0.9)
        kids = ImageMobject(str(P2 / "enfants.png")).scale_to_fit_width(7.6).move_to(UP * 1.6)
        frame = SurroundingRectangle(kids, color=INK, buff=0, corner_radius=0.05, stroke_width=3)
        self.play(FadeIn(Group(kids, frame), shift=UP * 0.4), run_time=0.6)
        ok1 = card("الحلول موجودة ✓", GREEN, 7.0, 1.3, 46).move_to(DOWN * 3.6)
        ok2 = card("دوركم: التشجيع", ORANGE, 7.0, 1.3, 46).move_to(DOWN * 5.3)
        self.sfx("pop")
        self.play(FadeIn(ok1, shift=LEFT * 0.6, rate_func=BOUNCE), run_time=0.6)
        self.sfx("pop")
        self.play(FadeIn(ok2, shift=LEFT * 0.6, rate_func=BOUNCE), run_time=0.6)
        hearts = VGroup(*[star(c, 0.3) for c in (YELL, ROSE, GREEN)]).arrange(RIGHT, buff=0.4)
        hearts.move_to(DOWN * 6.9)
        self.play(LaggedStart(*[FadeIn(h, scale=0.3, rate_func=BOUNCE) for h in hearts],
                              lag_ratio=0.2), run_time=0.7)
        self.fill()
        self.clear_all()

    # ── 9. Preuve : مجرَّب وأثبت نتائجه ──────────────────────────
    def s_preuve(self):
        self.seg(9)
        disc = Circle(radius=2.3, fill_color=GREEN, fill_opacity=1, stroke_color=INK, stroke_width=4)
        ring = Circle(radius=2.0, stroke_color="#FFFFFF", stroke_width=4).set_fill(opacity=0)
        check = Text("✓", font="DejaVu Sans", font_size=150, weight="BOLD", color="#FFFFFF")
        badge = VGroup(disc, ring, check).move_to(UP * 3.6)
        self.sfx("tada")
        self.play(GrowFromCenter(badge, rate_func=BOUNCE), run_time=0.8)
        t1 = ar("مجرَّب مع تلاميذ ماجور", 52, "BOLD", INK)
        fit(t1, 8.2).move_to(DOWN * 0.1)
        self.play(FadeIn(t1, shift=UP * 0.3), run_time=0.6)
        rate = stars_row(5, YELL, 0.42).move_to(DOWN * 2.0)
        self.play(LaggedStart(*[FadeIn(s, scale=0.2, rate_func=BOUNCE) for s in rate],
                              lag_ratio=0.15), run_time=0.9)
        t2 = pill("وأثبت نتائجه", ROYAL, 48).move_to(DOWN * 4.2)
        self.sfx("ding")
        self.play(GrowFromCenter(t2, rate_func=BOUNCE), run_time=0.6)
        self.fill()
        self.clear_all()

    # ── 10. Appel à l'action ───────────────────────────────────
    # ── 10. Le parent, artisan de la réussite (répond à l'accroche) ──
    def s_toi(self):
        self.seg(10)
        kids = ImageMobject(str(P2 / "enfants.png")).scale_to_fit_width(7.6).move_to(UP * 3.6)
        frame = SurroundingRectangle(kids, color=INK, buff=0, corner_radius=0.05, stroke_width=3)
        self.play(FadeIn(Group(kids, frame), shift=UP * 0.4), run_time=0.6)
        t1 = fit(ar("أنت من يصنع", 62, "BOLD", INK), 8.2).move_to(DOWN * 0.6)
        t2 = fit(ar("نجاح طفلك", 84, "BOLD", ROYAL), 8.2).move_to(DOWN * 2.3)
        self.play(Write(t1), run_time=0.7)
        self.play(FadeIn(t2, scale=0.6, rate_func=BOUNCE), run_time=0.6)
        main = pill("بيدك!", ORANGE, 70).move_to(DOWN * 4.6)
        self.sfx("tada")
        self.play(GrowFromCenter(main, rate_func=BOUNCE), run_time=0.7)
        sparks = VGroup(*[star(c, 0.3) for c in (YELL, ROSE, GREEN, BLUE)])
        for s_, (x, y) in zip(sparks, [(-3.4, -4.0), (3.4, -4.0), (-3.0, -5.6), (3.0, -5.6)]):
            s_.move_to([x, y, 0])
        self.play(LaggedStart(*[FadeIn(s_, scale=0.2, rate_func=BOUNCE) for s_ in sparks],
                              lag_ratio=0.12), run_time=0.6)
        self.fill()
        self.clear_all()

    def s_cta(self):
        self.seg(11)
        covers = Group(*[cover(n, 3.6) for n in ("math", "arabe", "hg", "fr")])
        covers.arrange_in_grid(2, 2, buff=0.35).move_to(UP * 3.4)
        self.play(LaggedStart(*[FadeIn(c, scale=0.6, rate_func=BOUNCE) for c in covers],
                              lag_ratio=0.15), run_time=0.9)
        btn = card("اطلبوه الآن: دفتر ماجور!", YELL, 8.2, 1.7, 56).move_to(DOWN * 3.4)
        self.sfx("tada")
        self.play(GrowFromCenter(btn, rate_func=BOUNCE), run_time=0.7)
        if CONTACT:
            ct = ar(CONTACT, 44, "BOLD", ROYAL).move_to(DOWN * 5.3)
            self.play(FadeIn(ct, shift=UP * 0.3), run_time=0.5)
        self.play(Indicate(btn, scale_factor=1.08, color=ORANGE), run_time=0.8)
        self.fill()

    # ── 11. Carte de fin ───────────────────────────────────────
    def s_fin(self):
        self.seg(12)
        others = [m for m in self.mobjects if id(m) not in self.keep and m is not self.logo]
        self.play(*[FadeOut(m) for m in others],
                  self.logo.animate.scale_to_fit_height(3.0).move_to(UP * 3.0), run_time=0.7)
        brand = Text("Major", font="DejaVu Sans", weight="BOLD", font_size=88, color=ROYAL)
        brand.next_to(self.logo, DOWN, buff=0.4)
        box = RoundedRectangle(corner_radius=0.3, width=8.0, height=1.5, fill_color=YELL,
                               fill_opacity=0.97, stroke_color=INK, stroke_width=3).move_to(DOWN * 2.4)
        slogan = fit(ar("ماجور معكم حتى النجاح", 52, "BOLD"), 7.4).move_to(box)
        self.sfx("ding")
        self.play(FadeIn(brand, shift=UP * 0.2), GrowFromCenter(VGroup(box, slogan), rate_func=BOUNCE),
                  run_time=0.8)
        rng = random.Random(9)
        rain = VGroup(*[star(PALETTE[i % 5], rng.uniform(0.14, 0.3)).move_to(
            [rng.uniform(-4.0, 4.0), rng.uniform(-7.5, 7.5), 0]) for i in range(18)])
        self.play(LaggedStart(*[FadeIn(s, scale=0.2, rate_func=BOUNCE) for s in rain],
                              lag_ratio=0.05), run_time=1.0)
        self.fill()
        self.wait(1.2)

    def construct(self):
        self.keep = set()
        decor = self.make_decor()
        self.add(decor)
        self.keep.update(id(m) for m in decor)
        self.keep.add(id(decor))
        self.s_hook()
        self.s_solution()
        self.s_collection()
        self.s_lecon()
        self.s_exos()
        self.s_plateforme()
        self.s_parents()
        self.s_preuve()
        self.s_toi()
        self.s_cta()
        self.s_fin()
