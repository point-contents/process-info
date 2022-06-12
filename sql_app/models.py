from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Process(Base):
    __tablename__ = "processes"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)
    host = Column(String, unique=False, index=True)
    source = Column(String, unique=False, index=True)
    destination = Column(String, unique=False, index=True)
