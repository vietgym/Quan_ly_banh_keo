import logging
from sqlalchemy.orm import Session

from app.core.exceptions import error_exception_handler
from app.constant.app_status import AppStatus
from app.schemas.schema_user import UserBase, ItemBase
from app.crud import crud_user

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def creat_user(self, user: UserBase):
        crt_user = crud_user.create_student(db=self.db, user=user)
        if not crt_user:
            return "LOi"
        return crt_user

    async def creat_item(self, user_id: str, item: ItemBase):
        crt_item = crud_user.get_user(db=self.db, user_id=user_id)
        if not crt_item:
            return "LOi"
        crt_item = crud_user.create_item(db=self.db, user_id=user_id, item=item)
        return crt_item

    async def update_item_by_id(self, item_id: str, item_update: ItemBase):
        current_std = crud_user.update_item(db=self.db, item_id=item_id, item_update=item_update)
        if not current_std:
            return "LOi"
        return current_std

    async def update_user_by_id(self, user_id: str, user_update: UserBase):
        current_std = crud_user.update_user(db=self.db, user_id=user_id, user_update=user_update)
        if not current_std:
            return "LOi"
        return current_std

    async def get_all_users(self, skip: int, limit: int):
        user_all = crud_user.get_all_users(db=self.db, skip=skip, limit=limit)
        if not user_all:
            return "LOI"
        return dict(users=user_all)

    async def del_user_by_id(self, user_id: str):
        del_user = crud_user.delete_user(db=self.db, user_id=user_id)
        if not del_user:
            return "LOI"
        return del_user

    async def del_item_by_id(self, item_id: str):
        del_item = crud_user.delete_item(db=self.db, item_id=item_id)
        if not del_item:
            return "LOI"
        return del_item
