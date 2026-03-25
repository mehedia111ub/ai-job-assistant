echo "Creating project structure..."

# Backend structure
mkdir -p backend/app/api
mkdir -p backend/app/core
mkdir -p backend/app/models
mkdir -p backend/app/schemas
mkdir -p backend/app/services
mkdir -p backend/app/db

# Frontend structure
mkdir -p frontend

# Create files
touch backend/app/main.py
touch backend/requirements.txt
touch frontend/app.py
touch README.md

echo "Project structure created successfully!"