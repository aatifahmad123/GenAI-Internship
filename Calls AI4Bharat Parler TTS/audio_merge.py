from pydub import AudioSegment

audio_files_folder = "call01/audios"
files = [f"{audio_files_folder}/audio({i}).mpga" for i in range(6)]
combined_audio_file = "call01/call01.mpga"  # Output as .mpga

def merge_audio(files):
    combined = AudioSegment.empty()
    
    for file in files:
        # Read MPGA files
        audio = AudioSegment.from_file(file, format="mp3")  # Format as MP3
        combined += audio
    
    # Export as MP3
    combined.export(combined_audio_file, format="mp3")  

merge_audio(files)
