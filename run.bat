@echo off
setlocal

REM --- Configuration ---
set "PY_EMBED=python_embedded\python-3.11.0-embed-amd64\python.exe"
set "BACKEND_SCRIPT=gui.backend.main:app"
set "UVICORN_OPTIONS=--reload --port 8001"
set "BROWSER_URL=http://localhost:8001"

REM --- Change to the script's directory ---
cd /d "%~dp0"
echo Current directory: %cd%

REM --- Launch the FastAPI GUI backend in a new window ---
echo Starting the GUI backend...
start "GUI Backend" %PY_EMBED% -s -m uvicorn %BACKEND_SCRIPT% %UVICORN_OPTIONS%

REM --- Wait a few seconds ---
timeout /t 3 > nul

REM --- Open the default browser ---
echo Launching browser at %BROWSER_URL%...
start "" "%BROWSER_URL%"

echo.
echo Application is running. Press any key to exit.
pause
endlocal
