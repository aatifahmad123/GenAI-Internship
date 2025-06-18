from google.cloud import speech
import io
import json
import os

# Start the client
client = speech.SpeechClient()

def transcribe_for_transcription():
    '''
    Transcribe multiple synthesis(i).wav files to generate transcription with speaker tags.
    '''
    transcript_lines = []
    speaker = "Customer"

    audio_directory = os.path.join(call_directory, "normal audios")
    audio_files = [f"synthesis({i}).wav" for i in range(15) if os.path.exists(os.path.join(audio_directory, f"synthesis({i}).wav"))]

    for audio_file in audio_files:
        file_path = os.path.join(audio_directory, audio_file)
        
        # Read audio file
        with io.open(file_path, "rb") as audio:
            content = audio.read()

        audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=24000,
            language_code="en-IN",
            model="latest_short",
            audio_channel_count=1,
            enable_automatic_punctuation=True,
        )

        # Transcribe audio
        response = client.recognize(config=config, audio=audio)

        # Process transcription
        for result in response.results:
            transcript = result.alternatives[0].transcript
            transcript_lines.append(f"{speaker}: {transcript}")

        # Switch speaker
        speaker = "Agent" if speaker == "Customer" else "Customer"

    # Save transcription
    with open(transcription_file_path, "w", encoding="utf-8") as tf:
        tf.write("\n".join(transcript_lines) + "\n")

    print(f"Transcript saved to {transcription_file_path} for {call_directory}")

def transcribe_for_timestamps():
    '''
    Transcribe a single normalAudio.wav file to generate timestamps without speaker tags.
    '''
    all_words_data = []

    audio_file = "normalAudio.wav"
    file_path = os.path.join(call_directory, audio_file)

    # Check if audio file exists
    if not os.path.exists(file_path):
        print(f"Audio file not found: {file_path}")
        return

    # Read audio file
    with io.open(file_path, "rb") as audio:
        content = audio.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=24000,
        language_code="en-IN",
        model="latest_short",
        audio_channel_count=1,
        enable_word_time_offsets=True,
        enable_automatic_punctuation=True,
    )

    # Transcribe audio
    response = client.recognize(config=config, audio=audio)

    # Process word-level timestamps without speaker
    for result in response.results:
        for word_info in result.alternatives[0].words:
            start_time = word_info.start_time.seconds
            end_time = word_info.end_time.seconds
            word_data = {
                "word": word_info.word,
                "start_time": f"{start_time:.3f} sec",
                "end_time": f"{end_time:.3f} sec",
            }
            all_words_data.append(word_data)

    # Save timestamps
    with open(timestamps_file_path, "w", encoding="utf-8") as jsonf:
        json.dump(all_words_data, jsonf, indent=2, ensure_ascii=False)

    print(f"Timestamps saved to {timestamps_file_path} for {call_directory}")

agents = ["Agent 01","Agent 02","Agent 03","Agent 04","Agent 05"]
calls = ["Call 01","Call 02","Call 03","Call 04","Call 05","Call 06","Call 07","Call 08","Call 09","Call 10"]

for agent in agents:
    for call in calls:
        call_directory = f"{agent}/{call}"
        transcription_file_path = os.path.join(call_directory, "transcription.txt")
        timestamps_file_path = os.path.join(call_directory, "timestamps.json")

        # Transcribe for transcription and timestamps
        transcribe_for_transcription()
        transcribe_for_timestamps()