
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from rag import get_answer
from tools import mock_lead_capture


# LLM SETUP

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)


# STATE

def init_state():
    return {
        "messages": [],
        "intent": "",
        "name": "",
        "email": "",
        "platform": ""
    }


# INTENT DETECTION (FIXED + SAFE)

def detect_intent(state):
    text = state["messages"][-1].lower()

    #  HARD RULE FIRST 
    if any(word in text for word in [
        "subscribe", "buy", "pro plan", "start", "sign up",
        "instagram", "youtube", "want"
    ]):
        state["intent"] = "high_intent"
        return state


    prompt = f"""
Classify intent into ONE:
- greeting
- pricing
- high_intent
- general

User: {text}

Return only label.
"""

    response = llm.invoke(prompt).content.strip().lower()

    valid = ["greeting", "pricing", "high_intent", "general"]
    state["intent"] = response if response in valid else "general"

    return state


# GREETING NODE

def greet(state):
    print("\nAgent: Hello! I can help you with pricing, features, or sign-up.")
    return state


# RAG NODE

def rag_node(state):
    query = state["messages"][-1]
    print("\nAgent:", get_answer(query))
    return state


# LEAD NODE

def lead_node(state):

    print("\nAgent: Great! I can help you get started ")

    if not state["name"]:
        state["name"] = input("Agent: What's your name? ")

    if not state["email"]:
        state["email"] = input("Agent: Your email? ")

    if not state["platform"]:
        state["platform"] = input("Agent: Platform (YouTube/Instagram)? ")

    mock_lead_capture(
        state["name"],
        state["email"],
        state["platform"]
    )

    return state


# ROUTER

def route(state):
    return state["intent"]


# GRAPH

graph = StateGraph(dict)

graph.add_node("intent", detect_intent)
graph.add_node("greet", greet)
graph.add_node("rag", rag_node)
graph.add_node("lead", lead_node)

graph.set_entry_point("intent")

graph.add_conditional_edges(
    "intent",
    route,
    {
        "greeting": "greet",
        "pricing": "rag",
        "general": "rag",
        "high_intent": "lead"
    }
)

graph.add_edge("greet", END)
graph.add_edge("rag", END)
graph.add_edge("lead", END)

app = graph.compile()


# CHAT LOOP

state = init_state()

print("AutoStream LLM + LangGraph Agent ")

while True:
    user = input("\nUser: ")
    state["messages"].append(user)

    state = app.invoke(state)
