from flask import Flask
from flask import request
from flask_cors import CORS

from database import save_chat

app = Flask(__name__)

CORS(app)


@app.route("/save_chat", methods=["POST"])
def save_chat_route():

    data = request.json

    print("\\n========== RECEIVED ==========")
    print(data["title"])
    print("==============================")

    save_chat(
        data["timestamp"],
        data["title"],
        data["content"]
    )

    return {
        "status": "success"
    }


@app.route("/")
def health():

    return {
        "status": "running"
    }


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )