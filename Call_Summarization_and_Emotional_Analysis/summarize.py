from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
import json

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

print(GEMINI_API_KEY)

call_id = int(input("Enter the call ID: "))

if call_id < 10:
    call_id = f"0{call_id}"

call_file = f"../Calls_Google_Cloud_TTS/call{call_id}/call{call_id}.json"

transcript = ""
with open(call_file, "r") as f:
    transcript = json.load(f)

print(f"Transcript: {transcript}")

client = genai.Client(api_key=GEMINI_API_KEY)

prompt = (
    "Summarize the following conversation in one professional sentence, "
    "no more than 10 words:"
    f"\n{transcript}"
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        max_output_tokens=25,
        temperature=0.2
    )
)

print("Call summary:", response.text.strip())


