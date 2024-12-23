from pydantic import BaseModel
from datetime import datetime
from .user import User
from .customer_car import CustomerCar

class OrderBase(BaseModel):
    administrator_id: int
    customer_car_id: int
    employee_id: int
    status: int
    start_date: datetime
    end_date: datetime

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    administrator: User
    customer_car: CustomerCar
    employee: User

    class Config:
        orm_mode = True
