from src.helpbot.bot import HelpBot

def test_greeting():
    bot = HelpBot()
    r = bot.reply("u", "hello")
    assert "assist you today" in r  # updated check

def test_smalltalk():
    bot = HelpBot()
    r = bot.reply("u", "how are you?")
    assert "i'm just a bot" in r.lower()  # updated check

