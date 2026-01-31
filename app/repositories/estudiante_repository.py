from sqlalchemy.orm import Session
from app.models.estudiante import Estudiante


class EstudianteRepository:

    # ==========================
    # GET
    # ==========================

    def find_all(self, db: Session):
        return db.query(Estudiante).filter(Estudiante.is_deleted == False).all()

    def find_by_id(self, db: Session, id: int):
        return db.query(Estudiante).filter(
            Estudiante.id == id,
            Estudiante.is_deleted == False
        ).first()

    def find_by_uuid(self, db: Session, uuid: str):
        return db.query(Estudiante).filter(
            Estudiante.uuid == uuid,
            Estudiante.is_deleted == False
        ).first()

    def find_by_dni(self, db: Session, dni: str):
        return db.query(Estudiante).filter(
            Estudiante.dni == dni,
            Estudiante.is_deleted == False
        ).first()

    def find_by_instituto_id(self, db: Session, instituto_id: int):
        return db.query(Estudiante).filter(
            Estudiante.instituto_id == instituto_id,
            Estudiante.is_deleted == False
        ).all()

    # ==========================
    # POST
    # ==========================

    def save(self, db: Session, estudiante: Estudiante):
        db.add(estudiante)
        db.commit()
        db.refresh(estudiante)
        return estudiante

    # ==========================
    # DELETE (Soft delete)
    # ==========================

    def soft_delete(self, db: Session, estudiante: Estudiante):
        estudiante.is_deleted = True
        db.commit()
        db.refresh(estudiante)
        return estudiante
    
    # ==========================
    # UPDATE
    # ==========================
    
    def update(self, db: Session, estudiante: Estudiante):
        db.commit()
        db.refresh(estudiante)
        return estudiante

