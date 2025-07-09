import assemblyai as aai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

# audio_file = "./local_file.mp3"
audio_file = "./audioFile.wav"

config = aai.TranscriptionConfig(iab_categories=True)

transcript = aai.Transcriber().transcribe(audio_file, config)
print(f"Transcript ID:", transcript.id)

# Get the parts of the transcript that were tagged with topics
for result in transcript.iab_categories.results:
    print(result.text)
    print(f"Timestamp: {result.timestamp.start} - {result.timestamp.end}")
    for label in result.labels:
        print(f"{label.label} ({label.relevance})")

# Get a summary of all topics in the transcript
for topic, relevance in transcript.iab_categories.summary.items():
    print(f"Audio is {relevance * 100}% relevant to {topic}")
