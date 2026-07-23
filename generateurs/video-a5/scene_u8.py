# -*- coding: utf-8 -*-
"""Vidéo U8 — مقارنة الأعداد وترتيبها.  Rendu : venv/bin/manim -qh scene_u8.py VideoU8
Cœur de la vidéo : comparaison خانة par خانة ANIMÉE (les colonnes s'allument de gauche
à droite jusqu'à la première différente, le symbole < surgit en gros), puis les nombres
qui se réordonnent en glissant pour le ترتيب تصاعدي/تنازلي."""
from manim import (VGroup, Line, Arrow, RoundedRectangle, SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter, Transform,
                   Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)

COLS = [-1.65, -0.55, 0.55, 1.65]      # آلاف، مئات، عشرات، آحاد (gauche → droite)
KHANAT = ["الآلاف", "المئات", "العشرات", "الآحاد"]


class VideoU8(MajorScene):
    AUDIO = HERE / "audio_u8"
    UNIT_AR = "الوحدة 8"
    UNIT_COLOR = ROSE
    TITLE = "مقارنة الأعداد"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 8"

    # ── aides ───────────────────────────────────────────────────
    def digits_row(self, s, y, size=56, color=INK, x0=0.0):
        g = VGroup()
        for i, ch in enumerate(s):
            d = num(ch, size, color)
            d.move_to([x0 + COLS[i + (4 - len(s))], y, 0])
            g.add(d)
        return g

    def tight_num(self, s, x, y, size=50, color=INK, gap=0.52):
        """Nombre compact chiffre par chiffre (pour colorier un chiffre isolé)."""
        g = VGroup()
        n = len(s)
        for i, ch in enumerate(s):
            d = num(ch, size, color)
            d.move_to([x + (i - (n - 1) / 2) * gap, y, 0])
            g.add(d)
        return g

    # ── 2. الرموز > < = ─────────────────────────────────────────
    def s_def(self):
        d = self.seg("def1")
        head = titled("أيهما أكبر؟ أيهما أصغر؟", 40, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(max(d - 0.9, 0.2))

        d = self.seg("def2")   # les 3 cartes-symboles, de droite à gauche (RTL)
        t = 0
        for sym, lab_t, col, x in [(">", "أكبر من", GREEN, 3.6),
                                   ("<", "أصغر من", ROSE, 0.0),
                                   ("=", "يساوي", BLUE, -3.6)]:
            box = RoundedRectangle(corner_radius=0.22, width=2.6, height=1.5,
                                   fill_color=col, fill_opacity=0.92,
                                   stroke_color=INK).move_to([x, 0.55, 0])
            s = num(sym, 64, "#FFFFFF").move_to(box)
            lab = ar(lab_t, 28, "BOLD", col).next_to(box, DOWN, buff=0.3)
            self.sfx("pop")
            self.play(GrowFromCenter(VGroup(box, s, lab), rate_func=BOUNCE), run_time=0.8)
            t += 0.8
        hint = ar("الفم المفتوح نحو العدد الأكبر!", 30, "BOLD", GOLD).move_to(DOWN * 2.2)
        self.sfx("ding")
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.9)
        self.wait(max(d - t - 0.9, 0.2))
        self.clear_all()

    # ── 3. القاعدة 1 : أعدّ الخانات (10 200 / 9 900) ────────────
    def s_count(self):
        d = self.seg("meth1")
        head = titled("أعدّ الخانات أولًا", 42, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        rule = ar("خانات أكثر ← عدد أكبر", 32, "BOLD", GREEN).move_to(UP * 1.5)
        self.play(FadeIn(rule, shift=LEFT * 0.4), run_time=0.9)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("meth2")
        n1 = num("10 200", 60).move_to([-2.9, 0.1, 0])
        n2 = num("9 900", 60).move_to([2.9, 0.1, 0])
        self.sfx("pop")
        self.play(Write(n1), run_time=0.8)
        self.sfx("pop")
        self.play(Write(n2), run_time=0.8)
        lab1 = ar("خمس خانات", 26, "BOLD", GREEN).next_to(n1, DOWN, buff=0.45)
        lab2 = ar("أربع خانات", 26, "BOLD", REDA).next_to(n2, DOWN, buff=0.45)
        self.play(Indicate(n1, color=GREEN, scale_factor=1.15), FadeIn(lab1), run_time=0.9)
        self.play(Indicate(n2, color=REDA, scale_factor=1.15), FadeIn(lab2), run_time=0.9)
        gt = num(">", 84, GOLD).move_to([0, 0.1, 0])
        self.sfx("ding")
        self.play(GrowFromCenter(gt, rate_func=BOUNCE), run_time=0.9)
        self.play(Flash(n1, color=GREEN, flash_radius=2.2), run_time=0.8)
        self.wait(max(d - 5.1, 0.2))
        self.clear_all()

    # ── 4. القاعدة 2 : خانة خانة من اليسار (4 325 / 4 352) ─────
    def s_compare(self):
        d = self.seg("comp1")
        head = titled("أقارن خانة خانة من اليسار", 36, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        hint = ar("أبدأ من اليسار", 28, "BOLD", GOLD).move_to(DOWN * 2.5 + LEFT * 3.4)
        self.play(FadeIn(hint, shift=RIGHT * 0.4), run_time=0.8)
        self.wait(max(d - 1.7, 0.2))

        d = self.seg("comp2")   # les deux nombres alignés sous leurs خانات
        labels = VGroup(*[ar(k, 20, "BOLD", "#999999").move_to([COLS[i], 2.0, 0])
                          for i, k in enumerate(KHANAT)])
        r_top = self.digits_row("4325", 1.2)
        r_bot = self.digits_row("4352", 0.3)
        self.play(FadeIn(labels), run_time=0.7)
        self.play(Write(r_top), run_time=1.0)
        self.play(Write(r_bot), run_time=1.0)
        self.wait(max(d - 2.7, 0.2))

        d = self.seg("comp3")   # آلاف puis مئات : égales, on continue
        t = 0
        for col in (0, 1):
            self.play(Indicate(VGroup(r_top[col], r_bot[col]), color=BLUE,
                               scale_factor=1.3), run_time=0.8)
            eq = num("=", 34, GREEN).move_to([COLS[col], 0.75, 0])
            self.sfx("pop")
            self.play(FadeIn(eq, scale=0.4, rate_func=BOUNCE), run_time=0.5)
            t += 1.3
        self.wait(max(d - t, 0.2))

        d = self.seg("comp4")   # عشرات : 2 < 5 → توقف!
        self.play(Indicate(VGroup(r_top[2], r_bot[2]), color=REDA, scale_factor=1.35),
                  run_time=0.9)
        box = SurroundingRectangle(VGroup(r_top[2], r_bot[2]), color=REDA,
                                   corner_radius=0.12, buff=0.18)
        self.play(Create(box), run_time=0.7)
        stop = ar("توقف هنا!", 28, "BOLD", REDA).move_to([3.6, 0.75, 0])
        self.sfx("boing")
        self.play(FadeIn(stop, scale=0.5, rate_func=BOUNCE), run_time=0.7)
        small = num("2 < 5", 40, REDA).move_to([-3.5, 0.75, 0])
        self.sfx("pop")
        self.play(FadeIn(small, shift=UP * 0.3), run_time=0.6)
        self.wait(max(d - 2.9, 0.2))

        d = self.seg("comp5")   # le symbole < surgit en gros
        n1 = num("4 325", 54).move_to([-2.7, -1.7, 0])
        n2 = num("4 352", 54).move_to([2.7, -1.7, 0])
        self.play(FadeIn(n1, shift=UP * 0.3), FadeIn(n2, shift=UP * 0.3), run_time=0.8)
        sym = num("<", 92, GOLD).move_to([0, -1.65, 0])
        self.sfx("ding")
        self.play(GrowFromCenter(sym, rate_func=BOUNCE), run_time=0.9)
        self.play(Flash(sym, color=GOLD, flash_radius=1.6), run_time=0.7)
        self.wait(max(d - 2.4, 0.2))
        self.clear_all()

    # ── 5. الترتيب التصاعدي والتنازلي ───────────────────────────
    def s_ordre(self):
        d = self.seg("ord1")
        head = titled("الترتيب التصاعدي والتنازلي", 36, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        up_lab = ar("تصاعدي: من الأصغر إلى الأكبر", 30, "BOLD", GREEN).move_to(UP * 1.6)
        self.play(FadeIn(up_lab, shift=LEFT * 0.4), run_time=0.9)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("ord2")   # les cartes glissent vers l'ordre croissant
        SLOTS = [-4.2, -1.4, 1.4, 4.2]
        vals = ["1 240", "1 402", "1 042", "1 204"]          # désordre initial
        sorted_x = {"1 042": SLOTS[0], "1 204": SLOTS[1],
                    "1 240": SLOTS[2], "1 402": SLOTS[3]}
        cards = {}
        for v, x in zip(vals, SLOTS):
            box = RoundedRectangle(corner_radius=0.2, width=2.5, height=1.0,
                                   fill_color="#FFFFFF", fill_opacity=0.95,
                                   stroke_color=INK, stroke_width=2.5)
            n = num(v, 40)
            cards[v] = VGroup(box, n.move_to(box)).move_to([x, -0.1, 0])
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(cards[v], scale=0.5, rate_func=BOUNCE)
                                for v in vals], lag_ratio=0.15), run_time=1.2)
        self.sfx("whoosh")
        self.play(*[cards[v].animate.move_to([sorted_x[v], -0.1, 0]) for v in vals],
                  run_time=1.6)
        self.lts = VGroup(*[num("<", 36, GOLD).move_to([x, -0.1, 0])
                            for x in (-2.8, 0.0, 2.8)])
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(s, scale=0.4) for s in self.lts],
                              lag_ratio=0.2), run_time=0.8)
        arr = Arrow([-4.6, -1.4, 0], [4.6, -1.4, 0], color=GREEN, stroke_width=5)
        arr_lab = ar("تصاعدي", 26, "BOLD", GREEN).next_to(arr, DOWN, buff=0.2)
        self.sfx("ding")
        self.play(Create(arr), FadeIn(arr_lab), run_time=0.8)
        self.wait(max(d - 4.4, 0.2))
        self.cards, self.arr, self.arr_lab, self.up_lab = cards, arr, arr_lab, up_lab

        d = self.seg("ord3")   # inversion → ordre décroissant
        down_lab = ar("تنازلي: من الأكبر إلى الأصغر", 30, "BOLD", ROSE).move_to(UP * 1.6)
        self.play(Transform(self.up_lab, down_lab), run_time=0.7)
        desc_x = {"1 402": SLOTS[0], "1 240": SLOTS[1],
                  "1 204": SLOTS[2], "1 042": SLOTS[3]}
        self.sfx("whoosh")
        self.play(*[self.cards[v].animate.move_to([desc_x[v], -0.1, 0])
                    for v in self.cards], run_time=1.5)
        gts = VGroup(*[num(">", 36, GOLD).move_to([x, -0.1, 0])
                       for x in (-2.8, 0.0, 2.8)])
        arr2 = Arrow([-4.6, -1.4, 0], [4.6, -1.4, 0], color=ROSE, stroke_width=5)
        arr2_lab = ar("تنازلي", 26, "BOLD", ROSE).next_to(arr2, DOWN, buff=0.2)
        self.sfx("ding")
        self.play(Transform(self.lts, gts), Transform(self.arr, arr2),
                  Transform(self.arr_lab, arr2_lab), run_time=0.9)
        self.wait(max(d - 3.1, 0.2))
        self.clear_all()

    # ── 6. انتبه : عدد الخانات قبل كل شيء ──────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! تحقّق من عدد الخانات أولًا", 34, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        n2 = num("9 999", 56).move_to([4.3, 0.3, 0])
        lab2 = ar("أربع خانات", 24, "BOLD", REDA).next_to(n2, DOWN, buff=0.35)
        self.sfx("pop")
        self.play(Write(n2), FadeIn(lab2), run_time=0.9)
        n1 = num("10 005", 56).move_to([-0.9, 0.3, 0])
        lab1 = ar("خمس خانات", 24, "BOLD", GREEN).next_to(n1, DOWN, buff=0.35)
        self.sfx("pop")
        self.play(Write(n1), FadeIn(lab1), run_time=0.9)
        sym = num(">", 76, GOLD).move_to([1.75, 0.3, 0])
        self.sfx("ding")
        self.play(GrowFromCenter(sym, rate_func=BOUNCE), run_time=0.8)
        self.play(Flash(n1, color=GREEN, flash_radius=2.0), run_time=0.7)
        self.play(Wiggle(garcon), run_time=1.0)
        self.wait(max(d - 5.3, 0.2))
        self.clear_all()

    # ── 7. السر : أول رقم مختلف يحسم ────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: ابدأ من اليسار!", 40, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        na = self.tight_num("4512", -2.5, 0.2)
        nb = self.tight_num("4521", 2.5, 0.2)
        self.sfx("pop")
        self.play(FadeIn(na, shift=UP * 0.3), FadeIn(nb, shift=UP * 0.3), run_time=0.9)
        for i in (0, 1):   # chiffres égaux : vert doux
            self.play(Indicate(VGroup(na[i], nb[i]), color=GREEN, scale_factor=1.3),
                      run_time=0.6)
        self.sfx("boing")   # premier chiffre différent : il décide !
        self.play(Indicate(VGroup(na[2], nb[2]), color=REDA, scale_factor=1.5),
                  na[2].animate.set_color(REDA), nb[2].animate.set_color(GREEN),
                  run_time=0.8)
        sym = num("<", 72, GOLD).move_to([0, 0.2, 0])
        self.sfx("ding")
        self.play(GrowFromCenter(sym, rate_func=BOUNCE), run_time=0.8)
        morale = ar("أول رقم مختلف يحسم فورًا!", 30, "BOLD", LILA).move_to(DOWN * 1.9)
        self.play(Write(morale), run_time=0.9)
        self.wait(max(d - 5.6, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أقارن عددين بالرموز: أكبر وأصغر ويساوي",
            "أرتّب الأعداد تصاعديًا وتنازليًا",
            "أحلّ مسائل مقارنة من الحياة اليومية",
        ])
        self.s_def()
        self.s_count()
        self.s_compare()
        self.s_ordre()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
