from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from user_manager import create_user, redis_client

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={
    r"/*": {
        "origins": "https://d3h83wdyrx615b.cloudfront.net",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

data_store = []

users = {}
user_counter = 1

@app.before_request
def log_request():
    print(f"[Flask] {request.method} {request.path}")

@app.route("/user/create", methods=["GET"])
def auto_create_user():
    # create new user and cache
    new_user = create_user()
    return jsonify({
        "message": "User created",
        "user_id": new_user.user_id
    }), 201
@app.route("/search", methods=["POST"], strict_slashes = False)
def search_data():
    print("Redis keys:", redis_client.keys("*"))
    print("Incoming JSON:", request.json)
    print("Redis ping:", redis_client.ping())
    input = request.json.get("query", "").strip()
    user_id = request.json.get("user_id", "").strip()
    print("user_id from request:", user_id)
    print(f"Received search query: {input}")  # Debugging log
    if not input:
        return jsonify({"error": "No user input provided. Please enter an input."}), 400
    print(user_id)
    raw_user = redis_client.get(user_id)
    print("raw_user from Redis:", raw_user)
    print(raw_user)
    if not raw_user:
        print(f"User ID {user_id} not found - creating a fallback user.")
        user = create_user()
        redis_client.set(user.user_id, pickle.dumps(user))
        return jsonify({"message": "New user created due to missing ID", "user_id": user.user_id, "results": []}), 201
    user = pickle.loads(raw_user)
    print(user)
    output = user.get_recipe_suggestions(input)
    print(output)
    return jsonify({"results": output})
@app.route("/set", methods=["GET"])
def set_user_input():
    return jsonify({"data": data_store})
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify({"data": data_store})
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)