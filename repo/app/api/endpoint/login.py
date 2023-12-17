from fastapi import Request, APIRouter, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.schemas.schema_user import UserLogin
from app.db.database import get_db
from app.services.service_login import LoginService
from app.schemas.schema_user import UserBase

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def load_rood(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/login/", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/home/", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# @router.get("/get_info_user/")
# async def get_info_user(username: str, password: str,
#                         db: Session = Depends(get_db)):
#     login_service = LoginService(db=db)
#     login_response = await login_service.login_user(name=username, password=password)
#     return login_response


@router.post("/get_info_user/")
async def get_info_user(username: str = Form(...),
                        password: str = Form(...),
                        db: Session = Depends(get_db)):
    print(f"Received username: {username}, password: {password}")
    login_service = LoginService(db=db)
    login_response = await login_service.login_user(name=username, password=password)
    return login_response


@router.post("/login_pass/")
async def login_pass(username: str = Form(...),
                     password: str = Form(...),
                     db: Session = Depends(get_db)):
    # form = await request.form()
    # username = form.get("username")
    # password = form.get("password")
    print(f"Received username: {username}, password: {password}")
    login_service = LoginService(db=db)
    login_response = await login_service.login_user(name=username, password=password)
    return login_response


@router.get("/load_register/", response_class=HTMLResponse)
def load_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register_user/")
async def register_user(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    username = form.get("username")
    password = form.get("password")
    re_password = form.get("re_password")
    name = form.get("name")
    email = form.get("email")
    print(f"Received username: {username}, password: {password}, name: {name}, email: {email}")
    user_service = LoginService(db=db)
    user_new = await user_service.ck_register_user(username=username, password=password, re_password=re_password,
                                                   name=name, email=email)
    if user_new == {"message": "mat khau nhap lai khong giong"}:
        return user_new
    crt_user = await user_service.creat_user(user=user_new)
    return crt_user

# @router.post("/register_user/")
# async def register_user(username: str = Form(...),
#                         password: str = Form(...),
#                         re_password: str = Form(...),
#                         name: str = Form(...),
#                         email: str = Form(...),
#                         db: Session = Depends(get_db)):
#     print(f"Received username: {username}, password: {password}, name: {name}, email: {email}")
#     user_service = LoginService(db=db)
#     user_new = await user_service.ck_register_user(username=username, password=password, re_password=re_password, name=name, email=email)
#     if user_new == {"message": "mat khau nhap lai khong giong"}:
#         return user_new
#     crt_user = await user_service.creat_user(user=user_new)
#     return crt_user


# @router.post("/creat_user/", response_model=schema_user.User)
# async def creat_user(user: schema_user.UserBase,
#                      db: Session = Depends(get_db)):
#     user_service = UserService(db=db)
#     user_response = await user_service.creat_user(user=user)
#     return user_response
