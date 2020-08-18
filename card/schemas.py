from datetime import datetime
from typing import List

from pydantic import BaseModel


class CardBase(BaseModel):
    project: str
    activity: str
    duration: int
    date: datetime

    class Config:
        orm_mode = True


class CardList(CardBase):
    id: int


class DurationProject(BaseModel):
    projects: List[CardBase]
    duration: int


class CardCreate(CardBase):
    pass


class UpdateCard(CardBase):
    pass


class project_list(CardBase):
    pass


