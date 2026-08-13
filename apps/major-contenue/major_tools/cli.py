"""
major_tools.cli — Interface en ligne de commande
=================================================

Point d'entrée CLI pour toutes les opérations sur les cahiers Major.

Usage :
    python -m major_tools <commande> [options]

Commandes disponibles :
    pdf         Convertit un HTML en PDF
    qr-export   Exporte tous les QR codes en fichiers PNG
    qr-inject   Injecte les QR codes dans les fichiers HTML
    trim        Rogne les pages surchargées
    repaginate  Renumérote les pages d'un cahier
    fix-print   Corrige le CSS @media print

Exemples :
    python -m major_tools pdf 6AF-ARABE/Cahier-Major-LangueArabe-Islamique-6AF.html
    python -m major_tools qr-export --output qrcodes/
    python -m major_tools qr-inject --all
    python -m major_tools trim 6AF-ARABE/Cahier-Major-Arabe-6AF.html
    python -m major_tools repaginate 6AF-ARABE/Cahier-Major-LangueArabe-Islamique-6AF.html
"""

import argparse
import sys
from pathlib import Path


def cmd_pdf(args):
    from .pdf import CahierConverter
    conv = CahierConverter()
    if args.folder:
        conv.convert_folder(args.file, pattern=args.pattern or "Cahier-Major-*.html")
    else:
        conv.convert(args.file, args.output or None)


def cmd_qr_export(args):
    from .qr import QRCodeGenerator
    gen = QRCodeGenerator()
    gen.export_all(output_dir=args.output or "qrcodes")


def cmd_qr_inject(args):
    from .injector import QRInjector
    inj = QRInjector(root=args.root or None)
    if args.all:
        inj.inject_all_html()
    elif args.file:
        inj.inject_file(args.file)
        if args.strips:
            inj.add_bottom_strips(args.file)
    else:
        print("Spécifiez --all ou --file <chemin>")
        sys.exit(1)


def cmd_trim(args):
    from .layout import LayoutFixer
    fixer = LayoutFixer(dry_run=args.dry_run)
    fixer.trim_overflows(args.file)


def cmd_repaginate(args):
    from .layout import LayoutFixer
    fixer = LayoutFixer(dry_run=args.dry_run)
    fixer.repaginate(args.file, start=args.start)


def cmd_fix_print(args):
    from .layout import LayoutFixer
    fixer = LayoutFixer(dry_run=args.dry_run)
    fixer.fix_print_css(args.file)


def main():
    parser = argparse.ArgumentParser(
        prog="python -m major_tools",
        description="Outils de génération des cahiers Major 6AF",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # ── pdf ──────────────────────────────────────────────────────────
    p_pdf = sub.add_parser("pdf", help="Convertir HTML -> PDF")
    p_pdf.add_argument("file",   help="Fichier HTML source ou dossier (avec --folder)")
    p_pdf.add_argument("-o", "--output", help="Chemin du PDF de sortie")
    p_pdf.add_argument("--folder",  action="store_true", help="Convertir tous les HTML du dossier")
    p_pdf.add_argument("--pattern", help="Glob pattern (défaut: Cahier-Major-*.html)")
    p_pdf.set_defaults(func=cmd_pdf)

    # ── qr-export ────────────────────────────────────────────────────
    p_qre = sub.add_parser("qr-export", help="Exporter tous les QR codes en PNG")
    p_qre.add_argument("-o", "--output", help="Dossier de sortie (défaut: qrcodes/)")
    p_qre.set_defaults(func=cmd_qr_export)

    # ── qr-inject ────────────────────────────────────────────────────
    p_qri = sub.add_parser("qr-inject", help="Injecter les QR codes dans les HTML")
    p_qri.add_argument("--file",   help="Fichier HTML ciblé")
    p_qri.add_argument("--all",    action="store_true", help="Traiter tous les HTML du projet")
    p_qri.add_argument("--strips", action="store_true", help="Ajouter aussi les bandeaux QR de bas de page")
    p_qri.add_argument("--root",   help="Dossier racine du projet")
    p_qri.set_defaults(func=cmd_qr_inject)

    # ── trim ─────────────────────────────────────────────────────────
    p_trim = sub.add_parser("trim", help="Rogner les pages surchargées")
    p_trim.add_argument("file", help="Fichier HTML cible")
    p_trim.add_argument("--dry-run", action="store_true", help="Simulation sans écriture")
    p_trim.set_defaults(func=cmd_trim)

    # ── repaginate ───────────────────────────────────────────────────
    p_rep = sub.add_parser("repaginate", help="Renuméroter les pages")
    p_rep.add_argument("file", help="Fichier HTML cible")
    p_rep.add_argument("--start", type=int, default=1, help="Numéro de départ (défaut: 1)")
    p_rep.add_argument("--dry-run", action="store_true", help="Simulation sans écriture")
    p_rep.set_defaults(func=cmd_rep)

    # ── fix-print ────────────────────────────────────────────────────
    p_fix = sub.add_parser("fix-print", help="Corriger le CSS d'impression")
    p_fix.add_argument("file", help="Fichier HTML cible")
    p_fix.add_argument("--dry-run", action="store_true", help="Simulation sans écriture")
    p_fix.set_defaults(func=cmd_fix_print)

    args = parser.parse_args()
    args.func(args)


# Fix du nom de fonction manquant (repaginate)
def cmd_rep(args):
    from .layout import LayoutFixer
    fixer = LayoutFixer(dry_run=args.dry_run)
    fixer.repaginate(args.file, start=args.start)


if __name__ == "__main__":
    main()
