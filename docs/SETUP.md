# E-Commerce Management System - Setup Guide

## Prerequisites
- MySQL 8.0+
- Python 3.10+
- Node.js 18+
- npm or yarn

## Database Setup

1. **Configure database credentials** in `database/scripts/setup_dev.sh`
2. **Run the setup script**:
   ```bash
   cd database/scripts
   chmod +x setup_dev.sh
   ./setup_dev.sh
   ```

This will create the database, tables, triggers, stored procedures, and insert sample data.

## Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Run the server**:
   ```bash
   uvicorn main:app --reload
   ```

API will be available at `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

## Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies** (if not already done):
   ```bash
   npm install
   ```

3. **Run the dev server**:
   ```bash
   npm run dev
   ```

Frontend will be available at `http://localhost:5173` or `http://localhost:5174`

## Default Credentials

- **Admin**: admin@ecommerce.com / password
- **Customer**: john.doe@example.com / password
- **Customer**: jane.smith@example.com / password

## API Testing

Use the Swagger UI at `http://localhost:8000/docs` to test API endpoints.
