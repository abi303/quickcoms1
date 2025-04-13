import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ELEVENLABS_API_KEY")
INPUT_FOLDER = "team_logs_weekly"
OUTPUT_FOLDER = "voiceovers"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

def generate_speech(text, output_path):
    payload = {
        "model_id": "eleven_monolingual_v1",
        "text": text,
        "voice_settings": {
            "stability": 0.3,
            "similarity_boost": 0.7
        }
    }
    voice_id = "XB0fDUnXU5powFXDhCwa"  # You can use others like "Adam", "Antoni", etc.

    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        headers=headers,
        json=payload,
        stream=True
    )

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"🎤 Saved: {output_path}")
    else:
        print(f"❌ Failed to generate audio: {response.text}")

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".txt"):
        team = os.path.splitext(filename)[0]
        with open(os.path.join(INPUT_FOLDER, filename), "r") as f:
            text = f.read().strip()
        if text:
            output_path = os.path.join(OUTPUT_FOLDER, f"{team}.mp3")
            generate_speech(text, output_path)

print("✅ All voiceovers generated!")
