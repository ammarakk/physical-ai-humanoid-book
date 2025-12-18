# Data Model: Book Platform UI, Chatbot, and Authentication System

## Entities

### User
- **Description**: Represents a registered user of the platform
- **Fields**:
  - id: UUID (Primary Key)
  - email: String (Unique, Valid email format)
  - password_hash: String (Securely hashed password)
  - first_name: String (Optional)
  - last_name: String (Optional)
  - created_at: DateTime (Timestamp when account was created)
  - updated_at: DateTime (Timestamp when account was last updated)
  - is_active: Boolean (Indicates if account is active)
- **Validation**:
  - Email must be unique and in valid format
  - Password must meet security requirements (minimum length, complexity)
- **Relationships**:
  - One-to-many with ChatbotQueries (optional, if tracking query history)

### AuthenticationToken (JWT)
- **Description**: Represents a JWT authentication token for a user
- **Fields**:
  - user_id: UUID (Foreign Key to User)
  - token: String (JWT token string)
  - expires_at: DateTime (Expiration time)
  - created_at: DateTime (Timestamp when token was issued)
  - is_revoked: Boolean (Whether the token has been revoked)
- **Validation**:
  - Token must be a valid JWT format
  - Must not be expired
  - Must not be revoked
- **Relationships**:
  - Belongs to User

### ChatbotQuery
- **Description**: Represents a user's question to the AI chatbot
- **Fields**:
  - id: UUID (Primary Key)
  - user_id: UUID (Foreign Key to User, optional if unauthenticated)
  - query_text: String (The user's question)
  - response_text: String (The AI's response)
  - book_content_retrieved: String (Relevant book content retrieved by RAG)
  - created_at: DateTime (Timestamp when query was made)
  - model_used: String (Which AI model was used)
  - conversation_id: UUID (To group related queries together)
- **Validation**:
  - query_text must not be empty
  - response_text must not be empty
- **Relationships**:
  - Belongs to User (optional)
  - One-to-many with ResponseFeedback (optional)

### BookContent
- **Description**: Represents content from the book used for RAG system
- **Fields**:
  - id: UUID (Primary Key)
  - title: String (Title of the content section)
  - content: String (The actual content text)
  - source_path: String (Path to the original document)
  - embedding_vector: Array<Float> (Vector representation of the content)
  - created_at: DateTime (Timestamp when content was processed)
  - updated_at: DateTime (Timestamp when content was last updated)
- **Validation**:
  - content must not be empty
  - embedding_vector must be valid
- **Relationships**:
  - Many-to-many with ChatbotQuery (via intermediate table, when content was used in a query)

### ResponseFeedback
- **Description**: Represents user feedback on chatbot responses
- **Fields**:
  - id: UUID (Primary Key)
  - chatbot_query_id: UUID (Foreign Key to ChatbotQuery)
  - user_id: UUID (Foreign Key to User, optional if unauthenticated)
  - feedback_type: String (e.g., "helpful", "not-helpful", "incorrect")
  - comment: String (Optional textual feedback)
  - created_at: DateTime (Timestamp when feedback was submitted)
- **Validation**:
  - feedback_type must be one of the allowed values
- **Relationships**:
  - Belongs to ChatbotQuery
  - Belongs to User (optional)

## State Transitions

### User Authentication States
- Unauthenticated → Pending Registration → Registered → Active → Inactive
- Unauthenticated → Authenticated (with JWT)
- Authenticated → Session Expired → Unauthenticated

### Query Processing States
- Received → Processing (RAG retrieval) → Response Generated → Response Delivered