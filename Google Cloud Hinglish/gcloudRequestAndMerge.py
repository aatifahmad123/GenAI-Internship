from google.cloud import texttospeech
from pydub import AudioSegment
import os

customer_vice = 'en-IN-Chirp3-HD-Umbriel'
agent_voice = 'en-IN-Chirp3-HD-Sulafat'

# Define the conversation
conversation = [
     "Namaste, mera naam Ravi Kumar hai. Mera debit card last week se kaam nahi kar raha hai.",
    "Namaste Ravi ji, main aapki help ke liye hoon. Kya aap bata sakte hain ki card kahaan use karne ki koshish ki thi?",
    "Haan, maine ek online shopping ki try ki, lekin har baar 'transaction declined' ka message aa raha hai.",
    "Samjha. Kya aap apna card number bata sakte hain taaki main check kar sakoon?",
    "Yeh lijiye, 2468-1357-2091-1234. Please jaldi dekho, mujhe yeh jaldi fix karwana hai.",
    "Ji, maine dekh liya. Aapke card pe ek technical block hai. Main ise abhi unblock kar deta hoon. 2 ghante mein yeh work karne lagega.",
    "Thanks, please sure karo ki yeh jaldi ho jaye.",
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
    filename = f"Agent 01/Call 01/normal audios/synthesis({i}).wav"
    voice = customer_vice if i % 2 == 0 else agent_voice
    generate_and_save_audio(text, voice, filename)

print("All audios generated and saved successfully.")

# Merge all audio files
audio_files_folder = "Agent 01/Call 01/normal audios"
files = [f"{audio_files_folder}/synthesis({i}).wav" for i in range(len(conversation))]
combined_audio_file = "Agent 01/Call 01/normalAudio.wav"

def merge_audio(files):
    combined = AudioSegment.empty()
    for file in files:
        audio = AudioSegment.from_wav(file)
        combined += audio
    combined.export(combined_audio_file, format="wav")
    print(f"All audios merged successfully into {combined_audio_file}.")

merge_audio(files)
