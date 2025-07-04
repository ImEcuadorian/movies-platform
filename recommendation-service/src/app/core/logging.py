import logging

from src.app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(settings.PROJECT_NAME)