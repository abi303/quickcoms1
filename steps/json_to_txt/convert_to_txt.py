from supabase import create_client, Client
import os
from dotenv import load_dotenv

# 🔑 Load your API keys from .env or environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

# 📥 Query data
response = supabase.table("slack_messages").select("text,channel").execute()

# 🧾 Extract data and error
slack_messages = response.data
# error = response.error

# ✅ Output

print("📄 Data:")
for row in slack_messages:
    print(row)