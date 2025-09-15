import os
from dotenv import load_dotenv

# Load values from .env file
load_dotenv()

BOT_NAME = os.getenv("HELPBOT_NAME", "HelpBot")
KB_PATH = os.getenv("HELPBOT_KB", "data/faq.md")
