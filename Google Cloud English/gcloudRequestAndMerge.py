from google.cloud import texttospeech
from pydub import AudioSegment
import os

customer_vice = 'en-US-Chirp3-HD-Achird'
agent_voice = 'en-US-Chirp3-HD-Autonoe'

# Define the conversation
conversation = [
    "Good afternoon, Mr. Verma! Ritesh this side, your Relationship Manager from Prestige Bank. Just checking in to see if everything is fine with your account?",
    "Hi Ritesh. Everything was fine until my net banking randomly stopped working. I’ve been trying to reset my password since morning — OTPs just vanish into a black hole.",
    "Oh I see. That must be frustrating, sir. Let me check… yes, looks like there’s a temporary block due to multiple failed login attempts.",
    "Yes, because your app kept saying 'something went wrong' after every attempt. Apparently the 'something' was my patience.",
    "Totally understand, sir. Happens sometimes — system gets sensitive after three failed tries. I’ll raise a request to unblock it. You’ll get a new link in 24–48 hours.",
    "Amazing. I love how everything urgent takes exactly 48 hours. It's like magic — or punishment.",
    "Haha, sir, I agree. It’s the process set by the IT department. Trust me, we also wish it was faster.",
    "Sure. And while we’re at it, I’ve been waiting for that credit card upgrade you promised in January. It’s July.",
    "Yes sir… I remember. It’s still 'under review' — I’ll escalate it again. These upgrades take time, especially if the usage criteria isn’t fully met yet.",
    "Well, maybe if you guys gave me the upgraded card, I’d *use* it enough to meet the criteria. Just a thought.",
    "Fair point, sir. Let me push it with the team once more and update you by tomorrow. Meanwhile, if there's anything else I can assist with — maybe a new fixed deposit or investment plan?",
    "Unless you have an FD that generates time, I’ll pass for now. Just please fix the basics first.",
    "Absolutely, sir. Prioritizing the net banking issue now. Thank you for your patience — and your sarcasm kept things entertaining!",
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
    filename = f"Agent 01/Call 11/normal audios/synthesis({i}).wav"
    voice = customer_vice if i % 2 == 0 else agent_voice
    generate_and_save_audio(text, voice, filename)

print("All audios generated and saved successfully.")

# Merge all audio files
audio_files_folder = "Agent 01/Call 11/normal audios"
files = [f"{audio_files_folder}/synthesis({i}).wav" for i in range(len(conversation))]
combined_audio_file = "Agent 01/Call 11/normalAudio.wav"

def merge_audio(files):
    combined = AudioSegment.empty()
    for file in files:
        audio = AudioSegment.from_wav(file)
        combined += audio
    combined.export(combined_audio_file, format="wav")
    print(f"All audios merged successfully into {combined_audio_file}.")

merge_audio(files)
