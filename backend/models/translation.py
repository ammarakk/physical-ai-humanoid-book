from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import Optional
import uuid

Base = declarative_base()

class CachedTranslation(Base):
    __tablename__ = "cached_translations"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    source_text_hash = Column(String, nullable=False)
    source_language = Column(String, default='en', nullable=False)
    target_language = Column(String, nullable=False)
    translated_text = Column(Text, nullable=False)
    source_file = Column(String, nullable=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

    # Relationship
    user = relationship("User", back_populates="cached_translations")

class CachedTranslationBase(BaseModel):
    source_text_hash: str
    source_language: str = "en"
    target_language: str
    translated_text: str
    source_file: Optional[str] = None
    user_id: Optional[str] = None

class CachedTranslationCreate(CachedTranslationBase):
    pass

class CachedTranslationUpdate(BaseModel):
    translated_text: Optional[str] = None

class CachedTranslationResponse(CachedTranslationBase):
    id: str
    created_at: str

    class Config:
        from_attributes = True