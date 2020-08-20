from fastapi import APIRouter

from user_activities import activities

router = APIRouter()
router.include_router(activities.router, prefix="/UserActivities")
