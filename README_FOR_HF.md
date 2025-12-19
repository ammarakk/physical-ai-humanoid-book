# Physical AI & Humanoid Robotics Book

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces)

This is an AI-powered technical publication about Physical AI and Humanoid Robotics, featuring a RAG-based chatbot that answers questions using book content.

## About This Project

This project combines a Docusaurus-based book platform with AI capabilities, featuring:
- Interactive book platform built with Docusaurus
- RAG-based chatbot that answers questions using book content
- Robotic/AI themed UI with dark mode and modern styling
- User authentication system for personalized experiences
- Support for multiple languages (English and Urdu)

## Architecture

The application consists of:
- **Frontend**: Docusaurus-based static site deployed on Hugging Face Spaces
- **Backend**: FastAPI server with RAG capabilities
- **AI Services**: Google Gemini for response generation
- **Embeddings**: Qwen or Hugging Face models for content indexing
- **Vector Database**: Qdrant for similarity search
- **Database**: SQLite for user data (PostgreSQL in production)

## Deployment on Hugging Face Spaces

This project is designed to run on Hugging Face Spaces using Docker. The application exposes a FastAPI backend that serves AI-powered features.

### Environment Variables Required

To run this application on Hugging Face Spaces, you need to configure the following environment variables:

- `GEMINI_API_KEY`: Your Google Gemini API key
- `QWEN_API_KEY`: Your Qwen API key (optional, for embeddings)
- `HF_TOKEN`: Your Hugging Face API token (for model access)
- `SECRET_KEY`: A secret key for JWT tokens
- `TRANSLATION_API_KEY`: Google Translate API key (optional)

### Local Setup

If you want to run this locally:

1. Clone this repository
2. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. Set up environment variables in a `.env` file
4. Run the backend:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
5. In another terminal, install and run the frontend:
   ```bash
   npm install
   npm start
   ```

## Features

- **AI Chatbot**: Ask questions about Physical AI and Humanoid Robotics and get answers based on book content
- **Content Search**: Search through the book content with semantic search
- **Multilingual Support**: Content available in English and Urdu
- **User Authentication**: Personalized experience with account creation
- **Responsive Design**: Works on desktop and mobile devices

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

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.