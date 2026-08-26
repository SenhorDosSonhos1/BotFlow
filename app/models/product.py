from app.database import Base
from sqlalchemy import Integer, String, Column, DECIMAL, DateTime, Text, Boolean
from datetime import datetime

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    price = Column(DECIMAL)
    active = Column(Boolean)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


