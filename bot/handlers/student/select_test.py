from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.student.states import EXECUTE_TEST, SELECT_TEST
from bot.keyboard.execution_test import get_execution_test_keyboard
from core.controllers.execute_test import ExecuteTestController


async def select_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    test_id = int(update.message.text)

    try:
        test_controller = ExecuteTestController.create(test_id)
        context.user_data["test_controller"] = test_controller

        await update.message.reply_text(test_controller.test_name, reply_markup=get_execution_test_keyboard())
        return EXECUTE_TEST

    except ExecuteTestController.TestNotFound:
        await update.message.reply_text("Теста с таким идентификатором не существует")
        await update.message.reply_text("Введите идентификатор теста")

        return SELECT_TEST
