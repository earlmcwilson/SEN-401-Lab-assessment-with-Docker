# ---- FastAPI backend service ----
FROM python:3.13-slim

# Prevent .pyc files and force stdout/stderr to be unbuffered (better logs)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (better layer caching: only re-runs if requirements change)
COPY fastapi_backend/requirements.txt ./fastapi_backend/requirements.txt
RUN pip install --no-cache-dir -r fastapi_backend/requirements.txt

# Copy the backend source code (fastapi_backend is a Python package, so it
# must sit at /app/fastapi_backend for "fastapi_backend.main" to be importable)
COPY fastapi_backend/ ./fastapi_backend/

# Seed database (a fresh students.db will be created automatically on startup
# if this one is not present, but we ship the sample data used in the lab)
COPY students.db ./students.db

EXPOSE 8000

# Basic container health check (no curl in slim image, so use Python's urllib)
HEALTHCHECK --interval=10s --timeout=5s --start-period=10s --retries=5 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/')" || exit 1

CMD ["uvicorn", "fastapi_backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
