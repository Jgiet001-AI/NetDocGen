from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager
import time

from app.config import settings
from app.routers import projects, documents, auth, health, analysis, metrics, collaboration
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
    description="""
    ## Network Documentation Generator API
    
    NetDocGen is a comprehensive platform for generating professional network documentation from Visio diagrams.
    
    ### Key Features
    
    * **Visio Parsing**: Extract network topology from .vsdx files
    * **Documentation Generation**: Create HTML, PDF, Word, and Markdown documents
    * **AI Enhancement**: Improve documentation quality with AI-powered content
    * **Collaboration**: Share projects and documents with team members
    * **Project Management**: Organize multiple network diagrams per project
    
    ### Authentication
    
    All endpoints except health checks require JWT authentication. Use the `/api/auth/login` endpoint to obtain access tokens.
    
    ### Rate Limiting
    
    API requests are rate-limited to ensure fair usage:
    - Anonymous: 10 requests per minute
    - Authenticated: 100 requests per minute
    - Document processing: 10 concurrent operations per user
    """,
    version="1.0.0",
    terms_of_service="https://netdocgen.com/terms",
    contact={
        "name": "NetDocGen Support",
        "url": "https://netdocgen.com/support",
        "email": "support@netdocgen.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
    lifespan=lifespan,
    servers=[
        {"url": "http://localhost:8000", "description": "Development server"},
        {"url": "https://api.netdocgen.com", "description": "Production server"}
    ],
    tags_metadata=[
        {
            "name": "auth",
            "description": "Authentication operations",
            "externalDocs": {
                "description": "JWT authentication guide",
                "url": "https://docs.netdocgen.com/auth"
            }
        },
        {
            "name": "projects",
            "description": "Project management operations"
        },
        {
            "name": "documents",
            "description": "Document upload and processing"
        },
        {
            "name": "analysis",
            "description": "AI-powered documentation enhancement"
        },
        {
            "name": "collaboration",
            "description": "Sharing and collaboration features"
        },
        {
            "name": "health",
            "description": "System health and monitoring"
        }
    ]
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
app.include_router(collaboration.router, prefix="/api/collaboration", tags=["collaboration"])
app.include_router(metrics.router, tags=["metrics"])

# Custom API documentation endpoints
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    )

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js",
    )

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