from flask import Blueprint, jsonify
from db import get_db_connection

series_bp = Blueprint('series', __name__)

@series_bp.route('/top-rated-series', methods=['GET'])
def top_rated_series():
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor()
        query = """
        SELECT TOP 3 Title, Rating
        FROM Series
        JOIN Ratings ON Series.ID = Ratings.Content_ID
        WHERE Ratings.Is_Movie = 0
        ORDER BY Rating DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        series = [{"title": row[0], "rating": row[1]} for row in results]
        return jsonify(series)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@series_bp.route('/series', methods=['GET'])
def series():
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor()
        query = """
        SELECT Title
        FROM Series
        """
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        series = [{"title": row[0]} for row in results]
        return jsonify(series)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@series_bp.route('/series-episodes', methods=['GET'])
def series_episodes():
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor()
        query = """
        SELECT 
            Series.ID AS series_id,
            Series.Title AS series_title,
            Episodes.Title_Episode AS episode_title,
            Episodes.Length AS episode_length,
            Episodes.Season AS episode_season
        FROM 
            Series
        JOIN 
            Episodes ON Series.ID = Episodes.Series_ID
        ORDER BY 
            Series.ID, Episodes.Season, Episodes.Title_Episode;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        series_dict = {}
        for row in results:
            series_id = row.series_id
            series_title = row.series_title

            if series_id not in series_dict:
                series_dict[series_id] = {
                    "series_id": series_id,
                    "series_title": series_title,
                    "episodes": []
                }

            series_dict[series_id]["episodes"].append({
                "episode_title": row.episode_title,
                "episode_length": row.episode_length,
                "episode_season": row.episode_season
            })

        series_list = list(series_dict.values())
        return jsonify(series_list)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
