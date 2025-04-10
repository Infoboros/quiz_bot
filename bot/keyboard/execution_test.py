from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_execution_test_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton("Начать", callback_data=0)]])