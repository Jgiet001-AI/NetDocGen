# NetDocGen API Reference

## Overview

The NetDocGen API provides programmatic access to network documentation generation features. This RESTful API allows you to upload Visio diagrams, generate documentation in multiple formats, and manage projects.

## Base URL

```
Development: http://localhost:8000
Production: https://api.netdocgen.com
```

## Authentication

All API endpoints except health checks require JWT authentication.

### Obtaining Access Token

```bash
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "your-password"
}
```

Response:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "full_name": "John Doe"
  }
}
```

### Using the Token

Include the access token in the Authorization header:
```
Authorization: Bearer <access_token>
```

## API Endpoints

### Authentication

#### Register User
```http
POST /api/auth/register
```

Request body:
```json
{
  "email": "user@example.com",
  "password": "secure-password",
  "full_name": "John Doe"
}
```

#### Login
```http
POST /api/auth/login
```

#### Refresh Token
```http
POST /api/auth/refresh
```

Request body:
```json
{
  "refresh_token": "your-refresh-token"
}
```

### Projects

#### List Projects
```http
GET /api/projects
```

Query parameters:
- `skip`: Number of records to skip (default: 0)
- `limit`: Maximum records to return (default: 100)

Response:
```json
[
  {
    "id": "uuid",
    "name": "Network Upgrade 2024",
    "description": "Main office network upgrade",
    "created_at": "2024-01-25T10:00:00Z",
    "updated_at": "2024-01-25T10:00:00Z",
    "document_count": 5
  }
]
```

#### Create Project
```http
POST /api/projects
```

Request body:
```json
{
  "name": "Network Upgrade 2024",
  "description": "Main office network upgrade"
}
```

#### Get Project
```http
GET /api/projects/{project_id}
```

#### Update Project
```http
PUT /api/projects/{project_id}
```

#### Delete Project
```http
DELETE /api/projects/{project_id}
```

### Documents

#### Upload Document
```http
POST /api/documents/upload
```

Multipart form data:
- `file`: Visio file (.vsdx)
- `project_id`: UUID of the project

Response:
```json
{
  "id": "uuid",
  "filename": "network-diagram.vsdx",
  "status": "uploaded",
  "project_id": "uuid",
  "uploaded_at": "2024-01-25T10:00:00Z"
}
```

#### Get Document Status
```http
GET /api/documents/{document_id}
```

Response:
```json
{
  "id": "uuid",
  "filename": "network-diagram.vsdx",
  "status": "completed",
  "shape_count": 45,
  "connection_count": 67,
  "parsed_at": "2024-01-25T10:05:00Z",
  "completed_at": "2024-01-25T10:06:00Z"
}
```

#### Generate Documentation
```http
POST /api/documents/{document_id}/generate
```

Request body:
```json
{
  "format": "pdf",
  "options": {
    "include_ai_enhancements": true,
    "template": "professional"
  }
}
```

Supported formats:
- `html`
- `pdf`
- `docx`
- `markdown`

#### Download Generated Document
```http
GET /api/documents/{document_id}/download?format=pdf
```

#### Delete Document
```http
DELETE /api/documents/{document_id}
```

### AI Enhancement

#### Enhance Documentation
```http
POST /api/analysis/documents/{document_id}/enhance
```

Response:
```json
{
  "document_id": "uuid",
  "enhancements": {
    "executive_summary": "This network infrastructure...",
    "glossary": [
      {
        "term": "VLAN",
        "definition": "Virtual Local Area Network..."
      }
    ],
    "enhanced_devices": [...],
    "suggested_sections": [...]
  }
}
```

#### Generate Executive Summary
```http
POST /api/analysis/documents/{document_id}/enhance/summary
```

#### Generate Glossary
```http
POST /api/analysis/documents/{document_id}/enhance/glossary
```

### Collaboration

#### Create Share Link
```http
POST /api/collaboration/share
```

Request body:
```json
{
  "project_id": "uuid",
  "permission": "view",
  "expires_at": "2024-02-01T00:00:00Z",
  "max_uses": 10,
  "password": "optional-password"
}
```

Response:
```json
{
  "id": "uuid",
  "token": "secure-token",
  "share_url": "https://app.netdocgen.com/share/secure-token",
  "permission": "view",
  "expires_at": "2024-02-01T00:00:00Z"
}
```

#### Access Shared Resource
```http
GET /api/collaboration/share/{token}?password=optional
```

#### Create Comment
```http
POST /api/collaboration/comments
```

Request body:
```json
{
  "content": "Great documentation!",
  "project_id": "uuid",
  "parent_id": null
}
```

#### List Comments
```http
GET /api/collaboration/comments?project_id=uuid
```

#### Get Activity Log
```http
GET /api/collaboration/activities?project_id=uuid&limit=50
```

### Health & Monitoring

#### Health Check
```http
GET /health
```

Response:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "services": {
    "database": "healthy",
    "redis": "healthy",
    "minio": "healthy",
    "rabbitmq": "healthy"
  }
}
```

