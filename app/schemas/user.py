from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    first_name: str
    last_name: str
    patronymic: Optional[str] = None
    role: int
    email: EmailStr
    is_send_notify: bool

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
