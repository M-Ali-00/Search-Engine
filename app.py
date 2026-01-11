from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from search import search

app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/api/query", methods=["POST"])
def handles_query():
    data = request.get_json()
    
    if not data or "query" not in data:
        return jsonify({"error": "No query provided"}), 400
        
    user_query = data.get("query")
    output= search(user_query) #checks for match in db 

    print(output)
    results = {
        "status": "success",
        "original_query": user_query,
        "length": len(user_query),
        "engine_output": output
    }

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    