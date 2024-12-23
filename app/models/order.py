from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    administrator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    customer_car_id = Column(Integer, ForeignKey('customer_cars.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(Integer, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    administrator = relationship("User", foreign_keys=[administrator_id])
    customer_car = relationship("CustomerCar", back_populates="orders")
    employee = relationship("User", foreign_keys=[employee_id])
