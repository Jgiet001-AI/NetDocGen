from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from app.config import settings
from app.models.user import User
from app.schemas.user import UserCreate, TokenData

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    """Authentication service for user management and JWT handling."""
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify a password against a hash."""
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password."""
        return pwd_context.hash(password)
    
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """Create a JWT access token."""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def decode_token(token: str) -> TokenData:
        """Decode and validate a JWT token."""
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            username: str = payload.get("sub")
            user_id: str = payload.get("user_id")
            
            if username is None:
                raise JWTError("Invalid token")
                
            return TokenData(username=username, user_id=user_id)
        except JWTError:
            raise
    
    async def authenticate_user(self, db: AsyncSession, username: str, password: str) -> Optional[User]:
        """Authenticate a user by username and password."""
        # Query user by username or email
        stmt = select(User).where(
            (User.username == username) | (User.email == username)
        )
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()
        
        if not user:
            return None
            
        if not self.verify_password(password, user.hashed_password):
            return None
            
        return user
    
    async def create_user(self, db: AsyncSession, user_create: UserCreate) -> User:
        """Create a new user."""
        # Check if user exists
        stmt = select(User).where(
            (User.username == user_create.username) | (User.email == user_create.email)
        )
        result = await db.execute(stmt)
        if result.scalar_one_or_none():
            raise ValueError("User with this username or email already exists")
        
        # Create new user
        hashed_password = self.hash_password(user_create.password)
        user = User(
            username=user_create.username,
            email=user_create.email,
            full_name=user_create.full_name,
            hashed_password=hashed_password
        )
        
        db.add(user)
        await db.commit()
        await db.refresh(user)
        
        return user
    
    async def get_user_by_id(self, db: AsyncSession, user_id: UUID) -> Optional[User]:
        """Get a user by ID."""
        stmt = select(User).where(User.id == user_id)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_user_by_username(self, db: AsyncSession, username: str) -> Optional[User]:
        """Get a user by username."""
        stmt = select(User).where(User.username == username)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

# Global auth service instance
auth_service = AuthService()