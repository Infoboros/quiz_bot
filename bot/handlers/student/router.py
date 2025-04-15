from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler, filters, MessageHandler

from bot.handlers.cancel import cancel
from bot.handlers.states import ROLE_SELECTION, STUDENT
from bot.handlers.student.actions import action_selection
from bot.handlers.student.execute_test import execute_test
from bot.handlers.student.result_test import result_test
from bot.handlers.student.select_test import select_test
from bot.handlers.student.states import EXECUTE_TEST, EXIT, RESULT_TEST, SELECT_TEST


def create_router():
    return ConversationHandler(
        entry_points=[CallbackQueryHandler(action_selection)],
        states={
            SELECT_TEST: [MessageHandler(filters.TEXT & ~filters.COMMAND, select_test)],
            EXECUTE_TEST: [CallbackQueryHandler(execute_test)],
            RESULT_TEST: [CallbackQueryHandler(result_test)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        map_to_parent={
            EXIT: ROLE_SELECTION
        }
    )