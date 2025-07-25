from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import time

from app.config import settings
from app.routers import projects, documents, auth, health, analysis, metrics
from app.database import engine
from app.models import Base
from app.metrics import (
    http_requests_in_progress,
    http_requests_total,
    http_request_duration_seconds
)

from app.services import storage_service, mq_service
import asyncio
import logging

# Configure logging
log_level = settings.LOG_LEVEL if hasattr(settings, 'LOG_LEVEL') else 'INFO'
logging.basicConfig(
    level=getattr(logging, log_level.upper(), logging.INFO),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Set specific loggers to DEBUG for troubleshooting
logging.getLogger('app.services.document').setLevel(logging.DEBUG)
logging.getLogger('app.services.message_queue').setLevel(logging.DEBUG)
logging.getLogger('app.services.storage').setLevel(logging.DEBUG)
logging.getLogger('app.routers.documents').setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting application lifespan...")
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Initialize services
    logger.info("Initializing storage service...")
    await storage_service.initialize()
    
    logger.info("Connecting to message queue...")
    await mq_service.connect()
    
    # Set up completion handlers
    logger.info("Setting up message queue completion handlers...")
    await mq_service.setup_completion_handlers()
    
    logger.info("Application startup complete")
    yield
    
    # Shutdown
    logger.info("Shutting down application...")
    await mq_service.disconnect()
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
app.include_router(analysis.router, prefix="/api/analysis", tags=["analysis"])
app.include_router(metrics.router, tags=["metrics"])


# Metrics middleware
@app.middleware("http")
async def track_requests(request: Request, call_next):
    """Track all HTTP requests for metrics"""
    # Skip metrics endpoint to avoid recursion
    if request.url.path == "/metrics":
        return await call_next(request)
    
    http_requests_in_progress.inc()
    start_time = time.time()
    
    try:
        response = await call_next(request)
        status = "success" if response.status_code < 400 else "error"
        
        # Track metrics
        http_requests_total.labels(
            method=request.method,
            endpoint=request.url.path,
            status=status
        ).inc()
        
        duration = time.time() - start_time
        http_request_duration_seconds.labels(
            method=request.method,
            endpoint=request.url.path
        ).observe(duration)
        
        return response
    except Exception as e:
        http_requests_total.labels(
            method=request.method,
            endpoint=request.url.path,
            status="error"
        ).inc()
        raise
    finally:
        http_requests_in_progress.dec()