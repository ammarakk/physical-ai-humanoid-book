# API Contracts: Book Platform Backend API

## Authentication Endpoints

### POST /api/auth/register
**Description**: Register a new user account
**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Response (201 Created)**:
```json
{
  "message": "User registered successfully",
  "user": {
    "id": "uuid-string",
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe"
  }
}
```

**Response (400 Bad Request)**:
```json
{
  "error": "Email already exists" 
}
```

### POST /api/auth/login
**Description**: Authenticate user and return JWT token
**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (200 OK)**:
```json
{
  "access_token": "jwt-token-string",
  "token_type": "bearer",
  "user": {
    "id": "uuid-string",
    "email": "user@example.com",
    "first_name": "John"
  }
}
```

**Response (401 Unauthorized)**:
```json
{
  "error": "Invalid credentials"
}
```

### POST /api/auth/logout
**Description**: Revoke the current user's JWT token
**Headers**: `Authorization: Bearer {access_token}`
**Response (200 OK)**:
```json
{
  "message": "Successfully logged out"
}
```

## Chatbot Endpoints

### POST /api/chatbot/query
**Description**: Submit a query to the RAG-based chatbot
**Headers**: `Authorization: Bearer {access_token}` (optional)
**Request Body**:
```json
{
  "query": "What is Physical AI?",
  "conversation_id": "uuid-string" (optional, for maintaining context)
}
```

**Response (200 OK)**:
```json
{
  "response": "Physical AI combines embodied intelligence with robotics...",
  "conversation_id": "uuid-string",
  "sources": [
    {
      "title": "Chapter 1: Foundations",
      "path": "/docs/chapter1"
    }
  ]
}
```

### GET /api/chatbot/conversations
**Description**: Get user's chatbot conversation history
**Headers**: `Authorization: Bearer {access_token}`
**Response (200 OK)**:
```json
[
  {
    "id": "uuid-string",
    "title": "What is Physical AI?",
    "created_at": "2023-01-01T00:00:00Z",
    "message_count": 5
  }
]
```

## Book Content Endpoints

### GET /api/book/search
**Description**: Search book content by query
**Request Params**: `q` (search query)
**Response (200 OK)**:
```json
[
  {
    "id": "uuid-string",
    "title": "Chapter Title",
    "content_preview": "Preview of the content...",
    "source_path": "/docs/chapter-path"
  }
]
```

## User Profile Endpoints

### GET /api/user/profile
**Description**: Get current user profile information
**Headers**: `Authorization: Bearer {access_token}`
**Response (200 OK)**:
```json
{
  "id": "uuid-string",
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "created_at": "2023-01-01T00:00:00Z"
}
```

### PUT /api/user/profile
**Description**: Update user profile information
**Headers**: `Authorization: Bearer {access_token}`
**Request Body**:
```json
{
  "first_name": "Jane",
  "last_name": "Smith"
}
```

**Response (200 OK)**:
```json
{
  "id": "uuid-string",
  "email": "user@example.com",
  "first_name": "Jane",
  "last_name": "Smith",
  "updated_at": "2023-01-01T00:00:00Z"
}
```