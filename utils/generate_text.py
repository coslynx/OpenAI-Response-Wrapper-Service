from openai import OpenAI
from .config import settings
from .models import GenerateRequest, GenerateResponse
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

openai = OpenAI(api_key=settings.OPENAI_API_KEY)

async def generate_text(request: GenerateRequest):
    """
    Generates text using the OpenAI API.

    Args:
        request: A GenerateRequest object containing the model, prompt, temperature, and max_tokens.

    Returns:
        A GenerateResponse object containing the generated text or an error message.
    """
    try:
        response = await openai.completions.create(
            model=request.model,
            prompt=request.prompt,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )
        
        result = response.choices[0].text

        return GenerateResponse(success=True, result=result)

    except Exception as e:
        logger.error(f"Error generating text: {e}")
        raise HTTPException(status_code=500, detail=f"Error generating text: {e}")