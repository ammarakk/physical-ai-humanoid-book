# Quickstart Guide: Book Platform UI, Chatbot, and Authentication System

## Prerequisites

- Node.js (v16 or higher)
- Python (v3.10 or higher)
- Git
- Access to Qwen embeddings API
- Access to Google Gemini API

## Initial Setup

### 1. Clone and Navigate to Repository
```bash
git clone <repository-url>
cd physical-ai-humanoid-book
```

### 2. Set up Frontend (Docusaurus)
```bash
# Install frontend dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys and configuration
```

### 3. Set up Backend (FastAPI)
```bash
# Navigate to backend directory (or create if separate)
# Create Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt] pydantic google-generativeai python-dotenv requests

# Set up environment variables for backend
cp .env.example .env
# Edit .env with your API keys and configuration
```

## Environment Variables

### Frontend (.env)
```
REACT_APP_GEMINI_API_KEY=your_google_gemini_api_key
REACT_APP_BACKEND_URL=http://localhost:8000
```

### Backend (.env)
```
SECRET_KEY=your-super-secret-key-for-jwt
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
QWEN_API_KEY=your-qwen-embeddings-api-key
GEMINI_API_KEY=your-google-gemini-api-key
DATABASE_URL=your-database-connection-string
```

## Running the Application

### 1. Start the Backend Server
```bash
cd backend  # if backend is in separate directory
uvicorn main:app --reload --port 8000
```

### 2. Start the Frontend (Docusaurus)
```bash
npm start
```

## Key Features and Usage

### 1. Landing Page with Animated Hero Section
- Visit the root URL to see the robotic-themed landing page
- The animated hero section will showcase the AI-powered book
- Use "Read the Book" to access book content
- Use "Open AI Chatbot" to access the chatbot

### 2. Authentication System
- Access signup/login at `/auth/signup` and `/auth/login`
- JWT-based authentication is used
- User information is stored securely

### 3. AI Chatbot
- Access the chatbot through the dedicated page or floating icon
- The chatbot uses RAG to answer questions based on book content
- Responses will include references to the book sections used

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout

### Chatbot
- `POST /api/chatbot/query` - Submit query to chatbot
- `GET /api/chatbot/conversations` - Get conversation history

### User Profile
- `GET /api/user/profile` - Get user profile
- `PUT /api/user/profile` - Update user profile

## Development

### Adding New Book Content
1. Add new markdown/MDX files to the `docs/` directory
2. Update `sidebars.js` to include the new content in navigation
3. The RAG system will automatically include new content after reprocessing

### Custom Components
- Add custom React components to `src/components/`
- Use MDX to embed interactive elements in documentation

### Theming
- Customize the robotic/AI theme in `src/css/custom.css`
- Update color scheme and styling as needed while maintaining the design language