-- Sample Users
INSERT INTO users (email, password_hash, first_name, last_name, role) VALUES
('admin@ecommerce.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWEMvUuO', 'Admin', 'User', 'admin'),
('john.doe@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWEMvUuO', 'John', 'Doe', 'customer'),
('jane.smith@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWEMvUuO', 'Jane', 'Smith', 'customer'),
('mike.wilson@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWEMvUuO', 'Mike', 'Wilson', 'customer');

-- Sample Categories
INSERT INTO categories (name, description) VALUES
('Electronics', 'Electronic devices and accessories'),
('Computers', 'Laptops, desktops, and computer accessories'),
('Smartphones', 'Mobile phones and accessories'),
('Audio', 'Headphones, speakers, and audio equipment'),
('Clothing', 'Apparel and fashion items'),
('Books', 'Physical and digital books'),
('Home & Garden', 'Home improvement and gardening supplies'),
('Sports', 'Sports equipment and fitness gear');

-- Sample Products (Realistic E-commerce items)
INSERT INTO products (category_id, name, description, price, stock_quantity, image_url, is_active) VALUES
-- Electronics
(1, 'Sony WH-1000XM5 Wireless Headphones', 'Industry-leading noise canceling with premium audio quality. 30-hour battery life.', 399.99, 45, 'https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=400', TRUE),
(1, 'Apple AirPods Pro (2nd Gen)', 'Active Noise Cancellation, Adaptive Transparency, and personalized Spatial Audio.', 249.99, 120, 'https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=400', TRUE),
(1, 'Samsung 55" QLED 4K Smart TV', 'Quantum HDR, Object Tracking Sound, and Gaming Hub. Stunning 4K display.', 897.99, 28, 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400', TRUE),

-- Computers
(2, 'MacBook Pro 14" M3 Pro', '18GB RAM, 512GB SSD, Liquid Retina XDR display. Perfect for professionals.', 1999.99, 15, 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400', TRUE),
(2, 'Dell XPS 15 Laptop', 'Intel i7, 16GB RAM, 512GB SSD, 15.6" FHD+ display. Premium build quality.', 1499.99, 22, 'https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=400', TRUE),
(2, 'Logitech MX Master 3S Wireless Mouse', 'Ergonomic design, 8K DPI sensor, quiet clicks, USB-C charging.', 99.99, 85, 'https://images.unsplash.com/photo-1527814050087-3793815479db?w=400', TRUE),
(2, 'Mechanical Gaming Keyboard RGB', 'Cherry MX switches, customizable RGB, aluminum frame, programmable keys.', 149.99, 60, 'https://images.unsplash.com/photo-1595225476474-87563907a212?w=400', TRUE),

-- Smartphones
(3, 'iPhone 15 Pro Max 256GB', 'A17 Pro chip, titanium design, advanced camera system, Action button.', 1199.99, 35, 'https://images.unsplash.com/photo-1592286927505-b0c2966d00b8?w=400', TRUE),
(3, 'Samsung Galaxy S24 Ultra', '200MP camera, S Pen included, 12GB RAM, stunning AMOLED display.', 1299.99, 28, 'https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400', TRUE),
(3, 'Google Pixel 8 Pro', 'Best Android camera, AI features, clean Android experience, 5G enabled.', 999.99, 42, 'https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=400', TRUE),

-- Audio
(4, 'Bose SoundLink Flex Speaker', 'Waterproof portable Bluetooth speaker, 12-hour battery, exceptional sound.', 149.99, 75, 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400', TRUE),
(4, 'Audio-Technica AT2020 Microphone', 'Professional cardioid condenser mic, perfect for streaming and recording.', 99.99, 50, 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=400', TRUE),

-- Clothing
(5, 'Premium Cotton T-Shirt', 'Soft, breathable 100% organic cotton. Available in 10 colors. Unisex fit.', 29.99, 200, 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400', TRUE),
(5, 'Classic Denim Jeans', 'Comfortable stretch denim, classic fit, durable construction. Multiple sizes.', 59.99, 150, 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400', TRUE),
(5, 'Wool Blend Sweater', 'Cozy and warm, perfect for winter. Machine washable. Premium quality.', 79.99, 90, 'https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=400', TRUE),
(5, 'Athletic Running Shoes', 'Lightweight, responsive cushioning, breathable mesh. Great for running.', 129.99, 110, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400', TRUE),

-- Books
(6, 'Clean Code by Robert Martin', 'A handbook of agile software craftsmanship. Essential for developers.', 39.99, 65, 'https://images.unsplash.com/photo-1532012197267-da84d127e765?w=400', TRUE),
(6, 'Atomic Habits by James Clear', 'Transform your life with tiny changes. #1 New York Times bestseller.', 27.99, 120, 'https://images.unsplash.com/photo-1589829085413-56de8ae18c73?w=400', TRUE),
(6, 'The Lean Startup', 'How todays entrepreneurs build successful businesses. Business essential.', 24.99, 80, 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400', TRUE),

-- Home & Garden
(7, 'Robot Vacuum Cleaner', 'Smart navigation, 2000Pa suction, app control, works with Alexa.', 299.99, 40, 'https://images.unsplash.com/photo-1558317374-067fb5f30001?w=400', TRUE),
(7, 'Indoor Plant Set (3 Plants)', 'Easy-care succulents, perfect for home or office. Includes decorative pots.', 49.99, 95, 'https://images.unsplash.com/photo-1459411621453-7b03977f4bfc?w=400', TRUE),
(7, 'Stainless Steel Cookware Set', '10-piece professional-grade cookware. Induction compatible, dishwasher safe.', 249.99, 35, 'https://images.unsplash.com/photo-1584990347449-39f4ca916c6a?w=400', TRUE),

-- Sports
(8, 'Yoga Mat Premium', 'Non-slip, eco-friendly, 6mm thick. Perfect for yoga and pilates.', 39.99, 140, 'https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=400', TRUE),
(8, 'Adjustable Dumbbells Set', '5-52.5 lbs per dumbbell. Space-saving, quick weight adjustment.', 349.99, 25, 'https://images.unsplash.com/photo-1638183910567-3e6368ce8e43?w=400', TRUE),
(8, 'Resistance Bands Set', '5 bands with different resistance levels. Perfect for home workouts.', 24.99, 180, 'https://images.unsplash.com/photo-1598289431512-b97b0917affc?w=400', TRUE);

-- Sample Addresses
INSERT INTO addresses (user_id, street_address, city, state, postal_code, country, is_default) VALUES
(2, '123 Main St', 'San Francisco', 'CA', '94102', 'USA', TRUE),
(3, '456 Oak Ave', 'New York', 'NY', '10001', 'USA', TRUE),
(4, '789 Pine Rd', 'Austin', 'TX', '78701', 'USA', TRUE);

-- Sample Cart Items
INSERT INTO cart_items (user_id, product_id, quantity) VALUES
(2, 1, 1),
(2, 13, 2),
(3, 8, 1),
(3, 20, 1),
(4, 5, 1);
