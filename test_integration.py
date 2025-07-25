#!/usr/bin/env python3
"""
Integration test for the complete NetDocGen pipeline.
Tests the flow from API -> Parser -> Generator with RabbitMQ and MinIO.
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from uuid import uuid4
from datetime import datetime

# Add directories to path
sys.path.append(str(Path(__file__)))

from dotenv import load_dotenv
load_dotenv()

from shared.messaging.queue import MessageQueue, RoutingKeys
from shared.storage.minio_client import MinioStorage

# Sample parsed data (simulating parser output)
SAMPLE_PARSED_DATA = {
    "title": "Integration Test Network",
    "filename": "test_integration.vsdx",
    "created_date": datetime.utcnow().isoformat(),
    "modified_date": datetime.utcnow().isoformat(),
    "author": "Integration Test",
    "pages": ["Network Topology", "Server Layout"],
    "shapes": [
        {
            "id": "shape1",
            "name": "Core Router A",
            "type": "router",
            "text": "Core Router A\n10.0.0.1",
            "master_shape": "Router"
        },
        {
            "id": "shape2",
            "name": "Distribution Switch 1",
            "type": "switch",
            "text": "Distribution Switch 1\n10.0.1.1",
            "master_shape": "Switch"
        },
        {
            "id": "shape3",
            "name": "Distribution Switch 2",
            "type": "switch",
            "text": "Distribution Switch 2\n10.0.2.1",
            "master_shape": "Switch"
        },
        {
            "id": "shape4",
            "name": "Web Server Farm",
            "type": "server",
            "text": "Web Server Farm\n10.10.1.0/24",
            "master_shape": "Server"
        },
        {
            "id": "shape5",
            "name": "Database Cluster",
            "type": "server",
            "text": "Database Cluster\n10.10.2.0/24",
            "master_shape": "Server"
        },
        {
            "id": "shape6",
            "name": "Perimeter Firewall",
            "type": "firewall",
            "text": "Perimeter Firewall\n10.0.0.254",
            "master_shape": "Firewall"
        }
    ],
    "connections": [
        {
            "id": "conn1",
            "source": "shape1",
            "target": "shape2",
            "type": "ethernet",
            "properties": {"bandwidth": "10Gbps", "vlan": "100"}
        },
        {
            "id": "conn2",
            "source": "shape1",
            "target": "shape3",
            "type": "ethernet",
            "properties": {"bandwidth": "10Gbps", "vlan": "200"}
        },
        {
            "id": "conn3",
            "source": "shape2",
            "target": "shape4",
            "type": "ethernet",
            "properties": {"bandwidth": "1Gbps", "vlan": "101"}
        },
        {
            "id": "conn4",
            "source": "shape3",
            "target": "shape5",
            "type": "ethernet",
            "properties": {"bandwidth": "1Gbps", "vlan": "201"}
        },
        {
            "id": "conn5",
            "source": "shape1",
            "target": "shape6",
            "type": "ethernet",
            "properties": {"bandwidth": "10Gbps", "vlan": "1"}
        }
    ]
}

async def test_integration():
    """Test the complete integration pipeline."""
    print("Starting NetDocGen Integration Test...")
    print("=" * 50)
    
    # Initialize services
    mq = MessageQueue(os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672"))
    storage = MinioStorage(
        endpoint=os.getenv("MINIO_ENDPOINT", "localhost:9000"),
        access_key=os.getenv("MINIO_ACCESS_KEY", "minioadmin"),
        secret_key=os.getenv("MINIO_SECRET_KEY", "minioadmin"),
        secure=False
    )
    
    try:
        # Connect to services
        print("\n1. Connecting to services...")
        await mq.connect()
        await storage.initialize_buckets()
        print("   ✓ Connected to RabbitMQ and MinIO")
        
        # Simulate document and project IDs
        document_id = str(uuid4())
        project_id = str(uuid4())
        
        print(f"\n2. Test IDs:")
        print(f"   Document ID: {document_id}")
        print(f"   Project ID: {project_id}")
        
        # Step 1: Upload parsed data to MinIO (simulating parser output)
        print("\n3. Uploading parsed data to MinIO...")
        parsed_data_path = f"parsed/{document_id}/parsed_data.json"
        
        from io import BytesIO
        parsed_json = json.dumps(SAMPLE_PARSED_DATA, indent=2)
        await storage.upload_file(
            bucket_type="parsed",
            object_name=f"{document_id}/parsed_data.json",
            file_data=BytesIO(parsed_json.encode()),
            content_type="application/json"
        )
        print(f"   ✓ Uploaded to: {parsed_data_path}")
        
        # Step 2: Publish generation request
        print("\n4. Publishing generation request to RabbitMQ...")
        generation_request = {
            "document_id": document_id,
            "project_id": project_id,
            "parsed_data_path": parsed_data_path,
            "formats": ["html", "markdown", "docx"]
        }
        
        await mq.publish(
            routing_key=RoutingKeys.GENERATE_DOC,
            message=generation_request
        )
        print("   ✓ Published generation request")
        print(f"   Formats: {', '.join(generation_request['formats'])}")
        
        # Step 3: Listen for completion
        print("\n5. Waiting for generation completion...")
        print("   (Make sure the generator service is running!)")
        
        completion_received = asyncio.Event()
        completion_message = None
        
        async def handle_completion(message):
            nonlocal completion_message
            completion_message = message
            completion_received.set()
        
        # Subscribe to completion messages
        await mq.consume(
            queue_name="test_completion_queue",
            routing_key=RoutingKeys.GENERATE_COMPLETE,
            callback=handle_completion
        )
        
        # Wait for completion (timeout after 30 seconds)
        try:
            await asyncio.wait_for(completion_received.wait(), timeout=30.0)
            
            if completion_message:
                print("\n   ✓ Generation completed!")
                print(f"   Status: {completion_message.get('status')}")
                
                if completion_message.get('status') == 'completed':
                    print(f"   Formats completed: {', '.join(completion_message.get('formats_completed', []))}")
                    print("\n   Generated files:")
                    for format_type, path in completion_message.get('generated_files', {}).items():
                        print(f"     - {format_type}: {path}")
                else:
                    print(f"   Error: {completion_message.get('error')}")
            
        except asyncio.TimeoutError:
            print("\n   ✗ Timeout waiting for generation completion")
            print("   Make sure the generator service is running!")
        
        print("\n" + "=" * 50)
        print("Integration test complete!")
        
    except Exception as e:
        print(f"\n✗ Error during integration test: {e}")
        raise
    finally:
        await mq.disconnect()

if __name__ == "__main__":
    asyncio.run(test_integration())