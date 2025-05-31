from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")


filename = '../Calls Data Google Cloud/Agent 01/Call 01/transcription.txt'

with open(f'{filename}', 'r') as file:
    transcription = file.read()

print(f'Transcription: {transcription}')

client = genai.Client(api_key=GEMINI_API_KEY)

prompt = (
    f'''
    Analyze the following call transcript and respond in the following JSON format.
    There can be multiple intents in a single call, and each intent should be captured separately in the JSON array.
    The transcription is an alternating conversation between a customer and an agent starting with the customer.
    
    {{
        "call id": "<Unique identifier for the call>",
        "agent id": "<Unique identifier for the agent>",
        "summary": "<One professional sentence, no more than 10 words>",
        "intents": [
            {{
                "intent": "<Intent recognized from the conversation>",
                "confidence": "<Confidence level of intent recognition, as a percentage (0-100)>",
                "keywords": "<The segment of transcription that indicates the intent: give the starting and ending word of the segment with their index, assume word indexing starts from 0>",)>",
                "products": "<List of products related to intent>",
                "issues": "<List of issues related to intent>",
                "actions of agent": "<List of actions taken by agent for the intent>",
                "resolution_status": "<Status of resolution, e.g., 'resolved', 'pending'>",
                "dominant emotions (customer)": "[<list main emotions expressed by the customer>]",
                "conversation sentiment": "<sentiment of the conversation: Positive/Negative/Neutral for that intent>",
                "agent professionalism": "<Brief comment on agent's professionalism>",
                "agent performance": "<Score from 1 to 10>",
                "customer satisfaction": "<Score from 1 to 10>",
                "callback promise": "<Yes/No>",
                "callback time": "<Date (relative for eg. same day or next day and Time if applicable, otherwise 'N/A'>"
            }}
        ]
    }}

    Transcription: {transcription}
    Call ID: 1
    Agent ID: 1
    '''
)


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        max_output_tokens=1000,
        temperature=0.2
    )
)

print("Call summary:", response.text.strip())
