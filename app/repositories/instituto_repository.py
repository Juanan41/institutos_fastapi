from app.models.estudiante import Estudiante
from sqlalchemy.orm import Session
from app.models.instituto import Instituto


class InstitutoRepository:

    # ==========================
    # GET
    # ==========================

    def find_all(self, db: Session):
        return db.query(Instituto).filter(Instituto.is_deleted == False).all()

    def find_by_id(self, db: Session, id: int):
        return db.query(Instituto).filter(
            Instituto.id == id,
            Instituto.is_deleted == False
        ).first()

    def find_by_uuid(self, db: Session, uuid: str):
        return db.query(Instituto).filter(
            Instituto.uuid == uuid,
            Instituto.is_deleted == False
        ).first()

    def find_by_codigo(self, db: Session, codigo_instituto: str):
        return db.query(Instituto).filter(
            Instituto.codigo_instituto == codigo_instituto,
            Instituto.is_deleted == False
        ).first()

    # ==========================
    # POST / PUT
    # ==========================

    def save(self, db: Session, instituto: Instituto):
        db.add(instituto)
        db.commit()
        db.refresh(instituto)
        return instituto

    # ==========================
    # DELETE (Soft delete)
    # ==========================

    def soft_delete(self, db: Session, instituto: Instituto):
        instituto.is_deleted = True
        db.commit()
        db.refresh(instituto)
        return instituto
    
    
    # ============================
    #   UPDATE 
    # ============================
    
    def update(self, db: Session, instituto: Instituto):
        db.commit()
        db.refresh(instituto)
        return instituto
    
    # ============================
    # FIND ESTUDIANTES
    # ============================
    
    def find_estudiantes(self, db: Session, instituto_id: int):
        return db.query(Estudiante).filter(
            Estudiante.instituto_id == instituto_id,
            Estudiante.is_deleted == False
        ).all()
