from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field

from ..utils import id_gen

class LabelModel(BaseModel):
    id: int = Field(default_factory=id_gen.generate_pk)
    purchase_order: int = Field(...)
    date: datetime = Field(default_factory=datetime.utcnow)
    description: Union[str, None] = Field(None)
    client: str = Field(...)
    quantity: int = Field(...)
    supplier: str = Field(...)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class LabelID(BaseModel):
    id: int = Field(...)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id" : 82495156843250
            }
        }
