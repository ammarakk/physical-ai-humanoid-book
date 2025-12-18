# Backend API for Physical AI Humanoid Book

This directory contains the backend API for the Physical AI Humanoid Book platform, built with FastAPI.

## Setup Instructions

### Prerequisites
- Python 3.10+
- Pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ammarakk/physical-ai-humanoid-book.git
   cd physical-ai-humanoid-book
   ```

2. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.env` file in the backend directory with the following content:
   ```env
   SECRET_KEY=your-super-secret-key-change-this-in-production
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   QWEN_API_KEY=your-qwen-api-key
   GEMINI_API_KEY=your-gemini-api-key
   DATABASE_URL=postgresql://user:password@localhost/dbname
   VECTOR_DB_URL=qdrant://localhost:6333
   ```

6. **Initialize the database and process book content:**
   ```bash
   python scripts/process_book_content.py
   ```

### Running the Server

To start the backend server:

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`.

### API Endpoints

- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Authenticate user and return JWT token
- `POST /api/auth/logout` - Logout user
- `GET /api/user/profile` - Get current user profile
- `PUT /api/user/profile` - Update user profile
- `POST /api/chatbot/query` - Submit a query to the RAG-based chatbot
- `GET /api/chatbot/conversations` - Get user's chatbot conversation history
- `GET /api/book/search` - Search book content by query

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs with Python 3.7+
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and ORM for Python
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and settings management
- [Google Generative AI SDK](https://cloud.google.com/vertex-ai/docs/generative-ai) - For interacting with Google's Gemini model
- [QDrant](https://qdrant.tech/) - Vector similarity search engine

## Security

- JWT-based authentication for API endpoints
- Passwords stored with bcrypt hashing
- Environment variables for sensitive data

## Deployment

For production deployment, consider:
- Using environment variables for configuration
- Setting up SSL for secure connections
- Implementing proper logging
- Using a production-grade database
- Adding monitoring and alerting