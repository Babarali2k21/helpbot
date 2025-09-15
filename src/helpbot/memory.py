from collections import defaultdict, deque
from typing import Deque, Dict, List

class Memory:
    def __init__(self, maxlen: int = 20):
        self._store: Dict[str, Deque[dict]] = defaultdict(lambda: deque(maxlen=maxlen))

    def remember(self, user_id: str, role: str, text: str):
        self._store[user_id].append({"role": role, "text": text})

    def get_recent(self, user_id: str, n: int = 5) -> List[dict]:
        return list(self._store[user_id])[-n:]

    def clear_user(self, user_id: str):
        self._store[user_id].clear()
