import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.auth import auth_service
from app.models.user import User


@pytest.mark.asyncio
async def test_register_success(client: AsyncClient):
    """Test successful user registration."""
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "Test User"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert data["full_name"] == "Test User"
    assert "id" in data
    assert "password" not in data


@pytest.mark.asyncio
async def test_register_duplicate_username(client: AsyncClient):
    """Test registration with duplicate username."""
    # First registration
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": "duplicate",
            "email": "first@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "First User"
        }
    )
    
    # Attempt duplicate registration
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "username": "duplicate",
            "email": "second@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "Second User"
        }
    )
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_register_duplicate_email(client: AsyncClient):
    """Test registration with duplicate email."""
    # First registration
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": "user1",
            "email": "duplicate@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "First User"
        }
    )
    
    # Attempt duplicate registration
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "username": "user2",
            "email": "duplicate@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "Second User"
        }
    )
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_register_weak_password(client: AsyncClient):
    """Test registration with weak password."""
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "username": "weakpass",
            "email": "weak@example.com",
            "password": "weak",
            "full_name": "Weak Password User"
        }
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_login_form_success(client: AsyncClient):
    """Test successful login with form data."""
    # Create user
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": "loginuser",
            "email": "login@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "Login User"
        }
    )
    
    # Login with form data
    response = await client.post(
        "/api/v1/auth/token",
        data={
            "username": "loginuser",
            "password": "StrongP@ssw0rd!"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_json_success(client: AsyncClient):
    """Test successful login with JSON."""
    # Create user
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": "jsonuser",
            "email": "json@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "JSON User"
        }
    )
    
    # Login with JSON
    response = await client.post(
        "/api/v1/auth/login",
        json={
            "username": "jsonuser",
            "password": "StrongP@ssw0rd!"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_with_email(client: AsyncClient):
    """Test login using email instead of username."""
    # Create user
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": "emaillogin",
            "email": "emaillogin@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "Email Login User"
        }
    )
    
    # Login with email
    response = await client.post(
        "/api/v1/auth/token",
        data={
            "username": "emaillogin@example.com",
            "password": "StrongP@ssw0rd!"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


@pytest.mark.asyncio
async def test_login_invalid_credentials(client: AsyncClient):
    """Test login with invalid credentials."""
    response = await client.post(
        "/api/v1/auth/token",
        data={
            "username": "nonexistent",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]


@pytest.mark.asyncio
async def test_login_wrong_password(client: AsyncClient):
    """Test login with wrong password."""
    # Create user
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": "wrongpass",
            "email": "wrongpass@example.com",
            "password": "CorrectP@ssw0rd!",
            "full_name": "Wrong Pass User"
        }
    )
    
    # Login with wrong password
    response = await client.post(
        "/api/v1/auth/token",
        data={
            "username": "wrongpass",
            "password": "WrongP@ssw0rd!"
        }
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_current_user(client: AsyncClient):
    """Test getting current user information."""
    # Create and login user
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": "currentuser",
            "email": "current@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "Current User"
        }
    )
    
    login_response = await client.post(
        "/api/v1/auth/token",
        data={
            "username": "currentuser",
            "password": "StrongP@ssw0rd!"
        }
    )
    token = login_response.json()["access_token"]
    
    # Get current user
    response = await client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "currentuser"
    assert data["email"] == "current@example.com"
    assert data["full_name"] == "Current User"


@pytest.mark.asyncio
async def test_get_current_user_invalid_token(client: AsyncClient):
    """Test getting current user with invalid token."""
    response = await client.get(
        "/api/v1/auth/me",
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_current_user_no_token(client: AsyncClient):
    """Test getting current user without token."""
    response = await client.get("/api/v1/auth/me")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_refresh_token(client: AsyncClient):
    """Test refreshing access token."""
    # Create and login user
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": "refreshuser",
            "email": "refresh@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "Refresh User"
        }
    )
    
    login_response = await client.post(
        "/api/v1/auth/token",
        data={
            "username": "refreshuser",
            "password": "StrongP@ssw0rd!"
        }
    )
    old_token = login_response.json()["access_token"]
    
    # Refresh token
    response = await client.post(
        "/api/v1/auth/refresh",
        headers={"Authorization": f"Bearer {old_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    # New token should be different
    assert data["access_token"] != old_token


@pytest.mark.asyncio
async def test_token_expiry(client: AsyncClient):
    """Test that expired tokens are rejected."""
    # Create an expired token
    expired_token = auth_service.create_access_token(
        data={"sub": "expireduser", "user_id": "123"},
        expires_delta=timedelta(seconds=-1)  # Already expired
    )
    
    response = await client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {expired_token}"}
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_case_insensitive_username_login(client: AsyncClient):
    """Test that username login is case-insensitive."""
    # Create user
    await client.post(
        "/api/v1/auth/register",
        json={
            "username": "CaseSensitive",
            "email": "case@example.com",
            "password": "StrongP@ssw0rd!",
            "full_name": "Case User"
        }
    )
    
    # Login with different case
    response = await client.post(
        "/api/v1/auth/token",
        data={
            "username": "casesensitive",  # lowercase
            "password": "StrongP@ssw0rd!"
        }
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_special_characters_in_password(client: AsyncClient):
    """Test registration and login with special characters in password."""
    special_password = "P@$$w0rd!#$%^&*()"
    
    # Register
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "username": "specialpass",
            "email": "special@example.com",
            "password": special_password,
            "full_name": "Special Pass User"
        }
    )
    assert response.status_code == 201
    
    # Login
    response = await client.post(
        "/api/v1/auth/token",
        data={
            "username": "specialpass",
            "password": special_password
        }
    )
    assert response.status_code == 200


# Import timedelta for the expired token test
from datetime import timedelta