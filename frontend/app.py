from flask import Flask, render_template
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5000/data"

@app.route("/")
def home():
    try:
        response = requests.get(BACKEND_URL)
        data = response.json()
    except:
        data = {"error": "Backend not reachable"}

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)