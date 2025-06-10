# AI Idea Debunker Backend

This is a FastAPI backend service that uses OpenAI's GPT to provide instant critiques on startup ideas.

## Setup

1. Copy `.env.example` to `.env` and add your OpenAI API key.

```
OPENAI_API_KEY=your_openai_api_key_here
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app locally:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Deployment

- Push the repo to GitHub.
- Connect it to [Render](https://render.com).
- Add your OpenAI API key as an environment variable (`OPENAI_API_KEY`).
- Use this start command on Render:

```
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## API

- POST `/critique`

**Request JSON:**

```json
{
  "idea": "Your startup idea text here"
}
```

**Response JSON:**

```json
{
  "score": 8,
  "analysis": {
    "strengths": "...",
    "weaknesses": "...",
    "competition": "...",
    "questions": "...",
    "next_steps": "..."
  }
}
```