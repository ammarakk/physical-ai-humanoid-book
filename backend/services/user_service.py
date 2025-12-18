from sqlalchemy.orm import Session
from typing import Optional
from datetime import timedelta

from ..models.user import User, UserCreate
from ..utils.hash import hash_password, verify_password
from ..utils.token import create_access_token


class UserService:
    @staticmethod
    def create_user(db: Session, user_data: UserCreate) -> User:
        """
        Create a new user account
        """
        # Hash the password
        hashed_password = hash_password(user_data.password)
        
        # Create user instance
        db_user = User(
            email=user_data.email,
            password_hash=hashed_password,
            first_name=user_data.first_name,
            last_name=user_data.last_name
        )
        
        # Add to database
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return db_user
    
    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
        """
        Authenticate a user by email and password
        """
        # Find user by email
        user = db.query(User).filter(User.email == email).first()
        
        # Verify password if user exists
        if not user or not verify_password(password, user.password_hash):
            return None
        
        # Check if user is active
        if not user.is_active:
            return None
        
        return user
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """
        Retrieve a user by email
        """
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: str) -> Optional[User]:
        """
        Retrieve a user by ID
        """
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def generate_access_token(user_id: str) -> str:
        """
        Generate a JWT access token for the user
        """
        access_token_expires = timedelta(minutes=30)
        access_token = create_access_token(
            data={"user_id": user_id}, expires_delta=access_token_expires
        )
        return access_token
    
    @staticmethod
    def update_user_profile(
        db: Session, 
        user: User, 
        first_name: Optional[str] = None, 
        last_name: Optional[str] = None
    ) -> User:
        """
        Update user profile information
        """
        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        
        db.commit()
        db.refresh(user)
        
        return user