def is_small_talk(text: str):
    phrases = {
        "thanks": "You're welcome! 😊",
        "thank you": "You're welcome! 😊",
        "ok": "👍",
        "okay": "👍",
        "ok thanks": "Happy to help!",
        "bye": "Goodbye 👋 Have a great day!",
        "goodbye": "Goodbye 👋",
        "who are you": "I’m your customer support assistant.",
        "how are you": "I'm doing well, thanks for asking!",
        "how was your day": "It’s been great helping customers like you 😊"
    }

    for key in phrases:
        if key in text:
            return phrases[key]

    return None
import re

# -------------------------------
# Greeting detection
# -------------------------------
def is_greeting(text: str) -> bool:
    greetings = [
        "hi", "hello", "hey", "good morning",
        "good afternoon", "good evening"
    ]
    return any(g in text for g in greetings)


# -------------------------------
# Order ID extractor
# -------------------------------
def extract_order_id(text: str):
    """
    Extracts numeric order ID from text
    Example:
    'my order id is 2345' -> 2345
    """
    match = re.search(r"\b\d{3,}\b", text)
    if match:
        return match.group()
    return None


# -------------------------------
# Small talk handler
# -------------------------------
def is_small_talk(text: str):
    phrases = {
        "thanks": "You're welcome! 😊",
        "thank you": "You're welcome! 😊",
        "ok": "👍",
        "okay": "👍",
        "okay thanks": "Happy to help!",
        "bye": "Goodbye 👋 Have a great day!",
        "goodbye": "Goodbye 👋",
        "who are you": "I’m your customer support assistant.",
        "how are you": "I'm doing well, thanks for asking!",
        "how was your day": "It’s been great helping customers 😊"
    }

    for key, value in phrases.items():
        if key in text:
            return value

    return None
