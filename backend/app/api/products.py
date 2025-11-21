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
    # Electronics & Tech
    {"id": 1, "name": "Sony WH-1000XM5 Headphones", "description": "Industry-leading noise canceling with premium audio quality. 30-hour battery life.", "price": 399.99, "stock_quantity": 45, "image_url": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400", "category_id": 1, "is_active": True},
    {"id": 2, "name": "Apple AirPods Pro (2nd Gen)", "description": "Active Noise Cancellation, Adaptive Transparency, personalized Spatial Audio.", "price": 249.99, "stock_quantity": 120, "image_url": "https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=400", "category_id": 1, "is_active": True},
    {"id": 3, "name": "MacBook Pro 14\" M3", "description": "18GB RAM, 512GB SSD, Liquid Retina XDR display. Perfect for professionals.", "price": 1999.99, "stock_quantity": 15, "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400", "category_id": 2, "is_active": True},
    {"id": 4, "name": "iPhone 15 Pro Max", "description": "A17 Pro chip, titanium design, advanced camera system.", "price": 1199.99, "stock_quantity": 35, "image_url": "https://images.unsplash.com/photo-1592286927505-b0c2966d00b8?w=400", "category_id": 3, "is_active": True},
    {"id": 5, "name": "Logitech MX Master 3S", "description": "Ergonomic wireless mouse, 8K DPI sensor, USB-C charging.", "price": 99.99, "stock_quantity": 85, "image_url": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=400", "category_id": 2, "is_active": True},
    
    # Gaming
    {"id": 6, "name": "PlayStation 5 Console", "description": "Next-gen gaming with ultra-fast SSD and ray tracing. Includes controller.", "price": 499.99, "stock_quantity": 12, "image_url": "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400", "category_id": 4, "is_active": True},
    {"id": 7, "name": "Xbox Series X", "description": "4K gaming at 120fps. 1TB SSD, Game Pass ready.", "price": 499.99, "stock_quantity": 18, "image_url": "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=400", "category_id": 4, "is_active": True},
    {"id": 8, "name": "Nintendo Switch OLED", "description": "7-inch OLED screen, enhanced audio, 64GB internal storage.", "price": 349.99, "stock_quantity": 42, "image_url": "https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=400", "category_id": 4, "is_active": True},
    {"id": 9, "name": "Gaming Mechanical Keyboard", "description": "RGB backlit, Cherry MX switches, aluminum frame.", "price": 149.99, "stock_quantity": 65, "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?w=400", "category_id": 4, "is_active": True},
    {"id": 10, "name": "Gaming Headset 7.1", "description": "Surround sound, noise-canceling mic, comfortable ear cups.", "price": 89.99, "stock_quantity": 78, "image_url": "https://images.unsplash.com/photo-1599669454699-248893623440?w=400", "category_id": 4, "is_active": True},
    
    # Fashion - Men
    {"id": 11, "name": "Premium Cotton T-Shirt", "description": "Soft, breathable 100% organic cotton. Available in 10 colors.", "price": 29.99, "stock_quantity": 200, "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400", "category_id": 5, "is_active": True},
    {"id": 12, "name": "Classic Denim Jeans", "description": "Comfortable stretch denim, classic fit, durable construction.", "price": 59.99, "stock_quantity": 150, "image_url": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=400", "category_id": 5, "is_active": True},
    {"id": 13, "name": "Leather Jacket", "description": "Genuine leather, timeless design, fully lined interior.", "price": 299.99, "stock_quantity": 25, "image_url": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400", "category_id": 5, "is_active": True},
    {"id": 14, "name": "Sneakers - White", "description": "Classic white sneakers, comfortable sole, versatile style.", "price": 89.99, "stock_quantity": 95, "image_url": "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400", "category_id": 5, "is_active": True},
    {"id": 15, "name": "Casual Hoodie", "description": "Ultra-soft fleece, kangaroo pocket, relaxed fit.", "price": 49.99, "stock_quantity": 120, "image_url": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400", "category_id": 5, "is_active": True},
    
    # Fashion - Women
    {"id": 16, "name": "Floral Summer Dress", "description": "Lightweight fabric, flattering fit, perfect for summer.", "price": 79.99, "stock_quantity": 55, "image_url": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400", "category_id": 5, "is_active": True},
    {"id": 17, "name": "Designer Handbag", "description": "Genuine leather, multiple compartments, elegant design.", "price": 249.99, "stock_quantity": 18, "image_url": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=400", "category_id": 5, "is_active": True},
    {"id": 18, "name": "High-Waist Yoga Pants", "description": "Moisture-wicking, 4-way stretch, squat-proof.", "price": 45.99, "stock_quantity": 140, "image_url": "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=400", "category_id": 5, "is_active": True},
    {"id": 19, "name": "Silk Scarf", "description": "100% pure silk, vibrant colors, versatile styling.", "price": 39.99, "stock_quantity": 72, "image_url": "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=400", "category_id": 5, "is_active": True},
    
    # Beauty & Skincare
    {"id": 20, "name": "Vitamin C Serum", "description": "Brightening serum, reduces dark spots, anti-aging formula.", "price": 34.99, "stock_quantity": 88, "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400", "category_id": 6, "is_active": True},
    {"id": 21, "name": "Luxury Face Cream", "description": "Hydrating moisturizer with hyaluronic acid and peptides.", "price": 59.99, "stock_quantity": 65, "image_url": "https://images.unsplash.com/photo-1556228994-d76d89c2f3a5?w=400", "category_id": 6, "is_active": True},
    {"id": 22, "name": "Makeup Brush Set", "description": "Professional 12-piece set, soft bristles, travel case included.", "price": 44.99, "stock_quantity": 92, "image_url": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400", "category_id": 6, "is_active": True},
    {"id": 23, "name": "Natural Lip Balm Set", "description": "Organic ingredients, 6 flavors, SPF protection.", "price": 19.99, "stock_quantity": 150, "image_url": "https://images.unsplash.com/photo-1596755389378-c31d21fd1273?w=400", "category_id": 6, "is_active": True},
    {"id": 24, "name": "Hair Straightener Pro", "description": "Ceramic plates, adjustable temperature, quick heat-up.", "price": 79.99, "stock_quantity": 48, "image_url": "https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=400", "category_id": 6, "is_active": True},
    {"id": 25, "name": "Perfume Gift Set", "description": "5 luxury fragrances, elegant packaging, perfect gift.", "price": 129.99, "stock_quantity": 35, "image_url": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400", "category_id": 6, "is_active": True},
    
    # Fitness & Wellness
    {"id": 26, "name": "Yoga Mat Premium", "description": "Non-slip, eco-friendly, 6mm thick. Perfect for yoga.", "price": 39.99, "stock_quantity": 140, "image_url": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=400", "category_id": 7, "is_active": True},
    {"id": 27, "name": "Adjustable Dumbbells", "description": "5-52.5 lbs per dumbbell. Space-saving design.", "price": 349.99, "stock_quantity": 25, "image_url": "https://images.unsplash.com/photo-1638183910567-3e6368ce8e43?w=400", "category_id": 7, "is_active": True},
    {"id": 28, "name": "Resistance Bands Set", "description": "5 bands with different resistance levels. Home workout essential.", "price": 24.99, "stock_quantity": 180, "image_url": "https://images.unsplash.com/photo-1598289431512-b97b0917affc?w=400", "category_id": 7, "is_active": True},
    {"id": 29, "name": "Smart Watch Fitness", "description": "Heart rate monitor, GPS, 50+ sport modes, waterproof.", "price": 199.99, "stock_quantity": 62, "image_url": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=400", "category_id": 7, "is_active": True},
    {"id": 30, "name": "Protein Powder Vanilla", "description": "25g protein per serving, grass-fed whey, no artificial flavors.", "price": 49.99, "stock_quantity": 95, "image_url": "https://images.unsplash.com/photo-1579722821273-0f6c7d44362f?w=400", "category_id": 7, "is_active": True},
    {"id": 31, "name": "Foam Roller", "description": "Deep tissue massage, muscle recovery, textured surface.", "price": 29.99, "stock_quantity": 110, "image_url": "https://images.unsplash.com/photo-1611672585731-fa10603fb9e0?w=400", "category_id": 7, "is_active": True},
    {"id": 32, "name": "Jump Rope Pro", "description": "Weighted handles, adjustable length, smooth ball bearings.", "price": 19.99, "stock_quantity": 145, "image_url": "https://images.unsplash.com/photo-1601422407692-ec4eeec1d9b3?w=400", "category_id": 7, "is_active": True},
    
    # Home & Kitchen
    {"id": 33, "name": "Robot Vacuum Cleaner", "description": "Smart navigation, 2000Pa suction, app control, Alexa compatible.", "price": 299.99, "stock_quantity": 40, "image_url": "https://images.unsplash.com/photo-1558317374-067fb5f30001?w=400", "category_id": 8, "is_active": True},
    {"id": 34, "name": "Espresso Machine", "description": "15-bar pressure, milk frother, programmable settings.", "price": 249.99, "stock_quantity": 32, "image_url": "https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=400", "category_id": 8, "is_active": True},
    {"id": 35, "name": "Air Fryer XL", "description": "7-quart capacity, digital touchscreen, 8 presets.", "price": 129.99, "stock_quantity": 58, "image_url": "https://images.unsplash.com/photo-1585515320310-259814833e62?w=400", "category_id": 8, "is_active": True},
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
