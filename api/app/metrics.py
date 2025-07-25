"""
Prometheus metrics for monitoring NetDocGen API
"""

from prometheus_client import Counter, Histogram, Gauge, Info
from prometheus_client import REGISTRY, PROCESS_COLLECTOR, PLATFORM_COLLECTOR, GC_COLLECTOR
import time
from functools import wraps
from typing import Callable
import asyncio

# Remove default collectors to avoid duplicate metrics
REGISTRY.unregister(PROCESS_COLLECTOR)
REGISTRY.unregister(PLATFORM_COLLECTOR)
REGISTRY.unregister(GC_COLLECTOR)

# API Info
api_info = Info(
    'netdocgen_api_info',
    'NetDocGen API information'
)
api_info.info({
    'version': '1.0.0',
    'service': 'api'
})

# Request metrics
http_requests_total = Counter(
    'netdocgen_http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

http_request_duration_seconds = Histogram(
    'netdocgen_http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint']
)

http_requests_in_progress = Gauge(
    'netdocgen_http_requests_in_progress',
    'HTTP requests in progress'
)

# Authentication metrics
auth_attempts_total = Counter(
    'netdocgen_auth_attempts_total',
    'Total authentication attempts',
    ['type', 'status']
)

active_users = Gauge(
    'netdocgen_active_users',
    'Number of active users'
)

# Project metrics
projects_total = Counter(
    'netdocgen_projects_total',
    'Total projects created'
)

projects_by_status = Gauge(
    'netdocgen_projects_by_status',
    'Number of projects by status',
    ['status']
)

# Document metrics
documents_uploaded_total = Counter(
    'netdocgen_documents_uploaded_total',
    'Total documents uploaded',
    ['status']
)

documents_processed_total = Counter(
    'netdocgen_documents_processed_total',
    'Total documents processed',
    ['format', 'status']
)

document_processing_duration_seconds = Histogram(
    'netdocgen_document_processing_duration_seconds',
    'Document processing duration in seconds',
    ['format'],
    buckets=(1, 5, 10, 30, 60, 120, 300, 600)
)

documents_in_queue = Gauge(
    'netdocgen_documents_in_queue',
    'Number of documents waiting to be processed'
)

# Storage metrics
storage_operations_total = Counter(
    'netdocgen_storage_operations_total',
    'Total storage operations',
    ['operation', 'status']
)

storage_bytes_total = Counter(
    'netdocgen_storage_bytes_total',
    'Total bytes stored'
)

# Message queue metrics
mq_messages_published_total = Counter(
    'netdocgen_mq_messages_published_total',
    'Total messages published to queue',
    ['queue', 'status']
)

mq_messages_consumed_total = Counter(
    'netdocgen_mq_messages_consumed_total',
    'Total messages consumed from queue',
    ['queue', 'status']
)

# AI/LLM metrics
llm_requests_total = Counter(
    'netdocgen_llm_requests_total',
    'Total LLM analysis requests',
    ['model', 'status']
)

llm_request_duration_seconds = Histogram(
    'netdocgen_llm_request_duration_seconds',
    'LLM request duration in seconds',
    ['model']
)

# Database metrics
db_connections_active = Gauge(
    'netdocgen_db_connections_active',
    'Active database connections'
)

db_queries_total = Counter(
    'netdocgen_db_queries_total',
    'Total database queries',
    ['operation']
)

db_query_duration_seconds = Histogram(
    'netdocgen_db_query_duration_seconds',
    'Database query duration in seconds',
    ['operation']
)

# Error metrics
errors_total = Counter(
    'netdocgen_errors_total',
    'Total errors',
    ['type', 'operation']
)


def track_request_metrics(method: str, endpoint: str):
    """Decorator to track HTTP request metrics"""
    def decorator(func: Callable):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            http_requests_in_progress.inc()
            start_time = time.time()
            status = "success"
            
            try:
                result = await func(*args, **kwargs)
                return result
            except Exception as e:
                status = "error"
                raise
            finally:
                duration = time.time() - start_time
                http_requests_total.labels(
                    method=method,
                    endpoint=endpoint,
                    status=status
                ).inc()
                http_request_duration_seconds.labels(
                    method=method,
                    endpoint=endpoint
                ).observe(duration)
                http_requests_in_progress.dec()
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            http_requests_in_progress.inc()
            start_time = time.time()
            status = "success"
            
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                status = "error"
                raise
            finally:
                duration = time.time() - start_time
                http_requests_total.labels(
                    method=method,
                    endpoint=endpoint,
                    status=status
                ).inc()
                http_request_duration_seconds.labels(
                    method=method,
                    endpoint=endpoint
                ).observe(duration)
                http_requests_in_progress.dec()
        
        return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
    return decorator


def track_db_operation(operation: str):
    """Decorator to track database operation metrics"""
    def decorator(func: Callable):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.time()
            
            try:
                result = await func(*args, **kwargs)
                db_queries_total.labels(operation=operation).inc()
                return result
            except Exception as e:
                errors_total.labels(type="database", operation=operation).inc()
                raise
            finally:
                duration = time.time() - start_time
                db_query_duration_seconds.labels(operation=operation).observe(duration)
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            start_time = time.time()
            
            try:
                result = func(*args, **kwargs)
                db_queries_total.labels(operation=operation).inc()
                return result
            except Exception as e:
                errors_total.labels(type="database", operation=operation).inc()
                raise
            finally:
                duration = time.time() - start_time
                db_query_duration_seconds.labels(operation=operation).observe(duration)
        
        return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
    return decorator


def track_storage_operation(operation: str):
    """Decorator to track storage operation metrics"""
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                result = await func(*args, **kwargs)
                storage_operations_total.labels(operation=operation, status="success").inc()
                return result
            except Exception as e:
                storage_operations_total.labels(operation=operation, status="error").inc()
                errors_total.labels(type="storage", operation=operation).inc()
                raise
        return wrapper
    return decorator