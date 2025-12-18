from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from collections import defaultdict
from datetime import datetime, timedelta
import time
import logging
from typing import Dict

# In-memory storage for rate limiting (in production, use Redis or similar)
request_counts: Dict[str, list] = defaultdict(list)

class RateLimitMiddleware:
    def __init__(self, max_requests: int = 100, window_size: int = 3600):  # 100 requests per hour
        self.max_requests = max_requests
        self.window_size = window_size

    async def __call__(self, request: Request, call_next):
        # Get client IP
        client_ip = request.client.host
        
        # Clean old requests outside the window
        now = time.time()
        request_counts[client_ip] = [
            req_time for req_time in request_counts[client_ip] 
            if now - req_time < self.window_size
        ]
        
        # Check if rate limit exceeded
        if len(request_counts[client_ip]) >= self.max_requests:
            return JSONResponse(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                content={"detail": "Rate limit exceeded"}
            )
        
        # Add current request
        request_counts[client_ip].append(now)
        
        response = await call_next(request)
        return response

# Error handling middleware
async def error_handler(request: Request, call_next):
    try:
        response = await call_next(request)
    except HTTPException as exc:
        # Already handled HTTPException
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )
    except Exception as exc:
        # Log the error
        logging.error(f"Internal server error: {str(exc)}", exc_info=True)
        
        # Return generic 500 error
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Internal server error"}
        )
    
    return response