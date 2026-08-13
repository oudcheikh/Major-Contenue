# -*- coding: utf-8 -*-
"""Assemble le CAHIER LUDIQUE A5 complet :
   - couvertures (reprises du PDF A5 existant, deja correctes)
   - pages de contenu 02..24 refondues (moteur _reflow) + footers renumerotes
   - rendu Chrome -> PDF, puis fusion [couv1 + contenu + couv25] via pypdf.
"""
import io, os, re, subprocess
import _reflow as R
from pypdf import PdfReader, PdfWriter

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
HERE   = os.path.abspath(".").replace("\\", "/")
EXIST  = "Cahier-Major-LangueArabe-Islamique-6AF-A5.pdf"   # pour reprendre les 2 couvertures
OUT    = "Cahier-Major-LangueArabe-Islamique-6AF-A5-LUDIQUE.pdf"

def chrome_pdf(html_path, pdf_path):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", "--virtual-time-budget=12000",
                    "--print-to-pdf=" + pdf_path, "file:///" + html_path],
                   capture_output=True, timeout=180)

def main():
    # 1) refonte du contenu
    content = []
    for i in range(2, 25):
        r = R.reflow_page("page-%02d.html" % i)
        if r: content += r
    total = len(content) + 2          # + 2 couvertures
    print("contenu refondu:", len(content), "pages | total avec couvertures:", total)

    # 2) renumeroter les footers (k / total), k = 2..total-1
    def renum(html, k):
        return re.sub(r'<div class="qr-footer-pgnum">.*?</div>',
                      '<div class="qr-footer-pgnum">&#128209; %d / %d</div>' % (k, total),
                      html, flags=re.DOTALL)
    content = [renum(p, idx) for idx, p in enumerate(content, start=2)]

    # 3) doc + rendu
    doc = R.doc_html(content)
    io.open("_content_lud.html", "w", encoding="utf-8").write(doc)
    chrome_pdf(HERE + "/_content_lud.html", HERE + "/_content_lud.pdf")
    cpdf = PdfReader("_content_lud.pdf")
    print("PDF contenu:", len(cpdf.pages), "pages")

    # 4) couvertures depuis le PDF A5 existant (page 0 = avant, derniere = arriere)
    ex = PdfReader(EXIST)
    cov_front, cov_back = ex.pages[0], ex.pages[-1]

    # 5) fusion
    w = PdfWriter()
    w.add_page(cov_front)
    for pg in cpdf.pages: w.add_page(pg)
    w.add_page(cov_back)
    with io.open(OUT, "wb") as f: w.write(f)
    print("OK ->", OUT, "|", len(w.pages), "pages A5")

if __name__ == "__main__":
    main()
