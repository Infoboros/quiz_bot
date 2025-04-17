from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler, filters, MessageHandler

from bot.handlers.callback_to_state import create_callback_to_state
from bot.handlers.cancel import cancel
from bot.handlers.mode.states import ROLE_SELECTION, STUDENT
from bot.handlers.student.actions import action_selection
from bot.handlers.student.execute_test import execute_test
from bot.handlers.student.result_test import result_test
from bot.handlers.student.select_test import print_callback, select_test
from bot.handlers.student.states import EXECUTE_TEST, RESULT_TEST, SELECT_TEST

def create_router():
    return ConversationHandler(
        entry_points=[CallbackQueryHandler(action_selection)],
        states={
            SELECT_TEST: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, select_test),
                create_callback_to_state(print_callback)
            ],
            EXECUTE_TEST: [CallbackQueryHandler(execute_test)],
            RESULT_TEST: [CallbackQueryHandler(result_test)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        map_to_parent={
            STUDENT: STUDENT,
            ROLE_SELECTION: ROLE_SELECTION,
        }
    )