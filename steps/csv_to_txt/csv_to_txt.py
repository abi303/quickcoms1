import csv
import os
from collections import defaultdict

INPUT_CSV = "steps/csv_to_txt/sample_input.csv"
OUTPUT_FOLDER = "logs_txt"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Dictionary to group logs by team
team_logs = defaultdict(list)

# Read CSV and group by team
with open(INPUT_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        team = row.get("team", "").strip().lower()
        log = row.get("log", "").strip()
        if team and log:
            team_logs[team].append(log)

# Write out .txt files per team
for team, logs in team_logs.items():
    output_path = os.path.join(OUTPUT_FOLDER, f"{team}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(logs))
    print(f"✅ Wrote: {output_path}")

print("🎯 All done!")

