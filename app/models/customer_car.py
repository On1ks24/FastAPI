from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class CustomerCar(Base):
    __tablename__ = 'customer_cars'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    year = Column(Integer, nullable=False, comment='Год выпуска')
    number = Column(String(255), nullable=False, comment='Номер машины')
    car = relationship("Car", back_populates="customer_cars")
    customer = relationship("User", back_populates="customer_cars")
