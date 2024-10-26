from fastapi import APIRouter, HTTPException, Depends
from .models import GenerateRequest, GenerateResponse
from .utils import generate_text
from .config import settings
from openai import OpenAI
import os

ai_router = APIRouter()

openai = OpenAI(api_key=settings.OPENAI_API_KEY) # Initialize OpenAI client with API key from settings

@ai_router.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    """
    Generates text using the OpenAI API.

    Args:
        request: A GenerateRequest object containing the model, prompt, temperature, and max_tokens.

    Returns:
        A GenerateResponse object containing the generated text or an error message.
    """
    try:
        # Send request to OpenAI API
        response = await openai.completions.create(
            model=request.model,
            prompt=request.prompt,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )
        
        # Extract generated text from response
        result = response.choices[0].text

        return GenerateResponse(success=True, result=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")