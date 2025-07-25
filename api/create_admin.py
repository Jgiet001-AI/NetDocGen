#!/usr/bin/env python3
"""
Create an admin user for NetDocGen.

Usage: python create_admin.py
"""

import asyncio
import sys
from getpass import getpass

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import AsyncSessionLocal
from app.services.auth import auth_service
from app.schemas.user import UserCreate

async def create_admin_user():
    """Create an admin user interactively."""
    print("Create NetDocGen Admin User")
    print("-" * 30)
    
    # Get user input
    username = input("Username: ").strip()
    email = input("Email: ").strip()
    full_name = input("Full Name (optional): ").strip() or None
    
    # Get password with confirmation
    while True:
        password = getpass("Password: ")
        confirm_password = getpass("Confirm Password: ")
        
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue
            
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            continue
            
        break
    
    # Create user
    async with AsyncSessionLocal() as db:
        try:
            user_create = UserCreate(
                username=username,
                email=email,
                full_name=full_name,
                password=password
            )
            
            user = await auth_service.create_user(db, user_create)
            
            # Make user an admin
            user.is_admin = True
            await db.commit()
            
            print(f"\nAdmin user '{username}' created successfully!")
            print(f"User ID: {user.id}")
            
        except ValueError as e:
            print(f"\nError: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    asyncio.run(create_admin_user())