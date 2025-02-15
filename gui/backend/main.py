# gui/backend/main.py
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import subprocess

app = FastAPI()

# Configure templates
templates = Jinja2Templates(directory="gui/frontend/templates")
# Mount static files directory
app.mount("/static", StaticFiles(directory="gui/frontend/static"), name="static")
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
        # Run src/main.py as a subprocess
        process = subprocess.Popen(["python", "src/main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Do NOT call process.communicate() here!

        return {"status": "success", "message": "CodeSym started."}  # Return immediately

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