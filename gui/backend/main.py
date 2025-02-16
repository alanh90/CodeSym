import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Set up directories for templates and static files.
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

templates = Jinja2Templates(directory=TEMPLATE_DIR)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# In–memory storage for API settings, active agents, debug logs.
api_config = {}
active_agents = ["Manager AI", "Function AI 1", "Function AI 2", "Planning Agent"]
debug_logs = ["[DEBUG] System initialized."]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/save_settings")
async def save_settings(request: Request):
    global api_config
    try:
        data = await request.json()
        api_config = data  # Save the API key configuration.
        debug_logs.append("[DEBUG] Settings updated.")
        return JSONResponse({"status": "success", "message": "Settings saved."})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)})

@app.get("/active_agents")
async def get_active_agents():
    return JSONResponse({"status": "success", "agents": active_agents})

@app.get("/debug_logs")
async def get_debug_logs():
    return JSONResponse({"status": "success", "logs": debug_logs})

# New endpoint: Prompt the Manager AI.
@app.post("/prompt_manager")
async def prompt_manager(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    # For demonstration, we echo back the prompt.
    response_text = f"Manager AI says: You asked: '{prompt}'"
    debug_logs.append(f"[DEBUG] Manager prompt received: {prompt}")
    return JSONResponse({"status": "success", "response": response_text})
