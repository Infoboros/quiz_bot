from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_select_role_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Я - Преподаватель!", callback_data="teacher"),
            InlineKeyboardButton("Я - Студент!", callback_data="student"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)