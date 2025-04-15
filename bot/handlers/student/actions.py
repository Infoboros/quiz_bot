from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.handlers.student.states import ENTRY_POINT, EXIT, SELECT_TEST
from bot.keyboard.select_role import get_select_role_keyboard
from bot.messages.student import print_message_state_change


async def action_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    action = query.data
    context.user_data["action"] = action
    if action == SELECT_TEST:
        return await print_message_state_change(ENTRY_POINT, SELECT_TEST, context, query.message.chat.id)
    else:
        await query.edit_message_text("Выберите вашу роль", reply_markup=get_select_role_keyboard())
        return EXIT