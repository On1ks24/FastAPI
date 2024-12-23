from pydantic import BaseModel
from .car import Car
from .user import User

class CustomerCarBase(BaseModel):
    car_id: int
    customer_id: int
    year: int
    number: str

class CustomerCarCreate(CustomerCarBase):
    pass

class CustomerCar(CustomerCarBase):
    id: int
    car: Car
    customer: User

    class Config:
        orm_mode = True
