from telegram.ext import ContextTypes

from bot.handlers.student.states import SELECT_TEST


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
        )

    return next_state