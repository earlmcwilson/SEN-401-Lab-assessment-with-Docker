import uuid
import enum
from typing import Optional
from sqlalchemy import String, Integer, Uuid, Enum, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from fastapi_backend.database.db import Base


class UserGender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    PREFER_NOT_TO_SAY = "prefer_not_to_say"


class Student(Base):
    __tablename__ = "students"
    __table_args__ = (
        CheckConstraint("score >= 0 AND score <= 100", name="check_score_range"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    )

    full_name: Mapped[str] = mapped_column(String(150), nullable=False)

    matric_no: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    gender: Mapped[Optional[UserGender]] = mapped_column(
        Enum(UserGender),
        nullable=True
    )

    score: Mapped[int] = mapped_column(Integer, nullable=False)

    department: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True
    )

    profile_image: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True,
        default=None
    )