import requests
from dotenv import load_dotenv
import os
import base64
from pydub import AudioSegment

# Load API keys from .env
load_dotenv()
GCLOUD_ACCESS_TOKEN = os.getenv("GCLOUD_ACCESS_TOKEN")
if not GCLOUD_ACCESS_TOKEN:
    raise ValueError("GCLOUD_ACCESS_TOKEN not found")


# Set voices
customer_voice = "en-IN-Chirp3-HD-Algenib"
agent_voice = "en-IN-Chirp3-HD-Aoede"

# SSML
conversation = [
    # Customer
    """<speak>
        I set up a <emphasis level="moderate">recurring deposit</emphasis>, and it’s so convenient!
        <break time="400ms"/>
        How do I <prosody pitch="+2st">increase the amount</prosody>?
    </speak>""",
    # Agent
    """<speak>
        Glad it’s working well, sir!
        <break time="300ms"/>
        Can you share your <emphasis level="reduced">account number</emphasis>?
    </speak>""",
    # Customer
    """<speak>
        It’s <say-as interpret-as="digits">6 7 8 9 0 1 2 3 4 4</say-as>.
        <break time="400ms"/>
        Can we do it quickly?
    </speak>""",
    # Agent
    """<speak>
        You’ll need to submit a request to modify the <sub alias="R D">RD</sub>.
        <break time="300ms"/>
        I’ll send the form to your email.
    </speak>""",
    # Customer
    """<speak>
        Awesome, thanks!
        <break time="300ms"/>
        You guys make banking <prosody rate="fast">easy</prosody>.
    </speak>""",
    # Agent
    """<speak>
        Thank you, sir!
        <break time="300ms"/>
        The form’s sent, and I’ll follow up once it’s processed.
    </speak>"""
]

# Prepare output directory
directory_path = '../Calls_Google_Cloud_TTS'

def count_directories(path):
    '''
    Function to count directories to get the call_id
    '''

    return sum(
        os.path.isdir(os.path.join(path, entry))
        for entry in os.listdir(path)
    )

current_call_id = count_directories(directory_path)
call_folder = f"{directory_path}/call{current_call_id}"
audio_folder = f"{call_folder}/audios"
os.makedirs(audio_folder, exist_ok=True)


def generate_and_save_audio(ssml, audio_voice, filename):
    '''
    Function to generate audio from SSML using Google Cloud TTS API
    '''

    url = 'https://texttospeech.googleapis.com/v1/text:synthesize'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {GCLOUD_ACCESS_TOKEN}'
    }
    payload = {
        "input": {
            "ssml": ssml
        },
        "voice": {
            "languageCode": "en-IN",
            "name": audio_voice
        },
        "audioConfig": {
            "audioEncoding": "LINEAR16"
        }
    }
    response = requests.post(url, headers=headers, json=payload)

    audio_content_str = response.json().get('audioContent')

    audio_bytes = base64.b64decode(audio_content_str)

    with open(filename, "wb") as f:
        f.write(audio_bytes)

    print(f"Saved audio to {filename}")

# Generate audio for each line
audio_files = []
for i, ssml in enumerate(conversation):
    filename = f"{audio_folder}/synthesis({i}).wav"
    audio_voice = customer_voice if i % 2 == 0 else agent_voice
    generate_and_save_audio(ssml, audio_voice, filename)
    audio_files.append(filename)

print("All audios generated and saved successfully.")

# Merge audio files
combined_audio_file = f"{call_folder}/call{current_call_id}_ssml.wav"

def merge_audio(files, output_file):
    '''
    Function to merge audio files together
    '''

    combined = AudioSegment.empty()
    for file in files:
        audio = AudioSegment.from_wav(file)
        combined += audio
    combined.export(output_file, format="wav")
    print(f"All audios merged successfully into {output_file}.")

merge_audio(audio_files, combined_audio_file)
