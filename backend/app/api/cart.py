from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.cart import CartItem
from app.models.product import Product
from app.models.user import User
from app.schemas.cart import CartItemCreate, CartItemUpdate, CartItemResponse
from app.core.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[dict])
def get_cart(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    rows = (
        db.query(CartItem, Product)
        .join(Product, CartItem.product_id == Product.id, isouter=True)
        .filter(CartItem.user_id == current_user.id)
        .all()
    )

    return [
        {
            "id": item.id,
            "product_id": item.product_id,
            "product_name": product.name if product else None,
            "product_price": float(product.price) if product else None,
            "product_image": product.image_url if product else None,
            "quantity": item.quantity,
            "subtotal": float(product.price * item.quantity) if product else 0,
        }
        for item, product in rows
    ]

@router.post("/", response_model=CartItemResponse, status_code=status.HTTP_201_CREATED)
def add_to_cart(
    cart_item: CartItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == cart_item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    existing_item = db.query(CartItem).filter(
        CartItem.user_id == current_user.id,
        CartItem.product_id == cart_item.product_id
    ).first()

    desired_qty = (existing_item.quantity + cart_item.quantity) if existing_item else cart_item.quantity
    if desired_qty > product.stock_quantity:
        raise HTTPException(status_code=400, detail="Requested quantity exceeds available stock")

    if existing_item:
        existing_item.quantity = desired_qty
        db.commit()
        db.refresh(existing_item)
        return existing_item

    new_item = CartItem(
        user_id=current_user.id,
        product_id=cart_item.product_id,
        quantity=cart_item.quantity,
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.put("/{item_id}", response_model=CartItemResponse)
def update_cart_item(
    item_id: int,
    cart_item: CartItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == current_user.id
    ).first()
    
    if not db_item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    product = db.query(Product).filter(Product.id == db_item.product_id).first()
    if product and cart_item.quantity > product.stock_quantity:
        raise HTTPException(status_code=400, detail="Requested quantity exceeds available stock")

    db_item.quantity = cart_item.quantity
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_from_cart(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == current_user.id
    ).first()
    
    if not db_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    db.delete(db_item)
    db.commit()
    return None

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def clear_cart(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db.query(CartItem).filter(CartItem.user_id == current_user.id).delete()
    db.commit()
    return None
