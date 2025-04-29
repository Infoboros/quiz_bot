from telegram.ext import ContextTypes

from bot.handlers.teacher.states import CREATE_TEST, LOAD_QUESTIONS, SHOW_TEST_RESULT, START_CREATE_TEST
from bot.keyboard.create_test import get_start_create_test_keyboard
from bot.keyboard.utils import get_back_keyboard


async def print_message_state_change(
        current_state: str,
        next_state: str,
        context: ContextTypes.DEFAULT_TYPE,
        chat_id: int
) -> str:
    if next_state == LOAD_QUESTIONS:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Загрузите файл txt формата\n"
                 "<b>Тег</b>; <b>Вопрос</b>; <b>Ответ 1</b>; <b>Ответ n</b>; <b>Правильный ответ 1</b>; <b>Правльный ответ m</b>\n"
                 "Правльный ответ должен быть указан и в списке ответов",
            reply_markup=get_back_keyboard(),
            parse_mode="HTML"
        )

    if next_state == START_CREATE_TEST:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Введите название теста"
        )

    if next_state == CREATE_TEST:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Загрузка вопросов...",
            reply_markup=get_start_create_test_keyboard()
        )

    if next_state == SHOW_TEST_RESULT:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Введите идентификатор теста",
            reply_markup=get_back_keyboard()
        )

    return next_state
