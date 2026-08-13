from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / "Cahier-V3-Cartoon-pages-A5"

FIT_SCRIPT = r'''<script>
(() => {
  const BASE_SCALE = 148 / 210;
  const FOOTER_GAP_MM = 6;
  const HORIZONTAL_GAP_MM = 5;
  const SAFETY = 0.992;
  const DECO = ['wave-footer', 'page-num', 'qr-strip', 'blob-wrap', 'spiral-strip'];

  const important = (el, prop, value) => el.style.setProperty(prop, value, 'important');
  const clear = (el, ...props) => props.forEach((prop) => el.style.removeProperty(prop));
  const px = (value) => Number.parseFloat(value) || 0;

  const page = () => document.querySelector('.page');
  const inner = () => document.querySelector('.page > .print-scale-inner');
  const footer = () => document.querySelector('.page > .qr-footer');

  const resetViewport = () => {
    const p = page();
    if (!p) return;
    clear(p, 'position', 'inset', 'top', 'left', 'right', 'bottom', 'transform',
      'transform-origin', 'margin', 'margin-top', 'margin-bottom');
    clear(document.documentElement, 'width', 'height', 'overflow', 'background');
    clear(document.body, 'width', 'height', 'overflow', 'padding', 'margin', 'background');
  };

  const measurableElements = (root) => Array.from(root.querySelectorAll('*')).filter((el) => {
    const st = getComputedStyle(el);
    if (st.display === 'none' || st.visibility === 'hidden') return false;
    if (DECO.some((cls) => el.closest('.' + cls))) return false;
    return true;
  });

  const measureContent = (root) => {
    const rootBox = root.getBoundingClientRect();
    let bottom = root.scrollHeight || 0;
    let left = 0;
    let right = Math.max(rootBox.width, root.scrollWidth || 0);

    measurableElements(root).forEach((el) => {
      const st = getComputedStyle(el);
      const box = el.getBoundingClientRect();
      if (!box.width && !box.height) return;

      const relTop = box.top - rootBox.top;
      const relBottom = box.bottom - rootBox.top;
      const relLeft = box.left - rootBox.left;
      const relRight = box.right - rootBox.left;

      bottom = Math.max(
        bottom,
        relBottom + px(st.marginBottom),
        relTop + el.offsetHeight + px(st.marginTop) + px(st.marginBottom)
      );
      left = Math.min(left, relLeft - px(st.marginLeft));
      right = Math.max(right, relRight + px(st.marginRight));
    });

    bottom = Math.max(bottom, root.scrollHeight || 0, rootBox.height);
    if (bottom < 10) bottom = rootBox.height;
    return { bottom, width: right - left };
  };

  const fitPage = () => {
    const p = page();
    const root = inner();
    if (!p || !root) return;

    resetViewport();
    important(root, 'transform', 'none');

    const pageBox = p.getBoundingClientRect();
    const rootBox = root.getBoundingClientRect();
    const footerBox = footer()?.getBoundingClientRect();
    const mmPx = pageBox.height / 210;
    const mmPxW = pageBox.width / 148;
    const reservedFooter = (footerBox?.height || 0) + FOOTER_GAP_MM * mmPx;
    const availableHeight = Math.max(1, pageBox.height - reservedFooter);
    const availableWidth = Math.max(1, pageBox.width - HORIZONTAL_GAP_MM * mmPxW);
    const content = measureContent(root);

    const scaleByFooter = availableHeight / content.bottom;
    const scaleByPageHeight = pageBox.height / content.bottom;
    const scaleByWidth = availableWidth / Math.max(rootBox.width, root.scrollWidth || 0, content.width);
    const scale = Math.min(BASE_SCALE, scaleByFooter, scaleByPageHeight, scaleByWidth) * SAFETY;

    root.style.setProperty('--page-scale', String(Math.max(0.1, scale)));
    root.style.removeProperty('transform');
  };

  const fitViewport = () => {
    if (window.matchMedia && window.matchMedia('print').matches) return;

    const p = page();
    if (!p) return;

    const pageW = p.offsetWidth;
    const pageH = p.offsetHeight;
    const scale = Math.min(1, (window.innerWidth - 8) / pageW, (window.innerHeight - 8) / pageH);
    const visualW = Math.ceil(pageW * scale);
    const visualH = Math.ceil(pageH * scale);

    important(document.documentElement, 'width', '100vw');
    important(document.documentElement, 'height', '100vh');
    important(document.documentElement, 'overflow', 'hidden');
    important(document.body, 'width', '100vw');
    important(document.body, 'height', '100vh');
    important(document.body, 'margin', '0');
    important(document.body, 'padding', '0');
    important(document.body, 'overflow', 'hidden');
    important(document.body, 'background', '#e5e7eb');

    important(p, 'position', 'fixed');
    important(p, 'top', '50%');
    important(p, 'left', '50%');
    important(p, 'margin', '0');
    important(p, 'transform-origin', 'center center');
    important(p, 'transform', 'translate(-50%, -50%) scale(' + scale.toFixed(4) + ')');

    document.documentElement.dataset.a5Fit = '1';
    window.__a5Fit = { scale, visualW, visualH, pageW, pageH };
  };

  const run = () => {
    fitPage();
    fitViewport();
  };

  const runPrint = () => {
    resetViewport();
    fitPage();
  };

  window.addEventListener('load', run);
  window.addEventListener('resize', run);
  window.addEventListener('beforeprint', runPrint);
  window.addEventListener('afterprint', run);

  if (document.fonts?.ready) {
    document.fonts.ready.then(run);
  }
  requestAnimationFrame(run);
})();
</script>'''


