from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pydantic import BaseModel
from typing import Optional
import uuid

Base = declarative_base()

class AuthenticationToken(Base):
    __tablename__ = "auth_tokens"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    token = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_revoked = Column(Boolean, default=False)

    # Relationship to user
    user = relationship("User")

class TokenBase(BaseModel):
    user_id: str
    token: str
    expires_at: str
    is_revoked: bool

class TokenCreate(BaseModel):
    user_id: str
    token: str
    expires_at: str

class TokenResponse(BaseModel):
    id: str
    user_id: str
    expires_at: str
    is_revoked: bool
    created_at: str

    class Config:
        from_attributes = True