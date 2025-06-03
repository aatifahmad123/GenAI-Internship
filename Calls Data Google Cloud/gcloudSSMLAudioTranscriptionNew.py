from google.cloud import speech
import io
import json
import os

# Start the client
client = speech.SpeechClient()

def transcribe_multiple_audios():
    
    '''
    Transcribe multiple audio files in a directory and save the transcription and timestamps with speaker information.
    '''
    
    all_words_data = []
    transcript_lines = []
    cumulative_time = 0
    speaker = "Customer"

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
            enable_word_time_offsets=True,
            enable_automatic_punctuation=True,
            enable_word_confidence=True,
        )

        # Transcribe audio
        response = client.recognize(config=config, audio=audio)

        # transcription
        for result in response.results:
            transcript = result.alternatives[0].transcript
            transcript_lines.append(f"{speaker}: {transcript}")

            # word-level timestamps
            for word_info in result.alternatives[0].words:
                # Add cumulative time to start and end times
                start_time = word_info.start_time.seconds + cumulative_time
                end_time = word_info.end_time.seconds + cumulative_time
                word_data = {
                    "word": word_info.word,
                    "start_time": f"{start_time:.3f} sec",
                    "end_time": f"{end_time:.3f} sec",
                    "confidence": round(word_info.confidence, 3),
                    "speaker": speaker
                }
                all_words_data.append(word_data)

        # Update cumulative time
        if response.results and response.results[-1].alternatives[0].words:
            last_word = response.results[-1].alternatives[0].words[-1]
            cumulative_time += last_word.end_time.seconds
        
        # Switch speaker
        speaker = "Agent" if speaker == "Customer" else "Customer"

    # Save transcription
    with open(transcription_file_path, "w", encoding="utf-8") as tf:
        tf.write("\n".join(transcript_lines) + "\n")

    # Save timestamps with speaker information
    with open(timestamps_file_path, "w", encoding="utf-8") as jsonf:
        json.dump(all_words_data, jsonf, indent=2)

    print(f"Transcript saved to {transcription_file_path} for {call_directory}")
    print(f"Timestamps saved to {timestamps_file_path} for {call_directory}")

agents = ["Agent 01"]
calls = ["Call 02"]

for agent in agents:
    for call in calls:
        call_directory = f"{agent}/{call}"
        audio_directory = os.path.join(call_directory, "normal audios")
        transcription_file_path = os.path.join(call_directory, "transcription.txt")
        timestamps_file_path = os.path.join(call_directory, "timestamps.json")

        # Transcribe the audio files in the directory
        transcribe_multiple_audios()

