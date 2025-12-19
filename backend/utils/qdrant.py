from typing import List, Dict, Any, Optional
import os
import logging
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import Distance, VectorParams, PointStruct
import uuid

# Get Qdrant URL from environment variables
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_ENABLED = os.getenv("QDRANT_ENABLED", "true").lower() == "true"

class QdrantService:
    def __init__(self):
        self.enabled = QDRANT_ENABLED
        if self.enabled:
            try:
                self.client = QdrantClient(url=QDRANT_URL)
                self.collection_name = "book_content_chunks"
                self.vector_size = 768  # For Qwen embeddings
                self.distance = Distance.COSINE
                # Create collection if it doesn't exist
                self._ensure_collection_exists()
            except Exception as e:
                logging.error(f"Qdrant connection failed: {e}. Running in disabled mode.")
                self.enabled = False
        else:
            logging.info("Qdrant is disabled via QDRANT_ENABLED environment variable.")
            self.enabled = False

    def _ensure_collection_exists(self):
        """Create the collection if it doesn't exist"""
        try:
            collections = self.client.get_collections()
            collection_names = [coll.name for coll in collections.collections]

            if self.collection_name not in collection_names:
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(size=self.vector_size, distance=self.distance)
                )
                logging.info(f"Created collection: {self.collection_name}")
            else:
                logging.info(f"Collection {self.collection_name} already exists")
        except Exception as e:
            logging.error(f"Error checking/creating collection: {e}")
            raise

    def store_chunk(self,
                    chunk_id: str,
                    content: str,
                    embedding: List[float],
                    metadata: Dict[str, Any]) -> bool:
        """Store a content chunk with its embedding in Qdrant"""
        if not self.enabled:
            logging.warning("Qdrant is disabled. Skipping store operation.")
            return False

        try:
            points = [PointStruct(
                id=chunk_id,
                vector=embedding,
                payload={
                    "content": content,
                    **metadata
                }
            )]

            self.client.upsert(
                collection_name=self.collection_name,
                points=points
            )
            return True
        except Exception as e:
            logging.error(f"Error storing chunk {chunk_id}: {e}")
            return False

    def search_chunks(self,
                      query_embedding: List[float],
                      limit: int = 5,
                      metadata_filter: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Search for similar content chunks based on embedding"""
        if not self.enabled:
            logging.warning("Qdrant is disabled. Skipping search operation.")
            return []

        try:
            # If there's a filter, convert it to Qdrant's filter format
            qdrant_filter = None
            if metadata_filter:
                conditions = []
                for key, value in metadata_filter.items():
                    conditions.append(models.FieldCondition(
                        key=f"payload.{key}",
                        match=models.MatchValue(value=value)
                    ))

                if conditions:
                    qdrant_filter = models.Filter(must=conditions)

            results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=limit,
                query_filter=qdrant_filter
            )

            return [
                {
                    "id": result.id,
                    "content": result.payload.get("content", ""),
                    "metadata": {k: v for k, v in result.payload.items() if k != "content"},
                    "score": result.score
                }
                for result in results
            ]
        except Exception as e:
            logging.error(f"Error searching chunks: {e}")
            return []

    def retrieve_relevant_content(self,
                                  query: str,
                                  embedding_service,
                                  top_k: int = 5,
                                  language: str = "en") -> List[Dict[str, Any]]:
        """Retrieve relevant content for RAG system based on query"""
        if not self.enabled:
            logging.warning("Qdrant is disabled. Skipping RAG operation.")
            # Return a response indicating that content isn't available when RAG is disabled
            return []

        try:
            # Generate embedding for the query
            query_embedding = embedding_service.generate_embedding(query)

            # First, try to retrieve content in the requested language
            metadata_filter = {"language": language} if language else None

            # Search for relevant chunks in the requested language
            results = self.search_chunks(
                query_embedding=query_embedding,
                limit=top_k,
                metadata_filter=metadata_filter
            )

            # If no results in the requested language and it's not English,
            # fall back to English content
            if not results and language != "en":
                logging.info(f"No content found in {language}, falling back to English")
                fallback_filter = {"language": "en"}
                results = self.search_chunks(
                    query_embedding=query_embedding,
                    limit=top_k,
                    metadata_filter=fallback_filter
                )

            return results
        except Exception as e:
            logging.error(f"Error retrieving relevant content: {e}")
            return []

    def retrieve_content_by_source(self, source_file: str) -> List[Dict[str, Any]]:
        """Retrieve all content chunks from a specific source file"""
        if not self.enabled:
            logging.warning("Qdrant is disabled. Skipping retrieve by source operation.")
            return []

        try:
            # Create a filter for the specific source file
            metadata_filter = {"source_file": source_file}

            # Create a scroll request to get all matching records
            results, _ = self.client.scroll(
                collection_name=self.collection_name,
                scroll_filter=models.Filter(
                    must=[models.FieldCondition(
                        key="payload.source_file",
                        match=models.MatchValue(value=source_file)
                    )]
                ),
                limit=1000  # Adjust as needed
            )

            return [
                {
                    "id": result.id,
                    "content": result.payload.get("content", ""),
                    "metadata": {k: v for k, v in result.payload.items() if k != "content"},
                }
                for result in results
            ]
        except Exception as e:
            logging.error(f"Error retrieving content by source: {e}")
            return []

    def delete_chunk(self, chunk_id: str) -> bool:
        """Delete a specific chunk from Qdrant"""
        if not self.enabled:
            logging.warning("Qdrant is disabled. Skipping delete operation.")
            return False

        try:
            self.client.delete(
                collection_name=self.collection_name,
                points_selector=[chunk_id]
            )
            return True
        except Exception as e:
            logging.error(f"Error deleting chunk {chunk_id}: {e}")
            return False

    def delete_collection(self):
        """Delete the entire collection (useful for reindexing)"""
        if not self.enabled:
            logging.warning("Qdrant is disabled. Skipping delete collection operation.")
            return False

        try:
            self.client.delete_collection(self.collection_name)
            # Recreate the collection
            self._ensure_collection_exists()
            return True
        except Exception as e:
            logging.error(f"Error deleting collection: {e}")
            return False

# Create a global instance
qdrant_service = QdrantService()