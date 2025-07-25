import pytest
from httpx import AsyncClient
from datetime import datetime
import uuid


async def create_test_user_and_login(client: AsyncClient, username: str = "testuser"):
    """Helper function to create a test user and get auth token."""
    # Create user
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": username,
            "email": f"{username}@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "Test User"
        }
    )
    
    # Login
    login_response = await client.post(
        "/api/v1/auth/token",
        data={
            "username": username,
            "password": "StrongP@ssw0rd!"
        }
    )
    return login_response.json()["access_token"]


@pytest.mark.asyncio
async def test_create_project_success(client: AsyncClient):
    """Test successful project creation."""
    token = await create_test_user_and_login(client, "projectuser1")
    
    response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Test Project",
            "description": "A test network documentation project"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Project"
    assert data["description"] == "A test network documentation project"
    assert "id" in data
    assert data["user_id"] is not None
    assert data["status"] == "pending"


@pytest.mark.asyncio
async def test_create_project_no_auth(client: AsyncClient):
    """Test project creation without authentication."""
    response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Unauthorized Project",
            "description": "Should fail"
        }
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_create_project_duplicate_name(client: AsyncClient):
    """Test creating project with duplicate name for same user."""
    token = await create_test_user_and_login(client, "projectuser2")
    
    # Create first project
    await client.post(
        "/api/v1/projects/",
        json={
            "name": "Duplicate Project",
            "description": "First project"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # Try to create duplicate
    response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Duplicate Project",
            "description": "Second project"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_create_project_different_users_same_name(client: AsyncClient):
    """Test that different users can have projects with the same name."""
    token1 = await create_test_user_and_login(client, "projectuser3")
    token2 = await create_test_user_and_login(client, "projectuser4")
    
    # User 1 creates project
    response1 = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Shared Name Project",
            "description": "User 1's project"
        },
        headers={"Authorization": f"Bearer {token1}"}
    )
    assert response1.status_code == 201
    
    # User 2 creates project with same name
    response2 = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Shared Name Project",
            "description": "User 2's project"
        },
        headers={"Authorization": f"Bearer {token2}"}
    )
    assert response2.status_code == 201


