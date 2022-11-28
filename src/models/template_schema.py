from typing import Optional
from pydantic import BaseModel, Field


class TemplateModel(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str = Field(...)
    description: int = Field(...)
    date: int = Field(...)
    purchase_order: int = Field(...)
    supplier: int = Field(...)
    barcode: int = Field(...)
    client: int = Field(...)
    quantity: int = Field(...)
    internal_code: int = Field(...)
    t_height: str = Field(...)
    t_width: str = Field(...)
    

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name" : "Interno",
                "description" : 0,
                "date" : 1,
                "purchase_order" : 0,
                "supplier" : 1,
                "barcode" : 1,
                "client" : 0,
                "quantity" : 0,
                "internal_code" : 1,
                "t_height" : "5cm",
                "t_width" : "10cm"
            }
        }

class TemplateID(BaseModel):
    id: int = Field(...)   

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id" : 1
            }
        }

class TemplateName(BaseModel):
    name: str = Field(...)   

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name" : "Interno"
            }
        }

class TemplateUpdate(BaseModel):
    id: int = Field(...)
    name: Optional[str] = Field(...)
    description: Optional[int] = Field(...)
    date: Optional[int] = Field(...)
    purchase_order: Optional[int] = Field(...)
    supplier: Optional[int] = Field(...)
    barcode: Optional[int] = Field(...)
    client: Optional[int] = Field(...)
    quantity: Optional[int] = Field(...)
    internal_code: Optional[int] = Field(...)
    t_height: Optional[str] = Field(...)
    t_width: Optional[str] = Field(...)
    

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id" : 3,
                "name" : "Interno",
                "description" : 0,
                "date" : 1,
                "purchase_order" : 0,
                "supplier" : 1,
                "barcode" : 1,
                "client" : 0,
                "quantity" : 0,
                "internal_code" : 1,
                "t_height" : "5cm",
                "t_width" : "10cm"
            }
        }
