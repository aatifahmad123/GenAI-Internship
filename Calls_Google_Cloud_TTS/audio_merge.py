from pydub import AudioSegment

audio_files_folder = "call28/audios"
files = [audio_files_folder + "/synthesis(0).wav", audio_files_folder + "/synthesis(1).wav", audio_files_folder + "/synthesis(2).wav", audio_files_folder + "/synthesis(3).wav", audio_files_folder + "/synthesis(4).wav", audio_files_folder + "/synthesis(5).wav"]
combined_audio_file = "call28/call28.wav"

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