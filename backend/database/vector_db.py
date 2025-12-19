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
        # Get vector database URL and enabled status from environment variables
        self.enabled = os.getenv("VECTOR_DB_ENABLED", "true").lower() == "true"
        vector_db_url = os.getenv("VECTOR_DB_URL", "http://localhost:6333")

        if self.enabled:
            try:
                self.client = QdrantClient(url=vector_db_url)
                # Initialize the collection for book content
                self.collection_name = "book_content"
                self._init_collection()
            except Exception as e:
                logging.error(f"Vector DB connection failed: {e}. Running in disabled mode.")
                self.enabled = False
        else:
            logging.info("Vector DB is disabled via VECTOR_DB_ENABLED environment variable.")
            self.enabled = False

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
        if not self.enabled:
            logging.warning("Vector DB is disabled. Skipping store operation.")
            return False

        try:
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
            return True
        except Exception as e:
            logging.error(f"Error storing embedding: {e}")
            return False

    def search_similar(self, query_embedding: List[float], limit: int = 5) -> List[dict]:
        """
        Search for similar content based on the query embedding
        """
        if not self.enabled:
            logging.warning("Vector DB is disabled. Skipping search operation.")
            return []

        try:
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
        except Exception as e:
            logging.error(f"Error searching similar content: {e}")
            return []

    def delete_content(self, content_id: str):
        """
        Delete a content entry from the vector database
        """
        if not self.enabled:
            logging.warning("Vector DB is disabled. Skipping delete operation.")
            return False

        try:
            self.client.delete(
                collection_name=self.collection_name,
                points_selector=models.PointIdsList(
                    points=[content_id]
                )
            )
            return True
        except Exception as e:
            logging.error(f"Error deleting content: {e}")
            return False

    def update_content(self, content_id: str, embedding: List[float], content_metadata: dict):
        """
        Update a content entry in the vector database
        """
        if not self.enabled:
            logging.warning("Vector DB is disabled. Skipping update operation.")
            return False

        try:
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
            return True
        except Exception as e:
            logging.error(f"Error updating content: {e}")
            return False

    def get_content(self, content_id: str) -> Optional[dict]:
        """
        Get content by ID from the vector database
        """
        if not self.enabled:
            logging.warning("Vector DB is disabled. Skipping get operation.")
            return None

        try:
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
        except Exception as e:
            logging.error(f"Error getting content: {e}")
            return None

# Singleton instance
vector_db = VectorDB()