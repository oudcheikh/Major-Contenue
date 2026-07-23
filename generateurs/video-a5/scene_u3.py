# -*- coding: utf-8 -*-
"""Vidéo U3 — الجمع والطرح.  Rendu : venv/bin/manim -qh scene_u3.py VideoU3
Cœur de la vidéo : opérations posées ANIMÉES chiffre par chiffre —
la retenue (الاحتفاظ) monte en rouge, l'emprunt (الاستلاف) barre et remplace."""
from manim import (VGroup, Line, RoundedRectangle, SurroundingRectangle, Cross,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter,
                   Indicate, Wiggle, Flash,
                   UP, DOWN, LEFT, RIGHT, DR)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)

COLS = [-1.65, -0.55, 0.55, 1.65]      # آلاف، مئات، عشرات، آحاد (gauche → droite)
KHANAT = ["الآلاف", "المئات", "العشرات", "الآحاد"]


class VideoU3(MajorScene):
    AUDIO = HERE / "audio_u3"
    UNIT_AR = "الوحدة 3"
    UNIT_COLOR = GREEN
    TITLE = "الجمع والطرح"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 3"

    # ── aides opération posée ───────────────────────────────────
    def digits_row(self, s, y, size=56, color=INK, x0=0.0):
        g = VGroup()
        for i, ch in enumerate(s):
            d = num(ch, size, color)
            d.move_to([x0 + COLS[i + (4 - len(s))], y, 0])
            g.add(d)
        return g

    def op_layout(self, top, bottom, sign, x0=0.0):
        """Deux nombres alignés + signe + trait, avec les خانات étiquetées au-dessus."""
        labels = VGroup(*[ar(k, 20, "BOLD", "#999999").move_to([x0 + COLS[i], 2.35, 0])
                          for i, k in enumerate(KHANAT)])
        r_top = self.digits_row(top, 1.55, x0=x0)
        r_bot = self.digits_row(bottom, 0.65, x0=x0)
        sgn = num(sign, 56, GOLD).move_to([x0 - 2.65, 0.65, 0])
        bar = Line([x0 - 2.95, 0.05, 0], [x0 + 2.35, 0.05, 0], color=INK, stroke_width=5)
        return labels, r_top, r_bot, sgn, bar

    # ── 2. تعريف : المجموع والفرق ───────────────────────────────
    def s_def(self):
        d = self.seg("def1")
        head = titled("الجمع يعطي المجموع · الطرح يعطي الفرق", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        plus = RoundedRectangle(corner_radius=0.22, width=3.6, height=1.1, fill_color=GREEN,
                                fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.6 + DOWN * 0.4)
        plus_t = ar("+  المجموع", 32, "BOLD", "#FFFFFF").move_to(plus)
        minus = RoundedRectangle(corner_radius=0.22, width=3.6, height=1.1, fill_color=ROSE,
                                 fill_opacity=0.92, stroke_color=INK).move_to(LEFT * 2.6 + DOWN * 0.4)
        minus_t = ar("−  الفرق", 32, "BOLD", "#FFFFFF").move_to(minus)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(plus, plus_t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(minus, minus_t), rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 2.7, 0.2))
        self.clear_all()

    # ── 3. المحاذاة puis الجمع avec الاحتفاظ ────────────────────
    def s_addition(self):
        d = self.seg("meth1")
        head = titled("سرّ النجاح: المحاذاة!", 42, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        labels, r_top, r_bot, sgn, bar = self.op_layout("1238", "5347", "+")
        self.wait(1.6)
        self.play(FadeIn(labels), run_time=0.8)
        self.play(Write(r_top), run_time=1.2)
        self.play(Write(r_bot), FadeIn(sgn), run_time=1.2)
        # petites flèches de correspondance خانة par خانة
        for i in range(3, -1, -1):   # آحاد d'abord (droite)
            self.play(Indicate(VGroup(r_top[i], r_bot[i]), color=BLUE, scale_factor=1.25),
                      run_time=0.6)
        self.wait(max(d - 8.1, 0.2))

        d = self.seg("meth2")
        self.sfx("whoosh")
        self.play(Create(bar), run_time=0.8)
        arrow_hint = ar("أبدأ من الآحاد ←", 26, "BOLD", GOLD).move_to([0.4, -0.6, 0])
        self.play(FadeIn(arrow_hint, shift=LEFT * 0.4), run_time=0.9)
        self.wait(max(d - 1.7, 0.2))
        self.play(FadeOut(arrow_hint), run_time=0.4)

        # add1 : 8+7=15 → 5, retenue 1
        d = self.seg("add1")
        self.play(Indicate(VGroup(r_top[3], r_bot[3]), color=YELL, scale_factor=1.3), run_time=1.0)
        self.wait(2.2)
        res5 = num("5", 56, GREEN).move_to([COLS[3], -0.65, 0])
        self.sfx("pop")
        self.play(FadeIn(res5, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.8)
        carry = num("1", 30, REDA).move_to([COLS[2], 2.0, 0])
        self.sfx("ding")
        self.play(FadeIn(carry, shift=UP * 0.4, rate_func=BOUNCE), run_time=0.8)
        carry_lab = ar("الاحتفاظ", 22, "BOLD", REDA).next_to(carry, LEFT, buff=0.25)
        self.play(FadeIn(carry_lab), run_time=0.6)
        self.wait(max(d - 5.4, 0.2))

        # add2 : 3+4+1=8
        d = self.seg("add2")
        self.play(Indicate(VGroup(r_top[2], r_bot[2], carry), color=YELL, scale_factor=1.3),
                  run_time=1.0)
        res8 = num("8", 56, GREEN).move_to([COLS[2], -0.65, 0])
        self.sfx("pop")
        self.play(FadeIn(res8, shift=UP * 0.3, rate_func=BOUNCE), FadeOut(carry_lab), run_time=0.8)
        self.wait(max(d - 1.8, 0.2))

        # add3 : 2+3=5 puis 1+5=6
        d = self.seg("add3")
        self.play(Indicate(VGroup(r_top[1], r_bot[1]), color=YELL, scale_factor=1.3), run_time=0.9)
        res_5c = num("5", 56, GREEN).move_to([COLS[1], -0.65, 0])
        self.sfx("pop")
        self.play(FadeIn(res_5c, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.7)
        self.wait(1.4)
        self.play(Indicate(VGroup(r_top[0], r_bot[0]), color=YELL, scale_factor=1.3), run_time=0.9)
        res6 = num("6", 56, GREEN).move_to([COLS[0], -0.65, 0])
        self.sfx("pop")
        self.play(FadeIn(res6, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.7)
        self.wait(max(d - 4.6, 0.2))

        # add4 : le مجموع encadré
        d = self.seg("add4")
        result = VGroup(res6, res_5c, res8, res5)
        frame = SurroundingRectangle(result, color=GREEN, corner_radius=0.15, buff=0.22)
        lab = ar("المجموع", 28, "BOLD", GREEN).next_to(frame, RIGHT, buff=0.5)
        self.sfx("ding")
        self.play(Create(frame), FadeIn(lab), run_time=1.0)
        self.play(Flash(result, color=GREEN, flash_radius=2.2), run_time=0.9)
        self.wait(max(d - 1.9, 0.2))
        self.clear_all()

    # ── 4. الطرح avec الاستلاف : 5347 − 1238 ───────────────────
    def s_soustraction(self):
        d = self.seg("sub1")
        head = titled("الطرح مع الاستلاف", 42, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        labels, r_top, r_bot, sgn, bar = self.op_layout("5347", "1238", "−")
        self.play(FadeIn(labels), Write(r_top), run_time=1.4)
        self.play(Write(r_bot), FadeIn(sgn), Create(bar), run_time=1.4)
        self.wait(max(d - 3.7, 0.2))

        # sub2 : 7−8 impossible → استلاف : le 4 devient 3, le 7 devient 17
        d = self.seg("sub2")
        self.play(Indicate(VGroup(r_top[3], r_bot[3]), color=REDA, scale_factor=1.3), run_time=1.0)
        imp = ar("لا يمكن!", 26, "BOLD", REDA).move_to([3.4, 1.1, 0])
        self.sfx("boing")
        self.play(FadeIn(imp, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        self.wait(1.6)
        # l'emprunt : barrer le 4, écrire 3 ; petit 1 devant le 7
        cross4 = Cross(r_top[2], stroke_color=REDA, stroke_width=5)
        small3 = num("3", 30, REDA).move_to([COLS[2], 2.0, 0])
        small1 = num("1", 30, REDA).move_to([COLS[3] - 0.38, 1.85, 0])
        self.sfx("whoosh")
        self.play(Create(cross4), FadeIn(small3, shift=UP * 0.3), run_time=0.9)
        self.sfx("ding")
        self.play(FadeIn(small1, shift=UP * 0.3, rate_func=BOUNCE),
                  FadeOut(imp), run_time=0.8)
        lab_b = ar("الاستلاف", 22, "BOLD", REDA).next_to(small1, RIGHT, buff=0.3).shift(UP * 0.15)
        self.play(FadeIn(lab_b), run_time=0.6)
        res9 = num("9", 56, ROSE).move_to([COLS[3], -0.65, 0])
        self.sfx("pop")
        self.play(FadeIn(res9, shift=UP * 0.3, rate_func=BOUNCE), FadeOut(lab_b), run_time=0.8)
        self.wait(max(d - 6.5, 0.2))

        # sub3 : 3−3=0 · 3−2=1 · 5−1=4
        d = self.seg("sub3")
        outs = [("0", 2), ("1", 1), ("4", 0)]
        t = 0
        for ch, col in outs:
            self.play(Indicate(VGroup(r_top[col], r_bot[col]), color=YELL, scale_factor=1.25),
                      run_time=0.8)
            r = num(ch, 56, ROSE).move_to([COLS[col], -0.65, 0])
            self.sfx("pop")
            self.play(FadeIn(r, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.7)
            self.wait(1.3)
            t += 2.8
            if col == 2:
                self.res0 = r
            elif col == 1:
                self.res1 = r
            else:
                self.res4 = r
        self.wait(max(d - t, 0.2))

        # sub4 : الفرق encadré
        d = self.seg("sub4")
        result = VGroup(self.res4, self.res1, self.res0, res9)
        frame = SurroundingRectangle(result, color=ROSE, corner_radius=0.15, buff=0.22)
        lab = ar("الفرق", 28, "BOLD", ROSE).next_to(frame, RIGHT, buff=0.5)
        self.sfx("ding")
        self.play(Create(frame), FadeIn(lab), run_time=1.0)
        self.play(Flash(result, color=ROSE, flash_radius=2.2), run_time=0.9)
        self.wait(max(d - 1.9, 0.2))
        self.clear_all()

    # ── 5. انتبه ────────────────────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! الاحتفاظ في الجمع · الاستلاف في الطرح", 34, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=4.4, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.9 + UP * 0.5)
        c1t = ar("الجمع ← الاحتفاظ ⬆", 28, "BOLD", "#FFFFFF").move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=4.4, height=1.1, fill_color=ROSE,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.9 + DOWN * 0.9)
        c2t = ar("الطرح ← الاستلاف", 28, "BOLD", "#FFFFFF").move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 6. السر : تحقق الطرح بالجمع ─────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: أتحقق من الطرح بالجمع", 38, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        op = num("542 − 33 = 509", 52).shift(UP * 0.8)
        self.play(Write(op), run_time=1.3)
        self.wait(2.6)
        check = num("509 + 33 = 542", 52, GREEN).shift(DOWN * 0.7)
        arrow = ar("أتحقق ↓", 26, "BOLD", LILA).move_to([4.4, 0.05, 0])
        self.sfx("whoosh")
        self.play(FadeIn(arrow), Write(check), run_time=1.6)
        ok = ar("طرحُنا صحيح!", 32, "BOLD", GREEN).shift(DOWN * 2.1)
        self.sfx("ding")
        self.play(FadeIn(ok, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        self.play(Flash(check, color=GREEN, flash_radius=2.6), run_time=0.9)
        self.wait(max(d - 6.3, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أضع عمليات الجمع والطرح عموديًا وأنجزها",
            "لا أنسى الاحتفاظ والاستلاف",
            "أحلّ مسائل من الحياة اليومية",
        ])
        self.s_def()
        self.s_addition()
        self.s_soustraction()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
