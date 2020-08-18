from datetime import datetime

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


class CardCreate(CardBase):
    pass


class UpdateCard(CardBase):
    pass


class project_list(CardBase):
    pass


