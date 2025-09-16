from src.helpbot.bot import HelpBot

def main():
    bot = HelpBot()
    user = "cli"
    print("HelpBot CLI — type 'quit' to exit.")
    while True:
        msg = input("> ").strip()
        if msg.lower() in {"quit", "exit"}:
            print("Bye!")
            break
        print(bot.reply(user, msg))

if __name__ == "__main__":
    main()
