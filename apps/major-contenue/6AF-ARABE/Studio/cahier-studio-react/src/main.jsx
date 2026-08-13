import React, { useEffect, useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

function Icon({ name, size = 16 }) {
  const common = {
    width: size,
    height: size,
    viewBox: '0 0 24 24',
    fill: 'none',
    stroke: 'currentColor',
    strokeWidth: 2,
    strokeLinecap: 'round',
    strokeLinejoin: 'round',
    'aria-hidden': true,
  };
  const paths = {
    book: [<path key="1" d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />, <path key="2" d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5z" />],
    copy: [<rect key="1" x="9" y="9" width="13" height="13" rx="2" />, <path key="2" d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />],
    filePlus: [<path key="1" d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />, <path key="2" d="M14 2v6h6" />, <path key="3" d="M12 18v-6" />, <path key="4" d="M9 15h6" />],
    minus: [<path key="1" d="M5 12h14" />],
    palette: [<path key="1" d="M12 22a10 10 0 1 1 10-10c0 2-1 3-3 3h-2a2 2 0 0 0-2 2c0 2-1 5-3 5z" />, <circle key="2" cx="7.5" cy="10.5" r=".5" />, <circle key="3" cx="12" cy="7.5" r=".5" />, <circle key="4" cx="16.5" cy="10.5" r=".5" />],
    plus: [<path key="1" d="M12 5v14" />, <path key="2" d="M5 12h14" />],
    printer: [<path key="1" d="M6 9V2h12v7" />, <path key="2" d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2" />, <path key="3" d="M6 14h12v8H6z" />],
    pen: [<path key="1" d="M12 20h9" />, <path key="2" d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z" />],
    trash: [<path key="1" d="M3 6h18" />, <path key="2" d="M8 6V4h8v2" />, <path key="3" d="M19 6l-1 16H6L5 6" />],
    upload: [<path key="1" d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />, <path key="2" d="M17 8l-5-5-5 5" />, <path key="3" d="M12 3v12" />],
  };
  return <svg {...common}>{paths[name]}</svg>;
}

const uid = () => Math.random().toString(36).slice(2, 9);
const clamp = (value, min, max) => Math.max(min, Math.min(max, value));
const mm = (value) => `${value}mm`;

const templates = {
  section: {
    type: 'section',
    title: '✎ عنوان الدرس',
    text: '',
    x: 47,
    y: 27,
    w: 86,
    h: 11,
    variant: 'section',
  },
  rule: {
    type: 'rule',
    title: 'القاعدة',
    text: 'اكتب هنا قاعدة الدرس بشكل مختصر وواضح.',
    x: 7,
    y: 41,
    w: 126,
    h: 18,
    variant: 'rule',
  },
  exercise: {
    type: 'exercise',
    title: 'أعرب الكلمات التي تحتها خط :',
    text: 'مثال: الجهل ظلام — الجهل: مبتدأ مرفوع.',
    x: 49,
    y: 67,
    w: 87,
    h: 51,
    variant: 'cartoon',
  },
  wide: {
    type: 'exercise',
    title: 'أكمل الجدول بما يناسب :',
    text: 'استعمل الكلمات المناسبة في الفراغات.',
    x: 7,
    y: 67,
    w: 126,
    h: 43,
    variant: 'cartoon',
  },
  table: {
    type: 'table',
    title: 'أكمل الجدول :',
    text: '',
    x: 7,
    y: 112,
    w: 70,
    h: 56,
    variant: 'soft',
  },
  writing: {
    type: 'writing',
    title: 'ركب جملة مفيدة :',
    text: '',
    x: 7,
    y: 153,
    w: 126,
    h: 32,
    variant: 'minimal',
  },
};

const createPage = (index) => ({
  id: uid(),
  title: `Page ${index}`,
  theme: 'blue',
  lesson: 'اللغة العربية — نموذج الدرس',
  footer: 'نموذج مستقل لصناعة الكراسات',
  blocks: [
    { ...templates.section, id: uid() },
    { ...templates.rule, id: uid() },
    { ...templates.exercise, id: uid() },
  ],
});

function App() {
  const [project, setProject] = useState(() => {
    const saved = localStorage.getItem('major-cahier-studio');
    return saved ? JSON.parse(saved) : { pages: [createPage(1)] };
  });
  const [pageId, setPageId] = useState(project.pages[0].id);
  const [selectedId, setSelectedId] = useState(project.pages[0].blocks[0]?.id ?? null);
  const [zoom, setZoom] = useState(0.86);
  const [jsonDraft, setJsonDraft] = useState('');

  const page = project.pages.find((candidate) => candidate.id === pageId) ?? project.pages[0];
  const selected = page.blocks.find((block) => block.id === selectedId) ?? null;

  useEffect(() => {
    localStorage.setItem('major-cahier-studio', JSON.stringify(project));
    setJsonDraft(JSON.stringify(project, null, 2));
  }, [project]);

  const updatePage = (patch) => {
    setProject((current) => ({
      pages: current.pages.map((candidate) =>
        candidate.id === page.id ? { ...candidate, ...patch } : candidate
      ),
    }));
  };

  const updateBlock = (blockId, patch) => {
    setProject((current) => ({
      pages: current.pages.map((candidate) =>
        candidate.id === page.id
          ? {
              ...candidate,
              blocks: candidate.blocks.map((block) =>
                block.id === blockId ? { ...block, ...patch } : block
              ),
            }
          : candidate
      ),
    }));
  };

  const addPage = () => {
    const next = createPage(project.pages.length + 1);
    setProject((current) => ({ pages: [...current.pages, next] }));
    setPageId(next.id);
    setSelectedId(next.blocks[0]?.id ?? null);
  };

  const addBlock = (kind) => {
    const source = templates[kind];
    const block = {
      ...source,
      id: uid(),
      x: source.x + page.blocks.length * 2,
      y: source.y + page.blocks.length * 2,
    };
    setProject((current) => ({
      pages: current.pages.map((candidate) =>
        candidate.id === page.id
          ? { ...candidate, blocks: [...candidate.blocks, block] }
          : candidate
      ),
    }));
    setSelectedId(block.id);
  };

  const duplicateBlock = () => {
    if (!selected) return;
    const copyBlock = { ...selected, id: uid(), x: selected.x + 5, y: selected.y + 5 };
    setProject((current) => ({
      pages: current.pages.map((candidate) =>
        candidate.id === page.id
          ? { ...candidate, blocks: [...candidate.blocks, copyBlock] }
          : candidate
      ),
    }));
    setSelectedId(copyBlock.id);
  };

  const deleteBlock = () => {
    if (!selected) return;
    setProject((current) => ({
      pages: current.pages.map((candidate) =>
        candidate.id === page.id
          ? { ...candidate, blocks: candidate.blocks.filter((block) => block.id !== selected.id) }
          : candidate
      ),
    }));
    setSelectedId(null);
  };

  const importProject = () => {
    const parsed = JSON.parse(jsonDraft);
    if (!parsed.pages?.length) return;
    setProject(parsed);
    setPageId(parsed.pages[0].id);
    setSelectedId(parsed.pages[0].blocks[0]?.id ?? null);
  };

  return (
    <div className="studio">
      <LeftPanel
        pages={project.pages}
        activePageId={page.id}
        onAddPage={addPage}
        onPickPage={(id) => {
          const nextPage = project.pages.find((candidate) => candidate.id === id);
          setPageId(id);
          setSelectedId(nextPage?.blocks[0]?.id ?? null);
        }}
        onAddBlock={addBlock}
      />

      <main className="canvasShell">
        <div className="topbar">
          <div className="floatingControls">
            <button className="iconButton" onClick={() => setZoom((value) => clamp(value - 0.08, 0.42, 1.25))} title="Zoom -">
              <Icon name="minus" size={17} />
            </button>
            <span>{Math.round(zoom * 100)}%</span>
            <button className="iconButton" onClick={() => setZoom((value) => clamp(value + 0.08, 0.42, 1.25))} title="Zoom +">
              <Icon name="plus" size={17} />
            </button>
          </div>
          <div className="floatingControls">
            <button className="button" onClick={() => window.print()}>
              <Icon name="printer" size={16} /> Imprimer A5
            </button>
            <button className="button dark" onClick={() => navigator.clipboard?.writeText(JSON.stringify(project, null, 2))}>
              <Icon name="copy" size={16} /> JSON
            </button>
          </div>
        </div>

        <PageCanvas
          page={page}
          selectedId={selectedId}
          zoom={zoom}
          onSelect={setSelectedId}
          onUpdateBlock={updateBlock}
        />
      </main>

      <RightPanel
        page={page}
        selected={selected}
        jsonDraft={jsonDraft}
        onJsonDraft={setJsonDraft}
        onImport={importProject}
        onUpdatePage={updatePage}
        onUpdateBlock={updateBlock}
        onDuplicate={duplicateBlock}
        onDelete={deleteBlock}
      />
    </div>
  );
}

function LeftPanel({ pages, activePageId, onAddPage, onPickPage, onAddBlock }) {
  const templateButtons = [
    ['section', 'Titre de section', 'Badge bleu comme V3'],
    ['rule', 'Règle / leçon', 'Encadré pédagogique'],
    ['exercise', 'Exercice 2 colonnes', 'Carte compacte'],
    ['wide', 'Exercice large', 'Pleine largeur'],
    ['table', 'Tableau', 'Colonnes réponses'],
    ['writing', 'Rédaction', 'Lignes libres'],
  ];

  return (
    <aside className="panel">
      <div className="brand">
        <div className="brandIcon">M</div>
        <div>
          <h1>Cahier Studio</h1>
          <p>éditeur React A5</p>
        </div>
      </div>

      <button className="button primary full" onClick={onAddPage}>
        <Icon name="filePlus" size={16} /> Ajouter une page
      </button>

      <h2>Pages</h2>
      <div className="pageList">
        {pages.map((page, index) => (
          <button
            key={page.id}
            className={`pageItem ${page.id === activePageId ? 'active' : ''}`}
            onClick={() => onPickPage(page.id)}
          >
            <span>
              <strong>{page.title}</strong>
              <small>{page.blocks.length} blocs</small>
            </span>
            <em>{String(index + 1).padStart(2, '0')}</em>
          </button>
        ))}
      </div>

      <h2>Bibliothèque</h2>
      {templateButtons.map(([kind, title, subtitle]) => (
        <button className="templateButton" key={kind} onClick={() => onAddBlock(kind)}>
          <strong>{title}</strong>
          <span>{subtitle}</span>
        </button>
      ))}
    </aside>
  );
}

function PageCanvas({ page, selectedId, zoom, onSelect, onUpdateBlock }) {
  const pageRef = useRef(null);

  const dragBlock = (event, block, mode) => {
    event.stopPropagation();
    onSelect(block.id);

    const box = pageRef.current.getBoundingClientRect();
    const mmPerPixel = 148 / box.width;
    const start = { ...block };
    const startX = event.clientX;
    const startY = event.clientY;

    const move = (moveEvent) => {
      const dx = (moveEvent.clientX - startX) * mmPerPixel;
      const dy = (moveEvent.clientY - startY) * mmPerPixel;

      if (mode === 'resize') {
        onUpdateBlock(block.id, {
          w: clamp(start.w + dx, 24, 148 - start.x),
          h: clamp(start.h + dy, 12, 210 - start.y - 18),
        });
      } else {
        onUpdateBlock(block.id, {
          x: clamp(start.x + dx, 0, 148 - start.w),
          y: clamp(start.y + dy, 22, 210 - start.h - 18),
        });
      }
    };

    const up = () => {
      window.removeEventListener('pointermove', move);
      window.removeEventListener('pointerup', up);
    };

    window.addEventListener('pointermove', move);
    window.addEventListener('pointerup', up);
  };

  return (
    <section
      className={`page theme-${page.theme}`}
      style={{ transform: `scale(${zoom})` }}
      ref={pageRef}
      onPointerDown={() => onSelect(null)}
    >
      <header className="pageHeader">
        <div>
          <strong>Major 6AF</strong>
          <span>{page.lesson}</span>
        </div>
        <div className="mascot"><Icon name="book" size={24} /></div>
      </header>
      <div className="spiral" />
      <div className="safeArea" />

      {page.blocks.map((block) => (
        <Block
          key={block.id}
          block={block}
          selected={block.id === selectedId}
          onPointerDown={dragBlock}
        />
      ))}

      <footer className="qrFooter">
        <div className="qrBox">QR</div>
        <div>
          <strong>امسح الرمز بهاتفك</strong>
          <span>{page.footer}</span>
        </div>
        <em>{page.title}</em>
      </footer>
    </section>
  );
}

function Block({ block, selected, onPointerDown }) {
  const className = `block block-${block.variant ?? 'cartoon'} ${selected ? 'selected' : ''}`;
  const style = {
    left: mm(block.x),
    top: mm(block.y),
    width: mm(block.w),
    height: mm(block.h),
  };

  return (
    <article className={className} style={style} onPointerDown={(event) => onPointerDown(event, block, 'move')}>
      {block.type === 'rule' && (
        <>
          <h3>{block.title}</h3>
          <p>{block.text}</p>
        </>
      )}

      {block.type === 'section' && (
        <h3>{block.title}</h3>
      )}

      {block.type === 'exercise' && (
        <>
          <div className="blockHead">
            <span>تمرين</span>
            <small>4 نقاط</small>
          </div>
          <h3>{block.title}</h3>
          <p className="example">{block.text}</p>
          <div className="itemsGrid">
            {[1, 2, 3, 4].map((item) => (
              <div className="exerciseItem" key={item}>
                <div className="itemTop"><b>{item}</b><span>عنصر {item}</span></div>
                <i />
                <i />
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
            <tbody>{[1, 2, 3].map((row) => <tr key={row}><td>كلمة</td><td /></tr>)}</tbody>
          </table>
        </>
      )}

      {block.type === 'writing' && (
        <>
          <h3>{block.title}</h3>
          <div className="writingLines">{[1, 2, 3, 4].map((line) => <i key={line} />)}</div>
        </>
      )}

      <span
        className="resizeHandle"
        onPointerDown={(event) => onPointerDown(event, block, 'resize')}
        title="Redimensionner"
      />
    </article>
  );
}

function RightPanel({
  page,
  selected,
  jsonDraft,
  onJsonDraft,
  onImport,
  onUpdatePage,
  onUpdateBlock,
  onDuplicate,
  onDelete,
}) {
  return (
    <aside className="panel right">
      <div className="brand">
        <div className="brandIcon alt"><Icon name="palette" size={18} /></div>
        <div>
          <h1>Inspecteur</h1>
          <p>contenu, style, export</p>
        </div>
      </div>

      <h2>Page</h2>
      <Field label="Nom page" value={page.title} onChange={(title) => onUpdatePage({ title })} />
      <Field label="Leçon" value={page.lesson} onChange={(lesson) => onUpdatePage({ lesson })} />
      <Field label="Footer QR" value={page.footer} onChange={(footer) => onUpdatePage({ footer })} />
      <label className="field">
        <span>Thème</span>
        <select value={page.theme} onChange={(event) => onUpdatePage({ theme: event.target.value })}>
          <option value="blue">Bleu Major</option>
          <option value="green">Vert islamique</option>
          <option value="purple">Violet moderne</option>
        </select>
      </label>

      <h2>Bloc</h2>
      {selected ? (
        <>
          <Field label="Titre / consigne" value={selected.title} onChange={(title) => onUpdateBlock(selected.id, { title })} />
          <label className="field">
            <span>Texte</span>
            <textarea value={selected.text} onChange={(event) => onUpdateBlock(selected.id, { text: event.target.value })} />
          </label>
          <label className="field">
            <span>Style</span>
            <select value={selected.variant} onChange={(event) => onUpdateBlock(selected.id, { variant: event.target.value })}>
              <option value="cartoon">Cartoon contour noir</option>
              <option value="soft">Doux bleu</option>
              <option value="glass">Verre moderne</option>
              <option value="minimal">Minimal</option>
              <option value="rule">Règle</option>
              <option value="section">Titre de section</option>
            </select>
          </label>
          <div className="miniGrid">
            <NumberField label="X" value={selected.x} onChange={(x) => onUpdateBlock(selected.id, { x })} />
            <NumberField label="Y" value={selected.y} onChange={(y) => onUpdateBlock(selected.id, { y })} />
            <NumberField label="L" value={selected.w} onChange={(w) => onUpdateBlock(selected.id, { w })} />
            <NumberField label="H" value={selected.h} onChange={(h) => onUpdateBlock(selected.id, { h })} />
          </div>
          <div className="actionRow">
            <button className="button" onClick={onDuplicate}><Icon name="pen" size={15} /> Dupliquer</button>
            <button className="button danger" onClick={onDelete}><Icon name="trash" size={15} /> Supprimer</button>
          </div>
        </>
      ) : (
        <p className="hint">Sélectionne un bloc sur la page.</p>
      )}

      <h2>Projet JSON</h2>
      <textarea className="jsonBox" value={jsonDraft} onChange={(event) => onJsonDraft(event.target.value)} />
      <div className="actionRow">
        <button className="button primary" onClick={onImport}><Icon name="upload" size={15} /> Importer</button>
      </div>
    </aside>
  );
}

function Field({ label, value, onChange }) {
  return (
    <label className="field">
      <span>{label}</span>
      <input value={value} onChange={(event) => onChange(event.target.value)} />
    </label>
  );
}

function NumberField({ label, value, onChange }) {
  return (
    <label className="field">
      <span>{label}</span>
      <input type="number" value={value} onChange={(event) => onChange(Number(event.target.value))} />
    </label>
  );
}

createRoot(document.getElementById('root')).render(<App />);
