from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings  # Import database URL from settings

# Use the specified version of psycopg2-binary
engine = create_engine(settings.DATABASE_URL, connect_args={"connect_timeout": 5})  # Configure timeout for the connection

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to create a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()