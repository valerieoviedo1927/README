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
### 9. **Finalización**
- Verifica que todos los archivos estén correctamente configurados.
- Sube tu código a GitHub.
- Si tienes un Docker Hub, crea un repositorio y configura las credenciales en GitHub Secrets para el paso de CI/CD de Docker.

Con estos pasos, tendrás tu proyecto configurado y listo para trabajar con CI/CD en una hora. ¡Sigue los pasos y asegúrate de completar cada sección!

Si necesitas más ayuda en algún paso específico, avísame.
