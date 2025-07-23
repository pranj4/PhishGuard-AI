from langgraph.graph import StateGraph
from dataclasses import dataclass
from utils.linkchecker import contains_suspicious_keywords, extract_urls, is_suspicious_domain


# Step 1: Define state
@dataclass
class VerifierState:
    subject: str
    sender: str
    body: str
    analysis: str     # Result from Agent A
    verification: str = ""  # Final verdict after checking links/keywords


# Step 2: Define verification function
def verify_email(state: VerifierState) -> VerifierState:
    urls = extract_urls(state.body)
    has_keywords = contains_suspicious_keywords(state.body)

    # Basic logic:
    # If Agent A says "phishing" OR keywords/urls are suspicious → Confirm phishing
    if "phishing" in state.analysis.lower() or has_keywords:
        # If URL present and suspicious → Strong confirmation
        for url in urls:
            if is_suspicious_domain(url):
                state.verification = "Phishing confirmed: Suspicious domain detected."
                return state

        state.verification = "Likely phishing: Suspicious content or keywords found."
    else:
        state.verification = "Safe: No phishing indicators found."

    return state


# Step 3: Build LangGraph flow for Verifier
def build_verifier_graph():
    graph = StateGraph(VerifierState)

    graph.add_node("verify", verify_email)
    graph.set_entry_point("verify")

    return graph.compile()
