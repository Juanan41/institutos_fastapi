from pydantic import BaseModel
from datetime import date
from typing import Optional

class EstudianteCreate(BaseModel):
    nombre: str
    apellidos: str
    dni: str
    email: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    codigo_instituto: str

class EstudianteResponse(BaseModel):
    id: int
    nombre: str
    apellidos: str
    dni: str
    email: Optional[str]
    fecha_nacimiento: Optional[date]
    uuid: str
    is_deleted: bool
    instituto_id: int   # ✅ AÑADIR ESTE

    class Config:
        from_attributes = True
