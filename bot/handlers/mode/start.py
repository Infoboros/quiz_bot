from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.states import ROLE_SELECTION
from bot.keyboard.select_role import get_select_role_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Выберите вашу роль", reply_markup=get_select_role_keyboard())
    return ROLE_SELECTION

