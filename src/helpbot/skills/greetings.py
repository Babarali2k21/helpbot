def greet(message: str) -> str:
    """Return a greeting if the message contains hello/hi/hey."""
    msg = message.lower()
    if any(word in msg for word in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"
    return ""
