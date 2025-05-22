import requests
from dotenv import load_dotenv
import os

# loading api keys from env
load_dotenv()

url = 'https://api.jsonbin.io/v3/b/68284a178561e97a5015a4e9/latest'
headers = {
  'X-Master-Key': os.getenv("JSON_BIN_MASTER_API_KEY")
}

call_id = 2
index = f'call_{call_id}'

req = requests.get(url, json=None, headers=headers)
if req.status_code == 200:
    print(req.json()["record"][index])
    print("Success")
else:
    print(f"Error: {req.status_code}")
