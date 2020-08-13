from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from utils import get_db
from . import service, schemas


router = APIRouter()


@router.get("/", response_model=List[schemas.PostList])
def post_list(db: Session = Depends(get_db)):
    return service.get_post_list(db)


@router.post("/create/", response_model=schemas.PostCreate)
def create_post(item: schemas.PostCreate, db: Session = Depends(get_db)):
    return service.create_post_list(db=db, item=item)


@router.delete("/delete/")
async def delete(id: int,  db: Session = Depends(get_db)):
    return service.delete_card(id, db)


@router.patch("/update/", response_model=schemas.UpdateCard)
async def update_card(id: int, item: schemas.UpdateCard, db: Session = Depends(get_db)):
    return service.update_card(id=id, db=db, item=item)


