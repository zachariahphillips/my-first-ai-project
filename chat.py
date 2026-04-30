"""
My First AI Chatbot (Terminal Version)
A simple conversational AI using the OpenAI API.
"""

import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def create_client():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: No API key found!")
        print("Create a .env file with your key:")
        print("  cp .env.example .env")
        print("  # Then edit .env and paste your real key")
        sys.exit(1)
    return OpenAI(api_key=api_key)


def chat(client, conversation_history):
    """Send the conversation to GPT and get a response."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        temperature=0.7,
        max_tokens=500,
    )
    return response.choices[0].message.content


def main():
    client = create_client()

    system_prompt = (
        "You are a friendly and helpful AI assistant. "
        "Keep your responses concise but informative. "
        "If you don't know something, say so honestly."
    )
    conversation_history = [{"role": "system", "content": system_prompt}]

    print("=" * 50)
    print("  Welcome to My First AI Chatbot!")
    print("  Powered by GPT-4o-mini")
    print("  Type 'quit' to exit, 'clear' to reset")
    print("=" * 50)
    print()

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        if user_input.lower() == "clear":
            conversation_history = [{"role": "system", "content": system_prompt}]
            print("Conversation cleared!\n")
            continue

        conversation_history.append({"role": "user", "content": user_input})

        try:
            reply = chat(client, conversation_history)
            conversation_history.append({"role": "assistant", "content": reply})
            print(f"\nAI: {reply}\n")
        except Exception as e:
            print(f"\nError: {e}\n")
            conversation_history.pop()


if __name__ == "__main__":
    main()
