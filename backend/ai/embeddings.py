from typing import List
import os
import requests
import json
import logging

class QwenEmbeddings:
    def __init__(self):
        self.api_key = os.getenv("QWEN_API_KEY")
        self.base_url = "https://dashscope.aliyuncs.com/api/v1/services/embeddings/text-embedding"
        self.enabled = bool(self.api_key)

        if not self.api_key:
            logging.warning("QWEN_API_KEY environment variable is not set. Embeddings will use a fallback method.")

    def get_embedding(self, text: str) -> List[float]:
        """
        Get the embedding for a single text
        """
        if not self.enabled:
            # Fallback: create a simple hash-based embedding
            import hashlib
            text_hash = hashlib.md5(text.encode()).hexdigest()
            # Convert the hex hash to a list of floats as a simple embedding
            embedding = []
            for i in range(0, len(text_hash), 2):
                hex_pair = text_hash[i:i+2]
                # Convert hex to int, normalize to [-1, 1] range
                val = (int(hex_pair, 16) / 255.0) * 2 - 1
                embedding.append(val)

            # Ensure embedding is of correct size (truncate or pad to 384 for MiniLM)
            while len(embedding) < 384:
                embedding.append(0.0)
            embedding = embedding[:384]

            return embedding

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
            logging.warning(f"Error getting embedding from Qwen API: {response.status_code} - {response.text}")
            # Fallback to simple hash embedding
            import hashlib
            text_hash = hashlib.md5(text.encode()).hexdigest()
            embedding = []
            for i in range(0, len(text_hash), 2):
                hex_pair = text_hash[i:i+2]
                val = (int(hex_pair, 16) / 255.0) * 2 - 1
                embedding.append(val)

            while len(embedding) < 384:
                embedding.append(0.0)
            embedding = embedding[:384]

            return embedding

        result = response.json()

        # Extract the embedding from the response
        # The exact structure depends on the Qwen API response format
        try:
            embedding = result["output"]["embeddings"][0]["embedding"]
        except (KeyError, IndexError):
            logging.warning("Unexpected response format from Qwen API, using fallback embedding.")
            # Fallback to simple hash embedding
            import hashlib
            text_hash = hashlib.md5(text.encode()).hexdigest()
            embedding = []
            for i in range(0, len(text_hash), 2):
                hex_pair = text_hash[i:i+2]
                val = (int(hex_pair, 16) / 255.0) * 2 - 1
                embedding.append(val)

            while len(embedding) < 384:
                embedding.append(0.0)
            embedding = embedding[:384]

        return embedding

    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Get embeddings for a list of texts
        """
        if not self.enabled:
            # Fallback: create hash-based embeddings for each text
            embeddings = []
            for text in texts:
                embeddings.append(self.get_embedding(text))
            return embeddings

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
            logging.warning(f"Error getting embeddings from Qwen API: {response.status_code} - {response.text}")
            # Fallback to hash-based embeddings
            embeddings = []
            for text in texts:
                embeddings.append(self.get_embedding(text))
            return embeddings

        result = response.json()

        # Extract all embeddings from the response
        try:
            embeddings = [item["embedding"] for item in result["output"]["embeddings"]]
        except (KeyError, TypeError):
            logging.warning("Unexpected response format from Qwen API, using fallback embeddings.")
            # Fallback to hash-based embeddings
            embeddings = []
            for text in texts:
                embeddings.append(self.get_embedding(text))

        return embeddings

# Singleton instance
qwen_embeddings = QwenEmbeddings()