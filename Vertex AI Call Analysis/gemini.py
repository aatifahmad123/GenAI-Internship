from vertexai.preview.generative_models import GenerativeModel, Part
from vertexai import init

# Initialize Vertex AI
init(
    project="icici-internship",
    location="asia-south1"
)

# Load Gemini model
model = GenerativeModel("gemini-1.5-flash")

# Reference the audio file in GCS
audio_part = Part.from_uri(
    uri="gs://icici-internship-calls-audio-files/audio-files/audioFile2.wav",
    mime_type="audio/wav"
)

# Create the prompt
prompt = [
    "Listen to this audio and give sentiment of each line",
    audio_part
]

# Call the model
response = model.generate_content(
    prompt,
    generation_config={"temperature": 0.7}
)

# Output result
print(response.text)
