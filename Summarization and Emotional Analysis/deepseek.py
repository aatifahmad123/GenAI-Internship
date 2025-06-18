import requests
import json

transcript = '''

{
  "conversation": [
    {
      "speaker": "Customer",
      "text": "Hey, I’ve been charged twice on my credit card for the same transaction! This is ridiculous!"
    },
    {
      "speaker": "RM",
      "text": "I’m so sorry to hear that, Sir. Can you share the transaction details so I can check the chargeback status?"
    },
    {
      "speaker": "Customer",
      "text": "It’s from last week, uh, some restaurant bill… ₹5,200. I saw it twice on my statement!"
    },
    {
      "speaker": "RM",
      "text": "Got it. Let me pull up your account. It sounds like a duplicate charge; we can initiate a chargeback request right away."
    },
    {
      "speaker": "Customer",
      "text": "You better! I can’t keep paying for your mistakes!"
    },
    {
      "speaker": "RM",
      "text": "Absolutely, I understand your frustration. I’ve flagged this for a refund, and it should reflect in 5-7 business days."
    }
  ]
}

'''

url = "http://130.211.227.244:11500/api/generate"
headers = {
    "Content-Type": "application/json"
}

prompt = (
    f'''
    Analyze the following call transcript and respond in the following JSON format: 
    {{
    "summary": "<One professional sentence, no more than 10 words>",
    "intents": [<List of intents>],
    "intent 1": {{
        "products": ["<product1>", "<product2>"],
        "issues": ["<issue1>", "<issue2>"],
        "actions": ["<action1>", "<action2>"],
        "resolution_status": "<resolved/pending>"
    }},
    "emotional_analysis": {{
        "dominant_emotions (customer)": ["<emotion1>", "<emotion2>"],
        "conversation sentiment": "<Positive/Negative/Neutral>",
        "agent_professionalism": "<comment>",
        "customer_satisfaction": "<comment>"
    }},
    "additional_info": {{
        "callback_promise": "<Yes/No>",
        "callback_time": "<relative time or N/A>"
    }}
    }}
    
    Transcript: {json.dumps(transcript)}
    '''
)

data = {
    "model": "deepseek-r1:8b",
    "prompt": prompt,
}

# Set stream=True to handle streaming response
with requests.post(url, headers=headers, data=json.dumps(data), stream=True) as response:
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            try:
                parsed = json.loads(decoded_line)
                print(parsed['response'], end='', flush=True)
            except json.JSONDecodeError:
                print("Failed to parse JSON:", decoded_line)
