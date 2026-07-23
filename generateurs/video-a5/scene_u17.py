# -*- coding: utf-8 -*-
"""Vidéo U17 — الكسور المتكافئة وجمع الكسور.  Rendu : venv/bin/manim -qh scene_u17.py VideoU17
Cœur de la vidéo : deux قرصين de même taille (النصف et اثنان على أربعة) — la surface
colorée est LA MÊME → متكافئان ; la règle ×2/×2 animée avec flèches ; le جمع sur le
شريط (خُمسان + خُمس = ثلاثة أخماس) ; et كسر من عدد : خُمسا 200 = 80 أوقية."""
from manim import (VGroup, Rectangle, RoundedRectangle, Line, CurvedArrow,
                   SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT, PI)

from video_common import (MajorScene, ar, num, titled, frac, pie, strip,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


class VideoU17(MajorScene):
    AUDIO = HERE / "audio_u17"
    UNIT_AR = "الوحدة 17"
    UNIT_COLOR = YELL
    TITLE = "الكسور المتكافئة وجمع الكسور"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 17"

    # ── 2. التكافؤ : نفس المساحة الملونة ────────────────────────
    def s_equiv(self):
        d = self.seg("eq1")
        head = titled("كسران متكافئان: نفس المساحة!", 34, YELL)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        p1 = pie(2, 1, radius=1.25, fill=BLUE).move_to([2.9, 0.1, 0])
        f1 = frac(1, 2, 44, BLUE).next_to(p1, DOWN, buff=0.35)
        self.sfx("pop")
        self.play(GrowFromCenter(p1, rate_func=BOUNCE), run_time=1.0)
        self.play(FadeIn(f1, shift=UP * 0.2), run_time=0.8)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("eq2")
        p2 = pie(4, 2, radius=1.25, fill=ROSE).move_to([-2.6, 0.1, 0])
        f2 = frac(2, 4, 44, ROSE).next_to(p2, DOWN, buff=0.35)
        self.sfx("pop")
        self.play(GrowFromCenter(p2, rate_func=BOUNCE), run_time=1.0)
        self.play(FadeIn(f2, shift=UP * 0.2), run_time=0.8)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("eq3")
        self.play(Indicate(p1, color=GOLD, scale_factor=1.12),
                  Indicate(p2, color=GOLD, scale_factor=1.12), run_time=1.2)
        eq = num("=", 52, GOLD).move_to([0.15, 0.1, 0])
        self.sfx("ding")
        self.play(GrowFromCenter(eq, rate_func=BOUNCE), run_time=0.8)
        lab = ar("متكافئان!", 34, "BOLD", GREEN).move_to([0.15, -2.3, 0])
        box = SurroundingRectangle(lab, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("pop")
        self.play(FadeIn(lab), Create(box), run_time=0.9)
        self.play(Flash(lab, color=GREEN, flash_radius=1.8), run_time=0.8)
        self.wait(max(d - 3.7, 0.2))
        self.clear_all()

    # ── 3. القاعدة : × نفس العدد، والتبسيط ──────────────────────
    def s_regle(self):
        d = self.seg("eq4")
        head = titled("القاعدة: أضرب البسط والمقام في نفس العدد", 28, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        fA = frac(1, 2, 56).move_to([2.6, 0.2, 0])
        fB = frac(2, 4, 56, GREEN).move_to([-2.2, 0.2, 0])
        self.sfx("pop")
        self.play(FadeIn(fA, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("eq5")
        a1 = CurvedArrow(fA[0].get_left() + LEFT * 0.15, fB[0].get_right() + RIGHT * 0.15,
                         angle=PI / 3, color=GOLD, stroke_width=4)
        a2 = CurvedArrow(fA[2].get_left() + LEFT * 0.15, fB[2].get_right() + RIGHT * 0.15,
                         angle=-PI / 3, color=GOLD, stroke_width=4)
        l1 = ar("× 2", 26, "BOLD", GOLD).move_to([0.2, 1.9, 0])
        l2 = ar("× 2", 26, "BOLD", GOLD).move_to([0.2, -1.5, 0])
        self.sfx("whoosh")
        self.play(Create(a1), FadeIn(l1), run_time=0.9)
        self.sfx("whoosh")
        self.play(Create(a2), FadeIn(l2), run_time=0.9)
        self.sfx("pop")
        self.play(FadeIn(fB, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.play(Flash(fB, color=GREEN, flash_radius=1.4), run_time=0.8)
        self.wait(max(d - 3.5, 0.2))
        self.clear_all()

        d = self.seg("simp1")
        head2 = titled("والتبسيط: أقسم على نفس العدد", 32, LILA)
        self.sfx("pop")
        self.play(FadeIn(head2, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        g1 = frac(6, 9, 56).move_to([2.6, -0.1, 0])
        g2 = frac(2, 3, 56, LILA).move_to([-2.2, -0.1, 0])
        fl = ar("÷ 3", 28, "BOLD", LILA).move_to([0.2, 1.3, 0])
        arr = CurvedArrow(g1.get_top() + UP * 0.1, g2.get_top() + UP * 0.1,
                          angle=PI / 3.5, color=LILA, stroke_width=4)
        self.sfx("pop")
        self.play(FadeIn(g1, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        self.sfx("whoosh")
        self.play(Create(arr), FadeIn(fl), run_time=0.9)
        self.sfx("ding")
        self.play(FadeIn(g2, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 2.6, 0.2))
        self.clear_all()

    # ── 4. الجمع : نفس المقام ───────────────────────────────────
    def s_add(self):
        d = self.seg("add1")
        head = titled("نفس المقام: أجمع البسطين فقط", 32, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        box = RoundedRectangle(corner_radius=0.25, width=9.4, height=1.25,
                               fill_color=BLUE, fill_opacity=0.92,
                               stroke_color=INK, stroke_width=2).move_to([0, 1.2, 0])
        boxt = ar("البسط + البسط، والمقام يبقى كما هو", 28, "BOLD", "#FFFFFF").move_to(box)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(box, boxt), rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 1.9, 0.2))

        d = self.seg("add2")
        eq = VGroup(frac(2, 5, 46), num("+", 42, GREEN), frac(1, 5, 46),
                    num("=", 42), frac(3, 5, 46, GREEN)).arrange(LEFT, buff=0.35)
        eq.move_to([0, -0.4, 0])
        self.sfx("pop")
        self.play(FadeIn(eq, shift=UP * 0.3), run_time=1.1)
        s = strip(5, 0, width=6.4, height=0.85, fill=GREEN).move_to([0, -2.1, 0])
        self.play(Create(s), run_time=0.9)
        s2 = strip(5, 2, width=6.4, height=0.85, fill=BLUE).move_to([0, -2.1, 0])
        self.sfx("whoosh")
        self.play(Transform(s, s2), run_time=0.9)
        s3 = strip(5, 3, width=6.4, height=0.85, fill=GREEN).move_to([0, -2.1, 0])
        self.sfx("ding")
        self.play(Transform(s, s3), run_time=0.9)
        self.play(Flash(s, color=GREEN, flash_radius=3.4), run_time=0.8)
        self.wait(max(d - 4.7, 0.2))
        self.clear_all()

    # ── 5. مقامان مختلفان : أوحّد أولًا ─────────────────────────
    def s_diff(self):
        d = self.seg("diff1")
        head = titled("مقامان مختلفان؟ أوحّدهما أولًا!", 32, REDA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        warn = RoundedRectangle(corner_radius=0.25, width=8.6, height=1.2,
                                fill_color=REDA, fill_opacity=0.92,
                                stroke_color=INK, stroke_width=2).move_to([0, 1.2, 0])
        warnt = ar("لا أجمع مباشرة أبدًا!", 30, "BOLD", "#FFFFFF").move_to(warn)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(warn, warnt), rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 1.9, 0.2))

        d = self.seg("diff2")
        l1 = VGroup(frac(2, 3, 42), num("+", 38, GREEN), frac(3, 4, 42)
                    ).arrange(LEFT, buff=0.3).move_to([2.9, -0.5, 0])
        self.sfx("pop")
        self.play(FadeIn(l1, shift=UP * 0.3), run_time=0.9)
        arr = ar("←", 40, "BOLD", GOLD).move_to([0.6, -0.5, 0])
        l2 = VGroup(frac(8, 12, 42, BLUE), num("+", 38, GREEN), frac(9, 12, 42, BLUE),
                    num("=", 38), frac(17, 12, 42, GREEN)
                    ).arrange(LEFT, buff=0.3).move_to([-3.1, -0.5, 0])
        self.sfx("whoosh")
        self.play(FadeIn(arr, scale=0.6), run_time=0.6)
        self.sfx("pop")
        self.play(FadeIn(l2, shift=LEFT * 0.4), run_time=1.1)
        lab = ar("وحّدت المقامين إلى 12", 26, "BOLD", BLUE).move_to([0, -2.4, 0])
        self.play(FadeIn(lab, shift=UP * 0.3), run_time=0.8)
        self.play(Flash(l2[-1], color=GREEN, flash_radius=1.2), run_time=0.8)
        self.wait(max(d - 3.4, 0.2))
        self.clear_all()

    # ── 6. كسر من عدد : خُمسا 200 ───────────────────────────────
    def s_fract(self):
        d = self.seg("fract1")
        head = titled("كسر من عدد: أضرب ثم أقسم", 34, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        c1 = RoundedRectangle(corner_radius=0.22, width=7.2, height=1.15, fill_color=GOLD,
                              fill_opacity=0.92, stroke_color=INK).move_to([0, 0.9, 0])
        c1t = ar("العدد × البسط ÷ المقام", 28, "BOLD", "#FFFFFF").move_to(c1)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 1.9, 0.2))

        d = self.seg("fract2")
        pb = ar("مع المختار 200 أوقية، أعطى صديقه خُمسيها", 28, "BOLD", INK)
        pb.move_to([0, -0.3, 0])
        self.sfx("pop")
        self.play(FadeIn(pb, shift=UP * 0.3), run_time=0.9)
        calc = VGroup(num("200", 42), ar("×", 30, "BOLD", GOLD), num("2", 42),
                      ar("÷", 30, "BOLD", ROSE), num("5", 42),
                      num("=", 38), num("80", 50, GREEN),
                      ar("أوقية", 26, "BOLD", GREEN)).arrange(LEFT, buff=0.28)
        calc.move_to([0, -1.7, 0])
        box = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        self.play(Flash(calc[6], color=GREEN, flash_radius=1.2), run_time=0.8)
        self.wait(max(d - 2.9, 0.2))
        self.clear_all()

    # ── 7. انتبه : لا أجمع المقامين ─────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! لا أجمع المقامين أبدًا", 34, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        ok = VGroup(frac(1, 4, 36), num("+", 32, "#FFFFFF"), frac(2, 4, 36),
                    num("=", 32, "#FFFFFF"), frac(3, 4, 36)).arrange(LEFT, buff=0.22)
        c1 = RoundedRectangle(corner_radius=0.22, width=6.2, height=1.7, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.5 + UP * 0.7)
        for m in ok:
            m.set_color("#FFFFFF")
        ok.move_to(c1)
        bad = VGroup(frac(3, 8, 36), ar("خطأ!", 26, "BOLD", "#FFFFFF")
                     ).arrange(LEFT, buff=0.5)
        c2 = RoundedRectangle(corner_radius=0.22, width=6.2, height=1.7, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.5 + DOWN * 1.35)
        for m in bad:
            m.set_color("#FFFFFF")
        bad.move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, ok), rate_func=BOUNCE), run_time=0.9)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(c2, bad), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 8. السر : نفس الكعكة بقطع أصغر ──────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ صغير: نفس الكعكة بقطع أصغر!", 32, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.6)
        p1 = pie(2, 1, radius=1.05, fill=YELL).move_to([2.7, -0.3, 0])
        self.sfx("pop")
        self.play(GrowFromCenter(p1, rate_func=BOUNCE), run_time=0.9)
        self.wait(1.4)
        p2 = pie(8, 4, radius=1.05, fill=YELL).move_to([-2.4, -0.3, 0])
        arr = ar("←", 38, "BOLD", GOLD).move_to([0.15, -0.3, 0])
        self.sfx("whoosh")
        self.play(FadeIn(arr, scale=0.6), GrowFromCenter(p2, rate_func=BOUNCE),
                  run_time=1.1)
        lab = ar("نفس الكمية تمامًا!", 30, "BOLD", GREEN).move_to([0.15, -2.3, 0])
        self.sfx("ding")
        self.play(FadeIn(lab, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - 4.9, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أتعرّف الكسور المتكافئة وأبسّط الكسر",
            "أجمع الكسور وأطرحها بمقام موحّد",
            "آخذ كسرًا من عدد في مسائل الشراء",
        ])
        self.s_equiv()
        self.s_regle()
        self.s_add()
        self.s_diff()
        self.s_fract()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
