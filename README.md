# Gemini AI Starter: Chatbot + Image Understanding

A beginner-friendly Streamlit project using Google's current `google-genai` Python SDK. It includes:
- **Chatbot** — asks Gemini questions and keeps recent conversation context.
- **Image understanding** — uploads an image and asks Gemini to describe or analyze it.
- Environment-variable based API key management.

> **Model availability:** The default model is configurable through `GEMINI_MODEL`. Model names and API features can vary by account and API release. If your account reports that the default model is unavailable, set `GEMINI_MODEL` to a model currently listed for your Google AI API account.

## Project structure

```text
gemini-ai-starter/
├── chatbot.py
├── vision.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 1. Requirements

- Python 3.10+ (use a Python version supported by the installed SDK)
- A Google AI API key
- Internet access

Create or obtain an API key through Google AI Studio. Keep it private.

## 2. Setup on Windows / Git Bash

Open Git Bash and navigate to your project folder. Example:

```bash
cd "/d/work/olama resm/Gemini AI"
```

Create and activate a virtual environment if you do not already have one:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

Install dependencies using the same Python interpreter:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Create your local environment file:

```bash
cp .env.example .env
```

Open `.env` in a text editor and replace the placeholder with your own key. Do not commit `.env`.

## 3. Run the chatbot

Make sure your terminal is in the project root — the directory containing `chatbot.py`, **not** inside `.venv`.

```bash
python -m streamlit run chatbot.py
```

## 4. Run image understanding

```bash
python -m streamlit run vision.py
```

## Troubleshooting

### `File does not exist: chatbot.py`

Check your current folder:

```bash
pwd
ls
```

Navigate to the folder containing `chatbot.py`, then rerun Streamlit. A virtual environment is a folder for Python packages; do not save your app files inside `.venv`.

### API key missing

- Confirm `.env` is in the same project root as `chatbot.py` and `vision.py`.
- Confirm the variable is spelled exactly `GEMINI_API_KEY`.
- Restart Streamlit after changing `.env`.

### Model not found / model unavailable

Set `GEMINI_MODEL` in `.env` to a model currently available to your API account. Do not assume a model name from an older tutorial will remain available.

### Slow response or quota errors

Check network connectivity, API quota, service status, and model availability. A long wait can be caused by service load or an API request that is not completing; changing the model may help if another supported model is available.

## Security

- Never hard-code API keys in Python files.
- Never commit `.env` or share screenshots containing your key.
- If a key was exposed publicly, revoke it and generate a replacement.

## Concepts demonstrated

- Streamlit UI and session state
- Environment variables with `python-dotenv`
- Calling the Gemini API with `google-genai`
- Chat history and multimodal image input
- Basic exception handling and user-facing errors

## Future improvements

- Add chat export and configurable generation parameters.
- Add file-based conversation memory.
- Add logging that avoids storing secrets or sensitive prompts.
- Add tests and deployment configuration.
