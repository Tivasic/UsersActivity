from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import schemas
from database import table_model


def get_activities(db: Session):
    # Получает все записи из базы данных.
    activities = db.query(table_model.Post).all()
    if not activities:
        raise HTTPException(
            status_code=404, detail="Activities not found.",
        )
    return activities


def create_activity(db: Session, item: schemas.ActivityCreate):
    # Создает новый словарь в соответствии со схемой
    # и добавляет запись на сервер.
    activities = table_model.Post(**item.dict())
    db.add(activities)
    db.commit()
    db.refresh(activities)
    return activities


def delete_activity(activity_id: int, db: Session):
    # Получает необходимую запись из БД по ID
    # и удаляет ее.
    activities = db.query(table_model.Post).get(activity_id)
    if not activities:
        raise HTTPException(
            status_code=404, detail="Activities not found.",
        )
    db.delete(activities)
    db.commit()
    return ["Запись", activity_id, "удалена"]


def projects_list(project: str, db: Session):
    # Получает необходимую запись из БД в соответствии
    # фильтрации по проектам и возвращает ее списком.
    list_projects = db.query(table_model.Post).filter(table_model.Post.project == project).all()
    if not list_projects:
        raise HTTPException(
            status_code=404, detail="Project not found.",
        )
    return list_projects


def duration_projects(project: str, db: Session):
    # Получает необходимую запись из БД в соответствии
    # фильтрации по проектам, а так же получает все
    # затраченное время на проекты и суммирует их.
    list_projects = db.query(table_model.Post).filter(table_model.Post.project == project).all()
    if not list_projects:
        raise HTTPException(
            status_code=404, detail="Project not found.",
        )
    durations = (
        db.query(table_model.Post.duration).filter(table_model.Post.project == project).all()
    )
    sum_of_durations = sum([value for value, in durations])
    return schemas.DurationProjects(projects=list_projects, duration=sum_of_durations)


def update_activity(activity_id: int, db: Session, item: schemas.ActivityUpdate):
    # Получает необходимую запись из БД в соответствии
    # фильтрации по ID. Далее распаковываются значения
    # и заносятся в новый словарь измененные данные и
    # затем добавляет обновленную запись в БД.
    stored_activities = db.query(table_model.Post).filter(table_model.Post.id == activity_id).first()
    if not stored_activities:
        raise HTTPException(
            status_code=404, detail="Stored user_activities not found.",
        )
    stored_data = {
        "activity_id": stored_activities.id,
        "project": stored_activities.project,
        "activity": stored_activities.activity,
        "duration": stored_activities.duration,
        "date": stored_activities.date,
        "user": stored_activities.user,
        "user_id": stored_activities.user_id,
    }
    update_data = item.dict(exclude_unset=True)
    for field in stored_data:
        if field in update_data:
            setattr(stored_activities, field, update_data[field])
    db.add(stored_activities)
    db.commit()
    db.refresh(stored_activities)
    return stored_activities
