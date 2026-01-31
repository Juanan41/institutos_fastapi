from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class Instituto(Base):
    __tablename__ = "institutos"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, default=lambda: str(uuid.uuid4()), unique=True, index=True)

    codigo_instituto = Column(String, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
    ciudad = Column(String)
    direccion = Column(String)
    telefono = Column(String)
    email = Column(String)

    numero_profesores = Column(Integer)
    tipo = Column(String)
    anio_fundacion = Column(Date)

    is_deleted = Column(Boolean, default=False)

    estudiantes = relationship(
        "Estudiante",
        back_populates="instituto",
        cascade="all, delete-orphan"
    )
