from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.handlers.student.states import EXECUTE_TEST, RESULT_TEST
from bot.keyboard.execution_test import get_answers_test_keyboard, get_result_test_keyboard
from core.controllers.execute_test import ExecuteTestController


async def execute_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("execute_test")
    query = update.callback_query
    await query.answer()
    answer_id = int(query.data)

    test_controller: ExecuteTestController = context.user_data["test_controller"]
    if answer_id:
        test_controller.answer(answer_id)

    question = test_controller.get_question()

    if question:
        answers = [
            (answer.answer, answer.id)
            for answer in test_controller.get_answers()
        ]
        await query.edit_message_text(
            question.question,
            reply_markup=get_answers_test_keyboard(answers)
        )
        return EXECUTE_TEST

    await query.edit_message_text(
        text="Вы прошли тест!",
        reply_markup=get_result_test_keyboard()
    )
    return RESULT_TEST
