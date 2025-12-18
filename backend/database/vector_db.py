from typing import List, Optional
import numpy as np
import json
import os
import logging
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import Distance, VectorParams

class VectorDB:
    def __init__(self):
        # Get vector database URL from environment variables
        vector_db_url = os.getenv("VECTOR_DB_URL", "http://localhost:6333")

        # Try to connect to a remote server first, fall back to in-memory if unavailable
        try:
            self.client = QdrantClient(url=vector_db_url)
            # Test connection
            self.client.get_collections()
            logging.info("Connected to Qdrant server at: %s", vector_db_url)
        except Exception as e:
            logging.warning(f"Could not connect to Qdrant server at {vector_db_url}: {e}")
            logging.info("Falling back to in-memory Qdrant instance")
            # Use in-memory client as fallback
            self.client = QdrantClient(":memory:")

        # Initialize the collection for book content
        self.collection_name = "book_content"
        self._init_collection()
    
    def _init_collection(self):
        """
        Initialize the Qdrant collection for storing book content embeddings
        """
        try:
            # Try to get the collection info
            self.client.get_collection(self.collection_name)
        except:
            # If collection doesn't exist, create it
            # Note: This assumes embeddings of size 768 (typical for many embedding models)
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=768, distance=Distance.COSINE),
            )
    
    def store_embedding(self, content_id: str, embedding: List[float], content_metadata: dict):
        """
        Store an embedding with its metadata in the vector database
        """
        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                models.PointStruct(
                    id=content_id,
                    vector=embedding,
                    payload={
                        "content_id": content_id,
                        "metadata": content_metadata
                    }
                )
            ]
        )
    
    def search_similar(self, query_embedding: List[float], limit: int = 5) -> List[dict]:
        """
        Search for similar content based on the query embedding
        """
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=limit
        )
        
        results = []
        for hit in search_result:
            results.append({
                "content_id": hit.payload["content_id"],
                "metadata": hit.payload["metadata"],
                "score": hit.score
            })
        
        return results
    
    def delete_content(self, content_id: str):
        """
        Delete a content entry from the vector database
        """
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=models.PointIdsList(
                points=[content_id]
            )
        )
    
    def update_content(self, content_id: str, embedding: List[float], content_metadata: dict):
        """
        Update a content entry in the vector database
        """
        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                models.PointStruct(
                    id=content_id,
                    vector=embedding,
                    payload={
                        "content_id": content_id,
                        "metadata": content_metadata
                    }
                )
            ]
        )
    
    def get_content(self, content_id: str) -> Optional[dict]:
        """
        Get content by ID from the vector database
        """
        points = self.client.retrieve(
            collection_name=self.collection_name,
            ids=[content_id]
        )
        
        if points:
            point = points[0]
            return {
                "content_id": point.payload["content_id"],
                "metadata": point.payload["metadata"],
                "vector": point.vector
            }
        
        return None

# Singleton instance
vector_db = VectorDB()