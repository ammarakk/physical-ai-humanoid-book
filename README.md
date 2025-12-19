# Physical AI & Humanoid Robotics Book

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/ammaraak/book)

This is an AI-powered technical publication about Physical AI and Humanoid Robotics, featuring a RAG-based chatbot that answers questions using book content. The project is deployed as a Hugging Face Space using Docker.

## About This Project

This project combines a Docusaurus-based book platform with AI capabilities, featuring:
- Interactive book platform built with Docusaurus
- RAG-based chatbot that answers questions using book content
- Robotic/AI themed UI with dark mode and modern styling
- User authentication system for personalized experiences
- Support for multiple languages (English and Urdu)

## Table of Contents
- [About This Project](#about-this-project)
- [Architecture](#architecture)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Architecture

The application consists of:
- **Frontend**: Docusaurus-based static site
- **Backend**: FastAPI server with RAG capabilities
- **AI Services**: Google Gemini for response generation
- **Embeddings**: Qwen or Hugging Face models for content indexing
- **Vector Database**: Qdrant for similarity search
- **Database**: SQLite for user data

## Features

- **AI Chatbot**: Ask questions about Physical AI and Humanoid Robotics and get answers based on book content
- **Content Search**: Search through the book content with semantic search
- **Multilingual Support**: Content available in English and Urdu
- **User Authentication**: Personalized experience with account creation
- **Responsive Design**: Works on desktop and mobile devices
- **Interactive Book Chapters**: Navigate through content organized in multiple parts and chapters

## Technology Stack

### Backend
- [FastAPI](https://fastapi.tiangolo.com/): Modern Python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/): Python SQL toolkit and ORM
- [Google Generative AI SDK](https://cloud.google.com/vertex-ai/docs/generative-ai): For Gemini integration
- [Qwen](https://github.com/QwenLM): For embedding generation
- [QDrant](https://qdrant.tech/): Vector database for similarity search

### Frontend
- [Docusaurus](https://docusaurus.io/): Static site generator for documentation
- [React](https://reactjs.org/): Component-based UI library
- [MDX](https://mdxjs.com/): JSX in Markdown files

## Installation

1. Clone this repository
```bash
git clone https://github.com/ammarakk/physical-ai-humanoid-book.git
cd physical-ai-humanoid-book
```

2. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Set up environment variables in a `.env` file

4. Install frontend dependencies:
```bash
cd ..
npm install
```

## Configuration

### Environment Variables

You need to create a `.env` file in the root backend directory with the following variables:

```env
# JWT Configuration
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# API Keys and Service Tokens
QWEN_API_KEY=your-qwen-api-key-here
GEMINI_API_KEY=your-gemini-api-key-here
HF_TOKEN=your-hf-token-here

# Alternative embedding service (Hugging Face API token)
HUGGING_FACE_API_KEY=your-huggingface-api-key-here

# Alternative embedding service (for fallback)
EMBEDDINGS_API_KEY=your-embeddings-api-key-here

# Database Configuration (using SQLite for local development)
DATABASE_URL=sqlite:///./physical_ai_book.db

# Vector Database Configuration
VECTOR_DB_URL=your-qdrant-url-here

# Translation API (Google Translate API)
TRANSLATION_API_KEY=your-translation-api-key

# Application Configuration
JWT_SECRET_KEY=your-super-secret-jwt-key-here
JWT_ALGORITHM=HS256

# Qdrant Vector Database Configuration
QDRANT_URL=your-qdrant-url-here
cluster-id=your-cluster-id-here
Endpoint=your-endpoint-here
qdrant-api-key=your-qdrant-api-key-here

# Feature flags
ENABLE_TRANSLATION=true
ENABLE_CHATBOT=true
ENABLE_RAG=true
ENABLE_AUTH=true
```

### Required Environment Variables

To run this application, you need to configure the following secrets:

- `GEMINI_API_KEY`: Your Google Gemini API key
- `QWEN_API_KEY`: Your Qwen API key (optional, for embeddings)
- `HF_TOKEN`: Your Hugging Face API token (for model access)
- `SECRET_KEY`: A secret key for JWT tokens
- `TRANSLATION_API_KEY`: Google Translate API key (optional)

## Usage

### Running Locally

1. Start the backend:
```bash
cd backend
python server.py
```

2. In another terminal, start the frontend:
```bash
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

### Using the Chatbot

Once the application is running, you can use the AI chatbot by:
1. Navigate to the chatbot page
2. Sign in or create an account
3. Ask questions about the Physical AI & Humanoid Robotics content
4. The chatbot will respond based on the book content using RAG (Retrieval Augmented Generation)

## Deployment

### Hugging Face Space Deployment

This application is containerized using Docker and deployed on Hugging Face Spaces. The entry point is defined in `app.py` which exposes a FastAPI application instance.

### GitHub Pages Deployment

The frontend is built with Docusaurus and can be deployed to GitHub Pages:

1. Build the site: `npm run build`
2. Deploy with `gh-pages`: `npx gh-pages -d build`

### Vercel Deployment

For Vercel deployment:
1. Import the repository in Vercel Dashboard
2. Set Build Command to `npm run build`
3. Set Output Directory to `build`
4. Add environment variables in Project Settings

### Docker Deployment

The application includes Dockerfiles for both frontend and backend:
- `Dockerfile` in the root directory for the frontend
- `backend/Dockerfile` for the backend

## Project Structure

```
physical-ai-humanoid-book/
├── backend/                # FastAPI backend
│   ├── api/                # API routes
│   ├── database/           # Database setup
│   ├── models/             # Database models
│   ├── services/           # Business logic
│   ├── utils/              # Utility functions
│   └── main.py             # FastAPI application entry point
├── docs/                   # Documentation files
├── src/                    # Docusaurus source files
│   ├── components/         # React components
│   ├── pages/              # Page components
│   └── theme/              # Theme customization
├── package.json            # Frontend dependencies
├── requirements.txt        # Backend dependencies
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Development Guidelines

- Follow the existing code style and conventions
- Write clear commit messages
- Document any new features or breaking changes
- Add tests for new functionality when possible

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors who worked on this project
- Inspired by advances in Physical AI and Humanoid Robotics research
- Powered by state-of-the-art AI models for enhanced learning experience

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository or contact the maintainers.