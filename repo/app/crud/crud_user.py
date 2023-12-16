import uuid
# from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from app.model.User import User
from app.model.Item import Item
from app.schemas import schema_user


def create_student(db: Session, user: schema_user.UserBase):
    id_tmp = str(uuid.uuid4())
    db_user = User(id=id_tmp, name_lg=user.name_lg, password=user.password, name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_item(db: Session, item_id: str, item_update: schema_user.ItemBase):
    db_item = get_item(db=db, item_id=item_id)
    if db_item is None:
        return "LOI"
    db_item = db.query(Item).filter(Item.id_item == item_id).first()
    for field, value in item_update.dict().items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_user(db: Session, user_id: str, user_update: schema_user.ItemBase):
    db_user_check = get_user(db=db, user_id=user_id)
    if db_user_check is None:
        return "LOI"
    db_user = db.query(User).filter(User.id == user_id).first()
    for field, value in user_update.dict().items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: str):
    user_response = db.query(User).filter(User.id == user_id).first()
    return user_response


def get_full_info_user(db: Session, user_id: str):
    stmt = (db.query(User, Item)
            .outerjoin(Item, User.id == Item.id)
            .filter(User.id == user_id)
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
    user_data = user_items_map.get(user_id, None)
    response_data = UserAndItemResponse(user=user_data["user"], items=user_data["items"]) if user_data else None
    return response_data


def get_item(db: Session, item_id: str):
    item_response = db.query(Item).filter(Item.id_item == item_id).first()
    return item_response


class UserAndItemResponse:
    def __init__(self, user, items):
        self.user = user
        self.item = items


def get_all_users(db: Session, skip: int, limit: int):
    stmt = (db.query(User, Item)
            .outerjoin(Item, User.id == Item.id)
            .offset(skip)
            .limit(limit)
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

    response_data = [UserAndItemResponse(user=data["user"], items=data["items"]) for data in user_items_map.values()]
    return response_data


def create_item(db: Session, user_id: str, item: schema_user.ItemBase):
    id_item = str(uuid.uuid4())
    db_item = Item(id=user_id, id_item=id_item, name_item=item.name_item, des_item=item.des_item,
                   manufacturers=item.manufacturers, distributor=item.distributor, ing_item=item.ing_item,
                   height=item.height, cost=item.cost)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: str):
    db_item = db.query(Item).filter(Item.id_item == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item


def delete_user(db: Session, user_id: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_items = db.query(Item).filter(Item.id == user_id).all()
        for db_item in db_items:
            db.delete(db_item)
        db.delete(db_user)
        db.commit()
    return db_user
