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