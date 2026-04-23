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

##  WhatsApp Deployment using Webhooks

This AutoStream agent can be deployed on WhatsApp using a webhook-based architecture integrated with the WhatsApp Business API.

###  Architecture Overview

The system follows a request-response flow where incoming user messages from WhatsApp are processed by the agent and responses are sent back in real time.

Flow:
User → WhatsApp → Webhook Server → LangGraph Agent → Response → WhatsApp → User

---

###  Step 1: WhatsApp Business API Setup

To enable communication, we use the WhatsApp Business API provided by Meta or third-party services like Twilio.  
This allows sending and receiving messages programmatically.

---

###  Step 2: Webhook Server

A backend server (Flask / FastAPI) exposes a webhook endpoint:

POST /webhook

Whenever a user sends a message on WhatsApp, the API forwards the message payload to this endpoint.

---

###  Step 3: Message Processing with Agent

The webhook extracts the user message and passes it to the LangGraph agent:

response = app.invoke(state)

The agent performs:
- Intent detection using LLM
- Knowledge retrieval using RAG
- Lead qualification and data collection

State is maintained per user session to ensure context-aware conversations.

---

###  Step 4: Sending Response Back

The generated response from the agent is sent back to the user via the WhatsApp API, completing the interaction loop.

---

###  Step 5: Lead Capture & Storage

When a high-intent user is detected, the agent collects:
- Name
- Email
- Platform

This data can be stored in:
- Databases (MongoDB, PostgreSQL)
- CRM systems
- External APIs for further processing

---

###  Step 6: Deployment

The webhook server and agent can be deployed on cloud platforms such as AWS, GCP, or Azure.  
Lightweight platforms like Render or Railway can also be used for quick deployment.

Flow:
User → WhatsApp → Webhook → Agent → Response → WhatsApp → User

---

##  Summary

This integration enables the AutoStream agent to operate as a real-time conversational assistant on WhatsApp, capable of:
- Understanding user intent
- Providing accurate responses using RAG
- Converting high-intent users into leads through automated workflows

This design ensures scalability, real-world usability, and seamless user experience.

---

##  How to Run

```bash
pip install -r requirements.txt
python app.py
