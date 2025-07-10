FROM python:3.12-slim AS base

ENV POETRY_VIRTUALENVS_CREATE=false \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

# Instalamos build-essential para C y libpq-dev para Postgres
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
       build-essential \
       libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalamos Poetry
RUN pip install --no-cache-dir poetry

WORKDIR /app

# Copiamos solo pyproject.toml y poetry.lock para cachear instalación de deps
COPY pyproject.toml poetry.lock* ./

# Instalamos deps vía Poetry (ya incluye asyncpg, fastapi, uvicorn, etc)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without dev --no-root

# Copiamos el código
COPY src/ ./src

# Creamos usuario no-root
RUN groupadd --system app \
    && useradd --system --gid app app \
    && chown -R app:app /app

USER app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
