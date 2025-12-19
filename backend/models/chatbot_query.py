from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pydantic import BaseModel
from typing import Optional
import uuid

Base = declarative_base()

class ChatbotQuery(Base):
    __tablename__ = "chatbot_queries"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=True)  # Optional - unauthenticated users can query
    query_text = Column(Text, nullable=False)
    response_text = Column(Text, nullable=False)
    book_content_retrieved = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    model_used = Column(String, nullable=True)
    conversation_id = Column(String, nullable=True)  # To group related queries together

    # Relationship to user
    user = relationship("User")

class ChatbotQueryBase(BaseModel):
    query_text: str
    response_text: str
    book_content_retrieved: Optional[str] = None
    model_used: Optional[str] = None
    conversation_id: Optional[str] = None

class ChatbotQueryCreate(ChatbotQueryBase):
    user_id: Optional[str] = None

class ChatbotQueryResponse(BaseModel):
    id: str
    user_id: Optional[str] = None
    query_text: str
    response_text: str
    book_content_retrieved: Optional[str] = None
    created_at: str
    model_used: Optional[str] = None
    conversation_id: Optional[str] = None

    class Config:
        from_attributes = True