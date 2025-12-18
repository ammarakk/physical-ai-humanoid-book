from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import logging
import os
from typing import Optional

import sys
import os
# Add the backend directory to the path to allow absolute imports
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from database import get_db
from models.user import User
from models.translation import CachedTranslation, CachedTranslationCreate
from middleware.auth import get_current_user
from pydantic import BaseModel
import requests
import hashlib

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TranslationRequest(BaseModel):
    text: str
    source_language: str = "en"
    target_language: str = "ur"

class TranslationResponse(BaseModel):
    translated_text: str
    source_language: str
    target_language: str

router = APIRouter(prefix="/api", tags=["translation"])

@router.post("/translate", response_model=TranslationResponse)
async def translate_text(
    request: TranslationRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Translate content from one language to another with caching
    """
    try:
        # Validate language pair
        supported_languages = ["en", "ur"]
        if request.source_language not in supported_languages or request.target_language not in supported_languages:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unsupported language pair: {request.source_language} to {request.target_language}. Supported: en, ur"
            )

        # Generate a hash of the source text for caching
        text_hash = hashlib.md5(f"{request.text}_{request.source_language}_{request.target_language}".encode()).hexdigest()

        # Check if translation is already cached
        cached_translation = db.query(CachedTranslation).filter(
            CachedTranslation.source_text_hash == text_hash,
            CachedTranslation.source_language == request.source_language,
            CachedTranslation.target_language == request.target_language
        ).first()

        if cached_translation:
            logger.info(f"Returning cached translation for hash: {text_hash}")
            return TranslationResponse(
                translated_text=cached_translation.translated_text,
                source_language=cached_translation.source_language,
                target_language=cached_translation.target_language
            )

        # If not cached, perform translation
        # Here we'll use a mock translation service or Google Translate API
        api_key = os.getenv("TRANSLATION_API_KEY")
        
        if api_key:
            # Use Google Translate API if available
            translated_text = await _translate_with_google(
                request.text, 
                request.source_language, 
                request.target_language, 
                api_key
            )
        else:
            # Fallback: mock translation for Urdu
            if request.target_language == "ur":
                # This is just a placeholder - a real implementation would handle actual translation
                # For now, we'll return the original text as a placeholder
                translated_text = f"[TRANSLATED TO URDU: {request.text[:50]}...]"
            else:
                translated_text = request.text

        # Create a new cached translation
        new_translation = CachedTranslation(
            source_text_hash=text_hash,
            source_language=request.source_language,
            target_language=request.target_language,
            translated_text=translated_text,
            source_file=None,  # Not from a specific file in this case
            user_id=current_user.id
        )

        # Add to database
        db.add(new_translation)
        db.commit()
        db.refresh(new_translation)

        logger.info(f"Stored new translation for hash: {text_hash}")

        return TranslationResponse(
            translated_text=translated_text,
            source_language=request.source_language,
            target_language=request.target_language
        )

    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        logger.error(f"Error translating text: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error processing translation"
        )

async def _translate_with_google(text: str, source_lang: str, target_lang: str, api_key: str) -> str:
    """
    Helper function to translate text using Google Translate API
    """
    try:
        url = f"https://translation.googleapis.com/language/translate/v2"
        
        payload = {
            "q": text,
            "source": source_lang,
            "target": target_lang,
            "format": "text"
        }
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            result = response.json()
            return result["data"]["translations"][0]["translatedText"]
        else:
            logger.error(f"Google Translate API error: {response.status_code}")
            # Return original text as fallback
            return text
    except Exception as e:
        logger.error(f"Error calling Google Translate API: {str(e)}")
        # Return original text as fallback
        return text