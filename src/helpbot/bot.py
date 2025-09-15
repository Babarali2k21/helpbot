from .memory import Memory
from .skills.greetings import greet
from .skills.smalltalk import smalltalk
from .retrieval import FAQRetriever

class HelpBot:
    def __init__(self):
        self.memory = Memory()
        self.retriever = FAQRetriever("data/faq.md")
        self.skills = [greet, smalltalk]

    def reply(self, user: str, message: str) -> str:
        # check skills
        for skill in self.skills:
            response = skill(message)
            if response:
                return response
        return "I'm not sure about that, but I'm learning!"
