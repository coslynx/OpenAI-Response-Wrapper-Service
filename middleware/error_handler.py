from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from .config import settings  # Import settings for logging configuration
import logging

logger = logging.getLogger(__name__)  # Initialize logger

# Configure the logger based on the settings
logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL)) 

@app.exception_handler(HTTPException)  # Handle HTTPExceptions specifically
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Custom exception handler for HTTPExceptions.

    This handler provides a standardized JSON response for HTTP exceptions, 
    including the error message, status code, and additional context.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "status_code": exc.status_code},
    )

@app.exception_handler(Exception)  # Catch all other exceptions
async def uncaught_exception_handler(request: Request, exc: Exception):
    """
    Custom exception handler for all uncaught exceptions.

    This handler provides a consistent error response for uncaught exceptions, 
    logging the error and returning a standard JSON error message to the client.
    """
    logger.error(f"Uncaught exception: {exc}")  # Log the uncaught exception
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
        content={"error": "Internal server error"},
    )