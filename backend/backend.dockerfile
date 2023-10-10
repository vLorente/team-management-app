# Usa la imagen oficial de Python 3.10 como punto de partida
FROM python:3.11-slim

# Instala Poetry globalmente
RUN pip install poetry

# Configura el entorno de producción
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Establece el directorio de trabajo en /app
WORKDIR /backend

# Copia el archivo de bloqueo de dependencias (pyproject.lock) y el archivo de configuración de Poetry (pyproject.toml)
COPY pyproject.toml poetry.lock ./

# Instala las dependencias del proyecto usando Poetry
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

# Copia el código fuente de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto en el que se ejecutará la aplicación FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]