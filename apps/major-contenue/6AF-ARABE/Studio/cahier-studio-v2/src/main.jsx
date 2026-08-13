import React, { useRef, useState, useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

/* ── helpers ── */
const uid = () => Math.random().toString(36).slice(2, 9);
const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));
const mm = (v) => `${v}mm`;

/* ── icons (SVG inline) ── */
function Ic({ n, s = 15 }) {
  const icons = {
    plus:    <path d="M12 5v14M5 12h14" />,
    minus:   <path d="M5 12h14" />,
    print:   <><path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><path d="M6 14h12v8H6z"/></>,
    copy:    <><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></>,
    upload:  <><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="M17 8l-5-5-5 5"/><path d="M12 3v12"/></>,
    trash:   <><path d="M3 6h18M8 6V4h8v2M19 6l-1 16H6L5 6"/></>,
    dup:     <><rect x="8" y="8" width="12" height="12" rx="2"/><path d="M4 16V4h12"/></>,
    chevL:   <path d="M15 18l-6-6 6-6" />,
    chevR:   <path d="M9 18l6-6-6-6" />,
    page:    <><rect x="3" y="2" width="14" height="18" rx="2"/><path d="M7 7h6M7 11h6M7 15h4"/></>,
    brush:   <><path d="M9.06 11.9l8.07-8.06a2.85 2.85 0 1 1 4.03 4.03l-8.06 8.08"/><path d="M7.07 14.94c-1.66 0-3 1.35-3 3.02 0 1.33-2.5 1.52-2 2.02 1 1 2.18.82 3.17.82 1.85 0 3.83-1.57 3.83-3.86 0-1.05-.86-2-2-2z"/></>,
    layout:  <><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></>,
    code:    <><path d="M16 18l6-6-6-6"/><path d="M8 6l-6 6 6 6"/></>,
  };
  return (
    <svg width={s} height={s} viewBox="0 0 24 24" fill="none"
      stroke="currentColor" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round">
      {icons[n]}
    </svg>
  );
}

/* ── block templates ── */
const TEMPLATES = {
  section:  { type:'section',  title:'✎ عنوان الدرس',                   text:'', x:45, y:27,  w:90,  h:11, variant:'section' },
  rule:     { type:'rule',     title:'القاعدة',                         text:'اكتب هنا قاعدة الدرس بشكل مختصر وواضح.', x:6, y:41, w:128, h:18, variant:'rule' },
  exercise: { type:'exercise', title:'أعرب الكلمات التي تحتها خط :',   text:'مثال: الجهلُ ظلامٌ — الجهلُ: مبتدأ مرفوع.', x:48, y:67, w:88, h:52, variant:'cartoon' },
  wide:     { type:'exercise', title:'أكمل الجدول بما يناسب :',         text:'استعمل الكلمات المناسبة في الفراغات.',      x:6,  y:67, w:128, h:44, variant:'cartoon' },
  table:    { type:'table',    title:'أكمل الجدول :',                   text:'', x:6,  y:113, w:70,  h:55, variant:'soft' },
  writing:  { type:'writing',  title:'ركب جملة مفيدة :',                text:'', x:6,  y:154, w:128, h:32, variant:'minimal' },
};

const LIBRARY = [
  { key:'section',  icon:'🏷️',  label:'Titre de section', sub:'Badge décoratif', bg:'linear-gradient(135deg,#1e3a5f,#2563eb)' },
  { key:'rule',     icon:'📌',  label:'Règle / leçon',    sub:'Encadré pédagogique', bg:'linear-gradient(135deg,#1d4ed8,#38bdf8)' },
  { key:'exercise', icon:'✏️',  label:'Exercice ×2',      sub:'Grille 2 colonnes', bg:'linear-gradient(135deg,#059669,#34d399)' },
  { key:'wide',     icon:'📋',  label:'Exercice large',   sub:'Pleine largeur', bg:'linear-gradient(135deg,#7c3aed,#22d3ee)' },
  { key:'table',    icon:'📊',  label:'Tableau',          sub:'Colonnes réponses', bg:'linear-gradient(135deg,#ea580c,#fb923c)' },
  { key:'writing',  icon:'📝',  label:'Rédaction',        sub:'Lignes libres', bg:'linear-gradient(135deg,#0f172a,#475569)' },
];

