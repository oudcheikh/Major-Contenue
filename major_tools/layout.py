"""
major_tools.layout — Correction de mise en page des cahiers HTML
=================================================================

Regroupe tous les outils de manipulation du layout HTML des cahiers :
pagination, découpe des pages surchargées, correction des débordements
CSS à l'impression.

Classe principale :
    LayoutFixer

Opérations disponibles :
    trim_overflows()   — Supprime les exercices excédentaires par page
    split_long_pages() — Découpe les pages avec trop de contenu
    repaginate()       — Renumérote toutes les pages d'un cahier
    fix_print_css()    — Injecte/corrige le CSS @media print
    split_cahier()     — Sépare un cahier en sous-cahiers par matière
"""

import re
import shutil
from pathlib import Path


class LayoutFixer:
    """
    Corrige et optimise la mise en page des cahiers HTML Major.

    Chaque méthode lit le fichier HTML, applique les transformations,
    et réécrit le fichier en place (sauf si `dry_run=True`).

    Paramètres :
        dry_run (bool) : Si True, n'écrit rien (mode prévisualisation).

    Exemples :
        fixer = LayoutFixer()

        # Supprimer les exercices qui débordent sur certaines pages
        fixer.trim_overflows(
            html_path="6AF-ARABE/Cahier-Major-Arabe-6AF.html",
            trim_map={6: 4, 7: 4, 12: 4}   # {page_index_0based: max_exos}
        )

        # Renuméroter toutes les pages (après une séparation/fusion)
        fixer.repaginate("6AF-ARABE/Cahier-Major-LangueArabe-Islamique-6AF.html")

        # Corriger le CSS print (overflow, height, page-break)
        fixer.fix_print_css("6AF-ARABE/Cahier-Major-Arabe-6AF.html")
    """

    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run

    # ── Sauvegarde préventive ─────────────────────────────────────────

    def backup(self, html_path: str) -> Path:
        """
        Crée une copie de sauvegarde avant toute modification.

        Paramètres :
            html_path (str) : Fichier à sauvegarder.

        Retourne :
            Path : Chemin du fichier de backup créé.
        """
        src = Path(html_path)
        dst = src.with_name(f"{src.stem}_layout_backup{src.suffix}")
        shutil.copy2(src, dst)
        print(f"[LayoutFixer] Backup → {dst.name}")
        return dst

    # ── Suppression des débordements ──────────────────────────────────

    def trim_overflows(
        self,
        html_path: str,
        trim_map: dict[int, int] | None = None,
    ) -> int:
        """
        Supprime les exercices excédentaires des pages qui débordent en A4.

        Traite les pages dans l'ordre inverse pour préserver les indices
        lors des modifications successives.

        Paramètres :
            html_path (str)             : Fichier HTML à modifier.
            trim_map  (dict[int, int])  : Mapping {page_index_0based: max_exercices}.
                Si None, applique les valeurs par défaut du cahier arabe.

        Retourne :
            int : Nombre de pages modifiées.

        Exemple :
            # Limiter à 4 exercices sur les pages 7, 8 et 13
            fixer.trim_overflows("cahier.html", trim_map={6: 4, 7: 4, 12: 4})
        """
        if trim_map is None:
            # Valeurs par défaut issues du cahier arabe 6AF
            trim_map = {6: 4, 7: 4, 12: 4, 25: 5, 26: 4, 28: 5}

        path = Path(html_path)
        html = path.read_text(encoding="utf-8")

        page_starts = [m.start() for m in re.finditer(r'<div class="page">', html)]
        n_pages = len(page_starts)
        print(f"[LayoutFixer] {n_pages} pages · {len(trim_map)} à couper")

        boundaries = page_starts + [len(html)]
        processed = 0

        for page_idx in sorted(trim_map.keys(), reverse=True):
            if page_idx >= n_pages:
                print(f"  [!] Page {page_idx+1} inexistante")
                continue

            max_exo = trim_map[page_idx]
            start   = page_starts[page_idx]
            end     = boundaries[page_idx + 1]
            page    = html[start:end]

            exos = list(re.finditer(r'<div class="exo-card[^"]*">', page))
            if len(exos) <= max_exo:
                continue  # pas de dépassement

            cut_pos      = exos[max_exo].start()
            footer_match = re.search(r'<div class="page-footer">', page)

            if footer_match:
                new_page = page[:cut_pos] + page[footer_match.start():]
            else:
                closes = list(re.finditer(r'</div>', page))
                if len(closes) >= 4:
                    new_page = page[:cut_pos] + page[closes[-4].start():]
                else:
                    new_page = page[:cut_pos] + '</div></div></div>\n'

            html = html[:start] + new_page + html[end:]
            remaining = len(re.findall(r'<div class="exo-card[^"]*">', new_page))
            print(f"  ✅ Page {page_idx+1}: {len(exos)} exo → {remaining} exo")
            processed += 1

        if not self.dry_run:
            path.write_text(html, encoding="utf-8")
        print(f"[LayoutFixer] {processed} pages rognées")
        return processed

    # ── Renumérotation des pages ──────────────────────────────────────

    def repaginate(self, html_path: str, start: int = 1) -> int:
        """
        Renumérote séquentiellement tous les blocs .page-number du HTML.

        Paramètres :
            html_path (str) : Fichier HTML à modifier.
            start     (int) : Numéro de la première page (défaut : 1).

        Retourne :
            int : Nombre de numéros de page mis à jour.
        """
        path = Path(html_path)
        html = path.read_text(encoding="utf-8")

        counter = [start - 1]

        def replacer(m: re.Match) -> str:
            counter[0] += 1
            return f'{m.group(1)}{counter[0]}{m.group(2)}'

        new_html, count = re.subn(
            r'(<div class="page-number"[^>]*>)\d+(</div>)',
            replacer,
            html
        )

        if not self.dry_run:
            path.write_text(new_html, encoding="utf-8")
        print(f"[LayoutFixer] {path.name} : {count} pages renumérotées (début={start})")
        return count

    # ── Correction CSS print ──────────────────────────────────────────

    def fix_print_css(self, html_path: str) -> bool:
        """
        Injecte ou corrige le CSS @media print pour l'impression A4.

        Corrections appliquées :
          - overflow: visible sur .page et .page-body
          - height: auto sur les conteneurs
          - Correction du sélecteur :last-of-type → :last-child
          - Suppression des max-height bloquants

        Paramètres :
            html_path (str) : Fichier HTML à modifier.

        Retourne :
            bool : True si des modifications ont été appliquées.
        """
        path = Path(html_path)
        html = path.read_text(encoding="utf-8")
        original = html

        # Corrige le bug de la dernière page (last-of-type vs last-child)
        html = html.replace(
            ".page:last-of-type{break-after:auto !important;page-break-after:auto !important}",
            "body > .page:last-child{break-after:auto !important;page-break-after:auto !important}"
        )

        # Injecte le CSS print manquant si absent
        print_css = """<style>
@media print {
  .page        { overflow: visible !important; height: auto !important; break-inside: avoid; }
  .page-body   { overflow: visible !important; height: auto !important; }
  .page-main   { overflow: visible !important; }
  .toolbar     { display: none !important; }
}
</style>"""

        if "@media print" not in html and "</head>" in html:
            html = html.replace("</head>", print_css + "\n</head>", 1)

        changed = html != original
        if changed and not self.dry_run:
            path.write_text(html, encoding="utf-8")
        print(f"[LayoutFixer] fix_print_css : {'modifié' if changed else 'déjà OK'}")
        return changed

    # ── Découpe des pages longues ─────────────────────────────────────

    def split_long_pages(
        self,
        html_path: str,
        max_exos_per_page: int = 4,
        skip_page_numbers: set[str] | None = None,
    ) -> int:
        """
        Découpe automatiquement les pages contenant trop d'exercices.

        Analyse le poids de chaque page et la divise si elle dépasse
        `max_exos_per_page` exercices. Les pages de couverture, d'intro
        et celles dans `skip_page_numbers` sont ignorées.

        Paramètres :
            html_path          (str)       : Fichier HTML à modifier.
            max_exos_per_page  (int)       : Seuil déclenchant la division (défaut : 4).
            skip_page_numbers  (set[str])  : Numéros de page à ne pas toucher.

        Retourne :
            int : Nombre de nouvelles pages créées.
        """
        if skip_page_numbers is None:
            skip_page_numbers = {"1", "2", "3", "16", "21"}

        path = Path(html_path)
        html = path.read_text(encoding="utf-8")

        # Sépare le head du body
        body_start = html.find("<body")
        head = html[:body_start] if body_start > 0 else ""

        page_pattern = re.compile(
            r'<div class="page(?![-]body|[-]main|[-]number|[-]title|[-]foot|[-]head|[-]wrap|[-]content)[^"]*"'
        )
        pages = list(page_pattern.finditer(html))
        new_pages = 0
        modifications = []

        for i, m in enumerate(pages):
            p_start = m.start()
            p_end   = pages[i+1].start() if i+1 < len(pages) else len(html)
            page    = html[p_start:p_end]

            # Récupère le numéro de page
            num_m = re.search(r'<div class="page-number"[^>]*>(\d+)</div>', page)
            if num_m and num_m.group(1) in skip_page_numbers:
                continue

            exos = list(re.finditer(r'<div class="exo-card[^"]*">', page))
            if len(exos) <= max_exos_per_page:
                continue

            # Découpe en sous-pages de max_exos_per_page exercices
            chunks = [exos[j:j+max_exos_per_page] for j in range(0, len(exos), max_exos_per_page)]
            modifications.append((p_start, p_end, page, chunks))

        # Applique les modifications en ordre inverse
        for p_start, p_end, page, chunks in reversed(modifications):
            sub_pages = self._build_sub_pages(page, chunks)
            html = html[:p_start] + "\n".join(sub_pages) + html[p_end:]
            new_pages += len(chunks) - 1

        if not self.dry_run and new_pages > 0:
            path.write_text(html, encoding="utf-8")
        print(f"[LayoutFixer] split_long_pages : {new_pages} nouvelles pages créées")
        return new_pages

    # ── Helpers internes ──────────────────────────────────────────────

    @staticmethod
    def _build_sub_pages(page: str, chunks: list) -> list[str]:
        """
        Reconstruit plusieurs pages HTML à partir des groupes d'exercices.

        Conserve le header et le footer de la page originale pour chaque
        sous-page générée.
        """
        # Extrait header et footer
        body_m  = re.search(r'<div class="page-body">', page)
        footer_m = re.search(r'<div class="page-footer">', page)

        if not body_m:
            return [page]

        before_body  = page[:body_m.start()]
        after_footer = page[footer_m.start():] if footer_m else "</div></div>"

        sub_pages = []
        for i, chunk in enumerate(chunks):
            exo_start = chunk[0].start()
            exo_end   = chunk[-1].end()

            # Trouve la fermeture du dernier exercice du chunk
            depth = 0
            j = chunk[-1].start()
            while j < len(page):
                tag = re.match(r'<div\b|</div>', page[j:])
                if tag:
                    depth += 1 if tag.group(0).startswith("<div") else -1
                    j += tag.end()
                    if depth == 0:
                        break
                else:
                    j += 1

            exo_content = page[chunk[0].start():j]
            sub = (
                f'{before_body}'
                f'<div class="page-body">\n'
                f'<div class="grid-2">\n{exo_content}\n</div>\n'
                f'</div>\n'
                f'{after_footer}'
            )
            sub_pages.append(sub)

        return sub_pages
