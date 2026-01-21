def detect_intent(text):
    if "refund" in text:
        return "refund"
    if "track" in text or "order status" in text:
        return "track"
    return None
