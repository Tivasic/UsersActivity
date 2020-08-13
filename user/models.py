from sqlalchemy import Column, String, Integer, DateTime, Boolean
from database.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    date = Column(DateTime)
    active = Column(Boolean, default=False)
    admin = Column(Boolean, default=False)
