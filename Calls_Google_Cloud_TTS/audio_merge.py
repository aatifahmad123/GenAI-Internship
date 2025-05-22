from pydub import AudioSegment

audio_files_folder = "call25/audios"
files = [audio_files_folder + "/synthesis(0).wav", audio_files_folder + "/synthesis(1).wav", audio_files_folder + "/synthesis(2).wav", audio_files_folder + "/synthesis(3).wav", audio_files_folder + "/synthesis(4).wav", audio_files_folder + "/synthesis(5).wav"]
combined_audio_file = "call25/call25.wav"

def merge_audio(files):
    # Initialize an empty AudioSegment
    combined = AudioSegment.empty()

    # Loop through the list of files and append each one to the combined AudioSegment
    for file in files:
        audio = AudioSegment.from_wav(file)
        combined += audio

    # Export the combined audio to a new file
    combined.export(combined_audio_file, format="wav")

merge_audio(files)