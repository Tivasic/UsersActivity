from fastapi import APIRouter
from card import card

router = APIRouter()

router.include_router(card.router, prefix="/UserActivities")
