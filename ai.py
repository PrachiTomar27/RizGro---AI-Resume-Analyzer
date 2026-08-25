import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def analyze_resume(resume_text, user_goal):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": "GROQ_API_KEY is not set. Check your .env file."
        }

    prompt = f"""
You are a senior software engineer and hiring manager.
Evaluate the resume based on the user's goal.
User goal: "{user_goal}"
STRICT RULES:
- Extract only relevant skills for this goal
- Remove irrelevant tools [excel for backend, etc]
- Identify real gaps
- Generate roadmap only for missing fields
- Make output different based on goal

Return only JSON:
{{
"skills":[],
"missing_skills":[],
"roadmap":[],
"interview_questions":[]
}}
Resume:
{resume_text}
"""
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": "openai/gpt-oss-20b",  # ✅ updated model
                "messages": [
                    {"role": "system", "content": "You're a strict hiring manager."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            }
        )


        data = response.json()

        if "choices" in data and len(data["choices"]) > 0:
            content = data["choices"][0]["message"]["content"].strip()
            start = content.find("{")
            end = content.rfind("}") + 1
            return json.loads(content[start:end])
        else:
            return {
                "skills": [],
                "missing_skills": [],
                "roadmap": [],
                "interview_questions": [],
                "error": f"Unexpected response: {data}"
            }

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }
