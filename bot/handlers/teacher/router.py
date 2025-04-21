from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler, filters, MessageHandler

from bot.handlers.callback_to_state import create_callback_to_state
from bot.handlers.cancel import cancel
from bot.handlers.mode.states import ROLE_SELECTION, TEACHER
from bot.handlers.teacher.actions import action_selection
from bot.handlers.teacher.create_test import create_test, start_create_test
from bot.handlers.teacher.load_questions import load_questions, print_callback
from bot.handlers.teacher.states import CREATE_TEST, LOAD_QUESTIONS, START_CREATE_TEST


def create_router():
    return ConversationHandler(
        entry_points=[CallbackQueryHandler(action_selection)],
        states={
            LOAD_QUESTIONS: [
                MessageHandler(filters.TEXT | filters.Document.ALL, load_questions),
                create_callback_to_state(print_callback)
            ],
            START_CREATE_TEST: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, start_create_test),
            ],
            CREATE_TEST: [
                CallbackQueryHandler(create_test),
            ]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        map_to_parent={
            ROLE_SELECTION: ROLE_SELECTION,
            TEACHER: TEACHER
        }
    )
