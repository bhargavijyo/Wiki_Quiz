print(">>> LOADED llm.py FROM:", __file__)
import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()  # <-- THIS WAS MISSING

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "models/gemini-flash-latest"
print(">>> USING MODEL:", MODEL)


def generate_quiz(text: str):
    prompt = f"""
You MUST return ONLY valid JSON.
DO NOT include markdown, explanations, or extra text.

JSON schema:
{{
  "summary": string,
  "quiz": [
    {{
      "question": string,
      "options": [string],
      "answer": string,
      "difficulty": string,
      "explanation": string
    }}
  ],
  "related_topics": [string]
}}

Content:
{text}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    raw = response.text.strip()
    print(">>> RAW MODEL OUTPUT:\n", raw)

    # Attempt direct JSON parse
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    # Fallback: extract JSON block
    import re
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not match:
        raise ValueError("Model did not return JSON")

    try:
        return json.loads(match.group())
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON from model: {e}")
