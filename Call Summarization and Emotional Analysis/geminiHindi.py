from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

print("GEMINI_API_KEY found:", GEMINI_API_KEY is not None)

agents = 1
calls_per_agent = 1

def get_gemini_response(transcription,timestamps,metadata, agent_id, call_id):
    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = (
        f'''
        Analyze the following call transcript and respond in the following JSON format.
        There can be multiple intents in a single call, and each intent should be captured separately in the JSON array.
        The transcription is an alternating conversation between a customer and an agent starting with the customer.
        Remember the timestamps here is empty, so you need to predict the timestamps based on the transcription and metadata.
        You may use timestamps or the nature of conversation in transcript to identify the interruptions.
        There can be multiple issues for same intent so keep the issues as a list of dictionaries.
        The JSON format is as follows:
        
        {{
            "call id": "<Unique identifier for the call>",
            "agent id": "<Unique identifier for the agent>",
            "call duration": "<Duration of the call in seconds, you can get this from metadata file>",
            "summary": "<One professional sentence, no more than 10 words>",
            "intents": [
                {{
                    "intent": "<Intent recognized from the conversation>",
                    "confidence": "<Confidence level of intent recognition, as a percentage (0-100)>",
                    "keywords": "<The part of transcription that identifies the intent, it has to be specific not a large part of transcription, atmost 10-15 words stretch, give a couple of beginning and ending words separated by '...' (mandatorily)>",
                    "intent timestamp": "<Beginning and Ending timestamp of the above keywords that identify the intent, give a relaxed timeframe of 5 seconds (mandatorily), you may use the timstamps data provided>",
                    "products": "<List of products related to intent>",
                    "issues": [
                        {{
                            "issue": "<Brief description of the issue identified by the agent if any>",
                            "reason(s)": "<Brief description of the reason for the issue identified by the agent if any>",
                            "issue type": "<Type of issue out of 
                            1. 'Technical': software bugs, hardware malfunctions, connectivity, or system errors,
                            2. 'Billing': invoices, payments, refunds, overcharges, or subscription,
                            3. 'Service': long wait times, unhelpful support, or lack of follow-up,
                            4. 'General Inquiry': questions not related to specific issues>",
                        }}
                    ],
                    "actions of agent": "<Brief description of the actions taken by the agent to handle the intent>",
                    "resolution status": "<Status of resolution, One out of: 'Resolved', 'Unresolved', Pending with Callback'>",
                    "Process Request": "<Brief description of the process request if any, otherwise 'N/A'. Process request happens when the agent has to do something in the backend or with a third party to resolve the issue>",
                    "resolution": "<Brief description of the resolution irrespective of resolution status>",
                    "resolution timestamp": "<Beginning and Ending timestamp of transcription that determines the resolution, again it has to be very specific atmost 10-15 words stretch, give a relaxed timeframe of 5 seconds (mandatorily), you may use the timstamps data provided>",
                    "dominant emotions (customer)": "[<list main emotions expressed by the customer>]",
                    "conversation sentiment": "<sentiment of the conversation: Positive/Negative/Neutral for that intent>",
                    "customer satisfaction": "<Satisfaction of the customer with the agent's handling of the intent, as a percentage (0-100)>"
                }}
            ],
            "basic greeting and closing": "<Yes/No, whether the agent greeted and closed the call properly>",
            "fatal behaviour": "<Yes/No, whether the agent exhibited any fatal behaviour during the call>",
            "agent professionalism (out of 10)": "<Score from 1 to 10>",
            "agent performance (out of 10)": "<Score from 1 to 10>",
            "customer satisfaction (out of 10)": "<Score from 1 to 10>",
            "interruptions by customer": "<Number of times the customer interrupted the agent>",
            "interruptions by agent": "<Number of times the agent interrupted the customer>",
            "callback promise": "<Yes/No>",
            "callback time": "<Date (relative for eg. same day or next day and Time if applicable, otherwise 'N/A'>
        }}
        
        Call ID: {call_id}
        Agent ID: {agent_id}
        
        Transcription: {transcription}
        
        Timestamps: {timestamps}
        
        Metadata: {metadata}
        
        Please ensure the JSON is well-formed and valid.
        ''')
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=1750,
            temperature=0.2
        )
    )
    return response.text.strip()

responseNumber = 1

for i in range(1, agents + 1):
    for j in range(1, calls_per_agent + 1):
        agentDir = f'../Google Cloud Hindi/Agent {i:02d}'
        callDir = f'Call {j:02d}'
        transcriptionFile = f'{agentDir}/{callDir}/transcription.txt'
        # timestampsFile = f'{agentDir}/{callDir}/timestamps.json'
        metadataFile = f'{agentDir}/{callDir}/metadata.txt'
        responsesFile = f'Gemini Responses Hindi/response{responseNumber:02d}.json'
        
        with open(transcriptionFile, 'r') as file:
            transcription = file.read()
            
            timestamps = {}
        # with open(timestampsFile, 'r') as file:
        #     timestamps = file.read()
            
        with open(metadataFile, 'r') as file:
            metadata = file.read()
        
        agent_id = i
        call_id = 10 * (i-1) + j
        
        response = get_gemini_response(transcription,timestamps,metadata,agent_id,call_id)
        
        if response.startswith("```json"):
            response = response.lstrip("```json").strip()
        if response.endswith("```"):
            response = response.rstrip("```").strip()

        
        with open(responsesFile, 'w') as file:
            file.write(response)
        
        
        print(f'Response saved to {responsesFile} for response number {responseNumber} with agent {agent_id} and call {call_id}')
        
        responseNumber += 1