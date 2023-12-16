from fastapi import APIRouter
from app.api.endpoint import login
from app.api.endpoint import user

router = APIRouter()
router.include_router(login.router, tags=["login"])
router.include_router(user.router, tags=["User"])
