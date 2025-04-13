# 🔁 Updated `text_to_speech.py` for smarter voiceovers


import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Rachel, change if needed

INPUT_FOLDER = "team_logs_weekly"
OUTPUT_FOLDER = "voiceovers"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

def summarize_for_voiceover(text):
    # 💡 Make voiceovers slightly more elaborate than slide text
    lines = text.strip().split("\n")
    bullet_points = [
        f"In this update, we {line.lower().strip().rstrip('.')}..." for line in lines
    ]
    return " ".join(bullet_points)

def generate_voiceover(text, output_path):
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"🎤 Saved: {output_path}")
    else:
        print(f"❌ Failed to generate audio for {output_path}: {response.text}")

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".txt"):
        team_name = filename.replace(".txt", "")
        with open(os.path.join(INPUT_FOLDER, filename), "r") as f:
            text = f.read()

        voiceover_text = summarize_for_voiceover(text)
        output_path = os.path.join(OUTPUT_FOLDER, f"{team_name}.mp3")
        generate_voiceover(voiceover_text, output_path)

print("✅ All voiceovers generated!")
