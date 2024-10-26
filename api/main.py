from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import ai_router
from .database import engine, Base
from .config import settings
from fastapi.responses import JSONResponse

app = FastAPI()

# Configure CORS middleware to allow all origins for development
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include AI router for API endpoints
app.include_router(ai_router, prefix="/api/v1/ai")

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    # Perform any startup tasks like connecting to external services or initializing caches
    # Example: Connecting to Redis for caching
    # from .utils.cache import cache
    # await cache.connect()

@app.on_event("shutdown")
async def shutdown_event():
    # Perform any shutdown tasks like closing connections or releasing resources
    # Example: Closing Redis connection
    # from .utils.cache import cache
    # await cache.close()

# Define a health check endpoint for monitoring
@app.get("/health")
async def health():
    return JSONResponse({"status": "ok"})

# Handle any uncaught exceptions to provide a consistent error response
@app.exception_handler(Exception)
async def uncaught_exception_handler(request, exc):
    return JSONResponse(
        {"error": str(exc)},
        status_code=500,
    )