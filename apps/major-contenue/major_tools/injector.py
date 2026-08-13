"""
major_tools.injector — Injection de QR codes dans les HTML
============================================================

Lit un fichier HTML de cahier Major, remplace les blocs de QR codes
fictifs (`<div class="fake-qr">`) par de vrais QR codes PNG encodés
en base64, et met à jour les URLs obsolètes (localhost → Vercel).

Classe principale :
    QRInjector

Modes d'injection supportés :
    - fake-qr     : <div class="fake-qr" id="ar-01"></div>
    - real-qr     : Régénère les QR d'un bloc .real-qr existant
    - qr-box      : Blocs de démonstration (.qr-box)
    - bottom-strip: Bandeaux QR en bas de chaque page d'exercices
    - url-update  : Remplace localhost:5173 → major-eval.vercel.app
"""

import re
from pathlib import Path

from .qr import QRCodeGenerator, BASE_URL, COLOR_BY_PREFIX


# ── Mapping fake-qr id → méta ─────────────────────────────────────────────────

FAKE_QR_MAP: dict[str, dict] = {
    "ar-01": {"url": f"{BASE_URL}/#/correction/ar-grammaire-base",  "label": "AR-01", "title": "الفاعل والمفعول",    "color": "#7c3aed"},
    "ar-02": {"url": f"{BASE_URL}/#/correction/arabe",              "label": "AR-02", "title": "الإملاء والخط",      "color": "#7c3aed"},
    "ar-03": {"url": f"{BASE_URL}/#/correction/arabe",              "label": "AR-03", "title": "الأفعال والصرف",     "color": "#7c3aed"},
    "ar-04": {"url": f"{BASE_URL}/#/correction/arabe",              "label": "AR-04", "title": "الجمع والإفراد",     "color": "#7c3aed"},
    "ar-05": {"url": f"{BASE_URL}/#/correction/arabe",              "label": "AR-05", "title": "التعبير الكتابي",    "color": "#7c3aed"},
    "hg-01": {"url": f"{BASE_URL}/#/correction/histoire_geo",       "label": "HG-01", "title": "موريتانيا",          "color": "#b45309"},
    "hg-02": {"url": f"{BASE_URL}/#/correction/histoire_geo",       "label": "HG-02", "title": "القارة الأفريقية",   "color": "#b45309"},
    "hg-03": {"url": f"{BASE_URL}/#/correction/histoire_geo",       "label": "HG-03", "title": "قارات العالم",       "color": "#b45309"},
    "hg-04": {"url": f"{BASE_URL}/#/correction/histoire_geo",       "label": "HG-04", "title": "التاريخ",            "color": "#b45309"},
    "hg-05": {"url": f"{BASE_URL}/#/correction/histoire_geo",       "label": "HG-05", "title": "الجغرافيا",          "color": "#b45309"},
    "hg-06": {"url": f"{BASE_URL}/#/correction/histoire_geo",       "label": "HG-06", "title": "التاريخ الأفريقي",   "color": "#b45309"},
    "is-01": {"url": f"{BASE_URL}/#/correction/islamique",          "label": "IS-01", "title": "أركان الإسلام",      "color": "#059669"},
    "is-02": {"url": f"{BASE_URL}/#/correction/islamique",          "label": "IS-02", "title": "أركان الإيمان",      "color": "#059669"},
    "is-03": {"url": f"{BASE_URL}/#/correction/islamique",          "label": "IS-03", "title": "الصلاة والعبادة",    "color": "#059669"},
    "is-04": {"url": f"{BASE_URL}/#/correction/islamique",          "label": "IS-04", "title": "الأخلاق الإسلامية",  "color": "#059669"},
    "is-05": {"url": f"{BASE_URL}/#/correction/islamique",          "label": "IS-05", "title": "الفقه والعبادات",    "color": "#059669"},
    "cv-01": {"url": f"{BASE_URL}/#/correction/arabe",              "label": "CV-01", "title": "التربية المدنية",    "color": "#1d4ed8"},
    "cv-02": {"url": f"{BASE_URL}/#/correction/arabe",              "label": "CV-02", "title": "حقوق وواجبات",       "color": "#1d4ed8"},
    "cv-03": {"url": f"{BASE_URL}/#/correction/arabe",              "label": "CV-03", "title": "المواطنة",            "color": "#1d4ed8"},
    "cv-04": {"url": f"{BASE_URL}/#/correction/arabe",              "label": "CV-04", "title": "القيم الوطنية",      "color": "#1d4ed8"},
}

