from fastapi.testclient import TestClient
from api import app   # ✅ api.py is at project root

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "HelpBot API is running!"}

def test_chat_greeting():
    res = client.post("/chat", json={"user": "cli", "text": "hello"})
    assert res.status_code == 200
    data = res.json()
    assert "response" in data
    assert "hello" in data["response"].lower() or "assist" in data["response"].lower()
