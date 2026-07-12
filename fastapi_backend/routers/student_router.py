import uuid
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from fastapi_backend.database.db import get_db
from fastapi_backend.schemas.student_schema import StudentCreate, StudentUpdate, StudentResponse
from fastapi_backend.services import student_service

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student_in: StudentCreate, db: Session = Depends(get_db)):
    return student_service.create_student(db, student_in)


@router.get("/", response_model=list[StudentResponse])
def list_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return student_service.get_students(db, skip=skip, limit=limit)


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: uuid.UUID, db: Session = Depends(get_db)):
    return student_service.get_student(db, student_id)


@router.patch("/{student_id}", response_model=StudentResponse)
def update_student(student_id: uuid.UUID, student_in: StudentUpdate, db: Session = Depends(get_db)):
    return student_service.update_student(db, student_id, student_in)


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: uuid.UUID, db: Session = Depends(get_db)):
    student_service.delete_student(db, student_id)
