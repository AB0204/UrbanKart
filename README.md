# E-Commerce-Management-System

## Current Plan - Tech Stack

* **Backend:** Python (FastAPI, SQLAlchemy, Pydantic)
* **Database:** MySQL (with triggers, stored procedures, roles)
* **Frontend:** React.js + TypeScript (SPA, Context API for state)
* **Security:** JWT (auth), bcrypt/Argon2 (passwords), HTTPS (network)
* **Other Tools:** Axios (API calls), Docker (optional deployment)

## Current Plan - Phases

### **Phase 1: Database Schema (MySQL)**

* Define all relevant tables.
* Add constraints, foreign keys, indexing.
* Write triggers (e.g., update stock on order).
* Write stored procedures (e.g., calculate order total).
* Insert sample data for testing.


### **Phase 2: Backend (FastAPI + SQLAlchemy)**

**2.1 Setup & DB Interaction**

* Initialize FastAPI project.
* Configure MySQL connection with SQLAlchemy.
* Create ORM models mapped to DB tables.
* Create repository layer (CRUD for each entity).

**2.2 Authentication & Security**

* User registration & login endpoints.
* Password hashing (bcrypt/Argon2).
* JWT token generation & validation.
* Role-based access (admin vs customer).

**2.3 Core Business Logic**

* Admin: product CRUD, stock management APIs.
* Customer: view products, cart management APIs.
* Order placement API: calculates totals (via stored procedure), updates stock (via trigger).

**2.4 API Organization & Utilities**

* Create Pydantic schemas (DTOs).
* Centralized exception handling.
* Middleware for request logging & error tracking.

### **Phase 3: Frontend (React.js + TypeScript)**

**3.1 Setup & Routing**

* Initialize React project.
* Add routing (React Router) for Home, Product, Cart, Checkout, Admin Dashboard.

**3.2 Components & State Management**

* Build reusable components: Navbar, ProductCard, CartItem, Forms.
* Set up Context API for Auth and Cart.

**3.3 API Integration**

* Create API services with Axios (auth, products, cart, orders).
* Connect login/register to backend JWT system.
* Fetch/display product catalog.
* Implement cart add/remove & checkout flow.
* Admin dashboard for managing products.

### **Phase 4: Testing & Finalization**

**4.1 Backend Testing**

* Unit tests for services (FastAPI + pytest).
* API endpoint testing with test DB.

**4.2 Frontend Testing**

* Component rendering tests (Jest/React Testing Library).
* Integration tests: login, add to cart, checkout.

**4.3 Security & Deployment Prep**

* Validate JWT expiry & refresh flow.
* Secure API routes with role checks.
* Use HTTPS (TLS).
* Finalize README, API docs, and ERD diagram.

