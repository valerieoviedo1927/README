# FastAPI CI/CD Example

Este proyecto implementa un pipeline CI/CD para una aplicación FastAPI.

## Instrucciones

1. Clona este repositorio.
2. Crea y activa un entorno virtual.
3. Instala las dependencias con `pip install -r requirements.txt`.
4. Ejecuta el servidor con `uvicorn app.main:app --reload`.
5. Ejecuta las pruebas con `pytest`.

## Docker

Para construir y ejecutar el contenedor:

```bash
docker build -t fastapi-ci-cd .
docker run -d -p 8000:8000 fastapi-ci-cd
Última actualización: 6 de mayo de 2025
