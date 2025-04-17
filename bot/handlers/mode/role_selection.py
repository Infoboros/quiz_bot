from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.handlers.mode.states import ROLE_SELECTION, STUDENT, TEACHER
from bot.messages.mode import print_message_state_change


async def role_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('role selection')
    query = update.callback_query
    await query.answer()
    role = query.data
    context.user_data["role"] = role

    if role in [TEACHER, STUDENT]:
        return await print_message_state_change(ROLE_SELECTION, role, context, query.message.chat.id)
    else:
        await query.edit_message_text(text="Неизвестная роль. Попробуйте ещё раз.")
        return await print_message_state_change(ROLE_SELECTION, ROLE_SELECTION, context, query.message.chat.id)
