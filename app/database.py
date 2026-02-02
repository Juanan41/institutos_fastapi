import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Intentar leer variable entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# FALLBACK para desarrollo local
if DATABASE_URL is None:
    DATABASE_URL = "postgresql://institutos_db_user:Hf8mVyMo3ANmkNmHkXU8ZPcW7svEkVyI@dpg-d5v1h7l6ubrc73c49180-a.virginia-postgres.render.com/institutos_db"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
