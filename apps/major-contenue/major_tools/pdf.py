"""
major_tools.pdf — Conversion HTML → PDF
========================================

Utilise Google Chrome en mode headless pour convertir un fichier HTML
en PDF imprimable format A4, sans marges et sans en-têtes/pieds Chrome.

Classe principale :
    CahierConverter
"""

import os
import subprocess
import sys
from pathlib import Path


# Chemins Chrome courants sur Windows
_CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Users\PC\AppData\Local\Google\Chrome\Application\chrome.exe",
]


class CahierConverter:
    """
    Convertit un fichier HTML de cahier Major en PDF imprimable.

    Utilise Chrome headless (--print-to-pdf) pour garantir un rendu
    fidèle au CSS print, y compris les polices arabes (Cairo) et les
    sauts de page (@page break-after).

    Paramètres :
        chrome_path (str | None) : Chemin vers chrome.exe.
            Si None, détecte automatiquement parmi les emplacements standards.

    Exemples :
        # Conversion simple (PDF dans le même dossier que le HTML)
        conv = CahierConverter()
        conv.convert("6AF-ARABE/Cahier-Major-LangueArabe-Islamique-6AF.html")

        # Avec chemin de sortie explicite
        conv.convert("cahier.html", "exports/cahier.pdf")

        # Conversion de tous les cahiers d'un dossier
        conv.convert_folder("6AF-ARABE/", pattern="Cahier-Major-*.html")
    """

    def __init__(self, chrome_path: str | None = None):
        self.chrome_path = chrome_path or self._detect_chrome()

    # ── Détection automatique de Chrome ──────────────────────────────

    def _detect_chrome(self) -> str:
        """Cherche chrome.exe dans les emplacements standards Windows."""
        for path in _CHROME_CANDIDATES:
            if os.path.exists(path):
                return path
        raise FileNotFoundError(
            "Chrome introuvable. Installez Google Chrome ou passez chrome_path= au constructeur."
        )

    # ── Conversion d'un seul fichier ─────────────────────────────────

    def convert(self, html_path: str, pdf_path: str | None = None) -> Path:
        """
        Convertit un fichier HTML en PDF.

        Paramètres :
            html_path (str) : Chemin vers le fichier HTML source.
            pdf_path  (str) : Chemin de sortie du PDF.
                Si None, génère <nom_du_fichier>.pdf dans le même dossier.

        Retourne :
            Path : Chemin absolu du PDF généré.

        Lève :
            FileNotFoundError : Si html_path n'existe pas.
            RuntimeError      : Si Chrome échoue à générer le PDF.
        """
        html_path = Path(html_path).resolve()
        if not html_path.exists():
            raise FileNotFoundError(f"Fichier introuvable : {html_path}")

        if pdf_path is None:
            pdf_path = html_path.with_suffix(".pdf")
        pdf_path = Path(pdf_path).resolve()

        cmd = [
            self.chrome_path,
            "--headless",
            "--disable-gpu",
            f"--print-to-pdf={pdf_path}",
            "--print-to-pdf-no-header",
            "--no-margins",
            str(html_path),
        ]

        print(f"[CahierConverter] Conversion : {html_path.name}")
        result = subprocess.run(cmd, capture_output=True, text=True)

        if not pdf_path.exists():
            raise RuntimeError(
                f"Échec de la conversion Chrome.\n{result.stderr}"
            )

        size_kb = pdf_path.stat().st_size / 1024
        print(f"[CahierConverter] ✅ {pdf_path.name} ({size_kb:.0f} Ko)")
        return pdf_path

    # ── Conversion d'un dossier entier ───────────────────────────────

    def convert_folder(
        self,
        folder: str,
        pattern: str = "Cahier-Major-*.html",
        output_dir: str | None = None,
    ) -> list[Path]:
        """
        Convertit tous les fichiers HTML correspondant au pattern dans un dossier.

        Paramètres :
            folder     (str) : Dossier à scanner.
            pattern    (str) : Glob pattern (défaut : "Cahier-Major-*.html").
            output_dir (str) : Dossier de sortie des PDF.
                Si None, les PDF sont placés à côté de chaque HTML.

        Retourne :
            list[Path] : Liste des fichiers PDF générés.
        """
        folder = Path(folder)
        html_files = sorted(folder.glob(pattern))

        if not html_files:
            print(f"[CahierConverter] Aucun fichier trouvé : {folder}/{pattern}")
            return []

        results = []
        for html in html_files:
            out = Path(output_dir) / html.with_suffix(".pdf").name if output_dir else None
            try:
                pdf = self.convert(str(html), str(out) if out else None)
                results.append(pdf)
            except Exception as e:
                print(f"[CahierConverter] ❌ {html.name} : {e}")

        print(f"\n[CahierConverter] {len(results)}/{len(html_files)} PDF générés.")
        return results
