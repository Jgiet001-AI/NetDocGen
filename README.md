# NetDocGen - Network Documentation Generator

NetDocGen is a comprehensive solution for automatically generating network documentation from Visio diagrams. It parses network diagrams and produces professional documentation in various formats.

## Features

- **Visio Diagram Parsing**: Extract network topology information from Visio files
- **Multi-format Output**: Generate documentation in HTML, PDF, Word, and Markdown
- **RESTful API**: Modern FastAPI backend with async support
- **Microservices Architecture**: Scalable design with separate services for parsing and generation
- **Object Storage**: MinIO integration for file management
- **Message Queue**: RabbitMQ for asynchronous processing
- **Authentication**: JWT-based authentication system
- **Web Interface**: React-based frontend for easy interaction

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Frontend  │────▶│   FastAPI   │────▶│  PostgreSQL │
│   (React)   │     │   Backend   │     │   Database  │
└─────────────┘     └─────────────┘     └─────────────┘
                           │
                    ┌──────┴──────┐
                    │             │
              ┌─────▼─────┐ ┌────▼────┐
              │  Parser   │ │Generator│
              │  Service  │ │ Service │
              └─────┬─────┘ └────┬────┘
                    │            │
              ┌─────▼────────────▼─────┐
              │      RabbitMQ          │
              │    Message Queue       │
              └────────────────────────┘
                           │
                    ┌──────▼──────┐
                    │    MinIO     │
                    │Object Storage│
                    └──────────────┘
```

## Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Node.js 18+ (for frontend development)
- PyCharm Professional (recommended for development)

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd NetDocGen
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start services with Docker Compose**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - API Documentation: http://localhost:8000/docs
   - RabbitMQ Management: http://localhost:15672
   - MinIO Console: http://localhost:9001

## Development Setup

### API Service

```bash
cd api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## Project Structure

```
netdocgen/
├── api/                    # FastAPI backend service
├── parser/                 # Visio parsing service
├── generator/              # Document generation service
├── frontend/               # React frontend
├── shared/                 # Shared libraries
├── docker-compose.yml      # Local development setup
└── README.md
```

## API Endpoints

- `GET /health` - Health check
- `POST /api/auth/token` - Authentication
- `GET /api/projects` - List projects
- `POST /api/projects` - Create project
- `POST /api/documents/upload` - Upload Visio file
- `GET /api/documents/{id}/generate` - Generate documentation

## Testing

Run tests for each service:

```bash
# API tests
cd api
pytest

# Parser tests
cd parser
pytest

# Generator tests
cd generator
pytest
```

## Deployment

For production deployment, use the production Docker Compose configuration:

```bash
docker-compose -f docker-compose.prod.yml up -d
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.