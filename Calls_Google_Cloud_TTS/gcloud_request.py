import requests
from dotenv import load_dotenv
import os
import base64

# loading api keys from env
load_dotenv()

GCLOUD_ACCESS_TOKEN = os.getenv("GCLOUD_ACCESS_TOKEN")

url = 'https://texttospeech.googleapis.com/v1/text:synthesize'
headers = {
    'Content-Type': 'application/json',
    'X-Goog-User-Project': 'icici-internship',
    'Authorization': f'Bearer {GCLOUD_ACCESS_TOKEN}'
}
payload = {
    "input": {
        "markup": "Hello, Hello, My card payment’s stuck on ‘processing’ for two days! What’s the deal?"
    },
    "voice": {
        "languageCode": "en-IN",
        "name": "en-IN-Chirp3-HD-Achernar",
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
with open("output.wav", "wb") as f:
    f.write(audio_bytes)

# save the audio
print("Saved audio to output.wav")
