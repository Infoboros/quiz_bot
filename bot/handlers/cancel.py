from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /cancel для отмены диалога."""
    await update.message.reply_text("Отмена.")
    return ConversationHandler.END