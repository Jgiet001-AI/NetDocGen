import logging
from typing import Optional, BinaryIO
from pathlib import Path
import io
from minio import Minio
from minio.error import S3Error

logger = logging.getLogger(__name__)

class MinioStorage:
    """MinIO object storage client for file management."""
    
    def __init__(self, endpoint: str, access_key: str, secret_key: str, secure: bool = False):
        self.client = Minio(
            endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure
        )
        self.buckets = {
            "uploads": "netdocgen-uploads",
            "parsed": "netdocgen-parsed",
            "generated": "netdocgen-generated"
        }
        
    async def initialize_buckets(self):
        """Create required buckets if they don't exist."""
        for bucket_name in self.buckets.values():
            try:
                if not self.client.bucket_exists(bucket_name):
                    self.client.make_bucket(bucket_name)
                    logger.info(f"Created bucket: {bucket_name}")
            except S3Error as e:
                logger.error(f"Error creating bucket {bucket_name}: {e}")
                raise
    
    async def upload_file(self, bucket_type: str, object_name: str, file_data: BinaryIO, 
                         content_type: str = "application/octet-stream") -> str:
        """
        Upload a file to MinIO.
        
        Args:
            bucket_type: Type of bucket (uploads, parsed, generated)
            object_name: Name of the object in the bucket
            file_data: File data as binary stream
            content_type: MIME type of the file
            
        Returns:
            Object path in MinIO
        """
        bucket_name = self.buckets.get(bucket_type)
        if not bucket_name:
            raise ValueError(f"Invalid bucket type: {bucket_type}")
        
        try:
            # Get file size
            file_data.seek(0, 2)
            file_size = file_data.tell()
            file_data.seek(0)
            
            self.client.put_object(
                bucket_name,
                object_name,
                file_data,
                file_size,
                content_type=content_type
            )
            logger.info(f"Uploaded {object_name} to {bucket_name}")
            return f"{bucket_name}/{object_name}"
        except S3Error as e:
            logger.error(f"Error uploading file: {e}")
            raise
    
    async def download_file(self, bucket_type: str, object_name: str) -> bytes:
        """
        Download a file from MinIO.
        
        Args:
            bucket_type: Type of bucket
            object_name: Name of the object
            
        Returns:
            File content as bytes
        """
        bucket_name = self.buckets.get(bucket_type)
        if not bucket_name:
            raise ValueError(f"Invalid bucket type: {bucket_type}")
        
        try:
            response = self.client.get_object(bucket_name, object_name)
            data = response.read()
            response.close()
            response.release_conn()
            return data
        except S3Error as e:
            logger.error(f"Error downloading file: {e}")
            raise
    
    async def delete_file(self, bucket_type: str, object_name: str):
        """Delete a file from MinIO."""
        bucket_name = self.buckets.get(bucket_type)
        if not bucket_name:
            raise ValueError(f"Invalid bucket type: {bucket_type}")
        
        try:
            self.client.remove_object(bucket_name, object_name)
            logger.info(f"Deleted {object_name} from {bucket_name}")
        except S3Error as e:
            logger.error(f"Error deleting file: {e}")
            raise