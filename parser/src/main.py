import asyncio
import json
import logging
import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional
import tempfile
from datetime import datetime

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

from dotenv import load_dotenv
from .parser import VisioParser
from .defaults import enrich_parsed_data
from shared.messaging.queue import MessageQueue, RoutingKeys
from shared.storage.minio_client import MinioStorage

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ParserService:
    """Main parser service that listens for parse requests and processes Visio files."""
    
    def __init__(self):
        self.mq = MessageQueue(os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672"))
        self.storage = MinioStorage(
            endpoint=os.getenv("MINIO_ENDPOINT", "localhost:9000"),
            access_key=os.getenv("MINIO_ACCESS_KEY", "minioadmin"),
            secret_key=os.getenv("MINIO_SECRET_KEY", "minioadmin"),
            secure=False
        )
        self.parser = VisioParser()
        
    async def start(self):
        """Start the parser service."""
        logger.info("Starting Visio Parser Service...")
        
        # Initialize storage buckets
        await self.storage.initialize_buckets()
        
        # Connect to message queue
        await self.mq.connect()
        
        # Start consuming messages
        await self.mq.consume(
            queue_name="visio_parser_queue",
            routing_key=RoutingKeys.PARSE_VISIO,
            callback=self.process_parse_request
        )
        
        logger.info("Parser service started. Waiting for messages...")
        
        # Keep service running
        try:
            await asyncio.Future()  # Run forever
        except KeyboardInterrupt:
            logger.info("Shutting down parser service...")
            await self.shutdown()
    
    async def process_parse_request(self, message: Dict[str, Any]):
        """
        Process a parse request message.
        
        Expected message format:
        {
            "document_id": "uuid",
            "file_path": "uploads/filename.vsdx",
            "project_id": "uuid"
        }
        """
        document_id = message.get("document_id")
        file_path = message.get("file_path")
        project_id = message.get("project_id")
        
        # Validate required fields
        if not document_id:
            error_msg = "Missing required field: document_id"
            logger.error(error_msg)
            await self._handle_parse_error(None, error_msg)
            return
            
        if not file_path:
            error_msg = "Missing required field: file_path"
            logger.error(f"{error_msg} for document {document_id}")
            await self._handle_parse_error(document_id, error_msg)
            return
            
        if not project_id:
            error_msg = "Missing required field: project_id"
            logger.error(f"{error_msg} for document {document_id}")
            await self._handle_parse_error(document_id, error_msg)
            return
        
        logger.info(f"Processing parse request for document {document_id}")
        
        try:
            # Download file from MinIO
            # file_path is in format "bucket_name/object_name", extract object_name
            if "/" in file_path:
                _, object_name = file_path.split("/", 1)
            else:
                object_name = file_path
            
            logger.info(f"Downloading file from MinIO: {object_name}")
            file_data = await self.storage.download_file("uploads", object_name)
            
            # Save to temporary file
            with tempfile.NamedTemporaryFile(suffix=".vsdx", delete=False) as temp_file:
                temp_file.write(file_data)
                temp_path = Path(temp_file.name)
            
            try:
                # Parse the file
                logger.info(f"Parsing Visio file: {temp_path}")
                parsed_data = self.parser.parse_file(temp_path)
                
                # Enrich with default values for missing information
                logger.info("Enriching parsed data with defaults for missing values")
                parsed_data = enrich_parsed_data(parsed_data)
                
                # Add metadata
                parsed_data["document_id"] = document_id
                parsed_data["project_id"] = project_id
                parsed_data["parsed_at"] = datetime.utcnow().isoformat()
                
                # Save parsed data to MinIO
                parsed_json = json.dumps(parsed_data, indent=2)
                parsed_path = f"{document_id}/parsed_data.json"
                
                # Convert to BytesIO for upload
                from io import BytesIO
                json_bytes = BytesIO(parsed_json.encode())
                
                await self.storage.upload_file(
                    bucket_type="parsed",
                    object_name=parsed_path,
                    file_data=json_bytes,
                    content_type="application/json"
                )
                
                logger.info(f"Saved parsed data to MinIO: {parsed_path}")
                
                # Publish completion message
                await self.mq.publish(
                    routing_key=RoutingKeys.PARSE_COMPLETE,
                    message={
                        "document_id": document_id,
                        "project_id": project_id,
                        "status": "completed",
                        "parsed_path": parsed_path,
                        "shape_count": len(parsed_data.get("shapes", [])),
                        "connection_count": len(parsed_data.get("connections", [])),
                        "page_count": parsed_data.get("page_count", 0)
                    }
                )
                
                logger.info(f"Successfully parsed document {document_id}")
                
            finally:
                # Clean up temporary file
                if temp_path.exists():
                    temp_path.unlink()
                    
        except Exception as e:
            logger.error(f"Error parsing document {document_id}: {e}")
            
            # Publish error message
            await self.mq.publish(
                routing_key=RoutingKeys.PARSE_COMPLETE,
                message={
                    "document_id": document_id,
                    "project_id": project_id,
                    "status": "failed",
                    "error": str(e)
                }
            )
    
    async def _handle_parse_error(self, document_id: Optional[str], error_message: str):
        """Handle parsing errors by publishing error message."""
        message = {
            "status": "failed",
            "error": error_message
        }
        
        if document_id:
            message["document_id"] = document_id
            
        # Only publish if we have document_id (required for routing)
        if document_id:
            await self.mq.publish(
                routing_key=RoutingKeys.PARSE_COMPLETE,
                message=message
            )
    
    async def shutdown(self):
        """Shutdown the service gracefully."""
        await self.mq.disconnect()

async def main():
    """Main entry point."""
    service = ParserService()
    await service.start()

if __name__ == "__main__":
    asyncio.run(main())