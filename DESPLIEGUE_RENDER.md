# Despliegue de FastAPI con PostgreSQL en Render

Este documento describe el proceso seguido para desplegar una aplicación FastAPI con base de datos PostgreSQL en la nube Render.

---

## 1. Subir el proyecto a GitHub

Desde la carpeta del proyecto:

git init  
git add .  
git commit -m "Proyecto listo para despliegue"  
git branch -M main  
git remote add origin https://github.com/Juanan41/institutos_fastapi.git  
git push -u origin main  

---

## 2. Crear base de datos PostgreSQL en Render

1. Acceder al panel de Render.
2. Pulsar New → PostgreSQL.
3. Indicar nombre y crear base de datos.

Render genera una URL de conexión. Se debe copiar la Internal Database URL.


---

## 3. Crear Web Service

1. New → Web Service  
2. Conectar repositorio GitHub  
3. Runtime: Python  

Build Command:

pip install -r requirements.txt  

Start Command:

uvicorn app.main:app --host 0.0.0.0 --port 10000  

---

## 4. Configurar variable de entorno

Dentro del Web Service:

Key: DATABASE_URL

Value: postgresql://institutos_db_user:Hf8mVyMo3ANmkNmHkXU8ZPcW7svEkVyI@dpg-d5v1h7l6ubrc73c49180-a/institutos_db


---

## 5. Arranque automático de tablas

En main.py:

from app.database import Base, engine  
Base.metadata.create_all(bind=engine)

---

## 6. Despliegue

Render construye y ejecuta el servicio automáticamente.

Al finalizar se proporciona una URL pública:

https://tu-app.onrender.com

---

## 7. Comprobación

https://tu-app.onrender.com  
https://tu-app.onrender.com/docs  

Si Swagger aparece correctamente, el despliegue es correcto.

---

## 8. Resultado

Aplicación FastAPI funcionando en Render con PostgreSQL.

---

Este despliegue permite acceder a la aplicación desde cualquier navegador sin necesidad de instalación local.


