from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/students")
def students():
    return jsonify([
        {"id": 1, "name": "Ali"},
        {"id": 2, "name": "Sara"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
