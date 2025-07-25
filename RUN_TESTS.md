# Testing NetDocGen Services

This guide explains how to test the NetDocGen services individually and as an integrated system.

## Prerequisites

Make sure you have:
1. All services installed with their dependencies
2. Infrastructure services running (RabbitMQ, MinIO, PostgreSQL)
3. Virtual environments activated for each service

## Individual Service Tests

### 1. Test the Parser Service

The parser service extracts network topology from Visio files.

```bash
cd parser
python test_parser.py
```

This will:
- Parse a sample Visio file
- Extract shapes and connections
- Display the parsed network topology
- Save results to `test_output/`

### 2. Test the Generator Service

The generator service creates documentation from parsed data.

```bash
cd generator
python test_generator.py
```

This will:
- Generate documents in all formats (HTML, Markdown, Word, PDF)
- Save generated files to `generator/test_output/`
- Show file sizes and generation status

**Note**: PDF generation requires WeasyPrint. Install with:
```bash
pip install weasyprint
```

### 3. Test the API Service

```bash
cd api

# Run unit tests
pytest

# Test API endpoints manually
# 1. Start the API service
uvicorn app.main:app --reload --port 8000

# 2. Visit http://localhost:8000/docs for Swagger UI
# 3. Test endpoints interactively
```

## Integration Testing

### Full Pipeline Test

This tests the complete flow: API → Parser → Generator

```bash
# From the root directory
python test_integration.py
```

**Important**: Make sure all services are running:
1. Start infrastructure (RabbitMQ, MinIO, PostgreSQL)
2. Start the Generator service: `cd generator && python src/main.py`
3. Run the integration test

The integration test will:
1. Upload sample parsed data to MinIO
2. Publish a generation request to RabbitMQ
3. Wait for the generator to process and complete
4. Display the results and generated file locations

### Manual End-to-End Test

1. **Start all services**:
   ```bash
   # Terminal 1: API
   cd api && uvicorn app.main:app --reload
   
   # Terminal 2: Parser
   cd parser && python src/main.py
   
   # Terminal 3: Generator
   cd generator && python src/main.py
   ```

2. **Create admin user**:
   ```bash
   cd api
   python create_admin.py
   ```

3. **Test via API**:
   - Login: `POST http://localhost:8000/api/auth/login`
   - Create project: `POST http://localhost:8000/api/projects`
   - Upload Visio file: `POST http://localhost:8000/api/documents/upload`
   - Check status: `GET http://localhost:8000/api/documents/{id}`
   - Download result: `GET http://localhost:8000/api/documents/{id}/download/html`

## Checking Results

### MinIO Browser

1. Visit http://localhost:9001
2. Login with credentials from .env (default: minioadmin/minioadmin)
3. Browse buckets:
   - `uploads`: Original Visio files
   - `parsed`: Parsed JSON data
   - `generated`: Generated documents

### RabbitMQ Management

1. Visit http://localhost:15672
2. Login with credentials (default: guest/guest)
3. Check:
   - Queues: See message counts
   - Exchanges: View routing
   - Connections: Active services

### Generated Files

- **Parser output**: JSON files in MinIO `parsed` bucket
- **Generator output**: Documents in MinIO `generated` bucket
- **Test outputs**: Local `test_output` directories

## Common Issues

### "No module named 'vsdx'"
```bash
cd parser
pip install -r requirements.txt
```

### "Cannot connect to RabbitMQ"
```bash
# Check if RabbitMQ is running
docker ps | grep rabbitmq

# Start if needed
docker-compose up -d rabbitmq
```

### "MinIO connection refused"
```bash
# Check if MinIO is running
docker ps | grep minio

# Start if needed
docker-compose up -d minio
```

### "Generator timeout in integration test"
Make sure the generator service is running:
```bash
cd generator
python src/main.py
```

## Debugging Tips

1. **Check service logs**: Each service outputs detailed logs
2. **Verify message flow**: Use RabbitMQ management UI
3. **Inspect storage**: Use MinIO browser to check files
4. **Test components**: Run individual test scripts first