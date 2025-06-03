from google.cloud import texttospeech
from pydub import AudioSegment
import os

customer_vice = 'en-IN-Chirp3-HD-Achird'
agent_voice = 'en-IN-Chirp3-HD-Autonoe'

# Define the conversation
conversation = [
    "Hey, I’ve been charged twice on my credit card for the same transaction! This is ridiculous!",
    "I’m so sorry to hear that, Sir. Could you please—",
    "No, seriously, this is the second time something like this has happened! I just checked my statement and—",
    "I completely understand your frustration. If you could just share the transaction details, I can—",
    "It’s from last week, some restaurant bill, ₹5,200. I saw it twice, right there, two lines!",
    "Thank you for that info. Let me pull up your account and—",
    "And don’t tell me it’ll take weeks to fix, okay? I need that money back!",
    "Of course, Sir. It sounds like a duplicate charge; I can initiate a chargeback request right away—",
    "You better! I can’t keep paying for your mistakes! This is just not acceptable.",
    "Absolutely, I understand. I’ve already flagged this for a refund, and—",
    "How long is this going to take? I need to know!",
    "It should reflect in 5–7 business days. I’ll keep you updated every step of the way.",
    "Fine. Just make sure it happens this time."
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
    filename = f"Agent 01/Call 02/normal audios/synthesis({i}).wav"
    voice = customer_vice if i % 2 == 0 else agent_voice
    generate_and_save_audio(text, voice, filename)

print("All audios generated and saved successfully.")

# Merge all audio files
audio_files_folder = "Agent 01/Call 02/normal audios"
files = [f"{audio_files_folder}/synthesis({i}).wav" for i in range(len(conversation))]
combined_audio_file = "Agent 01/Call 02/normalAudio.wav"

def merge_audio(files):
    combined = AudioSegment.empty()
    for file in files:
        audio = AudioSegment.from_wav(file)
        combined += audio
    combined.export(combined_audio_file, format="wav")
    print(f"All audios merged successfully into {combined_audio_file}.")

merge_audio(files)
