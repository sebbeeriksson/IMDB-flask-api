from flask import Flask, jsonify
from flask_cors import CORS
from Routes import register_routes  # Import the route registration function

app = Flask(__name__)
CORS(app)  # Enable CORS if needed

# Register routes
register_routes(app)

# Home route
@app.route('/')
def home():
    return jsonify({
        "endpoints for imdb, by Sebastian Eriksson ": {

            "/series": "GET: Returns all the series.",
            "/top-rated-series": "GET: Returns the 3 top-rated series.",
            "/series-episodes": "GET: Returns all the episodes of all the series.",

            "/most-oscar-wins": "GET: Returns the actors with most oscar wins.",
            "/actors": "GET: Returns all the actors.",

            "/users": "GET: Returns all the users data "
        }
    })

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
