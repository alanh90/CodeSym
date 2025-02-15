@echo off
cd "%~dp0"
call venv\Scripts\activate.bat
python -m uvicorn gui.backend.main:app --reload --port 8001
pause