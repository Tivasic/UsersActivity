from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship


from database.db import Base
from user.models import User


class Post(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True, index=True, unique=True)

    project = Column(String)
    activity = Column(String)
    duration = Column(String)
    date = Column(DateTime)

    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship(User)
