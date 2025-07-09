import assemblyai as aai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

audio_file = "./audioFile.wav"
# audio_file = "https://assembly.ai/wildfires.mp3"

config = aai.TranscriptionConfig(
  summarization=True,
  summary_model=aai.SummarizationModel.informative,
  summary_type=aai.SummarizationType.bullets
)

transcript = aai.Transcriber().transcribe(audio_file, config)

print(f"Transcript ID: ", transcript.id)
print(transcript.summary)
