import assemblyai as aai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
# audio_file = "./local_file.mp3"
audio_file = "./audioFile.wav"

config = aai.TranscriptionConfig(sentiment_analysis=True)

transcript = aai.Transcriber().transcribe(audio_file, config)
print(f"Transcript ID:", transcript.id)

for sentiment_result in transcript.sentiment_analysis:
    print(sentiment_result.text)
    print(sentiment_result.sentiment)  # POSITIVE, NEUTRAL, or NEGATIVE
    print(sentiment_result.confidence)
    print(f"Timestamp: {sentiment_result.start} - {sentiment_result.end}")
