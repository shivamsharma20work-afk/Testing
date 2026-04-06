from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Backend 🚀"

@app.route("/data")
def data():
    return jsonify({
        "name": "Shivam",
        "role": "DevOps Engineer",
        "message": "Hello from backend"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)