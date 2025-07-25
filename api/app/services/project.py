from typing import List, Optional
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, or_
from sqlalchemy.orm import selectinload
from fastapi import HTTPException, status

from app.models.project import Project, ProjectStatus
from app.models.document import Document
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.schemas.common import PaginationParams

class ProjectService:
    """Service for managing projects."""
    
    async def create_project(
        self, 
        db: AsyncSession, 
        project_create: ProjectCreate,
        user_id: UUID
    ) -> Project:
        """Create a new project."""
        # Check if a project with the same name already exists (case-insensitive)
        existing_project_stmt = select(Project).where(
            and_(
                func.lower(Project.name) == func.lower(project_create.name),
                Project.owner_id == user_id,
                Project.status != ProjectStatus.DELETED
            )
        )
        result = await db.execute(existing_project_stmt)
        existing_project = result.scalar_one_or_none()
        
        if existing_project:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"A project with the name '{project_create.name}' already exists"
            )
        
        project = Project(
            **project_create.model_dump(),
            owner_id=user_id
        )
        
        db.add(project)
        await db.commit()
        await db.refresh(project)
        
        return project
    
    async def get_project(
        self, 
        db: AsyncSession, 
        project_id: UUID,
        user_id: Optional[UUID] = None
    ) -> Optional[Project]:
        """Get a project by ID."""
        stmt = select(Project).where(Project.id == project_id)
        
        # If user_id provided, ensure user owns the project
        if user_id:
            stmt = stmt.where(Project.owner_id == user_id)
            
        result = await db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_project_with_documents(
        self,
        db: AsyncSession,
        project_id: UUID,
        user_id: Optional[UUID] = None
    ) -> Optional[Project]:
        """Get a project with its documents."""
        stmt = select(Project).options(
            selectinload(Project.documents)
        ).where(Project.id == project_id)
        
        if user_id:
            stmt = stmt.where(Project.owner_id == user_id)
            
        result = await db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def list_projects(
        self,
        db: AsyncSession,
        user_id: UUID,
        pagination: PaginationParams,
        status: Optional[ProjectStatus] = None
    ) -> tuple[List[Project], int]:
        """List projects for a user with pagination."""
        # Base query - exclude deleted projects by default
        base_query = select(Project).where(
            and_(
                Project.owner_id == user_id,
                Project.status != ProjectStatus.DELETED
            )
        )
        
        # Apply status filter if provided (allows querying deleted if explicitly requested)
        if status:
            if status == ProjectStatus.DELETED:
                # If specifically querying deleted projects, override the default filter
                base_query = select(Project).where(
                    and_(
                        Project.owner_id == user_id,
                        Project.status == status
                    )
                )
            else:
                base_query = base_query.where(Project.status == status)
            
        # Count total
        count_stmt = select(func.count()).select_from(base_query.subquery())
        total_result = await db.execute(count_stmt)
        total = total_result.scalar()
        
        # Get paginated results with documents relationship loaded
        stmt = base_query.options(
            selectinload(Project.documents)
        ).order_by(Project.created_at.desc()).offset(
            pagination.offset
        ).limit(pagination.limit)
        
        result = await db.execute(stmt)
        projects = result.scalars().all()
        
        return projects, total
    
    async def update_project(
        self,
        db: AsyncSession,
        project_id: UUID,
        project_update: ProjectUpdate,
        user_id: UUID
    ) -> Optional[Project]:
        """Update a project."""
        project = await self.get_project(db, project_id, user_id)
        
        if not project:
            return None
            
        # Update fields
        update_data = project_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(project, field, value)
            
        await db.commit()
        await db.refresh(project)
        
        return project
    
    async def delete_project(
        self,
        db: AsyncSession,
        project_id: UUID,
        user_id: UUID,
        soft_delete: bool = True
    ) -> bool:
        """Delete a project (soft delete by default)."""
        project = await self.get_project(db, project_id, user_id)
        
        if not project:
            return False
            
        if soft_delete:
            # Soft delete - just change status
            project.status = ProjectStatus.DELETED
            await db.commit()
        else:
            # Hard delete - remove from database
            await db.delete(project)
            await db.commit()
            
        return True
    
    async def get_project_statistics(
        self,
        db: AsyncSession,
        project_id: UUID,
        user_id: UUID
    ) -> dict:
        """Get statistics for a project."""
        project = await self.get_project(db, project_id, user_id)
        
        if not project:
            return {}
            
        # Count documents by status
        stmt = select(
            Document.status,
            func.count(Document.id)
        ).where(
            Document.project_id == project_id
        ).group_by(Document.status)
        
        result = await db.execute(stmt)
        status_counts = dict(result.all())
        
        return {
            "total_documents": sum(status_counts.values()),
            "status_breakdown": status_counts,
            "created_at": project.created_at,
            "updated_at": project.updated_at
        }

# Global project service instance
project_service = ProjectService()