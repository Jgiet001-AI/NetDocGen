from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import settings
from app.routers import projects, documents, auth, health, analysis
from app.database import engine
from app.models import Base

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