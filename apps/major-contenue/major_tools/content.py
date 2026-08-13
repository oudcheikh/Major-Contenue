"""
major_tools.content — Ajout de contenu aux cahiers HTML
=========================================================

Insère des pages d'exercices et des pages de concours blanc dans
les fichiers HTML des cahiers Major 6AF.

Classe principale :
    ContentBuilder

Opérations disponibles :
    append_pages()         — Ajoute du HTML de pages à la fin d'un cahier
    insert_concours_pages()— Insère des pages de concours blanc numérotées
    split_into_booklets()  — Sépare un cahier en 2 sous-cahiers par matière
"""

import re
from pathlib import Path
from .qr import QRCodeGenerator, BASE_URL


class ContentBuilder:
    """
    Construit et enrichit les cahiers HTML Major avec de nouvelles pages.

    Gère l'insertion de pages d'exercices supplémentaires, la génération
    de pages de simulation concours blanc, et la séparation d'un cahier
    multi-matières en sous-cahiers indépendants.

    Paramètres :
        qr_gen (QRCodeGenerator | None) : Générateur QR partagé.

    Exemples :
        builder = ContentBuilder()

        # Insérer les pages de concours blanc dans le cahier arabe
        builder.insert_concours_pages(
            html_path="6AF-ARABE/Cahier-Major-LangueArabe-Islamique-6AF.html",
            pages_html=MY_PAGES_HTML
        )

        # Séparer le grand cahier arabe en 2 sous-cahiers
        builder.split_into_booklets(
            html_path="6AF-ARABE/Cahier-Major-Arabe-6AF_backup.html",
            booklets=[
                {
                    "output": "Cahier-Major-LangueArabe-Islamique-6AF.html",
                    "page_ranges": [(1, 13), (20, 24)],
                    "title": "اللغة العربية · التربية الإسلامية",
                    "tabs": [("عربية", "#7c3aed"), ("إسلامية", "#059669")],
                },
                {
                    "output": "Cahier-Major-HistoireGeo-Civique-6AF.html",
                    "page_ranges": [(15, 19), (25, 29)],
                    "title": "التاريخ والجغرافيا · التربية المدنية",
                    "tabs": [("تاريخ", "#b45309"), ("مدنية", "#1d4ed8")],
                },
            ]
        )
    """

    def __init__(self, qr_gen: QRCodeGenerator | None = None):
        self.qr = qr_gen or QRCodeGenerator()

    # ── Ajout de pages HTML ───────────────────────────────────────────

    def append_pages(self, html_path: str, pages_html: str) -> int:
        """
        Ajoute des pages HTML à la fin d'un cahier, avant </body>.

        Paramètres :
            html_path  (str) : Fichier HTML de destination.
            pages_html (str) : HTML des pages à insérer.

        Retourne :
            int : Nombre de pages <div class="page"> insérées.

        Exemple :
            pages = "<div class='page'>...</div><div class='page'>...</div>"
            builder.append_pages("cahier.html", pages)
        """
        path = Path(html_path)
        html = path.read_text(encoding="utf-8")

        if "</body>" not in html:
            raise ValueError(f"Tag </body> introuvable dans {html_path}")

        html = html.replace("</body>", f"\n{pages_html}\n</body>", 1)
        count = pages_html.count('<div class="page">')
        path.write_text(html, encoding="utf-8")
        print(f"[ContentBuilder] {path.name} : {count} page(s) ajoutée(s)")
        return count

    # ── Pages concours blanc ──────────────────────────────────────────

    def insert_concours_pages(
        self,
        html_path: str,
        pages_html: str,
        after_page_number: int | None = None,
    ) -> int:
        """
        Insère des pages de concours blanc dans le cahier.

        Paramètres :
            html_path         (str)      : Fichier HTML cible.
            pages_html        (str)      : HTML des pages concours à insérer.
            after_page_number (int|None) : Insère après cette page numérotée.
                Si None, ajoute à la fin du document.

        Retourne :
            int : Nombre de pages insérées.
        """
        path = Path(html_path)
        html = path.read_text(encoding="utf-8")

        if after_page_number is not None:
            # Trouve la page correspondant au numéro demandé
            pattern = rf'<div class="page-number"[^>]*>{after_page_number}</div>'
            m = re.search(pattern, html)
            if m:
                # Trouve la fin du bloc <div class="page"> contenant ce numéro
                page_start = html.rfind('<div class="page">', 0, m.start())
                # Cherche la prochaine page ou </body>
                next_page = html.find('<div class="page">', m.end())
                insert_pos = next_page if next_page > 0 else html.find("</body>")
                html = html[:insert_pos] + f"\n{pages_html}\n" + html[insert_pos:]
            else:
                print(f"  [!] Page {after_page_number} non trouvée, ajout en fin de document")
                html = html.replace("</body>", f"\n{pages_html}\n</body>", 1)
        else:
            html = html.replace("</body>", f"\n{pages_html}\n</body>", 1)

        count = pages_html.count('<div class="page">')
        path.write_text(html, encoding="utf-8")
        print(f"[ContentBuilder] {path.name} : {count} page(s) concours insérée(s)")
        return count

    # ── Séparation en sous-cahiers ────────────────────────────────────

    def split_into_booklets(
        self,
        html_path: str,
        booklets: list[dict],
        output_dir: str | None = None,
    ) -> list[Path]:
        """
        Sépare un cahier multi-matières en sous-cahiers indépendants.

        Chaque entrée de `booklets` définit un sous-cahier avec :
          - "output"      (str)              : Nom du fichier de sortie.
          - "page_ranges" (list[tuple])      : Plages de pages [(start, end), ...].
                                               Indices 1-based inclusifs.
          - "title"       (str)              : Titre du document HTML.
          - "tabs"        (list[tuple])      : Onglets [(label, color), ...].
          - "extra_pages" (list[str])        : Pages HTML supplémentaires à ajouter.

        Paramètres :
            html_path  (str)        : Fichier source (backup recommandé).
            booklets   (list[dict]) : Configuration des sous-cahiers.
            output_dir (str | None) : Dossier de sortie. Défaut : même que source.

        Retourne :
            list[Path] : Fichiers HTML générés.

        Exemple :
            builder.split_into_booklets("cahier_backup.html", [
                {
                    "output": "Cahier-Arabe-Islamique.html",
                    "page_ranges": [(1, 13), (20, 24)],
                    "title": "اللغة العربية · التربية الإسلامية",
                    "tabs": [("عربية", "#7c3aed"), ("إسلامية", "#059669")],
                }
            ])
        """
        src  = Path(html_path)
        base = Path(output_dir) if output_dir else src.parent
        html = src.read_text(encoding="utf-8")

        # Extrait le <head> et la barre d'outils
        head_end = html.find("<body")
        head_html = html[:head_end] if head_end > 0 else ""
        toolbar_m = re.search(r'<div class="toolbar">.*?</script>', html, re.DOTALL)
        toolbar   = toolbar_m.group(0) if toolbar_m else ""

        # Trouve toutes les pages de premier niveau
        page_pat = re.compile(
            r'<div class="page(?![-]body|[-]main|[-]number|[-]title|[-]foot|[-]head|[-]wrap|[-]content)[^"]*"'
        )
        page_positions = list(page_pat.finditer(html))

        def extract_pages(ranges: list[tuple[int, int]]) -> list[str]:
            """Extrait les pages selon les plages 1-based spécifiées."""
            result = []
            for start, end in ranges:
                for i in range(start - 1, min(end, len(page_positions))):
                    p_start = page_positions[i].start()
                    p_end   = page_positions[i+1].start() if i+1 < len(page_positions) else len(html)
                    result.append(html[p_start:p_end])
            return result

        def renumber_pages(pages: list[str]) -> list[str]:
            """Renumérote les pages de 1 à N."""
            result = []
            for i, p in enumerate(pages):
                p = re.sub(
                    r'(<div class="page-number"[^>]*>)\d+(</div>)',
                    rf'\g<1>{i+1}\2', p
                )
                result.append(p)
            return result

        def apply_tabs(pages: list[str], tabs: list[tuple[str, str]]) -> list[str]:
            """Remplace les onglets .tabs dans chaque page."""
            tabs_html = "\n".join(
                f'    <div class="tab" style="background:{color}">{label}</div>'
                for label, color in tabs
            )
            result = []
            for p in pages:
                p = re.sub(
                    r'<div class="tabs">.*?</div>(?=\s*</div>)',
                    f'<div class="tabs">\n{tabs_html}\n  </div>',
                    p, flags=re.DOTALL
                )
                result.append(p)
            return result

        created = []
        for spec in booklets:
            output_name = spec["output"]
            page_ranges = spec.get("page_ranges", [])
            title       = spec.get("title", "Cahier Major 6AF")
            tabs        = spec.get("tabs", [])
            extra       = spec.get("extra_pages", [])

            pages = extract_pages(page_ranges) + extra
            pages = renumber_pages(pages)
            if tabs:
                pages = apply_tabs(pages, tabs)

            # Construit le document complet
            head = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", head_html)
            head = head.replace(
                ".page:last-of-type{break-after:auto !important;page-break-after:auto !important}",
                "body > .page:last-child{break-after:auto !important;page-break-after:auto !important}"
            )
            tb = toolbar.replace("'Cahier-Major-Arabe-6AF.html'", f"'{output_name}'")

            full_html = f"{head}<body>\n\n{tb}\n\n" + "\n\n".join(pages) + "\n\n</body>\n</html>"

            out_path = base / output_name
            out_path.write_text(full_html, encoding="utf-8")
            size_kb = len(full_html) / 1024
            print(f"[ContentBuilder] ✅ {output_name} ({size_kb:.0f} Ko, {len(pages)} pages)")
            created.append(out_path)

        return created

    # ── Ajout d'exercices depuis les examens officiels ────────────────

    def add_exercises_from_html(
        self,
        target_path: str,
        exercises_html: str,
        before_tag: str = '<div class="page-footer">',
        page_index: int = -1,
    ) -> bool:
        """
        Insère un bloc d'exercices HTML dans une page spécifique.

        Paramètres :
            target_path    (str) : Fichier HTML cible.
            exercises_html (str) : HTML des exercices à insérer.
            before_tag     (str) : Tag avant lequel insérer (défaut : page-footer).
            page_index     (int) : Page cible (0-based, -1 = dernière).

        Retourne :
            bool : True si l'insertion a réussi.
        """
        path = Path(target_path)
        html = path.read_text(encoding="utf-8")

        pages = [m.start() for m in re.finditer(r'<div class="page">', html)]
        if not pages:
            return False

        idx     = page_index if page_index >= 0 else len(pages) - 1
        p_start = pages[idx]
        p_end   = pages[idx+1] if idx+1 < len(pages) else len(html)
        page    = html[p_start:p_end]

        tag_pos = page.find(before_tag)
        if tag_pos < 0:
            return False

        new_page = page[:tag_pos] + exercises_html + "\n" + page[tag_pos:]
        html = html[:p_start] + new_page + html[p_end:]
        path.write_text(html, encoding="utf-8")
        print(f"[ContentBuilder] Exercices insérés dans la page {idx+1}")
        return True
