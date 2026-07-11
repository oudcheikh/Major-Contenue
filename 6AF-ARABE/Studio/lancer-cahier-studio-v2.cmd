@echo off
cd /d "%~dp0cahier-studio-v2"
echo.
echo  ╔═══════════════════════════════════╗
echo  ║   Cahier Studio V2 — Major 6AF   ║
echo  ╠═══════════════════════════════════╣
echo  ║  URL : http://127.0.0.1:5174     ║
echo  ║  Design System Major             ║
echo  ╚═══════════════════════════════════╝
echo.
echo  La fenetre doit rester ouverte pendant l'utilisation.
echo.
python -m http.server 5174 --bind 127.0.0.1 --directory dist
pause
