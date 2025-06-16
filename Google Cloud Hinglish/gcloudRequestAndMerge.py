from google.cloud import texttospeech
from pydub import AudioSegment
import os

customer_vice = 'hi-IN-Chirp3-HD-Umbriel'
agent_voice = 'hi-IN-Chirp3-HD-Sulafat'

# Define the conversation
conversation = [
    "नमस्ते, मेरा नाम रवि कुमार है। मेरा डेबिट कार्ड पिछले हफ्ते से काम नहीं कर रहा है।",
    "नमस्ते रवि जी, मैं आपकी मदद के लिए हूँ। क्या आप बता सकते हैं कि कार्ड का उपयोग कहाँ करने की कोशिश की थी?",
    "हाँ, मैंने एक ऑनलाइन खरीदारी की कोशिश की, लेकिन हर बार 'लेनदेन अस्वीकृत' का संदेश आ रहा है।",
    "समझा। क्या आप अपना कार्ड नंबर बता सकते हैं ताकि मैं इसे चेक कर सकूँ?",
    "ये लीजिए, 2468-1357-2091-1234। कृपया जल्दी देखिए, मुझे ये जल्द ठीक करवाना है।",
    "जी, मैंने देख लिया। आपके कार्ड पर एक तकनीकी ब्लॉक है। मैं इसे अभी अनब्लॉक कर देती हूँ। 2 घंटे में ये काम करने लगेगा।",
    "धन्यवाद, कृपया सुनिश्चित करें कि ये जल्दी हो जाए।",
]

# Initialize Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Function to synthesize speech and save to file
def generate_and_save_audio(text, audio_voice, filename):
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="hi-IN",
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
