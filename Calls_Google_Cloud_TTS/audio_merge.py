from pydub import AudioSegment

audio_files_folder = "call29/audios"
files = [f"{audio_files_folder}/synthesis({i}).wav" for i in range(6)]
combined_audio_file = "call29/call29.wav"

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