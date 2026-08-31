from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class OrderCreate(BaseModel):
    product_id: int 


class OrderResponse(OrderCreate):
    id: int
    user_id: int 
    price: Decimal
    status: str 
    created_at: datetime
    updated_at: datetime