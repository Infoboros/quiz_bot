from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.mode.states import ROLE_SELECTION
from bot.handlers.student.states import ENTRY_POINT, SELECT_TEST
from bot.messages.mode import print_message_state_change as print_message_state_change_mode
from bot.messages.student import print_message_state_change as print_message_state_change_student


async def action_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('action_selection')
    query = update.callback_query
    await query.answer()
    action = query.data
    context.user_data["action"] = action
    if action == SELECT_TEST:
        print('action_selection > SELECT_TEST')
        return await print_message_state_change_student(ENTRY_POINT, SELECT_TEST, context, query.message.chat.id)
    else:
        print('action_selection > ROLE_SELECTION')
        return await print_message_state_change_mode(ENTRY_POINT, ROLE_SELECTION, context, query.message.chat.id)