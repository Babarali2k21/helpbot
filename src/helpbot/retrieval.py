import math, re
from pathlib import Path
from typing import List, Tuple

def _tokenize(s: str) -> List[str]:
    return re.findall(r"[a-z0-9']+", s.lower())

def _tf(text: str) -> dict:
    toks = _tokenize(text)
    d = {}
    for t in toks:
        d[t] = d.get(t, 0) + 1
    n = max(1, len(toks))
    return {k: v / n for k, v in d.items()}

def cosine(a: dict, b: dict) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0) * b.get(k, 0) for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)

class FAQRetriever:
    def __init__(self, kb_path: str):
        self.kb_path = Path(kb_path)
        self.qas: List[Tuple[str, str]] = self._load()

    def _load(self) -> List[Tuple[str, str]]:
        text = self.kb_path.read_text(encoding="utf-8")
        blocks = re.split(r"\n##+\s*", text)
        qas = []
        for b in blocks:
            q = re.search(r"^Q:\s*(.+)", b, re.M)
            a = re.search(r"^A:\s*([\s\S]+)", b, re.M)
            if q and a:
                qas.append((q.group(1).strip(), a.group(1).strip()))
        return qas

    def query(self, question: str, k: int = 1):
        qvec = _tf(question)
        scored = []
        for q, a in self.qas:
            sim = cosine(qvec, _tf(q))
            scored.append((q, a, sim))
        scored.sort(key=lambda x: x[2], reverse=True)
        return scored[:k]
