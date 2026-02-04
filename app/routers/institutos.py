from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.instituto import InstitutoCreate, InstitutoResponse
from app.schemas.estudiante import EstudianteResponse
from app.services.instituto_service import InstitutoService
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(
    prefix="/api/v1/institutos",
    tags=["Institutos"]
)

service = InstitutoService()

# --------------------
# API REST
# --------------------

@router.get("", response_model=list[InstitutoResponse])
def find_all(db: Session = Depends(get_db)):
    return service.find_all(db)


@router.post("", response_model=InstitutoResponse, status_code=201)
def create(data: InstitutoCreate, db: Session = Depends(get_db)):
    return service.create(db, data)


@router.get("/{id}", response_model=InstitutoResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    return service.find_by_id(db, id)


@router.put("/{id}", response_model=InstitutoResponse)
def update(id: int, data: InstitutoCreate, db: Session = Depends(get_db)):
    return service.update(db, id, data)


@router.delete("/{id}", status_code=204)
def delete(id: int, db: Session = Depends(get_db)):
    service.delete(db, id)


@router.get("/{id}/estudiantes", response_model=list[EstudianteResponse])
def find_estudiantes(id: int, db: Session = Depends(get_db)):
    return service.find_estudiantes(db, id)

# --------------------
# WEB
# --------------------

@router.get("/vista", include_in_schema=False)
def vista_institutos(request: Request, db: Session = Depends(get_db)):
    institutos = service.find_all(db)
    return templates.TemplateResponse(
        "institutos/list.html",
        {"request": request, "institutos": institutos}
    )


@router.get("/nuevo", include_in_schema=False)
def formulario_nuevo_instituto(request: Request):
    return templates.TemplateResponse(
        "formulario/instituto-form.html",
        {"request": request}
    )
    
# --------------------
# FORM EDITAR INSTITUTO
# --------------------

@router.get("/{id}/editar", include_in_schema=False)
def form_editar_instituto(
    id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    instituto = service.find_by_id(db, id)

    return templates.TemplateResponse(
        "formulario/instituto-form.html",
        {
            "request": request,
            "instituto": instituto
        }
    )


@router.post("/{id}/editar", include_in_schema=False)
def editar_instituto(
    id: int,
    nombre: str = Form(...),
    direccion: str = Form(...),
    ciudad: str = Form(None),
    telefono: str = Form(None),
    email: str = Form(None),
    numero_profesores: int = Form(None),
    tipo: str = Form(None),
    anio_fundacion: str = Form(None),
    db: Session = Depends(get_db)
):
    data = InstitutoCreate(
        nombre=nombre,
        direccion=direccion,
        ciudad=ciudad,
        telefono=telefono,
        email=email,
        numero_profesores=numero_profesores,
        tipo=tipo,
        anio_fundacion=anio_fundacion
    )

    service.update(db, id, data)

    return RedirectResponse(
        url="/institutos",
        status_code=HTTP_303_SEE_OTHER
    )


@router.post("/{id}/editar", include_in_schema=False)
def guardar_edicion_instituto(
    id: int,
    nombre: str = Form(...),
    direccion: str = Form(...),
    ciudad: str = Form(None),
    telefono: str = Form(None),
    email: str = Form(None),
    numero_profesores: int = Form(None),
    tipo: str = Form(None),
    anio_fundacion: str = Form(None),
    db: Session = Depends(get_db)
):

    data = InstitutoCreate(
        nombre=nombre,
        direccion=direccion,
        ciudad=ciudad,
        telefono=telefono,
        email=email,
        numero_profesores=numero_profesores,
        tipo=tipo,
        anio_fundacion=anio_fundacion
    )

    service.update(db, id, data)

    return RedirectResponse(
        url="/institutos",
        status_code=HTTP_303_SEE_OTHER
    )



@router.post("/nuevo", include_in_schema=False)
def guardar_instituto(
    nombre: str = Form(...),
    direccion: str = Form(...),
    ciudad: str = Form(None),
    telefono: str = Form(None),
    email: str = Form(None),
    numero_profesores: int = Form(None),
    tipo: str = Form(None),
    anio_fundacion: str = Form(None),
    db: Session = Depends(get_db)
):

    data = InstitutoCreate(
        nombre=nombre,
        direccion=direccion,
        ciudad=ciudad,
        telefono=telefono,
        email=email,
        numero_profesores=numero_profesores,
        tipo=tipo,
        anio_fundacion=anio_fundacion
    )

    service.create(db, data)

    return RedirectResponse(
        url="/institutos",
        status_code=HTTP_303_SEE_OTHER
    )
