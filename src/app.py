import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


def get_db_conn():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ["DB_PORT"]),
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"],
        dbname=os.environ["DB_NAME"],
    )


@app.route("/")
def index():
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("SELECT message FROM greetings LIMIT 1")
        row = cur.fetchone()
        cur.close()
        conn.close()
        greeting = row[0] if row else "No greeting found"
        return jsonify({
            "type": "python",
            "greeting": greeting,
            "status": {"database": "OK"},
        }), 200
    except Exception as e:
        return jsonify({
            "type": "python",
            "greeting": None,
            "status": {"database": f"ERROR: {e}"},
        }), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
