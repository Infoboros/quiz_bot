from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.handlers.teacher.states import LOAD_QUESTIONS


def get_select_teacher_action_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Загрузить вопросы", callback_data=LOAD_QUESTIONS),
        ],
        [
            InlineKeyboardButton("Назад", callback_data="cancel"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
