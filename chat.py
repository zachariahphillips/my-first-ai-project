"""
My First AI Chatbot
A simple conversational AI using the Anthropic Claude API.
"""

import os
import sys

import anthropic


def create_client():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: No API key found!")
        print("Run this command first, replacing 'your-key' with your real key:")
        print('  export ANTHROPIC_API_KEY="your-key"')
        sys.exit(1)
    return anthropic.Anthropic(api_key=api_key)


SYSTEM_PROMPT = (
    "You are a friendly and helpful AI assistant. "
    "Keep your responses concise but informative. "
    "If you don't know something, say so honestly."
)


def chat(client, conversation_history):
    """Send the conversation to Claude and get a response."""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=conversation_history,
    )
    return response.content[0].text


def main():
    client = create_client()
    conversation_history = []

    print("=" * 50)
    print("  Welcome to My First AI Chatbot!")
    print("  Powered by Claude")
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
            conversation_history = []
            print("Conversation cleared!\n")
            continue

        conversation_history.append({"role": "user", "content": user_input})

        try:
            reply = chat(client, conversation_history)
            conversation_history.append({"role": "assistant", "content": reply})
            print(f"\nClaude: {reply}\n")
        except Exception as e:
            print(f"\nError: {e}\n")
            conversation_history.pop()


if __name__ == "__main__":
    main()
