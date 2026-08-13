from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "Cahier-Major-LangueArabe-Islamique-6AF-V3-Cartoon.html"
OUT = ROOT / "Cahier-V3-Cartoon-pages-A5"


def find_matching_page_end(text: str, start: int) -> int:
    pos = start
    depth = 0
    tag_re = re.compile(r"</?div\b[^>]*>", re.IGNORECASE)
    for match in tag_re.finditer(text, start):
        tag = match.group(0)
        if tag.startswith("</"):
            depth -= 1
            if depth == 0:
                return match.end()
        else:
            depth += 1
    raise RuntimeError(f"Could not find end of page starting at {start}")


def extract_pages(text: str) -> list[str]:
    starts = [m.start() for m in re.finditer(r'<div class="page"', text)]
    pages = []
    for start in starts:
        end = find_matching_page_end(text, start)
        pages.append(text[start:end])
    return pages


def main() -> None:
    text = SRC.read_text(encoding="utf-8", errors="replace")
    head = text[: text.index("</style>")]
    pages = extract_pages(text)
    OUT.mkdir(exist_ok=True)

    print_css = """

/* Page-by-page A5 export. Keeps the original page design, scaled once. */
html, body {
  margin:0 !important;
  padding:0 !important;
}
.page {
  display:block !important;
  width:148mm !important;
  height:210mm !important;
  min-height:210mm !important;
  padding:0 !important;
  overflow:hidden !important;
  position:relative !important;
}
.page > .print-scale-inner {
  position:absolute !important;
  top:0 !important;
  right:0 !important;
  width:210mm !important;
  height:297mm !important;
  transform:scale(var(--page-scale, .7047619)) !important;
  transform-origin:top right !important;
  background:inherit !important;
  overflow:visible !important;
}
.qr-strip { display:none !important; }
.cartoon-illus, .page-sticker { display:none !important; }

@media screen {
  body { background:#e5e7eb !important; padding:16px 0 !important; }
  .page { margin:0 auto !important; box-shadow:0 6px 36px rgba(0,0,0,.18) !important; }
}
@media print {
  @page { size:A5 portrait; margin:0; }
  html, body {
    width:148mm !important;
    height:210mm !important;
    margin:0 !important;
    padding:0 !important;
    background:#fff !important;
    overflow:hidden !important;
  }
  .print-btn, .no-print { display:none !important; }
  .page {
    width:148mm !important;
    height:210mm !important;
    min-height:210mm !important;
    margin:0 !important;
    padding:0 !important;
    box-shadow:none !important;
    overflow:hidden !important;
    position:relative !important;
    page-break-after:auto !important;
    break-after:auto !important;
  }
  * { -webkit-print-color-adjust:exact !important; print-color-adjust:exact !important; }
}
"""

    fit_script = """
<script>
(() => {
  const BASE_SCALE = 148 / 210;

  const fitPage = () => {
    const page = document.querySelector('.page');
    const inner = document.querySelector('.page > .print-scale-inner');
    if (!page || !inner) return;

    inner.style.transform = 'none';
    const pageBox = page.getBoundingClientRect();
    const innerBox = inner.getBoundingClientRect();
    let contentBottom = inner.scrollHeight;
    let contentRight = inner.scrollWidth;

    inner.querySelectorAll('*').forEach((el) => {
      const style = getComputedStyle(el);
      if (style.display === 'none' || style.visibility === 'hidden') return;
      const box = el.getBoundingClientRect();
      contentBottom = Math.max(contentBottom, box.bottom - innerBox.top);
      contentRight = Math.max(contentRight, box.right - innerBox.left);
    });

    const scaleByWidth = pageBox.width / Math.max(contentRight, innerBox.width);
    const scaleByHeight = pageBox.height / contentBottom;
    const scale = Math.min(BASE_SCALE, scaleByWidth, scaleByHeight) * 0.995;
    inner.style.setProperty('--page-scale', String(scale));
    inner.style.transform = '';
  };

  window.addEventListener('load', fitPage);
  window.addEventListener('resize', fitPage);
  window.addEventListener('beforeprint', fitPage);
  document.fonts && document.fonts.ready.then(fitPage);
})();
</script>
"""

    for idx, page in enumerate(pages, 1):
        wrapped = re.sub(
            r'(<div class="page"[^>]*>)',
            r'\1<div class="print-scale-inner">',
            page,
            count=1,
        ) + "</div>"
        html = (
            head
            + print_css
            + "\n</style>\n</head>\n<body>\n"
            + wrapped
            + fit_script
            + "\n</body>\n</html>\n"
        )
        html = (
            html.replace("url('assets/", "url('../assets/")
            .replace('url("assets/', 'url("../assets/')
            .replace('src="assets/', 'src="../assets/')
            .replace("src='assets/", "src='../assets/")
        )
        (OUT / f"page-{idx:02d}.html").write_text(html, encoding="utf-8")

    links = "\n".join(
        f'<a href="page-{idx:02d}.html">Page {idx:02d}</a>' for idx in range(1, len(pages) + 1)
    )
    index = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Pages A5 - Cahier V3 Cartoon</title>
<style>
body{{font-family:Arial,sans-serif;background:#f3f4f6;margin:0;padding:24px;color:#111827}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:10px;max-width:900px}}
a{{display:block;background:#fff;border:1px solid #d1d5db;border-radius:8px;padding:12px;text-align:center;color:#1d4ed8;text-decoration:none;font-weight:700}}
a:hover{{background:#eff6ff}}
</style>
</head>
<body>
<h1>Pages A5 - Cahier V3 Cartoon</h1>
<p>Ouvre une page, puis imprime en A5, marges aucune, echelle 100%, graphiques d'arriere-plan actives.</p>
<div class="grid">
{links}
</div>
</body>
</html>
"""
    (OUT / "index.html").write_text(index, encoding="utf-8")
    print(f"Generated {len(pages)} pages in {OUT}")


if __name__ == "__main__":
    main()
