"""
major_tools.qr — Génération de QR codes
=========================================

Génère des QR codes PNG encodés en base64 (pour injection HTML inline)
ou sauvegardés en fichiers, avec couleur par matière Major.

Classe principale :
    QRCodeGenerator

Mapping des matières :
    FR (Français)         → #2563eb (bleu royal)
    MA (Mathématiques)    → #fb923c (orange)
    SN (Sciences)         → #059669 (vert)
    AR (Arabe)            → #7c3aed (violet)
    HG (Histoire-Géo)     → #b45309 (brun)
    IS (Islamique)        → #059669 (vert)
    CV (Civique)          → #1d4ed8 (bleu foncé)
"""

import base64
import io
from pathlib import Path

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_H
except ImportError:
    raise ImportError("Installez qrcode : pip install qrcode[pil]")


# ── Palette Major par préfixe de code ────────────────────────────────────────

COLOR_BY_PREFIX: dict[str, str] = {
    "FR": "#2563eb",
    "MA": "#fb923c",
    "SN": "#059669",
    "AR": "#7c3aed",
    "HG": "#b45309",
    "IS": "#059669",
    "CV": "#1d4ed8",
}

# ── Mapping leçons (concours 6AF) ─────────────────────────────────────────────

BASE_URL = "https://major-eval.vercel.app"

LESSONS: list[tuple[str, str, str]] = [
    # (code, url_deep_link, label_fr)
    ("FR-01", f"{BASE_URL}/#/correction/fr-conjugaison-present", "Conjugaison — Présent"),
    ("FR-02", f"{BASE_URL}/#/correction/fr-conjugaison-passe",  "Conjugaison — Passé"),
    ("FR-03", f"{BASE_URL}/#/correction/fr-types-phrases",      "Types de phrases"),
    ("FR-04", f"{BASE_URL}/#/correction/fr-grammaire-fonctions","Fonctions grammaticales"),
    ("FR-05", f"{BASE_URL}/#/correction/fr-accord-gn",          "Accord du GN"),
    ("MA-01", f"{BASE_URL}/#/correction/math-fractions-base",   "Fractions — Addition"),
    ("MA-02", f"{BASE_URL}/#/correction/math-pourcentages",     "Pourcentages"),
    ("MA-03", f"{BASE_URL}/#/correction/math-proportionnalite", "Proportionnalité"),
    ("MA-04", f"{BASE_URL}/#/correction/math-perimetre-aire",   "Périmètre & Aire"),
    ("MA-05", f"{BASE_URL}/#/correction/math-decimaux",         "Nombres Décimaux"),
    ("SN-01", f"{BASE_URL}/#/correction/sci-digestion",         "Nutrition & Digestion"),
    ("SN-02", f"{BASE_URL}/#/correction/sci-circulation",       "Circulation Sanguine"),
    ("SN-03", f"{BASE_URL}/#/correction/sci-plantes",           "Les Plantes"),
    ("SN-04", f"{BASE_URL}/#/correction/sci-ecosystemes",       "Écosystèmes"),
    ("AR-01", f"{BASE_URL}/#/correction/ar-grammaire-base",     "الفاعل والمفعول به"),
    ("AR-02", f"{BASE_URL}/#/correction/arabe",                 "الأفعال — الماضي والمضارع"),
    ("AR-03", f"{BASE_URL}/#/correction/arabe",                 "الجمع — سالم وتكسير"),
    ("AR-04", f"{BASE_URL}/#/correction/arabe",                 "الإعراب — الحالات الثلاث"),
    ("AR-05", f"{BASE_URL}/#/correction/arabe",                 "النعت والضمائر"),
    ("HG-01", f"{BASE_URL}/#/correction/histoire_geo",          "موريتانيا — الجغرافيا"),
    ("HG-02", f"{BASE_URL}/#/correction/histoire_geo",          "القارة الأفريقية"),
    ("HG-03", f"{BASE_URL}/#/correction/histoire_geo",          "قارات العالم"),
    ("HG-04", f"{BASE_URL}/#/correction/histoire_geo",          "الإمبراطوريات الأفريقية"),
    ("IS-01", f"{BASE_URL}/#/correction/islamique",             "أركان الإسلام الخمسة"),
    ("IS-02", f"{BASE_URL}/#/correction/islamique",             "أركان الإيمان الستة"),
    ("IS-03", f"{BASE_URL}/#/correction/islamique",             "الصلاة — أحكام وأوقات"),
    ("IS-04", f"{BASE_URL}/#/correction/islamique",             "الأخلاق الإسلامية"),
]


