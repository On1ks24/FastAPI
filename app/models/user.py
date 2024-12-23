from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    patronymic = Column(String(255), nullable=True)
    role = Column(Integer, nullable=False)
    email = Column(String(255), nullable=False)
    is_send_notify = Column(Boolean, nullable=False)
    customer_cars = relationship("CustomerCar", back_populates="customer")
    orders_as_administrator = relationship("Order", foreign_keys="Order.administrator_id")
    orders_as_employee = relationship("Order", foreign_keys="Order.employee_id")
