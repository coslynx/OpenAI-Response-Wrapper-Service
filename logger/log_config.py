import logging
from logging.handlers import RotatingFileHandler
import os
from .config import settings  # Import logging settings from the settings module

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(getattr(logging, settings.LOG_LEVEL))  # Set the logging level based on the settings

# Create a rotating file handler
file_handler = RotatingFileHandler(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.log"),
    maxBytes=10 * 1024 * 1024,  # 10 MB file size
    backupCount=5,  # Keep 5 backup files
)
file_handler.setLevel(getattr(logging, settings.LOG_LEVEL))  # Set the logging level for the file handler

# Create a formatter for the log messages
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Define a custom logging function for convenience
def log_message(message: str, level: str = "INFO"):
    """Logs a message with the specified level.

    Args:
        message: The message to log.
        level: The logging level (INFO, DEBUG, WARNING, ERROR, CRITICAL).
    """
    getattr(logger, level.lower())(message)