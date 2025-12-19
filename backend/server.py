import os
import sys

# Add backend directory to path for imports
backend_dir = os.path.join(os.path.dirname(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Set environment variables to disable vector DBs
os.environ['QDRANT_ENABLED'] = 'false'
os.environ['VECTOR_DB_ENABLED'] = 'false'

def main():
    # Import after setting up environment
    from main import app
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

if __name__ == "__main__":
    main()