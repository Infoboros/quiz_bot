from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.mode.states import ENTRY_POINT, ROLE_SELECTION
from bot.messages.mode import print_message_state_change


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await print_message_state_change(ENTRY_POINT, ROLE_SELECTION, context, update.message.chat.id)
