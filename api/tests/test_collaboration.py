"""
Test collaboration features
"""
import pytest
from uuid import uuid4
from datetime import datetime, timedelta

from app.models import ShareLink, Comment, Activity, SharePermission
from app.schemas.collaboration import ShareLinkCreate, CommentCreate

@pytest.mark.asyncio
async def test_create_share_link(authenticated_client, test_project, test_db):
    """Test creating a share link for a project"""
    share_data = {
        "project_id": str(test_project.id),
        "permission": "view",
        "expires_at": (datetime.utcnow() + timedelta(days=7)).isoformat(),
        "max_uses": 10
    }
    
    response = await authenticated_client.post("/api/collaboration/share", json=share_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["project_id"] == str(test_project.id)
    assert data["permission"] == "view"
    assert data["use_count"] == 0
    assert "token" in data
    assert "share_url" in data

@pytest.mark.asyncio
async def test_access_share_link(client, test_project, test_db, test_user):
    """Test accessing a resource via share link"""
    # Create share link
    share_link = ShareLink(
        token="test-token-123",
        project_id=test_project.id,
        permission=SharePermission.VIEW,
        created_by=test_user.id
    )
    test_db.add(share_link)
    await test_db.commit()
    
    # Access share link
    response = await client.get(f"/api/collaboration/share/test-token-123")
    assert response.status_code == 200
    
    data = response.json()
    assert data["type"] == "project"
    assert data["permission"] == "view"

@pytest.mark.asyncio
async def test_share_link_with_password(authenticated_client, test_project):
    """Test share link with password protection"""
    share_data = {
        "project_id": str(test_project.id),
        "permission": "view",
        "password": "secret123"
    }
    
    response = await authenticated_client.post("/api/collaboration/share", json=share_data)
    assert response.status_code == 200
    
    token = response.json()["token"]
    
    # Try without password
    response = await authenticated_client.get(f"/api/collaboration/share/{token}")
    assert response.status_code == 401
    
    # Try with wrong password
    response = await authenticated_client.get(
        f"/api/collaboration/share/{token}",
        params={"password": "wrong"}
    )
    assert response.status_code == 401
    
    # Try with correct password
    response = await authenticated_client.get(
        f"/api/collaboration/share/{token}",
        params={"password": "secret123"}
    )
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_create_comment(authenticated_client, test_project):
    """Test creating a comment on a project"""
    comment_data = {
        "content": "This is a test comment",
        "project_id": str(test_project.id)
    }
    
    response = await authenticated_client.post("/api/collaboration/comments", json=comment_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["content"] == "This is a test comment"
    assert data["project_id"] == str(test_project.id)
    assert "user_name" in data

@pytest.mark.asyncio
async def test_comment_thread(authenticated_client, test_project, test_db):
    """Test creating comment threads"""
    # Create parent comment
    parent_data = {
        "content": "Parent comment",
        "project_id": str(test_project.id)
    }
    parent_response = await authenticated_client.post("/api/collaboration/comments", json=parent_data)
    parent_id = parent_response.json()["id"]
    
    # Create reply
    reply_data = {
        "content": "Reply to parent",
        "project_id": str(test_project.id),
        "parent_id": parent_id
    }
    
    response = await authenticated_client.post("/api/collaboration/comments", json=reply_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["parent_id"] == parent_id

@pytest.mark.asyncio
async def test_get_comments(authenticated_client, test_project, test_db, test_user):
    """Test retrieving comments for a project"""
    # Create multiple comments
    for i in range(3):
        comment = Comment(
            content=f"Comment {i}",
            project_id=test_project.id,
            user_id=test_user.id
        )
        test_db.add(comment)
    await test_db.commit()
    
    # Get comments
    response = await authenticated_client.get(
        "/api/collaboration/comments",
        params={"project_id": str(test_project.id)}
    )
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 3

@pytest.mark.asyncio
async def test_update_comment(authenticated_client, test_project, test_db, test_user):
    """Test updating a comment"""
    # Create comment
    comment = Comment(
        content="Original content",
        project_id=test_project.id,
        user_id=test_user.id
    )
    test_db.add(comment)
    await test_db.commit()
    await test_db.refresh(comment)
    
    # Update comment
    update_data = {"content": "Updated content"}
    response = await authenticated_client.put(
        f"/api/collaboration/comments/{comment.id}",
        json=update_data
    )
    assert response.status_code == 200
    
    data = response.json()
    assert data["content"] == "Updated content"

@pytest.mark.asyncio
async def test_delete_comment(authenticated_client, test_project, test_db, test_user):
    """Test deleting a comment"""
    # Create comment
    comment = Comment(
        content="To be deleted",
        project_id=test_project.id,
        user_id=test_user.id
    )
    test_db.add(comment)
    await test_db.commit()
    await test_db.refresh(comment)
    
    # Delete comment
    response = await authenticated_client.delete(f"/api/collaboration/comments/{comment.id}")
    assert response.status_code == 200
    
    # Verify soft delete
    await test_db.refresh(comment)
    assert comment.is_deleted == True

@pytest.mark.asyncio
async def test_get_activities(authenticated_client, test_project, test_db, test_user):
    """Test retrieving activity log"""
    # Create activities
    activities = [
        Activity(
            action="created",
            description="Created project",
            project_id=test_project.id,
            user_id=test_user.id
        ),
        Activity(
            action="updated",
            description="Updated project",
            project_id=test_project.id,
            user_id=test_user.id
        )
    ]
    
    for activity in activities:
        test_db.add(activity)
    await test_db.commit()
    
    # Get activities
    response = await authenticated_client.get(
        "/api/collaboration/activities",
        params={"project_id": str(test_project.id)}
    )
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 2
    assert data[0]["action"] in ["created", "updated"]