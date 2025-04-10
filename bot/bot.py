from telegram import Update
from telegram.ext import Application

from bot.handlers.mode.mode import create_mode_handler
from settings import TOKEN


class Bot:
    def __init__(self):
        self.application = Application.builder().token(TOKEN).build()

    def register_handlers(self):
        self.application.add_handler(create_mode_handler())

    def start(self):
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)
