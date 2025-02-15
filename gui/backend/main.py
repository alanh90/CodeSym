# gui/backend/main.py

import os
import subprocess
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Determine the base directory (two levels up from this file)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

templates = Jinja2Templates(directory=TEMPLATE_DIR)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Serves the main HTML page.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/run_codesym")
async def run_codesym():
    """
    Runs the CodeSym main script (src/main.py) as a subprocess.
    """
    try:
        # Adjust the command as needed—here we use the embedded Python to run src/main.py
        command = [
            os.path.join(os.getcwd(), "python_embedded", "python-3.11.0-embed-amd64", "python.exe"),
            "src/main.py"
        ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Not waiting for the process to complete—return immediately.
        return {"status": "success", "message": "CodeSym started."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.get("/get_output", response_class=JSONResponse)
async def get_output():
    """
    Reads the contents of the output file and returns it.
    """
    try:
        with open("output.txt", "r") as f:
            content = f.read()
        return {"status": "success", "output": content}
    except FileNotFoundError:
        return {"status": "error", "message": "Output file not found."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
