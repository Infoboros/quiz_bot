from bot.bot import Bot

if __name__ == '__main__':
    bot = Bot()
    bot.register_handlers()
    bot.start()