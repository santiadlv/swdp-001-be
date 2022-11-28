from sqlalchemy import Column, Integer, String
from ..data.database import Base


class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, unique=True, index=True)
    description = Column(Integer)
    date = Column(Integer)
    purchase_order = Column(Integer)
    supplier = Column(Integer)
    barcode = Column(Integer)
    client = Column(Integer)
    quantity = Column(Integer)
    internal_code = Column(Integer)
    t_height = Column(String)
    t_width = Column(String)
    