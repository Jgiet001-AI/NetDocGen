# Debugging Visio Upload Issues

## Overview
This guide helps troubleshoot issues when uploading Visio files to NetDocGen.

## Common Issues and Solutions

### 1. Nothing Happens After Upload

#### Check Service Status
First, ensure all required services are running:

```bash
docker-compose ps
```

All services should show as "Up":
- postgres
- redis
- minio
- rabbitmq
- api
- parser
- generator
- frontend

#### Check Service Logs

1. **API Service Logs** (for upload errors):
```bash
docker-compose logs -f api
```

2. **Parser Service Logs** (for parsing errors):
```bash
docker-compose logs -f parser
```

3. **RabbitMQ Logs** (for message queue issues):
```bash
docker-compose logs -f rabbitmq
```

4. **MinIO Logs** (for storage issues):
```bash
docker-compose logs -f minio
```

### 2. Check Connectivity

Use the debug endpoint to verify service connectivity:

```bash
# Replace with your actual auth token
curl -H "Authorization: Bearer YOUR_TOKEN" http://localhost:8000/api/documents/debug/connectivity
```

Expected response:
```json
{
  "rabbitmq": {"status": "connected", "error": null},
  "minio": {"status": "connected", "error": null}
}
```

### 3. Manual Status Refresh

If a document appears stuck, try refreshing its status manually:

```bash
# Replace with actual document ID and auth token
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/documents/{document_id}/refresh-status
```

### 4. Common Error Messages

#### "Project not found"
- Verify the project ID is correct
- Ensure you have access to the project

#### "Invalid file type"
- Only .vsd, .vsdx, and .vsdm files are supported
- Check file extension is correct

#### "Upload failed: Connection refused"
- RabbitMQ or MinIO might not be running
- Check docker-compose services

### 5. Debugging Steps

1. **Enable Debug Logging**:
   Add to your `.env` file:
   ```
   LOG_LEVEL=DEBUG
   ```

2. **Monitor All Logs**:
   ```bash
   docker-compose logs -f
   ```

3. **Check RabbitMQ Management UI**:
   - Open http://localhost:15672
   - Login: guest/guest
   - Check queues for messages

4. **Check MinIO Console**:
   - Open http://localhost:9001
   - Login: minioadmin/minioadmin
   - Verify files in "uploads" bucket

### 6. Reset Services

If issues persist, try restarting services:

```bash
# Restart all services
docker-compose restart

# Or restart specific services
docker-compose restart api parser rabbitmq minio
```

### 7. Database Issues

Check document status in database:

```bash
# Connect to database
docker-compose exec postgres psql -U postgres -d netdocgen_dev

# Check recent documents
SELECT id, filename, status, error_message, created_at 
FROM documents 
ORDER BY created_at DESC 
LIMIT 10;
```

### 8. File Size Limits

Default limits:
- Nginx: 100MB
- FastAPI: No limit by default
- MinIO: No limit

If uploading large files fails, check:
1. Frontend upload timeout
2. API request timeout
3. Available disk space

### 9. Network Issues

If running services on different machines:
1. Update service URLs in docker-compose.yml
2. Ensure ports are accessible
3. Check firewall rules

## Getting Help

When reporting issues, include:
1. Error messages from logs
2. File size and type
3. Browser console errors
4. Result of connectivity check
5. Docker service status