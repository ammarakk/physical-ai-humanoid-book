from sqlalchemy import Column, String, DateTime, Text, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from pydantic import BaseModel
from typing import Optional
import uuid

Base = declarative_base()

class BookContentChunk(Base):
    __tablename__ = "book_content_chunks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    source_file = Column(String, nullable=False)  # path to source markdown file
    section_title = Column(String, nullable=False)  # title of the section
    content = Column(Text, nullable=False)  # chunked content
    language = Column(String, default='en', nullable=False)  # default: 'en'
    chunk_index = Column(Integer, nullable=False)  # order of chunk in document
    content_metadata = Column(JSON)  # additional metadata like tags, categories
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

class BookContentChunkBase(BaseModel):
    source_file: str
    section_title: str
    content: str
    language: str = "en"
    chunk_index: int
    content_metadata: Optional[dict] = None

class BookContentChunkCreate(BookContentChunkBase):
    pass

class BookContentChunkUpdate(BaseModel):
    section_title: Optional[str] = None
    content: Optional[str] = None
    language: Optional[str] = None
    chunk_index: Optional[int] = None
    content_metadata: Optional[dict] = None

class BookContentChunkResponse(BaseModel):
    id: str
    source_file: str
    section_title: str
    content: str
    language: str
    chunk_index: int
    content_metadata: Optional[dict] = None
    created_at: str
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True