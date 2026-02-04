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

# 📦 Despliegue de Aplicación FastAPI con PostgreSQL en Render

## 📌 Descripción general

En esta práctica se ha desplegado una aplicación desarrollada con **FastAPI** que gestiona Institutos y Estudiantes. La aplicación utiliza plantillas **Jinja2** para mostrar páginas web y una base de datos **PostgreSQL** alojada en la nube mediante la plataforma **Render**.

El objetivo principal es demostrar que la API puede funcionar correctamente:

* En local.
* Con bases de datos en contenedores Docker.
* Y finalmente con una base de datos PostgreSQL en la nube.

Este documento explica las decisiones técnicas tomadas, los motivos de cada elección y el proceso seguido, usando un lenguaje adecuado para un alumno de 2º de DAW.

---

## 🧱 Arquitectura final del proyecto

La arquitectura final es la siguiente:

* Aplicación FastAPI desplegada como **Web Service** en Render.
* Base de datos PostgreSQL desplegada como **PostgreSQL Service** en Render.
* Comunicación entre ambos mediante una variable de entorno (`DATABASE_URL`).

Esto permite separar claramente:

* La lógica de la aplicación.
* La persistencia de datos.

Esta separación es una buena práctica porque facilita mantenimiento, escalabilidad y seguridad.

---

## 🗄️ Elección de PostgreSQL frente a MySQL

Aunque en algunos puntos de la práctica se utiliza MySQL, para el despliegue final se ha elegido **PostgreSQL** por los siguientes motivos:

* PostgreSQL está mejor integrado en Render.
* PostgreSQL tiene muy buena compatibilidad con SQLAlchemy.
* PostgreSQL es muy usado en entornos profesionales.
* Mejor soporte para tipos de datos avanzados.

No significa que MySQL sea malo, pero PostgreSQL suele ser la opción preferida en plataformas cloud modernas.

---

## 🔌 Elección del driver: psycopg2

Para conectar FastAPI con PostgreSQL se ha utilizado el driver:

```
psycopg2-binary
```

### ¿Por qué psycopg2?

* Es el driver más usado y probado para PostgreSQL en Python.
* Es totalmente compatible con SQLAlchemy.
* Tiene mucha documentación y ejemplos.
* Es estable y ampliamente utilizado en producción.

### ¿Por qué no psycopg3?

Aunque psycopg3 es más moderno, durante pruebas aparecieron errores de compatibilidad con SQLAlchemy.

Como alumno de 2º DAW, se prioriza:

* Estabilidad.
* Funcionamiento garantizado.
* Simplicidad.

Por eso se elige psycopg2, aunque no sea el más nuevo.

Esta decisión está basada en fiabilidad, no en moda tecnológica.

---

## 🧬 Cadena de conexión utilizada

La aplicación obtiene la cadena de conexión desde una variable de entorno:

```
DATABASE_URL
```

Ejemplo real usado en Render:

```
postgresql://usuario:password@host.render.com/institutos_db
```

### Ventajas de usar variables de entorno

* No se suben contraseñas al repositorio.
* Permite cambiar de base de datos sin modificar código.
* Es una práctica estándar en entornos profesionales.

---

## ⚙️ Configuración en database.py

Archivo `app/database.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

### Explicación sencilla

* `create_engine` crea la conexión.
* `sessionmaker` permite abrir sesiones.
* `Base` sirve para definir los modelos.

Esta estructura es la recomendada por SQLAlchemy.

---

## 🌍 Configuración del servicio Web en Render

Durante la creación del servicio:

* Lenguaje: Python 3
* Build Command:

```
pip install -r requirements.txt
```

* Start Command:

```
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

### Motivo del comando

Render necesita que la aplicación escuche en todas las interfaces (`0.0.0.0`) y en el puerto que la plataforma asigna.

---

## 🔐 Variables de entorno configuradas en Render

Se añadió:

* Nombre: DATABASE_URL
* Valor: cadena de conexión PostgreSQL

Esto conecta automáticamente la app con la base de datos cloud.

---

## 🧪 Comprobaciones realizadas

* Arranque correcto del servicio.
* Logs indican:

  * Construcción exitosa.
  * Uvicorn ejecutándose.
* Acceso web a la URL pública.
* Navegación:

  * Página Inicio.
  * Listado de institutos.
  * Listado de estudiantes.
  * Formularios de creación.

Todo funcionando correctamente.

---

## 🧠 Decisiones importantes justificadas

### 1️⃣ PostgreSQL en vez de MySQL

Porque Render lo integra mejor y es más estándar en cloud.

### 2️⃣ psycopg2 en vez de psycopg3

Porque es más estable con SQLAlchemy actualmente.

### 3️⃣ Variables de entorno

Por seguridad y buenas prácticas.

### 4️⃣ Separación app / base de datos

Facilita escalado y mantenimiento.

---

## 📚 Qué demuestra esta práctica

* Comprensión de arquitectura cliente-servidor.
* Uso de ORMs.
* Trabajo con contenedores.
* Uso de cloud.
* Buenas prácticas básicas de seguridad.

---

## ✅ Conclusión

El despliegue se ha realizado correctamente siguiendo buenas prácticas básicas para un entorno real:

* Código separado de configuración.
* Datos protegidos.
* Servicios desacoplados.

Aunque existen tecnologías más avanzadas, las decisiones tomadas priorizan:

* Simplicidad.
* Estabilidad.
* Aprendizaje.

Adecuado para el nivel de 2º de Desarrollo de Aplicaciones Web.

---

## 🔗 URL del proyecto desplegado

(https://institutos-fastapi-1.onrender.com/)

---

✍️ Autor: Alumno 2º DAW

