from pydantic import BaseModel, Field


class TemplateModel(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    description: int = Field(...)
    date: int = Field(...)
    purchase_order: int = Field(...)
    supplier: str = Field(...)
    barcode: int = Field(...)
    client: int = Field(...)
    quantity: int = Field(...)
    t_height: str = Field(...)
    t_width: str = Field(...)
    

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
