import random
from datetime import date

from app.database import SessionLocal
from app.models.instituto import Instituto
from app.models.estudiante import Estudiante


def main():
    db = SessionLocal()

    # ============================
    # CREAR 50 INSTITUTOS
    # ============================

    institutos = []

    for i in range(1, 51):
        instituto = Instituto(
            codigo_instituto=f"INS-{i:03}",
            nombre=f"Instituto {i}",
            ciudad=f"Ciudad {random.randint(1, 10)}",
            direccion=f"Calle {i}",
            telefono=f"600000{i:03}",
            email=f"instituto{i}@correo.com",
            numero_profesores=random.randint(20, 80),
            tipo=random.choice(["Publico", "Privado"]),
            anio_fundacion=date(1995, 1, 1)
        )
        db.add(instituto)
        institutos.append(instituto)

    db.commit()
    print("✔ 50 institutos creados")

    # ============================
    # CREAR 200 ESTUDIANTES
    # ============================

    for i in range(1, 201):
        estudiante = Estudiante(
            nombre=f"Alumno{i}",
            apellidos=f"Apellido{i}",
            dni=f"{i:08}A",
            email=f"alumno{i}@correo.com",
            instituto_id=random.choice(institutos).id
        )
        db.add(estudiante)

    db.commit()
    print("✔ 200 estudiantes creados")

    db.close()
    print("✔ Seed finalizado correctamente")


if __name__ == "__main__":
    main()
