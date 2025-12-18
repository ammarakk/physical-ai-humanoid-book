from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import time
from typing import Dict, Any

# Import API routers
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api.auth import router as auth_router
from api.chatbot import router as chatbot_router
from api.book import router as book_router
from api.translation import router as translation_router
from middleware.rate_limit import RateLimitMiddleware, error_handler

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Physical AI Humanoid Book API",
    description="Backend API for the Physical AI Humanoid Book platform",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add rate limiting middleware
app.middleware("http")(RateLimitMiddleware(max_requests=100, window_size=3600).__call__)
app.middleware("http")(error_handler)

# Include API routes
app.include_router(auth_router)
app.include_router(chatbot_router)
app.include_router(book_router)
app.include_router(translation_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Physical AI Humanoid Book platform"}

@app.get("/health")
async def health_check():
    """Health check endpoint to verify the service is running"""
    # In a real application, you might want to check database connectivity, etc.
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "services": {
            "database": "connected",
            "vector_store": "connected",
            "llm_provider": "available"
        }
    }

@app.get("/config")
async def get_config():
    """Get public configuration details"""
    return {
        "supported_languages": ["en", "ur"],
        "max_query_length": 1000,
        "max_translation_length": 5000
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)