const THEMES = [
  { id:'blue',   label:'Arabe',    bg:'linear-gradient(135deg,#1e3a5f,#2563eb,#38bdf8)' },
  { id:'green',  label:'Islamique',bg:'linear-gradient(135deg,#064e3b,#059669,#34d399)' },
  { id:'purple', label:'Moderne',  bg:'linear-gradient(135deg,#312e81,#7c3aed,#22d3ee)' },
  { id:'orange', label:'Maths',    bg:'linear-gradient(135deg,#7c2d12,#ea580c,#fb923c)' },
];

const VARIANTS = [
  { id:'cartoon', label:'Cartoon' },
  { id:'soft',    label:'Doux' },
  { id:'glass',   label:'Verre' },
  { id:'minimal', label:'Minimal' },
  { id:'rule',    label:'Règle' },
  { id:'section', label:'Titre' },
];

const mkPage = (n) => ({
  id: uid(),
  title: `Page ${n}`,
  theme: 'blue',
  lesson: 'اللغة العربية — نموذج الدرس',
  footer: 'Major 6AF · دفتر التمارين',
  blocks: [
    { ...TEMPLATES.section,  id: uid() },
    { ...TEMPLATES.rule,     id: uid() },
    { ...TEMPLATES.exercise, id: uid() },
  ],
});

