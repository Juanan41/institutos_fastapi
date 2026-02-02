# ================================
# Clase principal de FastAPI
# ================================
from fastapi import FastAPI, Request

# ================================
# Servir archivos estáticos (CSS, JS, imágenes)
# ================================
from fastapi.staticfiles import StaticFiles

# ================================
# Motor de plantillas Jinja2
# ================================
from fastapi.templating import Jinja2Templates

# ================================
# Base y motor de base de datos
# ================================
from app.database import Base, engine

# ================================
# Routers de la aplicación (API REST)
# ================================
from app.routers.institutos import router as institutos_router
from app.routers.estudiantes import router as estudiantes_router

# ================================
# Dependencias de base de datos
# ================================
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

# ================================
# Servicios (lógica de negocio)
# ================================
from app.services.instituto_service import InstitutoService
from app.services.estudiante_service import EstudianteService


# ================================
# Crear tablas en BD si no existen
# ================================
Base.metadata.create_all(bind=engine)

# ================================
# Crear instancia principal FastAPI
# ================================
app = FastAPI(title="Institutos API")

# ================================
# Registrar routers API
# ================================
app.include_router(institutos_router)
app.include_router(estudiantes_router)

# ================================
# Configurar motor de plantillas
# ================================
templates = Jinja2Templates(directory="app/templates")

# ================================
# Crear instancias de servicios
# ================================
instituto_service = InstitutoService()
estudiante_service = EstudianteService()

# ================================
# Montar carpeta de archivos estáticos
# ================================
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# ================================
# Página principal
# ================================
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "public/index.html",
        {"request": request}
    )


# ================================
# Página web: listado de institutos
# ================================
@app.get("/institutos", include_in_schema=False)
def web_institutos(request: Request, db: Session = Depends(get_db)):
    institutos = instituto_service.find_all(db)
    return templates.TemplateResponse(
        "institutos/list.html",
        {"request": request, "institutos": institutos}
    )

# ================================
# Página web: listado de estudiantes
# ================================
@app.get("/estudiantes", include_in_schema=False)
def web_estudiantes(request: Request, db: Session = Depends(get_db)):
    estudiantes = estudiante_service.find_all(db)
    return templates.TemplateResponse(
        "estudiantes/list.html",
        {"request": request, "estudiantes": estudiantes}
    )

# -------------------------------
# FORMULARIO NUEVO INSTITUTO
# -------------------------------
@app.get("/institutos/nuevo", include_in_schema=False)
def formulario_instituto(request: Request):
    return templates.TemplateResponse(
        "formulario/instituto-form.html",
        {"request": request}
    )


# -------------------------------
# FORMULARIO NUEVO ESTUDIANTE
# -------------------------------
@app.get("/estudiantes/nuevo", include_in_schema=False)
def formulario_estudiante(request: Request, db: Session = Depends(get_db)):
    institutos = instituto_service.find_all(db)

    return templates.TemplateResponse(
        "formulario/estudiante-form.html",
        {
            "request": request,
            "institutos": institutos
        }
    )
