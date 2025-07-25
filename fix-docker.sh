#!/bin/bash

echo "🔧 Fixing Docker issues..."

# Stop and rebuild the API container
echo "📦 Rebuilding API container with updated dependencies..."
docker-compose stop api
docker-compose build --no-cache api

# Start the API service again
echo "🚀 Starting API service..."
docker-compose up -d api

# Wait for it to be ready
sleep 10

# Run migrations again
echo "🗄️  Running database migrations..."
docker-compose exec -T api alembic upgrade head || echo "Migrations may have already been applied"

echo "✅ Fix complete! The API should now be working."
echo ""
echo "📋 To check API status:"
echo "   docker-compose logs api"
echo ""
echo "🌐 API should be available at: http://localhost:8000/docs"