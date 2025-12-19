from pydantic import BaseModel
from typing import Optional, List

class ChatbotQueryRequest(BaseModel):
    query: str
    conversation_id: Optional[str] = None

class ChatbotQueryResponse(BaseModel):
    response: str
    conversation_id: str
    sources: Optional[List[dict]] = []

class ChatHistoryResponse(BaseModel):
    id: str
    title: str
    created_at: str
    message_count: int