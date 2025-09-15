def smalltalk(message: str) -> str:
    """Handles smalltalk responses"""
    msg = message.lower()
    if "how are you" in msg:
        return "I'm just a bot, but I'm doing great! How about you?"
    if "thank you" in msg or "thanks" in msg:
        return "You're welcome!"
    if "bye" in msg:
        return "Goodbye! Have a great day!"
    return ""