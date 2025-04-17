from telegram.ext import ContextTypes

from bot.handlers.teacher.states import LOAD_QUESTIONS
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
            text="Загрузите файл xlsx",
            reply_markup=get_back_keyboard()
        )

    return next_state
