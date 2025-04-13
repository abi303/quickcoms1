from supabase import create_client, Client
import os
import csv
from dotenv import load_dotenv

# 🔑 Load your API keys
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

# 📥 Fetch from Supabase
response = supabase.table("slack_messages").select("text,channel").execute()
slack_messages = response.data

# 💾 Write to sample_input.csv
csv_path = "steps/csv_to_txt/sample_input.csv"
os.makedirs("steps/csv_to_txt", exist_ok=True)

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["log", "team"])
    writer.writeheader()
    for row in slack_messages:
        writer.writerow({
            "log": row.get("text", "").strip(),
            "team": row.get("channel", "").strip()
        })

print(f"✅ CSV saved to {csv_path}")
