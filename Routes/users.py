from flask import Blueprint, jsonify
from db import get_db_connection

users_bp = Blueprint('user', __name__)

@users_bp.route('/users', methods=['GET'])
def users():
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor()
        query = """
        SELECT * 
        FROM users
        
        """
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        users = [{"id": row[0], "name": row[1], "age": row[2]} for row in results]
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


