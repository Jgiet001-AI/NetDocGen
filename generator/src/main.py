import asyncio
import json
import logging
import os
import sys
from pathlib import Path
from typing import Dict, Any
from datetime import datetime

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

from dotenv import load_dotenv
from .generator import DocumentGenerator
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

class GeneratorService:
    """Main generator service that listens for generation requests and creates documents."""
    
    def __init__(self):
        self.mq = MessageQueue(os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672"))
        self.storage = MinioStorage(
            endpoint=os.getenv("MINIO_ENDPOINT", "localhost:9000"),
            access_key=os.getenv("MINIO_ACCESS_KEY", "minioadmin"),
            secret_key=os.getenv("MINIO_SECRET_KEY", "minioadmin"),
            secure=False
        )
        # Initialize generator with templates directory
        template_dir = Path(__file__).parent / "templates"
        self.generator = DocumentGenerator(template_dir)
        
    async def start(self):
        """Start the generator service."""
        logger.info("Starting Document Generator Service...")
        
        # Initialize storage buckets
        await self.storage.initialize_buckets()
        
        # Connect to message queue
        await self.mq.connect()
        
        # Start consuming messages
        await self.mq.consume(
            queue_name="document_generator_queue",
            routing_key=RoutingKeys.GENERATE_DOC,
            callback=self.process_generation_request
        )
        
        logger.info("Generator service started. Waiting for messages...")
        
        # Keep service running
        try:
            await asyncio.Future()  # Run forever
        except KeyboardInterrupt:
            logger.info("Shutting down generator service...")
            await self.shutdown()
    
    async def process_generation_request(self, message: Dict[str, Any]):
        """
        Process a document generation request.
        
        Expected message format:
        {
            "document_id": "uuid",
            "parsed_data_path": "parsed/uuid/parsed_data.json",
            "formats": ["html", "pdf", "docx", "markdown"],
            "project_id": "uuid"
        }
        """
        document_id = message.get("document_id")
        parsed_data_path = message.get("parsed_data_path")
        formats = message.get("formats", ["html"])
        project_id = message.get("project_id")
        
        logger.info(f"Processing generation request for document {document_id}")
        logger.info(f"Requested formats: {', '.join(formats)}")
        
        try:
            # Validate parsed_data_path
            if not parsed_data_path:
                raise ValueError("parsed_data_path is required but was not provided in the message")
                
            # Download parsed data from MinIO
            logger.info(f"Downloading parsed data from: {parsed_data_path}")
            
            # Always use "parsed" bucket type, the path is the object name
            bucket_type = "parsed"
            object_name = parsed_data_path
            
            parsed_json = await self.storage.download_file(bucket_type, object_name)
            parsed_data = json.loads(parsed_json.decode('utf-8'))
            
            # Add title if not present
            if "title" not in parsed_data:
                parsed_data["title"] = f"Network Documentation - {parsed_data.get('filename', 'Unknown')}"
            
            # Add project metadata for professional documentation
            project_metadata = message.get("project_metadata", {})
            if project_metadata:
                parsed_data.update(project_metadata)
            
            # Generate documents in requested formats
            generated_files = {}
            
            for format_type in formats:
                try:
                    logger.info(f"Generating {format_type} document...")
                    
                    # Generate document
                    document_bytes = self.generator.generate_documentation(
                        parsed_data, 
                        format_type
                    )
                    
                    # Upload to MinIO
                    from io import BytesIO
                    file_obj = BytesIO(document_bytes)
                    
                    # Determine content type
                    content_types = {
                        "html": "text/html",
                        "pdf": "application/pdf",
                        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        "markdown": "text/markdown"
                    }
                    content_type = content_types.get(format_type, "application/octet-stream")
                    
                    # Create storage path
                    storage_filename = f"{document_id}/{format_type}/document.{format_type}"
                    
                    # Upload to MinIO
                    storage_path = await self.storage.upload_file(
                        bucket_type="generated",
                        object_name=storage_filename,
                        file_data=file_obj,
                        content_type=content_type
                    )
                    
                    generated_files[format_type] = storage_path
                    logger.info(f"Generated {format_type} document saved to: {storage_path}")
                    
                except Exception as e:
                    logger.error(f"Error generating {format_type} document: {e}")
                    # Continue with other formats even if one fails
            
            # Publish completion message
            await self.mq.publish(
                routing_key=RoutingKeys.GENERATE_COMPLETE,
                message={
                    "document_id": document_id,
                    "project_id": project_id,
                    "status": "completed",
                    "generated_files": generated_files,
                    "generated_at": datetime.utcnow().isoformat(),
                    "formats_completed": list(generated_files.keys()),
                    "formats_failed": [f for f in formats if f not in generated_files]
                }
            )
            
            logger.info(f"Successfully generated documents for {document_id}")
            
        except Exception as e:
            logger.error(f"Error processing generation request for document {document_id}: {e}")
            
            # Publish error message
            await self.mq.publish(
                routing_key=RoutingKeys.GENERATE_COMPLETE,
                message={
                    "document_id": document_id,
                    "project_id": project_id,
                    "status": "failed",
                    "error": str(e)
                }
            )
    
    async def shutdown(self):
        """Shutdown the service gracefully."""
        await self.mq.disconnect()

async def main():
    """Main entry point."""
    service = GeneratorService()
    await service.start()

if __name__ == "__main__":
    asyncio.run(main())