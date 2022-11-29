import math
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, validator

from ..utils import id_gen

class LabelModel(BaseModel):
    id: int = Field(...)
    purchase_order: int = Field(...)
    date: datetime = Field(default_factory=datetime.utcnow)
    description: Union[str, None] = Field(None)
    client: str = Field(...)
    quantity: int = Field(...)
    supplier: str = Field(...)

    @validator('id', pre=True)
    def parse_id(cls, v):
        assert isinstance(v, int), "ID must be a number"
        assert int(math.log10(v)) + 1 == 14, "ID length must be 14 digits for barcode generation"
        return v

    @validator('date', pre=True)
    def parse_date(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v[:10], "%Y-%m-%d")
        return v


    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class LabelID(BaseModel):
    id: int = Field(...)

    @validator('id', pre=True)
    def parse_id(cls, v):
        assert isinstance(v, int), "ID must be a number"
        assert int(math.log10(v)) + 1 == 14, "ID length must be 14 digits for barcode generation"
        return v

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id" : 82495156843250
            }
        }
