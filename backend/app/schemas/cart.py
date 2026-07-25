from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int
    quantity: int = Field(default=1, gt=0)

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    quantity: int = Field(gt=0)

class CartItemResponse(CartItemBase):
    id: int
    user_id: int
    product_name: Optional[str] = None
    product_price: Optional[float] = None

    class Config:
        from_attributes = True