/* ═══════════════════════════════════════════════ */
function App() {
  const stored = localStorage.getItem('major-studio-v2');
  const [project, setProject] = useState(() =>
    stored ? JSON.parse(stored) : { pages: [mkPage(1)] }
  );
  const [pageId,     setPageId]     = useState(project.pages[0].id);
  const [selectedId, setSelectedId] = useState(null);
  const canvasRef = useRef(null);
  const [zoom,       setZoom]       = useState(0.82);
  const [tab,        setTab]        = useState('page');
  const [jsonDraft,  setJsonDraft]  = useState('');
  const [v3css,      setV3css]      = useState('');

  // Injecter le CSS V3-Cartoon dans <head>
  useEffect(() => {
    if (!v3css) return;
    let el = document.getElementById('v3-cartoon-css');
    if (!el) { el = document.createElement('style'); el.id = 'v3-cartoon-css'; document.head.appendChild(el); }
    el.textContent = v3css;
  }, [v3css]);

  const page = project.pages.find(p => p.id === pageId) ?? project.pages[0];
  const pageIdx = project.pages.findIndex(p => p.id === pageId);
  const selected = page.blocks.find(b => b.id === selectedId) ?? null;

  useEffect(() => {
    localStorage.setItem('major-studio-v2', JSON.stringify(project));
    setJsonDraft(JSON.stringify(project, null, 2));
  }, [project]);

  // Charger le vrai HTML V3-Cartoon (blocs HTML réels)
  const loadV3Cartoon = async () => {
    try {
      const res = await fetch('/v3cartoon.json');
      const data = await res.json();
      if (data.pages?.length) {
        setProject({ pages: data.pages });
        if (data.css) setV3css(data.css);
        setPageId(data.pages[0].id);
        setSelectedId(null);
        setTab('page');
      }
    } catch (e) {
      alert('Erreur : ' + e.message);
    }
  };

  // Auto-zoom : ajuste le zoom pour que la page A5 tienne dans le canvas
  useEffect(() => {
    const fit = () => {
      const el = canvasRef.current;
      if (!el) return;
      const W = el.clientWidth  - 56; // padding 28px × 2
      const H = el.clientHeight - 56;
      const pageW = 148 / 25.4 * 96;
      const pageH = 210 / 25.4 * 96;
      const z = Math.min(W / pageW, H / pageH, 1) * 0.97;
      setZoom(Math.max(0.38, z));
    };
    fit();
    window.addEventListener('resize', fit);
    return () => window.removeEventListener('resize', fit);
  }, []);

  /* page helpers */
  const addPage = () => {
    const p = mkPage(project.pages.length + 1);
    setProject(c => ({ pages: [...c.pages, p] }));
    setPageId(p.id);
    setSelectedId(null);
  };
  const goPage = (delta) => {
    const idx = clamp(pageIdx + delta, 0, project.pages.length - 1);
    setPageId(project.pages[idx].id);
    setSelectedId(null);
  };
  const updatePage = (patch) =>
    setProject(c => ({ pages: c.pages.map(p => p.id === page.id ? { ...p, ...patch } : p) }));

  /* block helpers */
  const addBlock = (kind) => {
    const b = { ...TEMPLATES[kind], id: uid(), x: TEMPLATES[kind].x + page.blocks.length * 2, y: TEMPLATES[kind].y + page.blocks.length * 2 };
    setProject(c => ({ pages: c.pages.map(p => p.id === page.id ? { ...p, blocks: [...p.blocks, b] } : p) }));
    setSelectedId(b.id);
    setTab('block');
  };
  const updateBlock = (id, patch) =>
    setProject(c => ({ pages: c.pages.map(p => p.id === page.id ? { ...p, blocks: p.blocks.map(b => b.id === id ? { ...b, ...patch } : b) } : p) }));
  const duplicateBlock = () => {
    if (!selected) return;
    const copy = { ...selected, id: uid(), x: selected.x + 4, y: selected.y + 4 };
    setProject(c => ({ pages: c.pages.map(p => p.id === page.id ? { ...p, blocks: [...p.blocks, copy] } : p) }));
    setSelectedId(copy.id);
  };
  const deleteBlock = () => {
    if (!selected) return;
    setProject(c => ({ pages: c.pages.map(p => p.id === page.id ? { ...p, blocks: p.blocks.filter(b => b.id !== selected.id) } : p) }));
    setSelectedId(null);
  };
  const importJson = () => {
    try {
      const parsed = JSON.parse(jsonDraft);
      if (parsed.pages?.length) {
        setProject(parsed);
        setPageId(parsed.pages[0].id);
        setSelectedId(null);
      }
    } catch {}
  };

  return (
    <div className="studio">
      {/* ── TOP NAV ── */}
      <nav className="topnav">
        <div className="nav-brand">
          <div className="nav-logo">M+</div>
          <div className="nav-title">
            <strong>Cahier Studio</strong>
            <span>Major 6AF — Éditeur de pages A5</span>
          </div>
        </div>

        <div className="nav-sep" />

        <div className="nav-pages">
          <button className="nav-arrow" onClick={() => goPage(-1)} disabled={pageIdx === 0}>
            <Ic n="chevR" s={14} />
          </button>
          <span className="nav-page-label">{page.title} · {pageIdx + 1}/{project.pages.length}</span>
          <button className="nav-arrow" onClick={() => goPage(+1)} disabled={pageIdx === project.pages.length - 1}>
            <Ic n="chevL" s={14} />
          </button>
        </div>

        <div className="nav-sep" />

        <div className="nav-actions">
          <div className="nav-zoom">
            <button onClick={() => setZoom(z => clamp(z - 0.08, 0.4, 1.3))}>−</button>
            <span>{Math.round(zoom * 100)}%</span>
            <button onClick={() => setZoom(z => clamp(z + 0.08, 0.4, 1.3))}>+</button>
          </div>
          <button className="btn-print" onClick={() => window.print()}>
            <Ic n="print" s={14} /> Imprimer A5
          </button>
          <button className="btn-export" onClick={() => navigator.clipboard?.writeText(JSON.stringify(project, null, 2))}>
            <Ic n="copy" s={14} /> JSON
          </button>
        </div>
      </nav>

      {/* ── LEFT PANEL ── */}
      <aside className="left-panel">
        {/* Bouton charger le vrai HTML V3-Cartoon */}
        <button className="btn-load-cahier" onClick={loadV3Cartoon}>
          <span>📖</span>
          <span className="btn-load-text">
            <strong>Cahier Arabe 6AF</strong>
            <small>25 pages · 157 blocs · style V3-Cartoon réel</small>
          </span>
        </button>

        <div className="panel-section">
          <div className="section-header">
            <span className="section-label">Pages</span>
            <button className="btn-add-page" onClick={addPage}>
              <Ic n="plus" s={12} /> Nouvelle
            </button>
          </div>
        </div>

        <div className="pages-scroll">
          {project.pages.map((p, idx) => (
            <button
              key={p.id}
              className={`page-thumb ${p.id === page.id ? 'active' : ''}`}
              onClick={() => { setPageId(p.id); setSelectedId(null); }}
            >
              <div className="page-mini">
                <div className="page-mini-header" style={{ background: THEMES.find(t=>t.id===p.theme)?.bg }} />
                <div className="page-mini-body"><span/><span/><span/></div>
              </div>
              <div className="page-thumb-info">
                <strong>{p.title}</strong>
                <small>{p.blocks.length} bloc{p.blocks.length !== 1 ? 's' : ''}</small>
              </div>
              <span className="page-thumb-num">{String(idx + 1).padStart(2,'0')}</span>
            </button>
          ))}
        </div>

        <div className="panel-section" style={{ paddingBottom: 10 }}>
          <div className="section-header">
            <span className="section-label">Bibliothèque de blocs</span>
          </div>
        </div>

        <div className="library-scroll">
          {LIBRARY.map(({ key, icon, label, sub, bg }) => (
            <button className="lib-btn" key={key} onClick={() => addBlock(key)}>
              <div className="lib-icon" style={{ background: bg }}>
                {icon}
              </div>
              <div className="lib-btn-info">
                <strong>{label}</strong>
                <span>{sub}</span>
              </div>
            </button>
          ))}
        </div>
      </aside>

      {/* ── CANVAS ── */}
      <main className="canvas-area" ref={canvasRef}>
        <PageCanvas
          page={page}
          selectedId={selectedId}
          zoom={zoom}
          onSelect={(id) => { setSelectedId(id); if (id) setTab('block'); }}
          onUpdateBlock={updateBlock}
        />
      </main>

      {/* ── RIGHT PANEL ── */}
      <aside className="right-panel">
        <div className="tabs-header">
          <button className={`tab-btn ${tab==='page'  ? 'active' : ''}`} onClick={() => setTab('page')}>
            <Ic n="page" s={13} /> Page
          </button>
          <button className={`tab-btn ${tab==='block' ? 'active' : ''}`} onClick={() => setTab('block')}>
            <Ic n="brush" s={13} /> Bloc
          </button>
          <button className={`tab-btn ${tab==='json'  ? 'active' : ''}`} onClick={() => setTab('json')}>
            <Ic n="code" s={13} /> JSON
          </button>
        </div>

        <div className="tab-content">
          {tab === 'page' && (
            <PageInspector page={page} onUpdate={updatePage} />
          )}
          {tab === 'block' && (
            <BlockInspector
              selected={selected}
              onUpdate={(patch) => selected && updateBlock(selected.id, patch)}
              onDuplicate={duplicateBlock}
              onDelete={deleteBlock}
            />
          )}
          {tab === 'json' && (
            <JsonTab jsonDraft={jsonDraft} onDraft={setJsonDraft} onImport={importJson} />
          )}
        </div>
      </aside>
    </div>
  );
}

