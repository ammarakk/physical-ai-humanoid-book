from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from pydantic import BaseModel
from typing import Optional, List
import uuid

Base = declarative_base()

class BookContent(Base):
    __tablename__ = "book_content"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    source_path = Column(String, nullable=False)  # Path to the original document
    embedding_vector = Column(String, nullable=True)  # Store as JSON string representation
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

class BookContentBase(BaseModel):
    title: str
    content: str
    source_path: str
    embedding_vector: Optional[str] = None

class BookContentCreate(BookContentBase):
    pass

class BookContentUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    source_path: Optional[str] = None
    embedding_vector: Optional[str] = None

class BookContentResponse(BaseModel):
    id: str
    title: str
    source_path: str
    created_at: str
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True