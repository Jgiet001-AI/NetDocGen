# NetDocGen Troubleshooting Guide

## Table of Contents
1. [Installation Issues](#installation-issues)
2. [Visio Parsing Errors](#visio-parsing-errors)
3. [Document Generation Problems](#document-generation-problems)
4. [Performance Issues](#performance-issues)
5. [API Errors](#api-errors)
6. [Frontend Issues](#frontend-issues)
7. [Database Problems](#database-problems)
8. [Docker/Kubernetes Issues](#dockerkubernetes-issues)
9. [Integration Problems](#integration-problems)
10. [Common Error Codes](#common-error-codes)

## Installation Issues

### Issue: Docker build fails with dependency errors
**Symptoms:**
```
ERROR: Could not find a version that satisfies the requirement...
```

**Solution:**
1. Clear Docker cache: `docker system prune -a`
2. Update base images in Dockerfile
3. Check for conflicting dependencies in requirements.txt
4. Use specific version pins for problematic packages

### Issue: Port conflicts during local development
**Symptoms:**
```
Error: bind: address already in use
```

**Solution:**
1. Check ports using: `netstat -tlnp | grep <port>`
2. Update docker-compose.yml with alternative ports
3. Kill conflicting processes: `kill -9 <PID>`
4. Use environment variables for port configuration

## Visio Parsing Errors

### Issue: Unsupported Visio format
**Symptoms:**
```
ParseError: Unable to read Visio file format
```

**Solution:**
1. Verify file extension (.vsdx, .vsd, .vsdm)
2. Check file isn't corrupted: `file <filename>`
3. Convert legacy formats using Visio application
4. Update parser library to latest version

### Issue: Missing network shapes in parsed output
**Symptoms:**
- Devices appear as generic shapes
- Missing device properties

**Solution:**
```python
# Add custom shape mapping
SHAPE_MAPPING = {
    'Router': ['router', 'rtr', 'gw'],
    'Switch': ['switch', 'sw', 'bridge'],
    'Firewall': ['firewall', 'fw', 'asa']
}

# Update parser configuration
parser_config = {
    'custom_shapes': True,
    'shape_mapping': SHAPE_MAPPING,
    'extract_all_properties': True
}
```

### Issue: Connection mapping failures
**Symptoms:**
- Missing network links
- Incorrect connection endpoints

**Solution:**
1. Enable verbose logging in parser
2. Check for grouped shapes or containers
3. Verify connection points in Visio
4. Use connection healing algorithm:

```python
def heal_connections(shapes, connections):
    for conn in connections:
        if not conn.has_valid_endpoints():
            nearest_shapes = find_nearest_shapes(conn)
            conn.reconnect(nearest_shapes)
    return connections
```

## Document Generation Problems

### Issue: PDF generation memory errors
**Symptoms:**
```
MemoryError: Unable to allocate memory for PDF generation
```

**Solution:**
1. Increase container memory limits:
```yaml
services:
  doc-generator:
    mem_limit: 4g
    memswap_limit: 4g
```

2. Enable streaming PDF generation:
```python
def generate_pdf_streaming(content):
    with tempfile.NamedTemporaryFile() as tmp:
        for chunk in content.chunks():
            tmp.write(process_chunk(chunk))
        return create_pdf(tmp)
```

### Issue: Missing fonts in generated PDFs
**Symptoms:**
- Text appears as boxes or missing
- Font substitution warnings

**Solution:**
1. Install required fonts in Docker image:
```dockerfile
RUN apt-get update && apt-get install -y \
    fonts-liberation \
    fonts-dejavu-core \
    fontconfig
```

2. Configure font paths:
```python
FONT_CONFIG = {
    'paths': ['/usr/share/fonts', '/app/fonts'],
    'default_font': 'DejaVu Sans'
}
```

## Performance Issues

### Issue: Slow diagram processing
**Symptoms:**
- Processing takes >10 minutes
- High CPU usage

**Solution:**
1. Enable parallel processing:
```python
from multiprocessing import Pool

def process_diagram_parallel(diagram):
    with Pool(processes=4) as pool:
        shapes = pool.map(parse_shape, diagram.shapes)
    return shapes
```

2. Implement caching:
```python
@lru_cache(maxsize=1000)
def parse_shape_cached(shape_id):
    return parse_shape(shape_id)
```

3. Optimize database queries:
```sql
-- Add indexes
CREATE INDEX idx_project_status ON projects(status);
CREATE INDEX idx_document_created ON documents(created_at);
```

### Issue: Frontend loading slowly
**Symptoms:**
- Long white screen on load
- Slow API responses

**Solution:**
1. Enable compression:
```nginx
gzip on;
gzip_types text/plain application/json application/javascript;
```

2. Implement lazy loading:
```javascript
const Dashboard = lazy(() => import('./components/Dashboard'));
```

3. Add Redis caching:
```python
@cache.memoize(timeout=300)
def get_project_list(user_id):
    return Project.query.filter_by(user_id=user_id).all()
```

## API Errors

### Issue: 401 Unauthorized errors
**Symptoms:**
```json
{"error": "Invalid or expired token"}
```

**Solution:**
1. Check token expiration settings
2. Verify JWT secret configuration
3. Implement token refresh:
```python
@app.post("/auth/refresh")
async def refresh_token(refresh_token: str):
    if verify_refresh_token(refresh_token):
        return {"access_token": create_access_token()}
    raise HTTPException(401)
```

### Issue: Rate limiting errors
**Symptoms:**
```json
{"error": "Rate limit exceeded", "retry_after": 60}
```

**Solution:**
1. Adjust rate limits for different user tiers
2. Implement exponential backoff:
```javascript
async function apiCallWithRetry(url, options, maxRetries = 3) {
    for (let i = 0; i < maxRetries; i++) {
        try {
            return await fetch(url, options);
        } catch (error) {
            if (error.status === 429) {
                await sleep(Math.pow(2, i) * 1000);
                continue;
            }
            throw error;
        }
    }
}
```

## Frontend Issues

### Issue: File upload failures
**Symptoms:**
- Upload progress stuck
- "Failed to upload" errors

**Solution:**
1. Increase upload limits:
```nginx
client_max_body_size 100M;
```

2. Implement chunked uploads:
```javascript
async function uploadChunked(file, chunkSize = 1024 * 1024) {
    const chunks = Math.ceil(file.size / chunkSize);
    for (let i = 0; i < chunks; i++) {
        const chunk = file.slice(i * chunkSize, (i + 1) * chunkSize);
        await uploadChunk(chunk, i, chunks);
    }
}
```

### Issue: State management inconsistencies
**Symptoms:**
- UI not updating after actions
- Stale data displayed

**Solution:**
1. Check Redux actions and reducers
2. Implement proper state normalization
3. Use RTK Query for API state:
```javascript
const apiSlice = createApi({
    reducerPath: 'api',
    baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
    tagTypes: ['Project', 'Document'],
    endpoints: (builder) => ({
        getProjects: builder.query({
            query: () => 'projects',
            providesTags: ['Project']
        })
    })
});
```

## Database Problems

### Issue: Connection pool exhausted
**Symptoms:**
```
psycopg2.OperationalError: FATAL: remaining connection slots are reserved
```

**Solution:**
1. Adjust pool settings:
```python
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_size': 20,
    'max_overflow': 40,
    'pool_pre_ping': True,
    'pool_recycle': 300
}
```

2. Implement connection cleanup:
```python
@app.teardown_appcontext
def cleanup_connections(error):
    db.session.remove()
```

### Issue: Migration failures
**Symptoms:**
- Alembic migration errors
- Schema inconsistencies

**Solution:**
1. Check migration dependencies
2. Create manual migration for complex changes:
```python
def upgrade():
    # Handle existing data
    op.execute("UPDATE projects SET status='active' WHERE status IS NULL")
    # Then add constraint
    op.alter_column('projects', 'status', nullable=False)
```

## Docker/Kubernetes Issues

### Issue: Pod crash loops
**Symptoms:**
```
CrashLoopBackOff 5 (2m ago) 10m
```

**Solution:**
1. Check logs: `kubectl logs <pod-name> --previous`
2. Verify resource limits
3. Add health checks:
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10
```

### Issue: Service discovery failures
**Symptoms:**
- Services can't communicate
- DNS resolution errors

**Solution:**
1. Verify service names and ports
2. Check network policies
3. Use proper service URLs:
```python
SERVICES = {
    'parser': 'http://parser-service:8081',
    'generator': 'http://generator-service:8082'
}
```

## Integration Problems

### Issue: S3/MinIO upload failures
**Symptoms:**
```
botocore.exceptions.NoCredentialsError
```

**Solution:**
1. Verify credentials configuration
2. Check bucket permissions
3. Implement retry logic:
```python
@retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000)
def upload_to_s3(file_path, bucket, key):
    s3_client.upload_file(file_path, bucket, key)
```

## Common Error Codes

| Code | Description | Solution |
|------|-------------|----------|
| E001 | Invalid Visio file | Check file format and corruption |
| E002 | Parser timeout | Reduce diagram complexity or increase timeout |
| E003 | Template not found | Verify template exists in system |
| E004 | Insufficient permissions | Check user roles and permissions |
| E005 | Database connection failed | Verify database credentials and connectivity |
| E006 | Memory limit exceeded | Increase container resources |
| E007 | API rate limit | Implement backoff or upgrade tier |
| E008 | Invalid configuration | Check environment variables |
| E009 | Storage quota exceeded | Clean up old files or increase quota |
| E010 | Network timeout | Check network connectivity and firewall rules |

## Debug Mode

Enable debug mode for detailed logging:

```bash
# Environment variable
export NETDOCGEN_DEBUG=true

# Or in docker-compose
environment:
  - NETDOCGEN_DEBUG=true
  - LOG_LEVEL=DEBUG
```

Debug endpoints:
- `/api/debug/health` - System health check
- `/api/debug/config` - View configuration (auth required)
- `/api/debug/metrics` - Performance metrics

## Getting Help

1. Check logs: `docker logs <container-name>`
2. Enable verbose logging
3. Search GitHub issues
4. Join community Slack channel
5. Submit bug report with:
   - Error messages
   - Steps to reproduce
   - Environment details
   - Sample files (sanitized)