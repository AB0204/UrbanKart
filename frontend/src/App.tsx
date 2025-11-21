import { useState, useEffect } from 'react';
import { MOCK_PRODUCTS } from './mockProducts';
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

const CATEGORIES = [
  { id: 0, name: 'All Products' },
  { id: 1, name: 'Electronics' },
  { id: 4, name: 'Gaming' },
  { id: 5, name: 'Fashion' },
  { id: 6, name: 'Beauty' },
  { id: 7, name: 'Fitness' },
  { id: 8, name: 'Home & Kitchen' },
];

function App() {
  const [products, setProducts] = useState<Product[]>([]);
  const [filteredProducts, setFilteredProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState(0);
  const [sortBy, setSortBy] = useState('name');
  const [cartCount, setCartCount] = useState(0);

  useEffect(() => {
    loadProducts();
  }, []);

  useEffect(() => {
    filterAndSortProducts();
  }, [products, searchQuery, selectedCategory, sortBy]);

  const loadProducts = async () => {
    // Simulate API delay for realism
    setTimeout(() => {
      setProducts(MOCK_PRODUCTS as Product[]);
      setLoading(false);
    }, 500);
  };

  const filterAndSortProducts = () => {
    let filtered = [...products];

    // Filter by search
    if (searchQuery) {
      filtered = filtered.filter(p =>
        p.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
        p.description.toLowerCase().includes(searchQuery.toLowerCase())
      );
    }

    // Filter by category
    if (selectedCategory !== 0) {
      filtered = filtered.filter(p => p.category_id === selectedCategory);
    }

    // Sort
    filtered.sort((a, b) => {
      switch (sortBy) {
        case 'price-low':
          return a.price - b.price;
        case 'price-high':
          return b.price - a.price;
        case 'name':
        default:
          return a.name.localeCompare(b.name);
      }
    });

    setFilteredProducts(filtered);
  };

  const handleAddToCart = () => {
    setCartCount(prev => prev + 1);
    // Simple animation feedback
    const btn = document.activeElement as HTMLElement;
    btn?.classList.add('added');
    setTimeout(() => btn?.classList.remove('added'), 600);
  };

  if (loading) {
    return (
      <div className="loading">
        <div className="spinner"></div>
        <h1>Loading UrbanKart...</h1>
      </div>
    );
  }

  return (
    <div className="App">
      <header className="header">
        <div className="container header-content">
          <div className="logo-section">
            <h1 className="logo">🏙️ UrbanKart</h1>
            <p className="tagline">Your Urban Lifestyle Destination</p>
          </div>
          <nav className="nav">
            <button className="cart-btn" onClick={() => alert(`Cart has ${cartCount} items!`)}>
              🛍️ Cart <span className="cart-badge">{cartCount}</span>
            </button>
          </nav>
        </div>
      </header>

      {/* Search and Filters */}
      <div className="filters-section">
        <div className="container">
          <div className="search-bar">
            <input
              type="text"
              placeholder="🔍 Search products..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="search-input"
            />
          </div>

          <div className="filters-row">
            <div className="category-filters">
              {CATEGORIES.map(cat => (
                <button
                  key={cat.id}
                  className={`filter-btn ${selectedCategory === cat.id ? 'active' : ''}`}
                  onClick={() => setSelectedCategory(cat.id)}
                >
                  {cat.name}
                </button>
              ))}
            </div>

            <select
              className="sort-select"
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
            >
              <option value="name">Sort by Name</option>
              <option value="price-low">Price: Low to High</option>
              <option value="price-high">Price: High to Low</option>
            </select>
          </div>
        </div>
      </div>

      <main className="container">
        <div className="results-header">
          <h2 className="section-title">
            {searchQuery ? `Search Results for "${searchQuery}"` :
              selectedCategory ? CATEGORIES.find(c => c.id === selectedCategory)?.name :
                'All Products'}
          </h2>
          <p className="results-count">{filteredProducts.length} products found</p>
        </div>

        {filteredProducts.length === 0 ? (
          <div className="no-results">
            <p>😔 No products found. Try a different search or category.</p>
          </div>
        ) : (
          <div className="product-grid">
            {filteredProducts.map((product) => (
              <div key={product.id} className="product-card">
                <div className="product-image-wrapper">
                  <img
                    src={product.image_url}
                    alt={product.name}
                    className="product-image"
                    onError={(e) => {
                      (e.target as HTMLImageElement).src = 'https://via.placeholder.com/400x300?text=Product';
                    }}
                  />
                  {product.stock_quantity < 20 && (
                    <span className="stock-badge">Only {product.stock_quantity} left!</span>
                  )}
                </div>
                <div className="product-info">
                  <h3 className="product-name">{product.name}</h3>
                  <p className="product-description">{product.description}</p>
                  <div className="product-footer">
                    <span className="product-price">${product.price.toFixed(2)}</span>
                    <button
                      className="add-to-cart-btn"
                      onClick={() => handleAddToCart()}
                    >
                      Add to Cart
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>

      <footer className="footer">
        <div className="container">
          <p>© 2024 UrbanKart - Your Urban Lifestyle Destination</p>
          <p>Built with ❤️ using FastAPI + React</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
