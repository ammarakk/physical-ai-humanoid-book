import os
import sys
from pathlib import Path
import markdown
from sqlalchemy.orm import Session

# Add the backend directory to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.database import get_db, engine
from backend.models.book_content import BookContent, Base
from backend.ai.embeddings import qwen_embeddings
from backend.database.vector_db import vector_db


def create_tables():
    """Create database tables if they don't exist"""
    Base.metadata.create_all(bind=engine)


def read_markdown_files(docs_dir: str):
    """Recursively read all markdown files in the docs directory"""
    md_files = []
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md') or file.endswith('.mdx'):
                file_path = os.path.join(root, file)
                md_files.append(file_path)
    return md_files


def extract_content_from_file(file_path: str):
    """Extract content from a markdown file, removing frontmatter if present"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has frontmatter (starts with ---)
    if content.startswith('---'):
        # Find the end of frontmatter
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]  # Skip the frontmatter part
    
    # Convert markdown to plain text (optional - just extract text content)
    # Using markdown library to convert to HTML, then strip HTML tags
    html = markdown.markdown(content)
    # Simple regex to strip HTML tags
    import re
    plain_text = re.sub('<[^<]+?>', '', html)
    
    return plain_text.strip()


def process_book_content():
    """Process all book content and store in database with embeddings"""
    print("Starting book content processing...")
    
    # Create tables
    create_tables()
    
    # Get database session
    db_gen = get_db()
    db: Session = next(db_gen)
    
    try:
        # Get all markdown files
        docs_dir = "docs"
        md_files = read_markdown_files(docs_dir)
        
        print(f"Found {len(md_files)} markdown files to process")
        
        for file_path in md_files:
            print(f"Processing: {file_path}")
            
            try:
                # Extract content from the file
                content_text = extract_content_from_file(file_path)
                
                # Only process if content is substantial
                if len(content_text.strip()) < 10:
                    print(f"Skipping {file_path}, content too short")
                    continue
                
                # Create embedding for the content
                embedding = qwen_embeddings.get_embedding(content_text[:2000])  # Limit to first 2000 chars
                
                # Create BookContent object
                book_content = BookContent(
                    title=Path(file_path).stem,  # Use filename without extension as title
                    content=content_text,
                    source_path=file_path,
                    embedding_vector=str(embedding)  # Store as string for now
                )
                
                # Add to database
                db.add(book_content)
                
                # Add to vector database
                content_id = book_content.id  # This will be set after adding to DB
                vector_db.store_embedding(
                    content_id=content_id,
                    embedding=embedding,
                    content_metadata={
                        "title": book_content.title,
                        "content": book_content.content[:500],  # Store first 500 chars as preview
                        "source_path": book_content.source_path
                    }
                )
                
                print(f"Processed: {file_path}")
                
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")
                continue
        
        # Commit all changes to database
        db.commit()
        print("Book content processing completed successfully!")
        
    except Exception as e:
        print(f"Error during book content processing: {str(e)}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    process_book_content()