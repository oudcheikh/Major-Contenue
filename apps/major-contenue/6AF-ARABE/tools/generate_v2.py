import json, sys
sys.stdout.reconfigure(encoding='utf-8')

qr = json.load(open('C:/Users/PC/Documents/Major-Contenue/6AF-ARABE/qr_data.json'))
AR = '#7c3aed'
IS = '#059669'

# ── Major logo (4 tiles: +, e^x, flask, DNA) ───────────────────
def major_logo(size=30):
    b = '#4D6EF5'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">
  <rect x="2" y="2" width="44" height="44" rx="10" fill="{b}"/>
  <line x1="24" y1="11" x2="24" y2="37" stroke="white" stroke-width="9" stroke-linecap="round"/>
  <line x1="11" y1="24" x2="37" y2="24" stroke="white" stroke-width="9" stroke-linecap="round"/>
  <rect x="54" y="2" width="44" height="44" rx="10" fill="{b}"/>
  <text x="57" y="42" font-family="Georgia,serif" font-size="29" fill="white" font-style="italic">e</text>
  <text x="80" y="25" font-family="Georgia,serif" font-size="17" fill="white" font-style="italic">x</text>
  <rect x="2" y="54" width="44" height="44" rx="10" fill="{b}"/>
  <path d="M20 63 L20 73 L12 87 Q11 92 15 93 L33 93 Q37 92 36 87 L28 73 L28 63 Z" fill="white"/>
  <rect x="18" y="60" width="12" height="5" rx="2.5" fill="{b}"/>
  <circle cx="19.5" cy="86" r="2.5" fill="{b}" opacity=".75"/>
  <circle cx="25" cy="82" r="2" fill="{b}" opacity=".75"/>
  <rect x="54" y="54" width="44" height="44" rx="10" fill="{b}"/>
  <path d="M71 60 C83 65 67 72 79 77 C91 82 67 89 79 95" stroke="white" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M81 60 C69 65 85 72 73 77 C61 82 85 89 73 95" stroke="white" stroke-width="3" fill="none" stroke-linecap="round"/>
  <line x1="73" y1="63" x2="79" y2="63" stroke="white" stroke-width="2.5"/>
  <line x1="71" y1="68" x2="81" y2="68" stroke="white" stroke-width="2.5"/>
  <line x1="73" y1="73" x2="79" y2="73" stroke="white" stroke-width="2.5"/>
  <line x1="74" y1="77" x2="78" y2="77" stroke="white" stroke-width="2.5"/>
  <line x1="73" y1="81" x2="79" y2="81" stroke="white" stroke-width="2.5"/>
  <line x1="71" y1="86" x2="81" y2="86" stroke="white" stroke-width="2.5"/>
  <line x1="73" y1="91" x2="79" y2="91" stroke="white" stroke-width="2.5"/>
</svg>'''

# ── SVG mascot (camel) ──────────────────────────────────────────
def camel(size=38):
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 38 38" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="19" cy="26" rx="13" ry="8" fill="#FCD34D" stroke="#D97706" stroke-width="1.5"/>
  <path d="M13 20 Q15 10 19 13 Q23 10 25 20" fill="#FCD34D" stroke="#D97706" stroke-width="1.5"/>
  <ellipse cx="29" cy="18" rx="5" ry="4" fill="#FCD34D" stroke="#D97706" stroke-width="1.5"/>
  <path d="M24.5 20 L28.5 15" stroke="#D97706" stroke-width="1.5" stroke-linecap="round"/>
  <circle cx="30.5" cy="16.5" r="1.2" fill="#1e293b"/>
  <path d="M28 19.5 Q30 21.5 32 19.5" stroke="#92400e" stroke-width="0.9" fill="none"/>
  <line x1="10" y1="32" x2="9" y2="38" stroke="#D97706" stroke-width="2" stroke-linecap="round"/>
  <line x1="15" y1="33.5" x2="14" y2="38" stroke="#D97706" stroke-width="2" stroke-linecap="round"/>
  <line x1="22" y1="33.5" x2="21" y2="38" stroke="#D97706" stroke-width="2" stroke-linecap="round"/>
  <line x1="27" y1="32" x2="28" y2="38" stroke="#D97706" stroke-width="2" stroke-linecap="round"/>
</svg>'''

# ── SVG student reading (for Arabic pages) ─────────────────────
def student_read(color):
    return f'''<svg width="56" height="56" viewBox="0 0 56 56" fill="none">
  <circle cx="28" cy="14" r="9" fill="#FBBF24" stroke="#D97706" stroke-width="1.2"/>
  <ellipse cx="28" cy="14" rx="4" ry="5" fill="#92400e" opacity=".6"/>
  <rect x="16" y="22" width="24" height="18" rx="4" fill="#60A5FA" stroke="#2563EB" stroke-width="1.2"/>
  <rect x="20" y="24" width="8" height="12" rx="2" fill="#FDE68A" stroke="#D97706" stroke-width="1"/>
  <line x1="21" y1="27" x2="27" y2="27" stroke="{color}" stroke-width="1"/>
  <line x1="21" y1="30" x2="27" y2="30" stroke="{color}" stroke-width="1"/>
  <line x1="21" y1="33" x2="25" y2="33" stroke="{color}" stroke-width="1"/>
  <rect x="28" y="24" width="9" height="12" rx="2" fill="#FDE68A" stroke="#D97706" stroke-width="1"/>
  <path d="M16 26 Q10 30 12 38" stroke="#FBBF24" stroke-width="2" stroke-linecap="round" fill="none"/>
  <path d="M40 26 Q46 30 44 38" stroke="#FBBF24" stroke-width="2" stroke-linecap="round" fill="none"/>
  <path d="M20 40 Q28 50 36 40" stroke="#3B82F6" stroke-width="2" stroke-linecap="round" fill="none"/>
</svg>'''

# ── SVG student writing (for exercise sections) ─────────────────
def student_write(color):
    return f'''<svg width="56" height="56" viewBox="0 0 56 56" fill="none">
  <circle cx="22" cy="12" r="8" fill="#FCD34D" stroke="#D97706" stroke-width="1.2"/>
  <ellipse cx="21" cy="11" rx="3" ry="4" fill="#92400e" opacity=".5"/>
  <rect x="12" y="19" width="20" height="16" rx="4" fill="#34D399" stroke="#059669" stroke-width="1.2"/>
  <rect x="30" y="28" width="18" height="12" rx="3" fill="#F3F4F6" stroke="#D1D5DB" stroke-width="1"/>
  <line x1="32" y1="32" x2="46" y2="32" stroke="#9CA3AF" stroke-width="1"/>
  <line x1="32" y1="35" x2="44" y2="35" stroke="#9CA3AF" stroke-width="1"/>
  <path d="M28 24 L36 28" stroke="#FCD34D" stroke-width="2" stroke-linecap="round"/>
  <path d="M43 26 L47 22 L49 24 L45 28 Z" fill="{color}" opacity=".8"/>
  <path d="M13 35 Q8 40 10 46" stroke="#FCD34D" stroke-width="2" stroke-linecap="round" fill="none"/>
  <path d="M32 35 Q35 42 30 46" stroke="#34D399" stroke-width="2" stroke-linecap="round" fill="none"/>
</svg>'''

# ── SVG book (alias for Arabic page headers) ────────────────────
def book_svg(color, size=28):
    return student_read(color)

# ── SVG mosque header ───────────────────────────────────────────
def mosque_svg(color, size=28):
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 28 28" fill="none">
  <path d="M14 3 Q16 7 18 8 L18 24 L10 24 L10 8 Q12 7 14 3Z" fill="{color}" opacity=".2" stroke="{color}" stroke-width="1.2"/>
  <path d="M12.5 3 Q14 1 15.5 3" stroke="{color}" stroke-width="1.2" fill="none"/>
  <circle cx="14" cy="2.5" r="1" fill="{color}" opacity=".7"/>
  <rect x="5" y="14" width="5" height="10" rx="1.5" fill="{color}" opacity=".15" stroke="{color}" stroke-width="1"/>
  <rect x="18" y="14" width="5" height="10" rx="1.5" fill="{color}" opacity=".15" stroke="{color}" stroke-width="1"/>
  <rect x="12" y="17" width="4" height="7" rx="2" fill="{color}" opacity=".3" stroke="{color}" stroke-width="1"/>
  <line x1="3" y1="24" x2="25" y2="24" stroke="{color}" stroke-width="1.5"/>
</svg>'''

# ── Decorative blobs (corner deco) ─────────────────────────────
def blobs(color):
    c1 = color + '18'
    c2 = color + '10'
    return f'''<div class="blob-wrap">
  <svg class="blob-tl" width="90" height="90" viewBox="0 0 90 90"><ellipse cx="30" cy="60" rx="40" ry="32" fill="{c1}" transform="rotate(-30 30 60)"/><circle cx="70" cy="20" r="18" fill="{c2}"/></svg>
  <svg class="blob-br" width="80" height="70" viewBox="0 0 80 70"><ellipse cx="55" cy="40" rx="36" ry="28" fill="{c1}" transform="rotate(20 55 40)"/></svg>
</div>'''

# ── Wave footer ──────────────────────────────────────────────────
def wave_footer(color):
    c = color + 'cc'
    c2 = color + '55'
    return f'''<div class="wave-footer"><svg viewBox="0 0 210 18" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 10 Q26 2 52 10 Q78 18 104 10 Q130 2 156 10 Q182 18 210 10 L210 18 L0 18 Z" fill="{c}"/>
  <path d="M0 13 Q26 6 52 13 Q78 20 104 13 Q130 6 156 13 Q182 20 210 13 L210 18 L0 18 Z" fill="{c2}"/>
</svg></div>'''

# ── Section pill label (j'apprend / je m'entraine style) ────────
def sec_pill(label, color, char_svg=''):
    return f'<div class="sec-pill-wrap"><div class="sec-pill" style="background:{color}">{label}</div>{char_svg}</div>'

# ── Hint box (mascot tip) ───────────────────────────────────────
def hint(text, color):
    bg = '#fefce8' if color == AR else '#f0fdf4'
    bc = '#fde68a' if color == AR else '#a7f3d0'
    return f'<div class="hint-box" style="background:{bg};border-color:{bc}"><span class="hint-camel">{camel(24)}</span><span class="hint-text">{text}</span></div>'

# ── QR strip (dashed border like math.pdf) ──────────────────────
def qi(code, color):
    src = qr.get(code, '')
    return f'<img src="{src}" style="width:65px;height:65px;border-radius:6px" alt="{code}"/>'

def qr_strip(code, color):
    tc = '#4c1d95' if color == AR else '#065f46'
    return f'''<div class="qr-strip" style="border-color:{color}">
  <div class="qr-img-wrap">{qi(code,color)}</div>
  <div class="qr-text" style="color:{tc}">
    <strong>&#128247; صوِّر إجابتك للتصحيح الفوري</strong>
    امسح الرمز بهاتفك &larr; Major يُصحح ويُشخّص أخطاءك فوراً
    <span style="font-size:9px;color:#9ca3af;display:block">{code}</span>
  </div>
