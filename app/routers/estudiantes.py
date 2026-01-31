from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.estudiante import EstudianteCreate, EstudianteResponse
from app.services.estudiante_service import EstudianteService

# ✅ ESTA VARIABLE TIENE QUE EXISTIR Y LLAMARSE router
router = APIRouter(prefix="/api/v1/estudiantes", tags=["Estudiantes"])

service = EstudianteService()


@router.get("", response_model=list[EstudianteResponse])
def find_all(db: Session = Depends(get_db)):
    return service.find_all(db)


@router.post("", response_model=EstudianteResponse, status_code=201)
def create(data: EstudianteCreate, db: Session = Depends(get_db)):
    return service.create(db, data)
