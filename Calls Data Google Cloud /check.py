import requests
import google.auth
from google.auth.transport.requests import Request

# Get credentials and generate access token
access_token = 'ya29.a0AW4XtxiCr-kdPp3bO19lo4y7q63KUe_lM9qpaDY10TaiW_Tk7iOvJWwwTTBojVb2m0hGhEJ-oBuCzsTRO406BrRryo09srlbzLZSy_VhXG-9wJ3HfiALB9_RwlAhgTrxgNKfsSmZmJmjAwsUtJvTVxa2DR0bhD0ZwILsR9IWICdfHtNssaFO0H6GonXy_tSavBbKlvW1yX_n0mQtSIx7pJE0GPsvsRVIIL00-GQk7c2r6FUZNjcSIDgSwNF1SCB17qwb6XWRJEp0MEzAvE2YI3qADPwfI-JnOxrFkwGfDv1QxjLLPiCfMhS5OozVNPwjHRI4drUxtdg885-shohCy9jUE0Uj4BpkY8zlf3PYHAMJ-qYb6ANoMl2VebwpFeORwRlKJ-qqDzArWI6C55GOZSd_y8x89-jJcD3-LwaCgYKARYSARUSFQHGX2Mikf6yapZYWHLAWdtc0ta-OQ0429'

project_id = 'icici-internship'

# Prepare the request
url = "https://texttospeech.googleapis.com/v1/text:synthesize"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}",
    "X-Goog-User-Project": project_id
}

data = {
    "input": {
        "markup": "hello"
    },
    "voice": {
        "languageCode": "en-IN",
        "name": "en-IN-Chirp3-HD-Achernar",
        "voiceClone": {}
    },
    "audioConfig": {
        "audioEncoding": "LINEAR16"
    }
}

# Make the request
response = requests.post(url, headers=headers, json=data)

print(response)

# Handle the response
if response.ok:
    audio_content = response.json().get("audioContent")
    with open("output.wav", "wb") as out:
        out.write(base64.b64decode(audio_content))
    print("Audio content written to output.wav")
else:
    print("Error:", response.text)
