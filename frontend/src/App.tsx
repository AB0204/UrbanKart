import { useState, useEffect } from 'react';
import { productService, Product } from './services/productService';
import { cartService } from './services/cartService';
import './App.css';

function App() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [cartCount, setCartCount] = useState(0);

  useEffect(() => {
    loadProducts();
    loadCartCount();
  }, []);

  const loadProducts = async () => {
    try {
      const data = await productService.getAll();
      setProducts(data);
    } catch (error) {
      console.error('Error loading products:', error);
    } finally {
      setLoading(false);
    }
  };

  const loadCartCount = async () => {
    try {
      const token = localStorage.getItem('token');
      if (token) {
        const cartItems = await cartService.getCart();
        setCartCount(cartItems.reduce((sum, item) => sum + item.quantity, 0));
      }
    } catch (error) {
      console.error('Error loading cart:', error);
    }
  };

  const handleAddToCart = async (productId: number) => {
    try {
      // For demo purposes, we'll skip auth and just show alert
      // In production, check if user is logged in first
      const token = localStorage.getItem('token');
      if (!token) {
        alert('Please log in to add items to cart. Demo credentials:\nEmail: john.doe@example.com\nPassword: password');
        return;
      }

      await cartService.addToCart(productId);
      await loadCartCount();
      alert('Product added to cart!');
    } catch (error: any) {
      if (error.response?.status === 401) {
        alert('Please log in first. Demo credentials:\nEmail: john.doe@example.com\nPassword: password');
      } else {
        alert('Error adding product to cart');
      }
    }
  };

  if (loading) {
    return <div className="loading">Loading products...</div>;
  }

  return (
    <div className="App">
      <header className="header">
        <div className="container">
          <h1>🛒 E-Commerce Store</h1>
          <nav>
            <button className="cart-btn">
              🛍️ Cart ({cartCount})
            </button>
          </nav>
        </div>
      </header>

      <main className="container">
        <h2 className="section-title">Featured Products</h2>
        <div className="product-grid">
          {products.map((product) => (
            <div key={product.id} className="product-card">
              <img
                src={product.image_url}
                alt={product.name}
                className="product-image"
              />
              <div className="product-info">
                <h3 className="product-name">{product.name}</h3>
                <p className="product-description">{product.description}</p>
                <div className="product-footer">
                  <span className="product-price">${product.price}</span>
                  <button
                    className="add-to-cart-btn"
                    onClick={() => handleAddToCart(product.id)}
                  >
                    Add to Cart
                  </button>
                </div>
                {product.stock_quantity < 20 && (
                  <span className="stock-badge">Only {product.stock_quantity} left!</span>
                )}
              </div>
            </div>
          ))}
        </div>
      </main>

      <footer className="footer">
        <p>© 2024 E-Commerce Store. Built with FastAPI + React. API Docs at <a href="http://localhost:8000/docs" target="_blank">localhost:8000/docs</a></p>
      </footer>
    </div>
  );
}

export default App;
