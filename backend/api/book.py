from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import logging

import sys
import os

from database import get_db
from models.book_content import BookContentResponse
from api.schemas import ChatbotQueryResponse
from middleware.auth import get_current_user
from models.user import User
from ai.embeddings import qwen_embeddings

# Use absolute import for vector_db since relative imports don't work when using uvicorn directly
from database.vector_db import vector_db

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/book", tags=["book"])

@router.get("/search", response_model=List[dict])
async def search_book_content(
    q: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Search book content by query
    """
    try:
        # Check if vector database is enabled
        if not vector_db.enabled:
            logger.warning("Vector DB is disabled. Cannot perform semantic search.")
            # Return an empty result when vector DB is disabled
            return []

        # Generate embedding for the search query
        query_embedding = qwen_embeddings.get_embedding(q)

        # Search for similar content in the vector database
        similar_contents = vector_db.search_similar(query_embedding, limit=5)

        # Format results
        results = []
        for content in similar_contents:
            metadata = content['metadata']
            results.append({
                "id": content['content_id'],
                "title": metadata['title'],
                "content_preview": metadata['content'][:200] + "..." if len(metadata['content']) > 200 else metadata['content'],
                "source_path": metadata['source_path']
            })

        logger.info(f"Book content search performed by user {current_user.email}")
        return results

    except Exception as e:
        logger.error(f"Error searching book content: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error searching book content"
        )