from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.handlers.student.states import SELECT_TEST


def get_select_student_action_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Выбрать тест", callback_data=SELECT_TEST),
            InlineKeyboardButton("Назад", callback_data="cancel"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)