from flask import Flask, request, jsonify
from flask_cors import CORS
from user import User

app = Flask(__name__)
CORS(app)  

data_store = []

users = {}
user_counter = 1

@app.route("/user/create", methods=["GET"])
def auto_create_user():
    # Creates a user at the beginning of a session
    global user_counter
    new_user = User(user_id=user_counter, name=f"User{user_counter}", preferences={})
    users[user_counter] = new_user
    user_counter += 1

    return jsonify({
        "message": "User created",
        "user_id": new_user.user_id,
        "user": new_user
    })
@app.route("/search", methods=["POST"])
def search_data():
    input = request.json.get("query", "").strip()
    user = request.json.get("user", "")
    print(f"Received search query: {input}")  # Debugging log
    if not input:
        return jsonify({"error": "No user input provided. Please enter an input."}), 400

    # TODO: get data results from claude/db
    data_store = User.get_recipe_suggestions(user, input)

    return jsonify({"results": data_store})
@app.route("/set", methods=["GET"])
def set_user_input():
    return jsonify({"data": data_store})
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify({"data": data_store})

if __name__ == "__main__":
    app.run(debug=True)