from sqlalchemy import Column, String, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from app.db.database import Base


class Item(Base):
    __tablename__ = "items"
    id_item = Column(String, primary_key=True, index=True)
    name_item = Column(String)
    des_item = Column(String)
    manufacturers = Column(String)
    distributor = Column(String)
    ing_item = Column(String)
    height = Column(String)
    cost = Column(String)

    id = Column(String, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="items")