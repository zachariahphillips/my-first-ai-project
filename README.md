# My First AI Project

A beginner-friendly AI chatbot with both a terminal and web interface, powered by OpenAI's GPT-4o-mini.

## What this does

Talk to an AI assistant through either:
- **Web app** (`app.py`) — A modern chat interface in your browser
- **Terminal** (`chat.py`) — A simple command-line version

The AI remembers your conversation history and can answer questions, write creatively, explain concepts, and more.

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set up your API key

```bash
cp .env.example .env
```

Then edit `.env` and replace `your-key-here` with your real OpenAI API key.
Get a key at: https://platform.openai.com/api-keys

### 3. Run the web app

```bash
python3 app.py
```

Open http://localhost:5000 in your browser.

### 3b. Or run the terminal version

```bash
python3 chat.py
```

## Cost

Uses GPT-4o-mini (~$0.15/million input tokens, ~$0.60/million output tokens).
For casual use, expect to spend pennies per session.

## Project Structure

```
my-first-ai-project/
├── app.py              # Web app (Flask)
├── chat.py             # Terminal chatbot
├── requirements.txt    # Python dependencies
├── .env.example        # Template for your API key
├── .gitignore          # Keeps secrets out of GitHub
├── templates/
│   └── index.html      # Chat UI
└── README.md           # You're reading this!
```

## Learning Resources

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Python Beginner Guide](https://wiki.python.org/moin/BeginnersGuide)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
