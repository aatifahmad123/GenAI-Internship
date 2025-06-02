from google.cloud import speech
import io
import json

client = speech.SpeechClient()
local_file_path = "Agent 05/Call 04/ssmlAudio.wav"

def transcribe_local_audio():
    with io.open(local_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=24000,
    language_code="en-IN",
    audio_channel_count=1,
    enable_word_time_offsets=True,
    enable_automatic_punctuation=True,
    enable_word_confidence=True,
    use_enhanced=True,  # Required for latest models
    model="telephony",  # Use telephony model for call center audio
    diarization_config=speech.SpeakerDiarizationConfig(
        enable_speaker_diarization=True,
        min_speaker_count=2,
        max_speaker_count=2
        )
    )


    # Use long_running_recognize for diarization (required)
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=300)  # Adjust timeout as needed

    print(response)

transcribe_local_audio()
