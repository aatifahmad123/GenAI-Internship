from google.cloud import texttospeech
import os

client = texttospeech.TextToSpeechClient()

customer_voice = 'en-IN-Wavenet-B'
agent_voice = 'en-IN-Wavenet-A'

ssml = f"""<speak>
  <voice name="{customer_voice}">
    <prosody rate="medium" volume="medium">
      Hello? I applied for a personal loan last month, 
      <break time="200ms"/>
      but nobody’s told me what’s happening with it.
    </prosody>
  </voice>

  <voice name="{agent_voice}">
    <prosody rate="medium" pitch="-1st">
      Good afternoon, Sir. 
      <break time="200ms"/>
      I’d be happy to check the status. 
      <break time="150ms"/>
      Could you provide your application ID or full name?
    </prosody>
  </voice>

  <voice name="{customer_voice}">
    <prosody rate="medium">
      It’s Priyansh Sharma. 
      <break time="150ms"/>
      I don’t have any ID number… nobody gave me one!
    </prosody>
  </voice>

  <voice name="{agent_voice}">
    <prosody rate="medium" pitch="-1st">
      No worries, I can search by name. 
      <break time="150ms"/>
      One moment—
    </prosody>
  </voice>

  <voice name="{customer_voice}">
    <prosody rate="medium" volume="medium">
      And please, don’t put me on hold for ages! 
      <break time="200ms"/>
      I’ve been waiting too long already.
    </prosody>
  </voice>

  <voice name="{agent_voice}">
    <prosody rate="medium" pitch="-1st">
      Of course, Sir. 
      <break time="150ms"/>
      I’ll be as quick as possible. 
      <break time="200ms"/>
      It looks like your application is under review 
      due to a pending <emphasis>CIBIL score update</emphasis>—
    </prosody>
  </voice>

  <voice name="{customer_voice}">
    <prosody rate="medium" volume="medium">
      <emphasis>CIBIL?</emphasis> What’s that? 
      <break time="200ms"/>
      Nobody told me about this! 
      <break time="150ms"/>
      Why is it taking so long?
    </prosody>
  </voice>

  <voice name="{agent_voice}">
    <prosody rate="medium" pitch="-1st">
      I apologize for the confusion. 
      <break time="200ms"/>
      CIBIL is your <emphasis>credit score</emphasis>, 
      and we’re waiting for the latest report—
    </prosody>
  </voice>

  <voice name="{customer_voice}">
    <prosody rate="medium" volume="medium">
      But I need the loan <emphasis>urgently!</emphasis> 
      <break time="150ms"/>
      Can’t you speed it up?
    </prosody>
  </voice>

  <voice name="{agent_voice}">
    <prosody rate="medium" pitch="-1st">
      Absolutely, I understand the urgency. 
      <break time="200ms"/>
      I’ll escalate this to expedite the process 
      and keep you updated.
    </prosody>
  </voice>

  <voice name="{customer_voice}">
    <prosody rate="medium" volume="medium">
      Please do. 
      <break time="150ms"/>
      I really hope I hear back soon this time.
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

output_path = "Agent 01/Call 02/ssmlAudio.wav"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "wb") as out:
    out.write(response.audio_content)
    print(f"Saved audio to {output_path}")
