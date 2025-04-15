from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.student.states import EXECUTE_TEST, SELECT_TEST
from bot.keyboard.execution_test import get_execution_test_keyboard
from core.controllers.execute_test import ExecuteTestController


async def select_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('select_test')
    telegram_id = update.effective_user.id
    try:
        test_id = int(update.message.text)
        test_controller = ExecuteTestController.create(telegram_id, test_id)
        context.user_data["test_controller"] = test_controller

        await update.message.reply_text(test_controller.test_name, reply_markup=get_execution_test_keyboard())
        print(f'select_test > {EXECUTE_TEST}')
        return EXECUTE_TEST

    except (ExecuteTestController.TestNotFound, ValueError):
        await update.message.reply_text("Теста с таким идентификатором не существует")
        await update.message.reply_text("Введите идентификатор теста")

        print(f'select_test > {SELECT_TEST}')
        return SELECT_TEST
