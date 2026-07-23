# -*- coding: utf-8 -*-
"""Test rendu RTL : Text vs MarkupText sur les chaînes qui perdent des glyphes."""
from manim import Scene, Text, MarkupText, VGroup, DOWN, config

config.background_color = "#FFF9EF"
INK = "#3A3A3A"
CASES = ["الوحدة 1", "أُشاهد ← أرسم ← أحسب", "الوحدات", "الآلاف"]


class TestRTL(Scene):
    def construct(self):
        rows = VGroup()
        for s in CASES:
            t1 = Text(s, font="Noto Sans Arabic", font_size=34, weight="BOLD", color=INK)
            t2 = MarkupText(s, font="Noto Sans Arabic", font_size=34, weight="BOLD", color=INK)
            row = VGroup(t1, t2).arrange(DOWN, buff=0.15)
            rows.add(row)
        rows.arrange(DOWN, buff=0.5)
        self.add(rows)
