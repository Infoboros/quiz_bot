from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from db.quiz import Answer


def get_execution_test_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton("Начать", callback_data=0)]])

def get_result_test_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton("Просмотреть результат", callback_data=0)]])


def get_answers_test_keyboard(answers: [(str, Answer)]) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=code, callback_data=answer.id)
        for code, answer in answers
    ]
    keyboard = [
        buttons[i:i + 2] for i in range(0, len(buttons), 2)
    ]
    return InlineKeyboardMarkup(keyboard)