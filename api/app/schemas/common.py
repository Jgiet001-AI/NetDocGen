from pydantic import BaseModel
from typing import Optional, Any, TypeVar, Generic
from uuid import UUID

T = TypeVar('T')

class Message(BaseModel):
    """Simple message response."""
    message: str
    
class ErrorResponse(BaseModel):
    """Error response model."""
    error: str
    detail: Optional[str] = None
    
class PaginationParams(BaseModel):
    """Pagination parameters."""
    page: int = 1
    page_size: int = 20
    
    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size
    
    @property
    def limit(self) -> int:
        return self.page_size

class PaginatedResponse(BaseModel, Generic[T]):
    """Paginated response wrapper."""
    items: list[T]
    total: int
    page: int
    page_size: int
    total_pages: int
    
    @classmethod
    def create(cls, items: list[T], total: int, page: int, page_size: int):
        total_pages = (total + page_size - 1) // page_size if page_size > 0 else 0
        return cls(
            items=items,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )