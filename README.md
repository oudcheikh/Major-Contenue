# Cahier Major — 6AF (Mauritanie)

Cahiers de révision intelligents A5 en arabe (RTL), connectés à l'app Major via QR codes.
Programme officiel mauritanien (IPN) — 6ème année fondamentale, préparation au concours.

## Structure du projet

```
livrables/      → PDFs finaux prêts à imprimer + leurs sources HTML
generateurs/    → scripts Python qui produisent les cahiers
sources/        → matière première (pptx d'origine, PDFs de référence IPN)
apps/           → applications liées (web, API, contenu Major)
notes/          → prompts de design, accès
archives/       → anciennes versions remplacées
```

## Livrables (`livrables/`)

| Fichier | Description |
|---|---|
| `Cahier-Major-Math-Sciences-6AF-A5.pdf` | **Maths + Sciences combiné** — 159 p. : 31 unités maths + 6 فصول sciences |
| `Cahier-Major-Math-6AF-A5.pdf` | Version maths seule — 31 unités |
| `Cahier-Major-Arabe-Islamique-6AF-A5.pdf` | Arabe + Éducation islamique — 96 p. : 18 unités عربية + 8 فصول إسلامية |
| `Cahier-Major-HistGeo-Civique-6AF-A5.pdf` | Histoire-Géo + Civique — 72 p. : 9 unités تاريخ + 9 جغرافيا + 7 تربية مدنية, 2 مسابقات تجريبيتين + بنك أسئلة الخريطة |
| `*.SOURCE.html` | Sources HTML (impression → PDF via navigateur, format A5) |

## Générateurs (`generateurs/`)

- **`math-a5/`** — générateur actuel du cahier A5.
  Contenu : `unites_1..5.py` (31 unités maths), `sciences_1..2.py` (6 فصول),
  `base_a5.py` (gabarit/CSS), `qr_major.py` (QR codes).
  **Build : `generateurs/.venv/bin/python generateurs/math-a5/build_a5.py`** → écrit dans `livrables/`.
  (venv : `python3 -m venv generateurs/.venv && generateurs/.venv/bin/pip install -r generateurs/requirements.txt`)
- **`arabe-islamique-a5/`** — cahier arabe + islamique (build : `generateurs/.venv/bin/python generateurs/arabe-islamique-a5/build_ai.py`).
- **`histoire-geo-civique-a5/`** — cahier histoire-géo + civique.
  Contenu : `unites_hist/geo/civ.py` (9+9+7 unités), `assets_hgc.py` (cartes SVG dont contour Mauritanie et planisphère issus de GeoJSON réels), `base_hgc.py`, `build_hgc.py`.
  QR : histoire+géo partagent la matière `hg6` (géo numérotée u10–u18 à la suite de l'histoire), civique = `civ6`.
  **Build : `generateurs/.venv/bin/python generateurs/histoire-geo-civique-a5/build_hgc.py`** → écrit dans `livrables/`.
- **PDF final** : `google-chrome --headless=new --no-pdf-header-footer --virtual-time-budget=30000 --print-to-pdf=X.pdf "file://…/X.SOURCE.html"`
- **`math-html/`** — ancien générateur HTML 17 pages (déprécié) → écrit dans `archives/`.
- **`sciences-pptx/`** — pptx sciences d'origine + script de traduction RTL.

## Sources (`sources/`)

- `pptx/` — les pptx d'origine : `math_principal.pptx` (FR), `_ar` (arabe), `_ar_A5`, `_ar_A5_scan`.
- `references/` — manuels officiels arabes (كتاب الرياضيات السنة السادسة, دروس مدارس المعارف).

## Apps (`apps/`)

- `major-web/` — front Vite/React (repo git : github.com/oudcheikh/major-web).
- `math-api/` — API FastAPI maths. ⚠️ le `.venv` a été déplacé → le recréer :
  `cd apps/math-api && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`
- `major-contenue/` — workspace contenu Major (cahiers 4AF/6AF, QR codes, tutor-api, outils). Possède son propre `CLAUDE.md`.

## Positionnement produit

« Cahier intelligent » de révision pour élève + parents (pas un manuel scolaire).
Impression locale à bas coût, noir + 1 couleur d'accent, scan mobile par QR code.
