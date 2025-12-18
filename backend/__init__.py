import logging
import sys

# Set up root logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),  # Output to stdout
        logging.FileHandler('app.log')      # Also save to file
    ]
)

# Create a logger for the application
logger = logging.getLogger(__name__)
logger.info("Application logger initialized")