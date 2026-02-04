from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.estudiante import EstudianteCreate, EstudianteResponse
from app.services.estudiante_service import EstudianteService

from fastapi.templating import Jinja2Templates

from fastapi import Form
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER


router = APIRouter(prefix="/api/v1/estudiantes", tags=["Estudiantes"])

service = EstudianteService()
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_model=list[EstudianteResponse])
def find_all(db: Session = Depends(get_db)):
    return service.find_all(db)


@router.post("", response_model=EstudianteResponse, status_code=201)
def create(data: EstudianteCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.get("/vista", include_in_schema=False)
def vista_estudiantes(request: Request, db: Session = Depends(get_db)):
    estudiantes = service.find_all(db)
    return templates.TemplateResponse(
        "estudiantes/list.html",
        {"request": request, "estudiantes": estudiantes}
    )
    
@router.get("/nuevo", include_in_schema=False)
def nuevo_estudiante(request: Request, db: Session = Depends(get_db)):
    institutos = service.get_all_institutos(db)

    return templates.TemplateResponse(
        "formulario/estudiante-form.html",
        {"request": request, "institutos": institutos}
    )
    
@router.post("/nuevo", include_in_schema=False)
def guardar_estudiante(
    nombre: str = Form(...),
    apellidos: str = Form(...),
    dni: str = Form(...),
    email: str = Form(...),
    instituto_id: int = Form(...),
    db: Session = Depends(get_db)
):
    data = EstudianteCreate(
        nombre=nombre,
        apellidos=apellidos,
        dni=dni,
        email=email,
        instituto_id=instituto_id
    )

    service.create(db, data)

    return RedirectResponse(
        url="/estudiantes",
        status_code=HTTP_303_SEE_OTHER
    )
    
# --------------------
# FORM EDITAR ESTUDIANTE
# --------------------

@router.get("/{id}/editar", include_in_schema=False)
def form_editar_estudiante(
    id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    estudiante = service.find_by_id(db, id)
    institutos = instituto_service.find_all(db)

    return templates.TemplateResponse(
        "formulario/estudiante-form.html",
        {
            "request": request,
            "estudiante": estudiante,
            "institutos": institutos
        }
    )


@router.post("/{id}/editar", include_in_schema=False)
def editar_estudiante(
    id: int,
    nombre: str = Form(...),
    apellidos: str = Form(...),
    dni: str = Form(...),
    email: str = Form(...),
    instituto_id: int = Form(...),
    db: Session = Depends(get_db)
):
    data = EstudianteCreate(
        nombre=nombre,
        apellidos=apellidos,
        dni=dni,
        email=email,
        instituto_id=instituto_id
    )

    service.update(db, id, data)

    return RedirectResponse(
        url="/estudiantes",
        status_code=HTTP_303_SEE_OTHER
    )




