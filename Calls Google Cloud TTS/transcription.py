import os

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

MAX_AUDIO_LENGTH_SECS = 8 * 60 * 60


def run_batch_recognize():
  # Instantiates a client.
  client = SpeechClient()

  # The output path of the transcription result.
  gcs_output_folder = "gs://icici-internship-bucket/transcripts"

  # The name of the audio file to transcribe:
  audio_gcs_uri = "gs://icici-internship-bucket/audio-files/call01.wav"

  config = cloud_speech.RecognitionConfig(
      explicit_decoding_config=cloud_speech.ExplicitDecodingConfig(
        encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=24000,
        audio_channel_count=1
      ),
      features=cloud_speech.RecognitionFeatures(
          enable_word_confidence=true,
          enable_word_time_offsets=true,
        ),
      model="telephony",
      language_codes=["en-IN"],
  )

  output_config = cloud_speech.RecognitionOutputConfig(
      gcs_output_config=cloud_speech.GcsOutputConfig(uri=gcs_output_folder),
  )

  files = [cloud_speech.BatchRecognizeFileMetadata(uri=audio_gcs_uri)]

  request = cloud_speech.BatchRecognizeRequest(
      recognizer="projects/icici-internship/locations/global/recognizers/_",
      config=config,
      files=files,
      recognition_output_config=output_config,
  )
  operation = client.batch_recognize(request=request)

  print("Waiting for operation to complete...")
  response = operation.result(timeout=3 * MAX_AUDIO_LENGTH_SECS)
  print(response)