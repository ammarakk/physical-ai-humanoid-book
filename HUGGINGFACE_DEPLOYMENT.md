# Deploying Physical AI Humanoid Book to Hugging Face Spaces

This guide explains how to deploy the Physical AI Humanoid Book Platform to Hugging Face Spaces.

## Overview

The Physical AI Humanoid Book Platform is a full-stack application consisting of a Docusaurus frontend and FastAPI backend with AI capabilities. This document outlines how to deploy it on Hugging Face Spaces using Docker.

## Preparing Your Repository

1. Make sure all files are in order:
   - Backend code in the `backend/` directory
   - Frontend code in the root directory (Docusaurus)
   - Dockerfile for containerization
   - app.py for Hugging Face Spaces entry point
   - Requirements files for dependencies
   - Environment configuration

2. The repository is already structured for deployment with:
   - A Dockerfile that builds the application
   - An app.py entry point for Hugging Face Spaces
   - Requirements.txt for Python dependencies
   - Proper .gitignore file to exclude sensitive data

## Deployment Steps

### Option 1: Direct Deployment via Hugging Face UI

1. Create a new Space on Hugging Face:
   - Go to [Hugging Face Spaces](https://huggingface.co/new-space)
   - Choose "Docker" as SDK
   - Select "GPU" or "CPU" based on your needs
   - Fill in the title and description

2. Push your code to the Space repository:
   - Add the Hugging Face Space as a remote
   - Push your code to the repository

3. Add your secrets:
   - Go to your Space's settings
   - In the "Secrets" section, add the following environment variables:
     - `GEMINI_API_KEY`: Your Google Gemini API key
     - `QWEN_API_KEY`: Your Qwen API key (optional)
     - `HF_TOKEN`: Your Hugging Face API token
     - `SECRET_KEY`: Your secret key for JWT tokens
     - `TRANSLATION_API_KEY`: Google Translate API key (optional)

4. The Space will automatically build using the Dockerfile and start the application.

### Option 2: Using the Hugging Face CLI

1. Install the Hugging Face Hub CLI:
   ```bash
   pip install huggingface_hub
   ```

2. Login to your Hugging Face account:
   ```bash
   huggingface-cli login
   ```

3. Create a new Space:
   ```bash
   huggingface-cli space create --repo-id <your-username/your-space-name> --sdk docker --hardware cpu --token <your-hf-token>
   ```

4. Upload your files:
   ```bash
   huggingface-cli upload <your-username/your-space-name> . . --repo-type space
   ```

## Configuration Notes

1. **Port Configuration**: The application is configured to run on port 7860, which is the standard for Hugging Face Spaces.

2. **Environment Variables**: The application is designed to use environment variables for configuration. These can be set as secrets in the Hugging Face Space settings.

3. **Database**: The application uses SQLite by default, which works well in Hugging Face Spaces for small-scale use. For production use, consider using PostgreSQL.

4. **AI Services**: The application integrates with Google Gemini for response generation and supports Qwen for embeddings. Make sure to provide the appropriate API keys.

## Security Considerations

1. Never commit API keys or sensitive information to the repository.
2. Use Hugging Face Space secrets to store sensitive information.
3. The `.env` files are properly ignored by the `.gitignore` file.
4. The frontend does not expose sensitive API keys directly.

## Customization

To customize the application for your use case:

1. Modify the book content in the `docs/` directory
2. Update the styling in `src/css/custom.css`
3. Add your own environment variables as needed
4. Update the `docusaurus.config.js` to change the site configuration

## Troubleshooting

1. **Build Issues**: Check the build logs in your Hugging Face Space dashboard to identify issues during the build process.

2. **Runtime Issues**: Check the runtime logs in your Hugging Face Space dashboard to identify issues during application execution.

3. **API Keys**: Ensure all required API keys are correctly set as secrets in your Space settings.

4. **Port Issues**: The application defaults to port 7860, which should work in Hugging Face Spaces.

## Scaling Considerations

For heavy usage:

1. Consider upgrading to a GPU-equipped Space if you're using larger AI models
2. The application is designed to be stateless and horizontally scalable
3. For production use, consider using PostgreSQL instead of SQLite for better concurrency

## Support

For questions about deployment, consult the [Hugging Face documentation](https://huggingface.co/docs/hub/spaces) or open an issue in the repository.