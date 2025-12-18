from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any
import logging
import os

import sys
import os
# Add the backend directory to the path to allow absolute imports
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from database import get_db
from models.user import User
from middleware.auth import get_current_user
from services.embedding_service import EmbeddingService
from utils.qdrant import qdrant_service
import google.generativeai as genai
from pydantic import BaseModel

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatQueryRequest(BaseModel):
    query: str
    language: str = "en"

class ChatQueryResponse(BaseModel):
    response: str
    retrieved_chunks: List[str]
    language: str

router = APIRouter(prefix="/api", tags=["chat"])

@router.post("/chat/query", response_model=ChatQueryResponse)
async def query_chatbot(
    chat_request: ChatQueryRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Query the RAG-based chatbot with strict content adherence
    """
    try:
        query = chat_request.query
        language = chat_request.language

        if not query:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Query parameter is required"
            )

        # Initialize embedding service
        embedding_service = EmbeddingService()

        # Retrieve relevant content using RAG
        relevant_chunks = qdrant_service.retrieve_relevant_content(
            query=query,
            embedding_service=embedding_service,
            top_k=5,
            language=language
        )

        # Generate response based on retrieved content
        if not relevant_chunks:
            # If no content found, return the specific message as required
            return ChatQueryResponse(
                response="This information is not available in the book.",
                retrieved_chunks=[],
                language=language
            )

        # Concatenate relevant content for context
        context = "\n\n".join([chunk["content"] for chunk in relevant_chunks])

        # Prepare the prompt for the LLM with strict instructions
        full_prompt = f"""
        You are an AI assistant for the Physical AI & Humanoid Robotics book.
        Answer the user's question based strictly on the following book content.
        Do not use external knowledge or fabricate information.

        Book Content:
        {context}

        User Question: {query}

        Answer: """

        # Use Google Gemini to generate response
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_ERROR,
                detail="GEMINI_API_KEY not configured"
            )

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')

        response = model.generate_content(full_prompt)
        response_text = response.text

        # Return the response with retrieved chunk IDs
        retrieved_chunk_ids = [chunk["id"] for chunk in relevant_chunks]

        return ChatQueryResponse(
            response=response_text,
            retrieved_chunks=retrieved_chunk_ids,
            language=language
        )

    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        logger.error(f"Error processing chatbot query: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error processing your request"
        )