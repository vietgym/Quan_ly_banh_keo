# import uuid
# from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from app.model.User import User
from app.model.Item import Item
from app.schemas import schema_user
from app.crud.crud_user import UserAndItemResponse


def login_user(db: Session, name: str, password: str):
    stmt = (db.query(User, Item)
            .outerjoin(Item, User.id == Item.id)
            .filter(User.name_lg == name, User.password == password)
            .all())
    user_items_map = {}
    for user, item in stmt:
        if user.id not in user_items_map:
            user_items_map[user.id] = {
                "user": user,
                "items": [] if item is None else [item]
            }
        elif item is not None:
            user_items_map[user.id]["items"].append(item)
    user_data = next(iter(user_items_map.values()), None)
    response_data = UserAndItemResponse(user=user_data["user"], items=user_data["items"]) if user_data else None
    return response_data

