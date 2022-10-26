from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field


class LabelModel(BaseModel):
    id: int = Field(...)
    purchase_order: int = Field(...)
    date: datetime = Field(...)
    description: Union[str, None] = Field(None)
    client: str = Field(...)
    quantity: int = Field(...)
    supplier: str = Field(...)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
