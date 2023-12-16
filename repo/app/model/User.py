from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    name_lg = Column(String)
    password = Column(String)
    name = Column(String)
    email = Column(String)

    items = relationship("Item", back_populates="user")