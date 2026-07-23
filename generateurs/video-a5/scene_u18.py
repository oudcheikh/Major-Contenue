# -*- coding: utf-8 -*-
"""Vidéo U18 — الضرب في 10 و100 و1000.  Rendu : venv/bin/manim -qh scene_u18.py VideoU18
Cœur de la vidéo : la فاصلة SAUTE à l'écran — pour ×10 un bond vers la droite,
pour ×100 deux bonds, pour ×1000 trois ; pour l'entier, les أصفار volent et
s'accrochent à droite ; et l'exemple du مصنع d'انواكشوط : 2,225 × 1000 = 2225 م."""
import numpy as np
from manim import (VGroup, Line, Arc, Rectangle, RoundedRectangle,
                   SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
                   GrowFromCenter, Indicate, Wiggle, Flash, LaggedStart,
                   UP, DOWN, LEFT, RIGHT, PI)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


class VideoU18(MajorScene):
    AUDIO = HERE / "audio_u18"
    UNIT_AR = "الوحدة 18"
    UNIT_COLOR = LILA
    TITLE = "الضرب في 10 و100 و1000"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 18"

    # ── 2. العدد الصحيح : أضيف الأصفار ──────────────────────────
    def s_entier(self):
        d = self.seg("ent1")
        head = titled("عدد صحيح: أضيف الأصفار!", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        rows = [("× 10", "صفر واحد", GREEN), ("× 100", "صفران", BLUE),
                ("× 1000", "ثلاثة أصفار", ROSE)]
        t = 0
        for i, (op, txt, col) in enumerate(rows):
            c = RoundedRectangle(corner_radius=0.22, width=6.6, height=1.0,
                                 fill_color=col, fill_opacity=0.92,
                                 stroke_color=INK).move_to([0, 1.0 - 1.2 * i, 0])
            cv = num(op, 30, "#FFFFFF").move_to(c.get_center() + RIGHT * 2.0)
            ct = ar(txt, 26, "BOLD", "#FFFFFF").move_to(c.get_center() + LEFT * 1.2)
            self.sfx("pop")
            self.play(GrowFromCenter(VGroup(c, cv, ct), rate_func=BOUNCE), run_time=0.85)
            t += 0.85
        self.wait(max(d - 0.9 - t, 0.2))
        self.clear_all()

        d = self.seg("ent2")
        head2 = titled("مثال: 45 × 10 و 307 × 100", 34, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head2, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # 45 × 10 : le 0 vole et s'accroche
        l1 = VGroup(num("45", 46), num("×", 38, GOLD), num("10", 46),
                    num("=", 40)).arrange(LEFT, buff=0.3).move_to([2.1, 0.7, 0])
        self.sfx("pop")
        self.play(FadeIn(l1, shift=UP * 0.3), run_time=0.9)
        r45 = num("45", 46, GREEN).move_to([-1.6, 0.7, 0])
        self.play(FadeIn(r45, scale=0.6), run_time=0.6)
        z = l1[2][1].copy().set_color(GOLD)      # le 0 du 10
        # les chiffres restent LTR : le 0 s'accroche à DROITE du 45 → 450
        z_target = num("0", 46, GOLD).next_to(r45, RIGHT, buff=0.07)
        self.sfx("whoosh")
        self.play(ReplacementTransform(z, z_target), run_time=1.0)
        self.sfx("ding")
        self.play(Flash(VGroup(r45, z_target), color=GREEN, flash_radius=1.4), run_time=0.7)
        # 307 × 100
        l2 = VGroup(num("307", 46), num("×", 38, GOLD), num("100", 46),
                    num("=", 40), num("30700", 50, BLUE)).arrange(LEFT, buff=0.3)
        l2.move_to([0, -1.1, 0])
        self.sfx("pop")
        self.play(FadeIn(l2, shift=UP * 0.3), run_time=1.0)
        self.play(Indicate(VGroup(*l2[4][3:]), color=GOLD, scale_factor=1.4), run_time=0.9)
        self.wait(max(d - 5.4, 0.2))
        self.clear_all()

    # ── 3. العدد العشري : الفاصلة تقفز ──────────────────────────
    def jump_comma(self, mob, jumps, y, label_txt, col):
        """Anime `jumps` bonds de la فاصلة vers la droite sur une copie du nombre."""
        lab = ar(label_txt, 26, "BOLD", col).move_to([mob.get_center()[0], y - 1.15, 0])
        self.play(FadeIn(lab, shift=UP * 0.2), run_time=0.6)
        return lab

    def s_decimal(self):
        d = self.seg("dec1")
        head = titled("الفاصلة تحب القفز نحو اليمين!", 32, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # 2,4 × 10 : un bond
        src = num("2,4", 60).move_to([2.6, 0.9, 0])
        op = VGroup(num("×", 40, GOLD), num("10", 48)).arrange(LEFT, buff=0.25)
        op.next_to(src, LEFT, buff=0.5)
        self.sfx("pop")
        self.play(FadeIn(src, scale=0.5, rate_func=BOUNCE), FadeIn(op), run_time=0.9)
        virg = src[1]
        hop = Arc(radius=0.42, start_angle=PI, angle=-PI, color=GOLD, stroke_width=4,
                  arc_center=virg.get_center() + RIGHT * 0.42 + UP * 0.15)
        self.sfx("boing")
        self.play(Create(hop), run_time=0.8)
        res = num("24", 60, GREEN).move_to([-1.9, 0.9, 0])
        eq = num("=", 46).move_to([-0.4, 0.9, 0])
        self.sfx("ding")
        self.play(FadeIn(eq), FadeIn(res, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        lab = ar("قفزة واحدة", 26, "BOLD", GOLD).move_to([0.4, -0.4, 0])
        self.play(FadeIn(lab, shift=UP * 0.2), run_time=0.7)
        self.wait(max(d - 3.3, 0.2))

        d = self.seg("dec2")
        r = ar("الأصفار = القفزات: 10 قفزة · 100 قفزتان · 1000 ثلاث", 26, "BOLD", LILA)
        r.move_to([0, -1.6, 0])
        box = SurroundingRectangle(r, color=LILA, corner_radius=0.15, buff=0.2)
        self.sfx("ding")
        self.play(FadeIn(r), Create(box), run_time=1.0)
        self.wait(max(d - 1.0, 0.2))
        self.clear_all()

        # dec3 : 2,4 × 100 = 240 (deux bonds + zéro ajouté)
        d = self.seg("dec3")
        head2 = titled("مثال: 2,4 × 100", 38, ROSE)
        self.sfx("pop")
        self.play(FadeIn(head2, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        src = num("2,4", 62).move_to([2.4, 0.4, 0])
        self.sfx("pop")
        self.play(FadeIn(src, scale=0.5, rate_func=BOUNCE), run_time=0.8)
        c = src[1].get_center()
        hop1 = Arc(radius=0.4, start_angle=PI, angle=-PI, color=GOLD, stroke_width=4,
                   arc_center=c + RIGHT * 0.4 + UP * 0.15)
        hop2 = Arc(radius=0.4, start_angle=PI, angle=-PI, color=GOLD, stroke_width=4,
                   arc_center=c + RIGHT * 1.2 + UP * 0.15)
        self.sfx("boing")
        self.play(Create(hop1), run_time=0.7)
        self.sfx("boing")
        self.play(Create(hop2), run_time=0.7)
        res = num("240", 62, GREEN).move_to([-1.9, 0.4, 0])
        res[2].set_color(GOLD)
        eq = num("=", 48).move_to([0.0, 0.4, 0])
        self.sfx("ding")
        self.play(FadeIn(eq), FadeIn(res, scale=0.5, rate_func=BOUNCE), run_time=0.9)
        note = ar("نقص رقم؟ أضيف صفرًا!", 26, "BOLD", GOLD).move_to([-1.6, -0.9, 0])
        self.play(FadeIn(note, shift=UP * 0.3), run_time=0.8)
        self.wait(max(d - 4.7, 0.2))

        # dec4 : 1,25 × 1000 = 1250
        d = self.seg("dec4")
        l3 = VGroup(num("1,25", 50), num("×", 38, GOLD), num("1000", 50),
                    num("=", 42), num("1250", 56, BLUE)).arrange(LEFT, buff=0.3)
        l3.move_to([0, -2.2, 0])
        l3[4][3].set_color(GOLD)
        self.sfx("pop")
        self.play(FadeIn(l3, shift=UP * 0.3), run_time=1.0)
        self.play(Flash(l3[4], color=BLUE, flash_radius=1.6), run_time=0.8)
        self.wait(max(d - 1.8, 0.2))
        self.clear_all()

    # ── 4. مصنع انواكشوط : 2,225 × 1000 ─────────────────────────
    def s_app(self):
        d = self.seg("app1")
        head = titled("مصنع انواكشوط: 1000 فستان", 34, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # فستان stylisé : triangle-jupe + corsage
        robe = VGroup(
            Rectangle(width=0.85, height=0.8, fill_color=ROSE, fill_opacity=0.95,
                      stroke_color=INK, stroke_width=2.5),
            RoundedRectangle(corner_radius=0.12, width=1.9, height=1.5,
                             fill_color=ROSE, fill_opacity=0.95,
                             stroke_color=INK, stroke_width=2.5).shift(DOWN * 1.1))
        robe.move_to([4.3, -0.3, 0])
        rl = VGroup(ar("للفستان الواحد:", 24, "BOLD"), num("2,225", 34, GOLD),
                    num("m", 28, GOLD)).arrange(LEFT, buff=0.25).move_to([0.2, 1.4, 0])
        self.sfx("pop")
        self.play(FadeIn(robe, scale=0.5, rate_func=BOUNCE), FadeIn(rl), run_time=1.0)
        q = ar("كم مترًا للطلبية كلها؟", 28, "BOLD", REDA).move_to([-0.4, 0.3, 0])
        self.play(FadeIn(q, shift=LEFT * 0.4), run_time=0.9)
        self.wait(max(d - 1.9, 0.2))

        d = self.seg("app2")
        calc = VGroup(num("2,225", 44), num("×", 36, GOLD), num("1000", 44),
                      num("=", 40), num("2225", 52, GREEN),
                      num("m", 34, GREEN)).arrange(LEFT, buff=0.3)
        calc.move_to([-0.6, -1.4, 0])
        box = SurroundingRectangle(calc, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(FadeIn(calc, shift=UP * 0.3), Create(box), run_time=1.1)
        lab = ar("ثلاث قفزات للفاصلة!", 26, "BOLD", GOLD).move_to([-0.6, -2.6, 0])
        self.play(FadeIn(lab, shift=UP * 0.2), run_time=0.8)
        self.play(Flash(calc[4], color=GREEN, flash_radius=1.5), run_time=0.8)
        self.wait(max(d - 2.7, 0.2))
        self.clear_all()

    # ── 5. انتبه : نحو اليمين لا اليسار ─────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! نحو اليمين لا اليسار", 34, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = RoundedRectangle(corner_radius=0.22, width=6.8, height=1.1, fill_color=GREEN,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.2 + UP * 0.5)
        c1t = VGroup(num("0,04 × 100 = 4", 32, "#FFFFFF"),
                     ar("صحيح", 24, "BOLD", "#FFFFFF")).arrange(LEFT, buff=0.5).move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.22, width=6.8, height=1.1, fill_color=REDA,
                              fill_opacity=0.92, stroke_color=INK).move_to(RIGHT * 2.2 + DOWN * 0.9)
        c2t = VGroup(num("0,0004", 32, "#FFFFFF"),
                     ar("خطأ!", 24, "BOLD", "#FFFFFF")).arrange(LEFT, buff=0.5).move_to(c2)
        self.sfx("pop")
        self.play(GrowFromCenter(VGroup(c1, c1t), rate_func=BOUNCE), run_time=0.9)
        self.sfx("boing")
        self.play(GrowFromCenter(VGroup(c2, c2t), rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))
        self.clear_all()

    # ── 6. السر : عُدّ الأصفار ثم اقفز ──────────────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: عُدّ الأصفار ثم اقفز!", 32, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.6)
        rows = [("10", "قفزة واحدة", GREEN), ("100", "قفزتان", BLUE),
                ("1000", "ثلاث قفزات", ROSE)]
        t = 0
        for i, (n_, txt, col) in enumerate(rows):
            c = RoundedRectangle(corner_radius=0.22, width=6.8, height=1.05,
                                 fill_color=col, fill_opacity=0.92,
                                 stroke_color=INK).move_to([0, 0.65 - 1.3 * i, 0])
            cv = num("× " + n_, 32, "#FFFFFF").move_to(c.get_center() + RIGHT * 1.9)
            ct = ar(txt, 27, "BOLD", "#FFFFFF").move_to(c.get_center() + LEFT * 1.5)
            self.sfx("pop")
            self.play(GrowFromCenter(VGroup(c, cv, ct), rate_func=BOUNCE), run_time=0.9)
            t += 0.9
        self.wait(max(d - 1.6 - t, 0.2))
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أضرب عددًا صحيحًا بإضافة الأصفار",
            "أنقل الفاصلة نحو اليمين للعدد العشري",
            "أحسب أثمانًا كبيرة دون آلة حاسبة",
        ])
        self.s_entier()
        self.s_decimal()
        self.s_app()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
