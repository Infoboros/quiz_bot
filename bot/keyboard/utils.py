from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_back_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Назад", callback_data=0),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)