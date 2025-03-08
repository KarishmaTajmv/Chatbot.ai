# src/config.py

import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")  # Google API key
print(f"The google api key is {GOOGLE_API_KEY}") # Add this
CHROMA_DB_PATH = "./chroma_db"
