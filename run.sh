#!/bin/bash
# Setup script for Hugging Face Spaces

# Set default environment variables for Hugging Face Spaces
export DATABASE_URL=${DATABASE_URL:-"sqlite:///./physical_ai_book.db"}
export QDRANT_URL=${QDRANT_URL:-"http://localhost:6333"}
export API_PORT=${PORT:-7860}

# Create the database directory if it doesn't exist
mkdir -p /app/backend

# Run the application
cd /app/backend
exec uvicorn main:app --host 0.0.0.0 --port $API_PORT