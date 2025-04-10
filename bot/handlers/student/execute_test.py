from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from core.controllers.execute_test import ExecuteTestController


async def execute_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    test_controller: ExecuteTestController = context.user_data["test_controller"]
    print(11111)
    print(test_controller.get_question())

    return ConversationHandler.END