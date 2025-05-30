import requests
from dotenv import load_dotenv
import os
import base64
from pydub import AudioSegment

# loading api keys from env
load_dotenv()

GCLOUD_ACCESS_TOKEN = os.getenv("GCLOUD_ACCESS_TOKEN")
CUSTOMER_VOICE = os.getenv("CUSTOMER_VOICE")
AGENT_VOICE = os.getenv("AGENT_01_VOICE")

conversation = [
    "Hey, I’ve been charged twice on my credit card for the same transaction! This is ridiculous!",
    "I’m so sorry to hear that, Sir. Can you share the transaction details so I can check the chargeback status?",
    "It’s from last week, uh, some restaurant bill… ₹5,200. I saw it twice on my statement!",
    "Got it. Let me pull up your account. It sounds like a duplicate charge; we can initiate a chargeback request right away.",
    "You better! I can’t keep paying for your mistakes!",
    "Absolutely, I understand your frustration. I’ve flagged this for a refund, and it should reflect in 5-7 business days."
]

def generate_and_save_audio(text, audio_voice, filename):

    '''
    Generate and save audio using Google Cloud TTS API.
    '''
    
    url = 'https://texttospeech.googleapis.com/v1/text:synthesize'
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-User-Project': 'icici-internship',
        'Authorization': f'Bearer {GCLOUD_ACCESS_TOKEN}'
    }
    payload = {
        "input": {
            "markup": text
        },
        "voice": {
            "languageCode": "en-IN",
            "name": audio_voice,
            "voiceClone": {}
        },
        "audioConfig": {
            "audioEncoding": "LINEAR16"
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    # get the audio content from the response
    audio_content_str = response.json().get('audioContent')

    # decode the base64 audio content
    audio_bytes = base64.b64decode(audio_content_str)
    with open(f"{filename}", "wb") as f:
        f.write(audio_bytes)

    # save the audio
    print(f"Saved audio to {filename}")


# loop through the conversation and generate audio for each line
for i in range(len(conversation)):

    filename = f"Agent 01/Call 01/normal audios/synthesis({i}).wav"
    audio_voice = ""
    text = conversation[i]

    if i % 2 == 0:
        audio_voice = CUSTOMER_VOICE

    else:
        audio_voice = AGENT_VOICE
    
    generate_and_save_audio(text, audio_voice, filename)


print("All audios generated and saved successfully.")

# Now, merge all the audio files into a single audio file
audio_files_folder = f'Agent 01/Call 01/normal audios'
files = [f"{audio_files_folder}/synthesis({i}).wav" for i in range(len(conversation))]
combined_audio_file = f'Agent 01/Call 01/normalAudio.wav'

def merge_audio(files):
    
    '''
    Merge multiple audio files into a single audio file.
    '''

    # Initialize an  AudioSegment
    combined = AudioSegment.empty()

    # append each file to the combined AudioSegment
    for file in files:
        audio = AudioSegment.from_wav(file)
        combined += audio

    # Export the combined audio
    combined.export(combined_audio_file, format="wav")

merge_audio(files)

print(f"All audios merged successfully into {combined_audio_file}.")


