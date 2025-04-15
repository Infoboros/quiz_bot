from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.student.states import RESULT_TEST, SELECT_TEST
from bot.messages.student import print_message_state_change
from core.controllers.execute_test import ExecuteTestController


async def result_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('result_test')
    query = update.callback_query
    await query.answer()

    test_controller: ExecuteTestController = context.user_data["test_controller"]
    result = test_controller.get_result_statistic()

    await query.edit_message_text(
        f"Поздравлем, вы прошли тест: <b>{result.test_name}</b>\n"
        f"Всего тест состоял из <b>{result.all_questions}</b> вопросов\n"
        f"Вы ответили на <b>{result.answers}</b> из них <b>{result.correct_answers}</b> правильных\n"
        f"Итого вы дали правильный ответ в <b>{round(result.correct_percentage, 2)}%</b> вопросов",
        parse_mode="HTML"
    )

    return await print_message_state_change(RESULT_TEST, SELECT_TEST, context, query.message.chat.id)
