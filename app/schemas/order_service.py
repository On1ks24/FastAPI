from pydantic import BaseModel

class OrderServiceBase(BaseModel):
    service_id: int
    order_id: int

class OrderServiceCreate(OrderServiceBase):
    pass

class OrderService(OrderServiceBase):
    id: int

    class Config:
        orm_mode = True
