from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f'User {self.username}'