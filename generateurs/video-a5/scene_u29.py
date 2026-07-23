# -*- coding: utf-8 -*-
"""Vidéo U29 — المساحات والقياسات الزراعية.  Rendu : venv/bin/manim -qh scene_u29.py VideoU29
Cœur de la vidéo : le carré de 1 m × 1 m qui se remplit de petits carreaux (4×4 stylisé),
le tableau de conversion à DEUX chiffres par colonne avec chiffres qui volent,
les carrés ha/a/ca côte à côte, et la conversion du cahier 5 ha و28 a = 528 a."""
from manim import (VGroup, Line, DashedLine, Rectangle, RoundedRectangle, Square,
                   SurroundingRectangle,
                   FadeIn, FadeOut, Write, Create, GrowFromCenter, LaggedStart,
                   Indicate, Wiggle, Flash,
                   UP, DOWN, LEFT, RIGHT, UR)

from video_common import (MajorScene, ar, num, titled,
                          INK, YELL, ROSE, GREEN, BLUE, LILA, REDA, GOLD, BOUNCE, HERE)


class VideoU29(MajorScene):
    AUDIO = HERE / "audio_u29"
    UNIT_AR = "الوحدة 29"
    UNIT_COLOR = GREEN
    TITLE = "المساحات والقياسات الزراعية"
    OUTRO_CALL = "والآن افتح كراسك وحلّ تمارين الوحدة 29"

    # ── aides ───────────────────────────────────────────────────
    def card(self, txt, size, fill, pos):
        t = ar(txt, size, "BOLD", "#FFFFFF")
        r = RoundedRectangle(corner_radius=0.22, width=t.width + 0.8, height=t.height + 0.55,
                             fill_color=fill, fill_opacity=0.92, stroke_color=INK, stroke_width=2)
        return VGroup(r, t).move_to(pos)

    def area_table(self, y0=0.35):
        """3 colonnes m² / dm² / cm², chacune coupée en DEUX cases (règle des 2 chiffres)."""
        cols = ["m²", "dm²", "cm²"]        # les chiffres se lisent de gauche à droite
        W, H = 2.3, 1.1
        table = VGroup()
        slots = {}
        for i, u in enumerate(cols):
            x = (i - 1) * W
            headbox = Rectangle(width=W, height=0.7, fill_color=GREEN, fill_opacity=0.9,
                                stroke_color=INK, stroke_width=2).move_to([x, y0 + H / 2 + 0.35, 0])
            htxt = num(u, 30, "#FFFFFF").move_to(headbox)
            body = Rectangle(width=W, height=H, fill_color="#FFFFFF", fill_opacity=0.9,
                             stroke_color=INK, stroke_width=2).move_to([x, y0, 0])
            mid = DashedLine([x, y0 - H / 2, 0], [x, y0 + H / 2, 0],
                             stroke_color="#B9B9B9", stroke_width=2)
            table.add(headbox, htxt, body, mid)
            slots[u] = ([x - W / 4, y0, 0], [x + W / 4, y0, 0])   # (case gauche, case droite)
        return table, slots

    # ── 2. المتر المربع qui se remplit de dm² ──────────────────
    def s_metre_carre(self):
        d = self.seg("def1")
        head = titled("المتر المربع: وحدة قياس المساحات", 36, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        sq = Square(side_length=3.0, stroke_color=INK, stroke_width=4,
                    fill_color="#FFFFFF", fill_opacity=0.9).move_to(RIGHT * 3.2 + DOWN * 0.7)
        lab_top = num("1 m", 32, GOLD).next_to(sq, UP, buff=0.18)
        lab_side = num("1 m", 32, GOLD).next_to(sq, RIGHT, buff=0.22)
        m2 = num("1 m²", 48, GREEN).move_to(sq)
        self.sfx("whoosh")
        self.play(Create(sq), run_time=1.2)
        self.sfx("pop")
        self.play(FadeIn(lab_top), FadeIn(lab_side), run_time=0.7)
        self.sfx("ding")
        self.play(FadeIn(m2, scale=0.4, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 3.6, 0.2))                                        # somme = 3.6

        d = self.seg("def2")   # remplissage 4×4 stylisé (représente 10×10)
        self.play(FadeOut(m2), run_time=0.4)
        cells = VGroup()
        for r in range(4):
            for c in range(4):
                cell = Square(side_length=0.75, stroke_color=BLUE, stroke_width=2,
                              fill_color=BLUE, fill_opacity=0.18)
                cell.move_to(sq.get_corner(UR) + LEFT * (0.375 + 0.75 * c)
                             + DOWN * (0.375 + 0.75 * r))
                cells.add(cell)
        self.sfx("pop")
        self.play(LaggedStart(*[FadeIn(c, scale=0.3) for c in cells], lag_ratio=0.05),
                  run_time=2.2)
        tag = num("1 dm²", 20, INK).move_to(cells[0])
        hundred = num("10 × 10 = 100", 32, BLUE).next_to(sq, DOWN, buff=0.28)
        self.play(FadeIn(tag), FadeIn(hundred, shift=UP * 0.2), run_time=0.8)
        eq = num("1 m² = 100 dm²", 44, GREEN).move_to(LEFT * 3.3 + DOWN * 0.7)
        box = SurroundingRectangle(eq, color=GREEN, corner_radius=0.15, buff=0.25)
        self.sfx("ding")
        self.play(Write(eq), Create(box), run_time=1.3)
        self.wait(max(d - 4.7, 0.2))                                        # somme = 4.7
        self.clear_all()

    # ── 3. المضاعفات والأجزاء ──────────────────────────────────
    def s_multiples(self):
        d = self.seg("def3")
        head = titled("مضاعفات المتر المربع وأجزاؤه", 38, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        units = ["km²", "hm²", "dam²", "m²", "dm²", "cm²", "mm²"]
        chips = VGroup()
        for i, u in enumerate(units):
            b = RoundedRectangle(corner_radius=0.18, width=1.5, height=0.9,
                                 fill_color=GREEN if u == "m²" else "#FFFFFF",
                                 fill_opacity=0.95, stroke_color=INK, stroke_width=2)
            t = num(u, 28, "#FFFFFF" if u == "m²" else INK).move_to(b)
            g = VGroup(b, t).move_to([-4.8 + 1.6 * i, 0.0, 0])
            chips.add(g)
        m_lab = ar("المضاعفات", 28, "BOLD", GOLD).move_to([-3.2, 1.25, 0])
        p_lab = ar("الأجزاء", 28, "BOLD", ROSE).move_to([3.2, 1.25, 0])
        self.sfx("pop")
        self.play(FadeIn(chips[3], scale=0.4, rate_func=BOUNCE), run_time=0.8)
        self.sfx("whoosh")
        self.play(FadeIn(m_lab),
                  LaggedStart(*[FadeIn(chips[i], shift=RIGHT * 0.3) for i in (2, 1, 0)],
                              lag_ratio=0.25), run_time=1.5)
        self.sfx("whoosh")
        self.play(FadeIn(p_lab),
                  LaggedStart(*[FadeIn(chips[i], shift=LEFT * 0.3) for i in (4, 5, 6)],
                              lag_ratio=0.25), run_time=1.5)
        self.wait(max(d - 4.7, 0.2))                                        # somme = 4.7
        self.clear_all()

    # ── 4. الجدول : رقمان لكل وحدة + chiffres qui volent ───────
    def s_table(self):
        d = self.seg("tab1")
        head = titled("جدول التحويل: رقمان لكل وحدة!", 38, GREEN)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        table, slots = self.area_table()
        self.sfx("whoosh")
        self.play(FadeIn(table, shift=UP * 0.3), run_time=1.2)
        two = ar("خانتان في كل عمود!", 30, "BOLD", REDA).move_to(DOWN * 1.5)
        self.sfx("ding")
        self.play(FadeIn(two, shift=UP * 0.2, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 2.9, 0.2))                                        # somme = 2.9
        self.play(FadeOut(two), run_time=0.4)

        d = self.seg("tab2")   # 3 m² = 300 dm² : chiffres qui volent
        q = num("3 m² = ? dm²", 40, GOLD).move_to(UP * 2.15 + LEFT * 4.0)
        self.play(Write(q), run_time=1.0)
        d3 = num("3", 44, BLUE).move_to(q.get_left() + RIGHT * 0.25)
        self.sfx("whoosh")
        self.play(d3.animate.move_to(slots["m²"][1]), run_time=1.0)
        z1 = num("0", 44, REDA).move_to(slots["dm²"][0])
        z2 = num("0", 44, REDA).move_to(slots["dm²"][1])
        self.sfx("pop")
        self.play(FadeIn(z1, shift=DOWN * 0.4, rate_func=BOUNCE),
                  FadeIn(z2, shift=DOWN * 0.4, rate_func=BOUNCE), run_time=0.9)
        res = num("3 m² = 300 dm²", 44, GREEN).move_to(DOWN * 1.8)
        box = SurroundingRectangle(res, color=GREEN, corner_radius=0.15, buff=0.22)
        self.sfx("ding")
        self.play(Write(res), Create(box), run_time=1.2)
        self.play(Flash(res, color=GREEN, flash_radius=2.6), run_time=0.8)
        self.wait(max(d - 5.3, 0.2))                                        # somme = 0.4+4.9
        self.clear_all()

    # ── 5. القياسات الزراعية : ha / a / ca ─────────────────────
    def s_agraire(self):
        d = self.seg("agr1")
        head = titled("القياسات الزراعية: في الحقول!", 38, GOLD)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        # trois carrés, bases alignées, de droite (le plus grand) à gauche
        ha_sq = Square(2.6).set_fill(GREEN, 0.35).set_stroke(INK, 3).move_to([3.9, -0.7, 0])
        a_sq = Square(1.5).set_fill(YELL, 0.55).set_stroke(INK, 3).move_to([0.3, -1.25, 0])
        ca_sq = Square(0.7).set_fill(ROSE, 0.6).set_stroke(INK, 3).move_to([-3.3, -1.65, 0])
        ha_n = ar("الهكتار ha", 28, "BOLD", GREEN).next_to(ha_sq, UP, buff=0.25)
        a_n = ar("الآر a", 28, "BOLD", GOLD).next_to(a_sq, UP, buff=0.25)
        ca_n = ar("السنتيار ca", 28, "BOLD", ROSE).next_to(ca_sq, UP, buff=0.25)
        for g in (VGroup(ha_sq, ha_n), VGroup(a_sq, a_n), VGroup(ca_sq, ca_n)):
            self.sfx("pop")
            self.play(FadeIn(g, scale=0.4, rate_func=BOUNCE), run_time=0.8)
        self.wait(max(d - 3.3, 0.2))                                        # somme = 3.3

        d = self.seg("agr2")   # a = 100 m² · ca = 1 m²
        a_v = num("1 a = 100 m²", 30, INK).next_to(a_sq, DOWN, buff=0.3)
        ca_v = num("1 ca = 1 m²", 30, INK).next_to(ca_sq, DOWN, buff=0.3)
        self.sfx("pop")
        self.play(FadeIn(a_v, shift=UP * 0.2), Indicate(a_sq, color=GOLD), run_time=1.1)
        self.sfx("pop")
        self.play(FadeIn(ca_v, shift=UP * 0.2), Indicate(ca_sq, color=ROSE), run_time=1.1)
        self.wait(max(d - 2.2, 0.2))                                        # somme = 2.2

        d = self.seg("agr3")   # ha = 100 a = 10 000 m²
        ha_v = num("1 ha = 100 a = 10 000 m²", 32, GREEN).next_to(ha_sq, DOWN, buff=0.3)
        ha_v.shift(LEFT * 0.8)
        self.sfx("ding")
        self.play(Indicate(ha_sq, color=GREEN, scale_factor=1.12), run_time=1.0)
        self.play(Write(ha_v), run_time=1.2)
        self.play(Flash(ha_v, color=GREEN, flash_radius=2.6), run_time=0.8)
        self.wait(max(d - 3.0, 0.2))                                        # somme = 3.0
        self.clear_all()

        # ex1 : 5 ha و28 a = 528 a
        d = self.seg("ex1")
        head = titled("أحوّل: 5 ha و28 a إلى الآر", 36, BLUE)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=0.9)
        self.wait(1.6)
        l1 = num("5 ha = 500 a", 44, INK).move_to(UP * 0.9)
        self.sfx("pop")
        self.play(Write(l1), run_time=1.2)
        self.wait(0.8)
        l2 = num("500 a + 28 a = 528 a", 46, GREEN).move_to(DOWN * 0.5)
        box = SurroundingRectangle(l2, color=GREEN, corner_radius=0.15, buff=0.25)
        self.sfx("ding")
        self.play(Write(l2), Create(box), run_time=1.4)
        self.play(Flash(l2, color=GREEN, flash_radius=3.0), run_time=0.9)
        self.wait(max(d - 6.8, 0.2))                                        # somme = 6.8
        self.clear_all()

    # ── 6. انتبه ────────────────────────────────────────────────
    def s_attention(self):
        d = self.seg("att1")
        head = titled("انتبه! رقمان لكل عمود في جدول المساحات", 34, REDA)
        garcon = self.boy(1.9).to_edge(LEFT, buff=0.25).shift(DOWN * 1.3)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE),
                  FadeIn(garcon, shift=RIGHT * 0.8, rate_func=BOUNCE), run_time=1.0)
        c1 = self.card("جدول الأطوال: رقم واحد", 28, BLUE, RIGHT * 2.9 + UP * 0.5)
        c2 = self.card("جدول المساحات: رقمان اثنان!", 28, GREEN, RIGHT * 2.9 + DOWN * 0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(c1, rate_func=BOUNCE), run_time=0.9)
        self.sfx("pop")
        self.play(GrowFromCenter(c2, rate_func=BOUNCE), run_time=0.9)
        self.play(Wiggle(garcon), run_time=1.1)
        self.wait(max(d - 3.9, 0.2))                                        # somme = 3.9
        self.clear_all()

    # ── 7. السر : ha = hm² · a = dam² · ca = m² ────────────────
    def s_astuce(self):
        d = self.seg("astuce")
        head = titled("سرّ ذهبي: أخوات وحدات المساحة", 38, LILA)
        self.sfx("pop")
        self.play(FadeIn(head, shift=DOWN * 0.3, rate_func=BOUNCE), run_time=1.0)
        self.wait(1.4)
        pairs = [("ha = hm²", GREEN, 3.7), ("a = dam²", GOLD, 0.0), ("ca = m²", ROSE, -3.7)]
        for txt, col, x in pairs:      # de droite à gauche
            t = num(txt, 40, col).move_to([x, 0.2, 0])
            b = SurroundingRectangle(t, color=col, corner_radius=0.18, buff=0.3)
            self.sfx("pop")
            self.play(FadeIn(VGroup(t, b), scale=0.5, rate_func=BOUNCE), run_time=0.8)
            self.wait(0.6)
        morale = ar("الجدول نفسه يخدمك!", 32, "BOLD", LILA).move_to(DOWN * 1.9)
        self.sfx("ding")
        self.play(Write(morale), run_time=1.3)
        self.wait(max(d - 7.9, 0.2))                                        # somme = 7.9
        self.clear_all()

    def construct(self):
        self.setup_common()
        self.s_intro_card("intro1")
        self.s_objectifs("intro2", [
            "أحوّل وحدات المساحة: رقمان لكل وحدة",
            "أستعمل الهكتار والآر والسنتيار",
            "أحلّ مسائل عن مساحات الحقول",
        ])
        self.s_metre_carre()
        self.s_multiples()
        self.s_table()
        self.s_agraire()
        self.s_attention()
        self.s_astuce()
        self.s_outro_end("outro")
