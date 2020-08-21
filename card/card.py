from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from utils import get_db

from card import service, schemas

router = APIRouter()


# 1.GET-запрос, который возвращает общее кол-во записей активности.

@router.get("/list_activities/", response_model=List[schemas.ActivitiesList])
def list_activities(db: Session = Depends(get_db)):
    return service.get_activities(db)


# 2.POST-запрос, который создает новую запись активности в базе данных.

@router.post("/create_activity/", response_model=schemas.ActivityCreate)
def create_activity(item: schemas.ActivityCreate, db: Session = Depends(get_db)):
    return service.create_activity(db=db, item=item)


# 3.DELETE-запрос, который удаляет запись активности из базы данных по ID.

@router.delete("/delete_activity/")
async def delete_activity(id: int, db: Session = Depends(get_db)):
    return service.delete_activity(id, db)


# 4.PATCH-запрос, который обновления запись активности из базы данных по ID.

@router.patch("/update_activity/", response_model=schemas.ActivityUpdate)
async def update_activity(id: int, item: schemas.ActivityUpdate, db: Session = Depends(get_db)):
    return service.update_activity(id=id, db=db, item=item)


# 5.GET-запрос, который возвращает список записей о проекте при вводе названия проекта
# .
@router.get("/projects_list/", response_model=List[schemas.ProjectsList])
def projects_list(project: str, db: Session = Depends(get_db)):
    return service.projects_list(project, db)


# 5.GET-запрос, который возвращает список записей о проекте и считает общее занятое время на него.

@router.get("/duration_projects/", response_model=schemas.DurationProjects)
def duration_projects(project: str, db: Session = Depends(get_db)):
    return service.duration_projects(project, db)
