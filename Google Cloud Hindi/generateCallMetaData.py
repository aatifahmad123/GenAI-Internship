import os
import wave

def get_audio_duration(audio_path):
    
    """
    Calculate the duration of an audio file in seconds.
    """
    
    with wave.open(audio_path, 'rb') as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        duration = frames / float(rate)
        return duration

def save_call_duration_metadata():
    
    """
    Save the duration of each call's audio file in a metadata file.
    """
    
    agents = ["Agent 01", "Agent 02", "Agent 03", "Agent 04", "Agent 05"]
    calls = ["Call 01","Call 02", "Call 03", "Call 04", "Call 05","Call 06", "Call 07", "Call 08", "Call 09", "Call 10"]

    for agent in agents:
        for call in calls:
            call_directory = os.path.join(agent, call)
            audio_path = os.path.join(call_directory, "normalAudio.wav")
            metadata_path = os.path.join(call_directory, "metadata.txt")

            if os.path.exists(audio_path):
                try:
                    duration = get_audio_duration(audio_path)
                    with open(metadata_path, "w", encoding="utf-8") as mf:
                        mf.write(f"Duration: {duration:.2f} seconds\n")
                    print(f"Saved duration to {metadata_path}")
                except Exception as e:
                    print(f"Error processing {audio_path}: {e}")
            else:
                print(f"File not found: {audio_path}")

# Run the script
save_call_duration_metadata()
