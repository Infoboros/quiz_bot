from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.mode.states import TEACHER
from bot.handlers.teacher.states import SHOW_TEST_RESULT
from bot.messages.mode import print_message_state_change as print_message_state_change_mode
from bot.messages.teacher import print_message_state_change as print_message_state_change_teacher
from bot.messages.utils import format_telegram_table
from core.controllers.permission import PermissionController
from core.controllers.statistics import StatisticsController


async def print_callback(context, chat_id):
    return await print_message_state_change_mode(SHOW_TEST_RESULT, TEACHER, context, chat_id)


async def show_test_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("show_test_result")
    try:
        test_id = int(update.message.text)
        controller = StatisticsController(PermissionController.get_user_by_telegram(update.effective_user).user)
        results = controller.get_test_statistic(test_id)

        await update.message.reply_text(
            format_telegram_table(
                [
                    "№",
                    "Респондент",
                    "% Верных ответов",
                    "Кол-во Верных ответов",
                    "Кол-во Вопросов",
                    "Кол-во Ответов",
                ],
                [
                    [
                        index,
                        result.respondent,
                        result.correct_percentage,
                        result.correct_answers,
                        result.all_questions,
                        result.answers,
                    ]
                    for index, result in enumerate(results, start=1)
                ]
            ),
            parse_mode='MarkdownV2'
        )
        return await print_message_state_change_mode(SHOW_TEST_RESULT, TEACHER, context, update.message.chat.id)

    except (StatisticsController.TestNotFound, ValueError):
        await update.message.reply_text("Теста с таким идентификатором не существует")
        return await print_message_state_change_teacher(SHOW_TEST_RESULT, SHOW_TEST_RESULT, context,
                                                        update.message.chat.id)