</div>'''

# ── Line helpers ─────────────────────────────────────────────────
def lines(n, solid=False):
    cls = 'answer-line solid' if solid else 'answer-line'
    return '<div class="answer-lines">' + f'<div class="{cls}"></div>' * n + '</div>'

def labeled_lines(items, color):
    out = '<div class="labeled-lines">'
    for label, n in items:
        out += f'<div class="ll-label" style="color:{color}">{label}</div>'
        out += '<div class="answer-line"></div>' * n
    out += '</div>'
    return out

def fill_grid(items, color):
    out = '<div class="fill-grid">'
    for idx, word, _ in items:
        out += f'<div class="fill-item"><span class="fill-index" style="color:{color}">{idx}</span><span class="fill-word">{word}</span><span class="fill-arrow">&#8592;</span><div class="fill-answer-line"></div></div>'
    out += '</div>'
    return out

def word_bank(words, color):
    tags = ''.join(f'<span class="bank-word" style="border-color:{color}66">{w}</span>' for w in words)
    return f'<div class="word-bank" style="background:{color}08;border-color:{color}44"><span class="bank-label" style="color:{color}">المفردات :</span><div class="bank-words">{tags}</div></div>'

def qcm_item(num, question, choices, color):
    chs = ''.join(f'<div class="choice-btn" style="border-color:{color}22;background:{color}06">{c}</div>' for c in choices)
    return f'<div class="qcm-item"><div class="qcm-q"><span class="qcm-num" style="color:{color}">{num}.</span> {question}</div><div class="qcm-choices">{chs}</div></div>'

def tf_item(question, color):
    return f'<div class="tf-item" style="border-color:{color}22;background:{color}06"><span class="tf-text">{question}</span><div class="tf-box" style="border-color:{color}"></div></div>'

def tbl(headers, rows, color):
    ths = ''.join(f'<th style="background:{color}">{h}</th>' for h in headers)
    trs = ''
    for row in rows:
        tds = ''
        for cell in row:
            if cell.startswith('__'):
                tds += '<td class="answer-cell"></td>'
            else:
                tds += f'<td class="word-cell">{cell}</td>'
        trs += f'<tr>{tds}</tr>'
    return f'<table class="ex-table"><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>'

def example_box(text, color):
    bg = '#f5f3ff' if color == AR else '#f0fdf4'
    bc = '#c4b5fd' if color == AR else '#6ee7b7'
    tc = '#5b21b6' if color == AR else '#065f46'
    return f'<div class="exo-example" style="background:{bg};border-color:{bc};color:{tc}"><span class="ex-label" style="background:{color}">مثال</span>{text}</div>'

def reading(title, paragraphs, color=AR):
    ps = ''.join(f'<p>{p}</p>' for p in paragraphs)
    bc = '#ddd6fe' if color == AR else '#a7f3d0'
    return f'<div class="reading-box" style="border-color:{bc}"><p class="reading-title" style="color:{color}">&#128214; {title}</p>{ps}</div>'

# ── Page header ─────────────────────────────────────────────────
def page_hdr(svg_icon, sub, color):
    return f'''{blobs(color)}
<div class="page-header" style="border-color:{color}">
  <div class="brand-wrap">
    <div class="brand-svg">{svg_icon}</div>
    <div>
      <div style="display:flex;align-items:center;gap:5px;margin-bottom:1px">{major_logo(26)}<span class="brand-name" style="color:{color}">Major 6AF</span></div>
      <div class="brand-sub">{sub}</div>
    </div>
  </div>
</div>
<div class="student-bar">
  <div class="info-field"><span class="fl">الاسم :</span><div class="fl-line"></div></div>
  <div class="info-field"><span class="fl">القسم :</span><div class="fl-line"></div></div>
  <div class="info-field"><span class="fl">المدرسة :</span><div class="fl-line"></div></div>
</div>'''

# ── Section pill header (j'apprend / je m'entraine style) ────────
def sec(title, color, icon='&#9998;', char=''):
    return f'''<div class="sec-pill-wrap">
  <div class="sec-pill" style="background:{color}">{icon} {title}</div>
  {char}
</div>'''

# ── Exercise card (circle+arrow badge like math.pdf) ─────────────
def exo(num, level, pts, instr, verb, content, color, tip_text=''):
    lmap = {
        '1': ('&#11088; سهل', 'level-easy'),
        '2': ('&#11088;&#11088; متوسط', 'level-medium'),
        '3': ('&#11088;&#11088;&#11088; صعب', 'level-hard')
    }
    l, lc = lmap.get(str(level), ('&#11088;&#11088; متوسط', 'level-medium'))
    tip_html = f'<div class="exo-tip" style="color:{color}">{camel(18)} <span>{tip_text}</span></div>' if tip_text else ''
    return f'''<div class="exo-card">
  <div class="major-corner">{major_logo(18)}</div>
  <div class="exo-head">
    <div class="exo-num-wrap">
      <span class="exo-circle" style="background:{color}">{num}</span>
      <span class="exo-arrow" style="color:{color}">&#9658;</span>
      <span class="exo-level {lc}">{l}</span>
    </div>
    <span class="exo-pts">{pts} نقاط</span>
  </div>
  <div class="exo-instr"><span class="exo-verb" style="color:{color}">{verb}</span> {instr}</div>
  {tip_html}{content}
