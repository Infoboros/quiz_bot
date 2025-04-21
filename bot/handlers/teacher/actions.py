from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.mode.states import ROLE_SELECTION
from bot.handlers.teacher.states import CREATE_TEST, ENTRY_POINT, LOAD_QUESTIONS, START_CREATE_TEST
from bot.messages.mode import print_message_state_change as print_message_state_change_mode
from bot.messages.teacher import print_message_state_change as print_message_state_change_teacher


async def action_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('teacher action_selection')
    query = update.callback_query
    await query.answer()
    action = query.data

    if action in [LOAD_QUESTIONS, START_CREATE_TEST]:
        print(f'teacher action_selection > {action}')
        return await print_message_state_change_teacher(ENTRY_POINT, action, context, query.message.chat.id)
    else:
        print('teacher action_selection > ROLE_SELECTION')
        return await print_message_state_change_mode(ENTRY_POINT, ROLE_SELECTION, context, query.message.chat.id)