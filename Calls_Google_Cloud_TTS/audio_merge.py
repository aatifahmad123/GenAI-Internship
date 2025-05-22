from pydub import AudioSegment
import os

# get the id of the current call to extract the paths of audio files inside
def count_directories(path):
    return sum(
        os.path.isdir(os.path.join(path, entry))
        for entry in os.listdir(path)
    )

directory_path = '../Calls_Google_Cloud_TTS'
current_call_id = count_directories(directory_path)

audio_files_folder = f'call{current_call_id}/audios'
files = [f"{audio_files_folder}/synthesis({i}).wav" for i in range(6)]
combined_audio_file = f'call{current_call_id}/call{current_call_id}.wav'

def merge_audio(files):
    # Initialize an  AudioSegment
    combined = AudioSegment.empty()

    # append each file to the combined AudioSegment
    for file in files:
        audio = AudioSegment.from_wav(file)
        combined += audio

    # Export the combined audio
    combined.export(combined_audio_file, format="wav")

merge_audio(files)