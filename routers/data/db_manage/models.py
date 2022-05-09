from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base


class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer,
                primary_key=True,
                index=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(20), index=True, unique=True, nullable=False)
