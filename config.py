import os
from dotenv import load_dotenv

load_dotenv()  # This loads environment variables from .env file

class Config:
    DATABASE_CONNECTION_STRING = os.getenv("DATABASE_CONNECTION_STRING")
