from flask import Flask, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)



@app.route("/logs")
def get_logs():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT timestamp, source, message FROM logs ORDER BY timestamp DESC LIMIT 20")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    logs = []
    for row in rows:
        logs.append({
            "timestamp": row[0].strftime("%Y-%m-%d %H:%M:%S"),
            "source": row[1],
            "message": row[2]
        })

    return jsonify(logs)

@app.route("/alerts")
def get_alerts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT timestamp, severity, description FROM alerts ORDER BY timestamp DESC LIMIT 20")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    alerts = []
    for row in rows:
        alerts.append({
            "timestamp": row[0].strftime("%Y-%m-%d %H:%M:%S"),
            "severity": row[1],
            "description": row[2]
        })

    return jsonify(alerts)

if __name__ == "__main__":
    print("Starting SIEM API on http://localhost:5000")
    app.run(host="0.0.0.0", port=5000)
