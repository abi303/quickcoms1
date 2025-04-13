import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

INPUT_FOLDER = "logs_txt"
OUTPUT_FOLDER = "team_logs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

TEAMS = ["Tech", "Finance", "Engineering", "Product"]

def categorize(content):
    prompt = f"""
    Given this Slack log, categorize it into one of the following teams: {', '.join(TEAMS)}.
    Return only the team name.

    Slack log:
    {content}
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a classifier that assigns Slack logs to teams."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".txt"):
        with open(os.path.join(INPUT_FOLDER, filename), "r") as file:
            content = file.read()

        team = categorize(content)

        # Clean and ensure team folder exists
        team_folder = os.path.join(OUTPUT_FOLDER, team)
        os.makedirs(team_folder, exist_ok=True)

        # Save the log file into the team folder
        dest_path = os.path.join(team_folder, filename)
        with open(dest_path, "w") as f:
            f.write(content)

print("✅ Categorization done. Results saved in `team_logs`")
