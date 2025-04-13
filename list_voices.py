import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")

headers = {
    "xi-api-key": api_key
}

response = requests.get("https://api.elevenlabs.io/v1/voices", headers=headers)
voices = response.json().get("voices", [])

for voice in voices:
    print(f"{voice['name']}: {voice['voice_id']}")

