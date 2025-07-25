import os
import io
from typing import BinaryIO, Optional
from uuid import UUID
from pathlib import Path
import logging

from app.config import settings

# Import the shared MinIO client
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))
from shared.storage.minio_client import MinioStorage

logger = logging.getLogger(__name__)

class StorageService:
    """Service for handling file storage operations."""
    
    def __init__(self):
        self.minio_client = MinioStorage(
            endpoint=settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            secure=settings.MINIO_SECURE
        )
        self._initialized = False
    
    async def initialize(self):
        """Initialize storage buckets."""
        if not self._initialized:
            logger.info("Initializing storage buckets...")
            try:
                await self.minio_client.initialize_buckets()
                self._initialized = True
                logger.info("Storage buckets initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize storage buckets: {str(e)}", exc_info=True)
                raise
    
    async def upload_visio_file(
        self, 
        file_data: bytes,
        filename: str,
        document_id: UUID,
        content_type: str = "application/vnd.visio"
    ) -> str:
        """
        Upload a Visio file to storage.
        
        Args:
            file_data: File content as bytes
            filename: Original filename
            document_id: Document UUID
            content_type: MIME type
            
        Returns:
            Storage path
        """
        logger.info(f"Uploading Visio file for document {document_id}, filename: {filename}")
        
        await self.initialize()
        
        # Create unique storage path
        file_extension = Path(filename).suffix
        storage_filename = f"{document_id}{file_extension}"
        logger.debug(f"Storage filename: {storage_filename}")
        
        # Convert bytes to file-like object
        file_obj = io.BytesIO(file_data)
        
        try:
            # Upload to MinIO
            logger.info(f"Uploading to MinIO bucket 'uploads' with object name: {storage_filename}")
            storage_path = await self.minio_client.upload_file(
                bucket_type="uploads",
                object_name=storage_filename,
                file_data=file_obj,
                content_type=content_type
            )
            logger.info(f"File uploaded successfully to: {storage_path}")
            return storage_path
        except Exception as e:
            logger.error(f"Failed to upload file to MinIO: {str(e)}", exc_info=True)
            raise
    
    async def download_file(self, bucket_type: str, object_name: str) -> bytes:
        """Download a file from storage."""
        await self.initialize()
        return await self.minio_client.download_file(bucket_type, object_name)
    
    async def delete_file(self, bucket_type: str, object_name: str):
        """Delete a file from storage."""
        await self.initialize()
        await self.minio_client.delete_file(bucket_type, object_name)
    
    async def upload_generated_document(
        self,
        file_data: bytes,
        document_id: UUID,
        format_type: str,
        content_type: Optional[str] = None
    ) -> str:
        """
        Upload a generated document.
        
        Args:
            file_data: Generated document content
            document_id: Document UUID
            format_type: Format (html, pdf, docx, markdown)
            content_type: MIME type
            
        Returns:
            Storage path
        """
        await self.initialize()
        
        # Determine content type if not provided
        if not content_type:
            content_types = {
                "html": "text/html",
                "pdf": "application/pdf",
                "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                "markdown": "text/markdown"
            }
            content_type = content_types.get(format_type, "application/octet-stream")
        
        # Create storage path
        storage_filename = f"{document_id}/{format_type}/document.{format_type}"
        
        # Convert to file-like object
        file_obj = io.BytesIO(file_data)
        
        # Upload to MinIO
        storage_path = await self.minio_client.upload_file(
            bucket_type="generated",
            object_name=storage_filename,
            file_data=file_obj,
            content_type=content_type
        )
        
        return storage_path
    
    def get_download_url(self, storage_path: str) -> str:
        """
        Generate a download URL for a file.
        
        Note: In production, you might want to generate pre-signed URLs
        for direct download from MinIO.
        """
        # For now, return a path that the API can use to stream the file
        return f"/api/documents/download/{storage_path}"

# Global storage service instance
storage_service = StorageService()