/* ─── PAGE CANVAS ─────────────────────────────── */
function PageCanvas({ page, selectedId, zoom, onSelect, onUpdateBlock }) {
  const wrapRef = useRef(null);
  const ref = useRef(null);

  const startDrag = (e, block, mode) => {
    e.stopPropagation();
    onSelect(block.id);
    const box = ref.current.getBoundingClientRect();
    const ratio = 148 / box.width;
    const ox = e.clientX, oy = e.clientY;
    const sx = block.x, sy = block.y, sw = block.w, sh = block.h;

    const move = (ev) => {
      const dx = (ev.clientX - ox) * ratio;
      const dy = (ev.clientY - oy) * ratio;
      if (mode === 'resize') {
        onUpdateBlock(block.id, { w: clamp(sw + dx, 20, 140 - sx), h: clamp(sh + dy, 10, 200 - sy - 20) });
      } else {
        onUpdateBlock(block.id, { x: clamp(sx + dx, 0, 140 - sw), y: clamp(sy + dy, 22, 190 - sh) });
      }
    };
    const up = () => { window.removeEventListener('pointermove', move); window.removeEventListener('pointerup', up); };
    window.addEventListener('pointermove', move);
    window.addEventListener('pointerup', up);
  };

  // Le wrapper gère la place que prend la page scalée dans le flux
  const PAGE_W_PX = 148 / 25.4 * 96; // 148mm en px
  const PAGE_H_PX = 210 / 25.4 * 96; // 210mm en px
  const wrapStyle = {
    width:  Math.round(PAGE_W_PX * zoom),
    height: Math.round(PAGE_H_PX * zoom),
    position: 'relative',
    flexShrink: 0,
  };
  const pageStyle = {
    transform: `scale(${zoom})`,
    transformOrigin: 'top left',
    position: 'absolute',
    top: 0, left: 0,
  };

  return (
    <div style={wrapStyle} ref={wrapRef}>
    <div
      className={`page theme-${page.theme}`}
      style={pageStyle}
      ref={ref}
      onPointerDown={() => onSelect(null)}
    >
      {/* Blobs décoratifs V3 */}
      <div className="page-blobs" aria-hidden="true">
        <svg width="90" height="90" viewBox="0 0 90 90" style={{position:'absolute',top:-15,right:-15}}>
          <ellipse cx="30" cy="60" rx="40" ry="32" fill="#2563eb18" transform="rotate(-30 30 60)"/>
          <circle cx="70" cy="20" r="18" fill="#2563eb10"/>
        </svg>
        <svg width="80" height="70" viewBox="0 0 80 70" style={{position:'absolute',bottom:18,left:-10}}>
          <ellipse cx="55" cy="40" rx="36" ry="28" fill="#2563eb18" transform="rotate(20 55 40)"/>
        </svg>
      </div>

      {/* Spirale */}
      <div className="spiral" aria-hidden="true" />

      {/* Header */}
      <header className="page-header">
        <div className="page-header-info">
          <strong>Major 6AF ✦</strong>
          <span>{page.lesson}</span>
        </div>
        <div className="page-mascot">🐪</div>
      </header>

      <div className="safe-zone" />

      {/* Blocks */}
      {page.blocks.map(block => (
        <Block
          key={block.id}
          block={block}
          selected={block.id === selectedId}
          onPointerDown={startDrag}
        />
      ))}

      {/* Footer */}
      <footer className="qr-footer">
        <div className="qr-box">QR</div>
        <div className="qr-text">
          <strong>📷 امسح الرمز بهاتفك</strong>
          <span>{page.footer}</span>
        </div>
        <em className="qr-page">{page.title}</em>
      </footer>
    </div>
    </div>
  );
}

