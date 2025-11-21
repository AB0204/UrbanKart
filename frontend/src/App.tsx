import { useState, useEffect } from 'react';
import './App.css';

interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  stock_quantity: number;
  image_url: string;
  category_id: number;
  is_active: boolean;
}

function App() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    loadProducts();
  }, []);

  const loadProducts = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/products');
      if (!response.ok) {
        throw new Error('Failed to fetch products');
      }
      const data = await response.json();
      setProducts(data);
      setError('');
    } catch (err: any) {
      console.error('Error loading products:', err);
      setError('Failed to load products. Make sure the backend is running on port 8000.');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="loading">
        <h1>Loading products...</h1>
      </div>
    );
  }

  if (error) {
    return (
      <div className="loading">
        <h1 style={{ color: 'red' }}>⚠️ {error}</h1>
        <p>Backend URL: http://localhost:8000</p>
      </div>
    );
  }

  return (
    <div className="App">
      <header className="header">
        <div className="container">
          <h1>🛒 E-Commerce Store</h1>
          <nav>
            <button className="cart-btn">
              🛍️ Cart (0)
            </button>
          </nav>
        </div>
      </header>

      <main className="container">
        <h2 className="section-title">Featured Products ({products.length})</h2>
        <div className="product-grid">
          {products.map((product) => (
            <div key={product.id} className="product-card">
              <img
                src={product.image_url}
                alt={product.name}
                className="product-image"
                onError={(e) => {
                  (e.target as HTMLImageElement).src = 'https://via.placeholder.com/400x300?text=Product+Image';
                }}
              />
              <div className="product-info">
                <h3 className="product-name">{product.name}</h3>
                <p className="product-description">{product.description}</p>
                <div className="product-footer">
                  <span className="product-price">${product.price}</span>
                  <button
                    className="add-to-cart-btn"
                    onClick={() => alert('Added to cart! (Login required for full functionality)')}
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
        <p>Loaded {products.length} products successfully!</p>
      </footer>
    </div>
  );
}

export default App;
