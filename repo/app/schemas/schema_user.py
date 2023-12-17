from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    name_lg: str
    password: str
    name: str
    email: str


class UserLogin(BaseModel):
    name_lg: str
    password: str


class User(UserBase):
    id: str

    class Config:
        from_attributes = True


class ItemBase(BaseModel):
    name_item: str
    des_item: str
    manufacturers: str
    distributor: str
    ing_item: str
    height: str
    cost: str


class Item(ItemBase):
    id_item: str
    id: str

    class Config:
        from_attributes = True


class UserFull(UserBase):
    items: Item

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: int(v.timestsmp())
        }