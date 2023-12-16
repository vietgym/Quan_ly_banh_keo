from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from sqlalchemy.orm import Session

from app.schemas import schema_user
from app.db.database import get_db
from app.crud import crud_user
from app.services.service_user import UserService

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/creat_user/", response_model=schema_user.User)
async def creat_user(user: schema_user.UserBase,
                     db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_response = await user_service.creat_user(user=user)
    return user_response


@router.post("/update_item_user/{user_id}", response_model=schema_user.Item)
async def create_student(user_id: str,
                         item: schema_user.ItemBase,
                         db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_response = await user_service.creat_item(user_id=user_id, item=item)
    return user_response


@router.put("/update_item_by_id/{item_id}", response_model=schema_user.Item)
async def edit_student_by_id(item_id: str,
                             item_update: schema_user.ItemBase,
                             db: Session = Depends(get_db)):
    item_service = UserService(db=db)
    item_response = await item_service.update_item_by_id(item_id=item_id, item_update=item_update)
    return item_response


@router.put("/update_user_by_id/{user_id}", response_model=schema_user.User)
async def edit_student_by_id(user_id: str,
                             user_update: schema_user.UserBase,
                             db: Session = Depends(get_db)):
    item_service = UserService(db=db)
    item_response = await item_service.update_user_by_id(user_id=user_id, user_update=user_update)
    return item_response


@router.get("/get_user_by_id/{user_id}")
def get_user_by_id(user_id: str,
                   db: Session = Depends(get_db)):
    return crud_user.get_user(db=db, user_id=user_id)


@router.get("/get_full_info_user_by_id/{user_id}")
def get_full_user_by_id(user_id: str,
                        db: Session = Depends(get_db)):
    return crud_user.get_full_info_user(db=db, user_id=user_id)


@router.get("/get_all_student/get_students")
async def get_students(skip: int, limit: int,
                       db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_all = await user_service.get_all_users(skip=skip, limit=limit)
    return user_all


@router.delete("/delete_item_by_id/{item_id}", response_model=schema_user.Item)
async def delete_student_endpoint(item_id: str,
                                  db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    del_item = await user_service.del_item_by_id(item_id=item_id)
    return del_item


@router.delete("/delete_user_by_id/{student_id}", response_model=schema_user.User)
async def delete_student_endpoint(user_id: str,
                                  db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    del_user = await user_service.del_user_by_id(user_id=user_id)
    return del_user
