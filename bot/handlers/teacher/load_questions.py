import io
import mimetypes

import telegram
from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.mode.states import TEACHER
from bot.handlers.teacher.states import LOAD_QUESTIONS
from bot.messages.mode import print_message_state_change as print_message_state_change_mode
from bot.messages.teacher import print_message_state_change as print_message_state_change_teacher
from core.controllers.import_questions import ImportQuestionController
from core.controllers.permission import PermissionController


async def print_callback(context, chat_id):
    return await print_message_state_change_mode(LOAD_QUESTIONS, TEACHER, context, chat_id)


async def load_questions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("load_questions")
    extension = mimetypes.guess_extension(update.message.document.mime_type) if update.message.document else None
    if extension == '.xlsx':
        document = await update.message.document.get_file()
        file = io.BytesIO()
        await document.download_to_memory(file)
        questions = ImportQuestionController(
            PermissionController.get_user_by_telegram_id(update.effective_user.id).user,
            file
        ).import_questions()
        await update.message.reply_text(
            f"Импорт успешно завершен, было импортировано <b>{len(questions)}</b> вопросов",
            parse_mode="HTML",
        )
        return await print_message_state_change_teacher(LOAD_QUESTIONS, LOAD_QUESTIONS, context, update.message.chat.id)

    await update.message.reply_text("Неверный формат файла")
    return await print_message_state_change_teacher(LOAD_QUESTIONS, LOAD_QUESTIONS, context, update.message.chat.id)
