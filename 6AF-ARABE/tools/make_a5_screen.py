#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transforme Cahier-Major-LangueArabe-Islamique-6AF-V3-Cartoon.html
en affichage A5 dans le navigateur (ecran + impression).
"""

SRC = r"c:\Users\PC\Documents\Major-Contenue\6AF-ARABE\Cahier-Major-LangueArabe-Islamique-6AF-V3-Cartoon.html"
OUT = r"c:\Users\PC\Documents\Major-Contenue\6AF-ARABE\Cahier-Major-LangueArabe-Islamique-6AF-A5.html"

A5_CSS = """
<style id="a5-screen-style">
/* ════ Affichage A5 ecran ════ */
@media screen {
  html { background: #d0d8e8; }
  body { background: #d0d8e8 !important; margin: 0; padding: 20px 0; }

  /* Chaque .page devient 148x210mm (A5) */
  .page {
    width:  148mm !important;
    height: 210mm !important;
    min-height: 210mm !important;
    overflow: hidden !important;
    position: relative !important;
    margin: 20px auto !important;
    padding: 0 !important;
    box-shadow: 0 20px 60px rgba(0,0,0,.4) !important;
  }

  /* Le scaler interne : contenu A4 ramene a A5 */
  .a5-scaler {
    position: absolute !important;
    top: 0 !important;
    right: 0 !important;
    width:  210mm !important;
    height: 297mm !important;
    transform: scale(0.7047619) !important;
    transform-origin: top right !important;
    background: inherit !important;
  }
}
</style>
"""

A5_JS = """
<script id="a5-screen-script">
(function () {
  /* Ne rien faire si on imprime */
  if (window.matchMedia && window.matchMedia('print').matches) return;

  function wrapPages() {
    document.querySelectorAll('.page').forEach(function (page) {
      /* Deja wrappe ? */
      if (page.querySelector('.a5-scaler')) return;

      var scaler = document.createElement('div');
      scaler.className = 'a5-scaler';

      /* Deplacer tous les enfants dans le scaler */
      while (page.firstChild) scaler.appendChild(page.firstChild);
      page.appendChild(scaler);
    });
  }

  /* Executer apres chargement complet */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wrapPages);
  } else {
    wrapPages();
  }
})();
</script>
"""

with open(SRC, 'r', encoding='utf-8') as f:
    html = f.read()

# Injecter le CSS juste avant </head>
html = html.replace('</head>', A5_CSS + '</head>', 1)

# Injecter le JS juste avant </body>
html = html.replace('</body>', A5_JS + '</body>', 1)

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print('OK ->', OUT)
size_kb = len(html) // 1024
print('Taille:', size_kb, 'KB')
