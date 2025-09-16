from fastapi import FastAPI
from pydantic import BaseModel
from src.helpbot.bot import HelpBot

app = FastAPI(title="HelpBot API")

bot = HelpBot()

class Message(BaseModel):
    user: str
    text: str

@app.get("/")
def root():
    return {"message": "HelpBot API is running!"}

@app.post("/chat")
def chat(msg: Message):
    response = bot.reply(msg.user, msg.text)
    return {"user": msg.user, "message": msg.text, "response": response}
