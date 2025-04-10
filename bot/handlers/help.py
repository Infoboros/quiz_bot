from telegram import Update
from telegram.ext import ContextTypes


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # TODO
    await update.message.reply_text("Тут будет красивенький ЧаВо")
