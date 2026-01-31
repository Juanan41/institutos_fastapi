from app.schemas.estudiante import EstudianteResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.instituto import InstitutoCreate, InstitutoResponse
from app.services.instituto_service import InstitutoService

from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

templates = Jinja2Templates(directory="app/templates")



router = APIRouter(prefix="/api/v1/institutos", tags=["Institutos"])



service = InstitutoService()


@router.get("", response_model=list[InstitutoResponse])
def find_all(db: Session = Depends(get_db)):
    return service.find_all(db)

@router.get("/institutos", include_in_schema=False)
def vista_institutos(request: Request, db: Session = Depends(get_db)):
    institutos = instituto_service.get_all(db)
    return templates.TemplateResponse(
        "institutos/list.html",
        {"request": request, "institutos": institutos}
    )



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
    return


@router.get("/{id}/estudiantes", response_model=list[EstudianteResponse])
def find_estudiantes(id: int, db: Session = Depends(get_db)):
    return service.find_estudiantes(db, id)

