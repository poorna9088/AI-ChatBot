from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    reply = chat_completion.choices[0].message.content

    return jsonify({
        "reply": reply
    })

if __name__ == "__main__":
    app.run(debug=True)