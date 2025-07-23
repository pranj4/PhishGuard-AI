from agents.agent_a_langgraph import build_analyzer_graph
from utils.email_input import sample_email

# Build graph
graph = build_analyzer_graph()

# Run email through graph
result = graph.invoke({
    "subject": sample_email["subject"],
    "sender": sample_email["from"],
    "body": sample_email["body"]
})

print("🔍 AI Analysis:")
print(result["analysis"])
