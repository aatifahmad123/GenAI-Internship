import assemblyai as aai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

# audio_file = "./local_file.mp3"
audio_file = "./audioFile.wav"

config = aai.TranscriptionConfig(content_safety=True)

transcript = aai.Transcriber().transcribe(audio_file, config)

print(f"Transcript ID:", transcript.id)

for result in transcript.content_safety.results:
    print(result.text)
    print(f"Timestamp: {result.timestamp.start} - {result.timestamp.end}")

    # Get category, confidence, and severity.
    for label in result.labels:
        print(f"{label.label} - {label.confidence} - {label.severity}")  # content safety category

# Get the confidence of the most common labels in relation to the entire audio file.
for label, confidence in transcript.content_safety.summary.items():
    print(f"{confidence * 100}% confident that the audio contains {label}")

# Get the overall severity of the most common labels in relation to the entire audio file.
for label, severity_confidence in transcript.content_safety.severity_score_summary.items():
    print(f"{severity_confidence.low * 100}% confident that the audio contains low-severity {label}")
    print(f"{severity_confidence.medium * 100}% confident that the audio contains medium-severity {label}")
    print(f"{severity_confidence.high * 100}% confident that the audio contains high-severity {label}")
