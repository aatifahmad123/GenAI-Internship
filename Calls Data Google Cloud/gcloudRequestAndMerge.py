from google.cloud import texttospeech
from pydub import AudioSegment
import os

customer_vice = 'en-IN-Chirp3-HD-Achird'
agent_voice = 'en-IN-Chirp3-HD-Erinome'


# Define the conversation
conversation = [
    "There’s a ₹200 charge on my savings account for no reason! What’s this about?",
    "I’m sorry for the confusion Sir. Can you share your account number to check the charge?",
    "It’s six nine zero, six one nine, zero eight, five two. I never signed up for any extra fees!",
    "I see it’s a maintenance fee due to a low balance. I can waive it as a one-time courtesy.",
    "Waive it? Why’s it there in the first place? Explain!",
    "The account requires a minimum balance of ₹10,000. I’ve waived the fee and can set up balance alerts for you."
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
    filename = f"Agent 03/Call 05/normal audios/synthesis({i}).wav"
    voice = customer_vice if i % 2 == 0 else agent_voice
    generate_and_save_audio(text, voice, filename)

print("All audios generated and saved successfully.")

# Merge all audio files
audio_files_folder = "Agent 03/Call 05/normal audios"
files = [f"{audio_files_folder}/synthesis({i}).wav" for i in range(len(conversation))]
combined_audio_file = "Agent 03/Call 05/normalAudio.wav"

def merge_audio(files):
    combined = AudioSegment.empty()
    for file in files:
        audio = AudioSegment.from_wav(file)
        combined += audio
    combined.export(combined_audio_file, format="wav")
    print(f"All audios merged successfully into {combined_audio_file}.")

merge_audio(files)
