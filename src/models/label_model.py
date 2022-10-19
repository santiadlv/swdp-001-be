from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from .database import Base


class Label(Base):
    __tablename__ = "labels"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    purchase_order = Column(Integer, unique=True, index=True)
    date = Column(DateTime, server_default=func.now())
    description = Column(String)
    client = Column(String)
    quantity = Column(Integer)
    supplier = Column(String)
    path = Column(String)