# Mapping matière → URL + couleur pour les QR de bas de page
SUBJECT_QR: dict[str, dict] = {
    "ar-ex": {"url": f"{BASE_URL}/#/correction/arabe",        "color": "#7c3aed", "label": "اللغة العربية"},
    "hg-ex": {"url": f"{BASE_URL}/#/correction/histoire_geo", "color": "#b45309", "label": "التاريخ والجغرافيا"},
    "is-ex": {"url": f"{BASE_URL}/#/correction/islamique",    "color": "#059669", "label": "التربية الإسلامية"},
    "cv-ex": {"url": f"{BASE_URL}/#/correction/arabe",        "color": "#1d4ed8", "label": "التربية المدنية"},
    "fr-ex": {"url": f"{BASE_URL}/#/correction/french",       "color": "#2563eb", "label": "Français"},
    "ma-ex": {"url": f"{BASE_URL}/#/correction/math",         "color": "#fb923c", "label": "Mathématiques"},
    "sn-ex": {"url": f"{BASE_URL}/#/correction/science",      "color": "#059669", "label": "Sciences"},
}

# Regex pour détecter les URLs obsolètes (localhost dev)
_OLD_BASE_RE = re.compile(r"https?://(?:localhost|172\.20\.10\.4):5173")


class QRInjector:
    """
    Injecte des QR codes réels dans les fichiers HTML des cahiers Major.

    Remplace les placeholders `fake-qr` par des images PNG encodées
    en base64, régénère les QR codes des blocs `real-qr` existants,
    et met à jour les URLs de développement vers la production Vercel.

    Paramètres :
        root       (str)  : Dossier racine du projet (défaut : parent du module).
        base_url   (str)  : URL Vercel de production.
        qr_gen     (QRCodeGenerator | None) : Instance partagée du générateur.

    Exemples :
        injector = QRInjector(root="c:/Users/PC/Documents/Major-Contenue")

        # Injecter dans un seul fichier
        injector.inject_file("6AF-ARABE/Cahier-Major-LangueArabe-Islamique-6AF.html")

        # Mettre à jour tous les HTML du projet (fake-qr + real-qr + URLs)
        injector.inject_all_html()

        # Ajouter un bandeau QR en bas de chaque page d'exercices
        injector.add_bottom_strips("6AF-ARABE/Cahier-Major-Arabe-6AF.html")
    """

    def __init__(
        self,
        root: str | None = None,
        base_url: str = BASE_URL,
        qr_gen: QRCodeGenerator | None = None,
    ):
        self.root     = Path(root) if root else Path(__file__).resolve().parent.parent
        self.base_url = base_url
        self.qr       = qr_gen or QRCodeGenerator(base_url=base_url)

    # ── API publique ──────────────────────────────────────────────────

    def inject_file(self, html_path: str) -> int:
        """
        Injecte les QR codes dans un fichier HTML (in-place).

        Traite dans l'ordre :
          1. Remplace `<div class="fake-qr" id="..."></div>` par de vrais QR
          2. Met à jour les URLs localhost → Vercel

        Paramètres :
            html_path (str) : Chemin du fichier HTML à modifier.

        Retourne :
            int : Nombre de QR codes injectés.
        """
        path = Path(html_path)
        html = path.read_text(encoding="utf-8")
        html, count = self._replace_fake_qr(html)
        html, _ = self._update_old_urls(html)
        path.write_text(html, encoding="utf-8", newline="")
        print(f"[QRInjector] {path.name} : {count} QR injectés")
        return count

    def inject_all_html(self, skip_backups: bool = True) -> dict:
        """
        Met à jour tous les fichiers HTML du projet.

        Parcourt récursivement `self.root`, ignore node_modules et
        les fichiers backup, et traite :
          - blocs .real-qr (régénération)
          - blocs .qr-box (régénération)
          - URLs obsolètes (localhost → Vercel)

        Paramètres :
            skip_backups (bool) : Ignore les fichiers *backup*.html (défaut True).

        Retourne :
            dict : {"files": int, "real_qr": int, "qr_box": int, "urls": int}
        """
        totals = {"files": 0, "real_qr": 0, "qr_box": 0, "urls": 0}

        for path in sorted(self.root.rglob("*.html")):
            parts = {p.lower() for p in path.parts}
            if "node_modules" in parts:
                continue
            if skip_backups and ("backup" in path.name.lower() or "_bak_" in path.name):
                continue

            html = path.read_text(encoding="utf-8")
            original = html
            html, n_real = self._update_div_blocks(html, "real-qr")
            html, n_box  = self._update_div_blocks(html, "qr-box")
            html, n_urls = self._update_old_urls(html)

            if html != original:
                path.write_text(html, encoding="utf-8", newline="")
                totals["files"] += 1
                totals["real_qr"] += n_real
                totals["qr_box"]  += n_box
                totals["urls"]    += n_urls
                print(f"  ✅ {path.relative_to(self.root)}")

        print(f"\n[QRInjector] {totals['files']} fichiers mis à jour — "
              f"{totals['real_qr']} real-qr · {totals['qr_box']} qr-box · "
              f"{totals['urls']} URLs")
        return totals

    def add_bottom_strips(self, html_path: str) -> int:
        """
        Ajoute un bandeau QR compact en bas de chaque page d'exercices.

        Détecte la matière dominante de chaque page via les classes CSS
        (ar-ex, hg-ex, is-ex, cv-ex, fr-ex, ma-ex, sn-ex) et insère
        un bandeau d'appel à l'action "Scanne pour te corriger".

        Paramètres :
            html_path (str) : Chemin du fichier HTML à modifier (in-place).

        Retourne :
            int : Nombre de bandeaux ajoutés.
        """
        path = Path(html_path)
        html = path.read_text(encoding="utf-8")
        pages = re.split(r'(?=<div class="page")', html)
        count = 0
        result = []
        for page in pages:
            new_page, added = self._add_strip_to_page(page)
            result.append(new_page)
            count += added
        path.write_text("".join(result), encoding="utf-8", newline="")
        print(f"[QRInjector] {path.name} : {count} bandeaux QR ajoutés")
        return count

    # ── Remplacement fake-qr ──────────────────────────────────────────

    def _replace_fake_qr(self, html: str) -> tuple[str, int]:
        """Remplace <div class="fake-qr" id="..."></div> par un vrai QR."""
        count = 0

        def replacer(m: re.Match) -> str:
            nonlocal count
            qr_id = m.group(1).strip().lower()
            meta  = FAKE_QR_MAP.get(qr_id)
            if not meta:
                print(f"  [!] fake-qr id non mappé : {qr_id!r}")
                return m.group(0)
            b64 = self.qr.make_b64(meta["url"], meta["label"])
            count += 1
            return self._real_qr_html(b64, meta["label"], meta["title"], meta["color"], meta["url"])

        html = re.sub(r'<div class="fake-qr"\s+id="([^"]+)"[^>]*></div>', replacer, html)

        # Fallback : fake-qr sans id (remplacement séquentiel depuis LESSONS)
        from .qr import LESSONS
        for code, url, label in LESSONS:
            if '<div class="fake-qr"></div>' not in html:
                break
            color = self.qr._color_for(code)
            b64   = self.qr.make_b64(url, code)
            replacement = self.qr.make_img_tag(code, url, label)
            html = html.replace('<div class="fake-qr"></div>', replacement, 1)
            count += 1

        return html, count

    # ── Mise à jour blocs real-qr / qr-box ───────────────────────────

    def _update_div_blocks(self, html: str, class_name: str) -> tuple[str, int]:
        """Régénère les QR dans tous les blocs <div class="{class_name}">."""
        needle = f'<div class="{class_name}'
        out: list[str] = []
        cursor = 0
        count  = 0
        pos = html.find(needle)

        while pos != -1:
            end   = self._find_div_end(html, pos)
            block = html[pos:end]
            code  = self._extract_code(block)
            url   = self._extract_url(block) or (self.qr._url_for_code(code) if code else None)

            if url and "data:image/png;base64," in block:
                b64       = self.qr.make_b64(url, code)
                new_block = re.sub(
                    r'src="data:image/png;base64,[^"]+"',
                    f'src="data:image/png;base64,{b64}"',
                    block, count=1, flags=re.DOTALL
                )
                new_block = re.sub(
                    r"https?://(?:localhost|172\.20\.10\.4):5173[^<\"'\s]+",
                    url, new_block
                )
                out.append(html[cursor:pos])
                out.append(new_block)
                cursor = end
                count += 1

            pos = html.find(needle, end)

        out.append(html[cursor:])
        return "".join(out), count

    # ── Mise à jour URLs ──────────────────────────────────────────────

    def _update_old_urls(self, html: str) -> tuple[str, int]:
        """Remplace les URLs localhost/dev par l'URL Vercel de production."""
        matches = list(_OLD_BASE_RE.finditer(html))
        html = _OLD_BASE_RE.sub(self.base_url, html)
        html = html.replace(f"{self.base_url}/#correction/", f"{self.base_url}/#/correction/")
        html = html.replace(f"{self.base_url}#correction/",  f"{self.base_url}/#/correction/")
        return html, len(matches)

    # ── Bandeau QR bas de page ────────────────────────────────────────

    def _add_strip_to_page(self, page_html: str) -> tuple[str, int]:
        """Détecte la matière et insère le bandeau QR avant .page-footer."""
        subject_key = None
        for sk in SUBJECT_QR:
            if f'class="exo-card {sk}' in page_html or f'exo-card {sk}"' in page_html:
                subject_key = sk
                break
        if not subject_key:
            return page_html, 0

        meta  = SUBJECT_QR[subject_key]
        b64   = self.qr.make_b64(meta["url"], subject_key.split("-")[0].upper() + "-01")
        color = meta["color"]
        label = meta["label"]

        strip = (
            f'\n      <div style="display:flex;align-items:center;gap:10px;'
            f'margin-top:8px;padding:7px 12px;border-radius:10px;'
            f'background:{color}11;border:1px solid {color}33;direction:rtl">'
            f'<img src="data:image/png;base64,{b64}" '
            f'style="width:72px;height:72px;border-radius:10px;border:2px solid {color}66;flex-shrink:0" '
            f'alt="QR correction"/>'
            f'<div style="flex:1">'
            f'<div style="font-size:9px;font-weight:900;color:{color};font-family:\'Cairo\',sans-serif">'
            f'📷 صوِّر إجابتك واحصل على تصحيح فوري بالذكاء الاصطناعي</div>'
            f'<div style="font-size:7.5px;color:#6b7280;margin-top:3px">{label}</div>'
            f'</div>'
            f'</div>\n'
        )

        new_html = re.sub(
            r'(\n    </div>\n    <div class="page-footer">)',
            strip + r'\1',
            page_html, count=1
        )
        changed = new_html != page_html
        return new_html, 1 if changed else 0

    # ── Helpers HTML ──────────────────────────────────────────────────

    @staticmethod
    def _find_div_end(html: str, div_start: int) -> int:
        """Trouve la position de fermeture d'un <div> imbriqué."""
        depth = 0
        for m in re.finditer(r"<div\b|</div>", html[div_start:], flags=re.IGNORECASE):
            token = m.group(0).lower()
            depth += 1 if token.startswith("<div") else -1
            if depth == 0:
                return div_start + m.end()
        return len(html)

    @staticmethod
    def _extract_code(block: str) -> str | None:
        """Extrait le code de leçon (ex: 'AR-01') d'un bloc HTML."""
        patterns = [
            r'alt="QR\s+([A-Z]{2}-(?:\d{2}|CB))"',
            r'class="qr-code-label"[^>]*>\s*([A-Z]{2}-(?:\d{2}|CB))\s*</div>',
            r'class="qr-label"[^>]*>\s*([A-Z]{2}-(?:\d{2}|CB))\s*</div>',
        ]
        for pattern in patterns:
            m = re.search(pattern, block, flags=re.IGNORECASE)
            if m:
                return m.group(1).upper()
        return None

    @staticmethod
    def _extract_url(block: str) -> str | None:
        """Extrait l'URL encodée dans un bloc QR HTML."""
        m = re.search(r"https?://(?:localhost|172\.20\.10\.4):5173[^<\"'\s]+", block)
        if m:
            return _OLD_BASE_RE.sub(BASE_URL, m.group(0))
        m = re.search(r"https://major-eval\.vercel\.app[^<\"'\s]+", block)
        return m.group(0) if m else None

    @staticmethod
    def _real_qr_html(b64: str, label: str, title: str, color: str, url: str) -> str:
        """Génère un bloc HTML real-qr complet."""
        return (
            f'<div class="real-qr" style="text-align:center;direction:rtl">'
            f'<img src="data:image/png;base64,{b64}" '
            f'style="width:86px;height:86px;border-radius:12px;'
            f'margin:8px auto 5px;display:block;border:2px solid {color}55" '
            f'alt="QR {label}"/>'
            f'<div style="font-size:7.5px;font-weight:900;color:{color};letter-spacing:.8px">{label}</div>'
            f'<div style="font-size:7px;color:#374151;font-weight:700;margin-top:2px">{title}</div>'
            f'<div style="font-size:6px;color:#9ca3af;margin-top:3px;font-family:monospace;word-break:break-all">{url}</div>'
            f'</div>'
        )
