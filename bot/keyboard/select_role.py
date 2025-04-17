from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.handlers.mode.states import STUDENT, TEACHER


def get_select_role_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Я - Преподаватель!", callback_data=TEACHER),
            InlineKeyboardButton("Я - Студент!", callback_data=STUDENT),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)