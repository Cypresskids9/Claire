import requests 
import aicamp_day1 

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": "whats 2 cubed ",
})

result = aicamp_day1.make_text(output)
print(result)