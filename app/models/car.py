from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    brand_id = Column(Integer, ForeignKey('brand.id'), nullable=False)
    model = Column(String(255), nullable=False)
    brand = relationship("Brand", back_populates="cars")
