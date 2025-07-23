from fastapi import FastAPI
from pydantic import BaseModel
import requests

# Import LangGraph logic
from agents.agent_a_langgraph import build_analyzer_graph
from prompts import EMAIL_ANALYZER_PROMPT

app = FastAPI()

class EmailRequest(BaseModel):
    subject: str
    sender: str
    body: str

@app.post("/analyze")
def analyze_email(request: EmailRequest):
    # Build and run Agent A graph
    graph = build_analyzer_graph()
    result = graph.invoke({
        "subject": request.subject,
        "sender": request.sender,
        "body": request.body
    })

    # Forward Agent A result to Agent B (A2A call)
    verification_response = requests.post(
        "http://localhost:8001/verify",
        json={
            "subject": request.subject,
            "sender": request.sender,
            "body": request.body,
            "analysis": result["analysis"]
        }
    )

    return {
        "analysis": result["analysis"],
        "verification": verification_response.json()["verification"]
    }
