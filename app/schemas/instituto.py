from pydantic import BaseModel
from datetime import date
from typing import Optional

class InstitutoCreate(BaseModel):
    nombre: str
    codigo_instituto: str
    ciudad: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    numero_profesores: Optional[int] = None
    tipo: Optional[str] = None
    anio_fundacion: Optional[date] = None

class InstitutoResponse(InstitutoCreate):
    id: int
    uuid: str
    is_deleted: bool

    class Config:
        from_attributes = True