/* ─── BLOCK ───────────────────────────────────── */
function Block({ block, selected, onPointerDown }) {
  const baseStyle = {
    position: 'absolute',
    left: mm(block.x), top: mm(block.y),
    width: mm(block.w), height: mm(block.h),
    touchAction: 'none',
    zIndex: 10,
    boxSizing: 'border-box',
    overflow: 'hidden',
  };

  // ── Bloc HTML réel (V3-Cartoon) ──
  if (block.html) {
    return (
      <div
        className={selected ? 'block-raw-selected' : ''}
        style={{
          ...baseStyle,
          outline: selected ? '3px solid #F0B429' : 'none',
          outlineOffset: '2px',
          cursor: 'move',
        }}
        onPointerDown={e => onPointerDown(e, block, 'move')}
      >
        <div
          style={{ width: '100%', height: '100%', pointerEvents: 'none' }}
          dangerouslySetInnerHTML={{ __html: block.html }}
        />
        <span
          className="resize-handle"
          onPointerDown={e => onPointerDown(e, block, 'resize')}
          style={{ pointerEvents: 'all' }}
        />
      </div>
    );
  }

  return (
    <article
      className={`block block-${block.variant ?? 'cartoon'} ${selected ? 'selected' : ''}`}
      style={{ left: mm(block.x), top: mm(block.y), width: mm(block.w), height: mm(block.h) }}
      onPointerDown={e => onPointerDown(e, block, 'move')}
    >
      {block.type === 'section' && (
        <div className="sec-label">
          <span className="sec-star">✎</span>
          <span>{block.title}</span>
        </div>
      )}

      {block.type === 'rule' && (
        <>
          <h3>📌 {block.title}</h3>
          <p>{block.text}</p>
        </>
      )}

      {block.type === 'exercise' && (
        <>
          <div className="block-head">
            <div style={{display:'flex',alignItems:'center',gap:5,flexDirection:'row-reverse'}}>
              <span
                style={{width:28,height:28,borderRadius:'50%',background:'linear-gradient(135deg,#2563eb,#38bdf8)',
                  border:'2px solid #111',boxShadow:'2px 2px 0 #111',display:'grid',placeItems:'center',
                  fontSize:11,fontWeight:900,color:'#fff',flexShrink:0}}>
                ✎
              </span>
              <span className="badge">تمرين</span>
              <span style={{fontSize:9,color:'#2563eb',fontWeight:900}}>◀</span>
              <span className="level">⭐ سهل</span>
            </div>
            <span className="pts">4 نقاط</span>
          </div>
          <h3 style={{marginBottom:3}}>{block.title}</h3>
          {block.text && <p className="example">{block.text}</p>}
          <div className="items-grid">
            {[1,2,3,4].map(n => (
              <div className="ex-item" key={n}>
                <div className="ex-item-top"><b>{n}</b><span>عنصر {n}</span></div>
                <i /><i />
              </div>
            ))}
          </div>
        </>
      )}

      {block.type === 'table' && (
        <>
          <h3>{block.title}</h3>
          <table>
            <thead><tr><th>المفرد</th><th>الجمع</th></tr></thead>
            <tbody>{[1,2,3].map(r => <tr key={r}><td>كلمة</td><td /></tr>)}</tbody>
          </table>
        </>
      )}

      {block.type === 'writing' && (
        <>
          <h3>{block.title}</h3>
          <div className="writing-lines">{[1,2,3,4].map(n => <i key={n}/>)}</div>
        </>
      )}

      <span className="resize-handle" onPointerDown={e => onPointerDown(e, block, 'resize')} />
    </article>
  );
}