## Planned Directory Structure
```
ecommerce-management-system/
├── README.md
├── .env.example
├── .gitignore
├── setup.sh                            # Quick project setup script
│
├── backend/                             # FastAPI Backend
│   ├── .env
│   ├── requirements.txt
│   ├── main.py                          # FastAPI app entry point
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py                    # Environment configuration
│   │   ├── database.py                  # Database connection & session
│   │   ├── dependencies.py              # Common dependencies (auth, db)
│   │   │
│   │   ├── core/                        # Core functionality
│   │   │   ├── __init__.py
│   │   │   ├── auth.py                  # JWT authentication
│   │   │   ├── security.py              # Password hashing, security utils
│   │   │   └── permissions.py           # Role-based permissions
│   │   │
│   │   ├── models/                      # SQLAlchemy ORM models
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── product.py
│   │   │   ├── category.py
│   │   │   ├── order.py
│   │   │   ├── cart.py
│   │   │   └── address.py
│   │   │
│   │   ├── schemas/                     # Pydantic schemas (DTOs)
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── product.py
│   │   │   ├── category.py
│   │   │   ├── order.py
│   │   │   ├── cart.py
│   │   │   └── address.py
│   │   │
│   │   ├── repositories/                # Data access layer (Repository pattern)
│   │   │   ├── __init__.py
│   │   │   ├── base.py                  # Base repository class
│   │   │   ├── user_repository.py
│   │   │   ├── product_repository.py
│   │   │   ├── order_repository.py
│   │   │   └── cart_repository.py
│   │   │
│   │   ├── services/                    # Business logic layer
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py
│   │   │   ├── user_service.py
│   │   │   ├── product_service.py
│   │   │   ├── order_service.py
│   │   │   └── cart_service.py
│   │   │
│   │   ├── api/                         # API route handlers
│   │   │   ├── __init__.py
│   │   │   ├── auth.py                  # Authentication endpoints
│   │   │   ├── users.py                 # User management
│   │   │   ├── products.py              # Product CRUD
│   │   │   ├── orders.py                # Order management
│   │   │   ├── cart.py                  # Shopping cart
│   │   │   ├── admin.py                 # Admin-only endpoints
│   │   │   └── main.py                  # API router aggregation
│   │   │
│   │   ├── utils/                       # Utility functions
│   │   │   ├── __init__.py
│   │   │   ├── logger.py                # Logging configuration
│   │   │   └── validators.py            # Custom validators
│   │   │
│   │   └── tests/                       # Backend tests
│   │       ├── __init__.py
│   │       ├── conftest.py              # Pytest configuration
│   │       ├── test_auth.py
│   │       ├── test_products.py
│   │       ├── test_orders.py
│   │       └── test_cart.py
│   │
│   └── alembic/                         # Database migrations (optional)
│       ├── versions/
│       ├── script.py.mako
│       ├── env.py
│       └── alembic.ini
│
├── database/                            # Database scripts
│   ├── README.md                        # Database setup instructions
│   │
│   ├── init/                           # Initial database setup
│   │   ├── 01_create_database.sql
│   │   └── 02_create_roles.sql
│   │
│   ├── schema/                         # Database schema definitions
│   │   ├── 01_users_table.sql
│   │   ├── 02_categories_table.sql
│   │   ├── 03_products_table.sql
│   │   ├── 04_addresses_table.sql
│   │   ├── 05_cart_items_table.sql
│   │   ├── 06_orders_table.sql
│   │   ├── 07_order_items_table.sql
│   │   └── 08_inventory_log_table.sql
│   │
│   ├── triggers/                       # Database triggers
│   │   ├── inventory_triggers.sql
│   │   └── order_triggers.sql
│   │
│   ├── procedures/                     # Stored procedures
│   │   ├── order_management.sql
│   │   └── inventory_management.sql
│   │
│   ├── seed/                           # Sample data
│   │   ├── dev_data.sql                # Development data
│   │   └── test_data.sql               # Test data
│   │
│   └── scripts/                        # Database utility scripts
│       ├── setup_dev.sh               # Development setup
│       ├── reset_db.sh                # Reset database (dev only)
│       └── run_all.sh                 # Run all SQL files in order
│
├── frontend/                           # React Frontend
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   │
│   ├── src/
│   │   ├── index.tsx                   # App entry point
│   │   ├── App.tsx
│   │   ├── index.css
│   │   │
│   │   ├── components/                 # Reusable UI components
│   │   │   ├── layout/
│   │   │   │   ├── Header.tsx
│   │   │   │   ├── Navbar.tsx
│   │   │   │   ├── Footer.tsx
│   │   │   │   └── Layout.tsx
│   │   │   │
│   │   │   ├── product/
│   │   │   │   ├── ProductCard.tsx
│   │   │   │   ├── ProductList.tsx
│   │   │   │   └── ProductDetail.tsx
│   │   │   │
│   │   │   ├── cart/
│   │   │   │   ├── CartItem.tsx
│   │   │   │   └── CartSummary.tsx
│   │   │   │
│   │   │   ├── forms/
│   │   │   │   ├── LoginForm.tsx
│   │   │   │   ├── RegisterForm.tsx
│   │   │   │   └── CheckoutForm.tsx
│   │   │   │
│   │   │   ├── common/
│   │   │   │   ├── Loading.tsx
│   │   │   │   ├── ErrorMessage.tsx
│   │   │   │   └── ProtectedRoute.tsx
│   │   │   │
│   │   │   └── admin/
│   │   │       ├── ProductManagement.tsx
│   │   │       └── OrderManagement.tsx
│   │   │
│   │   ├── pages/                      # Page components
│   │   │   ├── Home.tsx
│   │   │   ├── Products.tsx
│   │   │   ├── ProductDetail.tsx
│   │   │   ├── Cart.tsx
│   │   │   ├── Checkout.tsx
│   │   │   ├── Profile.tsx
│   │   │   ├── Login.tsx
│   │   │   ├── Register.tsx
│   │   │   └── admin/
│   │   │       └── AdminDashboard.tsx
│   │   │
│   │   ├── hooks/                      # Custom React hooks
│   │   │   ├── useAuth.ts
│   │   │   ├── useCart.ts
│   │   │   └── useApi.ts
│   │   │
│   │   ├── context/                    # React Context providers
│   │   │   ├── AuthContext.tsx
│   │   │   └── CartContext.tsx
│   │   │
│   │   ├── services/                   # API service layer
│   │   │   ├── api.ts                  # Axios configuration
│   │   │   ├── authService.ts
│   │   │   ├── productService.ts
│   │   │   ├── orderService.ts
│   │   │   └── cartService.ts
│   │   │
│   │   ├── types/                      # TypeScript type definitions
│   │   │   ├── auth.ts
│   │   │   ├── product.ts
│   │   │   ├── order.ts
│   │   │   └── cart.ts
│   │   │
│   │   └── utils/                      # Utility functions
│   │       ├── constants.ts
│   │       ├── helpers.ts
│   │       └── formatters.ts
│   │
│   ├── package.json
│   ├── tsconfig.json
│   └── tailwind.config.js
│
└── docs/                               # Essential documentation only
    ├── API.md                          # API documentation
    ├── DATABASE.md                     # Database schema docs
    └── SETUP.md                        # Development setup guide
```