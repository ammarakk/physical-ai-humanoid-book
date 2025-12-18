# Deploying to Your Hugging Face Space

This document provides instructions on how to deploy the Physical AI Humanoid Book Platform to your Hugging Face Space at https://huggingface.co/spaces/ammaraak/book

## Prerequisites

1. Hugging Face CLI installed:
   ```
   powershell -ExecutionPolicy ByPass -c "irm https://hf.co/cli/install.ps1 | iex"
   ```

2. A new API token (do not use the one previously exposed - regenerate it):
   - Go to https://huggingface.co/settings/tokens
   - Create a new token with write permissions

## Deployment Steps

### 1. Clone Your Space Repository

```bash
git clone https://huggingface.co/spaces/ammaraak/book
cd book
```

### 2. Copy Project Files

Copy all the files from this project directory to your cloned space directory:
- app.py
- Dockerfile
- README.md
- setup.py
- requirements.txt
- backend/ directory
- all other project files

### 3. Configure Environment Variables

In your Hugging Face Space settings, add the following secrets:

- `GEMINI_API_KEY`: Your Google Gemini API key
- `QWEN_API_KEY`: Your Qwen API key (optional)
- `HF_TOKEN`: Your Hugging Face API token
- `SECRET_KEY`: A secret key for JWT tokens
- `TRANSLATION_API_KEY`: Google Translate API key (optional)

### 4. Commit and Push Changes

```bash
git add .
git commit -m "Add Physical AI Humanoid Book Platform with AI chatbot"
git push
```

## Expected Behavior

Once deployed, your Hugging Face Space will:

1. Build using the provided Dockerfile
2. Install all required dependencies
3. Start the FastAPI backend on port 7860
4. Serve the AI-powered book platform with RAG capabilities

## Troubleshooting

If the deployment fails:

1. Check the build logs in your Space dashboard
2. Ensure all required environment variables are set as secrets
3. Verify that your API keys are valid and have the necessary permissions
4. Confirm that the Docker build completes without errors

## Updating the Space

To update your Space in the future:

1. Make changes to your local repository
2. Test the changes locally if possible
3. Commit and push the changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push
   ```

The Space will automatically rebuild with the new changes.

## Security Notes

- Never commit API keys directly to the repository
- Always use Hugging Face Space secrets for sensitive information
- The .gitignore file is configured to prevent accidental commits of .env files
- Regularly rotate your API keys for security