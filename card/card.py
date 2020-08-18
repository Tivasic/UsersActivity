from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from utils import get_db

from card import service, schemas


router = APIRouter()


@router.get("/list_activities/", response_model=List[schemas.ActivitiesList])
def list_activities(db: Session = Depends(get_db)):
    return service.get_activities(db)


@router.post("/create_activity/", response_model=schemas.ActivityCreate)
def create_activity(item: schemas.ActivityCreate, db: Session = Depends(get_db)):
    return service.create_activity(db=db, item=item)


@router.delete("/delete_activity/")
async def delete_activity(id: int,  db: Session = Depends(get_db)):
    return service.delete_activity(id, db)


@router.patch("/update_activity/", response_model=schemas.ActivityUpdate)
async def update_activity(id: int, item: schemas.ActivityUpdate, db: Session = Depends(get_db)):
    return service.update_activity(id=id, db=db, item=item)


@router.get("/projects_list/", response_model=List[schemas.ProjectsList])
def projects_list(project: str, db: Session = Depends(get_db)):
    return service.projects_list(project, db)


@router.get("/duration_projects/", response_model=schemas.DurationProjects)
def duration_projects(project: str, db: Session = Depends(get_db)):
    return service.duration_projects(project, db)



