from openai import OpenAI
from dotenv import load_dotenv
import os

# loading api keys from env
load_dotenv()

YOUR_API_KEY = os.getenv("PERPLEXITY_API_KEY")

messages = [
    {
        "role": "system",
        "content": (
            "You are an artificial intelligence assistant and you need to "
            "engage in a helpful, detailed, polite conversation with a user."
        ),
    },
    {   
        "role": "user",
        "content": (
            "What is CIBIL score? "
        ),
    },
]

client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

# chat completion endpoint
response = client.chat.completions.create(
    model="sonar-pro",
    messages=messages,
)
print(response)