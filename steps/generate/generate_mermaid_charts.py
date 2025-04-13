import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

INPUT_FOLDER = "team_logs"
OUTPUT_FOLDER = "flowcharts"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def generate_mermaid_chart(log_content):
    prompt = f"""You are a helpful assistant. Based on the following workday log, generate a mermaid flowchart showing the sequence of events. Keep it simple.

Log:
\"\"\"
{log_content}
\"\"\"

Reply ONLY with a mermaid chart using 'graph TD' format. No extra text.
"""
    print("🧪 Sending log to OpenAI:\n", log_content[:300], "\n---")
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that creates Mermaid flowcharts."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

for root, dirs, files in os.walk(INPUT_FOLDER):
    for filename in files:
        if filename.endswith(".txt"):
            team_name = os.path.splitext(filename)[0]
            file_path = os.path.join(root, filename)
            with open(file_path, "r") as f:
                log_content = f.read()

            if not log_content.strip():
                print(f"⚠️ Skipping empty file: {file_path}")
                continue

            print("🧪 Sending log to OpenAI:\n", log_content[:300], "\n---")
            chart = generate_mermaid_chart(log_content)
            # 🧽 Clean up markdown-style ```mermaid ... ``` if present
            if chart.startswith("```mermaid"):
                chart = chart.replace("```mermaid", "").replace("```", "").strip()

            output_path = os.path.join(OUTPUT_FOLDER, f"{team_name}.mmd")
            with open(output_path, "w") as out:
                out.write(chart)
            print(f"✅ Wrote: {output_path}")
            print(f"🔍 Preview of {team_name} chart:\n{chart}\n")

print("🎯 All done!")
