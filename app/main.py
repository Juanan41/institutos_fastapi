from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from app.database import Base, engine
from app.routers import institutos, estudiantes

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Institutos API")

# Routers API
app.include_router(institutos.router)
app.include_router(estudiantes.router)

# Jinja2
templates = Jinja2Templates(directory="app/templates")

# Archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Home
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "public/index.html",
        {"request": request}
    )
