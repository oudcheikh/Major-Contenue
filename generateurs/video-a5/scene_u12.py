# -*- coding: utf-8 -*-
"""Vidéo U12 — قسمة الكسور.  Rendu : venv/bin/manim -qh scene_u12.py VideoU12
Cœur de la vidéo : le مقلوب se FAIT à l'écran — le بسط et le مقام échangent leurs
places en croisant leurs trajectoires, puis 1/2 ÷ 3/4 : le ÷ devient ×, le second
kasr se retourne, et on vérifie au شريط : كم ثلثًا في وحدتين؟ ستة!"""
from manim import (VGroup, Line, SurroundingRectangle, RoundedRectangle,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled, frac, strip,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


class VideoU12(MajorScene):
    AUDIO = HERE / "audio_u12"
    UNIT_AR = "الوحدة 12"
    UNIT_COLOR = ROSE
    TITLE = "قسمة الكسور"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 12"

    # ── 2. المقلوب : تبديل البسط والمقام ────────────────────────
    def s_maqloub(self):
        d = self.seg("maq1")
        head = titled("مقلوب الكسر: أبدّل البسط والمقام", 34, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        f = frac(2, 3, 64).move_to([2.6, -0.2, 0])
        lab_b = ar("البسط", 26, "BOLD", GREEN).next_to(f[0], RIGHT, buff=0.6)
        lab_m = ar("المقام", 26, "BOLD", BLUE).next_to(f[2], RIGHT, buff=0.6)
        f[0].set_color(GREEN)
        f[2].set_color(BLUE)
        self.sfx("pop")
        self.play(FadeIn(f, scale=0.5, rate_func=BOUNCE),
                  FadeIn(lab_b), FadeIn(lab_m), run_time=1.0)
        self.wait(max(d - 1.9, 0.2))

        # maq2 : le 2 et le 3 échangent leurs places en croisant
        d = self.seg("maq2")
        arrow = ar("←", 46, "BOLD", GOLD).move_to([0.2, -0.2, 0])
        g = frac(3, 2, 64).move_to([-2.4, -0.2, 0])
        g[0].set_color(BLUE)
        g[2].set_color(GREEN)
        self.play(FadeIn(arrow, scale=0.6), Create(g[1]), run_time=0.8)
        c_top = f[0].copy()
        c_bot = f[2].copy()
        self.sfx("whoosh")
        self.play(c_top.animate.move_to(g[2].get_center()),
                  c_bot.animate.move_to(g[0].get_center()),
                  run_time=1.4, rate_func=BOUNCE)
        self.remove(c_top, c_bot)
        self.add(g[0], g[2])
        lab = ar("المقلوب", 30, "BOLD", GOLD).next_to(g, DOWN, buff=0.4)
        self.sfx("ding")
        self.play(FadeIn(lab, shift=UP * 0.3), Flash(g, color=GOLD, flash_radius=1.4),
                  run_time=1.0)
        self.wait(max(d - 3.2, 0.2))
        self.clear_all()

    # ── 3. القاعدة الذهبية + الخطوات الثلاث ─────────────────────
    def s_regle(self):
        d = self.seg("rule1")
        head = titled("القاعدة: أضرب في مقلوب الثاني", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        box = RoundedRectangle(corner_radius=0.25, width=9.6, height=1.3,
                               fill_color=GREEN, fill_opacity=0.92,
                               stroke_color=INK, stroke_width=2).shift(UP * 0.9)
        boxt = ar("القسمة على كسر = الضرب في مقلوبه", 32, "BOLD", "#FFFFFF").move_to(box)
        self.sfx("ding")
        self.play(GrowFromCenter(VGroup(box, boxt), rate_func=BOUNCE), run_time=1.0)
        self.wait(max(d - 1.9, 0.2))

        d = self.seg("steps1")
        steps = ["أُبقي الكسر الأول كما هو",
                 "أستبدل ÷ بعلامة ×",
                 "أقلب الكسر الثاني"]
        cols = [YELL, BLUE, ROSE]
        t = 0
        for i, (txt, col) in enumerate(zip(steps, cols)):
            c = RoundedRectangle(corner_radius=0.22, width=6.4, height=1.05,
                                 fill_color=col, fill_opacity=0.92,
                                 stroke_color=INK).move_to(RIGHT * 2.4 + DOWN * (0.35 + 1.25 * i))
            n = num(str(i + 1), 34, "#FFFFFF").move_to(c.get_right() + LEFT * 0.55)
            ct = ar(txt, 27, "BOLD", "#FFFFFF").move_to(c.get_center() + LEFT * 0.35)
            self.sfx("pop")
            self.play(GrowFromCenter(VGroup(c, n, ct), rate_func=BOUNCE), run_time=0.9)
            t += 0.9
        self.wait(max(d - t, 0.2))
        self.clear_all()

    # ── 4. المثال المحوري : 1/2 ÷ 3/4 = 2/3 ─────────────────────
    def s_exemple(self):
        d = self.seg("ex1")
        head = titled("مثال: النصف ÷ ثلاثة أرباع", 36, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        f1 = frac(1, 2, 56).move_to([3.6, 1.0, 0])      # الأول على اليمين (RTL)
        sgn = num("÷", 54, REDA).move_to([2.4, 1.0, 0])
        f2 = frac(3, 4, 56).move_to([1.2, 1.0, 0])
        self.sfx("pop")
        self.play(FadeIn(f1, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        self.sfx("pop")
        self.play(FadeIn(sgn, scale=0.5), FadeIn(f2, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 2.6, 0.2))

        # ex2 : ÷ devient × et 3/4 se retourne en 4/3
        d = self.seg("ex2")
        self.play(Indicate(f1, color=YELL, scale_factor=1.25), run_time=0.9)
        self.wait(1.2)
        sgn2 = num("×", 54, GOLD).move_to(sgn)
        self.sfx("boing")
        self.play(ReplacementTransform(sgn, sgn2), run_time=0.8)
        self.wait(0.8)
        c_top, c_bot = f2[0].copy().set_color(ROSE), f2[2].copy().set_color(ROSE)
        self.sfx("whoosh")
        self.play(c_top.animate.move_to(f2[2].get_center()),
                  c_bot.animate.move_to(f2[0].get_center()),
                  run_time=1.3, rate_func=BOUNCE)
        self.remove(f2[0], f2[2])
        lab = ar("انقلب!", 26, "BOLD", ROSE).next_to(f2, DOWN, buff=0.35)
        self.sfx("ding")
        self.play(FadeIn(lab, shift=UP * 0.2), run_time=0.7)
        self.wait(max(d - 5.0, 0.2))
        f2v = VGroup(c_top, f2[1], c_bot)

        # ex3 : بسط×بسط ، مقام×مقام → 4/6
        d = self.seg("ex3")
        eqs = num("=", 52).move_to([0.0, 1.0, 0])
        rf = frac(4, 6, 56).move_to([-1.4, 1.0, 0])
        rf[0].set_color(GREEN)
        rf[2].set_color(BLUE)
        self.play(FadeIn(eqs), Create(rf[1]), FadeOut(lab), run_time=0.8)
        self.play(Indicate(f1[0], color=GREEN, scale_factor=1.4),
                  Indicate(c_top, color=GREEN, scale_factor=1.4), run_time=1.0)
        a1, a2 = f1[0].copy().set_color(GREEN), c_top.copy().set_color(GREEN)
        self.sfx("pop")
        self.play(ReplacementTransform(VGroup(a1, a2), rf[0]), run_time=1.0)
        self.play(Indicate(f1[2], color=BLUE, scale_factor=1.4),
                  Indicate(c_bot, color=BLUE, scale_factor=1.4), run_time=1.0)
        b1, b2 = f1[2].copy().set_color(BLUE), c_bot.copy().set_color(BLUE)
        self.sfx("pop")
        self.play(ReplacementTransform(VGroup(b1, b2), rf[2]), run_time=1.0)
        self.wait(max(d - 4.8, 0.2))

        # ex4 : تبسيط 4/6 → 2/3 مؤطر
        d = self.seg("ex4")
        e2 = num("=", 52).move_to([-3.0, 1.0, 0])
        fd = frac(2, 3, 56, GREEN).move_to([-4.3, 1.0, 0])
        self.sfx("ding")
        self.play(FadeIn(e2), ReplacementTransform(rf.copy(), fd), run_time=1.0)
        frame = SurroundingRectangle(fd, color=GREEN, corner_radius=0.15, buff=0.25)
        lab2 = ar("الثلثان", 30, "BOLD", GREEN).next_to(frame, DOWN, buff=0.3)
        self.play(Create(frame), FadeIn(lab2), run_time=0.9)
        self.play(Flash(fd, color=GREEN, flash_radius=1.6), run_time=0.8)
        self.wait(max(d - 2.7, 0.2))
        self.clear_all()

    # ── 5. المعنى بالرسم : كم ثلثًا في وحدتين؟ ──────────────────
    def s_sens(self):
        d = self.seg("sens1")
        head = titled("كم ثلثًا في وحدتين؟", 36, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        s1 = strip(1, 1, width=3.0, height=0.95, fill=YELL).move_to([1.9, 0.8, 0])
        s2 = strip(1, 1, width=3.0, height=0.95, fill=YELL).move_to([-1.5, 0.8, 0])
        l1 = ar("وحدة", 26, "BOLD").next_to(s1, UP, buff=0.25)
        l2 = ar("وحدة", 26, "BOLD").next_to(s2, UP, buff=0.25)
        self.sfx("pop")
        self.play(FadeIn(VGroup(s1, l1), scale=0.7, rate_func=BOUNCE), run_time=0.8)
        self.sfx("pop")
        self.play(FadeIn(VGroup(s2, l2), scale=0.7, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 2.5, 0.2))

        # sens2 : chaque unité coupée en 3, on compte 1..6
        d = self.seg("sens2")
        t1 = strip(3, 3, width=3.0, height=0.95, fill=BLUE).move_to([1.9, 0.8, 0])
        t2 = strip(3, 3, width=3.0, height=0.95, fill=BLUE).move_to([-1.5, 0.8, 0])
        self.sfx("whoosh")
        self.play(Transform(s1, t1), Transform(s2, t2), run_time=1.1)
        nums = VGroup()
        cells = list(t1) + list(t2)          # de droite à gauche : 1 → 6
        for i, cell in enumerate(cells):
            n = num(str(i + 1), 34, "#FFFFFF").move_to(cell.get_center())
            nums.add(n)
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(n, scale=0.4, rate_func=BOUNCE) for n in nums],
                              lag_ratio=0.18), run_time=1.8)
        res = VGroup(num("2", 46), ar("÷", 34, "BOLD"), frac(1, 3, 40),
                     num("=", 44), num("2", 46), ar("×", 34, "BOLD", GOLD),
                     num("3", 46), num("=", 44), num("6", 54, GREEN)
                     ).arrange(LEFT, buff=0.3).move_to([0.2, -1.5, 0])
        box = SurroundingRectangle(res, color=GREEN, corner_radius=0.15, buff=0.25)
        self.sfx("ding")
        self.play(FadeIn(res, shift=UP * 0.3), Create(box), run_time=1.2)
        self.play(Flash(res[-1], color=GREEN, flash_radius=1.2), run_time=0.8)
        self.wait(max(d - 4.9, 0.2))
        self.clear_all()

    # ── 6. انتبه : أقلب الثاني فقط ──────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! أقلب الكسر الثاني فقط", 36, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=6.2, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.5 + UP * 0.5)
        c1t = ar("الكسر الثاني: أقلبه", 28, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=6.2, height=1.1, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.5 + DOWN * 0.9)
        c2t = ar("الكسر الأول: يبقى كما هو!", 28, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 7. السر : القسمة على النصف = الضرب في 2 ─────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: ÷ النصف = × 2", 36, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.6)
        q = ar("كم نصفًا في 3 وحدات؟", 32, "BOLD", BLUE).move_to([0.2, 1.3, 0])
        self.sfx("pop")
        self.play(FadeIn(q, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        strips = VGroup()
        for i in range(3):
            s = strip(1, 1, width=2.5, height=0.8, fill=YELL).move_to([2.9 - 2.85 * i, 0.1, 0])
            strips.add(s)
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(s, scale=0.7, rate_func=BOUNCE) for s in strips],
                              lag_ratio=0.25), run_time=1.5)
        self.wait(1.6)
        halves = VGroup()
        for i in range(3):
            h = strip(2, 2, width=2.5, height=0.8, fill=LILA).move_to([2.9 - 2.85 * i, 0.1, 0])
            halves.add(h)
        self.sfx("whoosh")
        self.play(*[Transform(strips[i], halves[i]) for i in range(3)], run_time=1.1)
        nums = VGroup()
        for i, h in enumerate(halves):
            for j, cell in enumerate(h):
                n = num(str(i * 2 + j + 1), 30, "#FFFFFF").move_to(cell.get_center())
                nums.add(n)
        self.play(LaggedStart(*[FadeIn(n, scale=0.4) for n in nums], lag_ratio=0.12),
                  run_time=1.4)
        res = VGroup(num("3", 44), ar("×", 32, "BOLD", GOLD), num("2", 44),
                     num("=", 42), num("6", 52, GREEN),
                     ar("أنصاف", 30, "BOLD", GREEN)).arrange(LEFT, buff=0.3)
        res.move_to([0.2, -1.7, 0])
        self.sfx("ding")
        self.play(FadeIn(res, shift=UP * 0.3), run_time=1.0)
        self.play(Flash(res[4], color=GREEN, flash_radius=1.2), run_time=0.8)
        self.wait(max(d - 9.9, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أجد مقلوب كسر بتبديل البسط والمقام",
            "أقسم كسرًا على كسر بالضرب في المقلوب",
            "أفهم معنى القسمة على كسر بالرسم",
        ])
        self.s_maqloub()
        self.s_regle()
        self.s_exemple()
        self.s_sens()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
