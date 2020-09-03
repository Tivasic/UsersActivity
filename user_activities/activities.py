from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from user_activities import schemas, service, results_excel
from utils import get_db


router = APIRouter()


@router.get("/list_activities/", response_model=List[schemas.ActivitiesList])
def list_activities(db: Session = Depends(get_db)):
    """Общее колличество записей активности в базе данных."""
    return service.get_activities(db)


@router.post("/create_activity/", response_model=schemas.ActivityCreate)
def create_activity(item: schemas.ActivityCreate,
                    db: Session = Depends(get_db)):
    """Создание новой записи активности в базе данных."""
    return service.create_activity(db=db, item=item)


@router.delete("/delete_activity/")
async def delete_activity(activity_id: int, db: Session = Depends(get_db)):
    """Удаление записи активности из базы данных по ID."""
    return service.delete_activity(activity_id, db)


@router.patch("/update_activity/", response_model=schemas.ActivityUpdate)
async def update_activity(
    activity_id: int, item: schemas.ActivityUpdate,
    db: Session = Depends(get_db)
):
    """Изменение записи активности в базе данных по ID."""
    return service.update_activity(activity_id=activity_id, db=db, item=item)


@router.get("/sorted_projects/", response_model=List[schemas.SortedProjects])
def sorted_projects(project: str, db: Session = Depends(get_db)):
    """Вывод всех имеющихся записей в базе данных по проекту."""
    return service.sorted_projects(project, db)


@router.get("/duration_projects/", response_model=schemas.DurationProjects)
def duration_projects(project: str, db: Session = Depends(get_db)):
    """Вывод списка записей о проекте и общее занятое время."""
    return service.duration_projects(project, db)


@router.get("/results_excel/", )
def get_excel(filename: str, year: int, month: int, day: int, db: Session = Depends(get_db)):
    """Создание отчета в xlsx формате."""
    return results_excel.save_results_to_excel(filename, year, month, day, db)
