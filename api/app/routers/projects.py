from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from uuid import UUID

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.project import ProjectStatus
from app.schemas.project import (
    Project, ProjectCreate, ProjectUpdate, 
    ProjectWithDocuments, ProjectSummary
)
from app.schemas.common import PaginatedResponse, PaginationParams, Message
from app.services.project import project_service

router = APIRouter()

@router.get("/", response_model=PaginatedResponse[ProjectSummary])
async def list_projects(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    status: Optional[ProjectStatus] = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List user's projects with pagination."""
    pagination = PaginationParams(page=page, page_size=page_size)
    
    projects, total = await project_service.list_projects(
        db, current_user.id, pagination, status
    )
    
    # Convert to summary with document count
    summaries = []
    for project in projects:
        summary = ProjectSummary(
            id=project.id,
            name=project.name,
            status=project.status,
            document_count=len(project.documents) if project.documents else 0,
            created_at=project.created_at
        )
        summaries.append(summary)
    
    return PaginatedResponse.create(
        items=summaries,
        total=total,
        page=page,
        page_size=page_size
    )

@router.post("/", response_model=Project, status_code=status.HTTP_201_CREATED)
async def create_project(
    project_create: ProjectCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new project."""
    project = await project_service.create_project(
        db, project_create, current_user.id
    )
    return project

@router.get("/{project_id}", response_model=ProjectWithDocuments)
async def get_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get project details including documents."""
    project = await project_service.get_project_with_documents(
        db, project_id, current_user.id
    )
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    return project

@router.put("/{project_id}", response_model=Project)
async def update_project(
    project_id: UUID,
    project_update: ProjectUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a project."""
    project = await project_service.update_project(
        db, project_id, project_update, current_user.id
    )
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    return project

@router.delete("/{project_id}", response_model=Message)
async def delete_project(
    project_id: UUID,
    permanent: bool = Query(False, description="Permanently delete the project"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a project (soft delete by default)."""
    success = await project_service.delete_project(
        db, project_id, current_user.id, soft_delete=not permanent
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    return Message(
        message="Project deleted successfully" if permanent else "Project archived successfully"
    )

@router.get("/{project_id}/statistics")
async def get_project_statistics(
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get project statistics."""
    stats = await project_service.get_project_statistics(
        db, project_id, current_user.id
    )
    
    if not stats:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    return stats