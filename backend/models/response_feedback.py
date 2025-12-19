from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pydantic import BaseModel
from typing import Optional
import uuid

Base = declarative_base()

class ResponseFeedback(Base):
    __tablename__ = "response_feedback"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    chatbot_query_id = Column(String, ForeignKey("chatbot_queries.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=True)  # Optional - unauthenticated users can provide feedback
    feedback_type = Column(String, nullable=False)  # e.g., "helpful", "not-helpful", "incorrect"
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    chatbot_query = relationship("ChatbotQuery")
    user = relationship("User")

class ResponseFeedbackBase(BaseModel):
    chatbot_query_id: str
    feedback_type: str
    comment: Optional[str] = None
    user_id: Optional[str] = None

class ResponseFeedbackCreate(ResponseFeedbackBase):
    pass

class ResponseFeedbackResponse(BaseModel):
    id: str
    chatbot_query_id: str
    user_id: Optional[str] = None
    feedback_type: str
    comment: Optional[str] = None
    created_at: str

    class Config:
        from_attributes = True