from pydantic import BaseModel
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int
    quantity: int = 1

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    quantity: int

class CartItemResponse(CartItemBase):
    id: int
    user_id: int
    product_name: Optional[str] = None
    product_price: Optional[float] = None

    class Config:
        from_attributes = True
