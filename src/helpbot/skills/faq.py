from ..memory import Memory
from ..retrieval import FAQRetriever

def faq_answer(retriever: FAQRetriever, threshold: float = 0.15):
    def _inner(message: str, memory: Memory):
        top = retriever.query(message, k=1)
        if not top:
            return None
        q, a, score = top[0]
        return a if score >= threshold else None
    return _inner
