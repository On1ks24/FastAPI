from sqlalchemy import Column, Integer, String
from ..database import Base

class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)
