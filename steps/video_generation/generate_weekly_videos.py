import os
import re
from moviepy.editor import concatenate_videoclips, TextClip, AudioFileClip, CompositeVideoClip
from dotenv import load_dotenv

load_dotenv()

TEAM_LOGS_DIR = "team_logs_weekly"
VOICEOVERS_DIR = "voiceovers"
VIDEOS_DIR = "videos"
os.makedirs(VIDEOS_DIR, exist_ok=True)

WIDTH, HEIGHT = 1280, 720
DURATION_PER_SLIDE = 4  # seconds
FONT_SIZE = 48
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)


def highlight_buzzwords(text, buzzwords):
    for word in buzzwords:
        text = re.sub(fr"\\b({word})\\b", r"<span fgcolor='purple'>\\1</span>", text, flags=re.IGNORECASE)
    return text


def create_slide(text, buzzwords):
    # For now, skip highlight attempt since it's not functional in TextClip
    return TextClip(
        txt=text,
        fontsize=FONT_SIZE,
        color='black',
        size=(WIDTH, HEIGHT),
        bg_color='white',
        method='caption'
    ).set_duration(DURATION_PER_SLIDE).set_position('center')



def create_video(team_name):
    bullet_texts = []
    for filename in sorted(os.listdir(TEAM_LOGS_DIR)):
        if filename.startswith(team_name) and filename.endswith(".txt"):
            with open(os.path.join(TEAM_LOGS_DIR, filename)) as f:
                bullet_texts.extend(f.read().strip().split("\n"))

    if not bullet_texts:
        print(f"❌ No logs for {team_name}. Skipping...")
        return

    buzzwords = ["API", "report", "schema", "budget", "expenses", "forecast", "feature", "deploy"]
    slides = [create_slide(text, buzzwords) for text in bullet_texts if text.strip()]

    voiceover_path = os.path.join(VOICEOVERS_DIR, f"{team_name}.mp3")
    if not os.path.exists(voiceover_path):
        print(f"❌ Missing audio for {team_name}. Skipping...")
        return

    audio_clip = AudioFileClip(voiceover_path)
    total_audio_duration = audio_clip.duration
    total_slide_duration = len(slides) * DURATION_PER_SLIDE

    if total_slide_duration < total_audio_duration:
        last_slide_duration = DURATION_PER_SLIDE + (total_audio_duration - total_slide_duration)
        slides[-1] = slides[-1].set_duration(last_slide_duration)

    video = concatenate_videoclips(slides, method="compose")
    final = CompositeVideoClip([video]).set_audio(audio_clip)

    output_path = os.path.join(VIDEOS_DIR, f"{team_name}.mp4")
    final.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
    print(f"🎥 Saved video for {team_name} at {output_path}")


if __name__ == "__main__":
    print("PYTHON PATH:", os.getenv("VIRTUAL_ENV"))
    for team_name in ["engineering", "engineering_1", "engineering_2", "finance", "finance_1", "finance_2"]:
        create_video(team_name)
    print("✅ All videos generated!")
