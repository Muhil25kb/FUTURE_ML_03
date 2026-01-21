from fastapi import FastAPI
from intent import detect_intent
from utils import extract_order_id, is_greeting, is_small_talk
from retriever import get_dataset_reply

app = FastAPI()

SESSION = {"intent": None, "order_id": None}

PRODUCT_WORDS = ["product", "details", "price", "specification", "phone", "mobile", "laptop"]

@app.post("/chat")
async def chat(data: dict):
    text = data.get("message", "").lower().strip()

    # 1️⃣ Greeting
    if is_greeting(text):
        SESSION["intent"] = None
        SESSION["order_id"] = None
        return {"reply": "Hello! How can I help you today?"}

    # 2️⃣ Small talk (thanks, bye, who are you, etc.)
    small = is_small_talk(text)
    if small:
        return {"reply": small}

    # 3️⃣ Extract order ID
    order_id = extract_order_id(text)
    if order_id:
        SESSION["order_id"] = order_id

    # 4️⃣ Detect intent
    intent = detect_intent(text)
    if intent:
        SESSION["intent"] = intent

    # 5️⃣ Refund
    if SESSION["intent"] == "refund":
        if SESSION["order_id"]:
            reply = f"Refund request registered for order {SESSION['order_id']}."
            SESSION["intent"] = None
            SESSION["order_id"] = None
            return {"reply": reply}
        return {"reply": "Please provide your order ID for the refund."}

    # 6️⃣ Track order
    if SESSION["intent"] == "track":
        if SESSION["order_id"]:
            reply = f"Your order {SESSION['order_id']} is currently in transit."
            SESSION["intent"] = None
            SESSION["order_id"] = None
            return {"reply": reply}
        return {"reply": "Please provide your order ID to track your order."}

    # 7️⃣ Product query
    if any(word in text for word in PRODUCT_WORDS):
        return {
            "reply": (
                "Sure! Please tell me the product name or model you want details about."
            )
        }

    # 8️⃣ Dataset fallback (SAFE)
    reply = get_dataset_reply(text)
    if reply:
        return {"reply": reply}

    # 9️⃣ Final fallback
    return {
        "reply": "I can help with orders, refunds, tracking, and product information 😊"
    }
