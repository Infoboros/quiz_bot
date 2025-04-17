import mimetypes

from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.mode.states import TEACHER
from bot.handlers.teacher.states import LOAD_QUESTIONS
from bot.messages.teacher import print_message_state_change as print_message_state_change_teacher
from bot.messages.mode import print_message_state_change as print_message_state_change_mode

async def print_callback(context, chat_id):
    return await print_message_state_change_mode(LOAD_QUESTIONS, TEACHER, context, chat_id)


async def load_questions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("load_questions")
    extension = mimetypes.guess_extension(update.message.document.mime_type) if update.message.document else None
    if extension == '.xlsx':
        document = await update.message.document.get_file()
        # TODO импорт
        await update.message.reply_text("Формат верный но функция еще не релизована")
        return await print_message_state_change_teacher(LOAD_QUESTIONS, LOAD_QUESTIONS, context, update.message.chat.id)

    await update.message.reply_text("Неверный формат файла")
    return await print_message_state_change_teacher(LOAD_QUESTIONS, LOAD_QUESTIONS, context, update.message.chat.id)
