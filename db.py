import pyodbc
from config import Config

def get_db_connection():
    try:
        conn = pyodbc.connect(Config.DATABASE_CONNECTION_STRING)
        return conn
    except Exception as e:
        print("Database connection failed:", e)
        return None
