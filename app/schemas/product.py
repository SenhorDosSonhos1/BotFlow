from pydantic import BaseModel, ConfigDict
from decimal import Decimal

class ProductBase(BaseModel):
    name: str 
    description: str 
    price: Decimal 
    active: bool 

class ProductCreate(ProductBase):
    pass 

class ProductUpdate(ProductBase):
    pass 

class ProductResponse(ProductBase):
    id: int 

    model_config = ConfigDict(from_attributes=True)