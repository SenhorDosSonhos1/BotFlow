from app.database import Base
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, DECIMAL



from datetime import datetime


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id =  Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    price = Column(DECIMAL, nullable=False)
    status = Column(String, default="PENDING", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.now, default=datetime.utcnow) #Quando atualiza