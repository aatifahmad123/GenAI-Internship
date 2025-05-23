import requests
from dotenv import load_dotenv
import os
import base64
from pydub import AudioSegment

def count_directories(path):

    '''
    Count the number of directories in the given path. This will give me current call id.
    '''

    return sum(
        os.path.isdir(os.path.join(path, entry))
        for entry in os.listdir(path)
    )

directory_path = '../Calls_Google_Cloud_TTS'
current_call_id = count_directories(directory_path)

# loading api keys from env
load_dotenv()

GCLOUD_ACCESS_TOKEN = os.getenv("GCLOUD_ACCESS_TOKEN")
if not GCLOUD_ACCESS_TOKEN:
    raise ValueError("GCLOUD_ACCESS_TOKEN not found")

conversation = [
    "I set up a recurring deposit, and it’s so convenient! How do I increase the amount?",
    "Glad it’s working well, sir! Can you share your account number?",
    "It’s six seven, eight nine, zero one, two three four four. Can we do it quickly?",
    "You’ll need to submit a request to modify the RD. I’ll send the form to your email.",
    "Awesome, thanks! You guys make banking easy.",
    "Thank you, sir! The form’s sent, and I’ll follow up once it’s processed."
]

# set customer and agent voices
customer_voice = "en-IN-Chirp3-HD-Algenib"
agent_voice = "en-IN-Chirp3-HD-Aoede"

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

    filename = f"call{current_call_id}/audios/synthesis({i}).wav"
    audio_voice = ""
    text = conversation[i]

    if i % 2 == 0:
        audio_voice = customer_voice

    else:
        audio_voice = agent_voice
    
    generate_and_save_audio(text, audio_voice, filename)


print("All audios generated and saved successfully.")

# Now, merge all the audio files into a single audio file
audio_files_folder = f'call{current_call_id}/audios'
files = [f"{audio_files_folder}/synthesis({i}).wav" for i in range(len(conversation))]
combined_audio_file = f'call{current_call_id}/call{current_call_id}.wav'

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


