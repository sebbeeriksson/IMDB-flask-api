from flask import Blueprint, jsonify
from db import get_db_connection

actors_bp = Blueprint('actors', __name__)

@actors_bp.route('/most-oscar-wins', methods=['GET'])
def most_oscar_wins():
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor()
        query = """
        SELECT top 3 Name, Oscar_Wins
        FROM Actors
        ORDER BY Oscar_Wins DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        actors = [{"name": row[0], "age": row[1]} for row in results]
        return jsonify(actors)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@actors_bp.route('/actors', methods=['GET'])
def actors():
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor()
        query = """
        SELECT Name, age
        FROM Actors
        """
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        actors = [{"name": row[0], "oscar_wins": row[1]} for row in results]
        return jsonify(actors)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
