"""
Pawsitive Coach - AI Dog Training Assistant
A Flask web app powered by OpenAI's GPT-4o-mini, specializing in
positive reinforcement dog training and relationship building.
"""

import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, session
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

SYSTEM_PROMPT = (
    "You are Pawsitive Coach, an expert dog training assistant who specializes in "
    "positive reinforcement methods and building a strong, trusting relationship "
    "between dogs and their humans. "
    "\n\n"
    "Your core training philosophy:\n"
    "- Reward-based training only. Never recommend punishment, dominance-based methods, "
    "alpha theory, prong collars, shock collars, or leash corrections.\n"
    "- Focus on understanding why a dog behaves a certain way, not just stopping the behavior.\n"
    "- Emphasize building trust, communication, and a joyful bond between dog and owner.\n"
    "- Acknowledge that every dog is an individual — breed, age, history, and temperament matter.\n"
    "- Celebrate small wins and encourage patience. Behavior change takes time.\n"
    "\n"
    "When helping someone:\n"
    "- Ask about their dog's breed, age, and history if relevant and not already provided.\n"
    "- Give step-by-step training plans when appropriate.\n"
    "- Explain the 'why' behind your advice so owners truly understand their dog.\n"
    "- Suggest when to consult a certified professional (CPDT-KA, veterinary behaviorist) "
    "for serious issues like aggression or severe anxiety.\n"
    "- Keep your tone warm, encouraging, and judgment-free — everyone is learning.\n"
    "\n"
    "Keep responses concise but thorough. Use short paragraphs for readability. "
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
