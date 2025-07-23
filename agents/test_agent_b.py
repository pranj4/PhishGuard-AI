from agents.agent_b_verifier import build_verifier_graph
from utils.email_input import sample_email

# Simulate Agent A result (normally this comes from Agent A)
fake_analysis = "This email looks like a phishing attempt due to suspicious domain."

# Build Verifier graph
graph = build_verifier_graph()

# Run through Verifier
result = graph.invoke({
    "subject": sample_email["subject"],
    "sender": sample_email["from"],
    "body": sample_email["body"],
    "analysis": fake_analysis
})

print("🔍 Verifier Result:")
print(result["verification"])
