from pydantic import BaseModel
from .brand import Brand

class CarBase(BaseModel):
    brand_id: int
    model: str

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: int
    brand: Brand

    class Config:
        orm_mode = True
