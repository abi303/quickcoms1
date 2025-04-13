import os
import json
import openai
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from supabase_client import supabase  # <-- make sure this is working

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_user_preferences(user_id: str):
    # Try Supabase first
    try:
        response = supabase.table("user_preferences").select("*").eq("slack_user_id", user_id).execute()
        if response.data and len(response.data) > 0:
            return response.data[0]
    except Exceptions as e:
        print("🔥 Supabase fetch error:", e)

    # Fallback to local db.json
    try:
        with open("db.json", "r") as f:
            data = json.load(f)
        return data.get(user_id)
    except Exception as e:
        print("📄 Local DB fetch error:", e)
        return None


# ✅ POST endpoint: Generate post using uploaded file + user preferences
@app.post("/generate-post/")
async def generate_post(
    file: UploadFile = File(...),
    user_id: str = Form(...)
):
    try:
        prefs = get_user_preferences(user_id)
        if prefs is None:
            return {"error": f"No preferences found for user_id: {user_id}"}

        tone = prefs.get("tone", "professional")
        platform = prefs.get("platform", "LinkedIn")
        length = prefs.get("length", "medium")

        content = await file.read()
        text = content.decode("utf-8")

        prompt = (
            f"You are a startup founder. Write a {tone}-toned, {length} "
            f"length post for {platform}, based on the update below:\n\n{text}"
        )

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a startup social media manager."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        post_text = response['choices'][0]['message']['content']
        return {"post": post_text.strip()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/test-insert")
def insert_sample():
    try:
        data = {
            "slack_user_id": "U123ABC",
            "tone": "casual",
            "audience": "founders",
            "platforms": ["twitter", "linkedin"],
            "prompt_before_post": True
        }

        response = supabase.table("user_preferences").insert(data).execute()

        print("🪵 Supabase response:", response)
        return {
            "status": "done",
            "inserted": response.data if hasattr(response, 'data') else None,
            "raw": str(response)
        }

    except Exception as e:
        print("🔥 Exception:", str(e))
        return {"error": str(e)}
