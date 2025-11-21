from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.product import Product
from app.models.user import User
from app.schemas.product import ProductResponse, ProductCreate, ProductUpdate
from app.core.auth import get_current_user, get_current_admin

router = APIRouter()

# Mock data for demo when database is not available
MOCK_PRODUCTS = [
    {"id": 1, "name": "Sony WH-1000XM5 Wireless Headphones", "description": "Industry-leading noise canceling with premium audio quality. 30-hour battery life.", "price": 399.99, "stock_quantity": 45, "image_url": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400", "category_id": 1, "is_active": True},
    {"id": 2, "name": "Apple AirPods Pro (2nd Gen)", "description": "Active Noise Cancellation, Adaptive Transparency, and personalized Spatial Audio.", "price": 249.99, "stock_quantity": 120, "image_url": "https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=400", "category_id": 1, "is_active": True},
    {"id": 3, "name": "MacBook Pro 14\" M3 Pro", "description": "18GB RAM, 512GB SSD, Liquid Retina XDR display. Perfect for professionals.", "price": 1999.99, "stock_quantity": 15, "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400", "category_id": 2, "is_active": True},
    {"id": 4, "name": "iPhone 15 Pro Max 256GB", "description": "A17 Pro chip, titanium design, advanced camera system, Action button.", "price": 1199.99, "stock_quantity": 35, "image_url": "https://images.unsplash.com/photo-1592286927505-b0c2966d00b8?w=400", "category_id": 3, "is_active": True},
    {"id": 5, "name": "Premium Cotton T-Shirt", "description": "Soft, breathable 100% organic cotton. Available in 10 colors. Unisex fit.", "price": 29.99, "stock_quantity": 200, "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400", "category_id": 5, "is_active": True},
    {"id": 6, "name": "Logitech MX Master 3S Wireless Mouse", "description": "Ergonomic design, 8K DPI sensor, quiet clicks, USB-C charging.", "price": 99.99, "stock_quantity": 85, "image_url": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=400", "category_id": 2, "is_active": True},
    {"id": 7, "name": "Samsung Galaxy S24 Ultra", "description": "200MP camera, S Pen included, 12GB RAM, stunning AMOLED display.", "price": 1299.99, "stock_quantity": 28, "image_url": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400", "category_id": 3, "is_active": True},
    {"id": 8, "name": "Yoga Mat Premium", "description": "Non-slip, eco-friendly, 6mm thick. Perfect for yoga and pilates.", "price": 39.99, "stock_quantity": 140, "image_url": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=400", "category_id": 8, "is_active": True},
]

@router.get("/", response_model=List[ProductResponse])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        products = db.query(Product).offset(skip).limit(limit).all()
        return products
    except Exception as e:
        # Return mock data if database is not available
        print(f"Database error, using mock data: {e}")
        return MOCK_PRODUCTS

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    try:
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    except HTTPException:
        raise
    except Exception as e:
        # Try to find in mock data
        print(f"Database error, checking mock data: {e}")
        for product in MOCK_PRODUCTS:
            if product["id"] == product_id:
                return product
        raise HTTPException(status_code=404, detail="Product not found")

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return None