class QRCodeGenerator:
    """
    Génère des QR codes PNG pour les leçons et exercices du cahier Major.

    Les QR codes pointent vers la webapp Vercel (major-eval.vercel.app)
    qui permet à l'élève de scanner et corriger son exercice avec l'IA.

    Paramètres :
        base_url   (str)  : URL de base de la webapp (défaut : Vercel prod).
        box_size   (int)  : Taille de chaque module du QR (défaut : 6).
        border     (int)  : Marge en modules autour du QR (défaut : 2).
        output_dir (str)  : Dossier de sauvegarde des PNG (défaut : ./qrcodes).

    Exemples :
        gen = QRCodeGenerator()

        # QR en base64 inline (pour injection HTML)
        b64 = gen.make_b64("https://major-eval.vercel.app/#/correction/arabe", code="AR-01")

        # Balise HTML complète prête à injecter
        html = gen.make_img_tag("AR-01")

        # Générer tous les QR codes et les sauvegarder en PNG
        gen.export_all(output_dir="exports/qrcodes")
    """

    def __init__(
        self,
        base_url: str = BASE_URL,
        box_size: int = 6,
        border: int = 2,
        output_dir: str = "qrcodes",
    ):
        self.base_url   = base_url
        self.box_size   = box_size
        self.border     = border
        self.output_dir = Path(output_dir)
        self._cache: dict[tuple, str] = {}  # (url, color) → base64

    # ── Utilitaires internes ──────────────────────────────────────────

    def _color_for(self, code: str | None) -> str:
        """Retourne la couleur Major pour un code de leçon (ex: 'AR-01' → '#7c3aed')."""
        if not code:
            return "#111827"
        prefix = code.split("-", 1)[0].upper()
        return COLOR_BY_PREFIX.get(prefix, "#111827")

    # ── Génération base64 ─────────────────────────────────────────────

    def make_b64(self, url: str, code: str | None = None) -> str:
        """
        Génère un QR code PNG et retourne son contenu encodé en base64.

        Paramètres :
            url  (str)       : URL encodée dans le QR.
            code (str | None): Code de leçon (ex: 'MA-02') pour la couleur.

        Retourne :
            str : Chaîne base64 du PNG (sans préfixe data:image).
        """
        color = self._color_for(code)
        cache_key = (url, color)

        if cache_key in self._cache:
            return self._cache[cache_key]

        qr = qrcode.QRCode(
            version=None,
            error_correction=ERROR_CORRECT_H,
            box_size=self.box_size,
            border=self.border,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color=color, back_color="white")

        buf = io.BytesIO()
        img.save(buf, format="PNG")
        b64 = base64.b64encode(buf.getvalue()).decode("ascii")

        self._cache[cache_key] = b64
        return b64

    # ── Génération HTML inline ────────────────────────────────────────

    def make_img_tag(
        self,
        code: str,
        url: str | None = None,
        label: str = "",
        size_px: int = 86,
    ) -> str:
        """
        Génère une balise HTML <div class="real-qr"> avec l'image QR inline.

        Paramètres :
            code    (str)       : Code de leçon (ex: 'FR-03').
            url     (str | None): URL à encoder. Si None, utilise le mapping LESSONS.
            label   (str)       : Texte affiché sous le QR.
            size_px (int)       : Taille de l'image en pixels (défaut : 86).

        Retourne :
            str : Fragment HTML prêt à injecter dans le cahier.
        """
        if url is None:
            url = self._url_for_code(code)
        b64 = self.make_b64(url, code)
        color = self._color_for(code)

        return (
            f'<div class="real-qr" style="text-align:center;direction:rtl">'
            f'<img src="data:image/png;base64,{b64}" '
            f'style="width:{size_px}px;height:{size_px}px;border-radius:12px;'
            f'margin:8px auto 5px;display:block;border:2px solid {color}55" '
            f'alt="QR {code}"/>'
            f'<div style="font-size:7.5px;font-weight:900;color:{color};letter-spacing:.8px">{code}</div>'
            f'<div style="font-size:7px;color:#374151;font-weight:700;margin-top:2px">{label}</div>'
            f'</div>'
        )

    # ── Export fichiers PNG ───────────────────────────────────────────

    def export_all(self, output_dir: str | None = None) -> list[Path]:
        """
        Génère et sauvegarde tous les QR codes de LESSONS en fichiers PNG.

        Paramètres :
            output_dir (str | None) : Dossier de sortie (défaut : self.output_dir).

        Retourne :
            list[Path] : Liste des fichiers PNG créés.
        """
        out = Path(output_dir) if output_dir else self.output_dir
        out.mkdir(parents=True, exist_ok=True)

        created = []
        for code, url, label in LESSONS:
            b64 = self.make_b64(url, code)
            png_bytes = base64.b64decode(b64)
            path = out / f"{code}.png"
            path.write_bytes(png_bytes)
            created.append(path)
            print(f"  ✅ {code} → {url}")

        print(f"\n[QRCodeGenerator] {len(created)} QR codes exportés dans {out}/")
        return created

    # ── Helpers privés ────────────────────────────────────────────────

    def _url_for_code(self, code: str) -> str:
        """Résout l'URL d'une leçon depuis le code (ex: 'MA-02')."""
        for c, url, _ in LESSONS:
            if c.upper() == code.upper():
                return url
        # Fallback par préfixe
        prefix = code.split("-", 1)[0].upper()
        routes = {
            "FR": "/#/correction/french",
            "MA": "/#/correction/math",
            "SN": "/#/correction/science",
            "AR": "/#/correction/arabe",
            "HG": "/#/correction/histoire_geo",
            "IS": "/#/correction/islamique",
            "CV": "/#/correction/arabe",
        }
        return self.base_url + routes.get(prefix, "/#/correction/french")
