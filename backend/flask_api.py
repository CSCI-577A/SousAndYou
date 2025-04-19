from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from user_manager import create_user, redis_client

app = Flask(__name__)
CORS(app)  

data_store = []

users = {}
user_counter = 1
@app.route("/user/create", methods=["GET"])
def auto_create_user():
    # create new user and cache
    new_user = create_user()
    return jsonify({
        "message": "User created",
        "user_id": new_user.user_id
    }), 201
@app.route("/search", methods=["POST"])
def search_data():
    print("Incoming JSON:", request.json)
    print("Redis ping:", redis_client.ping())
    input = request.json.get("query", "").strip()
    user_id = request.json.get("user_id", "").strip()
    print(f"Received search query: {input}")  # Debugging log
    if not input:
        return jsonify({"error": "No user input provided. Please enter an input."}), 400
    print(user_id)
    raw_user = redis_client.get(user_id)
    print(raw_user)
    if not raw_user:
        return jsonify({"error": "User not found"}), 404
    user = pickle.loads(raw_user)
    print(user)
    output = user.get_recipe_suggestions(input)
    print("out")
    print(output)
    return jsonify({"results": output})
@app.route("/set", methods=["GET"])
def set_user_input():
    return jsonify({"data": data_store})
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify({"data": data_store})

if __name__ == "__main__":
    app.run(debug=True)