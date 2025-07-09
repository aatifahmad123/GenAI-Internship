import assemblyai as aai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
# audio_file = "./local_file.mp3"
audio_file = "./audioFile.wav"

config = aai.TranscriptionConfig().set_redact_pii(
    policies=[
        aai.PIIRedactionPolicy.person_name,
        aai.PIIRedactionPolicy.organization,
        aai.PIIRedactionPolicy.occupation,
    ],
    substitution=aai.PIISubstitutionPolicy.hash,
)

transcript = aai.Transcriber().transcribe(audio_file, config)
print(f"Transcript ID:", transcript.id)

print(transcript.text)
