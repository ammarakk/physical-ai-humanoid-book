import os
import requests
from typing import List
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmbeddingService:
    def __init__(self):
        # Check for Qwen embeddings API key first, fall back to Google Gemini
        self.qwen_api_key = os.getenv("EMBEDDINGS_API_KEY")
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        
        if not self.qwen_api_key and not self.gemini_api_key:
            raise ValueError("Either EMBEDDINGS_API_KEY or GEMINI_API_KEY environment variable must be set")
        
        self.use_qwen = bool(self.qwen_api_key)
        self.base_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
        
    def generate_embedding(self, text: str) -> List[float]:
        """
        Generate an embedding for the given text
        """
        try:
            if self.use_qwen:
                # For now, using a Hugging Face model as a placeholder for Qwen embeddings
                # In a real implementation, this would call the Qwen API
                headers = {"Authorization": f"Bearer {self.qwen_api_key}"}
                response = requests.post(
                    self.base_url,
                    headers=headers,
                    json={"inputs": text, "options": {"wait_for_model": True}}
                )
                
                if response.status_code == 200:
                    embedding = response.json()
                    # The API might return a nested list, so we flatten if needed
                    if isinstance(embedding[0], list):
                        return embedding[0]
                    return embedding
                else:
                    # If Qwen API fails, fall back to a simple approach
                    logger.warning(f"Qwen API failed with status {response.status_code}, using fallback")
            
            # Fallback to a simple embedding approach if Qwen doesn't work
            # In a real implementation, we might use a local model or different API
            # For now, return a dummy embedding of appropriate size (384 for MiniLM)
            import hashlib
            text_hash = hashlib.md5(text.encode()).hexdigest()
            # Convert the hex hash to a list of floats as a simple embedding
            embedding = []
            for i in range(0, len(text_hash), 2):
                hex_pair = text_hash[i:i+2]
                # Convert hex to int, normalize to [-1, 1] range
                val = (int(hex_pair, 16) / 255.0) * 2 - 1
                embedding.append(val)
            
            # Ensure embedding is of correct size (truncate or pad)
            while len(embedding) < 384:
                embedding.append(0.0)
            embedding = embedding[:384]
            
            return embedding
        except Exception as e:
            logger.error(f"Error generating embedding for text: {str(e)}")
            # Return a zero vector as fallback
            return [0.0] * 384
    
    def generate_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a batch of texts
        """
        embeddings = []
        for text in texts:
            embedding = self.generate_embedding(text)
            embeddings.append(embedding)
        return embeddings