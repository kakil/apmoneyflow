import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    PINTEREST_USER = os.getenv("PINTEREST_USER")
    PINTEREST_PASS = os.getenv("PINTEREST_PASS")
    AMAZON_AFFILIATE_TAG = os.getenv("AMAZON_AFFILIATE_TAG")
