from telegram.ext import ContextTypes

from bot.handlers.mode.states import ROLE_SELECTION, STUDENT, TEACHER
from bot.keyboard.select_role import get_select_role_keyboard
from bot.keyboard.select_student_action import get_select_student_action_keyboard
from bot.keyboard.select_teacher_action import get_select_teacher_action_keyboard


async def print_message_state_change(
        current_state: str,
        next_state: str,
        context: ContextTypes.DEFAULT_TYPE,
        chat_id: int
) -> str:
    if next_state == ROLE_SELECTION:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Выберите вашу роль",
            reply_markup=get_select_role_keyboard()
        )

    if next_state == STUDENT:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Вы выбрали роль Студент.\n",
            reply_markup=get_select_student_action_keyboard()
        )

    if next_state == TEACHER:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Вы выбрали роль Преподаватель.\n",
            reply_markup=get_select_teacher_action_keyboard()
        )

    return next_state