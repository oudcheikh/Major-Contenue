# -*- coding: utf-8 -*-
"""Vidéo U2 — الكسور.  Rendu : venv/bin/manim -qh scene_u2.py VideoU2
Tout est imagé et synchronisé : le قرص se découpe pendant que la voix parle,
le بسط/المقام sont étiquetés sur la fraction, la comparaison se voit sur les barres."""
from pathlib import Path

from manim import (VGroup, Line, Arrow, RoundedRectangle,
                   FadeIn, FadeOut, Write, Create, Transform, GrowFromCenter,
                   Indicate, Wiggle,
                   UP, DOWN, LEFT, RIGHT, DR)

from video_common import (MajorScene, ar, num, titled, frac, pie, strip,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


class VideoU2(MajorScene):
    AUDIO = HERE / "audio_u2"
    UNIT_AR = "الوحدة 2"
    UNIT_COLOR = ROSE
    TITLE = "الكسور"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 2"

    # ── 2. المفهوم : le قرص qui se découpe ─────────────────────
    def s_concept(self):
        d = self.seg("conc1")
        head = titled("الكسر جزء من كلٍّ كامل", 40, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # un vrai Circle : AnnularSector à 360° se déforme
        from manim import Circle
        whole = Circle(radius=1.5, stroke_color=INK, stroke_width=3,
                       fill_color="#FFFFFF", fill_opacity=0.9).shift(LEFT * 3 + DOWN * 0.3)
        lab_w = ar("كلٌّ كامل", 30, "BOLD", GOLD).next_to(whole, DOWN, buff=0.4)
        self.play(GrowFromCenter(whole), FadeIn(lab_w), run_time=1.2)
        self.wait(max(d - 2.1, 0.2))

        d = self.seg("conc2")   # découpe en 4, on prend 1 → ربع
        quarters = pie(4, 0, radius=1.5).shift(LEFT * 3 + DOWN * 0.3)
        self.sfx("whoosh")
        self.play(Transform(whole, quarters), FadeOut(lab_w), run_time=1.1)
        self.wait(1.6)
        taken = pie(4, 1, radius=1.5).shift(LEFT * 3 + DOWN * 0.3)
        self.sfx("ding")
        self.play(Transform(whole, taken), run_time=1.0)
        self.fr = frac(1, 4, 60).shift(RIGHT * 3 + DOWN * 0.3)
        lab_q = ar("رُبع", 34, "BOLD", ROSE).next_to(self.fr, DOWN, buff=0.45)
        self.sfx("pop")
        self.play(FadeIn(self.fr, scale=0.5, rate_func=BOUNCE), FadeIn(lab_q), run_time=1.0)
        self.wait(max(d - 4.7, 0.2))
        self.lab_q = lab_q
        self.whole = whole

    # ── 3. البسط والمقام étiquetés sur la fraction ──────────────
    def s_bast_maqam(self):
        d = self.seg("conc3")
        self.play(FadeOut(self.lab_q), self.fr.animate.scale(1.25).move_to(RIGHT * 2.6 + DOWN * 0.2),
                  run_time=0.8)
        top, bar, bot = self.fr
        b_lab = VGroup(
            ar("البسط", 30, "BOLD", GREEN),
            ar("عدد الحصص المأخوذة", 24, color="#666666"),
        ).arrange(DOWN, buff=0.12)
        b_lab.next_to(top, LEFT, buff=1.1).shift(UP * 0.1)
        a_b = Arrow(b_lab.get_right(), top.get_left() + LEFT * 0.1, color=GREEN, stroke_width=4,
                    max_tip_length_to_length_ratio=0.2)
        m_lab = VGroup(
            ar("المقام", 30, "BOLD", BLUE),
            ar("عدد الحصص الكلية", 24, color="#666666"),
        ).arrange(DOWN, buff=0.12)
        m_lab.next_to(bot, LEFT, buff=1.1).shift(DOWN * 0.1)
        a_m = Arrow(m_lab.get_right(), bot.get_left() + LEFT * 0.1, color=BLUE, stroke_width=4,
                    max_tip_length_to_length_ratio=0.2)
        self.wait(1.2)
        self.sfx("pop")
        self.play(FadeIn(b_lab, shift=RIGHT * 0.3), Create(a_b),
                  top.animate.set_color(GREEN), run_time=1.2)
        self.wait(1.8)
        self.sfx("pop")
        self.play(FadeIn(m_lab, shift=RIGHT * 0.3), Create(a_m),
                  bot.animate.set_color(BLUE), run_time=1.2)
        self.wait(max(d - 5.4, 0.2))

        d = self.seg("conc4")   # le sourire du sirr : بسط au-dessus, مقام en dessous
        garcon = self.boy(1.8).to_corner(DR, buff=0.25)
        self.sfx("pop")
        self.play(FadeIn(garcon, scale=0.3, rate_func=BOUNCE), run_time=0.9)
        self.play(Indicate(top, color=GREEN, scale_factor=1.4), run_time=1.1)
        self.wait(0.9)
        self.play(Indicate(bot, color=BLUE, scale_factor=1.4), run_time=1.1)
        self.play(Wiggle(garcon), run_time=1.2)
        self.wait(max(d - 5.2, 0.2))
        self.clear_all()

    # ── 4. أشهر الكسور : نصف، ثلث، ربع، ثلاثة أرباع، كل كامل ────
    def s_reperes(self):
        d = self.seg("rep1")
        head = titled("أشهر الكسور", 42, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(1.4)
        trio = [("النصف", 2, 1, 3.9, YELL), ("الثلث", 3, 1, 0.0, GREEN), ("الربع", 4, 1, -3.9, BLUE)]
        pies = {}
        for lab_t, parts, filled, x, col in trio:   # droite → gauche, au rythme de la voix
            p = pie(parts, filled, radius=1.05, fill=col).move_to([x, 0.6, 0])
            f = frac(1, parts, 34).next_to(p, DOWN, buff=0.35)
            lab = ar(lab_t, 28, "BOLD", col if col != YELL else GOLD).next_to(f, DOWN, buff=0.2)
            pies[lab_t] = VGroup(p, f, lab)
            self.sfx("pop")
            self.play(FadeIn(pies[lab_t], scale=0.4, rate_func=BOUNCE), run_time=0.9)
            self.wait(0.75)
        self.wait(max(d - 2.3 - 3 * 1.65, 0.2))

        d = self.seg("rep2")   # ثلاثة أرباع
        self.play(*[FadeOut(v) for v in pies.values()], run_time=0.5)
        p34 = pie(4, 3, radius=1.35, fill=ROSE).move_to(LEFT * 2.8 + DOWN * 0.35)
        f34 = frac(3, 4, 54, ROSE).move_to(RIGHT * 2.6 + DOWN * 0.55)
        lab34 = ar("ثلاثة أرباع", 32, "BOLD", ROSE).next_to(f34, DOWN, buff=0.35)
        self.sfx("ding")
        self.play(GrowFromCenter(p34), FadeIn(f34, scale=0.5, rate_func=BOUNCE),
                  FadeIn(lab34), run_time=1.3)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("rep3")   # 4/4 = الكل الكامل = 1
        p44 = pie(4, 4, radius=1.35, fill=GREEN).move_to(LEFT * 2.8 + DOWN * 0.35)
        f44 = frac(4, 4, 54, GREEN).move_to(RIGHT * 3.4 + DOWN * 0.55)
        eq1 = num("= 1", 54, GREEN).next_to(f44, LEFT, buff=0.4)
        lab44 = ar("الكلُّ الكامل", 32, "BOLD", GREEN).next_to(VGroup(f44, eq1), DOWN, buff=0.35)
        self.sfx("whoosh")
        self.play(Transform(p34, p44), Transform(f34, f44), FadeOut(lab34), run_time=1.1)
        self.sfx("ding")
        self.play(FadeIn(eq1, scale=0.5, rate_func=BOUNCE), FadeIn(lab44), run_time=1.0)
        self.wait(max(d - 2.6, 0.2))
        self.clear_all()

    # ── 5. المقارنة (نفس المقام) sur les barres ────────────────
    def s_compare(self):
        d = self.seg("comp1")
        head = titled("أقارن كسرين لهما نفس المقام", 38, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        r1 = ar("أتأكد أن المقامين متساويان", 30)
        r2 = ar("صاحب البسط الأكبر هو الكسر الأكبر", 30, "BOLD", GREEN)
        c1 = num("1", 26, "#FFFFFF")
        c2 = num("2", 26, "#FFFFFF")
        b1 = RoundedRectangle(corner_radius=0.22, width=0.7, height=0.7, fill_color=BLUE,
                              fill_opacity=1, stroke_color=INK)
        b2 = RoundedRectangle(corner_radius=0.22, width=0.7, height=0.7, fill_color=GREEN,
                              fill_opacity=1, stroke_color=INK)
        c1.move_to(b1); c2.move_to(b2)
        row1 = VGroup(r1, VGroup(b1, c1))
        r1.next_to(b1, LEFT, buff=0.45)
        row1.move_to(UP * 0.9).to_edge(RIGHT, buff=1.0)
        row2 = VGroup(r2, VGroup(b2, c2))
        r2.next_to(b2, LEFT, buff=0.45)
        row2.move_to(UP * 0.0).to_edge(RIGHT, buff=1.0)
        self.wait(2.2)
        self.sfx("pop")
        self.play(FadeIn(row1, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.6)
        self.sfx("pop")
        self.play(FadeIn(row2, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 6.7, 0.2))

        d = self.seg("comp2")   # 5/7 > 2/7 sur des barres
        self.play(FadeOut(row1), FadeOut(row2), run_time=0.5)
        s57 = strip(7, 5, width=4.6, fill=GREEN).move_to(RIGHT * 3.1 + DOWN * 0.6)
        f57 = frac(5, 7, 36, GREEN).next_to(s57, DOWN, buff=0.3)
        s27 = strip(7, 2, width=4.6, fill=ROSE).move_to(LEFT * 3.1 + DOWN * 0.6)
        f27 = frac(2, 7, 36, ROSE).next_to(s27, DOWN, buff=0.3)
        self.sfx("pop")
        self.play(FadeIn(VGroup(s57, f57), scale=0.6, rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(FadeIn(VGroup(s27, f27), scale=0.6, rate_func=BOUNCE), run_time=0.9)
        gt = num(">", 72, GOLD).move_to(DOWN * 0.6)
        self.sfx("ding")
        self.play(GrowFromCenter(gt, rate_func=BOUNCE), run_time=0.8)
        self.play(Indicate(f57[0], color=GREEN, scale_factor=1.5), run_time=1.0)
        self.play(Indicate(f27[0], color=REDA, scale_factor=1.5), run_time=1.0)
        self.wait(max(d - 5.1, 0.2))
        self.clear_all()

    # ── 6. انتبه : المقام الأكبر ≠ كسر أكبر ─────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! المقام الأكبر لا يعني كسرًا أكبر", 38, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 1.0, 0.2))

        d = self.seg("att2")   # 1/2 vs 1/8, même largeur totale
        s12 = strip(2, 1, width=5.2, height=0.85, fill=GREEN).move_to(RIGHT * 0.6 + UP * 0.9)
        f12 = frac(1, 2, 32, GREEN).next_to(s12, RIGHT, buff=0.5)
        s18 = strip(8, 1, width=5.2, height=0.85, fill=ROSE).move_to(RIGHT * 0.6 + DOWN * 0.7)
        f18 = frac(1, 8, 32, ROSE).next_to(s18, RIGHT, buff=0.5)
        self.sfx("pop")
        self.play(FadeIn(VGroup(s12, f12), scale=0.7), run_time=0.9)
        self.wait(1.2)
        self.sfx("pop")
        self.play(FadeIn(VGroup(s18, f18), scale=0.7), run_time=0.9)
        self.wait(1.4)
        self.play(Indicate(s12[0], color=GREEN, scale_factor=1.15), run_time=1.0)
        self.play(Indicate(s18[0], color=REDA, scale_factor=1.3), run_time=1.0)
        verdict = ar("النصف أكبر من الثُّمُن", 30, "BOLD", GREEN).move_to(DOWN * 2.15 + RIGHT * 0.6)
        self.sfx("ding")
        self.play(Write(verdict), run_time=1.2)
        self.wait(max(d - 6.4, 0.2))
        self.clear_all()

    # ── 7. السر : نفس البسط ← كلما كبر المقام صغرت الحصة ───────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ صغير قبل أن نفترق", 42, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(2.6)
        rows = [(2, GREEN, 1.15), (4, BLUE, 0.0), (8, ROSE, -1.15)]
        for parts, col, y in rows:
            s = strip(parts, 1, width=5.2, height=0.8, fill=col).move_to([0.4, y - 0.35, 0])
            f = frac(1, parts, 28, col).next_to(s, RIGHT, buff=0.45)
            self.sfx("pop")
            self.play(FadeIn(VGroup(s, f), scale=0.7, rate_func=BOUNCE), run_time=0.8)
            self.wait(0.7)
        morale = ar("كلما كبر المقام، صغرت الحصة!", 32, "BOLD", LILA).move_to(DOWN * 2.6 + RIGHT * 0.4)
        self.sfx("ding")
        self.play(Write(morale), run_time=1.4)
        self.wait(max(d - 9.6, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أتعرّف البسط والمقام في الكسر",
            "أمثّل الكسور بالرسم",
            "أقارن الكسور",
        ])
        self.s_concept()
        self.s_bast_maqam()
        self.s_reperes()
        self.s_compare()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
