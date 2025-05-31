from google.cloud import texttospeech
from pydub import AudioSegment
import os

customer_vice = 'en-IN-Chirp3-HD-Achird'
agent_voice = 'en-IN-Chirp3-HD-Sulafat'

# Define the conversation
conversation = [
    "I paid my loan EMI, but there’s a lien on my account! What’s going on?",
    "I’m sorry for the confusion Sir. Can you share your loan account number to check the lien details?",
    "It’s five four six seven one nine eight three two. I paid on time, so why’s my money locked?. I paid on time, so why’s my money locked?",
    "I see the issue. The payment was processed, but a system error placed a lien. I’ll remove it now.",
    "Please fix it today! I need to withdraw cash.",
    "It’s resolved Sir. The lien is lifted, and your funds are available. I’ll send a confirmation."
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
    filename = f"Agent 02/Call 05/normal audios/synthesis({i}).wav"
    voice = customer_vice if i % 2 == 0 else agent_voice
    generate_and_save_audio(text, voice, filename)

print("All audios generated and saved successfully.")

# Merge all audio files
audio_files_folder = "Agent 02/Call 05/normal audios"
files = [f"{audio_files_folder}/synthesis({i}).wav" for i in range(len(conversation))]
combined_audio_file = "Agent 02/Call 05/normalAudio.wav"

def merge_audio(files):
    combined = AudioSegment.empty()
    for file in files:
        audio = AudioSegment.from_wav(file)
        combined += audio
    combined.export(combined_audio_file, format="wav")
    print(f"All audios merged successfully into {combined_audio_file}.")

merge_audio(files)
