"""
API endpoints for collaboration features
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_
from uuid import UUID, uuid4
from typing import List, Optional
from datetime import datetime
import secrets

from app.database import get_db
from app.dependencies import get_current_user
from app.models import User, Project, Document, ShareLink, Comment, Activity
from app.schemas.collaboration import (
    ShareLinkCreate, ShareLinkResponse, ShareLinkAccess,
    CommentCreate, CommentUpdate, CommentResponse,
    ActivityResponse, CollaboratorAdd, CollaboratorResponse
)
from app.utils.security import get_password_hash, verify_password

router = APIRouter()

# Share Link endpoints
@router.post("/share", response_model=ShareLinkResponse)
async def create_share_link(
    share_data: ShareLinkCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a share link for a project or document"""
    # Verify access to resource
    if share_data.project_id:
        project = await db.get(Project, share_data.project_id)
        if not project or project.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to share this project"
            )
    elif share_data.document_id:
        document = await db.get(Document, share_data.document_id)
        if not document:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Document not found"
            )
        project = await db.get(Project, document.project_id)
        if project.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to share this document"
            )
    
    # Create share link
    share_link = ShareLink(
        token=secrets.token_urlsafe(32),
        project_id=share_data.project_id,
        document_id=share_data.document_id,
        permission=share_data.permission,
        expires_at=share_data.expires_at,
        max_uses=share_data.max_uses,
        password_hash=get_password_hash(share_data.password) if share_data.password else None,
        created_by=current_user.id
    )
    
    db.add(share_link)
    await db.commit()
    await db.refresh(share_link)
    
    # Add activity
    activity = Activity(
        action="shared",
        description=f"Created share link with {share_data.permission} permission",
        project_id=share_data.project_id,
        document_id=share_data.document_id,
        user_id=current_user.id
    )
    db.add(activity)
    await db.commit()
    
    # Add share URL
    base_url = "http://localhost:3000"  # Should come from config
    share_link.share_url = f"{base_url}/share/{share_link.token}"
    
    return share_link

@router.get("/share/{token}")
async def access_shared_resource(
    token: str,
    password: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """Access a shared resource via share link"""
    # Get share link
    result = await db.execute(
        select(ShareLink).where(ShareLink.token == token)
    )
    share_link = result.scalar_one_or_none()
    
    if not share_link or not share_link.is_valid():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid or expired share link"
        )
    
    # Check password if required
    if share_link.password_hash:
        if not password or not verify_password(password, share_link.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid password"
            )
    
    # Update usage
    share_link.use_count += 1
    share_link.last_accessed = datetime.utcnow()
    await db.commit()
    
    # Return resource data
    if share_link.project_id:
        project = await db.get(Project, share_link.project_id)
        return {
            "type": "project",
            "resource": project,
            "permission": share_link.permission
        }
    else:
        document = await db.get(Document, share_link.document_id)
        return {
            "type": "document", 
            "resource": document,
            "permission": share_link.permission
        }

@router.delete("/share/{share_id}")
async def delete_share_link(
    share_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a share link"""
    share_link = await db.get(ShareLink, share_id)
    if not share_link:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Share link not found"
        )
    
    if share_link.created_by != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this share link"
        )
    
    share_link.is_active = False
    await db.commit()
    
    return {"message": "Share link deleted successfully"}

# Comment endpoints
@router.post("/comments", response_model=CommentResponse)
async def create_comment(
    comment_data: CommentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a comment on a project or document"""
    # Verify access to resource
    if comment_data.project_id:
        project = await db.get(Project, comment_data.project_id)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )
        # Check if user has access (owner or collaborator)
        if project.owner_id != current_user.id:
            # TODO: Check collaborator access
            pass
    elif comment_data.document_id:
        document = await db.get(Document, comment_data.document_id)
        if not document:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Document not found"
            )
    
    # Create comment
    comment = Comment(
        content=comment_data.content,
        project_id=comment_data.project_id,
        document_id=comment_data.document_id,
        parent_id=comment_data.parent_id,
        user_id=current_user.id
    )
    
    db.add(comment)
    await db.commit()
    await db.refresh(comment)
    
    # Add activity
    activity = Activity(
        action="commented",
        description=f"Added a comment",
        project_id=comment_data.project_id,
        document_id=comment_data.document_id,
        user_id=current_user.id
    )
    db.add(activity)
    await db.commit()
    
    # Add user info for response
    comment.user_name = current_user.full_name or current_user.email
    
    return comment

@router.get("/comments", response_model=List[CommentResponse])
async def get_comments(
    project_id: Optional[UUID] = Query(None),
    document_id: Optional[UUID] = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get comments for a project or document"""
    if not project_id and not document_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Either project_id or document_id must be provided"
        )
    
    # Build query
    query = select(Comment).where(
        and_(
            Comment.is_deleted == False,
            or_(
                Comment.project_id == project_id if project_id else False,
                Comment.document_id == document_id if document_id else False
            )
        )
    ).order_by(Comment.created_at.desc())
    
    result = await db.execute(query)
    comments = result.scalars().all()
    
    # Add user info
    for comment in comments:
        user = await db.get(User, comment.user_id)
        comment.user_name = user.full_name or user.email
    
    return comments

@router.put("/comments/{comment_id}", response_model=CommentResponse)
async def update_comment(
    comment_id: UUID,
    comment_update: CommentUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a comment"""
    comment = await db.get(Comment, comment_id)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )
    
    if comment.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this comment"
        )
    
    comment.content = comment_update.content
    comment.updated_at = datetime.utcnow()
    
    await db.commit()
    await db.refresh(comment)
    
    comment.user_name = current_user.full_name or current_user.email
    
    return comment

@router.delete("/comments/{comment_id}")
async def delete_comment(
    comment_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a comment"""
    comment = await db.get(Comment, comment_id)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )
    
    if comment.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this comment"
        )
    
    comment.is_deleted = True
    await db.commit()
    
    return {"message": "Comment deleted successfully"}

# Activity endpoints
@router.get("/activities", response_model=List[ActivityResponse])
async def get_activities(
    project_id: Optional[UUID] = Query(None),
    document_id: Optional[UUID] = Query(None),
    limit: int = Query(50, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get activity log for a project or document"""
    # Build query
    conditions = []
    if project_id:
        conditions.append(Activity.project_id == project_id)
    if document_id:
        conditions.append(Activity.document_id == document_id)
    
    if not conditions:
        # Get all activities for user's projects
        user_projects = await db.execute(
            select(Project.id).where(Project.owner_id == current_user.id)
        )
        project_ids = [p[0] for p in user_projects]
        conditions.append(Activity.project_id.in_(project_ids))
    
    query = select(Activity).where(
        or_(*conditions)
    ).order_by(Activity.timestamp.desc()).limit(limit)
    
    result = await db.execute(query)
    activities = result.scalars().all()
    
    # Add user info
    for activity in activities:
        user = await db.get(User, activity.user_id)
        activity.user_name = user.full_name or user.email
    
    return activities