from google.cloud import texttospeech

# Initialize the client
client = texttospeech.TextToSpeechClient()

# Set the text input
synthesis_input = texttospeech.SynthesisInput(text="hello")

# Set voice parameters
voice = texttospeech.VoiceSelectionParams(
    language_code="en-IN",
    name="en-IN-Chirp3-HD-Achird"
)

# Set audio config
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16
)

# Perform the text-to-speech request
response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

# Save the output
with open("output.wav", "wb") as out:
    out.write(response.audio_content)
    print("Audio content written to file 'output.wav'")
