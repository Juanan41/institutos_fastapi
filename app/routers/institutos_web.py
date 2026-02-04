from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from starlette.status import HTTP_303_SEE_OTHER
from fastapi.templating import Jinja2Templates

from app.database import get_db
from app.schemas.instituto import InstitutoCreate
from app.services.instituto_service import InstitutoService

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()
service = InstitutoService()

# --------------------
# WEB
# --------------------

@router.get("/institutos")
def vista_institutos(request: Request, db: Session = Depends(get_db)):
    institutos = service.find_all(db)
    return templates.TemplateResponse(
        "institutos/list.html",
        {"request": request, "institutos": institutos}
    )


@router.get("/institutos/nuevo")
def formulario_nuevo(request: Request):
    return templates.TemplateResponse(
        "formulario/instituto-form.html",
        {"request": request}
    )


@router.post("/institutos/nuevo")
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

    return RedirectResponse("/institutos", status_code=HTTP_303_SEE_OTHER)


@router.get("/institutos/delete/{id}")
def borrar_instituto(id: int, db: Session = Depends(get_db)):
    service.delete(db, id)
    return RedirectResponse("/institutos", status_code=HTTP_303_SEE_OTHER)

@router.get("/institutos/{id}")
def ver_detalle(id: int, request: Request, db: Session = Depends(get_db)):
    instituto = service.find_by_id(db, id)
    return templates.TemplateResponse(
        "institutos/detail.html",
        {"request": request, "instituto": instituto}
    )

@router.get("/institutos/editar/{id}")
def formulario_editar(id: int, request: Request, db: Session = Depends(get_db)):
    instituto = service.find_by_id(db, id)
    return templates.TemplateResponse(
        "formulario/instituto-edit.html",
        {"request": request, "instituto": instituto}
    )

@router.post("/institutos/editar/{id}")
def guardar_edicion(
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

    return RedirectResponse("/institutos", status_code=HTTP_303_SEE_OTHER)
