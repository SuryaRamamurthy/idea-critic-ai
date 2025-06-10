from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import openai
from dotenv import load_dotenv

load_dotenv()  # load .env variables

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class IdeaInput(BaseModel):
    idea: str

@app.post("/critique")
async def critique(data: IdeaInput):
    idea = data.idea.strip()

    if not idea:
        raise HTTPException(status_code=400, detail="Idea text is required")

    prompt = f"""
You are an expert startup advisor. Given the following startup idea, provide a critical analysis including:

- Strengths
- Weaknesses
- Market Competition
- Questions to Consider
- Next Steps

Startup idea:
"""{idea}"""

Format your response as a JSON object with keys: strengths, weaknesses, competition, questions, next_steps.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
            temperature=0.7,
        )

        content = response.choices[0].message.content

        import json
        analysis = json.loads(content)

        score = 8  # Placeholder score

        return {
            "score": score,
            "analysis": analysis
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))