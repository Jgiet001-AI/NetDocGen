# Visio Parser Service

The Visio Parser Service is responsible for extracting network diagram information from Microsoft Visio files (.vsdx format).

## Features

- **Cross-platform VSDX parsing**: Uses the `vsdx` Python library for parsing modern Visio files
- **Intelligent shape recognition**: Automatically detects network device types (routers, switches, firewalls, servers, etc.)
- **Connection extraction**: Identifies and categorizes network connections between devices
- **Metadata extraction**: Captures document properties like author, creation date, etc.
- **Async message queue integration**: Listens for parse requests via RabbitMQ
- **Object storage integration**: Downloads files from and uploads results to MinIO

## Architecture

The parser service follows a microservice architecture:

1. Listens for parse requests on RabbitMQ queue
2. Downloads Visio files from MinIO storage
3. Parses the file to extract network topology
4. Saves parsed JSON data back to MinIO
5. Publishes completion notifications

## Shape Recognition

The parser can identify the following network device types:

- **Router**: Core routers, edge routers, BGP routers
- **Switch**: L2/L3 switches, core/distribution/access switches
- **Firewall**: Various firewall appliances (ASA, Palo Alto, FortiGate, etc.)
- **Server**: Web servers, database servers, application servers, VMs
- **Workstation**: PCs, laptops, user devices
- **Cloud**: Cloud services, internet connections

## Installation

1. Install dependencies:
```bash
cd parser
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export RABBITMQ_URL=amqp://guest:guest@localhost:5672
export MINIO_ENDPOINT=localhost:9000
export MINIO_ACCESS_KEY=minioadmin
export MINIO_SECRET_KEY=minioadmin
```

## Running the Service

### Standalone
```bash
python src/main.py
```

### Docker
```bash
docker build -t netdocgen-parser .
docker run --env-file ../.env netdocgen-parser
```

## Testing

Run unit tests:
```bash
pytest tests/
```

Generate sample test data:
```bash
python tests/generate_test_data.py
```

## Message Format

### Input Message (via RabbitMQ)
```json
{
    "document_id": "uuid",
    "file_path": "uploads/filename.vsdx",
    "project_id": "uuid"
}
```

### Output (Parsed Data in MinIO)
```json
{
    "filename": "network_diagram.vsdx",
    "shapes": [
        {
            "id": "1",
            "name": "Core Router",
            "shape_type": "router",
            "x": 100.0,
            "y": 200.0,
            "width": 80.0,
            "height": 80.0,
            "properties": {
                "ip_address": "10.0.0.1"
            }
        }
    ],
    "connections": [
        {
            "id": "c1",
            "source_id": "1",
            "target_id": "2",
            "connection_type": "ethernet",
            "properties": {
                "bandwidth": "10Gbps"
            }
        }
    ],
    "metadata": {
        "author": "Network Admin",
        "created": "2024-01-01T00:00:00Z"
    },
    "page_count": 1
}
```

## Extending the Parser

### Adding New Shape Types

1. Add the new type to `ShapeType` enum in `shapes.py`
2. Add detection patterns in `detect_shape_type()` in `utils.py`
3. Update tests in `test_parser.py`

### Supporting Additional File Formats

The parser is designed to be extensible. To add support for legacy .vsd files or other formats:

1. Add appropriate parsing library to requirements.txt
2. Implement parsing method in `VisioParser` class
3. Update `parse_file()` method to handle the new format

## Troubleshooting

### Common Issues

1. **VSDX library not found**: Install with `pip install vsdx`
2. **Connection refused**: Check RabbitMQ and MinIO are running
3. **Parse errors**: Enable debug logging with `export LOG_LEVEL=DEBUG`

### Debug Mode

Run with verbose logging:
```bash
LOG_LEVEL=DEBUG python src/main.py
```

## Performance Considerations

- Large VSDX files may take several seconds to parse
- The service processes one file at a time
- Consider scaling horizontally for high throughput

## Future Enhancements

- Support for legacy .vsd files
- Batch processing capabilities
- Shape image extraction
- Custom stencil recognition
- Performance optimizations for large diagrams