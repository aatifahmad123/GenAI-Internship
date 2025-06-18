from google.cloud import texttospeech
from pydub import AudioSegment
import os
import json
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Generate and merge audio files for a call conversation.")
parser.add_argument("agent_id", type=int, help="Agent ID (integer)")
parser.add_argument("call_id", type=int, help="Call ID (integer)")
args = parser.parse_args()

# Get agent_id and call_id from command line
agent_id = args.agent_id
call_id = args.call_id

print(f"Agent id : {agent_id}, Call id : { call_id}")

customer_voice = 'en-IN-Chirp3-HD-Achird'
agent_voice = 'en-IN-Chirp3-HD-Autonoe'

if agent_id == 1:
    agent_voice = 'en-IN-Chirp3-HD-Autonoe'
elif agent_id == 2:
    agent_voice = 'en-IN-Chirp3-HD-Sulafat'
elif agent_id == 3:
    agent_voice = 'en-IN-Chirp3-HD-Erinome'
elif agent_id == 4:
    agent_voice = 'en-IN-Chirp3-HD-Sadaltager'
elif agent_id == 5:
    agent_voice = 'en-IN-Chirp3-HD-Schedar'


call_dir = f"Agent {agent_id:02d}/Call {call_id:02d}"

json_file_path = os.path.join(call_dir, "data.json")

with open(json_file_path, "r", encoding="utf-8") as jsonf:
    data = json.load(jsonf)

conversation = [item["text"] for item in data["conversation"]]

print(conversation)

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
    filename = os.path.join(call_dir, f"normal audios/synthesis({i}).wav")
    voice = customer_voice if i % 2 == 0 else agent_voice
    generate_and_save_audio(text, voice, filename)

print("All audios generated and saved successfully.")

# Merge all audio files
audio_files_folder = os.path.join(call_dir, "normal audios")
files = [os.path.join(audio_files_folder, f"synthesis({i}).wav") for i in range(len(conversation))]
combined_audio_file = os.path.join(call_dir, "normalAudio.wav")

def merge_audio(files):
    combined = AudioSegment.empty()
    for file in files:
        audio = AudioSegment.from_wav(file)
        combined += audio
    combined.export(combined_audio_file, format="wav")
    print(f"All audios merged successfully into {combined_audio_file}.")

merge_audio(files)