#### Prometheus Metrics
```http
GET /metrics
```

## Error Responses

All error responses follow this format:
```json
{
  "detail": "Error message describing what went wrong"
}
```

Common HTTP status codes:
- `400`: Bad Request - Invalid request data
- `401`: Unauthorized - Missing or invalid authentication
- `403`: Forbidden - Insufficient permissions
- `404`: Not Found - Resource doesn't exist
- `422`: Unprocessable Entity - Validation error
- `500`: Internal Server Error - Server-side error

## Rate Limiting

API requests are rate-limited:
- Anonymous: 10 requests per minute
- Authenticated: 100 requests per minute
- Document processing: 10 concurrent operations per user

Rate limit headers:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1706180460
```

## Webhooks

Configure webhooks to receive notifications:

```http
POST /api/webhooks
```

Request body:
```json
{
  "url": "https://your-server.com/webhook",
  "events": ["document.completed", "document.failed"],
  "secret": "webhook-secret"
}
```

Webhook payload:
```json
{
  "event": "document.completed",
  "timestamp": "2024-01-25T10:06:00Z",
  "data": {
    "document_id": "uuid",
    "project_id": "uuid",
    "status": "completed"
  }
}
```

## Code Examples

### Python
```python
import requests

# Login
response = requests.post(
    "http://localhost:8000/api/auth/login",
    json={"email": "user@example.com", "password": "password"}
)
tokens = response.json()

# Upload document
headers = {"Authorization": f"Bearer {tokens['access_token']}"}
files = {"file": open("network.vsdx", "rb")}
data = {"project_id": "project-uuid"}

response = requests.post(
    "http://localhost:8000/api/documents/upload",
    headers=headers,
    files=files,
    data=data
)
document = response.json()
```

### JavaScript
```javascript
// Login
const loginResponse = await fetch('http://localhost:8000/api/auth/login', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'password'
  })
});
const tokens = await loginResponse.json();

// Upload document
const formData = new FormData();
formData.append('file', fileInput.files[0]);
formData.append('project_id', 'project-uuid');

const uploadResponse = await fetch('http://localhost:8000/api/documents/upload', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${tokens.access_token}`
  },
  body: formData
});
```

### cURL
```bash
# Login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password"}'

# Upload document
curl -X POST http://localhost:8000/api/documents/upload \
  -H "Authorization: Bearer <access_token>" \
  -F "file=@network.vsdx" \
  -F "project_id=project-uuid"
```

## SDK Support

Official SDKs are available for:
- Python: `pip install netdocgen`
- JavaScript/TypeScript: `npm install @netdocgen/sdk`
- Go: `go get github.com/netdocgen/go-sdk`

## API Changelog

### Version 1.0.0 (2024-01-25)
- Initial API release
- Authentication endpoints
- Project management
- Document upload and processing
- AI enhancement features
- Collaboration features