@pytest.mark.asyncio
async def test_list_projects_empty(client: AsyncClient):
    """Test listing projects when user has none."""
    token = await create_test_user_and_login(client, "emptyuser")
    
    response = await client.get(
        "/api/v1/projects/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_list_projects_pagination(client: AsyncClient):
    """Test project listing with pagination."""
    token = await create_test_user_and_login(client, "paginationuser")
    
    # Create multiple projects
    for i in range(15):
        await client.post(
            "/api/v1/projects/",
            json={
                "name": f"Project {i}",
                "description": f"Description {i}"
            },
            headers={"Authorization": f"Bearer {token}"}
        )
    
    # Test default pagination
    response = await client.get(
        "/api/v1/projects/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10  # Default limit
    
    # Test custom pagination
    response = await client.get(
        "/api/v1/projects/?skip=5&limit=5",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5


@pytest.mark.asyncio
async def test_list_projects_only_own(client: AsyncClient):
    """Test that users only see their own projects."""
    token1 = await create_test_user_and_login(client, "ownuser1")
    token2 = await create_test_user_and_login(client, "ownuser2")
    
    # User 1 creates projects
    for i in range(3):
        await client.post(
            "/api/v1/projects/",
            json={
                "name": f"User1 Project {i}",
                "description": "User 1's project"
            },
            headers={"Authorization": f"Bearer {token1}"}
        )
    
    # User 2 creates projects
    for i in range(2):
        await client.post(
            "/api/v1/projects/",
            json={
                "name": f"User2 Project {i}",
                "description": "User 2's project"
            },
            headers={"Authorization": f"Bearer {token2}"}
        )
    
    # User 1 lists projects
    response1 = await client.get(
        "/api/v1/projects/",
        headers={"Authorization": f"Bearer {token1}"}
    )
    assert len(response1.json()) == 3
    
    # User 2 lists projects
    response2 = await client.get(
        "/api/v1/projects/",
        headers={"Authorization": f"Bearer {token2}"}
    )
    assert len(response2.json()) == 2


@pytest.mark.asyncio
async def test_get_project_by_id(client: AsyncClient):
    """Test getting a specific project by ID."""
    token = await create_test_user_and_login(client, "getuser")
    
    # Create project
    create_response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Get Test Project",
            "description": "Project to retrieve"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    project_id = create_response.json()["id"]
    
    # Get project
    response = await client.get(
        f"/api/v1/projects/{project_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    assert data["name"] == "Get Test Project"
    assert data["description"] == "Project to retrieve"


@pytest.mark.asyncio
async def test_get_project_not_found(client: AsyncClient):
    """Test getting a non-existent project."""
    token = await create_test_user_and_login(client, "notfounduser")
    
    fake_id = str(uuid.uuid4())
    response = await client.get(
        f"/api/v1/projects/{fake_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_project_unauthorized(client: AsyncClient):
    """Test that users cannot access other users' projects."""
    token1 = await create_test_user_and_login(client, "unauthorizeduser1")
    token2 = await create_test_user_and_login(client, "unauthorizeduser2")
    
    # User 1 creates project
    create_response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Private Project",
            "description": "User 1's private project"
        },
        headers={"Authorization": f"Bearer {token1}"}
    )
    project_id = create_response.json()["id"]
    
    # User 2 tries to access it
    response = await client.get(
        f"/api/v1/projects/{project_id}",
        headers={"Authorization": f"Bearer {token2}"}
    )
    assert response.status_code == 404  # Should appear as not found


@pytest.mark.asyncio
async def test_update_project(client: AsyncClient):
    """Test updating a project."""
    token = await create_test_user_and_login(client, "updateuser")
    
    # Create project
    create_response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Original Name",
            "description": "Original description"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    project_id = create_response.json()["id"]
    
    # Update project
    response = await client.put(
        f"/api/v1/projects/{project_id}",
        json={
            "name": "Updated Name",
            "description": "Updated description"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Name"
    assert data["description"] == "Updated description"
    assert data["id"] == project_id


@pytest.mark.asyncio
async def test_update_project_unauthorized(client: AsyncClient):
    """Test that users cannot update other users' projects."""
    token1 = await create_test_user_and_login(client, "updateunauth1")
    token2 = await create_test_user_and_login(client, "updateunauth2")
    
    # User 1 creates project
    create_response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "User1 Project",
            "description": "Cannot be updated by others"
        },
        headers={"Authorization": f"Bearer {token1}"}
    )
    project_id = create_response.json()["id"]
    
    # User 2 tries to update it
    response = await client.put(
        f"/api/v1/projects/{project_id}",
        json={
            "name": "Hacked Name",
            "description": "Should not work"
        },
        headers={"Authorization": f"Bearer {token2}"}
    )
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_project(client: AsyncClient):
    """Test deleting a project."""
    token = await create_test_user_and_login(client, "deleteuser")
    
    # Create project
    create_response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "To Be Deleted",
            "description": "This will be deleted"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    project_id = create_response.json()["id"]
    
    # Delete project
    response = await client.delete(
        f"/api/v1/projects/{project_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Project deleted successfully"
    
    # Verify it's deleted
    get_response = await client.get(
        f"/api/v1/projects/{project_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert get_response.status_code == 404


@pytest.mark.asyncio
async def test_delete_project_unauthorized(client: AsyncClient):
    """Test that users cannot delete other users' projects."""
    token1 = await create_test_user_and_login(client, "deleteunauth1")
    token2 = await create_test_user_and_login(client, "deleteunauth2")
    
    # User 1 creates project
    create_response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Protected Project",
            "description": "Cannot be deleted by others"
        },
        headers={"Authorization": f"Bearer {token1}"}
    )
    project_id = create_response.json()["id"]
    
    # User 2 tries to delete it
    response = await client.delete(
        f"/api/v1/projects/{project_id}",
        headers={"Authorization": f"Bearer {token2}"}
    )
    assert response.status_code == 404
    
    # Verify it still exists for user 1
    get_response = await client.get(
        f"/api/v1/projects/{project_id}",
        headers={"Authorization": f"Bearer {token1}"}
    )
    assert get_response.status_code == 200


@pytest.mark.asyncio
async def test_project_name_validation(client: AsyncClient):
    """Test project name validation."""
    token = await create_test_user_and_login(client, "validationuser")
    
    # Test empty name
    response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "",
            "description": "Empty name should fail"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 422
    
    # Test very long name
    response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "A" * 300,  # Too long
            "description": "Name too long"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_project_status_values(client: AsyncClient):
    """Test that project status has correct values."""
    token = await create_test_user_and_login(client, "statususer")
    
    # Create project
    response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Status Test Project",
            "description": "Testing status values"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["status"] in ["pending", "processing", "completed", "failed"]
    assert data["status"] == "pending"  # Default status