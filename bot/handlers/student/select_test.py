from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.mode.states import STUDENT
from bot.handlers.student.states import EXECUTE_TEST, SELECT_TEST
from bot.keyboard.execution_test import get_execution_test_keyboard
from bot.messages.mode import print_message_state_change as print_message_state_change_mode
from bot.messages.student import print_message_state_change
from core.controllers.execute_test import ExecuteTestController


async def print_callback(context, chat_id):
    return await print_message_state_change_mode(SELECT_TEST, STUDENT, context, chat_id)


async def select_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('select_test')
    try:
        test_id = int(update.message.text)
        test_controller = ExecuteTestController.create(update.effective_user, test_id)
        context.user_data["test_controller"] = test_controller

        await update.message.reply_text(test_controller.test_name, reply_markup=get_execution_test_keyboard())
        return EXECUTE_TEST

    except (ExecuteTestController.TestNotFound, ValueError):
        await update.message.reply_text("Теста с таким идентификатором не существует")
        return await print_message_state_change(SELECT_TEST, SELECT_TEST, context, update.message.chat.id)
