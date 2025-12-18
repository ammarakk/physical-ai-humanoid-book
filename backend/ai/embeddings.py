from typing import List
import os
import requests
import json

class QwenEmbeddings:
    def __init__(self):
        self.api_key = os.getenv("QWEN_API_KEY")
        self.base_url = "https://dashscope.aliyuncs.com/api/v1/services/embeddings/text-embedding"
        
        if not self.api_key:
            raise ValueError("QWEN_API_KEY environment variable is not set")
    
    def get_embedding(self, text: str) -> List[float]:
        """
        Get the embedding for a single text
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "text-embedding-v1",  # or whatever Qwen model you're using
            "input": {
                "texts": [text]
            }
        }
        
        response = requests.post(self.base_url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise Exception(f"Error getting embedding: {response.status_code} - {response.text}")
        
        result = response.json()
        
        # Extract the embedding from the response
        # The exact structure depends on the Qwen API response format
        embedding = result["output"]["embeddings"][0]["embedding"]
        
        return embedding
    
    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Get embeddings for a list of texts
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "text-embedding-v1",  # or whatever Qwen model you're using
            "input": {
                "texts": texts
            }
        }
        
        response = requests.post(self.base_url, headers=headers, json=payload)
        
        if response.status_code != 200:
            raise Exception(f"Error getting embeddings: {response.status_code} - {response.text}")
        
        result = response.json()
        
        # Extract all embeddings from the response
        embeddings = [item["embedding"] for item in result["output"]["embeddings"]]
        
        return embeddings

# Singleton instance
qwen_embeddings = QwenEmbeddings()