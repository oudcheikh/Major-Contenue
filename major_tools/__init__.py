"""
major_tools — Boîte à outils du projet Major 6AF
=================================================

Module Python regroupant tous les scripts de génération et manipulation
des cahiers scolaires Major (PDF, QR codes, mise en page, contenu).

Classes disponibles :
    CahierConverter  — Conversion HTML → PDF via Chrome headless
    QRCodeGenerator  — Génération de QR codes (PNG base64 ou fichiers)
    QRInjector       — Injection de QR codes dans les fichiers HTML
    LayoutFixer      — Correction de mise en page, pagination, débordements
    ContentBuilder   — Ajout de pages d'exercices et de pages concours blanc

Utilisation rapide :
    from major_tools import CahierConverter, QRInjector

    CahierConverter().convert("cahier.html")
    QRInjector().inject_all_html()
"""

from .pdf import CahierConverter
from .qr import QRCodeGenerator
from .injector import QRInjector
from .layout import LayoutFixer
from .content import ContentBuilder

__all__ = [
    "CahierConverter",
    "QRCodeGenerator",
    "QRInjector",
    "LayoutFixer",
    "ContentBuilder",
]

__version__ = "1.0.0"
__author__  = "Major 6AF — Mauritanie 🇲🇷"
