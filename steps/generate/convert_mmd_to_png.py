import os
import subprocess

INPUT_FOLDER = "flowcharts"
OUTPUT_FOLDER = "flowcharts"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".mmd"):
        name = os.path.splitext(filename)[0]
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, f"{name}.png")

        print(f"🖼 Converting {filename} to PNG...")
        subprocess.run([
            "mmdc",
            "-i", input_path,
            "-o", output_path
        ])
print("✅ All charts converted to PNG!")
