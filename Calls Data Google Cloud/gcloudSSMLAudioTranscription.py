from google.cloud import speech
import io
import json

# Instantiate the client
client = speech.SpeechClient()

local_file_path = "Agent 03/Call 01/ssmlAudio.wav"
transcription_file_path = "Agent 03/Call 01/transcription.txt"
timestamps_file_path = "Agent 03/Call 01/timestamps.json"

def transcribe_local_audio():
    with io.open(local_file_path, "rb") as audio_file:
        content = audio_file.read()

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

    response = client.recognize(config=config, audio=audio)

    with open(transcription_file_path, "w", encoding="utf-8") as tf:
        for result in response.results:
            tf.write(result.alternatives[0].transcript + "\n")

    # Save word-level timestamps and confidence
    all_words_data = []

    for result in response.results:
        for word_info in result.alternatives[0].words:
            word_data = {
                "word": word_info.word,
                "start_time": f"{word_info.start_time.seconds} sec",
                "end_time": f"{word_info.end_time.seconds} sec",
                "confidence": round(word_info.confidence, 3)
            }
            all_words_data.append(word_data)

    with open(timestamps_file_path, "w", encoding="utf-8") as jsonf:
        json.dump(all_words_data, jsonf, indent=2)

    print(f"Transcript saved to {transcription_file_path}")
    print(f"Timestamps saved to {timestamps_file_path}")


transcribe_local_audio()
