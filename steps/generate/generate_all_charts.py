import os
import subprocess

FLOWCHART_DIR = "flowcharts"

# Remove ``` lines if they exist
def clean_mermaid_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    cleaned_lines = [line for line in lines if not line.strip().startswith("```")]
    
    with open(file_path, "w") as f:
        f.writelines(cleaned_lines)

# Convert each .mmd to .png
def convert_all_mmd_to_png():
    for filename in os.listdir(FLOWCHART_DIR):
        if filename.endswith(".mmd"):
            mmd_path = os.path.join(FLOWCHART_DIR, filename)
            png_path = os.path.join(FLOWCHART_DIR, filename.replace(".mmd", ".png"))

            print(f"🧹 Cleaning {filename}...")
            clean_mermaid_file(mmd_path)

            print(f"🎨 Generating PNG: {png_path}...")
            subprocess.run(["mmdc", "-i", mmd_path, "-o", png_path], check=True)

    print("✅ All charts converted to PNG!")

if __name__ == "__main__":
    convert_all_mmd_to_png()
