# API Documentation

Base URL: `http://localhost:8000`

## Authentication

### Register
**POST** `/api/auth/register`

```json
{
  "email": "user@example.com",
  "password": "password123",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Response**: `201 Created`
```json
{
  "id": 1,
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "role": "customer",
  "created_at": "2024-01-01T00:00:00"
}
```

### Login
**POST** `/api/auth/login`

Form data:
- `username`: email
- `password`: password

**Response**: `200 OK`
```json
{
  "access_token": "eyJ...",
  "token_type": "bearer"
}
```

## Products

### Get All Products
**GET** `/api/products`

Query Parameters:
- `skip` (optional, default: 0)
- `limit` (optional, default: 100)

**Response**: `200 OK`
```json
[
  {
    "id": 1,
    "name": "Product Name",
    "description": "Product description",
    "price": 29.99,
    "stock_quantity": 100,
    "category_id": 1,
    "image_url": "https://...",
    "is_active": true
  }
]
```

### Get Product by ID
**GET** `/api/products/{product_id}`

**Response**: `200 OK`

### Create Product (Admin Only)
**POST** `/api/products`

Headers:
- `Authorization: Bearer <token>`

```json
{
  "name": "New Product",
  "description": "Product description",
  "price": 49.99,
  "stock_quantity": 50,
  "category_id": 1,
  "image_url": "https://...",
  "is_active": true
}
```

**Response**: `201 Created`

### Update Product (Admin Only)
**PUT** `/api/products/{product_id}`

Headers:
- `Authorization: Bearer <token>`

```json
{
  "price": 39.99,
  "stock_quantity": 75
}
```

**Response**: `200 OK`

### Delete Product (Admin Only)
**DELETE** `/api/products/{product_id}`

Headers:
- `Authorization: Bearer <token>`

**Response**: `204 No Content`

## Interactive Documentation

Visit `http://localhost:8000/docs` for Swagger UI with interactive API documentation.
