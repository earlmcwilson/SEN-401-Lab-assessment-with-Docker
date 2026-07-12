import uuid
from pydantic import BaseModel, ConfigDict, Field
from fastapi_backend.models.student_model import UserGender


class StudentCreate(BaseModel):
    full_name: str
    matric_no: str
    department: str
    score: int = Field(ge=0, le=100)
    gender: UserGender | None = None
    profile_image: str | None = None


class StudentUpdate(BaseModel):
    full_name: str | None = None
    matric_no: str | None = None
    gender: UserGender | None = None
    score: int | None = Field(default=None, ge=0, le=100)
    department: str | None = None
    profile_image: str | None = None


class StudentResponse(BaseModel):
    id: uuid.UUID
    full_name: str
    matric_no: str
    gender: UserGender | None = None
    score: int
    department: str | None = None
    profile_image: str | None = None

    model_config = ConfigDict(from_attributes=True)
