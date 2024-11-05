import os
from dotenv import load_dotenv


class Config:
    DATABASE_CONNECTION_STRING=("Driver={ODBC Driver 17 for SQL Server};"
                                "Server=tcp:imdbserverdb.database.windows.net,1433;"
                                "Database=IMDB_DB;"
                                "Uid=sqluser;"
                                "Pwd=123qweASD!;Encrypt=yes;"
                                "TrustServerCertificate=no;"
                                "Connection Timeout=30;")
