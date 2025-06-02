from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

print("GEMINI_API_KEY found:", GEMINI_API_KEY is not None)

agents = 5
calls_per_agent = 10

def get_gemini_response(transcription, agent_id, call_id):
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
                    "keywords": "<The segment of transcription that indicates the intent: give a couple of the starting words and a couple of ending words>",
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
        Call ID: {call_id}
        Agent ID: {agent_id}
        ''')
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=1000,
            temperature=0.2
        )
    )
    return response.text.strip()

responseNumber = 1

for i in range(1, agents + 1):
    for j in range(1, calls_per_agent + 1):
        agentDir = f'../Calls Data Google Cloud/Agent {i:02d}'
        callDir = f'Call {j:02d}'
        transcriptionFile = f'{agentDir}/{callDir}/transcription.txt'
        responsesFile = f'Gemini Responses/response{responseNumber:02d}.json'
        
        with open(transcriptionFile, 'r') as file:
            transcription = file.read()
        
        agent_id = i
        call_id = 10 * (i-1) + j
        
        response = get_gemini_response(transcription, agent_id, call_id)
        
        if response.startswith("```json"):
            response = response.lstrip("```json").strip()
        if response.endswith("```"):
            response = response.rstrip("```").strip()

        
        with open(responsesFile, 'w') as file:
            file.write(response)
        
        
        print(f'Response saved to {responsesFile} for response number {responseNumber} with agent {agent_id} and call {call_id}')
        
        responseNumber += 1