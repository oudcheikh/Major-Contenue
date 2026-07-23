# -*- coding: utf-8 -*-
"""Vidéo U24 — الفائدة السنوية.  Rendu : venv/bin/manim -qh scene_u24.py VideoU24
Cœur de la vidéo : les 3 boîtes رأس المال / النسبة / الفائدة, la formule
الفائدة = رأس المال × النسبة ÷ 100 construite pas à pas, l'exemple du cahier
(20 000 أوقية بنسبة 5 % ← 1 000, puis 6 أشهر ← 500) sur la barre des 12 mois."""
from manim import (VGroup, RoundedRectangle, SurroundingRectangle, Arrow, Circle,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter,
                   Indicate, Wiggle, Flash,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled, strip,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


def rtl_row(pieces, buff=0.3):
    """Aligne des morceaux de DROITE à GAUCHE (le 1er est le plus à droite)."""
    for i in range(1, len(pieces)):
        pieces[i].next_to(pieces[i - 1], LEFT, buff=buff)
    return VGroup(*pieces)


def coin(x, y):
    c = Circle(radius=0.32, fill_color=GOLD, fill_opacity=1,
               stroke_color=INK, stroke_width=2).move_to([x, y, 0])
    return c


class VideoU24(MajorScene):
    AUDIO = HERE / "audio_u24"
    UNIT_AR = "الوحدة 24"
    UNIT_COLOR = YELL
    TITLE = "الفائدة السنوية"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 24"

    # ── 2. المفهوم : المال ينمو في البنك ────────────────────────
    def s_concept(self):
        d = self.seg("def1")
        head = titled("مالُك في البنك ينمو", 40, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        banque = RoundedRectangle(corner_radius=0.25, width=3.2, height=2.2, fill_color=BLUE,
                                  fill_opacity=0.18, stroke_color=INK,
                                  stroke_width=3).move_to(LEFT * 3.2 + DOWN * 0.7)
        b_lab = ar("البنك", 28, "BOLD", BLUE).next_to(banque, DOWN, buff=0.25)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(banque, b_lab), rate_func=BOUNCE), run_time=1.0)
        pile = VGroup(coin(2.6, -1.4), coin(2.6, -0.8), coin(2.6, -0.2))
        self.sfx("pop")
        self.play(FadeIn(pile, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.8)
        plus = VGroup(coin(2.6, 0.4), coin(2.6, 1.0))
        for c in plus:                       # la pile grandit : c'est la fائدة
            self.sfx("ding")
            self.play(FadeIn(c, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.5)
        self.wait(max(d - 3.7, 0.2))

        d = self.seg("def2")   # les 3 boîtes, de droite à gauche
        self.play(FadeOut(banque), FadeOut(b_lab), FadeOut(pile), FadeOut(plus), run_time=0.5)
        trio = [("رأس المال", GREEN, 4.2), ("نسبة التوظيف", BLUE, 0.0), ("الفائدة السنوية", ROSE, -4.2)]
        self.boxes = VGroup()
        for txt, col, x in trio:
            b = RoundedRectangle(corner_radius=0.22, width=3.7, height=1.15, fill_color=col,
                                 fill_opacity=0.92, stroke_color=INK).move_to([x, -0.5, 0])
            t = ar(txt, 30, "BOLD", "#FFFFFF").move_to(b)
            self.boxes.add(VGroup(b, t))
            self.sfx("pop")
            self.play(GrowFromCenter(self.boxes[-1], rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 3.2, 0.2))

        d = self.seg("def3")   # 5 % : كل 100 أوقية تنتج 5 أوقيات
        cent = VGroup(num("100", 40, GREEN), ar("أوقية رأس مال", 22)).arrange(DOWN, buff=0.12)
        cent.move_to(RIGHT * 3.3 + DOWN * 2.4)
        arr = Arrow(RIGHT * 1.5 + DOWN * 2.4, LEFT * 0.3 + DOWN * 2.4, color=GOLD,
                    stroke_width=5, max_tip_length_to_length_ratio=0.2)
        cinq = VGroup(num("5", 40, ROSE), ar("أوقيات فائدة في السنة", 22)).arrange(DOWN, buff=0.12)
        cinq.move_to(LEFT * 2.6 + DOWN * 2.4)
        self.sfx("pop")
        self.play(FadeIn(cent, shift=LEFT * 0.3, rate_func=BOUNCE), run_time=0.8)
        self.sfx("whoosh")
        self.play(Create(arr), run_time=0.6)
        self.sfx("ding")
        self.play(FadeIn(cinq, shift=LEFT * 0.3, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 2.2, 0.2))
        self.clear_all()

    # ── 3. القاعدة الذهبية ثم المثال : 20 000 × 5 ÷ 100 ────────
    def s_formule(self):
        d = self.seg("form1")
        head = titled("القاعدة الذهبية", 42, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        pieces = [ar("الفائدة السنوية", 34, "BOLD", ROSE),
                  num("=", 44),
                  ar("رأس المال", 34, "BOLD", GREEN),
                  num("×", 44, GOLD),
                  ar("النسبة", 34, "BOLD", BLUE),
                  num("÷", 44, GOLD),
                  num("100", 44)]
        formule = rtl_row(pieces).move_to(UP * 0.9)
        for p in pieces:      # construction pas à pas, de droite à gauche
            self.sfx("pop")
            self.play(FadeIn(p, shift=LEFT * 0.3, rate_func=BOUNCE), run_time=0.4)
        cadre = SurroundingRectangle(formule, color=GOLD, corner_radius=0.18, buff=0.25)
        self.play(Create(cadre), run_time=0.8)
        self.formule = VGroup(formule, cadre)
        self.wait(max(d - 4.5, 0.2))

        d = self.seg("ex1")   # le تاجر du cahier
        donnees = rtl_row([ar("وظّف تاجر", 28),
                           num("20 000", 40, GREEN),
                           ar("أوقية بنسبة", 28),
                           num("5 %", 40, BLUE)], buff=0.35).move_to(DOWN * 0.6)
        self.sfx("pop")
        self.play(FadeIn(donnees, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 1.0, 0.2))

        d = self.seg("ex2")   # 20 000 × 5 ÷ 100 = 1 000
        calc = num("20 000 × 5 ÷ 100 = 1 000", 46, GREEN).move_to(DOWN * 1.9)
        self.play(Write(calc), run_time=1.4)
        lab = ar("أوقية فائدة في السنة", 24, "BOLD", GREEN).next_to(calc, DOWN, buff=0.25)
        self.sfx("ding")
        self.play(FadeIn(lab), run_time=0.6)
        self.play(Flash(calc, color=GREEN, flash_radius=3.2), run_time=0.8)
        self.wait(max(d - 2.8, 0.2))
        self.clear_all()

    # ── 4. فائدة عدة أشهر : شريط 12 شهرًا ───────────────────────
    def s_mois(self):
        d = self.seg("mois1")
        head = titled("فائدة عدة أشهر", 40, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        an = rtl_row([ar("فائدة السنة كاملة:", 26),
                      num("1 000", 36, GOLD),
                      ar("أوقية", 24)], buff=0.3).move_to(UP * 1.3)
        self.sfx("pop")
        self.play(FadeIn(an, shift=LEFT * 0.4, rate_func=BOUNCE), run_time=0.9)
        # barre des 12 mois, 6 remplis depuis la droite (RTL)
        bar = strip(12, 6, width=6.4, height=0.75, fill=GREEN).move_to(DOWN * 0.1)
        lab12 = ar("اثنا عشر شهرًا", 22).next_to(bar, UP, buff=0.2)
        lab6 = ar("ستة أشهر", 24, "BOLD", GREEN).next_to(bar, DOWN, buff=0.25).shift(RIGHT * 1.6)
        self.sfx("whoosh")
        self.play(FadeIn(bar, scale=0.7), FadeIn(lab12), run_time=1.0)
        self.sfx("pop")
        self.play(FadeIn(lab6, shift=UP * 0.2, rate_func=BOUNCE), run_time=0.7)
        self.wait(max(d - 3.5, 0.2))

        d = self.seg("mois2")   # 1 000 × 6 ÷ 12 = 500
        calc = num("1 000 × 6 ÷ 12 = 500", 46, GREEN).move_to(DOWN * 1.9)
        self.play(Write(calc), run_time=1.3)
        lab = ar("أوقية عن ستة أشهر", 24, "BOLD", GREEN).next_to(calc, DOWN, buff=0.25)
        self.sfx("ding")
        self.play(FadeIn(lab), run_time=0.6)
        self.play(Flash(calc, color=GREEN, flash_radius=3.0), run_time=0.8)
        self.wait(max(d - 2.7, 0.2))
        self.clear_all()

    # ── 5. انتبه : النسبة سنوية ─────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! النسبة سنوية لا شهرية", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        box = RoundedRectangle(corner_radius=0.22, width=6.6, height=1.15, fill_color=REDA,
                               fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 1.9 + DOWN * 0.4)
        boxt = ar("أحسب فائدة السنة كاملة أولًا ثم أقسم", 28, "BOLD", "#FFFFFF").move_to(box)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(box, boxt), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.0, 0.2))
        self.clear_all()

    # ── 6. السر : القاعدة تعمل في الاتجاهين ─────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: القاعدة تعمل في الاتجاهين", 34, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        inverse = rtl_row([ar("النسبة", 32, "BOLD", BLUE),
                           num("=", 40),
                           ar("الفائدة", 32, "BOLD", ROSE),
                           num("× 100 ÷", 40, GOLD),
                           ar("رأس المال", 32, "BOLD", GREEN)]).move_to(UP * 0.6)
        self.sfx("whoosh")
        self.play(FadeIn(inverse, shift=LEFT * 0.4), run_time=1.2)
        ex = num("600 × 100 ÷ 10 000 = 6 %", 44, GREEN).move_to(DOWN * 1.2)
        self.play(Write(ex), run_time=1.4)
        self.sfx("ding")
        self.play(Flash(ex, color=GREEN, flash_radius=3.2), run_time=0.8)
        self.wait(max(d - 4.4, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أحسب الفائدة السنوية من رأس المال والنسبة",
            "أحسب فائدة عدة أشهر",
            "أجد النسبة أو رأس المال عند الحاجة",
        ])
        self.s_concept()
        self.s_formule()
        self.s_mois()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
