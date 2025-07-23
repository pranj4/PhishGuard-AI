from langgraph.graph import StateGraph
from dataclasses import dataclass
import requests
from prompts import EMAIL_ANALYZER_PROMPT


# Step 1: Define state (what data moves through the graph)
@dataclass
class EmailState:
    subject: str
    sender: str
    body: str
    analysis: str = ""  # will store model's response


# Step 2: Define function (Node) to call Ollama LLM
def analyze_email(state: EmailState) -> EmailState:
    # Prepare prompt with email details
    formatted_prompt = EMAIL_ANALYZER_PROMPT.format(
        subject=state.subject,
        sender=state.sender,
        body=state.body
    )

    # Send request to local Ollama model
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": formatted_prompt,
            "stream": False
        }
    )

    # Extract response
    result_text = response.json()["response"]

    # Update state with analysis
    state.analysis = result_text
    return state


# Step 3: Build LangGraph workflow
def build_analyzer_graph():
    graph = StateGraph(EmailState)

    # Add node and mark as entry point
    graph.add_node("analyze", analyze_email)
    graph.set_entry_point("analyze")

    # Compile graph
    return graph.compile()
