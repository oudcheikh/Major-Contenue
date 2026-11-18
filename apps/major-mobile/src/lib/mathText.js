// Conversion des formules LaTeX inline ($...$) en texte Unicode lisible.
// Le web rend le même contenu avec KaTeX ; ici on reste en texte natif
// (pas de WebView par formule : trop lourd pour les quiz).

const SUPERSCRIPTS = { 0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹', '-': '⁻', '−': '⁻', '+': '⁺', n: 'ⁿ', m: 'ᵐ' }

function toSuperscript(str) {
  const out = [...str].map((c) => SUPERSCRIPTS[c])
  return out.every(Boolean) ? out.join('') : `^(${str})`
}

function convertLatex(tex) {
  let s = tex
  // \frac{a}{b} → a/b (parenthésé si composé), répété pour les fractions imbriquées simples
  for (let i = 0; i < 3; i++) {
    s = s.replace(/\\[dt]?frac\{([^{}]+)\}\{([^{}]+)\}/g, (_, a, b) => {
      const wrap = (x) => (/^[-−]?[\w.,'π]+$/.test(x) ? x : `(${x})`)
      return `${wrap(a)}/${wrap(b)}`
    })
  }
  // \sqrt{x} et \sqrt x
  s = s.replace(/\\sqrt\{([^{}]+)\}/g, (_, a) => (/^[\w.,]+$/.test(a) ? `√${a}` : `√(${a})`))
  s = s.replace(/\\sqrt ?(\w+)/g, '√$1')
  // \vec{AB} → AB⃗
  s = s.replace(/\\vec\{([^{}]+)\}/g, '$1⃗')
  // \text{...} et \mathrm{...}
  s = s.replace(/\\(?:text|mathrm)\{([^{}]+)\}/g, '$1')
  // Exposants ^{...} et ^x
  s = s.replace(/\^\{([^{}]+)\}/g, (_, a) => toSuperscript(a))
  s = s.replace(/\^([0-9nm])/g, (_, a) => toSuperscript(a))
  // Indices simples _{...} / _x
  s = s.replace(/_\{([^{}]+)\}/g, '$1')
  s = s.replace(/_([0-9A-Za-z])/g, '$1')
  // Degrés et fonctions trigonométriques
  s = s.replace(/\^\{?\\circ\}?/g, '°')
  // Symboles courants
  const MAP = {
    '\\cos': 'cos', '\\sin': 'sin', '\\tan': 'tan',
    '\\times': '×', '\\cdot': '·', '\\div': '÷', '\\pi': 'π',
    '\\le': '≤', '\\leq': '≤', '\\ge': '≥', '\\geq': '≥', '\\ne': '≠', '\\neq': '≠',
    '\\in': '∈', '\\subset': '⊂', '\\infty': '∞', '\\approx': '≈',
    '\\Leftrightarrow': '⟺', '\\Rightarrow': '⟹', '\\to': '→', '\\rightarrow': '→',
    '\\parallel': '∥', '\\perp': '⊥', '\\degree': '°', '\\%': '%',
    '\\mathbb{R}': 'ℝ', '\\mathbb{Q}': 'ℚ', '\\mathbb{Z}': 'ℤ', '\\mathbb{N}': 'ℕ', '\\mathbb{D}': '𝔻',
  }
  for (const [k, v] of Object.entries(MAP)) s = s.split(k).join(v)
  // Espaces LaTeX (\, \; \! \quad) et nettoyage final
  s = s.replace(/\\[,;!]/g, '').replace(/\\quad/g, ' ')
  s = s.replace(/\\[a-zA-Z]+/g, ' ').replace(/[{}\\]/g, '').replace(/\s+/g, ' ').trim()
  return s
}

// « Le volume vaut $V = \frac{1}{3} \times B \times h$ » → « Le volume vaut V = 1/3 × B × h »
export function plainMath(text) {
  const s = String(text ?? '')
  if (!s.includes('$')) return s
  return s.replace(/\$([^$]+)\$/g, (_, tex) => convertLatex(tex))
}
