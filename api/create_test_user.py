#!/usr/bin/env python3
"""Create a test user for development."""
import asyncio
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from app.models.user import User
from app.services.auth import AuthService
from app.config import settings
import uuid

def create_test_user():
    # Use sync engine for this script
    db_url = settings.DATABASE_URL.replace('+asyncpg', '')
    engine = create_engine(db_url, echo=True)
    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        # Check if user exists
        result = session.execute(
            select(User).where(User.username == "testuser")
        )
        existing_user = result.scalar_one_or_none()
        
        if existing_user:
            print("User already exists. Updating password...")
            existing_user.hashed_password = AuthService.hash_password("testpass123")
            session.commit()
            print(f"Updated user: {existing_user.username}")
        else:
            # Create new user
            user = User(
                id=uuid.uuid4(),
                username="testuser",
                email="testuser@example.com",
                full_name="Test User",
                hashed_password=AuthService.hash_password("testpass123"),
                is_active=True,
                is_admin=False
            )
            session.add(user)
            session.commit()
            print(f"Created user: {user.username}")
    
    engine.dispose()

if __name__ == "__main__":
    create_test_user()