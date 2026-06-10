from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json
import os

app = Flask(__name__)

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per day"]
)
limiter.init_app(app)

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

data = load_data()


@app.route("/set", methods=["POST"])
@limiter.limit("10 per minute")
def set_value():
    body = request.json

    key = body.get("key")
    value = body.get("value")

    if not key:
        return jsonify({"error": "Key is required"}), 400

    data[key] = value
    save_data()

    return jsonify({
        "message": "Value saved",
        "key": key,
        "value": value
    })


@app.route("/get/<key>", methods=["GET"])
def get_value(key):
    if key in data:
        return jsonify({
            "key": key,
            "value": data[key]
        })

    return jsonify({"error": "Key not found"}), 404


@app.route("/delete/<key>", methods=["DELETE"])
@limiter.limit("10 per minute")
def delete_value(key):
    if key in data:
        del data[key]
        save_data()

        return jsonify({
            "message": "Key deleted",
            "key": key
        })

    return jsonify({"error": "Key not found"}), 404


@app.route("/exists/<key>", methods=["GET"])
def exists(key):
    return jsonify({
        "key": key,
        "exists": key in data
    })


if __name__ == "__main__":
    app.run(debug=True)
