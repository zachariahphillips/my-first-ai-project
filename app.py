"""
My First AI Chatbot (Web Version)
A Flask web app with a chat UI powered by OpenAI's GPT-4o-mini.
"""

import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, session
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

SYSTEM_PROMPT = (
    "You are a friendly and helpful AI assistant. "
    "Keep your responses concise but informative. "
    "If you don't know something, say so honestly."
)


def get_client():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set. Check your .env file.")
    return OpenAI(api_key=api_key)


@app.route("/")
def home():
    session["conversation"] = []
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    if "conversation" not in session:
        session["conversation"] = []

    session["conversation"].append({"role": "user", "content": user_message})

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + session["conversation"]

    try:
        client = get_client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=500,
        )
        reply = response.choices[0].message.content
        session["conversation"].append({"role": "assistant", "content": reply})
        session.modified = True
        return jsonify({"reply": reply})
    except Exception as e:
        session["conversation"].pop()
        return jsonify({"error": str(e)}), 500


@app.route("/clear", methods=["POST"])
def clear():
    session["conversation"] = []
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
