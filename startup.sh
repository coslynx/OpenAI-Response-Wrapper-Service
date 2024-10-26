#!/bin/bash

# Set environment variables from .env file
source .env

# Install Python dependencies
pip install -r requirements.txt

# Create the PostgreSQL database
python scripts/create_database.py

# Start the FastAPI server
uvicorn api.main:app --host 0.0.0.0 --port $PORT --reload