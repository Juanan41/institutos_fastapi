from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.instituto import Instituto


from app.models.estudiante import Estudiante
from app.repositories.estudiante_repository import EstudianteRepository
from app.repositories.instituto_repository import InstitutoRepository
from app.schemas.estudiante import EstudianteCreate


class EstudianteService:

    def __init__(self):
        self.repo = EstudianteRepository()
        self.instituto_repo = InstitutoRepository()

    def find_all(self, db: Session):
        return self.repo.find_all(db)

    def create(self, db: Session, data: EstudianteCreate):
        # 1) Validar instituto
        instituto = self.instituto_repo.find_by_codigo(db, data.codigo_instituto)
        if not instituto:
            raise HTTPException(status_code=404, detail="Instituto no encontrado")

        # 2) Validar DNI único
        existente = self.repo.find_by_dni(db, data.dni)
        if existente:
            raise HTTPException(status_code=400, detail="Ya existe un estudiante con ese DNI")

        # 3) Crear estudiante
        estudiante = Estudiante(
            nombre=data.nombre,
            apellidos=data.apellidos,
            dni=data.dni,
            email=data.email,
            fecha_nacimiento=data.fecha_nacimiento,
            instituto_id=instituto.id
        )

        return self.repo.save(db, estudiante)

    def get_all_institutos(self, db):
         return db.query(Instituto).all()
    
        