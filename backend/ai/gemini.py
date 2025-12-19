import os
import google.generativeai as genai
from typing import List, Optional

class GeminiInterface:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set")
        
        genai.configure(api_key=api_key)
        
        # Initialize the model
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """
        Generate a response using Google Gemini based on the prompt and optional context
        """
        # If context is provided, prepend it to the prompt
        if context:
            full_prompt = f"Context: {context}\n\nQuestion: {prompt}\n\nPlease provide an accurate response based only on the provided context. If the information is not available in the context, clearly state that."
        else:
            full_prompt = prompt
        
        try:
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            # In case of an error, return a helpful message
            return f"Sorry, I couldn't process your request at the moment. Error: {str(e)}"
    
    def generate_embeddings(self, text: str) -> List[float]:
        """
        Generate embeddings for a text using the embedding model
        """
        try:
            result = genai.embed_content(
                model="models/embedding-001",
                content=text,
                task_type="semantic_similarity"
            )
            return result['embedding']
        except Exception as e:
            raise Exception(f"Error generating embeddings: {str(e)}")

# Singleton instance
gemini_interface = GeminiInterface()