import json

with open("knowledge_base.json", "r") as f:
    KB = json.load(f)

def get_answer(query):
    q = query.lower()

    # pricing intent (IMPORTANT FIX)
    if "price" in q or "pricing" in q or "plan" in q:
        return (
            f"Basic Plan: {KB['pricing']['basic']}\n"
            f"Pro Plan: {KB['pricing']['pro']}"
        )

    if "refund" in q:
        return KB["policies"]["refund"]

    if "support" in q:
        return KB["policies"]["support"]

    return "Sorry, I don't have that info."