SCRIPT_RE = re.compile(
    r"<script>\s*\(\(\)\s*=>\s*\{\s*const BASE_SCALE = 148 / 210;.*?</script>",
    re.DOTALL,
)

CSS_REPLACEMENTS = (
    (
        "transform:scale(.7047619) !important;",
        "transform:scale(var(--page-scale, .7047619)) !important;",
    ),
    (
        "padding:0 !important;\n    box-sizing:border-box !important;\n    transform:scale(var(--page-scale, .7047619)) !important;",
        "padding:6mm 20mm 52mm 9mm !important;\n    box-sizing:border-box !important;\n    transform:scale(var(--page-scale, .7047619)) !important;",
    ),
    (
        "width:210mm !important;\n  height:297mm !important;\n  transform:scale(var(--page-scale, .7047619)) !important;",
        "width:210mm !important;\n  height:297mm !important;\n  padding:6mm 20mm 52mm 9mm !important;\n  box-sizing:border-box !important;\n  transform:scale(var(--page-scale, .7047619)) !important;",
    ),
)

A5_INNER_PADDING_CSS = """
/* A5 wrapper: keep the original A4 page padding inside the scaled layer. */
.page > .print-scale-inner {
  padding:6mm 20mm 52mm 9mm !important;
  box-sizing:border-box !important;
}
"""

