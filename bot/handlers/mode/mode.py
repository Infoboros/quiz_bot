from telegram import Update
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler, filters, \
    MessageHandler

from bot.handlers.cancel import cancel
from bot.handlers.mode.role_selection import role_selection
from bot.handlers.mode.start import start
from bot.handlers.mode.states import ROLE_SELECTION, STUDENT, TEACHER
from bot.handlers.student.router import create_router


async def teacher_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # TODO
    print('teacher_callback')
    return ConversationHandler.END

async def student_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('student_callback')
    return ConversationHandler.END

def create_mode_handler():
    return ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ROLE_SELECTION: [CallbackQueryHandler(role_selection)],
            TEACHER: [MessageHandler(filters.TEXT & ~filters.COMMAND, teacher_callback)],
            STUDENT: [create_router()],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )