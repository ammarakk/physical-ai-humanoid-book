# Environment Setup

This document explains how to set up the required environment variables for the Physical AI Humanoid Book Platform.

## Backend Environment Variables

Copy the `.env.example` file in the `backend` directory to create a `.env` file:

```bash
cd backend
cp .env.example .env
```

Then update the values in the `.env` file with your actual keys:

### JWT Configuration
- `SECRET_KEY`: A secret key for JWT tokens (use a strong random string)
- `JWT_SECRET_KEY`: A secret key for JWT (use the same as SECRET_KEY or a different one)

### AI Service API Keys
- `QWEN_API_KEY`: Your Qwen API key (get it from Alibaba Cloud)
- `GEMINI_API_KEY`: Your Google Gemini API key (get it from Google AI Studio)
- `HF_TOKEN`: Your Hugging Face API token (get it from Hugging Face)
- `HUGGING_FACE_API_KEY`: Alternative Hugging Face API key
- `EMBEDDINGS_API_KEY`: Alternative embeddings API key
- `OPENAI_API_KEY`: OpenAI API key (if using OpenAI models)
- `ANTHROPIC_API_KEY`: Anthropic API key (if using Claude models)
- `COHERE_API_KEY`: Cohere API key (if using Cohere models)

### Database Configuration
- `DATABASE_URL`: Database connection string (SQLite by default for local development)
- `MONGODB_URL`: MongoDB connection string (if using MongoDB)

### Vector Database Configuration
- `VECTOR_DB_URL`: Vector database URL (for Qdrant or other vector DB)
- `QDRANT_URL`: Qdrant vector database URL

### Translation Services
- `TRANSLATION_API_KEY`: Google Translate API key (optional)

### Caching & Session Storage
- `REDIS_URL`: Redis URL (for caching/session storage if using Redis)

### Email Services
- `SMTP_SERVER`: SMTP server address
- `SMTP_PORT`: SMTP server port
- `SMTP_USERNAME`: SMTP username
- `SMTP_PASSWORD`: SMTP password
- `EMAIL_FROM`: Email address for sending emails

### Other Configuration
- `ALLOWED_ORIGINS`: Comma-separated list of allowed origins for CORS
- `LOG_LEVEL`: Logging level (INFO, DEBUG, ERROR, etc.)
- `API_REQUEST_TIMEOUT`: Timeout for API requests
- `RATE_LIMIT_MAX_REQUESTS`: Max requests for rate limiting
- `RATE_LIMIT_WINDOW_SIZE`: Time window size for rate limiting

## Frontend Environment Variables

For the frontend (Docusaurus), copy the `.env.example` file at the project root:

```bash
cp .env.example .env
```

Update the values in the `.env` file if necessary:

### API Configuration
- `API_BASE_URL`: The URL of your backend API (default: http://localhost:8000)
- `NEXT_PUBLIC_API_BASE_URL`: Public URL of your backend API

### Frontend Feature Flags
- `NEXT_PUBLIC_ENABLE_TRANSLATION`: Whether translation is enabled
- `NEXT_PUBLIC_ENABLE_CHATBOT`: Whether chatbot is enabled
- `NEXT_PUBLIC_ENABLE_AUTH`: Whether authentication is enabled
- `NEXT_PUBLIC_SUPPORTED_LANGUAGES`: Supported languages (comma-separated)

### Frontend AI Service Keys
- `NEXT_PUBLIC_GEMINI_API_KEY`: Your Google Gemini API key (if needed on frontend)
- `NEXT_PUBLIC_OPENAI_API_KEY`: Your OpenAI API key (if needed on frontend)
- `NEXT_PUBLIC_ANTHROPIC_API_KEY`: Your Anthropic API key (if needed on frontend)
- `NEXT_PUBLIC_COHERE_API_KEY`: Your Cohere API key (if needed on frontend)
- `NEXT_PUBLIC_HF_TOKEN`: Your Hugging Face token (if needed on frontend)

### Frontend Configuration
- `NEXT_PUBLIC_APP_TITLE`: Title of the application
- `NEXT_PUBLIC_APP_DESCRIPTION`: Description of the application
- `NEXT_PUBLIC_DEFAULT_LANGUAGE`: Default language
- `NEXT_PUBLIC_THEME_COLOR_PRIMARY`: Primary theme color
- `NEXT_PUBLIC_THEME_COLOR_SECONDARY`: Secondary theme color
- `NEXT_PUBLIC_ROBOTIC_THEME`: Whether to use robotic theme
- `NEXT_PUBLIC_DARK_MODE`: Whether to use dark mode

## Required API Keys

You will need the following API keys to run the application:

1. **Google Gemini API Key**:
   - Go to [Google AI Studio](https://aistudio.google.com/)
   - Create an account and get an API key
   - Set this as `GEMINI_API_KEY` in your backend `.env` file

2. **Qwen API Key** (optional, if using Qwen embeddings):
   - Go to [Alibaba Cloud](https://www.alibabacloud.com/)
   - Get a Qwen API key for embeddings
   - Set this as `QWEN_API_KEY` in your backend `.env` file

3. **Hugging Face Token**:
   - Go to [Hugging Face](https://huggingface.co/)
   - Create an account and access your token
   - Set this as `HF_TOKEN` in your backend `.env` file

4. **Alternative Embeddings API Key** (for fallback):
   - Can be another Hugging Face token or a different embeddings service
   - Set this as `EMBEDDINGS_API_KEY` in your backend `.env` file

5. **Translation API Key** (for Google Translate):
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Enable the Translation API and get an API key
   - Set this as `TRANSLATION_API_KEY` in your backend `.env` file

## Optional API Keys

You might also want to set up the following API keys for extended functionality:

1. **OpenAI API Key**:
   - Go to [OpenAI Platform](https://platform.openai.com/)
   - Create an account and get an API key
   - Set this as `OPENAI_API_KEY` in your `.env` files

2. **Anthropic API Key**:
   - Go to [Anthropic Console](https://console.anthropic.com/)
   - Get an API key for Claude models
   - Set this as `ANTHROPIC_API_KEY` in your `.env` files

3. **Cohere API Key**:
   - Go to [Cohere Platform](https://dashboard.cohere.ai/)
   - Create an account and get an API key
   - Set this as `COHERE_API_KEY` in your `.env` files

4. **Google API Key** (for additional Google services):
   - Get from [Google Cloud Console](https://console.cloud.google.com/)
   - Set this as `GOOGLE_API_KEY` in your backend `.env` file

5. **Google Custom Search Engine ID**:
   - Get from [Google CSE](https://cse.google.com/)
   - Set this as `GOOGLE_CSE_ID` in your backend `.env` file

## Running with Environment Variables

Make sure to set up your environment variables before running the application:

### Backend
```bash
# In the backend directory
cd backend
pip install -r requirements.txt  # or requirements_local.txt as needed
uvicorn main:app --reload
```

### Frontend
```bash
# In the project root
npm install
npm start
```

## Notes

- Never commit your `.env` files to version control
- The `.env` files are git-ignored by default
- Use the `.env.example` files to see the required environment variables
- Be cautious when using API keys in frontend code as they will be visible to users
- Consider using proxy servers to hide API keys from frontend requests in production