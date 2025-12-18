import os
import glob
from typing import List, Dict, Any
from pathlib import Path
import logging
from sqlalchemy.orm import Session

from ..models.book_content_chunk import BookContentChunk, BookContentChunkCreate
from ..utils.qdrant import qdrant_service
from ..services.embedding_service import EmbeddingService

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RagIngestionService:
    def __init__(self, db: Session):
        self.db = db
        self.embedding_service = EmbeddingService()
        
    def parse_docusaurus_markdown_files(self, base_path: str = "docs/") -> List[Dict[str, Any]]:
        """
        Parse all Docusaurus markdown files from the specified base path
        """
        markdown_files = []
        
        # Find all markdown files in the documentation directory
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.endswith('.md') or file.endswith('.mdx'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Extract title from the markdown content
                        title = self._extract_title(content)
                        
                        markdown_files.append({
                            'source_file': file_path,
                            'section_title': title,
                            'content': content,
                            'language': 'en'  # Default language
                        })
        
        logger.info(f"Found {len(markdown_files)} markdown files to process")
        return markdown_files
    
    def _extract_title(self, content: str) -> str:
        """
        Extract the title from markdown content (look for # Title pattern)
        """
        lines = content.split('\n')
        for line in lines:
            if line.strip().startswith('# '):
                return line.strip()[2:]  # Remove '# ' prefix
        return "Untitled"
    
    def chunk_content(self, content: str, max_chunk_size: int = 1000, overlap: int = 100) -> List[Dict[str, Any]]:
        """
        Chunk content with overlap and metadata
        """
        chunks = []
        
        # Remove markdown headers from the content to avoid duplication
        lines = content.split('\n')
        cleaned_lines = []
        for line in lines:
            if not line.strip().startswith('#'):
                cleaned_lines.append(line)
            else:
                # If it's a header, add it to the next relevant content block
                continue
        
        cleaned_content = '\n'.join(cleaned_lines)
        
        # Break content into chunks
        start = 0
        chunk_index = 0
        
        while start < len(cleaned_content):
            end = start + max_chunk_size
            
            # If we're not at the end, try to break at a sentence boundary
            if end < len(cleaned_content):
                # Find the last sentence ending before the max_chunk_size
                temp_end = end
                while temp_end > start and cleaned_content[temp_end] not in '.!?':
                    temp_end -= 1
                
                # If we couldn't find a good break point, just break at max_chunk_size
                if temp_end == start:
                    end = start + max_chunk_size
                else:
                    end = temp_end + 1  # Include the sentence ending
            
            chunk_text = cleaned_content[start:end].strip()
            
            if chunk_text:  # Only add non-empty chunks
                chunks.append({
                    'content': chunk_text,
                    'chunk_index': chunk_index
                })
                chunk_index += 1
            
            # Move start position, with overlap if possible
            start = end - overlap if end - overlap > start else end
            
            # Prevent infinite loop if we can't advance
            if start >= len(cleaned_content):
                break
        
        logger.info(f"Content chunked into {len(chunks)} pieces")
        return chunks
    
    def process_document(self, document_data: Dict[str, Any], max_chunk_size: int = 1000, overlap: int = 100):
        """
        Process a single document: chunk it, generate embeddings, and store in DB and vector store
        """
        logger.info(f"Processing document: {document_data['source_file']}")
        
        # Chunk the content
        content_chunks = self.chunk_content(document_data['content'], max_chunk_size, overlap)
        
        for i, chunk in enumerate(content_chunks):
            # Create the chunk entry in the database
            chunk_db = BookContentChunk(
                source_file=document_data['source_file'],
                section_title=document_data['section_title'],
                content=chunk['content'],
                language=document_data['language'],
                chunk_index=chunk['chunk_index'],
                content_metadata={
                    'original_title': document_data['section_title'],
                    'file_path': document_data['source_file'],
                    'chunk_total': len(content_chunks)
                }
            )
            
            # Add to database
            self.db.add(chunk_db)
            self.db.commit()
            self.db.refresh(chunk_db)
            
            # Generate embedding for the chunk
            try:
                embedding = self.embedding_service.generate_embedding(chunk['content'])
                
                # Store in Qdrant vector store
                success = qdrant_service.store_chunk(
                    chunk_id=chunk_db.id,
                    content=chunk['content'],
                    embedding=embedding,
                    metadata={
                        'source_file': document_data['source_file'],
                        'section_title': document_data['section_title'],
                        'language': document_data['language'],
                        'chunk_index': chunk['chunk_index']
                    }
                )
                
                if success:
                    logger.info(f"Successfully stored chunk {chunk_db.id} in vector store")
                else:
                    logger.error(f"Failed to store chunk {chunk_db.id} in vector store")
                    
            except Exception as e:
                logger.error(f"Error processing embedding for chunk {chunk_db.id}: {str(e)}")
    
    def ingest_all_documents(self, base_path: str = "docs/"):
        """
        Main method to ingest all documents: parse, chunk, embed, and store
        """
        logger.info(f"Starting RAG ingestion from base path: {base_path}")
        
        # Parse all markdown files
        documents = self.parse_docusaurus_markdown_files(base_path)
        
        # Process each document
        for doc_data in documents:
            try:
                self.process_document(doc_data)
            except Exception as e:
                logger.error(f"Error processing document {doc_data['source_file']}: {str(e)}")
                continue  # Continue with the next document even if one fails
        
        logger.info("RAG ingestion completed")