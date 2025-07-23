"""
Test script for the A2A pipeline.
- Sends email data to Agent A (Analyzer API)
- Agent A analyzes and forwards result to Agent B (Verifier API)
- Final combined result is returned
"""

import requests
from utils.email_input import sample_email

def test_pipeline():
    # Endpoint of Agent A service
    AGENT_A_URL = "http://localhost:8000/analyze"

    # Send the phishing email to Agent A
    response = requests.post(AGENT_A_URL, json=sample_email)

    # Check for errors
    if response.status_code != 200:
        print("❌ Error calling Agent A service:", response.text)
        return

    result = response.json()

    print("\n=== A2A Pipeline Test ===")
    print(f"Analyzer (Agent A) Output:\n{result['analysis']}\n")
    print(f"Verifier (Agent B) Output:\n{result['verification']}\n")


if __name__ == "__main__":
    test_pipeline()
    print("Running A2A Pipeline Test...")