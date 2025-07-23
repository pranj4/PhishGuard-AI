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

<img width="1407" height="1146" alt="ai_agents" src="https://github.com/user-attachments/assets/0aedcb9c-6936-4d1e-b86a-03556a806f12" />


```

- **Agent A**: Detects phishing indicators using LLM prompts
- **Agent B**: Performs secondary verification (keywords, domains)

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

<img width="1908" height="868" alt="image" src="https://github.com/user-attachments/assets/cd9f3b27-4ba1-4f1b-aa5f-6247bfc7c0d2" />

<img width="1888" height="520" alt="image" src="https://github.com/user-attachments/assets/ca32d417-5aac-4cfc-8b6a-3301892c6637" />



---

## Deployment



- Run LangGraph logic directly inside Streamlit app (no A2A)



## Contributing

Pull requests and feature suggestions are welcome. Open an issue for discussion before major changes.

---



## Credits

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Ollama](https://ollama.ai)
- [Streamlit](https://streamlit.io)
- [FastAPI](https://fastapi.tiangolo.com)

