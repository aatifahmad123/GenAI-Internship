from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
import json

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

# call_id = int(input("Enter the call ID: "))

# if call_id < 10:
#     call_id = f"0{call_id}"

# call_file = f"../Calls_Google_Cloud_TTS/call{call_id}/call{call_id}.json"

# transcript = ""
# with open(call_file, "r") as f:
#     transcript = json.load(f)

# print(f"Transcript: {transcript}")

transcript = '''Hey, I've been charged twice on my credit card for the same transaction. This is ridiculous. I am so sorry to hear that sir. Can you share the transaction details so I can check the charge back status. It's from last week some restaurant bill 5200. I saw it twice on my statement your account. It sounds like a duplicate charge. We can initiate the charge back request right away. I can't keep paying for your mistakes. Absolutely. I understand your frustration. I like this for a refund and it should reflect in 5 to 7 business days.'''

client = genai.Client(api_key=GEMINI_API_KEY)

prompt = (
    f'''
    Analyze the following call transcript and respond in the following JSON format: 
    {{
    "summary": "<One professional sentence, no more than 10 words>",
    "intents": "[<List of intents>]",
    "intent 1": {{
        "products": "<List of products related to intent 1>",
        "issues": "<List of issues related to intent 1>",
        "actions": "<List of actions related to intent 1>",
        "resolution_status": "<Status of resolution, e.g., 'resolved', 'pending'>"
    }},
    **extend as needed for more intents**
    "emotional_analysis": {{
        "dominant_emotions (customer)": "[<list main emotions expressed by the customer>]",
        "conversation sentiment": "<Overall sentiment of the conversation: Positive/Negative/Neutral>",
        "agent_professionalism": "<Brief comment>",
        "customer_satisfaction": "<Brief comment>"
    }},
    "additional_info": {{
        "callback_promise": "<Yes/No>",
        "callback_time": "<Date (relative for eg. same day or next day and Time if applicable, otherwise 'N/A'>"
    }}
    }}
    Transcript: {json.dumps(transcript)}
    '''
)


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        max_output_tokens=350,
        temperature=0.2
    )
)

print("Call summary:", response.text.strip())
