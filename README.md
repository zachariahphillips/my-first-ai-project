# My First AI Project

A beginner-friendly Python project to explore AI development using the Anthropic Claude API.

## What this does

This is a simple command-line chatbot that uses Anthropic's Claude model to have conversations.
You type a message, Claude responds, and it remembers the conversation history.

## Setup

1. Install Python dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

2. Get an Anthropic API key:
   - Go to https://console.anthropic.com/
   - Create an account and add a payment method
   - Go to https://console.anthropic.com/settings/keys
   - Click "Create Key" and copy it

3. Set your API key:
   ```bash
   export ANTHROPIC_API_KEY="your-key-here"
   ```

4. Run the chatbot:
   ```bash
   python3 chat.py
   ```

## Learning Resources

- [Anthropic API Docs](https://docs.anthropic.com/)
- [Claude Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
- [Python Beginner Guide](https://wiki.python.org/moin/BeginnersGuide)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
