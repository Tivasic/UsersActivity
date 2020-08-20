from datetime import datetime
from typing import List

from pydantic import BaseModel


class Activities(BaseModel):
    project: str
    activity: str
    duration: int
    date: datetime

    class Config:
        orm_mode = True


class DurationProjects(BaseModel):
    projects: List[Activities]
    duration: int


class ActivitiesList(Activities):
    id: int


class ActivityCreate(Activities):
    pass


class ActivityUpdate(Activities):
    pass


class ProjectsList(Activities):
    pass
