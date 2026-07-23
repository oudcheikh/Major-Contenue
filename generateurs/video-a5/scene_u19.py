# -*- coding: utf-8 -*-
"""Vidéo U19 — التقاسيم غير المتساوية.  Rendu : venv/bin/manim -qh scene_u19.py VideoU19
Cœur de la vidéo : le نموذج الشريط raconte les trois حالات — la قطعة du الفرق se
DÉTACHE du شريط (سيدي وموسى 550), les 4 حصص égales du عقد والخاتم s'alignent,
et les 5 حصص du كسر (عبد الله ومختار 2500) se remplissent une à une."""
from manim import (VGroup, Rectangle, RoundedRectangle, Line, Brace,
                   SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled, frac,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


def part(w, color, label=None, value=None):
    """Une حصة du نموذج الشريط."""
    r = Rectangle(width=w, height=0.9, fill_color=color, fill_opacity=0.92,
                  stroke_color=INK, stroke_width=2.5)
    g = VGroup(r)
    if value is not None:
        g.add(num(str(value), 30, "#FFFFFF").move_to(r))
    if label:
        g.add(ar(label, 22, "BOLD", color).next_to(r, UP, buff=0.18))
    return g


class VideoU19(MajorScene):
    AUDIO = HERE / "audio_u19"
    UNIT_AR = "الوحدة 19"
    UNIT_COLOR = ROSE
    TITLE = "التقاسيم غير المتساوية"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 19"

    # ── 2. الحالة 1 : الفرق (سيدي وموسى 550) ────────────────────
    def s_cas1(self):
        d = self.seg("cas1")
        head = titled("الحالة 1: بينهما فرق معلوم", 34, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        donnees = VGroup(
            VGroup(ar("معًا:", 28, "BOLD"), num("550", 38, GOLD),
                   ar("أوقية", 26, "BOLD")).arrange(LEFT, buff=0.25),
            VGroup(ar("لسيدي زيادة:", 28, "BOLD", ROSE), num("210", 38, ROSE)
                   ).arrange(LEFT, buff=0.25),
        ).arrange(DOWN, buff=0.4).move_to([0, 1.2, 0])
        self.sfx("pop")
        self.play(FadeIn(donnees, shift=DOWN * 0.3), run_time=1.1)
        self.wait(max(d - 2.0, 0.2))

        d = self.seg("cas1b")
        # نموذج الشريط : موسى | مثلها لسيدي | الفرق (RTL depuis la droite)
        p_moussa = part(2.0, BLUE, "موسى").move_to([3.3, -0.7, 0])
        p_sidi = part(2.0, BLUE, "مثلها لسيدي").move_to([1.25, -0.7, 0])
        p_diff = part(2.4, ROSE, "الفرق 210").move_to([-1.0, -0.7, 0])
        br = Brace(VGroup(p_moussa[0], p_diff[0]), DOWN, color=GOLD)
        brt = VGroup(ar("معًا", 24, "BOLD", GOLD), num("550", 32, GOLD)
                     ).arrange(LEFT, buff=0.25).next_to(br, DOWN, buff=0.2)
        self.sfx("pop")
        self.play(LaggedStart(FadeIn(p_moussa, shift=LEFT * 0.4, rate_func=BOUNCE),
                              FadeIn(p_sidi, shift=LEFT * 0.4, rate_func=BOUNCE),
                              FadeIn(p_diff, shift=LEFT * 0.4, rate_func=BOUNCE),
                              lag_ratio=0.3), run_time=1.7)
        self.play(GrowFromCenter(br), FadeIn(brt), run_time=0.9)
        self.wait(max(d - 2.6, 0.2))

        d = self.seg("cas1c")
        # le الفرق se détache
        self.sfx("whoosh")
        self.play(p_diff.animate.shift(DOWN * 1.9 + LEFT * 1.6), run_time=1.1)
        c1 = VGroup(num("550", 36), num("−", 32, REDA), num("210", 36),
                    num("=", 32), num("340", 44, GREEN)).arrange(LEFT, buff=0.25)
        c1.move_to([-4.0, 1.2, 0])
        self.sfx("pop")
        self.play(FadeIn(c1, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - 2.0, 0.2))

        d = self.seg("cas1d")
        c2 = VGroup(num("340", 36), ar("÷", 26, "BOLD"), num("2", 36),
                    num("=", 32), num("170", 44, BLUE)).arrange(LEFT, buff=0.25)
        c2.move_to([-4.0, 0.2, 0])
        self.sfx("pop")
        self.play(FadeIn(c2, shift=UP * 0.3), run_time=0.9)
        v1 = num("170", 30, "#FFFFFF").move_to(p_moussa[0])
        v2 = num("170", 30, "#FFFFFF").move_to(p_sidi[0])
        self.sfx("ding")
        self.play(FadeIn(v1, scale=0.4, rate_func=BOUNCE),
                  FadeIn(v2, scale=0.4, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("cas1e")
        c3 = VGroup(num("170", 36), num("+", 32, GREEN), num("210", 36),
                    num("=", 32), num("380", 44, ROSE)).arrange(LEFT, buff=0.25)
        c3.move_to([-4.0, -0.8, 0])
        self.sfx("pop")
        self.play(FadeIn(c3, shift=UP * 0.3), run_time=0.9)
        res = VGroup(ar("سيدي:", 26, "BOLD", ROSE), num("380", 36, ROSE),
                     ar("· موسى:", 26, "BOLD", BLUE), num("170", 36, BLUE)
                     ).arrange(LEFT, buff=0.3).move_to([2.2, -2.6, 0])
        self.sfx("ding")
        self.play(FadeIn(res, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("cas1f")
        ver = VGroup(num("380", 34), num("+", 30, GREEN), num("170", 34),
                     num("=", 30), num("550", 40, GOLD),
                     ar("صحيح!", 26, "BOLD", GREEN)).arrange(LEFT, buff=0.25)
        ver.move_to([-3.4, -2.6, 0])
        box = SurroundingRectangle(ver, color=GREEN, corner_radius=0.15, buff=0.2)
        self.sfx("ding")
        self.play(FadeIn(ver, shift=UP * 0.3), Create(box), run_time=1.0)
        self.play(Flash(ver, color=GREEN, flash_radius=2.4), run_time=0.8)
        self.wait(max(d - 1.8, 0.2))
        self.clear_all()

    # ── 3. الحالة 2 : المضاعف (عقد وخاتم 8800) ──────────────────
    def s_cas2(self):
        d = self.seg("cas2")
        head = titled("الحالة 2: حصة مضاعف للأخرى", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        don = VGroup(ar("عقد وخاتم معًا:", 28, "BOLD"), num("8800", 38, GOLD),
                     ar("· العقد = 3 أضعاف الخاتم", 26, "BOLD", GREEN)
                     ).arrange(LEFT, buff=0.3).move_to([0, 1.3, 0])
        self.sfx("pop")
        self.play(FadeIn(don, shift=DOWN * 0.3), run_time=1.0)
        self.wait(max(d - 1.9, 0.2))

        d = self.seg("cas2b")
        # 1 حصة خاتم + 3 حصص عقد
        parts = VGroup()
        xs = [3.6, 1.6, -0.4, -2.4]
        cols = [BLUE, GREEN, GREEN, GREEN]
        for x, col in zip(xs, cols):
            parts.add(part(1.9, col).move_to([x, -0.4, 0]))
        lab_k = ar("الخاتم", 24, "BOLD", BLUE).next_to(parts[0], UP, buff=0.2)
        lab_a = ar("العقد ×3", 24, "BOLD", GREEN).next_to(parts[2], UP, buff=0.2)
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(p, shift=LEFT * 0.4, rate_func=BOUNCE)
                                for p in parts], lag_ratio=0.25),
                  run_time=1.6)
        self.play(FadeIn(lab_k), FadeIn(lab_a), run_time=0.7)
        c = VGroup(num("3", 34), num("+", 30, GREEN), num("1", 34),
                   num("=", 30), num("4", 42, GOLD),
                   ar("حصص", 26, "BOLD", GOLD)).arrange(LEFT, buff=0.25)
        c.move_to([0, -1.9, 0])
        self.sfx("ding")
        self.play(FadeIn(c, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - 3.2, 0.2))

        d = self.seg("cas2c")
        r1 = VGroup(ar("الخاتم:", 26, "BOLD", BLUE), num("8800", 34),
                    ar("÷", 24, "BOLD"), num("4", 34), num("=", 30),
                    num("2200", 40, BLUE)).arrange(LEFT, buff=0.25).move_to([2.2, -2.9, 0])
        r2 = VGroup(ar("العقد:", 26, "BOLD", GREEN), num("2200", 34),
                    num("×", 28, GOLD), num("3", 34), num("=", 30),
                    num("6600", 40, GREEN)).arrange(LEFT, buff=0.25).move_to([-3.3, -2.9, 0])
        self.sfx("pop")
        self.play(FadeIn(r1, shift=UP * 0.3), run_time=0.9)
        self.sfx("ding")
        self.play(FadeIn(r2, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - 1.8, 0.2))
        self.clear_all()

    # ── 4. الحالة 3 : الكسر (عبد الله ومختار 2500) ──────────────
    def s_cas3(self):
        d = self.seg("cas3")
        head = titled("الحالة 3: حصة كسر من الأخرى", 34, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        don = VGroup(ar("معًا:", 28, "BOLD"), num("2500", 38, GOLD),
                     ar("· أخذ عبد الله", 26, "BOLD"), frac(2, 3, 34, LILA),
                     ar("حصة مختار", 26, "BOLD")).arrange(LEFT, buff=0.3)
        don.move_to([0, 1.3, 0])
        self.sfx("pop")
        self.play(FadeIn(don, shift=DOWN * 0.3), run_time=1.0)
        self.wait(max(d - 1.9, 0.2))

        d = self.seg("cas3b")
        parts = VGroup()
        xs = [4.4, 2.6, 0.8, -1.0, -2.8]
        cols = [ROSE, ROSE, BLUE, BLUE, BLUE]
        for x, col in zip(xs, cols):
            parts.add(part(1.7, col, value=500).move_to([x, -0.5, 0]))
        lab_a = ar("عبد الله", 24, "BOLD", ROSE).next_to(parts[0], UP, buff=0.2).shift(LEFT * 0.9)
        lab_m = ar("مختار", 24, "BOLD", BLUE).next_to(parts[3], UP, buff=0.2)
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(p, shift=LEFT * 0.4, rate_func=BOUNCE)
                                for p in parts], lag_ratio=0.2), run_time=1.7)
        self.play(FadeIn(lab_a), FadeIn(lab_m), run_time=0.7)
        c = VGroup(num("2500", 34), ar("÷", 24, "BOLD"), num("5", 34),
                   num("=", 30), num("500", 42, GOLD)).arrange(LEFT, buff=0.25)
        c.move_to([0, -2.0, 0])
        self.sfx("ding")
        self.play(FadeIn(c, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - 3.3, 0.2))

        d = self.seg("cas3c")
        r = VGroup(ar("عبد الله:", 26, "BOLD", ROSE), num("1000", 38, ROSE),
                   ar("· مختار:", 26, "BOLD", BLUE), num("1500", 38, BLUE)
                   ).arrange(LEFT, buff=0.3).move_to([0, -3.0, 0])
        box = SurroundingRectangle(r, color=GREEN, corner_radius=0.15, buff=0.2)
        self.sfx("ding")
        self.play(FadeIn(r, shift=UP * 0.3), Create(box), run_time=1.0)
        self.play(Flash(r, color=GREEN, flash_radius=2.6), run_time=0.8)
        self.wait(max(d - 1.8, 0.2))
        self.clear_all()

    # ── 5. انتبه : انزع الفرق أولًا ─────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! انزع الفرق أولًا", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=7.2, height=1.1, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.0 + UP * 0.5)
        c1t = ar("لا أقسم على 2 مباشرة إذا كان فرق!", 25, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=7.2, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.0 + DOWN * 0.9)
        c2t = ar("أنزع الفرق ← أقسم ← أعيده للأكبر", 25, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 6. السر : تحقّق بالجمع ──────────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: تحقّق بالجمع دائمًا!", 34, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.8)
        c = RoundedRectangle(corner_radius=0.25, width=10.4, height=1.5, fill_color=LILA,
                             fill_opacity=0.92, stroke_color=INK,
                             stroke_width=2).move_to([0, 0.2, 0])
        ct = ar("مجموع الحصص = المبلغ الكلي ← حسابك صحيح!", 28, "BOLD",
                "#FFFFFF").move_to(c)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(c, ct), rate_func=BOUNCE), run_time=1.1)
        self.play(Flash(VGroup(c, ct), color=LILA, flash_radius=3.0), run_time=0.9)
        self.wait(max(d - 3.8, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أقسم مبلغًا بين شخصين بينهما فرق",
            "أقسم عندما تكون حصة ضعف الأخرى",
            "أقسم عندما تكون حصة كسرًا من الأخرى",
        ])
        self.s_cas1()
        self.s_cas2()
        self.s_cas3()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
