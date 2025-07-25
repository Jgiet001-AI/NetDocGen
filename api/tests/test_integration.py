import pytest
from httpx import AsyncClient
import asyncio
from unittest.mock import patch, AsyncMock, Mock
import json


@pytest.mark.asyncio
async def test_full_workflow(client: AsyncClient):
    """Test the complete workflow from file upload to document generation."""
    # Step 1: Register and login
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": "integrationuser",
            "email": "integration@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "Integration Test User"
        }
    )
    
    login_response = await client.post(
        "/api/v1/auth/token",
        data={
            "username": "integrationuser",
            "password": "StrongP@ssw0rd!"
        }
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Step 2: Create a project
    project_response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Integration Test Project",
            "description": "Testing the full workflow"
        },
        headers=headers
    )
    assert project_response.status_code == 201
    project_id = project_response.json()["id"]
    
    # Step 3: Upload a Visio file
    files = {
        "file": ("test_network.vsdx", b"mock visio content", "application/vnd.ms-visio.drawing")
    }
    
    with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
        mock_upload.return_value = "test-file-key"
        
        upload_response = await client.post(
            f"/api/v1/documents/upload/{project_id}",
            files=files,
            headers=headers
        )
    
    assert upload_response.status_code == 202
    document_id = upload_response.json()["document_id"]
    
    # Step 4: Verify document was created
    doc_response = await client.get(
        f"/api/v1/documents/{document_id}",
        headers=headers
    )
    assert doc_response.status_code == 200
    doc_data = doc_response.json()
    assert doc_data["original_filename"] == "test_network.vsdx"
    assert doc_data["processing_status"] == "pending"
    
    # Step 5: Test document generation request
    with patch('app.services.message_queue.publish_message', new_callable=AsyncMock):
        gen_response = await client.post(
            f"/api/v1/documents/{document_id}/generate",
            json={"format": "pdf"},
            headers=headers
        )
        assert gen_response.status_code == 202
    
    # Step 6: List documents in project
    list_response = await client.get(
        f"/api/v1/documents/project/{project_id}",
        headers=headers
    )
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1
    
    # Step 7: Clean up - delete document and project
    with patch('app.services.storage.StorageService.delete_file', new_callable=AsyncMock):
        delete_doc_response = await client.delete(
            f"/api/v1/documents/{document_id}",
            headers=headers
        )
        assert delete_doc_response.status_code == 200
    
    delete_proj_response = await client.delete(
        f"/api/v1/projects/{project_id}",
        headers=headers
    )
    assert delete_proj_response.status_code == 200


@pytest.mark.asyncio
async def test_multiple_users_isolation(client: AsyncClient):
    """Test that users' data is properly isolated."""
    # Create two users
    users = []
    for i in range(2):
        await client.post(
            "/api/v1/auth/register",
            json={
                "username": f"isouser{i}",
                "email": f"isouser{i}@example.com",
                "password": "StrongP@ssw0rd!",
                "full_name": f"Isolation User {i}"
            }
        )
        
        login_response = await client.post(
            "/api/v1/auth/token",
            data={
                "username": f"isouser{i}",
                "password": "StrongP@ssw0rd!"
            }
        )
        token = login_response.json()["access_token"]
        users.append({"token": token, "projects": [], "documents": []})
    
    # Each user creates projects and uploads documents
    for i, user in enumerate(users):
        headers = {"Authorization": f"Bearer {user['token']}"}
        
        # Create 2 projects per user
        for j in range(2):
            proj_response = await client.post(
                "/api/v1/projects/",
                json={
                    "name": f"User{i} Project{j}",
                    "description": f"Project {j} for user {i}"
                },
                headers=headers
            )
            project_id = proj_response.json()["id"]
            user["projects"].append(project_id)
            
            # Upload a document to each project
            with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
                mock_upload.return_value = f"file-user{i}-proj{j}"
                
                files = {
                    "file": (f"diagram{j}.vsdx", b"content", "application/vnd.ms-visio.drawing")
                }
                upload_response = await client.post(
                    f"/api/v1/documents/upload/{project_id}",
                    files=files,
                    headers=headers
                )
                doc_id = upload_response.json()["document_id"]
                user["documents"].append(doc_id)
    
    # Verify isolation - each user should only see their own data
    for i, user in enumerate(users):
        headers = {"Authorization": f"Bearer {user['token']}"}
        
        # Check projects
        proj_list_response = await client.get("/api/v1/projects/", headers=headers)
        user_projects = proj_list_response.json()
        assert len(user_projects) == 2
        
        # Verify user can't access other user's projects
        other_user_idx = 1 - i  # Get the other user's index
        other_project_id = users[other_user_idx]["projects"][0]
        
        other_proj_response = await client.get(
            f"/api/v1/projects/{other_project_id}",
            headers=headers
        )
        assert other_proj_response.status_code == 404
        
        # Verify user can't access other user's documents
        other_doc_id = users[other_user_idx]["documents"][0]
        other_doc_response = await client.get(
            f"/api/v1/documents/{other_doc_id}",
            headers=headers
        )
        assert other_doc_response.status_code == 404


