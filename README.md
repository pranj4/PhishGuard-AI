# PhishGuard AI - AI-Powered Phishing Detection System

---

## Overview

**PhishGuard AI** is a modular AI-powered system for detecting phishing emails using an **Agent-to-Agent (A2A)** communication architecture. The system is built with:

- **LangGraph** for agent logic (Analyzer & Verifier)
- **FastAPI** for hosting agents as microservices
- **Ollama (LLaMA/DeepSeek)** as the local LLM backend
- **Streamlit** for an interactive and styled web interface

The system allows users to analyze emails in two ways:

1. **Structured Input** – Enter subject, sender, and email body
2. **Raw Email Input** – Paste entire email content for analysis

Agent A analyzes the email and forwards results to Agent B, which verifies and confirms phishing status. Results are displayed with color-coded risk levels in the UI.

---

## Features

- **Agent-to-Agent (A2A) Architecture** for modular communication
- **Two Input Modes:** Structured fields & raw email paste
- **Styled Streamlit UI** with color-coded results (Safe/Warning/Danger)
- **Local LLM Inference** using Ollama (free)
- **Scalable Microservices** (FastAPI agents can be deployed separately)

---

## Architecture

```
User (Streamlit UI)
   ↓
Agent A (Analyzer - FastAPI + LangGraph)
   ↓ (A2A over HTTP)
Agent B (Verifier - FastAPI + LangGraph)
```

- **Agent A**: Detects phishing indicators using LLM prompts
- **Agent B**: Performs secondary verification (keywords, domains)

---

## Project Structure

```
phishguard-ai/
│
├── agents/
│   ├── agent_a_langgraph.py    # Analyzer logic
│   └── agent_b_verifier.py     # Verifier logic
│
├── services/
│   ├── agent_a_service.py      # FastAPI wrapper for Agent A
│   └── agent_b_service.py      # FastAPI wrapper for Agent B
│
├── utils/
│   ├── email_input_example.py  # Sample phishing emails
│   └── link_checker.py         # URL & keyword check utilities
│
├── prompts.py                  # Prompt templates for LLMs
├── pipeline.py                 # Monolithic pipeline (optional)
├── app.py                      # Streamlit UI
├── test_a2a_pipeline.py        # Test script for A2A pipeline
├── requirements.txt
└── README.md
```

---

## Tech Stack

- **Backend (Agents):** Python, FastAPI, LangGraph
- **LLM Backend:** Ollama (LLaMA 3 / DeepSeek)
- **Frontend (UI):** Streamlit
- **Communication:** A2A (HTTP between agents)

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone <repo-url>
cd phishguard-ai
```

### 2. Install Dependencies (Using `uv`)

```bash
uv pip install -r requirements.txt
```

### 3. Start Agent Services

Run both agents via batch script:

```bash
start_agents.bat
```

OR manually:

```bash
python -m uvicorn services.agent_b_service:app --port 8001 --reload
python -m uvicorn services.agent_a_service:app --port 8000 --reload
```

### 4. Run Streamlit UI

```bash
streamlit run app.py
```

Open browser: [http://localhost:8501](http://localhost:8501)

---

## Usage

1. Enter **Subject, Sender, Body** OR paste full email content.
2. Click **Analyze Email**.
3. View:
   - Agent A (Analyzer) response
   - Agent B (Verifier) final decision
4. Results are **color-coded** (Safe, Suspicious, Phishing).

---

## Screenshots

*(Add screenshots of UI here)*

---

## Deployment

### Option 1: Streamlit Cloud (UI only)

- Host Agent APIs separately (Render/Heroku/VPS)
- Point Streamlit app to public API URLs

### Option 2: Merge All-In-One (For Simplicity)

- Run LangGraph logic directly inside Streamlit app (no A2A)

*(Detailed deployment instructions below)*

---

## Roadmap

-

---

## Contributing

Pull requests and feature suggestions are welcome. Open an issue for discussion before major changes.

---

## License

MIT License

---

## Credits

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Ollama](https://ollama.ai)
- [Streamlit](https://streamlit.io)
- [FastAPI](https://fastapi.tiangolo.com)

