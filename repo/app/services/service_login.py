import logging
from sqlalchemy.orm import Session

from app.core.exceptions import error_exception_handler
from app.constant.app_status import AppStatus
from app.schemas.schema_user import UserBase, ItemBase, UserLogin
from app.crud import crud_user, crud_login

logger = logging.getLogger(__name__)


class LoginService:
    def __init__(self, db: Session):
        self.db = db

    async def login_user(self, name: str, password: str):
        log_user = crud_login.login_user(db=self.db, name=name, password=password)
        if log_user is None:
            return "LOI"
        return "LOGIN-OK"

    async def ck_register_user(self, username: str, password: str,
                               re_password: str, name: str, email: str):
        if password != re_password:
            return {"message": "mat khau nhap lai khong giong"}
        user = UserBase
        user.name_lg = username
        user.password = password
        user.name = name
        user.email = email
        return user

    async def creat_user(self, user: UserBase):
        crt_user = crud_user.create_student(db=self.db, user=user)
        if not crt_user:
            return "LOi"
        return crt_user
