
import requests
from utils.email_input import sample_email

email_text = f"""
Subject: {sample_email['subject']}
From: {sample_email['from']}
Body: {sample_email['body']}
"""

# Send the request to the local model running via Ollama
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": f"Is this email a phishing attempt? Be honest.\n\n{email_text}",
        "stream": False
    }
)

print("🔍 Result from the model:\n")
print(response.json()["response"])