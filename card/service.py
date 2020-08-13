from sqlalchemy.orm import Session
from fastapi import HTTPException

from . import models, schemas


def get_list_card(db: Session):
    return db.query(models.Post).all()


def create_card(db: Session, item: schemas.CardCreate):
    card = models.Post(**item.dict())
    db.add(card)
    db.commit()
    db.refresh(card)
    return card


def delete_card(id: int, db: Session):
    card = db.query(models.Post).get(id)
    if not card:
        raise HTTPException(
            status_code=404,
            detail="Card not found.",
        )
    db.delete(card)
    db.commit()
    return ["Запись", id, "удалена"]


def update_card(id: int, db: Session, item: schemas.UpdateCard):
    stored_card = db.query(models.Post).filter(models.Post.id == id).first()
    if not stored_card:
        raise HTTPException(
            status_code=404,
            detail="Stored card not found.",
        )
    stored_data = {
        "id": stored_card.id,
        "project": stored_card.project,
        "activity": stored_card.activity,
        "duration": stored_card.duration,
        "date": stored_card.date,
        "user": stored_card.user,
        "user_id": stored_card.user_id
    }
    update_data = item.dict(exclude_unset=True)
    for field in stored_data:
        if field in update_data:
            setattr(stored_card, field, update_data[field])
    db.add(stored_card)
    db.commit()
    db.refresh(stored_card)
    return stored_card
