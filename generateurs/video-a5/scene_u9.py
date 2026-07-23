# -*- coding: utf-8 -*-
"""Vidéo U9 — الكتل.  Rendu : venv/bin/manim -qh scene_u9.py VideoU9
Cœur de la vidéo : une balance à deux plateaux DESSINÉE (1 kg = 1 000 g),
le tableau de conversion kg|hg|dag|g où le chiffre vole dans sa case,
et le نموذج الشريط du cahier (4 × 250 g = 1 kg)."""
from manim import (VGroup, Line, Polygon, Rectangle, RoundedRectangle,
                   SurroundingRectangle, Circle, Cross,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter,
                   Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT)

from video_common import (MajorScene, ar, num, titled, strip,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


class VideoU9(MajorScene):
    AUDIO = HERE / "audio_u9"
    UNIT_AR = "الوحدة 9"
    UNIT_COLOR = YELL
    TITLE = "الكتل"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 9"

    # ── balance à deux plateaux (Line/Polygon) ──────────────────
    def make_balance(self):
        beam = Line([-2.2, -0.3, 0], [2.2, -0.3, 0], color=INK, stroke_width=8)
        pivot = Polygon([0, -0.3, 0], [-0.45, -1.9, 0], [0.45, -1.9, 0],
                        fill_color=GOLD, fill_opacity=1, stroke_color=INK, stroke_width=3)
        base = Line([-1.1, -1.9, 0], [1.1, -1.9, 0], color=INK, stroke_width=8)
        h_l = Line([-2.2, -0.3, 0], [-2.2, -0.95, 0], color=INK, stroke_width=4)
        h_r = Line([2.2, -0.3, 0], [2.2, -0.95, 0], color=INK, stroke_width=4)
        pan_l = Polygon([-2.85, -0.95, 0], [-1.55, -0.95, 0], [-1.8, -1.35, 0],
                        [-2.6, -1.35, 0], fill_color="#FFFFFF", fill_opacity=0.95,
                        stroke_color=INK, stroke_width=3)
        pan_r = Polygon([1.55, -0.95, 0], [2.85, -0.95, 0], [2.6, -1.35, 0],
                        [1.8, -1.35, 0], fill_color="#FFFFFF", fill_opacity=0.95,
                        stroke_color=INK, stroke_width=3)
        return VGroup(pivot, base, beam, h_l, h_r, pan_l, pan_r)

    # ── 2. الكتلة والميزان ──────────────────────────────────────
    def s_balance(self):
        d = self.seg("def1")
        head = titled("الكتلة والميزان", 42, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        sub = ar("الكتلة تخبرنا كم يزن الجسم", 32).move_to(UP * 1.7)
        self.play(FadeIn(sub, shift=LEFT * 0.4), run_time=0.9)
        self.wait(max(d - 1.8, 0.2))

        d = self.seg("def2")
        bal = self.make_balance()
        self.sfx("whoosh")
        self.play(Create(bal), run_time=1.4)
        w_l = RoundedRectangle(corner_radius=0.12, width=1.15, height=0.6,
                               fill_color=ROSE, fill_opacity=0.95,
                               stroke_color=INK).move_to([-2.2, -0.62, 0])
        w_lt = num("1 kg", 26, "#FFFFFF").move_to(w_l)
        self.sfx("pop")
        self.play(FadeIn(VGroup(w_l, w_lt), shift=DOWN * 0.5, rate_func=BOUNCE),
                  run_time=0.8)
        w_r = RoundedRectangle(corner_radius=0.12, width=1.5, height=0.6,
                               fill_color=BLUE, fill_opacity=0.95,
                               stroke_color=INK).move_to([2.2, -0.62, 0])
        w_rt = num("1 000 g", 24, "#FFFFFF").move_to(w_r)
        self.sfx("pop")
        self.play(FadeIn(VGroup(w_r, w_rt), shift=DOWN * 0.5, rate_func=BOUNCE),
                  run_time=0.8)
        eq = num("1 kg = 1 000 g", 48, GREEN).move_to(UP * 0.85)
        self.sfx("ding")
        self.play(Write(eq), run_time=1.0)
        lab = ar("الميزان متوازن!", 28, "BOLD", GREEN).move_to(UP * 1.7)
        self.play(FadeOut(sub), FadeIn(lab, scale=0.5, rate_func=BOUNCE), run_time=0.7)
        self.wait(max(d - 4.7, 0.2))
        self.clear_all()

    # ── 3. الوحدات الثلاث g / kg / t ────────────────────────────
    def s_units(self):
        d = self.seg("unit1")
        head = titled("وحدات الكتلة", 44, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        t = 0.9
        cards = {}
        for sym, lab_t, col, x in [("g", "الغرام", GREEN, 3.9),
                                   ("kg", "الكيلوغرام", BLUE, 0.0),
                                   ("t", "الطن", ROSE, -3.9)]:
            box = RoundedRectangle(corner_radius=0.22, width=2.6, height=1.4,
                                   fill_color=col, fill_opacity=0.92,
                                   stroke_color=INK).move_to([x, 0.7, 0])
            s = num(sym, 54, "#FFFFFF").move_to(box)
            lab = ar(lab_t, 28, "BOLD", col).next_to(box, DOWN, buff=0.3)
            cards[sym] = VGroup(box, s, lab)
            self.sfx("pop")
            self.play(GrowFromCenter(cards[sym], rate_func=BOUNCE), run_time=0.8)
            t += 0.8
        self.wait(max(d - t, 0.2))

        d = self.seg("unit2")   # à quoi sert chaque unité
        tags = {"g": ar("خفيف: ملعقة سكر", 24, color="#666666"),
                "kg": ar("الوحدة الرئيسية", 24, "BOLD", GOLD),
                "t": ar("ثقيل: شاحنة", 24, color="#666666")}
        t = 0
        for sym in ("g", "kg", "t"):
            tags[sym].next_to(cards[sym], DOWN, buff=0.95)
            self.play(Indicate(cards[sym], color=GOLD, scale_factor=1.12), run_time=0.8)
            self.sfx("pop")
            self.play(FadeIn(tags[sym], shift=UP * 0.2), run_time=0.5)
            t += 1.3
        self.wait(max(d - t, 0.2))
        self.clear_all()

    # ── 4. العلاقات الذهبية ─────────────────────────────────────
    def s_relations(self):
        d = self.seg("rel1")
        head = titled("احفظ معي", 44, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        r1 = num("1 kg = 1 000 g", 46).move_to(UP * 0.9)
        r2 = num("1 t = 1 000 kg", 46).move_to(DOWN * 0.1)
        r3 = VGroup(num("= 100 kg", 46), ar("القنطار", 34, "BOLD")).arrange(RIGHT, buff=0.4)
        r3.move_to(DOWN * 1.1)
        t = 0.9
        for r in (r1, r2, r3):
            self.sfx("pop")
            self.play(FadeIn(r, shift=LEFT * 0.5, rate_func=BOUNCE), run_time=0.8)
            t += 0.8
        self.wait(max(d - t, 0.2))
        self.clear_all()

    # ── 5. جدول التحويل : 3 kg → 3 000 g ────────────────────────
    def s_conversion(self):
        d = self.seg("conv1")
        head = titled("جدول التحويل", 42, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        xs = {"kg": -1.8, "hg": -0.6, "dag": 0.6, "g": 1.8}
        cells, heads = {}, {}
        for u, x in xs.items():
            cells[u] = Rectangle(width=1.2, height=1.2, stroke_color=INK, stroke_width=3,
                                 fill_color="#FFFFFF", fill_opacity=0.95).move_to([x, 0, 0])
            heads[u] = num(u, 30, BLUE if u in ("kg", "g") else "#999999")
            heads[u].next_to(cells[u], UP, buff=0.2)
        self.play(LaggedStart(*[Create(cells[u]) for u in xs], lag_ratio=0.15),
                  run_time=1.2)
        self.play(FadeIn(VGroup(*heads.values())), run_time=0.7)
        self.src = num("3 kg", 54, GREEN).move_to(UP * 1.9 + LEFT * 4.3)
        self.sfx("pop")
        self.play(FadeIn(self.src, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 3.6, 0.2))
        self.cells = cells

        d = self.seg("conv2")   # le 3 vole dans sa case, les zéros suivent
        three = num("3", 56, GREEN).move_to(self.src)
        self.sfx("whoosh")
        self.play(three.animate.move_to(cells["kg"]), run_time=1.0)
        t = 1.0
        for u in ("hg", "dag", "g"):
            z = num("0", 56, INK).move_to(cells[u])
            self.sfx("pop")
            self.play(FadeIn(z, shift=UP * 0.3, rate_func=BOUNCE), run_time=0.6)
            t += 0.6
        self.wait(max(d - t, 0.2))

        d = self.seg("conv3")
        hint = ar("ثلاث درجات ← أضرب في ألف", 28, "BOLD", GOLD).move_to(DOWN * 1.3)
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.8)
        result = num("3 kg = 3 000 g", 52, GREEN).move_to(DOWN * 2.3)
        self.sfx("ding")
        self.play(Write(result), run_time=1.1)
        self.play(Flash(result, color=GREEN, flash_radius=2.6), run_time=0.8)
        self.wait(max(d - 2.7, 0.2))
        self.clear_all()

    # ── 6. مسألة الشريط : 4 خبزات × 250 g ──────────────────────
    def s_probleme(self):
        d = self.seg("prob1")
        head = titled("مسألة: أربع خبزات", 40, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        st = VGroup(num("250 g", 40), ar("كتلة كل خبزة:", 30)).arrange(RIGHT, buff=0.4)
        st.move_to(UP * 1.5)
        self.play(FadeIn(st, shift=LEFT * 0.4), run_time=0.8)
        breads = VGroup(*[Circle(radius=0.45, fill_color=YELL, fill_opacity=0.95,
                                 stroke_color=INK, stroke_width=3).move_to([x, 0.2, 0])
                          for x in (2.7, 0.9, -0.9, -2.7)])
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(b, scale=0.3, rate_func=BOUNCE) for b in breads],
                              lag_ratio=0.2), run_time=1.2)
        self.wait(max(d - 2.9, 0.2))

        d = self.seg("prob2")   # نموذج الشريط
        bar = strip(4, 4, width=6, height=0.8, fill=YELL).move_to(DOWN * 0.8)
        labs = VGroup(*[num("250", 26).move_to([x, -0.8, 0])
                        for x in (2.25, 0.75, -0.75, -2.25)])
        self.sfx("whoosh")
        self.play(FadeOut(breads), FadeIn(bar), FadeIn(labs), run_time=1.0)
        frame = SurroundingRectangle(bar, color=GREEN, corner_radius=0.15, buff=0.18)
        self.play(Create(frame), run_time=0.7)
        total = num("4 × 250 = 1 000 g = 1 kg", 44, GREEN).move_to(DOWN * 2.1)
        self.sfx("ding")
        self.play(Write(total), run_time=1.2)
        self.play(Flash(total, color=GREEN, flash_radius=3.0), run_time=0.8)
        self.wait(max(d - 3.7, 0.2))
        self.clear_all()

    # ── 7. انتبه : وحّد الوحدة قبل الجمع ────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! وحّد الوحدة قبل الجمع", 34, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        wrong = num("850 g + 1,25 kg", 46).move_to([1.2, 0.9, 0])
        self.play(FadeIn(wrong, shift=UP * 0.3), run_time=0.8)
        cross = Cross(wrong, stroke_color=REDA, stroke_width=5)
        self.sfx("boing")
        self.play(Create(cross), run_time=0.7)
        conv = num("1,25 kg = 1 250 g", 40, BLUE).move_to([1.2, -0.3, 0])
        self.sfx("whoosh")
        self.play(Write(conv), run_time=0.9)
        ok = num("850 + 1 250 = 2 100 g", 42, GREEN).move_to([1.2, -1.5, 0])
        self.sfx("ding")
        self.play(Write(ok), run_time=1.0)
        self.play(Wiggle(garcon), run_time=1.0)
        self.wait(max(d - 5.4, 0.2))
        self.clear_all()

    # ── 8. السر : الطن = 10 قناطير ──────────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: الطن عشرة قناطير!", 38, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        bar = strip(10, 10, width=9, height=0.85, fill=YELL).move_to(UP * 0.3)
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(c, scale=0.4) for c in bar], lag_ratio=0.08),
                  run_time=1.2)
        cap = VGroup(num("= 100 kg", 30), ar("كل حصة: قنطار واحد", 26, "BOLD", GOLD))
        cap.arrange(RIGHT, buff=0.35).next_to(bar, UP, buff=0.3)
        self.play(FadeIn(cap, shift=DOWN * 0.2), run_time=0.7)
        eq = num("1 t = 10 × 100 kg = 1 000 kg", 44, GREEN).move_to(DOWN * 1.4)
        self.sfx("ding")
        self.play(Write(eq), run_time=1.2)
        self.play(Flash(eq, color=GREEN, flash_radius=3.2), run_time=0.8)
        self.wait(max(d - 4.9, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أميّز وحدات الكتلة: الغرام والكيلوغرام والطن والقنطار",
            "أحوّل الكتل من وحدة إلى أخرى",
            "أحسب الكتلة الكلية والمتبقية في مسائل",
        ])
        self.s_balance()
        self.s_units()
        self.s_relations()
        self.s_conversion()
        self.s_probleme()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
