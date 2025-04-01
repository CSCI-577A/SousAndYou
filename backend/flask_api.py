from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

data_store = []  


@app.route("/search", methods=["POST"])
def search_data():
    query = request.json.get("query", "").lower()
    print(f"Received search query: {query}")  # Debugging log

    # TODO: get data results from claude/db
    data_store = query

    return jsonify({"results": data_store})

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify({"data": data_store})

if __name__ == "__main__":
    app.run(debug=True)