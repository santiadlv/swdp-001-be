from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime

from ..data.database import Base


class Label(Base):
    __tablename__ = "labels"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    purchase_order = Column(Integer)
    date = Column(DateTime, server_default=func.now())
    description = Column(String)
    client = Column(String)
    quantity = Column(Integer)
    supplier = Column(String)
