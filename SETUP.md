# NetDocGen Setup Guide

This guide will help you set up and run the complete NetDocGen application with all services including the Phi-3 AI integration.

## Prerequisites

- Docker and Docker Compose
- Node.js 16+ and npm
- Python 3.9+
- At least 8GB RAM (for running Ollama with Phi-3)

## Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd NetDocGen
```

### 2. Environment Setup

```bash
# Copy environment file
cp .env.example .env

# Edit .env with your configuration if needed
# Default values should work for local development
```

### 3. Start Infrastructure Services

```bash
# Start all infrastructure services
docker-compose up -d postgres redis minio rabbitmq ollama

# Wait for services to be ready
sleep 30

# Initialize Ollama with Phi-3 model
chmod +x init-ollama.sh
./init-ollama.sh
```

### 4. Setup Backend Services

#### API Service

```bash
cd api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
alembic upgrade head

# Create admin user
python create_admin.py

# Start API service
uvicorn app.main:app --reload --port 8000
```

#### Parser Service

In a new terminal:

```bash
cd parser

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start parser service
python src/main.py
```

#### Generator Service

In a new terminal:

```bash
cd generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Optional: Install WeasyPrint for PDF generation
# On macOS: brew install weasyprint
# On Ubuntu: sudo apt-get install weasyprint
# On Windows: See https://weasyprint.org/start/

# Start generator service
python src/main.py
```

### 5. Setup Frontend

In a new terminal:

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

The application will be available at http://localhost:3000

### 6. Using Docker (Alternative)

If you prefer to run everything in Docker:

```bash
# Build and start all services
docker-compose up --build

# In another terminal, initialize Ollama
docker exec -it netdocgen-ollama-1 ollama pull phi3
```

## Service URLs

- **Frontend**: http://localhost:3000
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **MinIO Console**: http://localhost:9001 (minioadmin/minioadmin)
- **RabbitMQ Management**: http://localhost:15672 (guest/guest)
- **Ollama API**: http://localhost:11434

## Using the Application

### 1. Login/Register

1. Navigate to http://localhost:3000
2. Click "Create a new account" to register
3. Fill in the registration form
4. Login with your credentials

### 2. Create a Project

1. Click "New Project" or navigate to Projects
2. Enter project name and description
3. Click "Create"

### 3. Upload Visio Diagram

1. Click "Upload Diagram" from dashboard or project page
2. Select your project
3. Drag and drop or select a .vsd/.vsdx/.vsdm file
4. Click "Upload and Process"

### 4. View Generated Documentation

1. Navigate to Documents
2. Click on your processed document
3. Once processing is complete, download in various formats:
   - HTML (Interactive web page)
   - PDF (Printable document)
   - Word (Editable document)
   - Markdown (Plain text)

### 5. AI Analysis (Phi-3 Integration)

1. On the document detail page, click "Analyze with AI"
2. The system will use Phi-3 to provide:
   - Executive summary
   - Architecture analysis
   - Security assessment
   - Optimization recommendations

## Troubleshooting

### Ollama Connection Issues

If the AI analysis fails:

```bash
# Check if Ollama is running
docker ps | grep ollama

# Test Ollama directly
curl http://localhost:11434/api/tags

# Pull Phi-3 model manually
docker exec -it netdocgen-ollama-1 ollama pull phi3
```

### Database Connection Issues

```bash
# Check PostgreSQL is running
docker ps | grep postgres

# Test connection
psql postgresql://postgres:postgres@localhost:5432/netdocgen_dev
```

### Parser Service Issues

If documents stay in "processing" state:

1. Check parser service logs
2. Verify RabbitMQ is accessible
3. Ensure MinIO buckets are created

### Frontend Build Issues

```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
npm start
```

## Development Tips

### Running Tests

```bash
# API tests
cd api && pytest

# Parser tests
cd parser && pytest

# Frontend tests
cd frontend && npm test
```

### Viewing Logs

```bash
# Docker logs
docker-compose logs -f [service-name]

# Python service logs
# Check console output or log files

# Check RabbitMQ messages
# Visit http://localhost:15672
```

### Resetting the System

```bash
# Stop all services
docker-compose down

# Remove volumes (WARNING: Deletes all data)
docker-compose down -v

# Start fresh
docker-compose up -d
```

## Production Deployment

For production deployment:

1. Update `.env` with production values
2. Use proper SSL certificates
3. Configure reverse proxy (nginx)
4. Set up monitoring (Prometheus/Grafana)
5. Enable backups for PostgreSQL and MinIO
6. Use Kubernetes for orchestration

## Support

For issues or questions:
- Check the troubleshooting section
- Review logs for error messages
- Create an issue in the repository