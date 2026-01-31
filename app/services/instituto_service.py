from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.instituto import Instituto
from app.repositories.instituto_repository import InstitutoRepository
from app.repositories.estudiante_repository import EstudianteRepository
from app.schemas.instituto import InstitutoCreate


class InstitutoService:

    def __init__(self):
        self.repo = InstitutoRepository()
        self.estudiante_repo = EstudianteRepository()

    def find_all(self, db: Session):
        return self.repo.find_all(db)

    def create(self, db: Session, data: InstitutoCreate):
        # 1) Validar código instituto único
        existente = self.repo.find_by_codigo(db, data.codigo_instituto)
        if existente:
            raise HTTPException(status_code=400, detail="Ya existe un instituto con ese código")

        instituto = Instituto(**data.model_dump())
        return self.repo.save(db, instituto)

    def find_by_id(self, db: Session, id: int):
        instituto = self.repo.find_by_id(db, id)
        if not instituto:
            raise HTTPException(status_code=404, detail="Instituto no encontrado")
        return instituto

    def update(self, db: Session, id: int, data: InstitutoCreate):
        instituto = self.find_by_id(db, id)

        # Validar código único (si cambia)
        if data.codigo_instituto != instituto.codigo_instituto:
            existente = self.repo.find_by_codigo(db, data.codigo_instituto)
            if existente:
                raise HTTPException(status_code=400, detail="Ya existe un instituto con ese código")

        # Actualizar campos
        for key, value in data.model_dump().items():
            setattr(instituto, key, value)

        return self.repo.update(db, instituto)

    def delete(self, db: Session, id: int):
        instituto = self.find_by_id(db, id)
        return self.repo.soft_delete(db, instituto)

    def find_estudiantes(self, db: Session, id: int):
        # Validar que existe instituto
        self.find_by_id(db, id)
        return self.repo.find_estudiantes(db, id)