</div>'''

# ══════════════════════════════════════════════════════════════════
CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Cairo','Tahoma',sans-serif;background:#d8cce8;color:#0f172a;direction:rtl}
.page{width:210mm;min-height:297mm;margin:16px auto;background:#fdf8f0;padding:9mm 11mm 20mm;box-shadow:0 6px 36px rgba(0,0,0,.18);position:relative;overflow:hidden}
@media print{
  body{background:#fff}
  .page{margin:0;box-shadow:none;page-break-after:always;page-break-inside:avoid;height:297mm;overflow:hidden;padding:6mm 9mm 16mm}
  .no-print{display:none!important}
  @page{size:A4;margin:0}
  .answer-line{height:20px!important;margin-bottom:2px!important}
  .exo-card{padding:6px 10px 5px!important;margin-bottom:5px!important}
  .fill-item{min-height:24px!important}
  .answer-cell{height:22px!important}
  .exo-instr{font-size:10.5px!important}
  .fill-word{font-size:11px!important}
  .reading-box{font-size:10.5px!important;line-height:1.65!important;padding:7px 11px!important}
  .sec-pill-wrap{margin:6px 0 5px!important}
  .grid2{gap:6px!important}
  .hint-box{padding:3px 8px!important;margin-bottom:4px!important}
  .student-bar{margin-bottom:7px!important}
  .page-header{padding-bottom:6px!important;margin-bottom:7px!important}
  .qr-strip{padding:5px 10px!important;margin-top:5px!important}
  .word-bank{padding:4px 9px!important;margin-bottom:5px!important}
  .exo-head{margin-bottom:5px!important}
  .exo-example{padding:4px 9px!important;margin-bottom:5px!important}
  .wave-footer svg{height:14px!important}
  .blob-wrap{display:none}
}
/* ── Page header ── */
.page-header{display:flex;align-items:center;justify-content:space-between;border-bottom:3px solid;padding-bottom:7px;margin-bottom:8px;gap:8px}
.brand-wrap{display:flex;align-items:center;gap:8px}
.brand-svg{flex-shrink:0}
.brand-name{font-size:15px;font-weight:900;line-height:1.1}
.brand-sub{font-size:9px;color:#64748b;font-weight:600}
.student-bar{display:grid;grid-template-columns:1fr 1fr 1fr;gap:7px;margin-bottom:8px}
.info-field{display:flex;align-items:center;gap:5px;border-bottom:1.5px solid #334155;padding:1px 4px}
.fl{font-size:9.5px;font-weight:900;color:#475569;white-space:nowrap;flex-shrink:0}
.fl-line{flex:1;min-height:15px}
/* ── Section pill (j'apprend style) ── */
.sec-pill-wrap{display:flex;align-items:center;gap:10px;margin:9px 0 7px}
.sec-pill{font-size:13px;font-weight:900;font-style:italic;color:#fff;padding:5px 20px;border-radius:999px;letter-spacing:.5px;box-shadow:0 3px 10px rgba(0,0,0,.2)}
/* ── Exercise card ── */
.exo-card{background:#fff;border-radius:16px;padding:9px 12px 8px;margin-bottom:7px;break-inside:avoid;position:relative;box-shadow:0 2px 10px rgba(0,0,0,.08)}
.major-corner{position:absolute;bottom:7px;left:8px;opacity:.28;pointer-events:none;user-select:none;line-height:0}
.exo-head{display:flex;flex-direction:row-reverse;justify-content:space-between;align-items:center;margin-bottom:6px}
.exo-num-wrap{display:flex;align-items:center;gap:6px}
/* circle + arrow badge like math.pdf */
.exo-circle{width:28px;height:28px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:12px;font-weight:900;color:#fff;flex-shrink:0}
.exo-arrow{display:inline-block;font-size:14px;font-weight:900;margin-right:4px}
.exo-level{font-size:8.5px;font-weight:900;padding:2px 9px;border-radius:999px}
.level-easy{background:#f0fdf4;color:#15803d}
.level-medium{background:#fffbeb;color:#b45309}
.level-hard{background:#fef2f2;color:#b91c1c}
.exo-pts{font-size:9.5px;font-weight:900;color:#94a3b8}
.exo-instr{font-size:11.5px;font-weight:700;line-height:1.65;color:#1e293b;margin-bottom:7px}
.exo-verb{font-weight:900;text-decoration:underline;text-decoration-style:wavy;margin-left:3px}
.exo-tip{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:700;margin-bottom:5px;opacity:.85}
.exo-example{border:1.5px dashed;border-radius:9px;padding:5px 10px;margin-bottom:6px;font-size:10.5px;font-weight:600;display:flex;align-items:center;gap:7px;flex-wrap:wrap}
.ex-label{font-size:9px;font-weight:900;color:#fff;border-radius:5px;padding:2px 7px;flex-shrink:0}
/* ── Hint box ── */
.hint-box{display:flex;align-items:center;gap:7px;border:1.5px solid;border-radius:10px;padding:5px 9px;margin-bottom:6px;font-size:9.5px;font-weight:700}
.hint-camel{flex-shrink:0}
.hint-text{line-height:1.5;opacity:.9}
/* ── Answer lines ── */
.answer-lines{margin-top:3px}
.labeled-lines{margin-top:3px}
.ll-label{font-size:9.5px;font-weight:900;margin:5px 0 2px}
.answer-line{height:26px;border-bottom:1.8px dashed #cbd5e1;margin-bottom:4px}
.answer-line.solid{border-bottom-style:solid;border-bottom-color:#94a3b8}
/* ── Fill grid ── */
.fill-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:4px}
.fill-item{background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:9px;padding:4px 9px;display:flex;align-items:center;gap:6px;min-height:30px}
.fill-index{font-size:9px;font-weight:900;flex-shrink:0;min-width:12px}
.fill-word{font-size:11.5px;font-weight:800;flex-shrink:0;max-width:110px}
.fill-arrow{font-size:10px;color:#94a3b8;flex-shrink:0}
.fill-answer-line{flex:1;height:20px;border-bottom:1.8px dashed #94a3b8}
/* ── Word bank ── */
.word-bank{border:1.5px dashed;border-radius:9px;padding:5px 11px;margin-bottom:7px;display:flex;align-items:center;gap:7px;flex-wrap:wrap;background:#fff}
.bank-label{font-size:9.5px;font-weight:900;white-space:nowrap}
.bank-words{display:flex;gap:6px;flex-wrap:wrap;flex:1;justify-content:flex-end}
.bank-word{background:#fff;border:1.5px solid;border-radius:7px;padding:2px 9px;font-size:11.5px;font-weight:700;color:#1e293b}
/* ── Table ── */
.ex-table{width:100%;border-collapse:collapse;margin-top:5px;font-size:10.5px}
.ex-table th{color:#fff;padding:5px 8px;font-weight:900;font-size:9.5px;border:1px solid rgba(0,0,0,.15)}
.ex-table td{padding:0;border:1px solid #e2e8f0;vertical-align:middle}
.ex-table td.word-cell{padding:5px 8px;font-weight:700;background:#f8fafc}
.ex-table td.answer-cell{height:28px}
.ex-table tr:nth-child(even) td.word-cell{background:#f1f5f9}
/* ── QCM / TF ── */
.qcm-item{margin-bottom:8px}
.qcm-q{font-size:11px;font-weight:700;margin-bottom:4px;line-height:1.55}
.qcm-num{font-weight:900;margin-left:3px}
.qcm-choices{display:grid;grid-template-columns:1fr 1fr;gap:4px;padding-right:10px}
.choice-btn{border:1.5px solid;border-radius:9px;padding:4px 10px;font-size:10.5px;font-weight:700;background:#fff}
.tf-item{display:flex;align-items:center;justify-content:space-between;border:1.5px solid;border-radius:9px;padding:6px 10px;margin-bottom:5px;font-size:11px;font-weight:700;background:#fff}
.tf-box{border:2px solid;width:22px;height:22px;border-radius:6px;flex-shrink:0;background:#fff}
/* ── QR strip (dashed like math.pdf) ── */
.qr-strip{display:flex;align-items:center;gap:10px;border:2.5px dashed;border-radius:16px;padding:7px 14px;margin-top:7px;background:#fff}
.qr-img-wrap{flex-shrink:0;background:#fff;border-radius:6px;padding:2px}
.qr-text{font-size:10px;font-weight:700;line-height:1.6}
.qr-text strong{font-size:11px;font-weight:900;display:block}
/* ── Reading ── */
.reading-box{background:#fff;border:1.5px solid;border-radius:14px;padding:10px 14px;margin-bottom:8px;font-size:11.5px;font-weight:600;line-height:1.85;direction:rtl;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.reading-title{font-size:13px;font-weight:900;margin-bottom:5px}
.reading-box p{margin-bottom:3px}
.writing-area{border:1.5px solid #e2e8f0;border-radius:9px;background:#fff;padding:6px 10px}
.writing-area .answer-line{border-bottom-color:#e2e8f0}
/* ── Grid ── */
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:8px}
/* ── Wave footer ── */
.wave-footer{position:absolute;bottom:0;left:0;right:0;line-height:0}
.wave-footer svg{width:100%;height:18px;display:block}
/* ── Blobs ── */
.blob-wrap{position:absolute;top:0;left:0;right:0;bottom:0;pointer-events:none;overflow:hidden}
.blob-tl{position:absolute;top:-15px;right:-15px}
.blob-br{position:absolute;bottom:18px;left:-10px}
/* ── Page num ── */
.page-num{position:absolute;bottom:6mm;left:50%;transform:translateX(-50%);font-size:9.5px;font-weight:700;color:rgba(255,255,255,.8)}
/* ── Print button ── */
.print-btn{position:fixed;bottom:24px;left:24px;background:linear-gradient(135deg,#7c3aed,#6d28d9);color:#fff;border:none;border-radius:50px;padding:12px 24px;font-family:'Cairo',sans-serif;font-size:14px;font-weight:900;cursor:pointer;box-shadow:0 8px 24px rgba(124,58,237,.4);z-index:99}
"""

# ══════════════════════════════════════════════════════════════════
#  COVER
# ══════════════════════════════════════════════════════════════════
cover = f"""
<div class="page" style="display:flex;flex-direction:column;align-items:center;justify-content:center;background:linear-gradient(160deg,#1e0a4a 0%,#4c1d95 40%,#7c3aed 70%,#a78bfa 100%)">
  <div style="text-align:center;color:#fff;padding:20px">
    <div style="font-size:70px;margin-bottom:10px">{camel(70)}</div>
    <div style="font-size:13px;font-weight:900;letter-spacing:3px;opacity:.7;margin-bottom:8px">MAJOR 6AF &mdash; موريتانيا</div>
    <h1 style="font-size:48px;font-weight:900;line-height:1;margin-bottom:6px">دفتر ماجور</h1>
    <div style="font-size:17px;font-weight:700;color:#fde68a;margin-bottom:20px">اللغة العربية &nbsp;&#183;&nbsp; التربية الإسلامية</div>
    <div style="display:flex;justify-content:center;gap:12px;margin-bottom:20px;flex-wrap:wrap">
      <span style="background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.3);border-radius:999px;padding:5px 18px;font-size:13px;font-weight:800">السنة السادسة الأساسية</span>
      <span style="background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.3);border-radius:999px;padding:5px 18px;font-size:13px;font-weight:800">&#129504; تحضير المسابقة الوطنية</span>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;max-width:360px;margin:0 auto 22px;text-align:right">
      <div style="background:rgba(255,255,255,.1);border-radius:14px;padding:12px 16px;border:1px solid rgba(255,255,255,.2)">
        <div style="font-size:11px;opacity:.7;font-weight:700;margin-bottom:4px">&#128331; اللغة العربية</div>
        <div style="font-size:14px;font-weight:900">١٥ صفحة &nbsp;&#183;&nbsp; ٩٠+ تمريناً</div>
      </div>
      <div style="background:rgba(255,255,255,.1);border-radius:14px;padding:12px 16px;border:1px solid rgba(255,255,255,.2)">
        <div style="font-size:11px;opacity:.7;font-weight:700;margin-bottom:4px">&#9770; التربية الإسلامية</div>
        <div style="font-size:14px;font-weight:900">٧ صفحات &nbsp;&#183;&nbsp; ٤٥+ تمريناً</div>
      </div>
    </div>
    <div style="background:rgba(253,230,138,.15);border:1px solid rgba(253,230,138,.4);border-radius:14px;padding:10px 16px;font-size:11.5px;font-weight:700;color:#fde68a;max-width:360px;margin:0 auto">
      &#128241; كل تمرين مرتبط بـQR Code<br>
      <span style="font-size:10px;opacity:.85">امسح الرمز للتصحيح الفوري بالذكاء الاصطناعي</span>
    </div>
  </div>
  <div style="position:absolute;bottom:12mm;color:rgba(255,255,255,.5);font-size:10px;font-weight:700">major-eval.vercel.app</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 1 — النحو : المبتدأ والخبر والفاعل والمفعول به
# ══════════════════════════════════════════════════════════════════
p1 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; النحو : المبتدأ والخبر والفاعل والمفعول به', AR)}
{sec('المبتدأ والخبر', AR)}
<div class="grid2">
{exo('تمرين 1','1','4','كل كلمة مشدّدة : هي مبتدأ أم خبر ؟','حدِّد',
  example_box('<strong>الطالبُ</strong> مجتهدٌ : مبتدأ &nbsp;|&nbsp; الدرسُ <strong>مفيدٌ</strong> : خبر', AR)+
  fill_grid([('1','<strong>المدرسةُ</strong> واسعةٌ',1),('2','الأبُ <strong>كريمٌ</strong>',1),('3','<strong>الكتابُ</strong> جديدٌ',1),('4','التلميذُ <strong>مجتهدٌ</strong>',1),('5','<strong>الجوُّ</strong> بارِدٌ',1),('6','النهرُ <strong>طويلٌ</strong>',1)], AR), AR)}
{exo('تمرين 2','1','4','الجدول بمبتدأ مناسب أو خبر مناسب :','أكمل',
  tbl(['المبتدأ','الخبر'],
    [['___','مجتهدٌ'],['الطقسُ','___'],['___','حلوةٌ'],['الوطنُ','___'],['___','واسعةٌ'],['القمرُ','___']], AR), AR)}
</div>
{sec('الفاعل والمفعول به', AR)}
<div class="grid2">
{exo('تمرين 3','2','4','الفاعل ثم المفعول به في كل جملة :','استخرج',
  fill_grid([('1','يقرأُ الطالبُ الكتابَ',1),('2','تعلّمَ أحمدُ الدرسَ',1),('3','فتحَ المعلمُ النافذةَ',1),('4','تأكلُ فاطمةُ التفاحةَ',1),('5','يكتبُ التلميذُ الواجبَ',1),('6','رأيتُ الطائرَ يغرّد',1)], AR), AR)}
{exo('تمرين 4','2','4','الجملة بفاعل ومفعول به مناسبين :','أكمل',
  labeled_lines([('يشربُ ________ ________',1),('كتبَ ________ ________',1),('يُحبُّ ________ ________',1),('يحمِلُ ________ ________',1)], AR), AR)}
</div>
{exo('تمرين 5','3','4','جملة فعلية مفيدة تشتمل على : فعل + فاعل + مفعول به + حرف جر :','ركِّب',
  '<div class="writing-area">'+'<div class="answer-line"></div>'*2+'</div>', AR,
  tip_text='الجملة الفعلية تبدأ دائماً بالفعل')}
{qr_strip('AR-01', AR)}
{wave_footer(AR)}<div class="page-num">1 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 2 — النحو : الإعراب وعلاماته وحروف الجر
# ══════════════════════════════════════════════════════════════════
p2 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; النحو : الإعراب وحروف الجر', AR)}
{sec('علامات الإعراب', AR)}
<div class="grid2">
{exo('تمرين 1','1','3','علامة الإعراب المناسبة (ضمة / فتحة / كسرة / سكون) :','ضع',
  example_box('جاءَ <strong>المعلمُ</strong> (ضمة) &nbsp;|&nbsp; رأيتُ <strong>المعلمَ</strong> (فتحة) &nbsp;|&nbsp; سلّمتُ على <strong>المعلمِ</strong> (كسرة)', AR)+
  fill_grid([('1','ذهبَ الولدُ__ إلى المدرسة',1),('2','رأيتُ الولدَ__ في الملعب',1),('3','لعبَ مع الولدِ__',1),('4','يكتبُ المعلمُ__ الدرسَ__',1),('5','أعطيتُ الكتابَ__ للطالبِ__',1),('6','لم يذهبْ__ التلميذُ__',1)], AR), AR)}
{exo('تمرين 2','1','3','أنواع الجمل (اسمية / فعلية) :','صنِّف',
  fill_grid([('1','الطالبُ يدرسُ',1),('2','يلعبُ الأطفالُ',1),('3','الجوُّ جميلٌ',1),('4','كتبَ أحمدُ الواجبَ',1),('5','المدرسةُ قريبةٌ',1),('6','يُحبُّ الولدُ أمَّهُ',1)], AR), AR)}
</div>
{sec('حروف الجر والأسماء المجرورة', AR)}
<div class="grid2">
{exo('تمرين 3','2','4','حرف الجر المناسب (في / من / إلى / على / عن / مع / الباء / اللام) :','أكمل',
  fill_grid([('1','ذهبتُ ___ المدرسةِ',1),('2','خرجَ ___ البيتِ',1),('3','الكتابُ ___ الطاولةِ',1),('4','تحدّثنا ___ الدرسِ',1),('5','كتبَ ___ القلمِ',1),('6','هذا ___ الوطنِ',1)], AR), AR)}
{exo('تمرين 4','2','4','الاسم المجرور وسبب جره :','استخرج',
  tbl(['الجملة','الاسم المجرور','سبب الجر'],
    [['ذهبتُ إلى المدرسةِ','__','__'],['الكتابُ على الطاولةِ','__','__'],['جاءَ مع أبيهِ','__','__'],['يتعلمُ في المدينةِ','__','__']], AR), AR)}
</div>
{exo('تمرين 5','3','4','هذه الجملة إعراباً تاماً : "يقرأُ الطالبُ الكتابَ في الفصلِ"','أعرب',
  tbl(['الكلمة','نوعها','علامة إعرابه وسببها'],
    [['يقرأُ','فعل مضارع','__'],['الطالبُ','__','__'],['الكتابَ','__','__'],['في الفصلِ','__','__']], AR),
  AR, tip_text='الفعل المضارع يُرفع بالضمة إذا لم يسبقه ناصب أو جازم')}
{qr_strip('AR-02', AR)}
{wave_footer(AR)}<div class="page-num">2 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 3 — الإملاء : الهمزات
# ══════════════════════════════════════════════════════════════════
p3 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; الإملاء : الهمزات', AR)}
{sec('همزة الوصل وهمزة القطع', AR)}
<div class="grid2">
{exo('تمرين 1','1','4','همزة الوصل (ا) أو همزة القطع (أ/إ) :','ضع',
  example_box('__بن &#8592; <strong>ا</strong>بن (وصل) &nbsp;|&nbsp; __كلَ &#8592; <strong>أ</strong>كلَ (قطع)', AR)+
  fill_grid([('1','__ستاذ',1),('2','__نطلقَ',1),('3','__حمد',1),('4','__لطالب',1),('5','__كتاب',1),('6','__يمان',1),('7','__نتَ',1),('8','__ستمعَ',1)], AR), AR,
  tip_text='همزة الوصل تسقط في وسط الكلام. تجد همزة الوصل في: ال، افتعل، انفعل، استفعل، وأسماء: ابن، اسم، امرأة...')}
{exo('تمرين 2','2','3','الكلمات بهمزة القطع في الأفعال :','صحِّح',
  fill_grid([('1','استيقظَ &#8594;',1),('2','اكلَ &#8594;',1),('3','احمد &#8594;',1),('4','اعطى &#8594;',1),('5','اسرعَ &#8594;',1),('6','اختارَ &#8594;',1)], AR), AR)}
</div>
{sec('الهمزة المتوسطة والمتطرفة', AR)}
<div class="grid2">
{exo('تمرين 3','2','4','الهمزة الصحيحة (أ / ؤ / ئ / ء) حسب حركتها وحركة ما قبلها :','اكتب',
  example_box('سَ__ل : حركة الهمزة فتحة + قبلها فتحة &rarr; <strong>سَأَل</strong>', AR)+
  fill_grid([('1','مَ__مور',1),('2','بِ__ر',1),('3','سُ__ال',1),('4','يَ__كُل',1),('5','فُ__اد',1),('6','شَ__ن',1),('7','رَ__يس',1),('8','مسْ__ول',1)], AR), AR)}
{exo('تمرين 4','2','3','الأخطاء الإملائية في الهمزة :','صحِّح',
  fill_grid([('1','مأكول &#8594;',1),('2','رئيس &#8594; ر_يس',1),('3','سأل (بالواو) &#8594;',1),('4','يأكل &#8594; يؤكل',1),('5','فؤاد (بالسطر) &#8594;',1),('6','بئر (بالواو) &#8594;',1)], AR), AR)}
</div>
{exo('تمرين 5','2','4','الجمل بالتشكيل الكامل مع ضبط الهمزات :','اكتب',
  fill_grid([('1','سأل الطالب',1),('2','المؤمن صادق',1),('3','قرأتُ كتاباً',1),('4','الرئيس عادل',1),('5','يأكل الخبز',1),('6','بئر عميقة',1)], AR), AR,
  tip_text='الهمزة المتطرفة تُكتب على حرف يناسب حركة ما قبلها')}
{qr_strip('AR-03', AR)}
{wave_footer(AR)}<div class="page-num">8 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 4 — الإملاء : التاء والألف والتشكيل
# ══════════════════════════════════════════════════════════════════
p4 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; الإملاء : التاء والألف والتشكيل', AR)}
{sec('التاء المربوطة والتاء المفتوحة', AR)}
<div class="grid2">
{exo('تمرين 1','1','4','(ة) أو (ت) في آخر كل كلمة :','ضع',
  example_box('فاطم__ : <strong>ة</strong> (مؤنث) &nbsp;|&nbsp; كتب__ : <strong>ت</strong> (فعل ماضٍ)', AR)+
  fill_grid([('1','مدرس__',1),('2','كتب__',1),('3','ذهب__',1),('4','فاطم__',1),('5','قرأ__',1),('6','حديق__',1),('7','رأي__',1),('8','شجر__',1)], AR), AR,
  tip_text='التاء المربوطة تُلفظ هاء عند الوقف. التاء المفتوحة تبقى تاءً.')}
{exo('تمرين 2','2','3','الجمل الخاطئة التاء :','صحِّح',
  fill_grid([('1','الطالبة رجعت &#8594;',1),('2','البنت قرأة &#8594;',1),('3','فاطمت مجتهدة &#8594;',1),('4','مكتبت المدرسة &#8594;',1),('5','ذهبة إلى البيت &#8594;',1),('6','الحديقت جميلة &#8594;',1)], AR), AR)}
</div>
{sec('الألف المقصورة والممدودة', AR)}
<div class="grid2">
{exo('تمرين 3','2','4','بالألف المناسبة : (ى) مقصورة أو (ا) ممدودة :','أكمل',
  example_box('مشَـ__ : <strong>مشى</strong> (مقصورة) &nbsp;|&nbsp; سمَـ__ : <strong>سماء</strong> (ممدودة)', AR)+
  fill_grid([('1','عيسَـ__',1),('2','رجَـ__',1),('3','فتَـ__',1),('4','دعَـ__',1),('5','هوَـ__',1),('6','رمَـ__',1),('7','مستشفَـ__',1),('8','صحرَـ__',1)], AR), AR)}
{exo('تمرين 4','2','3','كل كلمة : ألف مقصورة &#10003; أو ممدودة &#9651; :','صنِّف',
  fill_grid([('1','موسى',1),('2','سماء',1),('3','يسعى',1),('4','ماء',1),('5','الفتى',1),('6','دواء',1)], AR), AR)}
</div>
{exo('تمرين 5','2','5','الكلمات الآتية بالتشكيل الكامل :','شكِّل',
  word_bank(['كتبَ','طالبةٌ','مدرسةٌ','انطلقَ','أكرمَ','استمعَ','يذهبُ','مجتهدةٌ'], AR)+
  '<div class="answer-lines">'+'<div class="answer-line"></div>'*3+'</div>', AR,
  tip_text='ابدأ بالتشكيل من آخر الكلمة إلى أولها')}
{qr_strip('AR-04', AR)}
{wave_footer(AR)}<div class="page-num">9 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 5 — الأفعال : أنواعها ونواصبها وجوازمها
# ══════════════════════════════════════════════════════════════════
p5 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; الأفعال وأحكامها', AR)}
{sec('أنواع الفعل وتصريفه', AR)}
<div class="grid2">
{exo('تمرين 1','1','3','نوع كل فعل (ماضٍ / مضارع / أمر) :','حدِّد',
  fill_grid([('1','يقرأُ',1),('2','ذهبَ',1),('3','اجلسْ',1),('4','تعلّمَ',1),('5','يكتبُ',1),('6','افتحْ',1),('7','لعبَ',1),('8','تستمعُ',1),('9','ادرسْ',1)], AR), AR)}
{exo('تمرين 2','2','4','الفعل إلى الماضي والمضارع والأمر مع الضمائر المطلوبة :','حوِّل',
  tbl(['الفعل','ماضٍ (هو)','مضارع (أنت)','أمر (أنتَ)'],
    [['كتبَ','__','__','__'],['ذهبَ','__','__','__'],['قرأَ','__','__','__'],['فهِمَ','__','__','__']], AR), AR)}
</div>
{sec('نواصب المضارع وجوازمه', AR)}
<div class="grid2">
{exo('تمرين 3','2','4','المضارع بعد الأدوات الناصبة (أن / لن / كي / لام التعليل) :','حوِّل',
  example_box('يكتبُ &#8592; لن <strong>يكتبَ</strong>', AR)+
  fill_grid([('1','يدرسُ &#8592; لن ___',1),('2','يفهمُ &#8592; أن ___',1),('3','يذهبُ &#8592; كي ___',1),('4','يجتهدُ &#8592; لـ ___',1),('5','يلعبُ &#8592; لن ___',1),('6','يسألُ &#8592; أن ___',1)], AR), AR)}
{exo('تمرين 4','2','4','المضارع بعد أدوات الجزم (لم / لا الناهية / لام الأمر) :','حوِّل',
  fill_grid([('1','يذهبُ &#8592; لم ___',1),('2','تكذبُ &#8592; لا ___',1),('3','يقرأُ &#8592; لم ___',1),('4','يُهملُ &#8592; لا ___',1),('5','يكتبُ &#8592; لـ (أمر) ___',1),('6','تتأخرُ &#8592; لا ___',1)], AR), AR)}
</div>
{exo('تمرين 5','3','4','الأفعال الخمسة : أكمل الجدول :','أكمل',
  tbl(['الفعل المفرد','مع المثنى (هما)','مع الجمع (هم)','مع المؤنث (هي)'],
    [['يذهبُ','__','__','__'],['يكتبُ','__','__','__'],['يقرأُ','__','__','__']], AR),
  AR, tip_text='الأفعال الخمسة : يفعلان - يفعلون - تفعلان - تفعلون - تفعلين')}
{qr_strip('AR-05', AR)}
{wave_footer(AR)}<div class="page-num">11 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 6 — الصرف : المصدر واسم الفاعل والجموع
# ══════════════════════════════════════════════════════════════════
p6 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; الصرف والاشتقاق', AR)}
{sec('المصدر واسم الفاعل واسم المفعول', AR)}
{exo('تمرين 1','2','5','الجدول : استخرج المصدر واسم الفاعل واسم المفعول :','أكمل',
  tbl(['الفعل','المصدر','اسم الفاعل','اسم المفعول'],
    [['كَتَبَ','كتابة','__','__'],['فَهِمَ','__','__','__'],['أَكرمَ','__','__','__'],['دَرَسَ','__','__','__'],['انطلقَ','__','__','__'],['اجتهدَ','__','__','__']], AR), AR)}
{sec('المذكر والمؤنث &mdash; المفرد والمثنى والجمع', AR)}
<div class="grid2">
{exo('تمرين 2','1','3','المؤنث من كل اسم :','استخرج',
  fill_grid([('1','مدرِّس',1),('2','طالب',1),('3','كاتب',1),('4','مجتهد',1),('5','قائد',1),('6','نجيب',1)], AR), AR)}
{exo('تمرين 3','1','4','المثنى والجمع من كل كلمة :','أكمل',
  tbl(['المفرد','المثنى','جمع المذكر السالم','جمع المؤنث السالم'],
    [['مدرِّس','__','__','__'],['طالبة','__','__','__'],['مجتهد','__','__','__']], AR), AR)}
</div>
{sec('الجمع السالم والجمع التكسير', AR)}
<div class="grid2">
{exo('تمرين 4','2','3','الجمع مع بيان نوعه (سالم / تكسير) :','اكتب',
  fill_grid([('1','كتاب',1),('2','معلم',1),('3','صورة',1),('4','رجل',1),('5','طفل',1),('6','صديق',1)], AR), AR)}
{exo('تمرين 5','2','4','عائلة الكلمة من الجذر (كتب) : فعل ماضٍ + مضارع + أمر + مصدر + اسم فاعل + اسم مفعول :','استخرج',
  labeled_lines([('ماضٍ :',1),('مضارع :',1),('أمر :',1),('مصدر :',1),('اسم فاعل :',1),('اسم مفعول :',1)], AR), AR)}
</div>
{qr_strip('AR-01', AR)}
{wave_footer(AR)}<div class="page-num">12 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 7 — القراءة والفهم
# ══════════════════════════════════════════════════════════════════
p7 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; القراءة والفهم والتعبير', AR)}
{reading('الصيادُ الأمينُ', [
  'كانَ جابرٌ صيّاداً يعيشُ على ساحلِ نواكشوط. يستيقظُ كلَّ فجرٍ، يُصلّي ثم يحملُ شباكَهُ إلى البحرِ. يعملُ بصدقٍ وأمانةٍ، لا يَكذبُ في ميزانهِ ولا يَغشُّ زبائنَهُ.',
  'في يومٍ من الأيامِ، وجدَ في شباكهِ سمكةً ذهبيةً نادرةً. عرضَ عليهِ تاجرٌ ثمناً كبيراً، لكنّهُ رفضَ وأعادَها إلى البحرِ قائلاً : "الحلالُ أطيبُ من الحرامِ".',
], AR)}
{sec('أسئلة الفهم والتحليل', AR, '&#10067;')}
<div class="grid2">
{exo('س 1','1','2','من النص مباشرة :','أجب',
  labeled_lines([('أين يعيش جابر ؟ :',1),('متى يستيقظ ؟ :',1),('ماذا وجد في شباكه ؟ :',1)], AR), AR)}
{exo('س 2','2','2','عن المعاني والمفردات :','أجب',
  labeled_lines([('مرادف "نادرة" ومضاد "رفضَ" :',1),('معنى "لا يغشّ" بأسلوبك :',1),('عائلة كلمة "صادق" (3 كلمات) :',1)], AR), AR)}
</div>
{exo('س 3','2','3','من النص : جملة اسمية وجملة فعلية وأعرب أركانهما :','استخرج',
  tbl(['النوع','الجملة','الإعراب'],
    [['اسمية','__','__'],['فعلية','__','__']], AR), AR)}
{exo('س 4','3','3','الجملة : "يعملُ جابرٌ بصدقٍ وأمانةٍ" &nbsp;|&nbsp; أعرب كل كلمة :','أعرب',
  tbl(['الكلمة','نوعها','إعرابها'],
    [['يعملُ','__','__'],['جابرٌ','__','__'],['بصدقٍ','__','__'],['وأمانةٍ','__','__']], AR), AR,
  tip_text='الواو هنا حرف عطف، وما بعده معطوف على ما قبله في الإعراب')}
{exo('تعبير','3','4','فقرة من ٤ أسطر : "صفة من صفات الإنسان الصالح رأيتها في شخص تحبه" :','اكتب',
  '<div class="writing-area">'+'<div class="answer-line"></div>'*4+'</div>', AR)}
{qr_strip('AR-02', AR)}
{wave_footer(AR)}<div class="page-num">14 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 8 — امتحان عربية شامل
# ══════════════════════════════════════════════════════════════════
p8 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; نموذج امتحان شامل', AR)}
{reading('حُبُّ الوطنِ', [
  'الوطنُ هوَ المكانُ الذي وُلدَ فيهِ الإنسانُ ونشأَ بينَ أهلهِ. يُحبُّ المواطنُ وطنَهُ كما يُحبُّ أمَّهُ، يُدافعُ عنهُ ويَبنيهِ بعلمهِ وعملهِ.',
  'موريتانيا وطنُنا الحبيبُ، أرضُ المليونِ شاعرٍ. يجبُ على كلِّ مواطنٍ أن يخدمَ وطنَهُ بالصدقِ والإتقانِ.',
], AR)}
{sec('أسئلة الامتحان', AR, '&#128221;')}
<div class="grid2">
{exo('س 1 (3ن)','1','3','من النص مباشرة :','أجب',
  labeled_lines([('ما تعريف الوطن كما جاء في النص ؟ :',1),('كيف يُحب المواطن وطنه ؟ :',1),('ما اسم لقب موريتانيا ؟ :',1)], AR), AR)}
{exo('س 2 (3ن)','2','3','المفردات :','أجب',
  labeled_lines([('مرادف "يُدافع" ومضاد "يَبني" :',1),('معنى "الإتقان" في جملة من عندك :',2)], AR), AR)}
</div>
{exo('س 3 (4ن)','2','4','من النص : استخرج جملة اسمية وجملة فعلية + أعرب الجملة : "يُحبُّ المواطنُ وطنَهُ" :','استخرج',
  tbl(['الكلمة','نوعها','إعرابها'],
    [['يُحبُّ','__','__'],['المواطنُ','__','__'],['وطنَهُ','__','__']], AR), AR)}
{exo('س 4 (4ن)','3','4','فقرة من ٤ أسطر عن "واجباتنا نحو الوطن" :','اكتب',
  '<div class="writing-area">'+'<div class="answer-line"></div>'*4+'</div>', AR)}
{exo('س 5 (3ن)','2','3','صحِّح الأخطاء الإملائية والنحوية :','صحِّح',
  fill_grid([('1','ذهبتُ إلي المدرسةِ',1),('2','الولدة مجتهدٌ',1),('3','قرأتُ الكتابُ',1),('4','موسا يلعبُ',1),('5','رأيتُ المعلمُ',1),('6','الطالبُ الجديدة',1)], AR), AR)}
<div class="page-num">15 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 9 — العقيدة : أركان الإسلام والإيمان وصفات الله
# ══════════════════════════════════════════════════════════════════
p9 = f"""
<div class="page">
{page_hdr(mosque_svg(IS), 'التربية الإسلامية &mdash; العقيدة', IS)}
{sec('أركان الإسلام وأركان الإيمان', IS)}
<div class="grid2">
{exo('تمرين 1','1','4','أركان الإسلام الخمسة بالترتيب الصحيح :','رتِّب',
  word_bank(['الصومُ','الصلاةُ','الشهادةُ','الحجُّ','الزكاةُ'], IS)+
  labeled_lines([('1.',1),('2.',1),('3.',1),('4.',1),('5.',1)], IS), IS)}
{exo('تمرين 2','2','4','أركان الإيمان الستة مع شرح مختصر :','أكمل',
  tbl(['الركن','الشرح المختصر'],
    [['الإيمان بالله','__'],['الملائكة','__'],['الكتب','__'],['الرسل','__'],['اليوم الآخر','__'],['القدر','__']], IS), IS)}
</div>
{sec('صفات الله الواجبة والمستحيلة والجائزة', IS)}
<div class="grid2">
{exo('تمرين 3','2','5','الصفة المستحيلة مقابل كل صفة واجبة :','أكمل',
  tbl(['الواجبة','المستحيلة','الواجبة','المستحيلة'],
    [['الوجود','__','القِدَم','__'],['البقاء','__','الوحدانية','__'],['القدرة','__','الإرادة','__'],['العلم','__','الحياة','__']], IS), IS)}
{exo('تمرين 4','1','3','الإجابة الصحيحة بدائرة :','ضع',
  qcm_item('1','عدد صفات الله الواجبة :',['أ) 13','ب) 20','ج) 7','د) 99'], IS)+
  qcm_item('2','معنى "الوحدانية" :',['أ) كثرة','ب) انفراد بالألوهية','ج) الوجود','د) القدرة'], IS), IS)}
</div>
{exo('تمرين 5','2','3','هذه العبارات بـ &#10003; أو &#10007; :','صحِّح',
  tf_item('الله تعالى موجود في كل مكان بذاته.', IS)+
  tf_item('الإيمان بالقدر خيره وشره ركن من أركان الإيمان.', IS)+
  tf_item('الملائكة مخلوقون من نور يأكلون ويشربون.', IS)+
  tf_item('الإيمان بالله يقتضي الإيمان بأسمائه وصفاته.', IS), IS)}
{qr_strip('IS-01', IS)}
{wave_footer(IS)}<div class="page-num">16 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 10 — الفقه : الطهارة والصلاة
# ══════════════════════════════════════════════════════════════════
p10 = f"""
<div class="page">
{page_hdr(mosque_svg(IS), 'التربية الإسلامية &mdash; الفقه : الطهارة والصلاة', IS)}
{sec('الطهارة والوضوء', IS)}
<div class="grid2">
{exo('تمرين 1','1','4','فرائض الوضوء الستة بالترتيب :','رتِّب',
  word_bank(['مسح الرأس','النية','غسل الوجه','غسل اليدين','غسل الرجلين','الترتيب'], IS)+
  labeled_lines([('1.',1),('2.',1),('3.',1),('4.',1),('5.',1),('6.',1)], IS), IS)}
{exo('تمرين 2','2','3','مبطلات الوضوء (4 من أصل 6) :','اذكر',
  tf_item('خروج شيء من أحد السبيلين.', IS)+
  tf_item('الشرب والأكل يُبطلان الوضوء.', IS)+
  tf_item('النوم المستغرق يُبطل الوضوء.', IS)+
  tf_item('الضحك يُبطل الوضوء.', IS), IS,
  tip_text='بعض العبارات خاطئة — صحِّح ما يلزم')}
</div>
{sec('الصلاة : أركانها وواجباتها وسننها', IS)}
{exo('تمرين 3','2','5','الجدول بأحكام الصلاة :','أكمل',
  tbl(['الصفة','الحكم','المثال'],
    [['الركن','يُبطل تركه الصلاة','__'],['الواجب','تُجبر الصلاة بسجود السهو','__'],['السنة','لا شيء في تركه','__'],['شرط الصحة','لا تصح بدونه','__']], IS), IS)}
<div class="grid2">
{exo('تمرين 4','1','3','أركان الصلاة : ضع &#10003; أو &#10007; :','حدِّد',
  tf_item('تكبيرة الإحرام ركن من أركان الصلاة.', IS)+
  tf_item('الفاتحة ركن في كل ركعة.', IS)+
  tf_item('التشهد الأول ركن واجب.', IS)+
  tf_item('الجلوس للتشهد الأخير ركن.', IS), IS)}
{exo('تمرين 5','2','4','الإجابة الصحيحة :','ضع',
  qcm_item('1','عدد ركعات الفجر :',['أ) 2','ب) 3','ج) 4','د) 2 سنة + 2 فرض'], IS)+
  qcm_item('2','وقت صلاة العصر :',['أ) من الزوال','ب) من العصر إلى الغروب','ج) من الفجر','د) من المغرب'], IS), IS)}
</div>
{qr_strip('IS-03', IS)}
{wave_footer(IS)}<div class="page-num">18 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 11 — الفقه : الزكاة والصيام والحج
# ══════════════════════════════════════════════════════════════════
p11 = f"""
<div class="page">
{page_hdr(mosque_svg(IS), 'التربية الإسلامية &mdash; الفقه : الزكاة والصيام والحج', IS)}
{sec('الزكاة', IS)}
<div class="grid2">
{exo('تمرين 1','1','4','أحكام الزكاة الأساسية :','أكمل',
  tbl(['الحكم','التفصيل'],
    [['نصاب الذهب','__ ديناراً (85 غراماً)'],['نسبة الزكاة','__%'],['الحول','__ شهراً'],['8 مصارف الزكاة','الفقير - المسكين - __ - __ - __ - __ - __ - __']], IS), IS)}
{exo('تمرين 2','2','3','حالات وجوب الزكاة : &#10003; أو &#10007; :','حدِّد',
  tf_item('الزكاة واجبة على كل مسلم بالغ عاقل حر مالك للنصاب.', IS)+
  tf_item('تجب الزكاة عن الأطفال في أموالهم.', IS)+
  tf_item('الزكاة ركن من أركان الإسلام الخمسة.', IS), IS)}
</div>
{sec('الصيام والحج', IS)}
<div class="grid2">
{exo('تمرين 3','2','4','الجدول بأحكام الصيام :','أكمل',
  tbl(['','الحكم'],
    [['تعريف الصوم','__'],['ركنا الصوم','النية + الإمساك'],['مبطل 1','__'],['مبطل 2','__'],['كفارة الإفطار عمداً','__']], IS), IS)}
{exo('تمرين 4','2','4','الجدول بأحكام الحج :','أكمل',
  tbl(['','التفصيل'],
    [['تعريف الحج','__'],['الركن الأعظم','الوقوف بعرفة'],['ركن 2','__'],['واجب 1','__'],['شرط الاستطاعة','__']], IS), IS)}
</div>
{exo('تمرين 5','3','3','الإجابة الصحيحة :','ضع',
  qcm_item('1','كفارة الإفطار عمداً في رمضان :',['أ) قضاء يوم','ب) إطعام مسكين','ج) عتق رقبة أو صيام شهرين أو إطعام 60 مسكيناً','د) لا كفارة'], IS)+
  qcm_item('2','الركن الأعظم للحج :',['أ) الإحرام','ب) الطواف','ج) الوقوف بعرفة','د) السعي'], IS), IS,
  tip_text='الحج مرة واحدة في العمر فريضة على المستطيع')}
{qr_strip('IS-04', IS)}
{wave_footer(IS)}<div class="page-num">19 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 12 — السيرة النبوية والأخلاق
# ══════════════════════════════════════════════════════════════════
p12 = f"""
<div class="page">
{page_hdr(mosque_svg(IS), 'التربية الإسلامية &mdash; السيرة النبوية والأخلاق', IS)}
{sec('مراحل حياة النبي &#9786;', IS)}
{exo('تمرين 1','1','4','الأحداث الكبرى في حياة النبي &#9786; بالترتيب الزمني :','رتِّب',
  word_bank(['البعثة النبوية','مولده بمكة','الهجرة إلى المدينة','الإسراء والمعراج','فتح مكة','الوفاة الشريفة'], IS)+
  fill_grid([('1','_______________',1),('2','_______________',1),('3','_______________',1),('4','_______________',1),('5','_______________',1),('6','_______________',1)], IS), IS)}
{sec('الغزوات والمعارك الكبرى', IS)}
{exo('تمرين 2','2','5','الجدول بمعلومات الغزوات :','أكمل',
  tbl(['الغزوة','السنة (هـ)','عدد المسلمين','النتيجة'],
    [['بدر الكبرى','2 هـ','__','انتصار المسلمين'],['أُحُد','__','700','__'],['الخندق (الأحزاب)','__','__','انتصار المسلمين'],['فتح مكة','8 هـ','__','__']], IS), IS)}
{sec('الأخلاق الإسلامية', IS)}
<div class="grid2">
{exo('تمرين 3','2','4','كل خُلُق بدليل من القرآن الكريم أو السنة النبوية :','صل',
  tbl(['الخُلُق الإسلامي','الدليل الشرعي'],
    [['الصدق','__'],['الأمانة','__'],['بر الوالدين','__'],['حسن الجوار','__'],['الرفق والرحمة','__']], IS), IS)}
{exo('تمرين 4','3','3','قيمة إسلامية تطبّقها في مدرستك وكيف :','اذكر',
  labeled_lines([('القيمة :',1),('كيف أُطبّقها :',2)], IS), IS,
  tip_text='اختر قيمة حقيقية تُمارسها فعلاً')}
</div>
{qr_strip('IS-04', IS)}
{wave_footer(IS)}<div class="page-num">20 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE 13 — امتحان إسلامية شامل
# ══════════════════════════════════════════════════════════════════
p13 = f"""
<div class="page">
{page_hdr(mosque_svg(IS), 'التربية الإسلامية &mdash; نموذج امتحان شامل', IS)}
{sec('الجزء الأول — العقيدة والفقه (10 نقاط)', IS, '&#128221;')}
<div class="grid2">
{exo('س 1 (3ن)','2','3','المعلومات المطلوبة :','أكمل',
  fill_grid([
    ('أركان الإيمان :','الله &middot; ___ &middot; ___ &middot; ___ &middot; ___ &middot; ___',1),
    ('أركان الإسلام :','___ &middot; ___ &middot; ___ &middot; ___ &middot; ___',1),
    ('نصاب الذهب :','___ ديناراً',1),
    ('كفارة الإفطار عمداً :','_________________',1),
  ], IS), IS)}
{exo('س 2 (3ن)','1','3','دائرة حول الإجابة الصحيحة :','ضع',
  qcm_item('1','أول ما يُسأل عنه العبد يوم القيامة :',['أ) الزكاة','ب) الصلاة','ج) الصيام','د) الحج'], IS)+
  qcm_item('2','الركن الأعظم للحج :',['أ) الإحرام','ب) الطواف','ج) الوقوف بعرفة','د) السعي'], IS), IS)}
</div>
{exo('س 3 (4ن)','2','4','أكمل الآيات واذكر السور :','أكمل',
  labeled_lines([
    ('&#171;قُلْ هُوَ اللَّهُ ______________________________&#187; &larr; سورة :',1),
    ('&#171;وَبِالْوَالِدَيْنِ ______________________________&#187; &larr; سورة :',1),
    ('&#171;إِنَّ اللَّهَ مَعَ ______________________________&#187; &larr; سورة :',1),
  ], IS), IS)}
{sec('الجزء الثاني — السيرة والأخلاق (10 نقاط)', IS, '&#128214;')}
{exo('س 4 (4ن)','2','4','العشرة المبشرين بالجنة :','اذكر',
  '<div class="fill-grid">'+''.join([f'<div class="fill-item"><span class="fill-index" style="color:{IS}">{i}.</span><div class="fill-answer-line"></div></div>' for i in range(1,11)])+'</div>', IS)}
{exo('س 5 (3ن)','3','3','فقرة من ٣ أسطر عن "كيف تكون مثل النبي &#9786; في أخلاقه مع أصدقائك" :','اكتب',
  '<div class="writing-area">'+'<div class="answer-line"></div>'*3+'</div>', IS,
  tip_text='اذكر صفات محددة : الصدق، الرفق، الوفاء بالعهد...')}
{qr_strip('IS-05', IS)}
{wave_footer(IS)}<div class="page-num">22 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE p_nahw3 — النعت (الصفة) والتركيب الإضافي
# ══════════════════════════════════════════════════════════════════
p_nahw3 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; النحو : النعت والإضافة', AR)}
{sec('النعت (الصفة) ومطابقته للمنعوت', AR)}
<div class="grid2">
{exo('تمرين 1','1','4','النعت المناسب من بين القوسين :','اختر',
  fill_grid([('1','جاءَ رجلٌ (طويلٌ / طويلةٌ) ___',1),('2','رأيتُ سيارةً (سريعٍ / سريعةً) ___',1),('3','اشتريتُ كتاباً (مفيدٌ / مفيداً) ___',1),('4','مررتُ بطالبٍ (مجتهدٍ / مجتهدَ) ___',1),('5','قرأتُ القصةَ (الجميلةَ / الجميلُ) ___',1),('6','جلستُ على كرسيٍّ (المريحِ / المريحَ) ___',1)], AR), AR,
  tip_text='النعت يتبع المنعوت في: الإعراب، النوع، العدد، التعريف/التنكير')}
{exo('تمرين 2','2','4','نعت مناسب لكل اسم مع مراعاة المطابقة :','أضف',
  tbl(['الاسم المنعوت','النعت المناسب'],
    [['طالبٌ ___','__'],['مدرسةٌ ___','__'],['معلمٌ ___','__'],['حديقةٌ ___','__'],['كتابٌ ___','__'],['سيارةٌ ___','__']], AR), AR)}
</div>
{sec('التركيب الإضافي (المضاف والمضاف إليه)', AR)}
<div class="grid2">
{exo('تمرين 3','2','4','المضاف والمضاف إليه وعلامة جر المضاف إليه :','حدِّد',
  example_box('كتابُ <strong>الطالبِ</strong> : مضاف إليه مجرور بالكسرة', AR)+
  fill_grid([('1','بابُ الفصلِ',2),('2','قلمُ المعلمِ',2),('3','سطحُ البيتِ',2),('4','حديقةُ المدرسةِ',2)], AR), AR)}
{exo('تمرين 4','2','3','التركيب الإضافي بربط هذه الأسماء :','كوِّن',
  tbl(['الاسم 1','الاسم 2','التركيب الإضافي'],
    [['باب','فصل','__'],['كتاب','أستاذ','__'],['سيارة','مدير','__'],['لون','سماء','__']], AR), AR)}
</div>
{exo('تمرين 5','3','3','جملة مفيدة تحتوي على نعت وإضافة معاً في سياق واحد :','اكتب',
  '<div class="writing-area">'+'<div class="answer-line"></div>'*2+'</div>', AR,
  tip_text='مثال : زارَنا مديرُ المدرسةِ الكبيرةِ')}
{qr_strip('AR-03', AR)}
{wave_footer(AR)}<div class="page-num">3 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE p_nahw4 — الضمائر والأعداد والمعدود
# ══════════════════════════════════════════════════════════════════
p_nahw4 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; النحو : الضمائر والأعداد', AR)}
{sec('الضمائر المنفصلة والمتصلة', AR)}
<div class="grid2">
{exo('تمرين 1','1','4','الضمير المنفصل المناسب :','ضع',
  example_box('___ طالبٌ مجتهدٌ → <strong>هو</strong> طالبٌ مجتهدٌ', AR)+
  fill_grid([('1','___ يذهبُ إلى المدرسةِ (مفرد مذكر غائب)',1),('2','___ تحبُّ القراءةَ (مفرد مؤنث غائب)',1),('3','___ نتعلمُ معاً (المتكلم جمع)',1),('4','___ تجتهدُ في دراستكَ (مخاطب مفرد)',1),('5','___ تحبُّ المدرسةَ (مخاطب مؤنث)',1),('6','___ يلعبُون في الملعبِ (جمع مذكر غائب)',1)], AR), AR)}
{exo('تمرين 2','2','4','الضمير المتصل وبيان نوعه :','استخرج',
  tbl(['الجملة','الضمير المتصل','نوعه'],
    [['كتابُه على الطاولةِ','__','__'],['أعطيتُه الكتابَ','__','__'],['ذهبتُ معها','__','__'],['نحبُّهم كثيراً','__','__'],['بيتُنا قريبٌ','__','__']], AR), AR)}
</div>
{sec('الأعداد والمعدود (3 – 10)', AR)}
<div class="grid2">
{exo('تمرين 3','2','4','العدد مع المعدود مع مراعاة التذكير والتأنيث :','اكتب',
  example_box('3 كتب → <strong>ثلاثةُ</strong> كتبٍ &nbsp;|&nbsp; 3 بنات → <strong>ثلاثُ</strong> بناتٍ', AR)+
  fill_grid([('1','5 أولاد ←',1),('2','7 بنات ←',1),('3','4 معلمين ←',1),('4','8 طالبات ←',1),('5','6 كتب ←',1),('6','9 قلوب ←',1)], AR), AR,
  tip_text='الأعداد 3-10 تخالف المعدود في التذكير والتأنيث')}
{exo('تمرين 4','2','3','العدد المناسب بالكلمات :','أكمل',
  fill_grid([('1','في الفصل ___ (20) طالباً',1),('2','قرأتُ ___ (12) قصةً',1),('3','عندي ___ (11) كتاباً',1),('4','في السنة ___ (12) شهراً',1)], AR), AR)}
</div>
{exo('تمرين 5','3','3','أجب عن هذه الأسئلة بجملة كاملة تستخدم العدد : كم عدد أيام الأسبوع ؟ كم عدد أشهر السنة ؟ كم عدد أركان الإسلام ؟','أجب',
  '<div class="writing-area">'+'<div class="answer-line"></div>'*3+'</div>', AR,
  tip_text='أجب بجملة كاملة : في الأسبوع سبعةُ أيامٍ')}
{qr_strip('AR-03', AR)}
{wave_footer(AR)}<div class="page-num">4 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE p_nahw5 — الحال + التمييز + المنادى + الاستثناء
# ══════════════════════════════════════════════════════════════════
p_nahw5 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; النحو : الحال والتمييز والمنادى', AR)}
{sec('الحال والتمييز', AR)}
<div class="grid2">
{exo('تمرين 1','2','4','الحال من كل جملة وصاحبه :','استخرج',
  example_box('جاءَ الطالبُ <strong>مسرعاً</strong> : حال منصوب، صاحبه الطالب', AR)+
  fill_grid([('1','رجعَ الأبُ فرِحاً',2),('2','تحدّثَ المعلمُ هادئاً',2),('3','نامَ الطفلُ مطمئناً',2),('4','يمشي الولدُ مسرعاً',2)], AR), AR,
  tip_text='الحال: اسم منصوب يبيّن هيئة صاحبه عند وقوع الفعل')}
{exo('تمرين 2','2','3','التمييز في كل جملة وبيان نوعه :','حدِّد',
  fill_grid([('1','اشتريتُ كيلوغراماً سكراً',1),('2','عندي لترٌ زيتاً',1),('3','امتلأَ الإناءُ ماءً',1),('4','طابَ الجوُّ هواءً',1)], AR), AR)}
</div>
{sec('المنادى والاستثناء', AR)}
<div class="grid2">
{exo('تمرين 3','2','4','المنادى وعلامة بنائه أو إعرابه :','حدِّد',
  example_box('يا <strong>طالبُ</strong> اجتهدْ : مفرد علم مبني على الضم', AR)+
  fill_grid([('1','يا طالبُ اجتهدْ',2),('2','يا أيُّها المعلمُ',2),('3','يا أبتِ ساعدني',2),('4','يا طلابَ العلمِ',2)], AR), AR,
  tip_text='المنادى المفرد العلم والنكرة المقصودة يُبنيان على الضم')}
{exo('تمرين 4','2','3','المستثنى وضبطه بالشكل الصحيح :','استخرج',
  fill_grid([('1','جاءَ الطلابُ إلا خالداً___',1),('2','حضرَ الجميعُ إلا طالبةً___',1),('3','نجحَ الكلُّ إلا واحداً___',1),('4','ذهبَ الأولادُ إلا محمداً___',1)], AR), AR)}
</div>
{exo('تمرين 5','3','4','فقرة قصيرة (٣ جمل) تستخدم فيها حالاً ومنادى وأسلوب استثناء :','اكتب',
  '<div class="writing-area">'+'<div class="answer-line"></div>'*3+'</div>', AR,
  tip_text='مثال : يا أحمدُ، حضرَ التلاميذُ مسرعين إلا واحداً')}
{qr_strip('AR-04', AR)}
{wave_footer(AR)}<div class="page-num">5 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE p_nahw6 — كان وأخواتها وإن وأخواتها
# ══════════════════════════════════════════════════════════════════
p_nahw6 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; النحو : كان وأخواتها وإن وأخواتها', AR)}
{sec('كان وأخواتها (الأفعال الناقصة)', AR)}
<div class="grid2">
{exo('تمرين 1','1','4','اسم كان وخبرها في كل جملة :','حدِّد',
  example_box('كانَ <strong>الطالبُ</strong> (اسمها مرفوع) <strong>مجتهداً</strong> (خبرها منصوب)', AR)+
  fill_grid([('1','كانَ الجوُّ بارداً',2),('2','أصبحَ الولدُ كبيراً',2),('3','صارَ المعلمُ مشهوراً',2),('4','ليسَ الكسلُ مفيداً',2)], AR), AR,
  tip_text='كان وأخواتها: كان، أصبح، أمسى، صار، أضحى، ليس، مازال، مادام')}
{exo('تمرين 2','2','4','الفعل الناسخ المناسب :','أكمل',
  fill_grid([('1','___ الطقسُ جميلاً (صار)',1),('2','___ أحمدُ مريضاً (أصبح)',1),('3','___ البيتُ واسعاً (كان)',1),('4','___ الدرسُ سهلاً (ليس)',1),('5','___ الولدُ نائماً (مازال)',1),('6','___ الجوُّ دافئاً (أضحى)',1)], AR), AR)}
</div>
{sec('إن وأخواتها (الحروف الناسخة)', AR)}
<div class="grid2">
{exo('تمرين 3','2','4','اسم إن وخبرها مع ضبط الشكل الصحيح :','حدِّد',
  example_box('إنَّ <strong>الطالبَ</strong> (اسمها منصوب) <strong>مجتهدٌ</strong> (خبرها مرفوع)', AR)+
  fill_grid([('1','إنَّ العلمَ نورٌ',2),('2','لكنَّ الكسلَ ضارٌّ',2),('3','كأنَّ القمرَ شمسٌ',2),('4','ليتَ الصيفَ يعودُ',2)], AR), AR,
  tip_text='إن وأخواتها: إنَّ، أنَّ، لكنَّ، كأنَّ، ليتَ، لعلَّ')}
{exo('تمرين 4','2','4','إن المناسبة لكل سياق :','اختر',
  fill_grid([('1','___ المطرَ نزلَ (تمنِّي)',1),('2','___ العلمَ مفيدٌ (توكيد)',1),('3','___ الطقسَ جميلٌ (تشبيه)',1),('4','___ الوقتَ ثمينٌ (استدراك)',1),('5','___ أحمدَ قادمٌ (ترجٍّ)',1),('6','___ الكذبَ مذمومٌ (توكيد)',1)], AR), AR)}
</div>
{exo('تمرين 5','3','3','جملتين : واحدة بكان وأخواتها وأخرى بإن وأخواتها :','اكتب',
  '<div class="writing-area">'+'<div class="answer-line"></div>'*2+'</div>', AR,
  tip_text='مثال : كانَ الطقسُ بارداً / إنَّ العلمَ نورٌ')}
{qr_strip('AR-04', AR)}
{wave_footer(AR)}<div class="page-num">6 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE p_nahw7 — ظرف الزمان والمكان + المثنى والجموع السالمة
# ══════════════════════════════════════════════════════════════════
p_nahw7 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; النحو : الظرف والمثنى والجموع', AR)}
{sec('ظرف الزمان وظرف المكان', AR)}
<div class="grid2">
{exo('تمرين 1','1','4','ظرف زمان أم ظرف مكان ؟ واستخرجه من الجملة :','صنِّف',
  example_box('جلستُ <strong>أمامَ</strong> البيتِ : ظرف مكان &nbsp;|&nbsp; جئتُ <strong>يومَ</strong> الجمعةِ : ظرف زمان', AR)+
  fill_grid([('1','ذهبتُ صباحاً إلى المدرسةِ',2),('2','وقفَ الطالبُ خلفَ المعلمِ',2),('3','نمتُ ليلاً وسهرتُ نهاراً',2),('4','الكتابُ فوقَ الطاولةِ',2)], AR), AR,
  tip_text='الظرف اسم منصوب يبيّن زمان الفعل أو مكانه')}
{exo('تمرين 2','2','3','ظرف الزمان أو المكان المناسب :','أكمل',
  fill_grid([('1','ذهبتُ ___ (فوقَ/أمسِ) إلى المدرسةِ',1),('2','الكتابُ ___ (تحتَ/غداً) الطاولةِ',1),('3','سأزورُكَ ___ (يميناً/غداً)',1),('4','وقفَ ___ (أمامَ/ليلاً) البابِ',1)], AR), AR)}
</div>
{sec('المثنى وجمع المذكر/المؤنث السالم', AR)}
<div class="grid2">
{exo('تمرين 3','2','4','المثنى في حالات الإعراب الثلاث :','صنِّف',
  example_box('طالبٌ → طالبانِ (رفع) &nbsp;/&nbsp; طالبَيْنِ (نصب وجر)', AR)+
  fill_grid([('1','كتابٌ ← رفع :__ / نصب :__',1),('2','معلمٌ ← رفع :__ / نصب :__',1),('3','بنتٌ ← رفع :__ / نصب :__',1),('4','مدرسةٌ ← رفع :__ / نصب :__',1)], AR), AR,
  tip_text='المثنى: يُرفع بالألف ويُنصب ويُجر بالياء')}
{exo('تمرين 4','2','4','جمع المذكر السالم وجمع المؤنث السالم :','كوِّن',
  tbl(['المفرد','جمع مذكر سالم','جمع مؤنث سالم'],
    [['معلمٌ','معلمون','__'],['طالبةٌ','__','طالباتٌ'],['مسلمٌ','__','__'],['مؤمنةٌ','__','__'],['ناجحٌ','__','__']], AR), AR,
  tip_text='ج.م.سالم يُرفع بالواو ونونه / يُنصب ويُجر بالياء ونونه')}
</div>
{exo('تمرين 5','3','3','جملتين : المثنى في حالتين مختلفتين + جمع سالم :','اكتب',
  '<div class="writing-area">'+'<div class="answer-line"></div>'*3+'</div>', AR,
  tip_text='مثال : جاءَ المعلمانِ / رأيتُ المعلمَيْنِ / المعلمون مجتهدون')}
{qr_strip('AR-04', AR)}
{wave_footer(AR)}<div class="page-num">7 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE p_imlaa3 — الإملاء المتقدم : الألف الفارقة + التنوين + الوقف
# ══════════════════════════════════════════════════════════════════
p_imlaa3 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; الإملاء : الألف الفارقة والتنوين', AR)}
{sec('الألف الفارقة بين واو الجماعة والتنوين', AR)}
<div class="grid2">
{exo('تمرين 1','2','4','هل الألف فارقة أم ألف تنوين ؟','ميِّز',
  example_box('كتبوا (ألف فارقة — جمع) &nbsp;|&nbsp; كتاباً (ألف تنوين — نصب)', AR)+
  fill_grid([('1','يذهبون',1),('2','طالباً',1),('3','يكتبون',1),('4','كتاباً',1),('5','يلعبونا &#8594; خطأ ←',1),('6','معلماً',1)], AR), AR,
  tip_text='الألف الفارقة تُكتب بعد واو جماعة الأفعال لتمييزها')}
{exo('تمرين 2','2','4','التنوين المناسب (ضم / فتح / كسر) :','ضع',
  fill_grid([('1','جاءَ طالب___',1),('2','رأيتُ طالب___',1),('3','مررتُ بطالب___',1),('4','حضرَ معلم___',1),('5','رأيتُ بيت___',1),('6','سكنتُ في بيت___',1)], AR), AR)}
</div>
{sec('الوقف على أواخر الكلمات والملاءة الإملائية', AR)}
<div class="grid2">
{exo('تمرين 3','2','3','كيف تقف على كل كلمة (السكون أو الإبقاء) :','بيِّن',
  fill_grid([('1','الطالبُ',1),('2','كتبَ',1),('3','مدرسةٍ',1),('4','يقرأُ',1),('5','الكتابَ',1),('6','مجتهدٌ',1)], AR), AR,
  tip_text='عند الوقف: نسكّن آخر الكلمة عادةً')}
{exo('تمرين 4','3','3','اكتشف الأخطاء الإملائية وصحِّحها :','صحِّح',
  fill_grid([('1','يذهبونا إلى المدرسة ←',1),('2','رأيتُ طالبٌ ←',1),('3','هم يلعبوا ←',1),('4','عندي كتابً ←',1)], AR), AR)}
</div>
{exo('تمرين 5','3','3','اكتب هذه الجملة بخطك مع الضبط الصحيح : "جلسَ الطلابُ في الفصلِ يكتبونَ الدرسَ باهتمامٍ شديدٍ ويستمعون إلى المعلمِ المجتهدِ"','اكتب',
  '<div class="writing-area">'+'<div class="answer-line"></div>'*3+'</div>', AR,
  tip_text='انتبه للتنوين، الألف الفارقة، وعلامات الإعراب')}
{qr_strip('AR-05', AR)}
{wave_footer(AR)}<div class="page-num">10 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE p_sarf2 — الصرف المتقدم : الفعل المجرد/المزيد والصحيح/المعتل
# ══════════════════════════════════════════════════════════════════
p_sarf2 = f"""
<div class="page">
{page_hdr(book_svg(AR), 'اللغة العربية &mdash; الصرف المتقدم : المجرد والمزيد', AR)}
{sec('الفعل المجرد والمزيد', AR)}
<div class="grid2">
{exo('تمرين 1','2','4','مجرد أم مزيد ؟ واذكر حروفه الزائدة :','صنِّف',
  example_box('كَتَبَ : مجرد ثلاثي &nbsp;|&nbsp; اكتَتَبَ : مزيد (زيادة همزة + تاء)', AR)+
  fill_grid([('1','جلسَ',2),('2','تعلَّمَ',2),('3','فتحَ',2),('4','استعملَ',2),('5','ذهبَ',2),('6','انكسرَ',2)], AR), AR,
  tip_text='المزيد يُضاف إليه حرف أو أكثر للمعنى: المطاوعة، المشاركة، الطلب')}
{exo('تمرين 2','2','4','وزن كل فعل ونوعه :','حدِّد',
  tbl(['الفعل','وزنه','نوعه'],
    [['كَتَبَ','فَعَلَ','مجرد'],['تعلّمَ','__','__'],['استفسرَ','__','__'],['قرّرَ','__','__'],['انكسرَ','__','__']], AR), AR)}
</div>
{sec('الفعل الصحيح والمعتل', AR)}
<div class="grid2">
{exo('تمرين 3','2','4','صحيح أم معتل ؟ واذكر نوعه :','صنِّف',
  example_box('كتبَ : صحيح سالم &nbsp;|&nbsp; قالَ : معتل أجوف &nbsp;|&nbsp; دعا : معتل ناقص', AR)+
  fill_grid([('1','قالَ',2),('2','كتبَ',2),('3','باعَ',2),('4','دعا',2),('5','وجدَ',2),('6','رمى',2)], AR), AR,
  tip_text='المعتل: فيه حرف علة (ا، و، ي) في أحد أصوله الثلاثة')}
{exo('تمرين 4','3','3','الجذر الثلاثي لكل فعل :','استخرج',
  fill_grid([('1','استقبلَ ←',1),('2','تحدّثَ ←',1),('3','انطلقَ ←',1),('4','اجتمعَ ←',1),('5','تصارعَ ←',1)], AR), AR)}
</div>
{exo('تمرين 5','3','3','مصدر كل فعل واستخدامه في جملة مفيدة :','اشتق',
  tbl(['الفعل','المصدر','جملة بالمصدر'],
    [['كتبَ','كتابةٌ','__'],['تعلّمَ','__','__'],['قرأَ','__','__'],['ذهبَ','__','__']], AR), AR,
  tip_text='المصدر: يدل على الحدث مجرداً من الزمان')}
{qr_strip('AR-05', AR)}
{wave_footer(AR)}<div class="page-num">13 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE p_islami_extra1 — التوحيد المتقدم + الطهارة الكاملة
# ══════════════════════════════════════════════════════════════════
p_islami_extra1 = f"""
<div class="page">
{page_hdr(mosque_svg(IS), 'التربية الإسلامية &mdash; التوحيد وصفات الله والطهارة', IS)}
{sec('صفات الله تعالى وأسماؤه الحسنى', IS)}
<div class="grid2">
{exo('تمرين 1','1','4','صل كل اسم بمعناه :','صل',
  tbl(['اسم من أسماء الله','المعنى'],
    [['الرحمن','__'],['العليم','__'],['القدير','__'],['السميع','__'],['الغفور','__'],['الرزاق','__']], IS), IS,
  tip_text='لله 99 اسماً حسناً، كلها تدل على صفات الكمال المطلق')}
{exo('تمرين 2','1','3','أين وُرِدَ كل اسم في القرآن الكريم (اذكر سورة واحدة) :','اذكر',
  fill_grid([('1','الرحمن الرحيم ←',1),('2','العليم القدير ←',1),('3','السميع البصير ←',1)], IS), IS)}
</div>
{sec('الطهارة الكاملة : الغسل والتيمم والأذان', IS)}
<div class="grid2">
{exo('تمرين 3','2','4','موجبات الغسل الشرعي :','اذكر',
  '<div class="fill-grid">'+''.join([f'<div class="fill-item"><span class="fill-index" style="color:{IS}">{i}.</span><div class="fill-answer-line"></div></div>' for i in range(1,6)])+'</div>'+
  word_bank(['الجنابة','الحيض','النفاس','الوفاة','إسلام الكافر'], IS), IS,
  tip_text='الغسل الشرعي له نية وترتيب يختلف عن الاغتسال العادي')}
{exo('تمرين 4','2','4','ترتيب التيمم خطوةً بخطوة :','رتِّب',
  word_bank(['الضرب على التراب الطاهر','النية','مسح الوجه','مسح اليدين إلى الرسغين','البسملة'], IS), IS,
  tip_text='التيمم بديل الوضوء عند عدم الماء أو المرض أو الضرر')}
</div>
{exo('تمرين 5','3','4','ألفاظ الأذان بالترتيب الصحيح مع بيان عدد مرات كل عبارة :','اكتب',
  tbl(['عبارة الأذان','عدد المرات'],
    [['الله أكبر','__'],['أشهد أن لا إله إلا الله','__'],['أشهد أن محمداً رسول الله','__'],['حي على الصلاة','__'],['حي على الفلاح','__'],['الله أكبر لا إله إلا الله','__']], IS), IS,
  tip_text='الأذان 15 كلمة / الإقامة 11 كلمة')}
{qr_strip('IS-03', IS)}
{wave_footer(IS)}<div class="page-num">17 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  PAGE p_islami_extra2 — القرآن الكريم + السيرة التكميلية
# ══════════════════════════════════════════════════════════════════
p_islami_extra2 = f"""
<div class="page">
{page_hdr(mosque_svg(IS), 'التربية الإسلامية &mdash; القرآن الكريم والسيرة', IS)}
{sec('السور القرآنية المقررة', IS)}
<div class="grid2">
{exo('تمرين 1','1','4','أكمل الآيات الكريمة :','أكمل',
  labeled_lines([
    ('&#171;قُلْ أَعُوذُ بِرَبِّ ________________________&#187;',1),
    ('&#171;قُلْ هُوَ اللَّهُ أَحَدٌ &middot; اللَّهُ _______________________&#187;',1),
    ('&#171;الْحَمْدُ لِلَّهِ رَبِّ _______________________&#187;',1),
    ('&#171;بِسْمِ اللَّهِ الرَّحْمَنِ _______________________&#187;',1),
  ], IS), IS,
  tip_text='السور المقررة: الفاتحة، الإخلاص، الفلق، الناس، الكافرون')}
{exo('تمرين 2','1','3','ربط كل سورة بمكان نزولها وموضوعها الرئيسي :','صل',
  tbl(['السورة','مكان النزول','موضوعها الرئيسي'],
    [['الفاتحة','__','__'],['الإخلاص','__','__'],['الكافرون','__','__'],['الفلق','__','__']], IS), IS)}
</div>
{sec('السيرة النبوية التكميلية', IS)}
<div class="grid2">
{exo('تمرين 3','2','4','أزواج النبي &#9786; الكريمات الأربع الأوائل :','اذكر',
  '<div class="fill-grid">'+''.join([f'<div class="fill-item"><span class="fill-index" style="color:{IS}">{i}.</span><div class="fill-answer-line"></div></div>' for i in range(1,5)])+'</div>'+
  word_bank(['خديجة بنت خويلد','عائشة بنت أبي بكر','حفصة بنت عمر','أم سلمة'], IS), IS)}
{exo('تمرين 4','2','3','الصحابة الكرام بمناقبهم :','صل',
  tbl(['الصحابي','ما عُرف به'],
    [['أبو بكر الصديق','__'],['عمر بن الخطاب','__'],['عثمان بن عفان','__'],['علي بن أبي طالب','__']], IS), IS,
  tip_text='أبو بكر=الصدق، عمر=العدل، عثمان=الحياء، علي=العلم')}
</div>
{exo('تمرين 5','3','4','فقرة من 4 أسطر عن "الهجرة النبوية : أسبابها وأحداثها ونتائجها" :','اكتب',
  '<div class="writing-area">'+'<div class="answer-line"></div>'*4+'</div>', IS,
  tip_text='الهجرة 622 م / 1 هـ ← بداية التقويم الهجري')}
{qr_strip('IS-05', IS)}
{wave_footer(IS)}<div class="page-num">21 / 22</div>
</div>"""

# ══════════════════════════════════════════════════════════════════
#  ASSEMBLE HTML
# ══════════════════════════════════════════════════════════════════
html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>دفتر ماجور — اللغة العربية &middot; التربية الإسلامية — 6AF V2</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{cover}
{p1}{p2}{p_nahw3}{p_nahw4}{p_nahw5}{p_nahw6}{p_nahw7}{p3}{p4}{p_imlaa3}{p5}{p6}{p_sarf2}{p7}{p8}
{p9}{p_islami_extra1}{p10}{p11}{p12}{p_islami_extra2}{p13}
<button class="print-btn no-print" onclick="window.print()">&#128424; طباعة الدفتر</button>
</body>
</html>"""

out = 'C:/Users/PC/Documents/Major-Contenue/6AF-ARABE/Cahier-Major-LangueArabe-Islamique-6AF-V2.html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'OK: {len(html):,} chars -> {out}')
