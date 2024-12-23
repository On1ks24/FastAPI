from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class OrderService(Base):
    __tablename__ = 'order_service'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    service = relationship("Service", back_populates="order_services")
    order = relationship("Order", back_populates="order_services")
