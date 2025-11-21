from fastapi import APIRouter
from app.api import auth, products, cart

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(products.router, prefix="/products", tags=["Products"])
api_router.include_router(cart.router, prefix="/cart", tags=["Shopping Cart"])
