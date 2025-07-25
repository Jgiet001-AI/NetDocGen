#!/bin/bash

echo "🚀 Starting NetDocGen with Docker Compose..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "📋 Creating .env file from .env.example..."
    cp .env.example .env
fi

# Start infrastructure services first
echo "🏗️  Starting infrastructure services..."
docker-compose up -d postgres redis minio rabbitmq ollama

# Wait for services to be ready
echo "⏳ Waiting for services to be ready..."
sleep 30

# Initialize Ollama with Phi-3
echo "🤖 Initializing Ollama with Phi-3 model..."
docker-compose exec -T ollama ollama pull phi3 || echo "Note: Phi-3 will be pulled on first use"

# Start application services
echo "🎯 Starting application services..."
docker-compose up -d api parser generator

# Wait a bit for API to be ready
sleep 10

# Run database migrations
echo "🗄️  Running database migrations..."
docker-compose exec -T api alembic upgrade head

# Start frontend
echo "🎨 Starting frontend..."
docker-compose up -d frontend

echo "✅ NetDocGen is starting up!"
echo ""
echo "📍 Service URLs:"
echo "   Frontend:      http://localhost:3000"
echo "   API:           http://localhost:8000"
echo "   API Docs:      http://localhost:8000/docs"
echo "   MinIO Console: http://localhost:9001 (minioadmin/minioadmin)"
echo "   RabbitMQ:      http://localhost:15672 (guest/guest)"
echo ""
echo "📋 Next steps:"
echo "   1. Wait for all services to fully start (check docker-compose logs -f)"
echo "   2. Create an admin user: docker-compose exec api python create_admin.py"
echo "   3. Open http://localhost:3000 in your browser"
echo ""
echo "🛑 To stop: docker-compose down"
echo "📊 To view logs: docker-compose logs -f [service-name]"