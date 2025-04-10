from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.handlers.student.states import EXIT, SELECT_TEST
from bot.keyboard.select_role import get_select_role_keyboard


async def action_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('action selection')
    query = update.callback_query
    await query.answer()
    action = query.data
    context.user_data["action"] = action
    if action == SELECT_TEST:
        print('SELECT_TEST')
        await query.edit_message_text(
            text="Введите идентификатор теста."
        )
        return SELECT_TEST
    else:
        await query.edit_message_text("Выберите вашу роль", reply_markup=get_select_role_keyboard())
        return EXIT