/* ─── INSPECTORS ──────────────────────────────── */
function PageInspector({ page, onUpdate }) {
  return (
    <>
      <div className="inspector-section">
        <p className="inspector-section-title">Infos de la page</p>
        <Field label="Nom" value={page.title}  onChange={v => onUpdate({ title: v })} />
        <Field label="Leçon / matière" value={page.lesson} onChange={v => onUpdate({ lesson: v })} />
        <Field label="Texte footer QR" value={page.footer} onChange={v => onUpdate({ footer: v })} />
      </div>

      <div className="inspector-section">
        <p className="inspector-section-title">Thème couleur</p>
        <div className="theme-grid">
          {THEMES.map(t => (
            <button
              key={t.id}
              className={`theme-dot ${page.theme === t.id ? 'active' : ''}`}
              style={{ background: t.bg }}
              onClick={() => onUpdate({ theme: t.id })}
              title={t.label}
            >
              {t.label.slice(0,3)}
            </button>
          ))}
        </div>
      </div>
    </>
  );
}

function BlockInspector({ selected, onUpdate, onDuplicate, onDelete }) {
  if (!selected) {
    return (
      <div className="no-selection">
        <div className="icon-big">✦</div>
        <p>Clique sur un bloc dans la page pour l'éditer.</p>
      </div>
    );
  }
  return (
    <>
      <div className="inspector-section">
        <p className="inspector-section-title">Contenu</p>
        <Field label="Titre / consigne" value={selected.title} onChange={v => onUpdate({ title: v })} />
        <div className="field">
          <label>Texte / exemple</label>
          <textarea value={selected.text} onChange={e => onUpdate({ text: e.target.value })} />
        </div>
      </div>

      <div className="inspector-section">
        <p className="inspector-section-title">Style</p>
        <div className="variant-grid">
          {VARIANTS.map(v => (
            <button
              key={v.id}
              className={`variant-chip ${selected.variant === v.id ? 'active' : ''}`}
              onClick={() => onUpdate({ variant: v.id })}
            >
              {v.label}
            </button>
          ))}
        </div>
      </div>

      <div className="inspector-section">
        <p className="inspector-section-title">Position & taille (mm)</p>
        <div className="grid-2">
          <NumField label="X" value={selected.x} onChange={v => onUpdate({ x: v })} />
          <NumField label="Y" value={selected.y} onChange={v => onUpdate({ y: v })} />
          <NumField label="Largeur" value={selected.w} onChange={v => onUpdate({ w: v })} />
          <NumField label="Hauteur" value={selected.h} onChange={v => onUpdate({ h: v })} />
        </div>
      </div>

      <div className="block-actions">
        <button className="btn sm" onClick={onDuplicate}><Ic n="dup" s={13} /> Dupliquer</button>
        <button className="btn sm danger" onClick={onDelete}><Ic n="trash" s={13} /> Supprimer</button>
      </div>
    </>
  );
}

function JsonTab({ jsonDraft, onDraft, onImport }) {
  return (
    <>
      <div className="inspector-section">
        <p className="inspector-section-title">Export / Import JSON</p>
        <textarea
          className="json-box"
          value={jsonDraft}
          onChange={e => onDraft(e.target.value)}
          spellCheck={false}
        />
      </div>
      <div style={{ display:'flex', gap:8, flexWrap:'wrap' }}>
        <button className="btn primary sm" onClick={onImport}><Ic n="upload" s={13} /> Importer</button>
        <button className="btn sm" onClick={() => navigator.clipboard?.writeText(jsonDraft)}>
          <Ic n="copy" s={13} /> Copier
        </button>
      </div>
    </>
  );
}

/* ─── FIELDS ──────────────────────────────────── */
function Field({ label, value, onChange }) {
  return (
    <div className="field">
      <label>{label}</label>
      <input value={value} onChange={e => onChange(e.target.value)} />
    </div>
  );
}
function NumField({ label, value, onChange }) {
  return (
    <div className="field">
      <label>{label}</label>
      <input type="number" value={value} onChange={e => onChange(Number(e.target.value))} />
    </div>
  );
}

createRoot(document.getElementById('root')).render(<App />);
