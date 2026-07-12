from fastapi import FastAPI

from fastapi_backend.core.config import settings
from fastapi_backend.database.db import engine, Base
from fastapi_backend.routers import student_router

# Import models so they're registered on Base.metadata before create_all runs
from fastapi_backend.models import student_model  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

app.include_router(student_router.router)


@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running"}
