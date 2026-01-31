from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, default=lambda: str(uuid.uuid4()), unique=True, index=True)

    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)

    dni = Column(String, unique=True, nullable=False)
    email = Column(String)
    fecha_nacimiento = Column(Date)

    is_deleted = Column(Boolean, default=False)

    instituto_id = Column(Integer, ForeignKey("institutos.id"), nullable=False)
    instituto = relationship("Instituto", back_populates="estudiantes")
