# PyCharm Setup Guide for NetDocGen

## Table of Contents
1. [Project Structure](#project-structure)
2. [Initial PyCharm Setup](#initial-pycharm-setup)
3. [Python Environment Configuration](#python-environment-configuration)
4. [Docker Integration](#docker-integration)
5. [Database Tools Setup](#database-tools-setup)
6. [Run/Debug Configurations](#rundebug-configurations)
7. [Remote Development](#remote-development)
8. [Testing Configuration](#testing-configuration)
9. [Git Integration](#git-integration)
10. [Productivity Tips](#productivity-tips)

## Project Structure

First, create the proper directory structure for your project:

```
netdocgen/
├── .idea/                    # PyCharm configuration (auto-generated)
├── api/                      # FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI app entry point
│   │   ├── config.py        # Configuration management
│   │   ├── models/          # Database models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── routers/         # API endpoints
│   │   ├── services/        # Business logic
│   │   ├── utils/           # Utility functions
│   │   └── dependencies.py  # Dependency injection
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── parser/                   # Visio parser service
│   ├── src/
│   │   ├── parser.py
│   │   ├── shapes.py
│   │   └── utils.py
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── generator/               # Document generator service
│   ├── src/
│   │   ├── generator.py
│   │   ├── templates/
│   │   └── utils.py
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/                # React frontend
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
├── shared/                  # Shared libraries
│   ├── database/
│   ├── messaging/
│   └── storage/
├── docker-compose.yml       # Local development
├── docker-compose.prod.yml  # Production config
├── .env.example            # Environment template
├── .gitignore
├── README.md
└── pyproject.toml          # Python project config
```

## Initial PyCharm Setup

### 1. Create New Project

1. Open PyCharm Professional (recommended for Docker support)
2. File → New Project
3. Location: `/path/to/netdocgen`
4. Create a Git repository: ✓
5. Python Interpreter: Create new environment using Virtualenv

### 2. Configure Project Structure

```python
# File → Settings → Project Structure

# Mark directories:
- api/app → Mark as "Sources Root"
- parser/src → Mark as "Sources Root"
- generator/src → Mark as "Sources Root"
- shared → Mark as "Sources Root"
- */tests → Mark as "Test Sources Root"
```

### 3. Create Initial Files

Create `.gitignore`:
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv

# IDE
.idea/
.vscode/
*.swp
*.swo

# Environment
.env
.env.local
.env.*.local

# Docker
*.log
docker-compose.override.yml

# OS
.DS_Store
Thumbs.db

# Project specific
/data/
/logs/
/temp/
```

Create `pyproject.toml`:
```toml
[tool.poetry]
name = "netdocgen"
version = "0.1.0"
description = "Network Documentation Generator"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.11"

[tool.black]
line-length = 100
target-version = ['py311']

[tool.isort]
profile = "black"
line_length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
addopts = "-v --cov=app --cov-report=html"

[tool.mypy]
python_version = "3.11"
ignore_missing_imports = true
```

## Python Environment Configuration

### 1. Create Virtual Environments for Each Service

API Service:
```bash
cd api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
```

Create `api/requirements.txt`:
```txt
# Core
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-dotenv==1.0.0
pydantic==2.5.0
pydantic-settings==2.1.0

# Database
sqlalchemy==2.0.23
alembic==1.12.1
asyncpg==0.29.0
psycopg2-binary==2.9.9

# Redis
redis==5.0.1
aioredis==2.0.1

# Storage
minio==7.2.0
boto3==1.29.7

# Message Queue
aio-pika==9.3.0
celery==5.3.4

# Auth
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6

# Utils
httpx==0.25.2
python-dateutil==2.8.2
pytz==2023.3

# Development
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
black==23.11.0
isort==5.12.0
flake8==6.1.0
mypy==1.7.1
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Configure PyCharm Interpreters

1. File → Settings → Project → Python Interpreter
2. Click gear icon → Add
3. Existing Environment → Select `api/venv/bin/python`
4. Repeat for parser and generator services

### 3. Create FastAPI Application Structure

Create `api/app/main.py`:
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import settings
from app.routers import projects, documents, auth, health
from app.database import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown
    await engine.dispose()

app = FastAPI(
    title="NetDocGen API",
    description="Network Documentation Generator API",
    version="1.0.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, tags=["health"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(projects.router, prefix="/api/projects", tags=["projects"])
app.include_router(documents.router, prefix="/api/documents", tags=["documents"])
```

Create `api/app/config.py`:
```python
from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # Application
    APP_NAME: str = "NetDocGen"
    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str
    
    # Redis
    REDIS_URL: str
    
    # MinIO
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_SECURE: bool = False
    
    # RabbitMQ
    RABBITMQ_URL: str
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
```

## Docker Integration

### 1. Docker Support in PyCharm

Enable Docker support:
1. File → Settings → Build, Execution, Deployment → Docker
2. Add Docker configuration (usually Docker for Desktop)
3. Test connection

### 2. Create Docker Configurations

Create `api/Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app ./app

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

### 3. Docker Compose for Development

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: netdocgen_dev
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  minio:
    image: minio/minio
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - minio_data:/data

  rabbitmq:
    image: rabbitmq:3-management
    environment:
      RABBITMQ_DEFAULT_USER: guest
      RABBITMQ_DEFAULT_PASS: guest
    ports:
      - "5672:5672"
      - "15672:15672"

  api:
    build:
      context: ./api
      dockerfile: Dockerfile
    volumes:
      - ./api:/app
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://postgres:postgres@postgres:5432/netdocgen_dev
      REDIS_URL: redis://redis:6379
      MINIO_ENDPOINT: minio:9000
      MINIO_ACCESS_KEY: minioadmin
      MINIO_SECRET_KEY: minioadmin
      RABBITMQ_URL: amqp://guest:guest@rabbitmq:5672
      SECRET_KEY: dev-secret-key
    depends_on:
      - postgres
      - redis
      - minio
      - rabbitmq

volumes:
  postgres_data:
  minio_data:
```

### 4. PyCharm Docker Compose Integration

1. Right-click `docker-compose.yml`
2. Create 'docker-compose' Run Configuration
3. Services: Select all or specific services
4. Click Run to start services

## Database Tools Setup

### 1. Configure Database Connection

1. View → Tool Windows → Database
2. Click + → Data Source → PostgreSQL
3. Configuration:
   - Host: localhost
   - Port: 5432
   - Database: netdocgen_dev
   - User: postgres
   - Password: postgres
4. Test Connection → OK

### 2. Create Database Migrations

Create `api/alembic.ini`:
```ini
[alembic]
script_location = alembic
prepend_sys_path = .
sqlalchemy.url = postgresql://postgres:postgres@localhost:5432/netdocgen_dev

[loggers]
keys = root,sqlalchemy,alembic
```

Initialize Alembic:
```bash
cd api
alembic init alembic
```

## Run/Debug Configurations

### 1. FastAPI Development Server

Create Run Configuration:
1. Run → Edit Configurations → +Python
2. Name: "API Development Server"
3. Script path: `-m uvicorn`
4. Parameters: `app.main:app --reload --host 0.0.0.0 --port 8000`
5. Working directory: `$PROJECT_DIR$/api`
6. Environment variables: Load from .env file

### 2. Celery Worker

Create Run Configuration:
1. Run → Edit Configurations → +Python
2. Name: "Celery Worker"
3. Script path: `-m celery`
4. Parameters: `-A app.worker worker --loglevel=info`
5. Working directory: `$PROJECT_DIR$/api`

### 3. Debug Configuration

For debugging with breakpoints:
1. Create Python Debug configuration
2. Script path: `api/debug.py`

Create `api/debug.py`:
```python
import uvicorn
from app.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
```

## Remote Development

### 1. Connect to Azure VM

1. File → Settings → Build, Execution, Deployment → Deployment
2. Add new SFTP connection:
   - Host: Your Azure VM IP
   - Username: azureuser
   - Auth type: Key pair
   - Private key: `~/.ssh/netdocgen_key`

### 2. Remote Interpreter

1. File → Settings → Project → Python Interpreter
2. Add → SSH Interpreter
3. Configure SSH connection to Azure VM
4. Interpreter path: `/opt/netdocgen/venv/bin/python`

### 3. Sync Files

1. Tools → Deployment → Configuration
2. Mappings: Local path → `/opt/netdocgen`
3. Enable automatic upload

## Testing Configuration

### 1. Create Test Structure

Create `api/tests/conftest.py`:
```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db

# Test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
```

### 2. Configure pytest in PyCharm

1. File → Settings → Tools → Python Integrated Tools
2. Default test runner: pytest
3. Add pytest options: `-v --cov=app`

### 3. Create Test Run Configuration

1. Run → Edit Configurations → + → pytest
2. Target: `api/tests`
3. Additional arguments: `--cov=app --cov-report=html`

## Git Integration

### 1. Initialize Repository

```bash
git init
git add .
git commit -m "Initial commit"
```

### 2. Configure Git in PyCharm

1. VCS → Enable Version Control Integration → Git
2. Configure .gitignore (already created above)
3. Set up remote: VCS → Git → Remotes

### 3. Pre-commit Hooks

Create `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.11.0
    hooks:
      - id: black
        language_version: python3.11

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        args: ['--max-line-length=100']

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

Install pre-commit:
```bash
pip install pre-commit
pre-commit install
```

## Productivity Tips

### 1. PyCharm Shortcuts

Essential shortcuts:
- `Ctrl+Shift+F10`: Run current file
- `Shift+F9`: Debug
- `Ctrl+Shift+F`: Find in project
- `Ctrl+Alt+L`: Reformat code
- `Ctrl+Alt+O`: Optimize imports
- `Alt+Enter`: Show intention actions
- `Ctrl+B`: Go to declaration
- `Ctrl+Shift+A`: Find action

### 2. Live Templates

Create custom templates:
1. File → Settings → Editor → Live Templates
2. Add new template group: "NetDocGen"
3. Add templates:

FastAPI Endpoint:
```python
@router.$METHOD$("/$PATH$")
async def $FUNCTION_NAME$($PARAMS$):
    """$DESCRIPTION$"""
    return {"message": "$MESSAGE$"}
```

### 3. File Watchers

Auto-format on save:
1. File → Settings → Tools → File Watchers
2. Add → Custom
3. Name: Black Formatter
4. File type: Python
5. Program: `$PyInterpreterDirectory$/black`
6. Arguments: `$FilePath$`

### 4. Database Tools

SQL scratch files:
1. Right-click database → New → Query Console
2. Write and test SQL queries
3. Generate code from queries

### 5. HTTP Client

Test API endpoints:
1. Create `api/http-requests/test.http`:
```http
### Health Check
GET http://localhost:8000/health

### Login
POST http://localhost:8000/api/auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "password"
}

### Create Project
POST http://localhost:8000/api/projects
Authorization: Bearer {{auth_token}}
Content-Type: application/json

{
  "name": "Test Project",
  "description": "Test Description"
}
```

### 6. Environment Variables

Create `.env` file in project root:
```env
# Development Environment
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/netdocgen_dev
REDIS_URL=redis://localhost:6379
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
RABBITMQ_URL=amqp://guest:guest@localhost:5672
SECRET_KEY=dev-secret-key-change-in-production
DEBUG=True
```

### 7. Code Style Configuration

Configure PyCharm to match project style:
1. File → Settings → Editor → Code Style → Python
2. Set line length: 100
3. Enable: "Add trailing comma in multiline"
4. Configure imports: One import per line

## Debugging Tips

### 1. Remote Debugging

For debugging code running in Docker:

1. Add to Dockerfile:
```dockerfile
RUN pip install debugpy
```

2. Add debug configuration:
```python
import debugpy
debugpy.listen(("0.0.0.0", 5678))
debugpy.wait_for_client()  # Optional: wait for debugger
```

3. Create Remote Debug configuration in PyCharm

### 2. Logging Configuration

Create `api/app/logging_config.py`:
```python
import logging
import sys

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("app.log")
        ]
    )
    
    # Set specific loggers
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
```

## Next Steps

1. **Set up CI/CD**: Configure GitHub Actions or Azure DevOps
2. **Add monitoring**: Integrate with Application Insights
3. **Create documentation**: Use Sphinx for API docs
4. **Performance profiling**: Use PyCharm profiler
5. **Security scanning**: Integrate Bandit and Safety