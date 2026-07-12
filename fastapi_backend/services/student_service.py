import uuid
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from fastapi_backend.models.student_model import Student
from fastapi_backend.schemas.student_schema import StudentCreate, StudentUpdate


def get_students(db: Session, skip: int = 0, limit: int = 100) -> list[Student]:
    return db.query(Student).offset(skip).limit(limit).all()


def get_student(db: Session, student_id: uuid.UUID) -> Student:
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} not found",
        )
    return student


def create_student(db: Session, student_in: StudentCreate) -> Student:
    student = Student(**student_in.model_dump())
    db.add(student)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A student with this matric_no already exists",
        )
    db.refresh(student)
    return student


def update_student(db: Session, student_id: uuid.UUID, student_in: StudentUpdate) -> Student:
    student = get_student(db, student_id)

    update_data = student_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(student, field, value)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A student with this matric_no already exists",
        )
    db.refresh(student)
    return student


def delete_student(db: Session, student_id: uuid.UUID) -> None:
    student = get_student(db, student_id)
    db.delete(student)
    db.commit()
