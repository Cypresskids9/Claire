import requests
import aicamp_day1

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "what color is grass? ",
})

result = aicamp_day1.make_text(output)
print(result)