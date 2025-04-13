import subprocess

print("🟢 Step 1: Convert JSON to TXT")
subprocess.run(["python3", "steps/json_to_txt/convert_json_to_txt.py", "steps/json_to_txt/sample_input.json"])

print("🟢 Step 2: Categorize TXT files into teams")
subprocess.run(["python3", "steps/categorize/categorize_txt_to_team.py"])

print("🟢 Step 3: Generate Mermaid charts")
subprocess.run(["python3", "steps/generate/generate_mermaid_charts.py"])

print("🟢 Step 4: Convert Mermaid charts to PNG")
subprocess.run(["python3", "steps/generate/convert_mmd_to_png.py"])

print("✅ Done! All steps completed.")
