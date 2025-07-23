from fastapi import FastAPI
from pydantic import BaseModel

# Import LangGraph logic
from agents.agent_b_verifier import build_verifier_graph

app = FastAPI()

class VerificationRequest(BaseModel):
    subject: str
    sender: str
    body: str
    analysis: str

@app.post("/verify")
def verify_email(request: VerificationRequest):
    graph = build_verifier_graph()
    result = graph.invoke({
        "subject": request.subject,
        "sender": request.sender,
        "body": request.body,
        "analysis": request.analysis
    })
    return {"verification": result["verification"]}
