#  AutoStream – Social-to-Lead Agentic Workflow

##  Overview
AutoStream is an AI-powered conversational agent built for a fictional SaaS product that provides automated video editing tools for content creators. The system converts user conversations into qualified business leads using a combination of LLMs, RAG, and agentic workflow orchestration.

---

##  Architecture

The system is built using **LangGraph** to manage multi-step conversational workflows. The agent follows a state-based design where each user input updates a shared state object containing message history, intent, and lead details.

### Workflow:
1. User sends a message
2. Intent is classified using an LLM (Groq - LLaMA 3)
3. Based on intent:
   - Greeting → Friendly response
   - Pricing → RAG system fetches data from local JSON
   - High-intent → Lead capture flow starts
4. If high-intent is detected, the system collects:
   - Name
   - Email
   - Platform (YouTube/Instagram)
5. After collecting all details, a mock API function is triggered to simulate lead capture.

### Why LangGraph?
LangGraph is used because it allows structured agent workflows with state persistence, making it ideal for multi-turn conversational systems with branching logic.

### State Management
The system maintains a state dictionary across 5–6 turns, storing:
- messages
- intent
- name
- email
- platform

---

##  RAG System
The knowledge base is stored in a local JSON file containing:
- Pricing (Basic & Pro plans)
- Company policies

The RAG module retrieves relevant responses based on user queries.

---

##  Tech Stack
- Python 3.9+
- LangGraph
- LangChain
- Groq LLM (LLaMA 3)
- JSON (for knowledge base)

---

##  WhatsApp Integration (Webhook Concept)

The agent can be integrated with WhatsApp using the WhatsApp Cloud API:

1. WhatsApp message → Webhook (FastAPI/Flask)
2. Webhook sends message to LangGraph agent
3. Agent processes request (RAG / intent / lead capture)
4. Response is sent back via WhatsApp API

Flow:
User → WhatsApp → Webhook → Agent → WhatsApp API → User

---

##  How to Run

```bash
pip install -r requirements.txt
python app.py
