from google.cloud import texttospeech
from pydub import AudioSegment
import os

customer_vice = 'en-IN-Chirp3-HD-Achird'
agent_voice = 'en-IN-Chirp3-HD-Autonoe'

# Define the conversation
conversation = [
    "I’ve been trying to activate my new credit card for hours! It’s not working, do it now!",
    "I’m sorry for the delay, sir. Can you confirm the last four digits of your card so I can check the activation status?",
    "It’s seven eight nine zero. I followed all the steps, but it’s still not active!",
    "Thank you. It seems the activation request didn’t process. I’ll activate it manually now. Please wait a moment.",
    "Hurry up! I need to use it today!",
    "It’s done, sir. Your card is active now. You can use it immediately. Would you like me to send a confirmation?",
    "Finally! Yeah, send it."
]

# Initialize Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Function to synthesize speech and save to file
def generate_and_save_audio(text, audio_voice, filename):
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-IN",
        name=audio_voice
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f"Saved audio to {filename}")

# Generate audio for each line
for i, text in enumerate(conversation):
    filename = f"Agent 01/Call 10/normal audios/synthesis({i}).wav"
    voice = customer_vice if i % 2 == 0 else agent_voice
    generate_and_save_audio(text, voice, filename)

print("All audios generated and saved successfully.")

# Merge all audio files
audio_files_folder = "Agent 01/Call 10/normal audios"
files = [f"{audio_files_folder}/synthesis({i}).wav" for i in range(len(conversation))]
combined_audio_file = "Agent 01/Call 10/normalAudio.wav"

def merge_audio(files):
    combined = AudioSegment.empty()
    for file in files:
        audio = AudioSegment.from_wav(file)
        combined += audio
    combined.export(combined_audio_file, format="wav")
    print(f"All audios merged successfully into {combined_audio_file}.")

merge_audio(files)
