#!/bin/bash

# Database setup script
# Usage: ./setup_dev.sh

echo "Setting up E-Commerce database..."

# Database credentials (change as needed)
DB_USER="root"
DB_PASS="password"
DB_HOST="localhost"

# Run database initialization
echo "Creating database..."
mysql -u $DB_USER -p$DB_PASS -h $DB_HOST < init/01_create_database.sql

# Run schema scripts
echo "Creating tables..."
for file in schema/*.sql; do
    echo "Running $file..."
    mysql -u $DB_USER -p$DB_PASS -h $DB_HOST ecommerce_db < "$file"
done

# Run triggers
echo "Creating triggers..."
for file in triggers/*.sql; do
    echo "Running $file..."
    mysql -u $DB_USER -p$DB_PASS -h $DB_HOST ecommerce_db < "$file"
done

# Run stored procedures
echo "Creating stored procedures..."
for file in procedures/*.sql; do
    echo "Running $file..."
    mysql -u $DB_USER -p$DB_PASS -h $DB_HOST ecommerce_db < "$file"
done

# Insert seed data
echo "Inserting seed data..."
mysql -u $DB_USER -p$DB_PASS -h $DB_HOST ecommerce_db < seed/dev_data.sql

echo "Database setup complete!"