A5_COMPACT_CSS = """
/* A5 compact exercise density. */
.page > .print-scale-inner .page-header {
  padding:7px 12px 6px !important;
  margin-bottom:6px !important;
}
.page > .print-scale-inner .student-bar {
  margin-bottom:5px !important;
}
.page > .print-scale-inner .sec-pill-wrap {
  margin:5px 0 4px !important;
}
.page > .print-scale-inner .sec-pill {
  min-height:30px !important;
  padding:5px 28px 5px 16px !important;
  border-radius:9px !important;
}
.page > .print-scale-inner .qaaida-box {
  padding:5px 9px !important;
  margin-bottom:5px !important;
  border-radius:10px !important;
}
.page > .print-scale-inner .qaaida-title {
  font-size:12px !important;
  margin-bottom:2px !important;
}
.page > .print-scale-inner .qaaida-text {
  font-size:9.8px !important;
  line-height:1.42 !important;
}
.page > .print-scale-inner .grid2,
.page > .print-scale-inner .fill-grid,
.page > .print-scale-inner .circle-grid {
  grid-template-columns:minmax(0,1fr) minmax(0,1fr) !important;
  gap:5px !important;
  min-width:0 !important;
}
.page > .print-scale-inner .exo-card,
.page > .print-scale-inner .fill-item,
.page > .print-scale-inner .circle-item,
.page > .print-scale-inner .harf-item,
.page > .print-scale-inner .damir-item {
  min-width:0 !important;
  max-width:100% !important;
}
.page > .print-scale-inner .exo-card {
  padding:4px 6px 3px !important;
  margin-bottom:4px !important;
  border-radius:10px !important;
  border-width:2px !important;
  box-shadow:2px 2px 0 #111 !important;
}
.page > .print-scale-inner .exo-head {
  margin-bottom:3px !important;
}
.page > .print-scale-inner .exo-circle {
  font-size:9.2px !important;
  padding:2px 7px !important;
  border-width:1.5px !important;
  box-shadow:1px 1px 0 #111 !important;
}
.page > .print-scale-inner .exo-level,
.page > .print-scale-inner .exo-pts {
  font-size:8.5px !important;
}
.page > .print-scale-inner .exo-instr {
  font-size:10px !important;
  line-height:1.35 !important;
  margin-bottom:4px !important;
}
.page > .print-scale-inner .exo-example,
.page > .print-scale-inner .exo-tip,
.page > .print-scale-inner .hint-box {
  padding:4px 8px !important;
  margin-bottom:4px !important;
  font-size:9.4px !important;
  line-height:1.35 !important;
  border-radius:8px !important;
}
.page > .print-scale-inner .fill-item {
  min-height:38px !important;
  padding:4px 7px !important;
  gap:4px !important;
  border-radius:8px !important;
  box-shadow:1px 1px 0 rgba(37,99,235,.1) !important;
}
.page > .print-scale-inner .fill-item.two-lines {
  min-height:auto !important;
  padding:4px 7px !important;
  gap:2px !important;
}
.page > .print-scale-inner .fill-item.two-lines .fill-top {
  padding-bottom:2px !important;
  gap:4px !important;
  border-bottom-width:1px !important;
}
.page > .print-scale-inner .fill-index {
  width:18px !important;
  height:18px !important;
  min-width:18px !important;
  font-size:9px !important;
}
.page > .print-scale-inner .fill-word,
.page > .print-scale-inner .fill-item.two-lines .fill-top .fill-word {
  font-size:10px !important;
  line-height:1.25 !important;
}
.page > .print-scale-inner .fill-answer-2 {
  gap:1px !important;
  margin-top:0 !important;
}
.page > .print-scale-inner .fill-answer-2 .ans-row {
  gap:4px !important;
}
.page > .print-scale-inner .fill-answer-2 .ans-label {
  font-size:7.6px !important;
  padding:0 5px !important;
  border-radius:4px !important;
}
.page > .print-scale-inner .fill-answer-2 .ans-line {
  height:13px !important;
  border-bottom-width:1.5px !important;
}
.page > .print-scale-inner .answer-line {
  height:22px !important;
  margin-bottom:2px !important;
  border-bottom-width:1.5px !important;
}
.page > .print-scale-inner .labeled-lines .answer-line,
.page > .print-scale-inner .writing-area .answer-line {
  height:18px !important;
  margin-bottom:1px !important;
}
.page > .print-scale-inner .writing-area {
  padding:3px 8px !important;
  border-radius:7px !important;
}
.page > .print-scale-inner .ex-table {
  font-size:9px !important;
  margin-top:3px !important;
}
.page > .print-scale-inner .ex-table th,
.page > .print-scale-inner .ex-table td.word-cell {
  padding:3px 5px !important;
  font-size:8.5px !important;
}
.page > .print-scale-inner .ex-table td.answer-cell {
  height:24px !important;
}
.page > .print-scale-inner .circle-item,
.page > .print-scale-inner .harf-item,
.page > .print-scale-inner .damir-item {
  padding:5px 8px !important;
  border-radius:8px !important;
}
"""

COMPACT_RE = re.compile(
    r"\n/\* A5 compact exercise density\. \*/.*?(?=\n</style>)",
    re.DOTALL,
)


def main() -> None:
    changed = []
    for path in sorted(PAGES_DIR.glob("page-*.html")):
        html = path.read_text(encoding="utf-8")
        new_html, count = SCRIPT_RE.subn(FIT_SCRIPT, html, count=1)
        if count != 1:
            raise RuntimeError(f"{path.name}: expected one fit script, replaced {count}")
        for before, after in CSS_REPLACEMENTS:
            new_html = new_html.replace(before, after)
        if "A5 wrapper: keep the original A4 page padding" not in new_html:
            new_html = new_html.replace("</style>", A5_INNER_PADDING_CSS + "</style>", 1)
        new_html = COMPACT_RE.sub("", new_html)
        new_html = new_html.replace("</style>", A5_COMPACT_CSS + "</style>", 1)
        if new_html != html:
            path.write_text(new_html, encoding="utf-8", newline="")
            changed.append(path.name)

    print(f"Updated {len(changed)} files:")
    for name in changed:
        print(f"  {name}")


if __name__ == "__main__":
    main()