@pytest.mark.asyncio
async def test_concurrent_operations(client: AsyncClient):
    """Test system behavior under concurrent operations."""
    # Create a user
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": "concurrentuser",
            "email": "concurrent@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "Concurrent Test User"
        }
    )
    
    login_response = await client.post(
        "/api/v1/auth/token",
        data={
            "username": "concurrentuser",
            "password": "StrongP@ssw0rd!"
        }
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create multiple projects concurrently
    async def create_project(index):
        response = await client.post(
            "/api/v1/projects/",
            json={
                "name": f"Concurrent Project {index}",
                "description": f"Testing concurrent creation {index}"
            },
            headers=headers
        )
        return response.json()["id"]
    
    # Create 5 projects concurrently
    project_tasks = [create_project(i) for i in range(5)]
    project_ids = await asyncio.gather(*project_tasks)
    
    assert len(project_ids) == 5
    assert len(set(project_ids)) == 5  # All IDs should be unique
    
    # Upload documents concurrently to first project
    project_id = project_ids[0]
    
    async def upload_document(index):
        with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
            mock_upload.return_value = f"concurrent-file-{index}"
            
            files = {
                "file": (f"concurrent{index}.vsdx", b"content", "application/vnd.ms-visio.drawing")
            }
            response = await client.post(
                f"/api/v1/documents/upload/{project_id}",
                files=files,
                headers=headers
            )
            return response.json()["document_id"]
    
    # Upload 3 documents concurrently
    upload_tasks = [upload_document(i) for i in range(3)]
    document_ids = await asyncio.gather(*upload_tasks)
    
    assert len(document_ids) == 3
    assert len(set(document_ids)) == 3  # All IDs should be unique
    
    # Verify all documents were created
    list_response = await client.get(
        f"/api/v1/documents/project/{project_id}",
        headers=headers
    )
    documents = list_response.json()
    assert len(documents) == 3


@pytest.mark.asyncio
async def test_error_recovery(client: AsyncClient):
    """Test system recovery from various error conditions."""
    # Create user and login
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": "erroruser",
            "email": "error@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "Error Test User"
        }
    )
    
    login_response = await client.post(
        "/api/v1/auth/token",
        data={
            "username": "erroruser",
            "password": "StrongP@ssw0rd!"
        }
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Test 1: Storage service failure during upload
    project_response = await client.post(
        "/api/v1/projects/",
        json={
            "name": "Error Recovery Project",
            "description": "Testing error recovery"
        },
        headers=headers
    )
    project_id = project_response.json()["id"]
    
    with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
        mock_upload.side_effect = Exception("Storage service unavailable")
        
        files = {
            "file": ("error_test.vsdx", b"content", "application/vnd.ms-visio.drawing")
        }
        upload_response = await client.post(
            f"/api/v1/documents/upload/{project_id}",
            files=files,
            headers=headers
        )
        
        # Should handle the error gracefully
        assert upload_response.status_code >= 400
    
    # Test 2: Verify project is still accessible after error
    proj_response = await client.get(
        f"/api/v1/projects/{project_id}",
        headers=headers
    )
    assert proj_response.status_code == 200
    
    # Test 3: Message queue failure
    # First, successfully upload a file
    with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
        mock_upload.return_value = "recovery-file-key"
        
        files = {
            "file": ("recovery.vsdx", b"content", "application/vnd.ms-visio.drawing")
        }
        upload_response = await client.post(
            f"/api/v1/documents/upload/{project_id}",
            files=files,
            headers=headers
        )
        document_id = upload_response.json()["document_id"]
    
    # Now test message queue failure during generation
    with patch('app.services.message_queue.publish_message', new_callable=AsyncMock) as mock_publish:
        mock_publish.side_effect = Exception("Message queue unavailable")
        
        gen_response = await client.post(
            f"/api/v1/documents/{document_id}/generate",
            json={"format": "pdf"},
            headers=headers
        )
        
        # Should handle the error gracefully
        assert gen_response.status_code >= 400
    
    # Verify document is still accessible
    doc_response = await client.get(
        f"/api/v1/documents/{document_id}",
        headers=headers
    )
    assert doc_response.status_code == 200