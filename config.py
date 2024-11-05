import os
from dotenv import load_dotenv

load_dotenv()  # This loads environment variables from .env file
DATABASE_CONNECTION_STRING = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=tcp:yourserver.database.windows.net,1433;"
    "Database=yourdb;"
    "Uid=yourusername;"
    "Pwd=yourpassword;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)
class Config:
    DATABASE_CONNECTION_STRING = os.getenv("DATABASE_CONNECTION_STRING")
