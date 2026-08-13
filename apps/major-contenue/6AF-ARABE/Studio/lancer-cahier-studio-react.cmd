@echo off
cd /d "%~dp0cahier-studio-react"
echo.
echo Cahier Major Studio React
echo -------------------------
echo URL: http://127.0.0.1:5173
echo.
echo La fenetre doit rester ouverte pendant que tu utilises le site.
echo.
python -m http.server 5173 --bind 127.0.0.1 --directory dist
pause
