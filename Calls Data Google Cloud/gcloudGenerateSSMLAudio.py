from google.cloud import texttospeech
import os

client = texttospeech.TextToSpeechClient()

customer_voice = 'en-IN-Wavenet-B'
agent_voice = 'en-IN-Wavenet-A'

ssml = f"""<speak>
  <voice name="{customer_voice}">
    <prosody pitch="+1st" rate="medium">
      I got an overdraft facility on my account, and it’s a lifesaver!
      <break time="100ms"/>
      How do I increase the limit?
    </prosody>
  </voice>

  <voice name="{agent_voice}">
    <prosody pitch="0st" rate="medium">
      Glad it’s helping Sir!
      <break time="75ms"/>
      Can you confirm your account number for the request?
    </prosody>
  </voice>

  <voice name="{customer_voice}">
    <prosody pitch="+1st" rate="medium">
      It’s seven eight nine, one two three, four five six.
      <break time="100ms"/>
      Can you make it quick?
    </prosody>
  </voice>

  <voice name="{agent_voice}">
    <prosody pitch="0st" rate="medium">
      I’ll need your latest income proof to process the increase.
      <break time="75ms"/>
      Can you email it to us?
    </prosody>
  </voice>

  <voice name="{customer_voice}">
    <prosody pitch="+2st" rate="medium">
      Sure thing.
      <break time="75ms"/>
      This bank’s been great, by the way!
    </prosody>
  </voice>

  <voice name="{agent_voice}">
    <prosody pitch="0st" rate="medium">
      Thank you Sir!
      <break time="75ms"/>
      Once we receive the documents,
      <break time="50ms"/>
      I’ll expedite the limit increase.
    </prosody>
  </voice>
</speak>
"""

synthesis_input = texttospeech.SynthesisInput(ssml=ssml)

voice = texttospeech.VoiceSelectionParams(
    language_code="en-IN"
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

output_path = "Agent 04/Call 10/ssmlAudio.wav"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "wb") as out:
    out.write(response.audio_content)
    print(f"Saved audio to {output_path}")
