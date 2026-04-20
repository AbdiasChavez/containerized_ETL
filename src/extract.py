import os
import requests
from src.logger_config import get_logger

logger = get_logger(__name__) 

API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("API_KEY")
