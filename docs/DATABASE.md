# Database Schema

## Tables

### users
- `id` (INT, PK, AUTO_INCREMENT)
- `email` (VARCHAR(255), UNIQUE, NOT NULL)
- `password_hash` (VARCHAR(255), NOT NULL)
- `first_name` (VARCHAR(100))
- `last_name` (VARCHAR(100))
- `role` (ENUM: 'customer', 'admin')
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)

### categories
- `id` (INT, PK, AUTO_INCREMENT)
- `name` (VARCHAR(100), UNIQUE, NOT NULL)
- `description` (TEXT)
- `parent_id` (INT, FK to categories.id)
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)

### products
- `id` (INT, PK, AUTO_INCREMENT)
- `category_id` (INT, FK to categories.id)
- `name` (VARCHAR(255), NOT NULL)
- `description` (TEXT)
- `price` (DECIMAL(10,2), NOT NULL)
- `stock_quantity` (INT, NOT NULL, DEFAULT 0)
- `image_url` (VARCHAR(255))
- `is_active` (BOOLEAN, DEFAULT TRUE)
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)

### addresses
- `id` (INT, PK, AUTO_INCREMENT)
- `user_id` (INT, FK to users.id, NOT NULL)
- `street_address` (VARCHAR(255), NOT NULL)
- `city` (VARCHAR(100), NOT NULL)
- `state` (VARCHAR(100))
- `postal_code` (VARCHAR(20), NOT NULL)
- `country` (VARCHAR(100), NOT NULL)
- `is_default` (BOOLEAN, DEFAULT FALSE)
- `created_at` (TIMESTAMP)

### cart_items
- `id` (INT, PK, AUTO_INCREMENT)
- `user_id` (INT, FK to users.id, NOT NULL)
- `product_id` (INT, FK to products.id, NOT NULL)
- `quantity` (INT, NOT NULL, DEFAULT 1)
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)
- UNIQUE: (user_id, product_id)

### orders
- `id` (INT, PK, AUTO_INCREMENT)
- `user_id` (INT, FK to users.id, NOT NULL)
- `address_id` (INT, FK to addresses.id)
- `total_amount` (DECIMAL(10,2), NOT NULL)
- `status` (ENUM: 'pending', 'processing', 'shipped', 'delivered', 'cancelled')
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)

### order_items
- `id` (INT, PK, AUTO_INCREMENT)
- `order_id` (INT, FK to orders.id, NOT NULL)
- `product_id` (INT, FK to products.id)
- `quantity` (INT, NOT NULL)
- `price_at_purchase` (DECIMAL(10,2), NOT NULL)
- `created_at` (TIMESTAMP)

### inventory_logs
- `id` (INT, PK, AUTO_INCREMENT)
- `product_id` (INT, FK to products.id, NOT NULL)
- `change_amount` (INT, NOT NULL)
- `reason` (VARCHAR(255))
- `created_at` (TIMESTAMP)

## Triggers

### after_product_update
Logs changes to product stock quantity in the `inventory_logs` table.

## Stored Procedures

### CalculateOrderTotal(orderId INT)
Calculates and updates the total amount for an order based on its items.
