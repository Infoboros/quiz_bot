from telegram import Update
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler, filters, \
    MessageHandler

from bot.handlers.cancel import cancel
from bot.handlers.mode.role_selection import role_selection
from bot.handlers.mode.start import start
from bot.handlers.mode.states import ROLE_SELECTION, STUDENT, TEACHER
from bot.handlers.student.router import create_router as create_router_student
from bot.handlers.teacher.router import create_router as create_router_teacher


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
            TEACHER: [create_router_teacher()],
            STUDENT: [create_router_student()],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )