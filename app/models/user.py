from app.database import Base, engine
from sqlalchemy import Column, Integer, String, DateTime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password_hash = Column(String)
    created_at = Column(DateTime)

    def __str__(self):
        return f'User {self.username}'