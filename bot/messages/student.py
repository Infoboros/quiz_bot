from telegram.ext import ContextTypes

from bot.handlers.student.states import SELECT_TEST
from bot.keyboard.utils import get_back_keyboard


async def print_message_state_change(
        current_state: str,
        next_state: str,
        context: ContextTypes.DEFAULT_TYPE,
        chat_id: int
) -> str:
    if next_state == SELECT_TEST:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Введите идентификатор теста.",
            reply_markup=get_back_keyboard()
        )

    return next_state
