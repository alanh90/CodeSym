@echo off
setlocal

REM --- Configuration ---
set "VENV_NAME=venv"
set "PYTHON_EXECUTABLE=python"  REM Use "python3" if "python" doesn't work
set "MAIN_SCRIPT=gui.backend.main:app"
set "UVICORN_OPTIONS=--reload --port 8001"

REM --- Get the script's directory ---
cd /d "%~dp0"

REM --- Check if virtual environment exists ---
if not exist "%VENV_NAME%\Scripts\activate.bat" (
    echo Creating virtual environment (%VENV_NAME%)...
    %PYTHON_EXECUTABLE% -m venv "%VENV_NAME%"
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment.
        pause
        exit /b 1
    )
)

REM --- Activate the virtual environment ---
call "%VENV_NAME%\Scripts\activate.bat"
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment.
    pause
    exit /b 1
)

REM --- Check if required packages are installed ---
where /q uvicorn
if errorlevel 1 (
    echo Installing required packages (FastAPI, Uvicorn, Jinja2)...
    pip install fastapi uvicorn Jinja2
    if errorlevel 1 (
        echo ERROR: Failed to install required packages.
        pause
        exit /b 1
    )
    pip freeze > requirements.txt
)

REM --- Run the application ---
echo Running CodeSym...
python -m uvicorn %MAIN_SCRIPT% %UVICORN_OPTIONS%

pause
endlocal