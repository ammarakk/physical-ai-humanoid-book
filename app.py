"""
Hugging Face Space entry point
This file serves as the entry point for the Hugging Face Space deployment
"""
import os
from backend.main import app

# Set environment variables that are required
os.environ.setdefault('DATABASE_URL', 'sqlite:///./physical_ai_book.db')
os.environ.setdefault('QDRANT_URL', 'http://localhost:6333')

# The app variable is what Hugging Face Spaces will look for
# This is the main FastAPI application instance