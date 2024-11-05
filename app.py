from flask import Flask, jsonify, request
from flask_cors import CORS  # For enabling CORS if needed
import pyodbc  # For database connection

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (optional)

# Database connection settings
DATABASE_CONNECTION_STRING = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=tcp:imdbserverdb.database.windows.net,1433;"
    "Database=IMDB_DB;"
    "Uid=sqluser;"
    "Pwd=123qweASD!;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)


# Function to get a database connection
def get_db_connection():
    conn = pyodbc.connect(DATABASE_CONNECTION_STRING)
    return conn

# Home route (useful to test if the API is live)
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Example route: Get top-rated shows
@app.route('/top-rated-shows', methods=['GET'])
def top_rated_shows():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        SELECT TOP 5 Title, Rating
        FROM Series
        JOIN Ratings ON Series.ID = Ratings.Content_ID
        WHERE Ratings.Is_Movie = 0
        ORDER BY Rating DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        # Format the results into JSON
        shows = [{"title": row[0], "rating": row[1]} for row in results]
        return jsonify(shows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Example route: Get actors with the most Oscar wins
@app.route('/most-oscar-wins', methods=['GET'])
def most_oscar_wins():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        SELECT Name, Oscar_Wins
        FROM Actors
        ORDER BY Oscar_Wins DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        # Format the results into JSON
        actors = [{"name": row[0], "oscar_wins": row[1]} for row in results]
        return jsonify(actors)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Optional: Documentation endpoint
@app.route('/docs', methods=['GET'])
def docs():
    return jsonify({
        "endpoints": {
            "/": "Home route to check if the API is live.",
            "/top-rated-shows": "GET: Returns the top-rated shows.",
            "/most-oscar-wins": "GET: Returns actors with the most Oscar wins."
        }
    })
def test_connection():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT TOP 1 * FROM Movies")  # Replace with an actual table
        row = cursor.fetchone()
        print("Connection successful:", row)
    except Exception as e:
        print("Connection failed:", e)
    finally:
        conn.close()

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    test_connection()
