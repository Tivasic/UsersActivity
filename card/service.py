from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException

from . import models, schemas


def get_post_list(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).all()


def create_post_list(db: Session, item: schemas.CardCreate):
    card = models.Post(**item.dict())
    db.add(card)
    db.commit()
    db.refresh(card)
    return card


def delete_card(id: int, db: Session):
    card = db.query(models.Post).get(id)
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
    stored_data = jsonable_encoder(stored_card)
    update_data = item.dict(exclude_unset=True)
    for field in stored_data:
        if field in update_data:
            setattr(stored_card, field, update_data[field])
    db.add(stored_card)
    db.commit()
    db.refresh(stored_card)
    return stored_card
