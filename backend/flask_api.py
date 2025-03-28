from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = ["test"]  # Simple in-memory storage

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify({"data": data_store})

@app.route("/data", methods=["POST"])
def set_data():
    new_data = request.json.get("item")
    if new_data:
        data_store.append(new_data)
        return jsonify({"message": "Data added", "data": data_store}), 201
    return jsonify({"error": "No data provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
