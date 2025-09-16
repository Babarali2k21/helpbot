from src.helpbot.bot import HelpBot

def test_faq_answer():
    bot = HelpBot()
    r = bot.reply("u", "what is helpbot?")
    assert "learning" in r.lower()  # updated check
