from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.mode.states import ROLE_SELECTION, TEACHER
from bot.handlers.teacher.states import ENTRY_POINT, LIST_TEST, LOAD_QUESTIONS, SHOW_TEST_RESULT, START_CREATE_TEST
from bot.messages.mode import print_message_state_change as print_message_state_change_mode
from bot.messages.teacher import print_message_state_change as print_message_state_change_teacher
from bot.messages.utils import format_telegram_table
from core.controllers.permission import PermissionController
from core.controllers.statistics import StatisticsController


async def action_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('teacher action_selection')
    query = update.callback_query
    await query.answer()
    action = query.data

    if action == LIST_TEST:
        tests = StatisticsController(
            PermissionController.get_user_by_telegram(update.effective_user).user
        ).get_tests()
        await query.edit_message_text(
            format_telegram_table(
                ["№", "Название", "Идентификатор"],
                [
                    [index, test.name, test.id]
                    for index, test in enumerate(tests, start=1)
                ]
            ),
            parse_mode='MarkdownV2'
        )
        return await print_message_state_change_mode(ENTRY_POINT, TEACHER, context, query.message.chat.id)

    if action in [LOAD_QUESTIONS, START_CREATE_TEST, SHOW_TEST_RESULT]:
        print(f'teacher action_selection > {action}')
        return await print_message_state_change_teacher(ENTRY_POINT, action, context, query.message.chat.id)
    else:
        print('teacher action_selection > ROLE_SELECTION')
        return await print_message_state_change_mode(ENTRY_POINT, ROLE_SELECTION, context, query.message.chat.id)
