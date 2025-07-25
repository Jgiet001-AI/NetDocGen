import pytest
from httpx import AsyncClient
import uuid
from unittest.mock import patch, AsyncMock


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


async def create_test_project(client: AsyncClient, token: str, name: str = "Test Project"):
    """Helper function to create a test project."""
    response = await client.post(
        "/api/v1/projects/",
        json={
            "name": name,
            "description": "Test project for documents"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.json()["id"]


@pytest.mark.asyncio
async def test_upload_visio_file_success(client: AsyncClient):
    """Test successful Visio file upload."""
    token = await create_test_user_and_login(client, "uploaduser1")
    project_id = await create_test_project(client, token, "Upload Project")
    
    # Create a mock Visio file
    files = {
        "file": ("test_diagram.vsdx", b"mock visio content", "application/vnd.ms-visio.drawing")
    }
    
    with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
        mock_upload.return_value = "test-file-key"
        
        response = await client.post(
            f"/api/v1/documents/upload/{project_id}",
            files=files,
            headers={"Authorization": f"Bearer {token}"}
        )
    
    assert response.status_code == 202
    data = response.json()
    assert data["message"] == "File uploaded successfully and processing started"
    assert "document_id" in data


@pytest.mark.asyncio
async def test_upload_invalid_file_type(client: AsyncClient):
    """Test uploading non-Visio file."""
    token = await create_test_user_and_login(client, "uploaduser2")
    project_id = await create_test_project(client, token, "Invalid File Project")
    
    # Create a non-Visio file
    files = {
        "file": ("test.txt", b"not a visio file", "text/plain")
    }
    
    response = await client.post(
        f"/api/v1/documents/upload/{project_id}",
        files=files,
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 400
    assert "Only Visio files" in response.json()["detail"]


@pytest.mark.asyncio
async def test_upload_no_file(client: AsyncClient):
    """Test upload endpoint without file."""
    token = await create_test_user_and_login(client, "uploaduser3")
    project_id = await create_test_project(client, token, "No File Project")
    
    response = await client.post(
        f"/api/v1/documents/upload/{project_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_upload_to_nonexistent_project(client: AsyncClient):
    """Test uploading to a project that doesn't exist."""
    token = await create_test_user_and_login(client, "uploaduser4")
    fake_project_id = str(uuid.uuid4())
    
    files = {
        "file": ("test.vsdx", b"mock content", "application/vnd.ms-visio.drawing")
    }
    
    response = await client.post(
        f"/api/v1/documents/upload/{fake_project_id}",
        files=files,
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_upload_to_another_users_project(client: AsyncClient):
    """Test that users cannot upload to other users' projects."""
    token1 = await create_test_user_and_login(client, "uploaduser5")
    token2 = await create_test_user_and_login(client, "uploaduser6")
    
    # User 1 creates project
    project_id = await create_test_project(client, token1, "Private Upload Project")
    
    # User 2 tries to upload
    files = {
        "file": ("test.vsdx", b"mock content", "application/vnd.ms-visio.drawing")
    }
    
    response = await client.post(
        f"/api/v1/documents/upload/{project_id}",
        files=files,
        headers={"Authorization": f"Bearer {token2}"}
    )
    
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_list_documents_empty(client: AsyncClient):
    """Test listing documents when project has none."""
    token = await create_test_user_and_login(client, "listuser1")
    project_id = await create_test_project(client, token, "Empty Docs Project")
    
    response = await client.get(
        f"/api/v1/documents/project/{project_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_list_documents_with_results(client: AsyncClient):
    """Test listing documents with uploaded files."""
    token = await create_test_user_and_login(client, "listuser2")
    project_id = await create_test_project(client, token, "Docs List Project")
    
    # Upload multiple files
    with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
        mock_upload.return_value = "test-file-key"
        
        for i in range(3):
            files = {
                "file": (f"diagram{i}.vsdx", b"mock content", "application/vnd.ms-visio.drawing")
            }
            await client.post(
                f"/api/v1/documents/upload/{project_id}",
                files=files,
                headers={"Authorization": f"Bearer {token}"}
            )
    
    # List documents
    response = await client.get(
        f"/api/v1/documents/project/{project_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3


@pytest.mark.asyncio
async def test_get_document_by_id(client: AsyncClient):
    """Test getting a specific document."""
    token = await create_test_user_and_login(client, "getdocuser1")
    project_id = await create_test_project(client, token, "Get Doc Project")
    
    # Upload a file
    with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
        mock_upload.return_value = "test-file-key"
        
        files = {
            "file": ("test.vsdx", b"mock content", "application/vnd.ms-visio.drawing")
        }
        upload_response = await client.post(
            f"/api/v1/documents/upload/{project_id}",
            files=files,
            headers={"Authorization": f"Bearer {token}"}
        )
        document_id = upload_response.json()["document_id"]
    
    # Get document
    response = await client.get(
        f"/api/v1/documents/{document_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == document_id
    assert data["project_id"] == project_id
    assert data["original_filename"] == "test.vsdx"


@pytest.mark.asyncio
async def test_get_document_unauthorized(client: AsyncClient):
    """Test that users cannot access other users' documents."""
    token1 = await create_test_user_and_login(client, "getdocuser2")
    token2 = await create_test_user_and_login(client, "getdocuser3")
    project_id = await create_test_project(client, token1, "Private Doc Project")
    
    # User 1 uploads file
    with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
        mock_upload.return_value = "test-file-key"
        
        files = {
            "file": ("private.vsdx", b"mock content", "application/vnd.ms-visio.drawing")
        }
        upload_response = await client.post(
            f"/api/v1/documents/upload/{project_id}",
            files=files,
            headers={"Authorization": f"Bearer {token1}"}
        )
        document_id = upload_response.json()["document_id"]
    
    # User 2 tries to access
    response = await client.get(
        f"/api/v1/documents/{document_id}",
        headers={"Authorization": f"Bearer {token2}"}
    )
    
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_download_generated_document(client: AsyncClient):
    """Test downloading a generated document."""
    token = await create_test_user_and_login(client, "downloaduser1")
    project_id = await create_test_project(client, token, "Download Project")
    
    # Create a document with generated content
    with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
        mock_upload.return_value = "test-file-key"
        
        files = {
            "file": ("test.vsdx", b"mock content", "application/vnd.ms-visio.drawing")
        }
        upload_response = await client.post(
            f"/api/v1/documents/upload/{project_id}",
            files=files,
            headers={"Authorization": f"Bearer {token}"}
        )
        document_id = upload_response.json()["document_id"]
    
    # Mock the download
    with patch('app.services.storage.StorageService.get_file_url', new_callable=AsyncMock) as mock_url:
        mock_url.return_value = "https://minio.example.com/download-url"
        
        response = await client.get(
            f"/api/v1/documents/{document_id}/download/pdf",
            headers={"Authorization": f"Bearer {token}"}
        )
    
    assert response.status_code == 200
    data = response.json()
    assert "download_url" in data
    assert data["format"] == "pdf"


@pytest.mark.asyncio
async def test_download_invalid_format(client: AsyncClient):
    """Test downloading with invalid format."""
    token = await create_test_user_and_login(client, "downloaduser2")
    fake_doc_id = str(uuid.uuid4())
    
    response = await client.get(
        f"/api/v1/documents/{fake_doc_id}/download/invalid",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # Should fail at path validation
    assert response.status_code == 404  # Path not found


@pytest.mark.asyncio
async def test_delete_document(client: AsyncClient):
    """Test deleting a document."""
    token = await create_test_user_and_login(client, "deleteuser1")
    project_id = await create_test_project(client, token, "Delete Doc Project")
    
    # Upload a file
    with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
        mock_upload.return_value = "test-file-key"
        
        files = {
            "file": ("to_delete.vsdx", b"mock content", "application/vnd.ms-visio.drawing")
        }
        upload_response = await client.post(
            f"/api/v1/documents/upload/{project_id}",
            files=files,
            headers={"Authorization": f"Bearer {token}"}
        )
        document_id = upload_response.json()["document_id"]
    
    # Mock storage deletion
    with patch('app.services.storage.StorageService.delete_file', new_callable=AsyncMock) as mock_delete:
        # Delete document
        response = await client.delete(
            f"/api/v1/documents/{document_id}",
            headers={"Authorization": f"Bearer {token}"}
        )
    
    assert response.status_code == 200
    assert response.json()["message"] == "Document deleted successfully"
    
    # Verify it's deleted
    get_response = await client.get(
        f"/api/v1/documents/{document_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert get_response.status_code == 404


@pytest.mark.asyncio
async def test_generate_document_formats(client: AsyncClient):
    """Test generating documents in different formats."""
    token = await create_test_user_and_login(client, "generateuser1")
    project_id = await create_test_project(client, token, "Generate Formats Project")
    
    # Upload a file
    with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
        mock_upload.return_value = "test-file-key"
        
        files = {
            "file": ("test.vsdx", b"mock content", "application/vnd.ms-visio.drawing")
        }
        upload_response = await client.post(
            f"/api/v1/documents/upload/{project_id}",
            files=files,
            headers={"Authorization": f"Bearer {token}"}
        )
        document_id = upload_response.json()["document_id"]
    
    # Test different formats
    formats = ["pdf", "html", "docx", "markdown"]
    
    with patch('app.services.message_queue.publish_message', new_callable=AsyncMock):
        for format_type in formats:
            response = await client.post(
                f"/api/v1/documents/{document_id}/generate",
                json={"format": format_type},
                headers={"Authorization": f"Bearer {token}"}
            )
            assert response.status_code == 202
            assert f"generation in {format_type} format" in response.json()["message"]


@pytest.mark.asyncio
async def test_document_processing_status(client: AsyncClient):
    """Test document processing status updates."""
    token = await create_test_user_and_login(client, "statususer1")
    project_id = await create_test_project(client, token, "Status Project")
    
    # Upload a file
    with patch('app.services.storage.StorageService.upload_file', new_callable=AsyncMock) as mock_upload:
        mock_upload.return_value = "test-file-key"
        
        files = {
            "file": ("status.vsdx", b"mock content", "application/vnd.ms-visio.drawing")
        }
        upload_response = await client.post(
            f"/api/v1/documents/upload/{project_id}",
            files=files,
            headers={"Authorization": f"Bearer {token}"}
        )
        document_id = upload_response.json()["document_id"]
    
    # Get document and check initial status
    response = await client.get(
        f"/api/v1/documents/{document_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    data = response.json()
    assert data["processing_status"] == "pending"


@pytest.mark.asyncio
async def test_file_size_limit(client: AsyncClient):
    """Test file size validation."""
    token = await create_test_user_and_login(client, "sizeuser1")
    project_id = await create_test_project(client, token, "Size Test Project")
    
    # Create a large file (over 50MB limit)
    large_content = b"x" * (51 * 1024 * 1024)  # 51MB
    
    files = {
        "file": ("large.vsdx", large_content, "application/vnd.ms-visio.drawing")
    }
    
    response = await client.post(
        f"/api/v1/documents/upload/{project_id}",
        files=files,
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # Should fail due to size
    assert response.status_code == 413 or response.status_code == 400