from google.cloud import texttospeech
from pydub import AudioSegment
import os

customer_vice = 'en-US-Chirp3-HD-Achird'
agent_voice = 'en-US-Chirp3-HD-Autonoe'

# Define the conversation
conversation = [
    "Hello? I applied for a personal loan last month, but nobody’s told me what’s happening with it.",
    "Good afternoon, Sir. I’d be happy to check the status. Could you provide your application ID or full name?",
    "It’s Priyansh Sharma. I don’t have any ID number… nobody gave me one!",
    "No worries, I can search by name. One moment—",
    "And please, don’t put me on hold for ages! I’ve been waiting too long already.",
    "Of course, Sir. I’ll be as quick as possible. It looks like your application is under review due to a pending CIBIL score update—",
    "CIBIL? What’s that? Nobody told me about this! Why is it taking so long?",
    "I apologize for the confusion. CIBIL is your credit score, and we’re waiting for the latest report—",
    "But I need the loan urgently! Can’t you speed it up?",
    "Absolutely, I understand the urgency. I’ll escalate this to expedite the process and keep you updated.",
    "Please do. I really hope I hear back soon this time."
]

# Initialize Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Function to synthesize speech and save to file
def generate_and_save_audio(text, audio_voice, filename):
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
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
