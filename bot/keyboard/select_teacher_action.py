from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.handlers.teacher.states import CREATE_TEST, LOAD_QUESTIONS, START_CREATE_TEST


def get_select_teacher_action_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Загрузить вопросы", callback_data=LOAD_QUESTIONS),
        ],
        [
            InlineKeyboardButton("Создать тест", callback_data=START_CREATE_TEST),
        ],
        [
            InlineKeyboardButton("Назад", callback_data="cancel"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
