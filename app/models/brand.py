from sqlalchemy import Column, Integer, String
from ..database import Base

class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
