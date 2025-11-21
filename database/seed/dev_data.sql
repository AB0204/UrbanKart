-- Sample Users
INSERT INTO users (email, password_hash, first_name, last_name, role) VALUES
('admin@ecommerce.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWEMvUuO', 'Admin', 'User', 'admin'),
('john.doe@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWEMvUuO', 'John', 'Doe', 'customer'),
('jane.smith@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWEMvUuO', 'Jane', 'Smith', 'customer');

-- Sample Categories
INSERT INTO categories (name, description) VALUES
('Electronics', 'Electronic devices and accessories'),
('Clothing', 'Apparel and fashion items'),
('Books', 'Physical and digital books'),
('Home & Garden', 'Home improvement and gardening supplies');

-- Sample Products
INSERT INTO products (category_id, name, description, price, stock_quantity, image_url, is_active) VALUES
(1, 'Wireless Headphones', 'High-quality Bluetooth headphones with noise cancellation', 79.99, 50, 'https://via.placeholder.com/300', TRUE),
(1, 'Smart Watch', 'Fitness tracker with heart rate monitor', 199.99, 30, 'https://via.placeholder.com/300', TRUE),
(2, 'Cotton T-Shirt', 'Comfortable cotton t-shirt in various colors', 19.99, 100, 'https://via.placeholder.com/300', TRUE),
(2, 'Denim Jeans', 'Classic blue denim jeans', 49.99, 75, 'https://via.placeholder.com/300', TRUE),
(3, 'Programming Book', 'Learn Python programming from scratch', 39.99, 40, 'https://via.placeholder.com/300', TRUE),
(4, 'Garden Tools Set', 'Complete set of essential garden tools', 89.99, 25, 'https://via.placeholder.com/300', TRUE);

-- Sample Addresses
INSERT INTO addresses (user_id, street_address, city, state, postal_code, country, is_default) VALUES
(2, '123 Main St', 'San Francisco', 'CA', '94102', 'USA', TRUE),
(3, '456 Oak Ave', 'New York', 'NY', '10001', 'USA', TRUE);

-- Sample Cart Items
INSERT INTO cart_items (user_id, product_id, quantity) VALUES
(2, 1, 2),
(2, 3, 1),
(3, 2, 1);
