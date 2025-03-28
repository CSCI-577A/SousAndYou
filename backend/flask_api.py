from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

data_store = []  


@app.route("/search", methods=["POST"])
def search_data():
    query = request.json.get("query", "").lower()
    print(f"Received search query: {query}")  # Debugging log

    results = [item for item in data_store if query in item.lower()]
    print(f"Search results: {results}")  # Debugging log

    return jsonify({"results": results})


if __name__ == "__main__":
    app.run(debug=True)